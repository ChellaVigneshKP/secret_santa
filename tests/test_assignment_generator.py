from models.employee import Employee
from models.assignment import Assignment
from services.assignment_generator import AssignmentGenerator


def test_assignments_are_unique_and_no_self_assignment():
    # Setup employees
    employees = [
        Employee("Alice", "alice@mail.com"),
        Employee("Bob", "bob@mail.com"),
        Employee("Charlie", "charlie@mail.com"),
    ]

    # No previous assignments
    generator = AssignmentGenerator(employees=employees, previous_assignments=[])
    assignments = generator.generate()

    # Validate
    receivers = {a.receiver.email for a in assignments}

    # Each giver has exactly one receiver
    assert len(assignments) == len(employees)

    # All child assignments must be unique
    assert len(receivers) == len(employees)

    # Self assignment not allowed
    for a in assignments:
        assert a.giver.email != a.receiver.email


def test_previous_assignment_avoided():
    employees = [
        Employee("A", "a@mail.com"),
        Employee("B", "b@mail.com"),
        Employee("C", "c@mail.com"),
    ]

    # Previous assignments: A->B, B->C, C->A
    prev = [
        Assignment(employees[0], employees[1]),
        Assignment(employees[1], employees[2]),
        Assignment(employees[2], employees[0]),
    ]

    generator = AssignmentGenerator(employees, prev)
    assignments = generator.generate()

    # Ensure no previous mapping is repeated
    prev_map = {a.giver.email: a.receiver.email for a in prev}
    for a in assignments:
        assert prev_map[a.giver.email] != a.receiver.email
