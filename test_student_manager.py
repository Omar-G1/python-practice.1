import os
import pytest
from students_manager import StudentManager

@pytest.fixture(autouse=True)
def isolated_manager(monkeypatch):
    """Fixture to create a new manager for each test and use a temporary file."""
    temp_file = "test_students.json"
    monkeypatch.setattr("students_manager.FILE_PATH", temp_file)
    manager = StudentManager()
    yield manager
    if os.path.exists(temp_file):
        os.remove(temp_file)

def test_add_student(isolated_manager):
    manager = isolated_manager
    initial_count = len(manager.students)
    manager.add_student("Test Student", 90, 20)
    assert len(manager.students) == initial_count + 1

def test_view_all_students(capsys, isolated_manager):
    manager = isolated_manager
    manager.add_student("Test Student", 90, 20)
    manager.view_all_students()
    captured = capsys.readouterr()
    assert "Test Student - Grade: 90, Age: 20" in captured.out

def test_search_student(capsys, isolated_manager):
    manager = isolated_manager
    manager.add_student("Test Student", 90, 20)
    manager.search_student("Test Student")
    captured = capsys.readouterr()
    assert "Found: Test Student (Grade: 90, Age: 20)" in captured.out

def test_statistics(capsys, isolated_manager):
    manager = isolated_manager
    manager.add_student("Test Student", 90, 20)
    manager.add_student("Another Student", 80, 22)
    manager.statistics()
    captured = capsys.readouterr()
    assert "Average grade: 85.00" in captured.out
    assert "Highest grade: 90" in captured.out
    assert "Lowest grade: 80" in captured.out

def test_calculator(isolated_manager):
    manager = isolated_manager
    assert manager.calculator(5, 3, "add") == 8
    assert manager.calculator(5, 3, "subtract") == 2
    assert manager.calculator(5, 3, "multiply") == 15
    assert manager.calculator(6, 3, "divide") == 2.0
    assert manager.calculator(5, 0, "divide") == "Error: divide by zero"
    assert manager.calculator(5, 3, "unknown") == "Error: unknown operation"