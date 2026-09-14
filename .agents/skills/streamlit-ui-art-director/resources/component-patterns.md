# Component Patterns
## Smart GPA Calculator — Streamlit UI Art Director Skill

Each pattern below specifies the component's purpose, the recommended
implementation method, and any CSS classes or HTML structures required.

Classification codes:
- **[NATIVE]** — standard `st.*` widget, no extra CSS needed
- **[CSS]** — `st.*` widget or `st.markdown()` + injected CSS
- **[OPTIONAL]** — possible via Streamlit + CSS but can be simplified
- **[NO]** — not recommended for this project

---

## 1. Opening Page — Hero Card

**Purpose**: First screen the user sees. Must communicate the tool's purpose,
establish academic credibility, present Team WebForge, and offer the single CTA.

**Classification**: [CSS]

**Structure**:
```
open-page-bg (full-viewport flex, centered)
  └── open-card (max-width 640px, centered)
        ├── open-emoji         🎓 (4rem)
        ├── open-title         H1, gradient text, 32px/900
        ├── open-subtitle      2–3 sentences, 16px/400, muted
        ├── open-divider       1px tinted rule
        ├── open-desc          14px/400, muted, max-width 520px
        ├── open-features      3-step flow chips: [📊 Scores]→[⚖️ Weights]→[🏅 Results]
        ├── [Start Calculation button — see #4]
        ├── open-divider
        └── open-team-block    [see #3]
```

**CSS classes required**: `open-page-bg`, `open-card`, `open-emoji`,
`open-title`, `open-subtitle`, `open-divider`, `open-desc`, `open-features`,
`open-chip`

**Rules**:
- Card background: `--bg-surface`
- Card border: `1px solid --border-subtle`
- Card radius: 24px
- Opening card entrance: `slideUp` animation, one-shot, wrapped in
  `@media (prefers-reduced-motion: no-preference)`
- No decorative radial gradients on the card pseudo-element in the redesign
  (remove `::before` gradient overlay)

---

## 2. Academic / Data Visual Element

**Purpose**: Provides a visual anchor that signals "data tool" rather than a
generic web page.

**Classification**: [CSS]

**Recommended approach**:
A horizontal row of 3 inline-block bars at 20%, 55%, and 85% width in
`--accent-primary` at 25% opacity, placed between the subtitle and description.
This is rendered as inline HTML in the `open-card` block.

```html
<div class="open-data-visual">
  <div class="dv-bar" style="width:20%"></div>
  <div class="dv-bar" style="width:55%"></div>
  <div class="dv-bar" style="width:85%"></div>
</div>
```

**Fallback** (simpler): The 3-step flow chip row (`open-features`) already
fulfills the visual anchor role. The data bars are additive and optional.

---

## 3. Team WebForge Block

**Purpose**: Credits the team on the opening page. Replaces the single-creator
`open-creator` div (currently on line 989 of `app.py`).

**Classification**: [CSS]

**HTML structure**:
```html
<div class="open-team-block">
  <div class="open-team-label">Created by Team WebForge</div>
  <div class="open-team-members">
    <span class="open-member">Muhammad Saad
      <span class="member-id">| 202512370</span></span>
    <span class="open-member">Parneet Kaur
      <span class="member-id">| 202612034</span></span>
    <span class="open-member">Abdimazhitova Aikol
      <span class="member-id">| 202601019</span></span>
    <span class="open-member">Nasriddinov Mukhammadzokhir
      <span class="member-id">| 202412350</span></span>
  </div>
</div>
```

**CSS**:
- `.open-team-label`: 11px, 700, ALL CAPS, 0.12em tracking, `--text-secondary`
- `.open-member`: 13px, 500, `--text-primary`
- `.member-id`: 11px, 400, `--text-tertiary`
- `.open-team-members`: `display: flex; flex-wrap: wrap; gap: 6px 16px; justify-content: center`

**Mobile**: At < 480px, `flex-direction: column; align-items: center`

---

## 4. Start Calculation CTA Button

**Purpose**: The single action on the opening page. Navigates to the main dashboard.

**Classification**: [NATIVE + CSS]

**Implementation**:
```python
_c1, _c2, _c3 = st.columns([1.5, 2, 1.5])
with _c2:
    if st.button("▶  Start Calculation", key="open_start_btn",
                 use_container_width=True):
        st.session_state.page = "main"
        st.rerun()
```

