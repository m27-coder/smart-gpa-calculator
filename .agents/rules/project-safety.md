# Project Safety Rule — Smart GPA Calculator and Prediction System
# Team WebForge

> This rule is always active for all agents and tasks in this workspace.
> Any agent performing a design, CSS, or UI task must read and follow this rule
> before touching any file in this project.

---

## Absolute Protection: Never Change These

The following elements must NEVER be modified during design, UX/UI, or
visual implementation tasks. Any change to these requires an explicit,
separate instruction that is **not** a design or styling task.

### 1. Score Calculation Formulas

**Dynamic Final Score** (when final exam is available):
```
Final Score =
    (Assignment Score  × Assignment Weight  / 100)
  + (Midterm Score     × Midterm Weight     / 100)
  + (Final Exam Score  × Final Exam Weight  / 100)
  + (Attendance Score  × Attendance Weight  / 100)
```

**Dynamic Current Contribution** (when final exam is NOT available):
```
Current Contribution =
    (Assignment Score  × Assignment Weight  / 100)
  + (Midterm Score     × Midterm Weight     / 100)
  + (Attendance Score  × Attendance Weight  / 100)
```

**Required Final Exam Score** (Prediction Mode):
```
Required Final =
    (Target Score - Current Contribution) / (Final Exam Weight / 100)
```

### 2. Attendance Score Calculation

```
Attendance Score (%) =
    ((Total Classes - Missed Classes) / Total Classes) × 100
```

This formula is computed automatically. No widget asks the user directly for
attendance score. The inputs are:
- Total Classes (`st.number_input`)
- Maximum Allowed Missed Classes (`st.number_input`)
- Number of Missed Classes (`st.number_input`)

### 3. Attendance Failure Override

```
IF Missed Classes > Maximum Allowed Missed Classes:
    Grade  = "F"
    GPA    = 0.0
    Required Final Exam result is NOT presented as achievable
    Overall Score is set to None (not displayed as a number)
```

This override must take absolute precedence over all score calculations.
Never display a passing grade or a positive required-final value when
attendance has failed.

### 4. Grading Weight Validation

```
Total Weight = Assignment Weight + Midterm Weight + Final Exam Weight + Attendance Weight

IF Total Weight ≠ 100:
    All score calculations are BLOCKED (set to None or "—")
    A visible warning must be displayed
    No grade, GPA, or required final is shown
```

### 5. GPA and Grade Scale (4.5 Scale — 9 Tiers)

This scale must not be altered, condensed, or extended:

| Score Range | Grade | GPA  | Meaning        |
|-------------|-------|------|----------------|
| 95 – 100    | A+    | 4.5  | Outstanding    |
| 90 – 94     | A     | 4.0  | Excellent      |
| 85 – 89     | B+    | 3.5  | Very Good      |
| 80 – 84     | B     | 3.0  | Good           |
| 75 – 79     | C+    | 2.5  | Above Average  |
| 70 – 74     | C     | 2.0  | Satisfactory   |
| 65 – 69     | D+    | 1.5  | Below Average  |
| 60 – 64     | D     | 1.0  | Passing        |
| Below 60    | F     | 0.0  | Failing        |

The `score_to_grade()` function and the `GRADE_SCALE` constant implement this
table. Do not change either.

### 6. Demo Case Preset Values

**Demo Case 1** (Prediction Mode):
- Assignment Score: 85
- Midterm Score: 75
- Total Classes: 16
- Max Allowed Missed: 5
- Missed Classes: 1
- has_final: False
- Target Score: 80
- Weights: Assignment 10 / Midterm 30 / Final 40 / Attendance 20

**Demo Case 2** (Final Exam Available):
- Assignment Score: 85
- Midterm Score: 75
- Total Classes: 16
- Max Allowed Missed: 5
- Missed Classes: 1
- has_final: True
- Final Score: 80
- Weights: Assignment 10 / Midterm 30 / Final 40 / Attendance 20

These values in `_load_demo_case_1()` and `_load_demo_case_2()` must not change.

### 7. Session State Keys and Widget Keys

The following `st.session_state` keys and widget `key=` parameters must not
be renamed, removed, or reassigned to different widgets:

| Key | Widget / Usage |
|-----|---------------|
| `page` | Navigation gate ("start" / "main") |
| `theme` | Theme state ("dark" / "light") |
| `assignment_score` | Assignment slider |
| `midterm_score` | Midterm slider |
| `total_classes` | Total classes number_input |
| `max_allowed_missed` | Max missed number_input |
| `missed_classes` | Missed classes number_input |
| `has_final` | Final exam checkbox |
| `final_score` | Final exam slider |
| `target_score` | Target score slider |
| `w_assignment` | Assignment weight number_input |
| `w_midterm` | Midterm weight number_input |
| `w_final` | Final exam weight number_input |
| `w_attendance` | Attendance weight number_input |
| `open_start_btn` | Start Calculation button |
| `sidebar_home_btn` | ← Home button |
| `demo_case_1_btn` | Load Demo Case button |
| `demo_case_2_btn` | With Final Exam button |
| `op_theme_radio` | Opening page theme toggle |
| `sb_theme_radio` | Sidebar theme toggle |

### 8. Session State Navigation Logic

```python
if "page" not in st.session_state:
    st.session_state.page = "start"

if st.session_state.page == "start":
    # Opening page renders here
    st.stop()   # ← this line must remain; prevents dashboard from rendering

# Dashboard renders here
```

The `st.stop()` call after the opening page is critical. Do not remove it.

### 9. Theme State Logic

```python
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
_dark = (st.session_state.theme == "dark")
```

Both the opening page theme radio and the sidebar theme radio write to
`st.session_state.theme` and call `st.rerun()`. This pattern must be preserved.

### 10. Default Widget Weights (Canonical Values)

Default values injected by Streamlit when no session state exists:
- Assignment Weight: 10%
- Midterm Weight: 30%
- Final Exam Weight: 40%
- Attendance Weight: 20%

These must remain the defaults for a clean session.

### 11. Protected Files (Do Not Modify During Design Tasks)

| File | Protection Reason |
|------|------------------|
| `app.py` (calculation blocks) | Core formulas |
| `requirements.txt` | Deployment dependencies |
| `.streamlit/config.toml` | Streamlit server configuration |
| `DEPLOY.md` | Deployment documentation |
| `.gitignore` | Version control configuration |
| `verify_calculations.py` | Test verification script |
| All `app_backup_*.py` files | Historical backups — read-only |

---

## What Design Tasks MAY Change

Design and UX/UI tasks are explicitly permitted to change:

- CSS injection blocks (`st.markdown('<style>…</style>', unsafe_allow_html=True)`)
- HTML template strings in `st.markdown('…', unsafe_allow_html=True)` — for
  non-functional display text, styling classes, and structure
- Chart function aesthetics (colors, backgrounds, fonts) via a `dark: bool` param
- The `.open-creator` div text (Team WebForge identity update)
- The footer HTML content (team name and member names)
- Google Fonts `@import` statements in the CSS block

---

## Violation Response

If an agent is about to perform an action that would change a protected element:

1. **Stop immediately.**
2. Report the intended change and why it was identified as a violation.
3. Ask for explicit confirmation before proceeding.
4. If working autonomously (Goal mode), skip the protected change entirely and
   complete all safe changes. Log the skipped item in the final report.

---

*Smart GPA Calculator and Prediction System — Team WebForge*
*Muhammad Saad · Parneet Kaur · Abdimazhitova Aikol · Nasriddinov Mukhammadzokhir*
