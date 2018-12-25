from collections import deque
from itertools import islice
from typing import Any, Iterator, List


class CycleDetector:
    def __init__(self,
                 return_value_for_iteration: int = None,
                 max_cycle_size: int = 11000,
                 min_cycle_size: int = 3):
        self.return_value_for_iteration = return_value_for_iteration
        self.max_cycle_size = max_cycle_size
        self.min_cycle_size = min_cycle_size
        self.queue = deque(maxlen=self.max_cycle_size * 2 + 1)
        self.internal_iteration = 0
        # output values
        self.cycle_size_: int = None
        self.iteration_of_first_cycle_start_: int = None
        self.value_on_requested_iteration_: int = None
        self.cycle_: List[Any] = None

    def next_and_check(self, value: Any, iteration: int = None) -> bool:
        self.internal_iteration += 1
        if iteration is None:
            iteration = self.internal_iteration
        if iteration == self.return_value_for_iteration:
            print(f'no cycle detected but reached requested iteration {iteration}')
            self.value_on_requested_iteration_ = value
            return value

        if value in self.queue:
            v_index_reversed = next(
                (i for i, v in enumerate(reversed(self.queue))
                 if v == value and i >= self.min_cycle_size - 1),
                None)
            cycle_candidate_length = v_index_reversed + 1 if v_index_reversed is not None else None
            if cycle_candidate_length and cycle_candidate_length >= self.min_cycle_size:
                first_cycle_start = len(self.queue) - 2 * cycle_candidate_length
                second_cycle_start = len(self.queue) - cycle_candidate_length
                if first_cycle_start >= 0 and self.queue[first_cycle_start] == value:
                    first_cycle = list(islice(self.queue, first_cycle_start, second_cycle_start))
                    second_cycle = list(islice(self.queue, second_cycle_start, len(self.queue)))
                    if first_cycle == second_cycle:
                        # cycle detected
                        print(f'detected cycle of length {cycle_candidate_length} at iteration {iteration}')
                        self.cycle_size_ = cycle_candidate_length
                        self.cycle_ = first_cycle
                        self.iteration_of_first_cycle_start_ = iteration - 2 * cycle_candidate_length

                        if self.return_value_for_iteration is not None:
                            # at current iteration, cycle is at index 0, so calculate what the value
                            # will be on requested iteration
                            shift = (self.return_value_for_iteration - iteration) % self.cycle_size_
                            self.value_on_requested_iteration_ = first_cycle[shift]

                        return True

        self.queue.append(value)
        return False


def find_value_at(iterator: Iterator[Any],
                  iteration: int,
                  max_cycle_size: int = 500,
                  min_cycle_size: int = 3) -> (Any, CycleDetector):
    cd = CycleDetector(return_value_for_iteration=iteration,
                       max_cycle_size=max_cycle_size,
                       min_cycle_size=min_cycle_size)
    i = -1
    for i, value in enumerate(iterator):
        if cd.next_and_check(value, i + 1):
            return cd.value_on_requested_iteration_, cd
    print(f'iterator exhausted after {i + 1} iterations, no cycle detected')
    return None
