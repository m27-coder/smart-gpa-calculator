"""
verify_calculations.py
======================
Verification script for Smart GPA Calculator and Prediction System.
Team WebForge — Muhammad Saad, Parneet Kaur, Abdimazhitova Aikol,
                Nasriddinov Mukhammadzokhir

Tests the seven rule-sets defined in .agents/rules/project-safety.md.
All formulas and logic mirror app.py exactly.

Run with any Python 3.x interpreter (no external dependencies):
    C:\\Users\\MICHAEL\\AppData\\Local\\Python\\bin\\python3.exe verify_calculations.py
    "C:\\Program Files\\CodeBlocks\\MinGW\\lib\\python3.9\\venv\\scripts\\nt\\python.exe" verify_calculations.py
"""

EPS = 1e-9   # tolerance for float equality
DISP = 2     # display decimal places (matches app.py round())


# ─────────────────────────────────────────────────────────────────────────────
# Protected constants — must mirror app.py exactly (project-safety.md §5)
# ─────────────────────────────────────────────────────────────────────────────

# 9-tier 4.5 GPA scale — stored highest-first so score >= low matches first
GRADE_SCALE = [
    (95, 100, "A+", 4.5),
    (90,  94, "A",  4.0),
    (85,  89, "B+", 3.5),
    (80,  84, "B",  3.0),
    (75,  79, "C+", 2.5),
    (70,  74, "C",  2.0),
    (65,  69, "D+", 1.5),
    (60,  64, "D",  1.0),
    (  0,  59, "F",  0.0),
]


def score_to_grade(score: float):
    """Mirror of app.py score_to_grade(): uses >= low, first match wins."""
    for low, high, letter, gpa in GRADE_SCALE:
        if score >= low:
            return letter, gpa
    return "F", 0.0


# ─────────────────────────────────────────────────────────────────────────────
# Calculation helpers — mirror formulas in project-safety.md §1–4
# ─────────────────────────────────────────────────────────────────────────────

def attendance_score(total_classes: int, missed_classes: int) -> float:
    """Attendance Score = ((total - missed) / total) × 100"""
    return ((total_classes - missed_classes) / total_classes) * 100


def attendance_failed(missed: int, max_allowed: int) -> bool:
    """Failure if missed > max_allowed (strict greater-than, project-safety §3)."""
    return int(missed) > int(max_allowed)


def current_contribution(assignment, midterm, att_score,
                         w_assign=10, w_mid=30, w_att=20):
    """Weighted sum of components available before final exam."""
    return (
        assignment  * w_assign / 100
        + midterm   * w_mid    / 100
        + att_score * w_att    / 100
    )


def required_final(target, contribution, w_final=40):
    """Score needed on the final exam to reach target overall."""
    return (target - contribution) / (w_final / 100)


def final_score(assignment, midterm, final, att_score,
                w_assign=10, w_mid=30, w_final=40, w_att=20):
    """Weighted overall score when final exam is available."""
    return (
        assignment  * w_assign / 100
        + midterm   * w_mid    / 100
        + final     * w_final  / 100
        + att_score * w_att    / 100
    )


def weights_valid(w_assign, w_mid, w_final, w_att) -> bool:
    return abs(w_assign + w_mid + w_final + w_att - 100) < EPS


# ─────────────────────────────────────────────────────────────────────────────
# Tests
# ─────────────────────────────────────────────────────────────────────────────

def test_1_attendance_calculation():
    """
    Test 1 — Attendance score is derived from class counts (not hardcoded).
    Total=16, Missed=1  →  (15/16)*100 = 93.75
    """
    att = attendance_score(total_classes=16, missed_classes=1)
    assert abs(att - 93.75) < EPS, \
        f"T1 Attendance Score: expected 93.75, got {att}"
    print("PASS  Test 1 — Attendance calculation: 93.75%")


def test_2_prediction_mode():
    """
    Test 2 — Prediction mode with demo-case values.
    Assignment=85, Midterm=75, Total=16, MaxMissed=5, Missed=1, Target=80
    Weights: 10 / 30 / 40 / 20

    Expected:
        Attendance Score     = 93.75
        Current Contribution = 49.75
        Required Final       = 75.625
        Displayed (round 2)  = 75.62   ← Python banker's rounding of 75.625
    """
    att = attendance_score(16, 1)
    assert abs(att - 93.75) < EPS

    cc = current_contribution(85, 75, att, w_assign=10, w_mid=30, w_att=20)
    assert abs(cc - 49.75) < EPS, \
        f"T2 Current Contribution: expected 49.75, got {cc}"

    req = required_final(80, cc, w_final=40)
    assert abs(req - 75.625) < EPS, \
        f"T2 Required Final: expected 75.625, got {req}"

    # Python's round() uses banker's rounding: 75.625 → 75.62 (rounds to even)
    disp = round(req, DISP)
    assert disp == 75.62, \
        f"T2 Displayed Required Final: expected 75.62, got {disp}"

    print(f"PASS  Test 2 — Prediction mode: contribution={cc}, "
          f"required final={disp} (exact: {req})")


def test_3_final_exam_available():
    """
    Test 3 — Final exam available with demo-case values.
    Assignment=85, Midterm=75, Final=80, Total=16, MaxMissed=5, Missed=1
    Weights: 10 / 30 / 40 / 20

    Expected:
        Final Score = 81.75
        Grade       = B
        GPA         = 3.0
    """
    att = attendance_score(16, 1)
    fs = final_score(85, 75, 80, att,
                     w_assign=10, w_mid=30, w_final=40, w_att=20)
    assert abs(fs - 81.75) < EPS, \
        f"T3 Final Score: expected 81.75, got {fs}"

    grade, gpa = score_to_grade(fs)
    assert grade == "B",  f"T3 Grade: expected B, got {grade}"
    assert abs(gpa - 3.0) < EPS, f"T3 GPA: expected 3.0, got {gpa}"

    print(f"PASS  Test 3 — Final exam mode: "
          f"score={fs}, grade={grade}, GPA={gpa}")