**CSS**: Override Streamlit's default button to match primary CTA style:
- Background: `--accent-primary`; hover: `--accent-primary-hover`
- Text: white, 15px, weight 700; border-radius: 8px; min-height: 44px
- Transition: 0.15s ease on background-color and box-shadow
- Hover shadow: `0 6px 20px rgba(37,99,235,0.25)` (light) or `rgba(59,130,246,0.30)` (dark)

---

## 5. Theme Selector

**Purpose**: Allows switching between dark and light mode. Available on the
opening page and in the sidebar.

**Classification**: [NATIVE]

**Opening page placement**: above the card, in `st.columns([3, 2, 3])`, center
column, `horizontal=True`, `label_visibility="collapsed"`.

**Sidebar placement**: below the Home button, above the logo, in the existing
position.

**Implementation**: `st.radio()` with `key="op_theme_radio"` (opening page) and
`key="sb_theme_radio"` (sidebar). On change: write `st.session_state.theme` and
call `st.rerun()`.

**Do not** convert to a toggle — the radio makes both options visible at once,
reducing discoverability risk.

---

## 6. Sidebar Input Groups

**Purpose**: Organizes all inputs into logical, scannable sections. Users build
understanding by reading top to bottom.

**Classification**: [NATIVE + CSS]

**Group order and labels**:
```
Position 1:  ← Home           [button, NATIVE]
             ─── divider ───
Position 2:  🎨 THEME          [sb-label, CSS] + radio [NATIVE]
             ─── divider ───
Position 3:  App logo block    [CSS]
             ─── divider ───
Position 4:  📸 DEMO CASES     [sb-label, CSS] + 2 buttons [NATIVE]
             ─── divider ───
Position 5:  📋 SCORE INPUTS   [sb-label, CSS] + sliders [NATIVE] + pills [CSS]
             ─── divider ───
Position 6:  📅 ATTENDANCE     [sb-label, CSS] + number_inputs [NATIVE] + pills [CSS]
             ─── divider ───
Position 7:  🎯 FINAL EXAM /   [sb-label, CSS] + checkbox/sliders [NATIVE] + pills [CSS]
             🔮 PREDICTION
             ─── divider ───
Position 8:  ⚖️ GRADING WEIGHTS [sb-label, CSS] + number_inputs [NATIVE] + total pill [CSS]
```

**CSS for `.sb-label`**: 11px, 700, ALL CAPS, 0.12em tracking, `--text-secondary`
**CSS for `.sb-divider`**: `height: 1px; background: --border-subtle; margin: 8px 0`

---

## 7. Score Display Pills

**Purpose**: Shows the currently entered score alongside the slider, confirming
input and showing the component weight.

**Classification**: [CSS]

**HTML**:
```html
<div class="score-pill">
  <span>📝 Assignment <small>(10%)</small></span>
  <span class="pill-val">85</span>
</div>
```

**CSS**:
- Container: `display:flex; justify-content:space-between; align-items:center`
- Background: `--bg-elevated`; border: `1px solid --border-subtle`
- Border-radius: 10px; padding: 6px 12px; font-size: 12px
- `.pill-val`: 14px, weight 700, `--text-accent`
- Hover transition: 0.2s ease on border-color

**Semantic variants**:
- Attendance eligible: border `--accent-success` at 35% opacity
- Attendance failed: border `--accent-danger` at 45% opacity

---

## 8. Attendance Configuration

**Purpose**: Three number inputs that auto-calculate attendance percentage and
eligibility without requiring the user to do any math.

**Classification**: [NATIVE + CSS]

**Widgets** (key names must not change):
- `st.number_input("Total Classes", key="total_classes")`
- `st.number_input("Maximum Allowed Missed Classes", key="max_allowed_missed")`
- `st.number_input("Number of Missed Classes", key="missed_classes")`

**Auto-calculated output** (Python, not a widget):
```python
attendance_score  = ((total_classes - missed_classes) / total_classes) * 100
attendance_failed = int(missed_classes) > int(max_allowed_missed)
```

**Status display**: Attendance score pill + status banner (both CSS).
- Green pill + "✅ Eligible" banner when `not attendance_failed`
- Red pill + "❌ Failed — Attendance Policy" when `attendance_failed`

