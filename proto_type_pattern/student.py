from typing import override
from iclone import IClone
import copy


class Student(IClone):

    def __init__(self, name: str, student_id: str):
        self.name = name
        self.id = student_id
        self.grades = {}
        self.is_active = True

    def add_grade(self, course_id: int, grade: float) -> None:
        self.grades[course_id] = grade

    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def toggle_active_status(self) -> None:
        self.is_active = not self.is_active

    @override
    def clone(self) -> "Student":
        return copy.deepcopy(self)

    def __repr__(self):
        return (f"Student(name={self.name!r}, id={self.id!r}, "
                f"grades={self.grades}, is_active={self.is_active})")
