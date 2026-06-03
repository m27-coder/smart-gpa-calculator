"""Verify required grading formulas and demo test cases (run: python verify_calculations.py)."""

WEIGHTS = {
    "Assignments": 0.10,
    "Midterm Exam": 0.30,
    "Final Exam": 0.40,
    "Attendance": 0.20,
}

GRADE_SCALE = [
    (90, 100, "A", 4.0),
    (80, 89, "B", 3.0),
    (70, 79, "C", 2.0),
    (60, 69, "D", 1.0),
    (0, 59, "F", 0.0),
]


def score_to_grade(score: float):
    for low, high, letter, gpa in GRADE_SCALE:
        if low <= score <= high:
            return letter, gpa
    return "F", 0.0


def current_contribution(assignment, midterm, attendance):
    return (
        assignment * WEIGHTS["Assignments"]
        + midterm * WEIGHTS["Midterm Exam"]
        + attendance * WEIGHTS["Attendance"]
    )


def required_final_exam(target, contribution):
    return (target - contribution) / WEIGHTS["Final Exam"]


def final_score(assignment, midterm, final, attendance):
    return (
        assignment * WEIGHTS["Assignments"]
        + midterm * WEIGHTS["Midterm Exam"]
        + final * WEIGHTS["Final Exam"]
        + attendance * WEIGHTS["Attendance"]
    )


def test_case_1():
    a, m, att, target = 85, 75, 90, 80
    cc = current_contribution(a, m, att)
    req = required_final_exam(target, cc)
    assert cc == 49.0, f"Current Contribution: expected 49, got {cc}"
    assert req == 77.5, f"Required Final: expected 77.5, got {req}"
    print("PASS Test Case 1: contribution=49, required final=77.5")


def test_case_2():
    a, m, att, f = 85, 75, 90, 80
    fs = final_score(a, m, f, att)
    grade, gpa = score_to_grade(fs)
    assert fs == 81.0, f"Final Score: expected 81, got {fs}"
    assert grade == "B", f"Grade: expected B, got {grade}"
    assert gpa == 3.0, f"GPA: expected 3.0, got {gpa}"
    print("PASS Test Case 2: final score=81, grade=B, GPA=3.0")


def test_weights_sum():
    assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9


if __name__ == "__main__":
    test_weights_sum()
    test_case_1()
    test_case_2()
    print("\nAll required calculation tests passed.")
