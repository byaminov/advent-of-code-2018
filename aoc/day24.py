import re
from typing import List

from dataclasses import dataclass

from aoc import search_minimum_matching


@dataclass(eq=False)
class Group:
    belongs_to: str
    n_units: int
    unit_hp: int
    attack_damage: int
    attack_type: str
    initiative: int
    weaknesses: List[str]
    immunities: List[str]

    def effective_power(self):
        return self.n_units * self.attack_damage

    def receive_damage(self, amount):
        n_killed = amount // self.unit_hp
        self.n_units = max(0, self.n_units - n_killed)

    def alive(self):
        return self.n_units > 0

    def would_get_damage(self, another) -> int:
        if another.attack_type in self.immunities:
            return 0
        if another.attack_type in self.weaknesses:
            return another.effective_power() * 2
        return another.effective_power()


class DrawException(Exception):
    pass


def solve1(text: str, boost: int = 0):
    immune_system, infection = parse_input(text, boost)
    round_number = 1
    while True:
        if round_number % 1000 == 0:
            print('at round', round_number)
        if not play_round(immune_system, infection):
            break
        round_number += 1
    return sum(map(lambda g: g.n_units, get_alive_groups(immune_system, infection)))


def play_round(immune_system: List[Group], infection: List[Group]) -> bool:
    # target selection
    all_groups = get_alive_groups(immune_system, infection)

    all_groups.sort(key=lambda g: (g.effective_power(), g.initiative), reverse=True)

    will_attack = dict()

    for group in all_groups:
        enemy_groups = [g for g in all_groups
                        if g.belongs_to != group.belongs_to and g not in will_attack.values()]
        enemy_groups.sort(key=lambda g: (
            g.would_get_damage(group), g.effective_power(), g.initiative
        ), reverse=True)
        if not enemy_groups or \
                enemy_groups[0].would_get_damage(group) == 0:
            # no go for this group
            pass
        else:
            target = enemy_groups[0]
            will_attack[group] = target

    # attacking
    if not will_attack:
        # nobody can attack anybody, it's a draw
        raise DrawException()

    all_groups.sort(key=lambda g: g.initiative, reverse=True)
    for group in all_groups:
        if not group.alive():
            continue
        if group not in will_attack:
            continue
        target = will_attack[group]
        damage_amount = target.would_get_damage(group)
        target.receive_damage(damage_amount)

    # results
    n_alive_immune = len([g for g in immune_system if g.alive()])
    n_alive_infect = len([g for g in infection if g.alive()])
    return n_alive_immune > 0 and n_alive_infect > 0


def get_alive_groups(immune_system, infection):
    all_groups = []
    for g in immune_system:
        if g.alive():
            all_groups.append(g)
    for g in infection:
        if g.alive():
            all_groups.append(g)
    return all_groups


def parse_input(text, boost: int = 0):
    immune_system: List[Group] = []
    infection: List[Group] = []
    index = 1
    lines = text.split('\n')
    for line in lines[1:]:
        if not line:
            index += 1
            continue
        if line.startswith('Infection:'):
            index += 1
            break
        group = parse_group(line, 'immune_system', boost)
        immune_system.append(group)
        index += 1
    for line in lines[index:]:
        if not line:
            continue
        group = parse_group(line, 'infection')
        infection.append(group)
    return immune_system, infection


def parse_group(line: str, group_type: str, boost: int = 0) -> Group:
    # 17 units each with 5390 hit points (weak to radiation, bludgeoning)
    #   with an attack that does 4507 fire damage at initiative 2
    # 4485 units each with 2961 hit points (immune to radiation; weak to fire, cold)
    #   with an attack that does 12 slashing damage at initiative 4
    group_pattern = re.compile(r'(\d+) units each with (\d+) hit points (\([^)]+\) )?'
                               r'with an attack that does (\d+) (\w+) damage at initiative (\d+)')
    m = group_pattern.match(line)
    if not m:
        raise ValueError('Failed to parse:\n' + line)
    n_units, hp, traits, attack, attack_type, initiative = m.groups()
    weaknesses = []
    immunities = []
    if traits:
        traits = traits.replace('(', '').replace(')', '').strip()
        for part in traits.split('; '):
            if part.startswith('weak to'):
                weaknesses = part.replace('weak to ', '').split(', ')
            elif part.startswith('immune to'):
                immunities = part.replace('immune to ', '').split(', ')
            else:
                assert False
    return Group(
        belongs_to=group_type,
        n_units=int(n_units),
        unit_hp=int(hp),
        attack_damage=int(attack) + boost,
        attack_type=attack_type,
        initiative=int(initiative),
        weaknesses=weaknesses,
        immunities=immunities
    )


def solve2(text: str):
    def can_win(boost):
        print('playing with boost:', boost)
        immune_system, infection = parse_input(text, boost)
        round_number = 1
        while True:
            if round_number % 1000 == 0:
                print(f'with boost {boost} at round {round_number}')
            try:
                still_playing = play_round(immune_system, infection)
                if not still_playing:
                    first_alive = get_alive_groups(immune_system, infection)[0]
                    return first_alive.belongs_to == 'immune_system'
            except DrawException:
                print('draw at boost', boost)
                return False
            round_number += 1

    minimum_boost = search_minimum_matching(can_win, 1)
    return solve1(text, minimum_boost)
