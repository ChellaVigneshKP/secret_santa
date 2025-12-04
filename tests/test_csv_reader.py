import pytest

from services.csv_reader import CSVReader
from utils.exceptions import InvalidCSVError


def test_read_employees_valid(tmp_path):
    test_file = tmp_path / "employees.csv"
    test_file.write_text(
        "Employee_Name,Employee_EmailID\nAlice,alice@mail.com\nBob,bob@mail.com\n"
    )
    result = CSVReader.read_employees(str(test_file))
    assert len(result) == 2


def test_read_employees_missing_file():
    with pytest.raises(InvalidCSVError):
        CSVReader.read_employees("missing.csv")


def test_read_employees_missing_columns(tmp_path):
    test_file = tmp_path / "bad.csv"
    test_file.write_text("InvalidColumn\nValue\n")
    with pytest.raises(InvalidCSVError):
        CSVReader.read_employees(str(test_file))


def test_read_previous_assignments_missing_file():
    result = CSVReader.read_previous_assignments("not_exists.csv")
    assert result == []


def test_read_previous_assignments_valid(tmp_path):
    test_file = tmp_path / "prev.csv"
    test_file.write_text(
        "Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID\n"
        "Alice,alice@mail.com,Bob,bob@mail.com\n"
        "Bob,bob@mail.com,Alice,alice@mail.com\n"
    )
    result = CSVReader.read_previous_assignments(str(test_file))
    assert len(result) == 2
    assert result[0].giver.name == "Alice"
    assert result[0].receiver.email == "bob@mail.com"


def test_read_previous_assignments_missing_columns(tmp_path):
    test_file = tmp_path / "invalid_prev.csv"
    test_file.write_text("WrongCol1,WrongCol2\nA,B\n")
    with pytest.raises(InvalidCSVError):
        CSVReader.read_previous_assignments(str(test_file))
