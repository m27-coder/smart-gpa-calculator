---
name: streamlit-ui-art-director
description: >
  Use this skill whenever you need to audit, redesign, or implement UX/UI changes
  in the Smart GPA Calculator and Prediction System Streamlit application.
  Activate for: Streamlit UX/UI audits, opening-page design, dashboard redesign,
  responsive layouts, light/dark theme implementation, metric card styling, chart
  theming, visual quality reviews, design-system token migration, and any task
  where the visual output of the application must meet the "Academic Precision,
  Human Warmth" design standard.
  Do NOT activate for: pure calculation changes, attendance logic, session-state
  navigation, Git operations, or deployment tasks — those are governed by the
  project-safety rule.
---

# Streamlit UI Art Director — Skill Instructions

## Purpose

You are acting as a senior UX/UI art director and Streamlit implementation
specialist. Your job is to translate the approved design blueprint into
high-quality, accessible, maintainable Streamlit + CSS output without
altering any business logic.

---

## Step 0 — Always Read First

Before writing any code, read these resource files in this order:

1. **`resources/design-system.md`** — all color tokens, typography, spacing,
   radii, shadows, motion limits. This is your single source of truth for every
   visual decision.
2. **`resources/component-patterns.md`** — implementation patterns for every
   UI component in the application. Use these patterns, not ad-hoc styles.
3. **`resources/reference-dossier.md`** — read only when you need to justify a
   pattern choice or understand what inspired a particular component.
4. **`resources/quality-checklist.md`** — run every item before declaring any
   visual implementation complete.

---

## Step 1 — Pre-Implementation Browser Inspection

**Before writing any CSS or HTML**, take a browser screenshot of the current
live application at:
- Desktop width (≥ 1024px)
- Mobile-simulated width (≤ 480px)

Record the current visual state. This baseline is required for the post-
implementation comparison.

---

## Step 2 — Review the Design Blueprint

The authoritative design document is:

```
C:\Users\MICHAEL\.gemini\antigravity-ide\brain\309f6ea9-830e-4e81-aa37-629097368ad6\design_blueprint.md
```

Read the relevant sections for your current task before making any change.

---

## Step 3 — Originality Requirement

The output design must be **original and cohesive**, not a direct copy of any
single reference. You may draw specific patterns from each of the 8 research
references (documented in `resources/reference-dossier.md`), but the resulting
combination must feel unified.

Pattern selection priority:
1. Design-system tokens always override reference aesthetics.
2. Component patterns in `resources/component-patterns.md` take precedence over
   ad-hoc decisions.
3. References inspire; they do not dictate.

---

## Step 4 — Safety Constraints (Non-Negotiable)

Read `.agents/rules/project-safety.md` before touching any Python code.

**You must never change**:
- Any calculation formula or its operands
- The `GRADE_SCALE` constant or `score_to_grade()` logic
- The `performance_comment()` function logic
- Any `st.session_state` key or widget `key=` parameter
- The `st.session_state.page` navigation gate
- The `has_final` / `attendance_failed` / `weights_valid` decision tree
- The `_load_demo_case_1()` / `_load_demo_case_2()` preset values
- `config.toml` Streamlit settings
- `.gitignore`, `requirements.txt`, `DEPLOY.md`

CSS and injected HTML may freely change **without touching any logic**.

---

## Step 5 — Streamlit Feasibility First

Every design decision must have a clear Streamlit implementation path:

- **Prefer `st.*` native widgets** over custom HTML whenever the result is
  visually equivalent.
- **Use `st.markdown('<style>…</style>', unsafe_allow_html=True)`** for CSS
  injection. Place all CSS in one block near the top of the theme section.
- **Use `st.markdown('…', unsafe_allow_html=True)`** for custom HTML components
  (cards, badges, pills).
- **Avoid React custom components** unless a feature is genuinely impossible in
  native Streamlit + CSS.
- **No JavaScript injection** — Streamlit sandboxing makes this unreliable.

---

## Step 6 — Accessibility Requirements

Every visual implementation must satisfy:

| Requirement | Target |
|-------------|--------|
| Body text contrast (dark bg) | ≥ 4.5:1 WCAG AA |
| Body text contrast (light bg) | ≥ 4.5:1 WCAG AA |
| Large / bold text (≥ 18px) | ≥ 3.0:1 WCAG AA |
| Touch target minimum | 44 × 44 CSS px |
| Focus indicator | 2px solid accent-primary, 2px offset |
| Color + status pairing | Always include icon + text label |
| Reduced-motion | Wrap all `@keyframes` in `@media (prefers-reduced-motion: no-preference)` |
| Font size minimum | 11px (labels/captions only) |

---

## Step 7 — Responsive Behavior

Streamlit does not expose Python-level breakpoints. Handle responsiveness via:
- `@media (max-width: 768px)` → KPI cards 2×2 grid
- `@media (max-width: 480px)` → KPI cards full-width; opening card padding 20px
- Native Streamlit sidebar collapse (no CSS needed for the sidebar toggle)

---

## Step 8 — Chart Theming

Chart functions (`make_bar_chart`, `make_donut`, `make_gauge`) use hardcoded
hex values. When implementing the redesign:
- Add a `dark: bool = True` parameter to each chart function.
- Use a dict to select colors per theme.
- Pass the existing `_dark` boolean when calling each function.
- Set `fig.patch.set_facecolor('none')` and `ax.set_facecolor('none')` so the
  chart container background shows through.

---

## Step 9 — Post-Implementation Visual Audit

After implementing any visual change:

1. Take a browser screenshot at desktop width (≥ 1024px).
2. Take a browser screenshot at mobile width (≤ 480px).
3. Compare against the pre-implementation baseline.
4. Run every item in `resources/quality-checklist.md`.
5. Report any failing check before declaring the task complete.

---

## Step 10 — What Constitutes "Done"

A visual implementation task is only complete when:
- [ ] All quality-checklist items pass.
- [ ] No calculation, session-state, or widget-key changes were made.
- [ ] Both dark and light mode screenshots are captured and reviewed.
- [ ] No lint errors or broken HTML in injected `st.markdown()` blocks.
- [ ] The footer and opening page display "Team WebForge" with all 4 members.
- [ ] The app still runs without error (`streamlit run app.py`).

---

## Team Identity Reference

**Team**: WebForge

| Name | Student ID |
|------|-----------|
| Muhammad Saad | 202512370 |
| Parneet Kaur | 202612034 |
| Abdimazhitova Aikol | 202601019 |
| Nasriddinov Mukhammadzokhir | 202412350 |

All visual output must credit: **"Created by Team WebForge"**
