from dataclasses import dataclass


@dataclass(frozen=True)
class Employee:
    """Represents an employee participating in Secret Santa."""
    name: str
    email: str

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"
