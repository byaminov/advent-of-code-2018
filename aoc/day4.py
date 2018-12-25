import re
from collections import defaultdict

import numpy as np


def fill_in_minutes(text: str):
    lines = text.split('\n')
    lines.sort()

    guards = defaultdict(lambda: np.full([60], 0))
    current_minutes = None
    time_went_asleep = None

    line_pattern = re.compile(r'\[\d+-\d+-\d+ \d\d:(\d\d)\] (.*)')
    guard_pattern = re.compile(r'Guard #(\d+) .*')

    for line in lines:
        # [1518-11-01 00:00] Guard #10 begins shift
        # [1518-11-01 00:30] falls asleep
        # [1518-11-01 00:55] wakes up
        m = line_pattern.match(line)
        time = int(m.group(1))
        action = m.group(2)

        if action.startswith('Guard #'):
            guard_id = int(guard_pattern.match(action).group(1))
            current_minutes = guards[guard_id]
        elif action == 'falls asleep':
            time_went_asleep = time
        else:
            for t in range(time_went_asleep, time):
                current_minutes[t] += 1

    return guards


def solve1(text: str):
    guards = fill_in_minutes(text)

    most_minutes_asleep = 0
    most_sleepy_guard_id = None
    minute_most_asleep = None
    for guard_id in guards:
        minutes = guards[guard_id]
        if minutes.sum() > most_minutes_asleep:
            most_minutes_asleep = minutes.sum()
            most_sleepy_guard_id = guard_id
            minute_most_asleep = np.argmax(minutes)

    return most_sleepy_guard_id * minute_most_asleep


def solve2(text: str):
    guards = fill_in_minutes(text)

    max_sleep_time = 0
    max_sleep_minute = None
    most_sleepy_guard_id = None

    for guard_id in guards:
        minutes = guards[guard_id]
        if minutes.max() > max_sleep_time:
            max_sleep_time = minutes.max()
            most_sleepy_guard_id = guard_id
            max_sleep_minute = np.argmax(guards[guard_id])

    return most_sleepy_guard_id * max_sleep_minute
