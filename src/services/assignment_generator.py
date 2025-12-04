import random
from typing import Dict, List, Optional

from models.assignment import Assignment
from models.employee import Employee
from utils.exceptions import AssignmentGenerationError


class AssignmentGenerator:
    """Generates Secret Santa assignments with constraints."""

    def __init__(
            self,
            employees: List[Employee],
            previous_assignments: Optional[List[Assignment]] = None,
    ) -> None:
        self.employees = employees
        self.previous_assignments = previous_assignments or []

        self.prev_map: Dict[str, str] = {
            a.giver.email: a.receiver.email for a in self.previous_assignments
        }

    def generate(self) -> List[Assignment]:
        """Generate a valid set of assignments or raise AssignmentGenerationError."""

        givers = list(self.employees)
        receivers = list(self.employees)

        random.shuffle(givers)
        random.shuffle(receivers)

        used = set()
        result: Dict[str, Employee] = {}

        def backtrack(index: int) -> bool:
            if index == len(givers):
                return True

            giver = givers[index]
            candidates = receivers[:]
            random.shuffle(candidates)

            for receiver in candidates:
                if receiver.email in used:
                    continue
                if receiver.email == giver.email:
                    continue
                if self.prev_map.get(giver.email) == receiver.email:
                    continue

                used.add(receiver.email)
                result[giver.email] = receiver

                if backtrack(index + 1):
                    return True

                used.remove(receiver.email)
                del result[giver.email]

            return False

        if not backtrack(0):
            raise AssignmentGenerationError("Could not generate a valid Secret Santa assignment with the given constraints.")

        assignments: List[Assignment] = []
        for giver in sorted(self.employees, key=lambda e: e.email):
            receiver = result[giver.email]
            assignments.append(Assignment(giver=giver, receiver=receiver))

        return assignments
