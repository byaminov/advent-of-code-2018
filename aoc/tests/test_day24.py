import unittest

from aoc.day24 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        print('Testing')
        self.assertEqual(5216, solve1('''Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4'''))
        print('Solving 1')
        self.assertEqual(16006, solve1(text))

    def test_solve2(self):
        print('Testing')
        self.assertEqual(51, solve1('''Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4''',
                                    boost=1570))
        print('Solving 2')
        self.assertEqual(6221, solve2(text))


text = '''Immune System:
3020 units each with 3290 hit points with an attack that does 10 radiation damage at initiative 16
528 units each with 6169 hit points with an attack that does 113 fire damage at initiative 9
4017 units each with 2793 hit points (weak to radiation) with an attack that does 6 slashing damage at initiative 1
2915 units each with 7735 hit points with an attack that does 26 cold damage at initiative 4
3194 units each with 1773 hit points (immune to radiation; weak to fire) with an attack that does 5 cold damage at initiative 13
1098 units each with 4711 hit points with an attack that does 36 radiation damage at initiative 7
2530 units each with 3347 hit points (immune to slashing) with an attack that does 12 bludgeoning damage at initiative 5
216 units each with 7514 hit points (immune to cold, slashing; weak to bludgeoning) with an attack that does 335 slashing damage at initiative 15
8513 units each with 9917 hit points (immune to slashing; weak to cold) with an attack that does 10 fire damage at initiative 14
1616 units each with 3771 hit points with an attack that does 19 bludgeoning damage at initiative 10

Infection:
1906 units each with 37289 hit points (immune to radiation; weak to fire) with an attack that does 28 radiation damage at initiative 3
6486 units each with 32981 hit points with an attack that does 9 bludgeoning damage at initiative 18
489 units each with 28313 hit points (immune to radiation, bludgeoning) with an attack that does 110 bludgeoning damage at initiative 6
1573 units each with 44967 hit points (weak to bludgeoning, cold) with an attack that does 42 slashing damage at initiative 12
2814 units each with 11032 hit points (immune to fire, slashing; weak to radiation) with an attack that does 7 slashing damage at initiative 2
1588 units each with 18229 hit points (weak to slashing; immune to radiation, cold) with an attack that does 20 radiation damage at initiative 19
608 units each with 39576 hit points (immune to bludgeoning) with an attack that does 116 slashing damage at initiative 20
675 units each with 48183 hit points (immune to cold, slashing, bludgeoning) with an attack that does 138 slashing damage at initiative 8
685 units each with 11702 hit points with an attack that does 32 fire damage at initiative 17
1949 units each with 32177 hit points with an attack that does 32 radiation damage at initiative 11'''
