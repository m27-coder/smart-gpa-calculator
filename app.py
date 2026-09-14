import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

PROJECT_TITLE = "Smart GPA Calculator and Prediction System"

# ──────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title=PROJECT_TITLE,
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────────────────
# THEME  — must be initialised before the CSS block
# ──────────────────────────────────────────────────────────────────────────────
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
_dark = (st.session_state.theme == "dark")

# ──────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS  (dark-mode base — always applied)
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* ── App background ── */
.stApp {
    background: #0b0a1a;
    background-image:
        radial-gradient(ellipse 80% 60% at 20% 0%,  rgba(109,40,217,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 85% 10%, rgba(37,99,235,0.15)  0%, transparent 55%),
        radial-gradient(ellipse 50% 40% at 50% 90%, rgba(16,185,129,0.08) 0%, transparent 50%);
    min-height: 100vh;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0b1f 0%, #0f1629 60%, #0a1020 100%) !important;
    border-right: 1px solid rgba(139,92,246,0.2) !important;
}
[data-testid="stSidebar"] * { color: #e2e0f0 !important; }
[data-testid="stSidebar"] .stSlider [data-testid="stThumbValue"] {
    color: #a78bfa !important;
}

/* ── Sidebar score pill ── */
.score-pill {
    display: flex; align-items: center; justify-content: space-between;
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.25);
    border-radius: 10px;
    padding: 8px 14px;
    margin: 6px 0 14px 0;
    font-size: 0.82rem; color: #c4b5fd;
}
.score-pill .pill-val {
    font-size: 1.1rem; font-weight: 700; color: #a78bfa;
}

/* ── Sidebar section label ── */
.sb-label {
    font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em;
    text-transform: uppercase; color: #6d5d9e !important;
    margin: 18px 0 8px 2px;
}

/* ── Sidebar divider ── */
.sb-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139,92,246,0.3), transparent);
    margin: 14px 0;
}

/* ── Metric cards ── */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 22px 20px 18px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    position: relative;
    overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}
div[data-testid="metric-container"]:hover {
    transform: translateY(-4px);
    border-color: rgba(139,92,246,0.4);
    box-shadow: 0 16px 40px rgba(109,40,217,0.22), 0 0 0 1px rgba(139,92,246,0.15);
}
div[data-testid="metric-container"] label {
    color: #7c6fa0 !important;
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}
div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #f0eeff !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.02em !important;
}

/* ── Section header ── */
.sec-hdr {
    display: flex; align-items: center; gap: 10px;
    font-size: 0.72rem; font-weight: 800; letter-spacing: 0.12em;
    text-transform: uppercase; color: #7c6fa0;
    margin: 0 0 16px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(139,92,246,0.18);
}
.sec-hdr span { font-size: 1rem; }

