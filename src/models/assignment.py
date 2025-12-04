from dataclasses import dataclass

from .employee import Employee


@dataclass(frozen=True)
class Assignment:
    """Represents a Secret Santa assignment: giver -> receiver."""
    giver: Employee
    receiver: Employee