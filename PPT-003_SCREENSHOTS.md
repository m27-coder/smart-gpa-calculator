# PPT-003 Screenshot Guide

Use these steps to capture slides for **Smart GPA Calculator and Prediction System**.

## Run the app

```powershell
cd path\to\smart-gpa-calculator
.\venv\Scripts\activate
streamlit run app.py
```

Open: **http://localhost:8501**

---

## Screenshot 1 — Prediction mode (Test Case 1)

1. In the sidebar, click **Case 1 — Prediction**.
2. Confirm **Final exam score is available** is **unchecked**.
3. Capture the full dashboard showing:
   - **Current Contribution** = **49.00**
   - **Required Final Exam** = **77.50**
   - Bar chart (3 components)
   - Performance insight + formula section (scroll if needed)

**Inputs:** Assignment 85, Midterm 75, Attendance 90, Target 80.

---

## Screenshot 2 — Final score mode (Test Case 2)

1. Click **Case 2 — Final Score**.
2. Confirm the final exam checkbox is **checked** and Final = **80**.
3. Capture the dashboard showing:
   - **Final Score** = **81.00**
   - **Grade** = **B**
   - **GPA Points** = **3.0**
   - Bar chart with all 4 components

---

## Screenshot 3 — Sidebar & inputs (optional)

1. Use either case; widen the sidebar if needed.
2. Capture sidebar sliders, checkbox, weight reference, and demo buttons.

---

## Screenshot 4 — Formula & footer (optional)

Scroll to **Formula Explanation** and the footer:

**Smart GPA Calculator and Prediction System**

---

## Verify calculations (CLI)

```powershell
python verify_calculations.py
```

Expected output: both test cases PASS.