**Info note above inputs** (CSS):
Small italic note: "Attendance score is calculated automatically from total
classes and missed classes."

---

## 9. Grading-Weight Customization

**Purpose**: 4 number inputs with a live running total. Users can customize
how each component contributes to the final grade.

**Classification**: [NATIVE + CSS]

**Widgets** (key names must not change):
- `st.number_input("Assignment Weight (%)", key="w_assignment")`
- `st.number_input("Midterm Weight (%)", key="w_midterm")`
- `st.number_input("Final Exam Weight (%)", key="w_final")`
- `st.number_input("Attendance Weight (%)", key="w_attendance")`

**Live total pill** (CSS):
```html
<div class="weight-total-pill [valid|invalid]">
  Total: 100% ✅
</div>
```
- Valid state: green border + green text
- Invalid state: red border + red text

**Validation**: If `total_weight ≠ 100`, all main-area calculations are blocked
and a warning box is shown. This logic must not be changed.

---

## 10. Final Exam / Prediction Mode Toggle

**Purpose**: Switches between two calculation modes. Controls whether the final
exam score is provided (Score Mode) or the target is set and required final
is calculated (Prediction Mode).

**Classification**: [NATIVE + CSS]

**Widget** (key must not change):
```python
has_final = st.checkbox("Final exam score is available", key="has_final")
```

**When checked** (Score Mode):
- Show: `st.slider("Final Exam Score", key="final_score")` + pink pill
- Hide: target score slider and prediction label

**When unchecked** (Prediction Mode):
- Show: `st.markdown('<div class="sb-label">🔮 PREDICTION MODE</div>')`
- Show: `st.slider("Target Overall Score", key="target_score")` + indigo pill
- Hide: final exam slider

**Mode badge** in main area header:
- Score Mode: pink pill `[✓ FINAL SCORE MODE]`
- Prediction Mode: indigo pill `[🔮 PREDICTION MODE]`

---

## 11. Validation Messages

**Purpose**: Communicates input errors clearly without hiding them or allowing
the user to misread a blocked result.

**Classification**: [NATIVE + CSS]

Three types, displayed in the main area below the KPI banner:

| Type | Trigger | Box Class | Icon |
|------|---------|-----------|------|
| Weights warning | `total_weight ≠ 100` | `perf-warn` | ⚖️ |
| Attendance failure | `attendance_failed == True` | `perf-danger` | 🚫 |
| Final weight = 0 | `w_final == 0` in prediction mode | `perf-warn` | ⚠️ |

**HTML structure** (existing pattern, correct — only colors need updating):
```html
<div class="perf-box perf-[class]">
  <div class="perf-icon">🚫</div>
  <div class="perf-content">
    <div class="perf-title">Title</div>
    <div class="perf-body">Body text</div>
  </div>
</div>
```

**CSS**:
- Left border: 3px solid semantic color
- Background: semantic color at 8% opacity
- Border-radius: 12px; padding: 16px 20px

---

## 12. Primary Result Cards (KPI Banner)

**Purpose**: The first data the user sees in the dashboard. Four metrics in a
row immediately below the header.

**Classification**: [NATIVE + CSS]

**Implementation**:
```python
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("📋 Current Contribution", value)
with c2: st.metric("🏁 Final Score" / "🎯 Required Final Exam", value)
with c3: st.metric("📊 Grade", grade)
with c4: st.metric("⭐ GPA Points", f"{gpa:.1f}")
```

**CSS overrides** on `div[data-testid="metric-container"]`:
- Background: `--bg-surface`
- Border: `1px solid --border-subtle`
- Border-radius: 14px
- Top border accent (3px, per card):
  - Card 1: `#60A5FA` (Blue — Contribution)
  - Card 2: `#818CF8` (Indigo — Score/Required)
  - Card 3: `#34D399` (Emerald — Grade)
  - Card 4: `#F59E0B` (Amber — GPA)
- Hover: `transform: translateY(-3px)`, updated border-color, shadow

**KPI stat values**: 30px / 800, `font-variant-numeric: tabular-nums`
**KPI labels**: 11px / 700, ALL CAPS, `--text-secondary`

---

## 13. Grade Result Card + Interpretation Panel

**Purpose**: The primary result section. Grade letter is the visual focal point.
Interpretation provides contextual guidance.

**Classification**: [CSS]

