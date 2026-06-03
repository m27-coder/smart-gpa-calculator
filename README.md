# 🎓 Smart GPA Calculator & Prediction System

A modern, interactive academic dashboard built with **Python** and **Streamlit**. Calculate your final weighted score, predict the final exam score you need to hit your target GPA, and get smart performance insights — all in real time.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **Weighted Score Calculation** | Computes your final score using official grading weights |
| 🔮 **Prediction Mode** | Calculates the exact final exam score needed to reach your target |
| 🏅 **Grade & GPA Output** | Instant letter grade and 4.0-scale GPA |
| 💡 **Smart Performance Comment** | Context-aware academic feedback |
| 📈 **Bar Chart & Pie Chart** | Visual breakdown of weighted score contributions |
| 📋 **Score Breakdown Table** | Detailed component-level contribution view |
| 🧮 **Formula Explanation** | Transparent display of all calculation formulas |

---

## 📐 Grading Weights

| Component      | Weight |
|----------------|--------|
| Assignments    | 10%    |
| Midterm Exam   | 30%    |
| Final Exam     | 40%    |
| Attendance     | 20%    |

---

## 📊 Grade Scale

| Score Range | Grade | GPA |
|-------------|-------|-----|
| 90 – 100    | A     | 4.0 |
| 80 – 89     | B     | 3.0 |
| 70 – 79     | C     | 2.0 |
| 60 – 69     | D     | 1.0 |
| Below 60    | F     | 0.0 |

---

## 🧮 Formulas

**When final exam score IS available:**
```
Final Score = Assignment×0.10 + Midterm×0.30 + Final×0.40 + Attendance×0.20
```

**When final exam score is NOT available (Prediction Mode):**
```
Current Contribution = Assignment×0.10 + Midterm×0.30 + Attendance×0.20
Required Final Exam  = (Target Score − Current Contribution) ÷ 0.40
```

---

## 🖥️ How to Run Locally

### 1. Prerequisites

Make sure you have **Python 3.9+** installed. You can check with:
```bash
python --version
```

### 2. Navigate to the project directory
```bash
cd path\to\smart-gpa-calculator
```

### 3. (Recommended) Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Launch the app
```bash
streamlit run app.py
```

The app will open automatically in your default browser at:
```
http://localhost:8501
```

---

## 🌐 Deploy as a public website (free)

Host this app online with **Streamlit Community Cloud** (public URL like `https://your-app-name.streamlit.app`).

**Full steps:** see **[DEPLOY.md](DEPLOY.md)**

Quick overview:

1. Push this project to a **public GitHub** repository (do not upload `venv/`)
2. Sign in at **[share.streamlit.io](https://share.streamlit.io/)** with GitHub
3. **Create app** → select your repo → main file: **`app.py`** → **Deploy**

After deploy, share the live link in your presentation or submission.

---

## ✅ Verify required test cases

```bash
python verify_calculations.py
```

| Test | Expected |
|------|----------|
| Case 1 (no final) | Current Contribution **49**, Required Final **77.5** |
| Case 2 (final = 80) | Final Score **81**, Grade **B**, GPA **3.0** |

In the app sidebar, use **Case 1** / **Case 2** buttons to load demo values for screenshots.

## 📸 PPT-003 screenshots

See **[PPT-003_SCREENSHOTS.md](PPT-003_SCREENSHOTS.md)** for slide-by-slide capture instructions.

---

## 📁 Project Structure

```
smart-gpa-calculator/
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies (used by cloud host)
├── .streamlit/config.toml   # Streamlit theme & server settings
├── .python-version          # Python 3.11 for Streamlit Cloud
├── verify_calculations.py   # Automated formula tests
├── DEPLOY.md                # Public website deployment guide
├── PPT-003_SCREENSHOTS.md   # Screenshot guide for presentations
└── README.md                # This file
```

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** — interactive web UI framework
- **Pandas** — data table rendering
- **Matplotlib** — chart generation
- **NumPy** — numerical utilities

---

## 📄 License

This project was created for university coursework. Feel free to adapt it for your own academic needs.