/* ── Grade badge ── */
.grade-wrap {
    text-align: center; padding: 28px 16px 22px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 22px;
    position: relative; overflow: hidden;
}
.grade-wrap::before {
    content:''; position:absolute; inset:0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(139,92,246,0.12), transparent);
    pointer-events: none;
}
.grade-letter {
    font-size: 5rem; font-weight: 900; line-height: 1;
    letter-spacing: -0.03em; display: inline-block;
    padding: 4px 32px 8px;
    border-radius: 16px;
    margin-bottom: 14px;
}
.grade-A  { background: linear-gradient(135deg,#059669,#34d399); color:#002f1e;
           box-shadow: 0 8px 28px rgba(52,211,153,0.35); }
.grade-Ap { background: linear-gradient(135deg,#065f46,#10b981); color:#fff;
           box-shadow: 0 8px 28px rgba(16,185,129,0.50); }
.grade-B  { background: linear-gradient(135deg,#1d4ed8,#60a5fa); color:#001230;
           box-shadow: 0 8px 28px rgba(96,165,250,0.35); }
.grade-Bp { background: linear-gradient(135deg,#1e40af,#3b82f6); color:#fff;
           box-shadow: 0 8px 28px rgba(59,130,246,0.45); }
.grade-C  { background: linear-gradient(135deg,#d97706,#fbbf24); color:#2d1500;
           box-shadow: 0 8px 28px rgba(251,191,36,0.35); }
.grade-Cp { background: linear-gradient(135deg,#92400e,#f59e0b); color:#fff;
           box-shadow: 0 8px 28px rgba(245,158,11,0.45); }
.grade-D  { background: linear-gradient(135deg,#b91c1c,#f87171); color:#fff;
           box-shadow: 0 8px 28px rgba(248,113,113,0.35); }
.grade-Dp { background: linear-gradient(135deg,#7f1d1d,#ef4444); color:#fff;
           box-shadow: 0 8px 28px rgba(239,68,68,0.50); }
.grade-F  { background: linear-gradient(135deg,#374151,#6b7280); color:#fff;
           box-shadow: 0 8px 28px rgba(107,114,128,0.25); }
.grade-gpa {
    font-size: 0.82rem; font-weight: 600; color: #9d8ec4;
    letter-spacing: 0.04em;
}
.grade-gpa strong { color: #e0d8ff; font-size: 1rem; }
.grade-sub {
    font-size: 0.78rem; color: #7060a0; margin-top: 6px;
}
.grade-sub b { color: #b8a8e0; }

/* ── Performance comment box ── */
.perf-box {
    display: flex; gap: 16px; align-items: flex-start;
    border-radius: 16px; padding: 20px 20px;
    margin-bottom: 4px;
    backdrop-filter: blur(8px);
    position: relative; overflow: hidden;
}
.perf-box::before {
    content: ''; position: absolute; left: 0; top: 0; bottom: 0;
    width: 4px; border-radius: 4px 0 0 4px;
}
.perf-success {
    background: rgba(16,185,129,0.09);
    border: 1px solid rgba(16,185,129,0.22);
}
.perf-success::before { background: linear-gradient(180deg,#10b981,#34d399); }
.perf-info {
    background: rgba(99,102,241,0.09);
    border: 1px solid rgba(99,102,241,0.22);
}
.perf-info::before { background: linear-gradient(180deg,#6366f1,#818cf8); }
.perf-warn {
    background: rgba(245,158,11,0.09);
    border: 1px solid rgba(245,158,11,0.22);
}
.perf-warn::before { background: linear-gradient(180deg,#f59e0b,#fbbf24); }
.perf-danger {
    background: rgba(239,68,68,0.09);
    border: 1px solid rgba(239,68,68,0.22);
}
.perf-danger::before { background: linear-gradient(180deg,#ef4444,#f87171); }
.perf-icon { font-size: 2rem; flex-shrink: 0; margin-top: 2px; }
.perf-content .perf-title {
    font-size: 1rem; font-weight: 700; color: #f0eeff;
    margin-bottom: 6px;
}
.perf-content .perf-body {
    font-size: 0.88rem; line-height: 1.65; color: #b0a8d0;
}

/* ── Formula section ── */
.formula-outer {
    background: rgba(10,8,28,0.65);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 20px;
    overflow: hidden;
}
.formula-header {
    background: linear-gradient(90deg, rgba(109,40,217,0.25), rgba(37,99,235,0.15));
    padding: 14px 24px;
    border-bottom: 1px solid rgba(139,92,246,0.2);
    font-size: 0.72rem; font-weight: 800; letter-spacing: 0.12em;
    text-transform: uppercase; color: #9d8ec4;
}
.formula-body { padding: 20px 24px; }
.formula-block {
    background: rgba(15,10,40,0.6);
    border: 1px solid rgba(139,92,246,0.15);
    border-radius: 12px;
    padding: 16px 18px;
    margin-bottom: 14px;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 0.82rem; line-height: 1.9; color: #b8b0d8;
}
.formula-block .fb-title {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: #6d5d9e;
    margin-bottom: 10px;
}
.formula-block .fb-eq { color: #a0ffcc; font-weight: 600; }
.formula-block .fb-eq-b { color: #93c5fd; font-weight: 600; }
.formula-block .fb-eq-c { color: #fcd34d; font-weight: 600; }
.weight-chip {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 8px; padding: 4px 10px;
    font-size: 0.78rem; color: #c4b5fd;
    margin: 3px 4px 3px 0;
}
.weight-chip .wc-pct {
    font-weight: 700; color: #a78bfa;
}

/* ── Grading table rows ── */
.grade-row {
    display: flex; align-items: center; gap: 12px;
    padding: 10px 16px;
    border-radius: 10px;
    margin-bottom: 6px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    font-size: 0.88rem;
}
.grade-row:hover { background: rgba(139,92,246,0.08); border-color: rgba(139,92,246,0.2); }
.grade-row .gr-range { color: #9d8ec4; flex: 1; font-size: 0.82rem; }
.grade-row .gr-letter { font-weight: 800; font-size: 1.2rem; width: 28px; }
.grade-row .gr-gpa { color: #7c6fa0; font-size: 0.8rem; width: 50px; text-align: right; }
.grade-row .gr-tag {
    font-size: 0.7rem; font-weight: 700; letter-spacing: 0.06em;
    padding: 2px 10px; border-radius: 20px;
}
.tag-A  { background: rgba(52,211,153,0.15);  color: #34d399; }
.tag-Ap { background: rgba(16,185,129,0.18);  color: #10b981; border: 1px solid rgba(16,185,129,0.3); }
.tag-B  { background: rgba(96,165,250,0.15);  color: #60a5fa; }
.tag-Bp { background: rgba(59,130,246,0.18);  color: #3b82f6; border: 1px solid rgba(59,130,246,0.3); }
.tag-C  { background: rgba(251,191,36,0.15);  color: #fbbf24; }
.tag-Cp { background: rgba(245,158,11,0.18);  color: #f59e0b; border: 1px solid rgba(245,158,11,0.3); }
.tag-D  { background: rgba(248,113,113,0.15); color: #f87171; }
.tag-Dp { background: rgba(239,68,68,0.18);   color: #ef4444; border: 1px solid rgba(239,68,68,0.3); }
.tag-F  { background: rgba(107,114,128,0.15); color: #9ca3af; }

/* ── Footer ── */
.app-footer {
    margin-top: 56px;
    padding: 32px 0 24px;
    border-top: 1px solid rgba(139,92,246,0.18);
    text-align: center;
    position: relative;
}
.app-footer::before {
    content: '';
    position: absolute; top: 0; left: 20%; right: 20%; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139,92,246,0.5), rgba(99,102,241,0.4), transparent);
}
.footer-title {
    font-size: 1.05rem; font-weight: 700; color: #c4b5fd;
    letter-spacing: 0.02em; margin-bottom: 6px;
}
.footer-sub {
    font-size: 0.76rem; color: #4a3f70;
    letter-spacing: 0.04em; margin-bottom: 14px;
}
.footer-badges {
    display: flex; justify-content: center; gap: 8px;
    flex-wrap: wrap; margin-top: 12px;
}
.footer-badge {
    font-size: 0.7rem; font-weight: 600; letter-spacing: 0.06em;
    padding: 3px 14px; border-radius: 20px;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.22);
    color: #9d8ec4;
    transition: background 0.2s;
}
.footer-badge:hover { background: rgba(139,92,246,0.22); }
.footer-team-credit {
    font-size: 0.82rem; font-weight: 700; color: #c4b5fd;
    letter-spacing: 0.03em; margin-bottom: 8px;
}
.footer-team-credit strong { color: #a78bfa; }
.footer-members {
    font-size: 0.72rem; color: #5a4f80;
    letter-spacing: 0.02em; margin-bottom: 14px;
    line-height: 1.8;
}

/* ── Demo case buttons ── */
.demo-btn-wrap { margin: 4px 0 10px; }
[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    border-radius: 10px;
    border: 1px solid rgba(139,92,246,0.35);
    background: rgba(139,92,246,0.12);
    color: #c4b5fd !important;
    font-size: 0.78rem;
    font-weight: 600;
    transition: all 0.2s;
}
[data-testid="stSidebar"] .stButton > button:hover {
    border-color: rgba(167,139,250,0.6);
    background: rgba(139,92,246,0.22);
    box-shadow: 0 4px 14px rgba(139,92,246,0.2);
}

/* ── Main area primary Start / action buttons ── */
.stButton > button[kind="primary"],
[data-testid="stMainBlockContainer"] .stButton > button {
    background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%) !important;
    border: none !important;
    color: #fff !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.04em !important;
    border-radius: 14px !important;
    padding: 14px 0 !important;
    box-shadow: 0 8px 28px rgba(109,40,217,0.38) !important;
    transition: all 0.25s !important;
}
[data-testid="stMainBlockContainer"] .stButton > button:hover {
    background: linear-gradient(135deg, #6d28d9 0%, #4338ca 100%) !important;
    box-shadow: 0 12px 36px rgba(109,40,217,0.5) !important;
    transform: translateY(-2px) !important;
}

/* ── Generic text overrides ── */
p, li { color: #b0a8cc !important; }
h1, h2, h3, h4, h5 { color: #f0eeff !important; }
[data-testid="stDataFrame"] { border-radius: 14px; overflow: hidden; }
[data-testid="stDataFrame"] table { font-size: 0.84rem !important; }

/* ── Slider thumb colour ── */
[data-baseweb="slider"] [data-testid="stThumb"] {
    background: #7c3aed !important;
    border-color: #a78bfa !important;
}

/* ── Number input improvements ── */
[data-testid="stNumberInput"] input {
    border-radius: 9px !important;
    border-color: rgba(139,92,246,0.3) !important;
    background: rgba(139,92,246,0.06) !important;
    color: #f0eeff !important;
    font-size: 0.9rem !important;
}

/* ── Section card wrapper ── */
.section-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(139,92,246,0.12);
    border-radius: 22px;
    padding: 28px 24px;
    margin-bottom: 24px;
}

/* ── Chart section background ── */
.chart-bg {
    background: rgba(10,8,28,0.55);
    border: 1px solid rgba(139,92,246,0.14);
    border-radius: 18px;
    padding: 20px 18px;
}

/* ── Opening page ── */
.open-page-bg {
    min-height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px 16px 60px;
}
.open-card {
    max-width: 740px;
    width: 100%;
    background: rgba(10,8,28,0.88);
    border: 1px solid rgba(139,92,246,0.35);
    border-radius: 28px;
    padding: 60px 64px 52px;
    box-shadow: 0 24px 90px rgba(0,0,0,0.55), 0 0 0 1px rgba(139,92,246,0.08);
    text-align: center;
    position: relative;
    overflow: hidden;
}
.open-card::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% -10%, rgba(139,92,246,0.14), transparent);
    pointer-events: none;
}
.open-emoji { font-size: 4rem; line-height: 1; margin-bottom: 22px; }
.open-title {
    font-size: 2.5rem; font-weight: 900; line-height: 1.22;
    background: linear-gradient(100deg,#c4b5fd 0%,#818cf8 45%,#67e8f9 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 18px;
}
.open-subtitle {
    font-size: 1.0rem; color: #9d8ec4; margin-bottom: 18px; line-height: 1.65;
    max-width: 560px; margin-left: auto; margin-right: auto;
}
.open-desc {
    font-size: 0.88rem; color: #5a4f80; line-height: 1.8;
    margin-bottom: 32px; max-width: 520px; margin-left: auto; margin-right: auto;
}
.open-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139,92,246,0.35), transparent);
    margin: 0 0 30px;
}
.open-features {
    display: flex; flex-wrap: wrap; gap: 10px;
    justify-content: center; margin-bottom: 34px;
}
.open-chip {
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.28);
    border-radius: 50px;
    padding: 6px 18px;
    font-size: 0.79rem; color: #b8a8e0; font-weight: 600;
    letter-spacing: 0.02em;
}
.open-creator {
    font-size: 0.85rem; color: #5a4f80;
    margin-bottom: 28px; letter-spacing: 0.04em;
    padding: 10px 20px;
    background: rgba(139,92,246,0.06);
    border-radius: 30px;
    display: inline-block;
}
.open-creator strong { color: #a78bfa; font-weight: 700; }

/* ── Team WebForge block (opening page) ── */
.open-team-block {
    margin-top: 4px;
    margin-bottom: 28px;
    padding: 14px 20px;
    background: rgba(139,92,246,0.06);
    border: 1px solid rgba(139,92,246,0.18);
    border-radius: 16px;
    text-align: center;
}
.open-team-label {
    font-size: 0.72rem; font-weight: 700;
    letter-spacing: 0.12em; text-transform: uppercase;
    color: #9d8ec4; margin-bottom: 10px;
}
.open-team-members {
    display: flex; flex-wrap: wrap;
    justify-content: center; gap: 4px 14px;
}
.open-member {
    font-size: 0.8rem; font-weight: 500; color: #c4b5fd;
    white-space: nowrap;
}
.member-id {
    font-size: 0.72rem; font-weight: 400; color: #5a4f80;
}
@media (max-width: 480px) {
    .open-team-members { flex-direction: column; align-items: center; gap: 6px; }
    .open-member { white-space: normal; }
}

/* ══════════════════════════════════════════════════════════════════════
   ANIMATIONS  (theme-agnostic — motion only, no colour overrides)
   ══════════════════════════════════════════════════════════════════════ */

/* ── Keyframes ── */
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(32px); }
    to   { opacity: 1; transform: translateY(0);    }
}
@keyframes subtlePulse {
    0%,100% { box-shadow: 0 0 0 0   rgba(139,92,246,0);    }
    50%      { box-shadow: 0 0 22px 4px rgba(139,92,246,0.18); }
}

/* ── Opening page entrance ── */
.open-page-bg {
    animation: fadeIn 0.45s ease-out both;
}
.open-card {
    animation: slideUp 0.55s cubic-bezier(0.22,1,0.36,1) both;
    animation-delay: 0.05s;
}
.open-emoji    { animation: fadeIn 0.4s ease both; animation-delay: 0.25s; }
.open-title    { animation: fadeIn 0.5s ease both; animation-delay: 0.35s; }
.open-subtitle { animation: fadeIn 0.5s ease both; animation-delay: 0.45s; }
.open-desc     { animation: fadeIn 0.5s ease both; animation-delay: 0.50s; }
.open-features { animation: fadeIn 0.5s ease both; animation-delay: 0.55s; }
.open-creator  { animation: fadeIn 0.5s ease both; animation-delay: 0.62s; }

/* ── Feature chip hover ── */
.open-chip {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    cursor: default;
}
.open-chip:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 18px rgba(139,92,246,0.22);
}

/* ── Section header slide-in ── */
.sec-hdr {
    animation: slideUp 0.4s ease both;
    animation-delay: 0.05s;
}

/* ── Grade badge hover glow ── */
.grade-wrap {
    transition: box-shadow 0.28s ease, border-color 0.28s ease, transform 0.22s ease;
}
.grade-wrap:hover {
    transform: translateY(-3px);
    border-color: rgba(139,92,246,0.5) !important;
    box-shadow: 0 20px 56px rgba(109,40,217,0.28) !important;
}

/* ── Performance insight box hover ── */
.perf-box {
    transition: transform 0.22s ease, box-shadow 0.22s ease;
}
.perf-box:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.18);
}

/* ── Grade scale row hover ── */
.grade-row {
    transition: background 0.18s ease, border-color 0.18s ease, transform 0.18s ease;
}
.grade-row:hover {
    transform: translateX(5px);
}

/* ── Formula card hover ── */
.formula-outer {
    transition: box-shadow 0.25s ease;
}
.formula-outer:hover {
    box-shadow: 0 10px 32px rgba(109,40,217,0.14);
}
.formula-block {
    transition: border-color 0.2s ease;
}
.formula-block:hover {
    border-color: rgba(139,92,246,0.32) !important;
}

/* ── Weight chip hover ── */
.weight-chip {
    transition: transform 0.18s ease, box-shadow 0.18s ease;
    cursor: default;
}
.weight-chip:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 14px rgba(139,92,246,0.2);
}

/* ── Score pill hover ── */
.score-pill {
    transition: border-color 0.2s ease, background 0.2s ease;
}

/* ── Footer badge hover ── */
.footer-badge {
    transition: background 0.2s ease, transform 0.18s ease;
}
.footer-badge:hover {
    transform: translateY(-2px);
}

/* ── Section card hover ── */
.section-card {
    transition: box-shadow 0.25s ease, border-color 0.25s ease;
}
.section-card:hover {
    box-shadow: 0 8px 28px rgba(109,40,217,0.1);
    border-color: rgba(139,92,246,0.22) !important;
}

/* ── Open creator pill pulse (one shot, then stops) ── */
.open-creator {
    animation: fadeIn 0.5s ease both, subtlePulse 2.5s ease-in-out 0.8s 2;
}
</style>

""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# LIGHT MODE CSS  (additive overrides — only injected when theme == "light")
# ──────────────────────────────────────────────────────────────────────────────
if not _dark:
    st.markdown("""
    <style>
    /* ===== LIGHT MODE OVERRIDES ===== */

    /* App background */
    .stApp {
        background: #f7f6ff !important;
        background-image:
            radial-gradient(ellipse 80% 60% at 20% 0%, rgba(109,40,217,0.06), transparent 60%),
            radial-gradient(ellipse 60% 50% at 85% 10%, rgba(37,99,235,0.05), transparent 55%) !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg,#eeebff 0%,#e5e0f8 60%,#eae7f8 100%) !important;
        border-right: 1px solid rgba(139,92,246,0.2) !important;
    }
    [data-testid="stSidebar"] * { color: #2d1f5e !important; }
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(139,92,246,0.1) !important;
        border-color: rgba(109,40,217,0.3) !important;
        color: #3d2f7e !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(139,92,246,0.2) !important;
    }

    /* Metric cards */
    div[data-testid="metric-container"] {
        background: rgba(255,255,255,0.95) !important;
        border: 1px solid rgba(139,92,246,0.14) !important;
        box-shadow: 0 4px 20px rgba(109,40,217,0.07) !important;
    }
    div[data-testid="metric-container"]:hover {
        box-shadow: 0 10px 32px rgba(109,40,217,0.13) !important;
        border-color: rgba(139,92,246,0.28) !important;
    }
    div[data-testid="metric-container"] label { color: #5a4f80 !important; }
    div[data-testid="metric-container"] [data-testid="stMetricValue"] { color: #1a1535 !important; }

    /* Section header */
    .sec-hdr { color: #5a4f80 !important; border-bottom-color: rgba(109,40,217,0.15) !important; }

    /* Grade wrap */
    .grade-wrap {
        background: rgba(255,255,255,0.97) !important;
        border-color: rgba(139,92,246,0.18) !important;
        box-shadow: 0 8px 32px rgba(109,40,217,0.07) !important;
    }
    .grade-gpa { color: #5a4f80 !important; }
    .grade-gpa strong { color: #1a1535 !important; }
    .grade-sub { color: #7060a0 !important; }
    .grade-sub b { color: #3d2f7e !important; }

    /* Performance boxes */
    .perf-success { background: rgba(16,185,129,0.07) !important; }
    .perf-info    { background: rgba(99,102,241,0.07) !important; }
    .perf-warn    { background: rgba(245,158,11,0.07) !important; }
    .perf-danger  { background: rgba(239,68,68,0.07) !important; }
    .perf-content .perf-title { color: #1a1535 !important; }
    .perf-content .perf-body  { color: #4a3f70 !important; }

    /* Score pill (sidebar) */
    .score-pill { background: rgba(109,40,217,0.07) !important; border-color: rgba(109,40,217,0.2) !important; color: #3d2f7e !important; }
    .score-pill .pill-val { color: #5b21b6 !important; }

    /* Sidebar labels & divider */
    .sb-label { color: #5a4f80 !important; }
    .sb-divider { background: linear-gradient(90deg,transparent,rgba(109,40,217,0.2),transparent) !important; }

    /* Weight chips */
    .weight-chip { background: rgba(109,40,217,0.07) !important; border-color: rgba(109,40,217,0.18) !important; color: #3d2f7e !important; }
    .weight-chip .wc-pct { color: #5b21b6 !important; }

    /* Grade rows */
    .grade-row { background: rgba(255,255,255,0.85) !important; border-color: rgba(109,40,217,0.1) !important; }
    .grade-row:hover { background: rgba(109,40,217,0.05) !important; border-color: rgba(109,40,217,0.2) !important; }
    .grade-row .gr-range { color: #5a4f80 !important; }
    .grade-row .gr-gpa   { color: #7060a0 !important; }

    /* Formula */
    .formula-outer { background: rgba(255,255,255,0.92) !important; border-color: rgba(109,40,217,0.13) !important; }
    .formula-header { background: linear-gradient(90deg,rgba(109,40,217,0.07),rgba(37,99,235,0.04)) !important; color: #4a3f70 !important; border-bottom-color: rgba(109,40,217,0.12) !important; }
    .formula-block { background: rgba(238,235,255,0.65) !important; border-color: rgba(109,40,217,0.12) !important; color: #2d1f5e !important; }
    .formula-block .fb-title { color: #5a4f80 !important; }
    .formula-block .fb-eq   { color: #065f46 !important; }
    .formula-block .fb-eq-b { color: #1e40af !important; }
    .formula-block .fb-eq-c { color: #92400e !important; }

    /* Opening card */
    .open-card {
        background: rgba(255,255,255,0.97) !important;
        border-color: rgba(109,40,217,0.2) !important;
        box-shadow: 0 24px 80px rgba(109,40,217,0.09), 0 4px 16px rgba(0,0,0,0.05) !important;
    }
    .open-title {
        background: linear-gradient(100deg,#5b21b6 0%,#4f46e5 45%,#0369a1 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .open-subtitle { color: #3d2f7e !important; }
    .open-desc     { color: #5a4f80 !important; }
    .open-chip { background: rgba(109,40,217,0.07) !important; border-color: rgba(109,40,217,0.18) !important; color: #3d2f7e !important; }
    .open-creator { background: rgba(109,40,217,0.05) !important; color: #5a4f80 !important; }
    .open-creator strong { color: #5b21b6 !important; }
    .open-divider { background: linear-gradient(90deg,transparent,rgba(109,40,217,0.22),transparent) !important; }
    .open-team-block { background: rgba(109,40,217,0.05) !important; border-color: rgba(109,40,217,0.15) !important; }
    .open-team-label { color: #5a4f80 !important; }
    .open-member { color: #3d2f7e !important; }
    .member-id { color: #8b7db5 !important; }
    .footer-team-credit { color: #3d2f7e !important; }
    .footer-team-credit strong { color: #5b21b6 !important; }
    .footer-members { color: #7060a0 !important; }

    /* Footer */
    .footer-title { color: #3d2f7e !important; }
    .footer-sub   { color: #7060a0 !important; }
    .footer-badge { background: rgba(109,40,217,0.07) !important; color: #4a3f70 !important; }

    /* Generic text */
    p, li { color: #4a3f70 !important; }
    h1, h2, h3, h4, h5 { color: #1a1535 !important; }

    /* Native Streamlit input overrides */
    [data-testid="stNumberInput"] input {
        background: rgba(255,255,255,0.92) !important;
        color: #1a1535 !important;
        border-color: rgba(109,40,217,0.25) !important;
    }

    /* Section utilities */
    .section-card { background: rgba(255,255,255,0.85) !important; border-color: rgba(109,40,217,0.1) !important; }
    .chart-bg     { background: rgba(255,255,255,0.8)  !important; border-color: rgba(109,40,217,0.1) !important; }
    </style>
    """, unsafe_allow_html=True)


WEIGHTS = {
    "Assignments": 0.10,
    "Midterm Exam": 0.30,
    "Final Exam":   0.40,
    "Attendance":   0.20,
}

# 4.5 GPA scale — 9 grades
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

# CSS-safe grade name: '+' is not a valid CSS identifier character.
_GRADE_CSS = {
    "A+": "Ap", "A": "A",
    "B+": "Bp", "B": "B",
    "C+": "Cp", "C": "C",
    "D+": "Dp", "D": "D",
    "F":  "F",  "—": "F",
}

def score_to_grade(score: float):
    """Return (letter, gpa) using >= low matching to handle float boundary scores correctly."""
    for low, high, letter, gpa in GRADE_SCALE:
        if score >= low:
            return letter, gpa
    return "F", 0.0

def performance_comment(score: float, has_final: bool, required: float = None):
    """Returns (icon, title, body, box_class)."""
    if has_final:
        if score >= 90:
            return ("🏆", "Outstanding!", "You've achieved an excellent score. Keep up the remarkable work — you're a top performer!", "perf-success")
        elif score >= 80:
            return ("✅", "Great Job!", "You're in a strong position. A little extra push and you can reach the top grade!", "perf-success")
        elif score >= 70:
            return ("📘", "Satisfactory", "You're passing, but there's meaningful room to grow. Focus on weaker areas in your next course.", "perf-info")
        elif score >= 60:
            return ("⚠️", "Just Passing", "This grade meets the minimum threshold. Consider seeking additional support or study resources.", "perf-warn")
        else:
            return ("❌", "Below Passing", "This score does not meet the minimum requirement. Consider speaking with your advisor about your options.", "perf-danger")
    else:
        if required is None:
            return ("📊", "Awaiting Input", "Enter your scores to see your prediction.", "perf-info")
        if required < 0:
            return ("🎉", "Already Secured!", "You've already secured your target score regardless of final exam performance!", "perf-success")
        elif required <= 60:
            return ("✅", "On Track!", "You only need a modest final exam score to reach your target. Stay focused!", "perf-success")
        elif required <= 80:
            return ("📘", "Achievable", "You need a solid final exam performance. Dedicate focused study time to key topics.", "perf-info")
        elif required <= 100:
            return ("⚠️", "Challenging Target", "You need a very high final exam score. Consider whether your target score is realistic.", "perf-warn")
        else:
            return ("❌", "Target Not Achievable", "Even a perfect final exam score cannot reach your target. Try lowering your goal.", "perf-danger")

def make_bar_chart(components: dict, colors: list):
    labels = list(components.keys())
    values = list(components.values())
    max_val = max(max(values), 1)
    n = len(labels)

    fig, ax = plt.subplots(figsize=(8, max(2.8, n * 0.78)))
    fig.patch.set_facecolor("#0b0a1a")
    ax.set_facecolor("#0d0b1f")

    y_pos = np.arange(n)
    bar_h = 0.48

    # Background track
    ax.barh(y_pos, [max_val * 1.15] * n, height=bar_h,
            color="#1a1535", zorder=1, left=0)

    # Gradient-style bars (simulate with solid + alpha overlay)
    for i, (val, color) in enumerate(zip(values, colors)):
        ax.barh(y_pos[i], val, height=bar_h,
                color=color, alpha=0.88, zorder=3, left=0,
                linewidth=0)
        # Highlight strip on top
        strip_bottom = y_pos[i] + bar_h * 0.37
        ax.barh(strip_bottom, val, height=bar_h * 0.25,
                color="#ffffff", alpha=0.10, zorder=4)
        # Value label
        ax.text(val + max_val * 0.02, y_pos[i],
                f"{val:.1f} pts",
                va="center", ha="left",
                color="#e0d8ff", fontsize=9.5, fontweight="700",
                fontfamily="sans-serif")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color="#c4b5fd", fontsize=10, fontweight="600")
    ax.set_xlim(0, max_val * 1.35)
    ax.set_xlabel("Weighted Contribution (points)", color="#5a4f80", fontsize=8.5, labelpad=8)
    ax.tick_params(axis="x", colors="#4a3f70", labelsize=8)
    ax.tick_params(axis="y", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.xaxis.grid(True, color="#1e1a38", linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)

    # Colour legend dots
    patches = [mpatches.Patch(color=c, label=l) for l, c in zip(labels, colors)]
    ax.legend(handles=patches, loc="lower right",
              framealpha=0, labelcolor="#9d8ec4", fontsize=7.5,
              handlelength=1, handleheight=0.8)

    ax.set_title("Weighted Score Breakdown", color="#c4b5fd",
                 fontsize=11, fontweight="700", pad=14, loc="left")
    plt.tight_layout(pad=1.2)
    return fig

def make_donut(sizes, labels, colors):
    fig, ax = plt.subplots(figsize=(4, 4))
    fig.patch.set_facecolor("#0b0a1a")
    ax.set_facecolor("#0b0a1a")

    wedges, texts, autotexts = ax.pie(
        sizes, labels=None, colors=colors,
        autopct="%1.0f%%", startangle=120,
        pctdistance=0.72,
        wedgeprops={"edgecolor": "#0b0a1a", "linewidth": 3, "width": 0.55},
        textprops={"color": "#c4b5fd", "fontsize": 8},
    )
    for at in autotexts:
        at.set_color("#ffffff"); at.set_fontweight("700"); at.set_fontsize(8)

    # Centre label
    ax.text(0, 0, f"{sum(sizes):.1f}", ha="center", va="center",
            fontsize=17, fontweight="800", color="#f0eeff")
    ax.text(0, -0.22, "pts total", ha="center", va="center",
            fontsize=7.5, color="#7c6fa0")

    patches = [mpatches.Patch(color=c, label=l) for c, l in zip(colors, labels)]
    ax.legend(handles=patches, loc="lower center", bbox_to_anchor=(0.5, -0.14),
              ncol=2, framealpha=0, labelcolor="#9d8ec4", fontsize=7.5,
              handlelength=1)

    ax.set_title("Score Composition", color="#c4b5fd",
                 fontsize=11, fontweight="700", pad=10)
    plt.tight_layout(pad=0.8)
    return fig

def make_gauge(required_final):
    clamped = max(0, min(100, required_final))
    danger  = required_final > 85

    fig, ax = plt.subplots(figsize=(5, 2.2))
    fig.patch.set_facecolor("#0b0a1a")
    ax.set_facecolor("#0d0b1f")

    # Background track
    ax.barh([0], [100], height=0.55, color="#1a1535", zorder=1)
    # Filled bar
    bar_color = "#f87171" if danger else "#818cf8"
    ax.barh([0], [clamped], height=0.55, color=bar_color, alpha=0.9, zorder=3)
    # Bright edge cap
    if clamped > 2:
        ax.barh([0], [min(clamped, 3)], height=0.55,
                color="#ffffff", alpha=0.2, zorder=4, left=max(0, clamped - 3))

    label_text = f"{required_final:.1f} / 100" if required_final <= 100 else "Impossible (> 100)"
    ax.text(50, 0, label_text,
            ha="center", va="center",
            color="#ffffff", fontsize=11, fontweight="800", zorder=5)

    ax.set_xlim(0, 100)
    ax.set_ylim(-0.7, 0.7)
    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.tick_params(axis="x", colors="#4a3f70", labelsize=7.5)
    for spine in ax.spines.values(): spine.set_visible(False)
    ax.set_xlabel("Score needed out of 100", color="#4a3f70", fontsize=8, labelpad=6)
    ax.set_title("Final Exam Score Required", color="#c4b5fd",
                 fontsize=11, fontweight="700", pad=12, loc="left")
    plt.tight_layout(pad=1.0)
    return fig

def _load_demo_case_1():
    """Load the primary demo: prediction mode, 10/30/40/20 weights."""
    st.session_state.assignment_score = 85
    st.session_state.midterm_score    = 75
    st.session_state.total_classes    = 16
    st.session_state.max_allowed_missed = 5
    st.session_state.missed_classes   = 1
    st.session_state.has_final        = False
    st.session_state.target_score     = 80
    # Weights reset to canonical demo values
    st.session_state.w_assignment  = 10
    st.session_state.w_midterm     = 30
    st.session_state.w_final       = 40
    st.session_state.w_attendance  = 20


def _load_demo_case_2():
    """Load the secondary demo: final exam available, 10/30/40/20 weights."""
    st.session_state.assignment_score = 85
    st.session_state.midterm_score    = 75
    st.session_state.total_classes    = 16
    st.session_state.max_allowed_missed = 5
    st.session_state.missed_classes   = 1
    st.session_state.has_final        = True
    st.session_state.final_score      = 80
    # Weights reset to canonical demo values
    st.session_state.w_assignment  = 10
    st.session_state.w_midterm     = 30
    st.session_state.w_final       = 40
    st.session_state.w_attendance  = 20


# ──────────────────────────────────────────────────────────────────────────────
# OPENING PAGE  (shown first; dashboard renders only after Start is clicked)
# ──────────────────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "start"

if st.session_state.page == "start":
    # Compact theme toggle — top of opening page
    _op_t1, _op_t2, _op_t3 = st.columns([3, 2, 3])
    with _op_t2:
        _op_theme_choice = st.radio(
            "Theme", ["🌙 Dark", "☀️ Light"],
            index=0 if _dark else 1,
            horizontal=True,
            label_visibility="collapsed",
            key="op_theme_radio",
        )
        _op_want_dark = (_op_theme_choice == "🌙 Dark")
        if _op_want_dark != _dark:
            st.session_state.theme = "dark" if _op_want_dark else "light"
            st.rerun()
    st.markdown("""
    <div class='open-page-bg'>
    <div class='open-card'>
        <div class='open-emoji'>🎓</div>
        <div class='open-title'>Smart GPA Calculator<br>and Prediction System</div>
        <div class='open-subtitle'>
            A public academic performance dashboard for GPA calculation
            and final exam score prediction.
        </div>
        <div class='open-divider'></div>
        <div class='open-desc'>
            The system helps students calculate their current academic standing,
            estimate the required final exam score, and understand their
            performance visually.
        </div>
        <div class='open-features'>
            <div class='open-chip'>📊 GPA Calculation</div>
            <div class='open-chip'>🔮 Required Final Exam Prediction</div>
            <div class='open-chip'>🏅 Grade &amp; GPA Conversion</div>
            <div class='open-chip'>📈 Visual Charts</div>
            <div class='open-chip'>🌐 Public Web Access</div>
        </div>
        <div class='open-team-block'>
            <div class='open-team-label'>Created by Team WebForge</div>
            <div class='open-team-members'>
                <span class='open-member'>Muhammad Saad <span class='member-id'>| 202512370</span></span>
                <span class='open-member'>Parneet Kaur <span class='member-id'>| 202612034</span></span>
                <span class='open-member'>Abdimazhitova Aikol <span class='member-id'>| 202601019</span></span>
                <span class='open-member'>Nasriddinov Mukhammadzokhir <span class='member-id'>| 202412350</span></span>
            </div>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    _oc1, _oc2, _oc3 = st.columns([1.3, 2, 1.3])
    with _oc2:
        if st.button("🚀 Start Calculation", key="open_start_btn", use_container_width=True):
            st.session_state.page = "main"
            st.rerun()
    st.stop()   # ← prevents sidebar and dashboard from rendering on the start page

# ──────────────────────────────────────────────────────────────────────────────
# SIDEBAR — INPUTS
# ──────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    # ← Home link
    if st.button("← Home", key="sidebar_home_btn", help="Return to the opening page"):
        st.session_state.page = "start"
        st.rerun()
    st.markdown("<div class='sb-divider' style='margin-top:4px;'></div>", unsafe_allow_html=True)

    # Theme toggle
    st.markdown("<div class='sb-label'>🎨 Theme</div>", unsafe_allow_html=True)
    _sb_theme_choice = st.radio(
        "Theme", ["🌙 Dark Mode", "☀️ Light Mode"],
        index=0 if _dark else 1,
        horizontal=True,
        label_visibility="collapsed",
        key="sb_theme_radio",
    )
    _sb_want_dark = (_sb_theme_choice == "🌙 Dark Mode")
    if _sb_want_dark != _dark:
        st.session_state.theme = "dark" if _sb_want_dark else "light"
        st.rerun()
    st.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)

    # Logo &amp; title
    st.markdown(f"""
    <div style='padding:20px 4px 10px; text-align:center;'>
        <div style='font-size:3.2rem; line-height:1; margin-bottom:10px;'>🎓</div>
        <div style='font-size:0.95rem; font-weight:800; color:#c4b5fd;
                    letter-spacing:0.02em; line-height:1.35;'>
            Smart GPA Calculator
        </div>
        <div style='font-size:0.7rem; color:#5a4f80; margin-top:4px; letter-spacing:0.05em;'>
            and Prediction System
        </div>
    </div>
    <div class='sb-divider'></div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='sb-label'>📸 Demo Cases</div>", unsafe_allow_html=True)
    d1, d2 = st.columns(2)
    with d1:
        if st.button(
            "Load Demo Case",
            key="demo_case_1_btn",
            help="Prediction mode — Assignment 85, Midterm 75, 1/16 missed, Target 80, Weights 10/30/40/20",
            use_container_width=True,
        ):
            _load_demo_case_1()
            st.rerun()
    with d2:
        if st.button(
            "With Final Exam",
            key="demo_case_2_btn",
            help="Final exam available — Final 80, Grade B, GPA 3.0",
            use_container_width=True,
        ):
            _load_demo_case_2()
            st.rerun()
    st.markdown("""
    <div style='font-size:0.7rem; color:#5a4f80; line-height:1.6;
                padding:6px 10px; margin:6px 0 2px;
                background:rgba(139,92,246,0.06); border-radius:8px;
                border-left:2px solid rgba(139,92,246,0.3);'>
        <b style='color:#9d8ec4;'>Demo:</b> Assignment&nbsp;85, Midterm&nbsp;75,
        1&nbsp;missed&nbsp;out&nbsp;of&nbsp;16, Target&nbsp;80, Weights&nbsp;10/30/40/20
    </div>""", unsafe_allow_html=True)
    st.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)

    # ── Score Inputs ──
    st.markdown("<div class='sb-label'>📋 Score Inputs</div>", unsafe_allow_html=True)

    assignment_score = st.slider("Assignment Score", 0, 100, 85, 1,
                                  key="assignment_score",
                                  help="Your assignment score (0–100)")
    st.markdown(f"""<div class='score-pill'>
        <span>📝 Assignment <small style='opacity:.6;'>(10%)</small></span>
        <span class='pill-val'>{assignment_score}</span>
    </div>""", unsafe_allow_html=True)

    midterm_score = st.slider("Midterm Exam Score", 0, 100, 75, 1,
                               key="midterm_score",
                               help="Your midterm exam score (0–100)")
    st.markdown(f"""<div class='score-pill'>
        <span>📖 Midterm <small style='opacity:.6;'>(30%)</small></span>
        <span class='pill-val'>{midterm_score}</span>
    </div>""", unsafe_allow_html=True)

    # ── Attendance Tracking (auto-calculated) ──
    st.markdown("""<div style='font-size:0.74rem; color:#6d5d9e; margin:8px 0 10px 2px; line-height:1.55;'>
        📌 Attendance score is calculated automatically from total classes and missed classes.
    </div>""", unsafe_allow_html=True)

    total_classes = st.number_input("Total Classes", min_value=1, max_value=200,
                                     value=16, step=1, key="total_classes")
    _tc = int(total_classes)
    # Clamp dependent session-state values if total_classes was reduced
    if st.session_state.get("max_allowed_missed", 5) > _tc:
        st.session_state["max_allowed_missed"] = _tc
    if st.session_state.get("missed_classes", 0) > _tc:
        st.session_state["missed_classes"] = _tc

    max_allowed_missed = st.number_input("Maximum Allowed Missed Classes",
                                          min_value=0, max_value=_tc,
                                          value=min(5, _tc), step=1,
                                          key="max_allowed_missed")
    missed_classes = st.number_input("Number of Missed Classes",
                                      min_value=0, max_value=_tc,
                                      value=0, step=1,
                                      key="missed_classes")

    # Auto-calculate attendance score and eligibility
    attendance_score  = ((total_classes - missed_classes) / total_classes) * 100
    attendance_failed = int(missed_classes) > int(max_allowed_missed)

    # Colour-coded attendance score pill
    _att_border = "rgba(239,68,68,0.45)" if attendance_failed else "rgba(52,211,153,0.35)"
    _att_bg     = "rgba(239,68,68,0.08)"  if attendance_failed else "rgba(52,211,153,0.08)"
    _att_col    = "#f87171" if attendance_failed else "#34d399"
    st.markdown(f"""<div class='score-pill' style='border-color:{_att_border};background:{_att_bg};'>
        <span>📅 Attendance <small style='opacity:.6;'>(20%)</small></span>
        <span class='pill-val' style='color:{_att_col};'>{attendance_score:.2f}%</span>
    </div>""", unsafe_allow_html=True)

    # Attendance status + policy note
    _status_text = "❌ Failed — Attendance Policy" if attendance_failed else "✅ Eligible"
    st.markdown(f"""<div style='font-size:0.74rem; padding:7px 12px; border-radius:8px;
                    background:{"rgba(239,68,68,0.1)" if attendance_failed else "rgba(52,211,153,0.1)"};
                    border:1px solid {"rgba(239,68,68,0.25)" if attendance_failed else "rgba(52,211,153,0.25)"};
                    color:{_att_col}; margin:4px 0 4px;'>
        <b>Attendance Status:</b> {_status_text}<br>
        <span style='opacity:0.75; font-size:0.7rem;'>
            📌 Policy: &gt;{int(max_allowed_missed)} missed class(es) = automatic grade F.
        </span>
    </div>""", unsafe_allow_html=True)

    st.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)

    # ── Final Exam ──
    st.markdown("<div class='sb-label'>🎯 Final Exam</div>", unsafe_allow_html=True)
    has_final = st.checkbox("Final exam score is available", value=False, key="has_final")

    if has_final:
        final_score = st.slider("Final Exam Score", 0, 100, 80, 1,
                                 key="final_score",
                                 help="Your final exam score (0–100)")
        st.markdown(f"""<div class='score-pill' style='border-color:rgba(244,114,182,0.35);
                         background:rgba(244,114,182,0.08);'>
            <span>📝 Final Exam <small style='opacity:.6;'>(40%)</small></span>
            <span class='pill-val' style='color:#f472b6;'>{final_score}</span>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)
        st.markdown("<div class='sb-label'>🔮 Prediction Mode</div>", unsafe_allow_html=True)
        target_score = st.slider("Target Overall Score", 0, 100, 80, 1,
                                  key="target_score",
                                  help="The overall score you want to achieve (0–100)")
        st.markdown(f"""<div class='score-pill' style='border-color:rgba(99,102,241,0.35);
                         background:rgba(99,102,241,0.08);'>
            <span>🎯 Target Score</span>
            <span class='pill-val' style='color:#818cf8;'>{target_score}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)

    # ── Grading Weight Settings ──
    st.markdown("<div class='sb-label'>⚖️ Grading Weight Settings</div>", unsafe_allow_html=True)
    st.markdown("""<div style='font-size:0.74rem; color:#6d5d9e; margin:0 0 10px 2px; line-height:1.55;'>
        Adjust the weight of each component. Total must equal 100%.
    </div>""", unsafe_allow_html=True)

    w_assignment = st.number_input("Assignment Weight (%)", min_value=0, max_value=100,
                                    value=10, step=1, key="w_assignment")
    w_midterm    = st.number_input("Midterm Weight (%)",    min_value=0, max_value=100,
                                    value=30, step=1, key="w_midterm")
    w_final      = st.number_input("Final Exam Weight (%)", min_value=0, max_value=100,
                                    value=40, step=1, key="w_final")
    w_attendance = st.number_input("Attendance Weight (%)", min_value=0, max_value=100,
                                    value=20, step=1, key="w_attendance")

    total_weight  = int(w_assignment) + int(w_midterm) + int(w_final) + int(w_attendance)
    weights_valid = (total_weight == 100)

    _wt_col = "#f87171" if not weights_valid else "#34d399"
    st.markdown(f"""<div style='font-size:0.74rem; padding:7px 12px; border-radius:8px;
                    background:{"rgba(239,68,68,0.1)" if not weights_valid else "rgba(52,211,153,0.1)"};
                    border:1px solid {"rgba(239,68,68,0.25)" if not weights_valid else "rgba(52,211,153,0.25)"};
                    color:{_wt_col}; margin:6px 0 4px;'>
        <b>Total Weight:</b> {total_weight}%
        {"&nbsp;&nbsp;✅ Valid" if weights_valid else "&nbsp;&nbsp;⚠️ Must equal 100%"}
    </div>""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# CALCULATIONS
# attendance_score / attendance_failed computed in sidebar.
# w_assignment / w_midterm / w_final / w_attendance are the live custom weights (%).
# ──────────────────────────────────────────────────────────────────────────────
_wa  = w_assignment / 100
_wm  = w_midterm    / 100
_wf  = w_final      / 100
_watt = w_attendance / 100

if not weights_valid:
    # Invalid weights — skip all calculations to avoid misleading results
    assignment_contrib   = 0.0
    midterm_contrib      = 0.0
    attendance_contrib   = 0.0
    current_contribution = 0.0
    final_contrib        = None
    overall_score        = None
    grade, gpa           = "—", 0.0
    required_final       = None
    prediction_mode      = not has_final
else:
    assignment_contrib   = assignment_score  * _wa
    midterm_contrib      = midterm_score     * _wm
    attendance_contrib   = attendance_score  * _watt
    current_contribution = assignment_contrib + midterm_contrib + attendance_contrib

    if attendance_failed:
        # Attendance policy failure — override all grade/score results
        final_contrib   = (final_score * _wf) if has_final else None
        overall_score   = None
        grade, gpa      = "F", 0.0
        required_final  = None
        prediction_mode = not has_final
    elif has_final:
        final_contrib   = final_score * _wf
        overall_score   = current_contribution + final_contrib
        grade, gpa      = score_to_grade(overall_score)
        required_final  = None
        prediction_mode = False
    else:
        final_contrib   = None
        overall_score   = None
        if _wf == 0:
            # Cannot divide by zero — treat as unachievable
            required_final = float('inf')
        else:
            required_final = (target_score - current_contribution) / _wf
        prediction_mode = True
        if 0 <= required_final <= 100:
            grade, gpa = score_to_grade(target_score)
        elif required_final < 0:
            grade, gpa = score_to_grade(current_contribution)
        else:
            grade, gpa = "F", 0.0

# ──────────────────────────────────────────────────────────────────────────────
# MAIN DASHBOARD
# ──────────────────────────────────────────────────────────────────────────────

# ── Hero ─────────────────────────────────────────────────────────────────────
mode_badge = (
    '<span style="background:rgba(244,114,182,0.15);border:1px solid rgba(244,114,182,0.3);'
    'color:#f472b6;font-size:0.7rem;font-weight:700;letter-spacing:0.08em;'
    'padding:3px 12px;border-radius:20px;">✓ FINAL SCORE MODE</span>'
    if has_final else
    '<span style="background:rgba(99,102,241,0.15);border:1px solid rgba(99,102,241,0.3);'
    'color:#818cf8;font-size:0.7rem;font-weight:700;letter-spacing:0.08em;'
    'padding:3px 12px;border-radius:20px;">🔮 PREDICTION MODE</span>'
)
st.markdown(f"""
<div style='padding:36px 0 28px; text-align:center;'>
    <div style='margin-bottom:14px;'>{mode_badge}</div>
    <h1 style='font-size:2.1rem; font-weight:900; margin:0; line-height:1.2;
               background:linear-gradient(100deg,#c4b5fd 0%,#818cf8 40%,#67e8f9 100%);
               -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
        Smart GPA Calculator and Prediction System
    </h1>
    <p style='color:#4a3f70; font-size:0.88rem; margin-top:10px; letter-spacing:0.04em;'>
        University academic dashboard &nbsp;·&nbsp; Weighted scores &nbsp;·&nbsp; Grade &amp; GPA
    </p>
</div>
""", unsafe_allow_html=True)

# ── Metric Cards ─────────────────────────────────────────────────────────────
# Inject per-card accent top-border via nth-child trick
card_accent_css = """
<style>
/* Card 1 – purple */
div[data-testid="column"]:nth-child(1) div[data-testid="metric-container"] {
    border-top: 3px solid #a78bfa;
}
/* Card 2 – blue / pink */
div[data-testid="column"]:nth-child(2) div[data-testid="metric-container"] {
    border-top: 3px solid #60a5fa;
}
/* Card 3 – green */
div[data-testid="column"]:nth-child(3) div[data-testid="metric-container"] {
    border-top: 3px solid #34d399;
}
/* Card 4 – yellow */
div[data-testid="column"]:nth-child(4) div[data-testid="metric-container"] {
    border-top: 3px solid #fbbf24;
}
</style>
"""
st.markdown(card_accent_css, unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    _cc_disp = f"{current_contribution:.2f}" if weights_valid else "—"
    st.metric("📋 Current Contribution", _cc_disp,
              help=f"Assignment×{w_assignment}% + Midterm×{w_midterm}% + Attendance×{w_attendance}%")
with c2:
    if has_final:
        if not weights_valid:
            _disp2 = "—"
        elif attendance_failed:
            _disp2 = "N/A (Attendance Fail)"
        else:
            _disp2 = f"{overall_score:.2f}"
        st.metric("🏁 Final Score", _disp2,
                  help=f"Assignment×{w_assignment}% + Midterm×{w_midterm}% + Final×{w_final}% + Attendance×{w_attendance}%")
    else:
        if not weights_valid:
            _disp_rf = "—"
        elif required_final is not None and required_final != float('inf'):
            _disp_rf = f"{required_final:.2f}"
        else:
            _disp_rf = "—"
        st.metric("🎯 Required Final Exam", _disp_rf,
                  help="Final exam score needed to hit your target")
with c3:
    st.metric("📊 Grade", grade, help="Letter grade based on your score")
with c4:
    st.metric("⭐ GPA Points", f"{gpa:.1f}", help="GPA on a 4.0 scale")

st.markdown("<br>", unsafe_allow_html=True)

# ── Weight Validation Warning ─────────────────────────────────────────────────
if not weights_valid:
    st.markdown(f"""
    <div class='perf-box perf-warn' style='margin-bottom:16px;'>
        <div class='perf-icon'>⚖️</div>
        <div class='perf-content'>
            <div class='perf-title'>Invalid Grading Weights</div>
            <div class='perf-body'>
                The total grading weight must be <b>100%</b>, but the current total is
                <b>{total_weight}%</b> ({'+' if total_weight > 100 else ''}{total_weight - 100}%).
                <br><br>
                Please adjust the weights in the sidebar until the total equals 100%.
                Calculations are paused to avoid misleading results.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Attendance Status Banner ───────────────────────────────────────────────────
if attendance_failed:
    st.markdown(f"""
    <div class='perf-box perf-danger' style='margin-bottom:16px;'>
        <div class='perf-icon'>🚫</div>
        <div class='perf-content'>
            <div class='perf-title'>Attendance Policy Failure</div>
            <div class='perf-body'>
                You missed <b>{int(missed_classes)}</b> out of <b>{int(total_classes)}</b> classes,
                exceeding the maximum allowed limit of <b>{int(max_allowed_missed)}</b> missed class(es).
                <br><br>
                Per attendance policy, your grade is automatically set to <b>F</b> (GPA&nbsp;0.0)
                regardless of exam scores. The required final exam score is not applicable.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Final Weight = 0 with no final available ───────────────────────────────────
if weights_valid and not has_final and not attendance_failed and w_final == 0:
    st.markdown("""
    <div class='perf-box perf-warn' style='margin-bottom:16px;'>
        <div class='perf-icon'>⚠️</div>
        <div class='perf-content'>
            <div class='perf-title'>Final Exam Weight is 0%</div>
            <div class='perf-body'>
                Required final exam score cannot be calculated because the Final Exam Weight is 0%.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Grade + Performance Comment ───────────────────────────────────────────────
left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
    st.markdown("<div class='sec-hdr'><span>🏅</span> Grade Result</div>",
                unsafe_allow_html=True)
    if not weights_valid:
        score_line = "Weights: <b>Invalid (must total 100%)</b>"
    elif attendance_failed:
        score_line = "Attendance: <b>Policy Failure</b>"
    elif has_final:
        score_line = f"Final Score: <b>{overall_score:.2f}</b>"
    else:
        score_line = f"Target Score: <b>{target_score}</b>"
    st.markdown(f"""
    <div class='grade-wrap'>
        <div class='grade-letter grade-{_GRADE_CSS.get(grade, "F")}' style='{'opacity:0.35;' if not weights_valid else ''}'>{grade}</div>
        <div class='grade-gpa'>GPA &nbsp;<strong>{gpa:.1f}</strong> / 4.5</div>
        <div class='grade-sub'>{score_line}</div>
    </div>
    """, unsafe_allow_html=True)

with right_col:
    st.markdown("<div class='sec-hdr'><span>💡</span> Smart Performance Insight</div>",
                unsafe_allow_html=True)
    if not weights_valid:
        icon, title, body, box_cls = (
            "⚖️",
            "Invalid Grading Weights",
            "Adjust the weights in the sidebar so they total <b>100%</b> to see your results.",
            "perf-warn",
        )
    elif attendance_failed:
        icon, title, body, box_cls = (
            "🚫",
            "Attendance Policy Failure",
            "Your grade is <b>F</b> (GPA 0.0) due to exceeding the maximum allowed "
            "missed classes. Contact your academic advisor for options.",
            "perf-danger",
        )
    else:
        icon, title, body, box_cls = performance_comment(
            score=overall_score if has_final else current_contribution,
            has_final=has_final,
            required=required_final,
        )
    st.markdown(f"""
    <div class='perf-box {box_cls}'>
        <div class='perf-icon'>{icon}</div>
        <div class='perf-content'>
            <div class='perf-title'>{title}</div>
            <div class='perf-body'>{body}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='sec-hdr'><span>📐</span> Score Breakdown</div>",
                unsafe_allow_html=True)
    rows = {
        "Component":    ["📝 Assignment", "📖 Midterm Exam", "📅 Attendance",
                         "📝 Final Exam" if has_final else "📝 Final Exam (pending)"],
        "Raw Score":    [str(assignment_score), str(midterm_score),
                         f"{attendance_score:.2f}%",
                         str(final_score) if has_final else "—"],
        "Weight":       [f"{w_assignment}%", f"{w_midterm}%",
                         f"{w_attendance}%", f"{w_final}%"],
        "Contribution": [f"{assignment_contrib:.2f}", f"{midterm_contrib:.2f}",
                         f"{attendance_contrib:.2f}",
                         f"{final_contrib:.2f}" if (has_final and final_contrib is not None) else "—"],
    }
    # astype(str) ensures every column is object dtype — prevents PyArrow int64 inference
    st.dataframe(pd.DataFrame(rows).astype(str), hide_index=True, width="stretch")

st.markdown("<br>", unsafe_allow_html=True)

# ── Chart + Donut / Gauge ─────────────────────────────────────────────────────
chart_col, viz_col = st.columns([3, 2], gap="large")

with chart_col:
    st.markdown("<div class='sec-hdr'><span>📊</span> Weighted Score Chart</div>",
                unsafe_allow_html=True)
    if has_final:
        components = {"Assignments": assignment_contrib, "Midterm Exam": midterm_contrib,
                      "Attendance": attendance_contrib, "Final Exam": final_contrib}
        bar_colors = ["#a78bfa", "#60a5fa", "#34d399", "#f472b6"]
    else:
        components = {"Assignments": assignment_contrib, "Midterm Exam": midterm_contrib,
                      "Attendance": attendance_contrib}
        bar_colors = ["#a78bfa", "#60a5fa", "#34d399"]
    st.pyplot(make_bar_chart(components, bar_colors))

with viz_col:
    st.markdown("<div class='sec-hdr'><span>🔬</span> Score Analysis</div>",
                unsafe_allow_html=True)
    if has_final:
        sizes  = [assignment_contrib, midterm_contrib, attendance_contrib, final_contrib]
        labels = [f"Assignment ({w_assignment}%)", f"Midterm ({w_midterm}%)",
                  f"Attendance ({w_attendance}%)", f"Final ({w_final}%)"]
        colors = ["#a78bfa", "#60a5fa", "#34d399", "#f472b6"]
        st.pyplot(make_donut(sizes, labels, colors))
    else:
        if not weights_valid:
            st.markdown("""<div class='perf-box perf-warn' style='padding:14px 16px;'>
                <div class='perf-icon' style='font-size:1.4rem;'>⚖️</div>
                <div class='perf-content'>
                    <div class='perf-body'>Required final exam score is <b>not shown</b> — please fix the grading weights first.</div>
                </div></div>""", unsafe_allow_html=True)
        elif attendance_failed:
            st.markdown("""<div class='perf-box perf-danger' style='padding:14px 16px;'>
                <div class='perf-icon' style='font-size:1.4rem;'>🚫</div>
                <div class='perf-content'>
                    <div class='perf-body'>Required final exam score is <b>not applicable</b> — grade is F due to attendance policy failure.</div>
                </div></div>""", unsafe_allow_html=True)
        elif w_final == 0:
            st.markdown("""<div class='perf-box perf-warn' style='padding:14px 16px;'>
                <div class='perf-icon' style='font-size:1.4rem;'>⚠️</div>
                <div class='perf-content'>
                    <div class='perf-body'>Required final exam score <b>cannot be calculated</b> — Final Exam Weight is 0%.</div>
                </div></div>""", unsafe_allow_html=True)
        else:
            st.pyplot(make_gauge(required_final))

            if required_final < 0:
                st.markdown("""<div class='perf-box perf-success' style='padding:14px 16px; margin-top:10px;'>
                    <div class='perf-icon' style='font-size:1.4rem;'>🎉</div>
                    <div class='perf-content'>
                        <div class='perf-body'>You've <b>already secured</b> your target — any final exam score will do!</div>
                    </div></div>""", unsafe_allow_html=True)
            elif required_final <= 100:
                st.markdown(f"""<div class='perf-box perf-info' style='padding:14px 16px; margin-top:10px;'>
                    <div class='perf-icon' style='font-size:1.4rem;'>📌</div>
                    <div class='perf-content'>
                        <div class='perf-body'>Score at least <b>{required_final:.1f} / 100</b> on the final to reach target <b>{target_score}</b>.</div>
                    </div></div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div class='perf-box perf-danger' style='padding:14px 16px; margin-top:10px;'>
                    <div class='perf-icon' style='font-size:1.4rem;'>⚠️</div>
                    <div class='perf-content'>
                        <div class='perf-body'>Target <b>{target_score}</b> is unreachable even with a perfect final. Lower your target.</div>
                    </div></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Grading Scale ─────────────────────────────────────────────────────────────
st.markdown("<div class='sec-hdr'><span>📋</span> Grading Scale Reference</div>",
            unsafe_allow_html=True)

grade_rows = [
    ("95 – 100", "A+", "4.5", "Outstanding",  "Ap"),
    ("90 – 94",  "A",  "4.0", "Excellent",    "A"),
    ("85 – 89",  "B+", "3.5", "Very Good",    "Bp"),
    ("80 – 84",  "B",  "3.0", "Good",         "B"),
    ("75 – 79",  "C+", "2.5", "Above Average","Cp"),
    ("70 – 74",  "C",  "2.0", "Satisfactory", "C"),
    ("65 – 69",  "D+", "1.5", "Below Average","Dp"),
    ("60 – 64",  "D",  "1.0", "Passing",      "D"),
    ("Below 60", "F",  "0.0", "Failing",      "F"),
]
g1, g2 = st.columns(2, gap="medium")
for i, (rng, ltr, gp, meaning, tag) in enumerate(grade_rows):
    col = g1 if i < 5 else g2
    with col:
        st.markdown(f"""
        <div class='grade-row'>
            <span class='gr-letter grade-{tag}' style='border-radius:6px;padding:2px 8px;
                  font-size:1rem;display:inline-block;'>{ltr}</span>
            <span class='gr-range'>{rng}</span>
            <span class='gr-tag tag-{tag}'>{meaning}</span>
            <span class='gr-gpa'>GPA {gp}</span>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Formula Explanation ───────────────────────────────────────────────────────
st.markdown("<div class='sec-hdr'><span>🧮</span> Formula Explanation</div>",
            unsafe_allow_html=True)

f_left, f_right = st.columns(2, gap="medium")

with f_left:
    st.markdown(f"""
    <div class='formula-outer'>
        <div class='formula-header'>⚖️ &nbsp;Grading Weight Distribution</div>
        <div class='formula-body'>
            <div style='display:flex; flex-wrap:wrap; gap:4px; margin-bottom:14px;'>
                <div class='weight-chip'>📝 Assignment <span class='wc-pct'>{w_assignment}%</span></div>
                <div class='weight-chip'>📖 Midterm <span class='wc-pct'>{w_midterm}%</span></div>
                <div class='weight-chip'>📝 Final Exam <span class='wc-pct'>{w_final}%</span></div>
                <div class='weight-chip'>📅 Attendance <span class='wc-pct'>{w_attendance}%</span></div>
            </div>
            <div class='formula-block'>
                <div class='fb-title'>① When Final Exam IS available</div>
                <span class='fb-eq'>Final Score =</span><br>
                &nbsp;&nbsp;Assignment × {w_assignment/100:.2f}<br>
                &nbsp;+ Midterm × {w_midterm/100:.2f}<br>
                &nbsp;+ Final × {w_final/100:.2f}<br>
                &nbsp;+ Attendance × {w_attendance/100:.2f}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with f_right:
    st.markdown(f"""
    <div class='formula-outer'>
        <div class='formula-header'>🔮 &nbsp;Prediction Mode Formula</div>
        <div class='formula-body'>
            <div class='formula-block'>
                <div class='fb-title'>② When Final Exam is NOT available</div>
                <span class='fb-eq-b'>Current Contribution =</span><br>
                &nbsp;&nbsp;Assignment × {w_assignment/100:.2f}<br>
                &nbsp;+ Midterm × {w_midterm/100:.2f}<br>
                &nbsp;+ Attendance × {w_attendance/100:.2f}<br><br>
                <span class='fb-eq-c'>Required Final Exam =</span><br>
                &nbsp;&nbsp;(Target − Current Contribution) ÷ {w_final/100:.2f}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class='app-footer'>
    <div class='footer-title'>🎓 Smart GPA Calculator and Prediction System</div>
    <div class='footer-sub'>University Academic Performance Dashboard · v1.0</div>
    <div class='footer-team-credit'>Developed by <strong>Team WebForge</strong></div>
    <div class='footer-members'>
        Muhammad Saad | 202512370&nbsp;&nbsp;·&nbsp;&nbsp;
        Parneet Kaur | 202612034&nbsp;&nbsp;·&nbsp;&nbsp;
        Abdimazhitova Aikol | 202601019&nbsp;&nbsp;·&nbsp;&nbsp;
        Nasriddinov Mukhammadzokhir | 202412350
    </div>
    <div class='footer-badges'>
        <span class='footer-badge'>Python</span>
        <span class='footer-badge'>Streamlit</span>
        <span class='footer-badge'>Pandas</span>
        <span class='footer-badge'>Matplotlib</span>
    </div>
</div>
""", unsafe_allow_html=True)