**Layout**: `st.columns([1, 2], gap="large")`

**Left — Grade Card** (`.grade-wrap`):
- Large grade letter badge (60–72px, weight 900, gradient fill by tier)
- GPA line: "GPA  4.5 / 4.5"
- Score context line: "Final Score: 92.00" or "Target Score: 80"

**Right — Interpretation** (`.perf-box` with semantic class):
- Section header: "💡 Smart Performance Insight"
- Icon + title + body paragraph
- Followed by: Score Breakdown table (`st.dataframe()`)

---

## 14. Charts

**Purpose**: Provides visual explanation of how the final score is composed.

**Classification**: [NATIVE + CSS]

**Layout**: `st.columns([3, 2], gap="large")`

### Bar Chart (left, 60%)

- Type: `ax.barh()` horizontal
- Data: weighted contribution per component
- Background: transparent (`fig.patch.set_facecolor('none')`)
- No legend — labels on bars via `ax.bar_label()`
- Grid: horizontal only, `alpha=0.15`, dashed
- Spines: all hidden
- Title: left-aligned, `--text-primary` color
- Theme: pass `dark: bool` parameter

### Right Panel (40%)

- **Score Mode** → Donut chart: `ax.pie()` with `wedgeprops=dict(width=0.4)`
  - Center label: total points
  - Colors: per component chart palette
- **Prediction Mode** → Gauge: `ax.barh()` progress bar showing required final
  - Red when required > 85, indigo when ≤ 85
  - Label: "XX.X / 100" centered on bar
  - Followed by inline result note (`.perf-box`)

---

## 15. GPA Scale Reference

**Purpose**: Educational reference showing all grade tiers with their ranges,
meanings, and GPA values.

**Classification**: [CSS]

**Layout**: `st.columns(2, gap="medium")`, 5 rows left / 4 rows right

**Each row** (`.grade-row`):
```html
<div class="grade-row">
  <span class="gr-letter grade-[tag]">A+</span>
  <span class="gr-range">95 – 100</span>
  <span class="gr-tag tag-[tag]">Outstanding</span>
  <span class="gr-gpa">GPA 4.5</span>
</div>
```

Hover: `transform: translateX(4px)`, background tint — 0.18s ease.

---

## 16. Footer

**Purpose**: Closes the page with tool identity, tech stack, and team credit.

**Classification**: [CSS]

**HTML structure** (updated for Team WebForge):
```html
<div class="app-footer">
  <div class="footer-title">🎓 Smart GPA Calculator and Prediction System</div>
  <div class="footer-sub">University Academic Performance Dashboard · Team WebForge · v2.0</div>
  <div class="footer-team">
    Muhammad Saad · Parneet Kaur · Abdimazhitova Aikol · Nasriddinov Mukhammadzokhir
  </div>
  <div class="footer-badges">
    <span class="footer-badge">Python</span>
    <span class="footer-badge">Streamlit</span>
    <span class="footer-badge">Pandas</span>
    <span class="footer-badge">Matplotlib</span>
  </div>
</div>
```

---

## 17. Mobile Stacking

**Classification**: [CSS]

Stacking rules applied via injected `@media` queries:

| Breakpoint | Component | Behavior |
|-----------|-----------|---------|
| < 768px | KPI cards | 2×2 grid (`min-width: calc(50% - 8px)`) |
| < 480px | KPI cards | Full-width stack |
| < 480px | Opening card | Padding reduced to 20px |
| < 480px | Team members | `flex-direction: column` |
| < 480px | Flow chips | `flex-wrap: wrap`, centered |
| All mobile | Sidebar | Native Streamlit collapse (no CSS needed) |

---

## Patterns — NOT Recommended

| Pattern | Reason |
|---------|--------|
| React / JS custom components | Adds build complexity; all features achievable natively |
| Continuous `@keyframes` animations | Violates motion budget; accessibility risk |
| Glassmorphism on main cards | GPU cost; visual inconsistency with academic tone |
| Floating AI chat widget | Creates false expectation; not in tool scope |
| Gamification (badges, streaks, XP) | Inappropriate for a serious academic calculator |
| Multi-step onboarding forms | Opening page should have a single CTA |
| Neon / glow accents | Incompatible with "Academic Precision, Human Warmth" concept |

---

*Smart GPA Calculator — Team WebForge — Component Patterns v2.0*