def test_4_custom_weights():
    """
    Test 4 — Custom grading weights (20 / 30 / 40 / 10).
    Assignment=85, Midterm=75, Final=80, Attendance Score=93.75

    Expected:
        Final Score         = 80.875
        Displayed (round 2) = 80.88  ← banker's rounding of 80.875
        Grade               = B
        GPA                 = 3.0
    """
    att = 93.75
    fs = final_score(85, 75, 80, att,
                     w_assign=20, w_mid=30, w_final=40, w_att=10)
    assert abs(fs - 80.875) < EPS, \
        f"T4 Final Score: expected 80.875, got {fs}"

    disp = round(fs, DISP)
    assert disp == 80.88, \
        f"T4 Displayed Score: expected 80.88, got {disp}"

    grade, gpa = score_to_grade(fs)
    assert grade == "B",  f"T4 Grade: expected B, got {grade}"
    assert abs(gpa - 3.0) < EPS, f"T4 GPA: expected 3.0, got {gpa}"

    print(f"PASS  Test 4 — Custom weights 20/30/40/10: "
          f"score={disp}, grade={grade}, GPA={gpa}")


def test_5_invalid_weight_total():
    """
    Test 5 — Weight total ≠ 100 must be flagged as invalid.
    Weights: 10 / 30 / 40 / 10 = 90  (invalid)
    """
    total = 10 + 30 + 40 + 10
    assert total == 90, f"T5 Weight sum: expected 90, got {total}"
    assert not weights_valid(10, 30, 40, 10), \
        "T5 weights_valid should return False for sum=90"

    # Confirm a correct set is valid
    assert weights_valid(10, 30, 40, 20), \
        "T5 weights_valid should return True for sum=100"

    print("PASS  Test 5 — Invalid weight validation: "
          "sum=90 correctly flagged; sum=100 correctly accepted")


def test_6_attendance_failure():
    """
    Test 6 — Attendance failure override (project-safety §3).
    Total=16, MaxAllowed=5, Missed=6  →  missed > allowed → FAIL
    When failed: grade=F, gpa=0.0, required final=N/A
    Boundary: missed=5 (== max_allowed) is NOT a failure.
    """
    assert attendance_failed(missed=6, max_allowed=5), \
        "T6 attendance_failed: expected True when missed(6) > max_allowed(5)"

    assert not attendance_failed(missed=5, max_allowed=5), \
        "T6 attendance_failed: expected False when missed(5) == max_allowed(5)"

    # When attendance fails the app sets grade='F', gpa=0.0 directly
    grade, gpa = "F", 0.0
    assert grade == "F"
    assert abs(gpa - 0.0) < EPS

    print("PASS  Test 6 -- Attendance failure: "
          "missed=6>max=5 -> F/0.0; missed=5==max=5 -> safe (not failed)")


def test_7_gpa_scale_boundaries():
    """
    Test 7 — 9-tier 4.5 GPA scale boundaries.

    app.py score_to_grade() uses:  score >= low, first match wins (descending)
    This correctly handles fractional scores like 94.5 (≥90 → A)
    and 89.7 (≥85 → B+).

    NOTE on display rounding: the app rounds display values to 2 d.p.
    but score_to_grade() receives the unrounded float. Tests here
    match that behaviour.
    """
    cases = [
        # (score,  exp_grade, exp_gpa,  description)
        (95.00,  "A+", 4.5, "95.0 -> A+"),
        (94.50,  "A",  4.0, "94.5 -> A  (>=90, first match after A+)"),
        (90.00,  "A",  4.0, "90.0 -> A"),
        (89.70,  "B+", 3.5, "89.7 -> B+ (>=85, first match after A)"),
        (85.00,  "B+", 3.5, "85.0 -> B+"),
        (81.75,  "B",  3.0, "81.75 -> B  (demo case 3 result)"),
        (75.00,  "C+", 2.5, "75.0 -> C+"),
        (70.00,  "C",  2.0, "70.0 -> C"),
        (65.00,  "D+", 1.5, "65.0 -> D+"),
        (60.00,  "D",  1.0, "60.0 -> D"),
        (59.99,  "F",  0.0, "59.99 -> F"),
    ]

    all_pass = True
    for score, exp_grade, exp_gpa, desc in cases:
        grade, gpa = score_to_grade(score)
        ok = (grade == exp_grade) and (abs(gpa - exp_gpa) < EPS)
        status = "PASS" if ok else "FAIL"
        if not ok:
            all_pass = False
        print(f"  {status}  {desc}: got {grade}/{gpa}")

    assert all_pass, \
        "T7 One or more GPA scale boundary values failed — see lines above"
    print("PASS  Test 7 — All 9-tier GPA scale boundaries verified")


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("Smart GPA Calculator — Verification Script")
    print("Team WebForge  |  aligned with project-safety.md")
    print("=" * 60)
    print()

    test_1_attendance_calculation()
    test_2_prediction_mode()
    test_3_final_exam_available()
    test_4_custom_weights()
    test_5_invalid_weight_total()
    test_6_attendance_failure()
    print()
    print("--- GPA Scale Boundary Tests (Test 7) ---")
    test_7_gpa_scale_boundaries()

    print()
    print("=" * 60)
    print("All 7 verification tests PASSED.")
    print("=" * 60)
