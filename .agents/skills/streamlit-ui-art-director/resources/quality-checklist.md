# Visual Quality Checklist
## Smart GPA Calculator — Streamlit UI Art Director Skill
### Run before declaring any visual implementation complete

---

## How to Use This Checklist

Run every item below after implementing a visual change.
Mark items as:
- `[x]` — Passed
- `[ ]` — Not yet checked
- `[!]` — Failed — must be fixed before task is complete

A task is only complete when **all items are [x]**.
Report any `[!]` items in the final response with the specific problem found.

---

## Section A — Visual Hierarchy

- `[ ]` **A1** The app title (H1) is the largest text element on every page
- `[ ]` **A2** No more than 4 distinct font sizes are visible simultaneously on any screen
- `[ ]` **A3** Section labels use ALL CAPS + 0.12em tracking + 11px — never the same size as body text
- `[ ]` **A4** KPI stat values are the dominant numeric elements (≥ 28px, weight 800)
- `[ ]` **A5** The grade letter badge is visually prominent (large, colored) — not buried in a row
- `[ ]` **A6** The performance interpretation box is clearly secondary to the grade badge
- `[ ]` **A7** The footer is visually de-emphasized (smaller text, muted color) compared to content

---

## Section B — Spacing Consistency

- `[ ]` **B1** Card internal padding is consistent (16–22px) — no card has noticeably more or less space
- `[ ]` **B2** The vertical gap between KPI cards and the grade/chart section is ≥ 24px
- `[ ]` **B3** Sidebar group items are separated by divider lines; groups have consistent top padding
- `[ ]` **B4** The opening page card has ≥ 48px vertical breathing room (padding-top and padding-bottom)
- `[ ]` **B5** No two adjacent sections use `<br>` tags as the only spacing mechanism — CSS margin preferred
- `[ ]` **B6** The footer has ≥ 32px top margin separating it from the formula section

---

## Section C — Typography Consistency

- `[ ]` **C1** Inter is loaded and rendering for all body text (not falling back to system-ui)
- `[ ]` **C2** JetBrains Mono is rendering in the formula explanation cards
- `[ ]` **C3** All KPI stat values use `font-variant-numeric: tabular-nums`
- `[ ]` **C4** No font weight below 400 is used in any rendered text
- `[ ]` **C5** Minimum rendered font size is 11px — no text is smaller
- `[ ]` **C6** The H1 gradient title uses `-webkit-background-clip: text` correctly
       (text is visible; no pink/purple boxes appear instead of gradient text)
- `[ ]` **C7** Badge and pill text is 11–12px / weight 600 consistently

---

## Section D — Dark Mode Readability

- `[ ]` **D1** App background renders as `#0F172A` (Slate 900) — not pure black, not purple
- `[ ]` **D2** Card surfaces render as `#1E293B` (Slate 800) — distinguishable from the background
- `[ ]` **D3** Primary text (`--text-primary`) is `#F1F5F9` — not pure white
- `[ ]` **D4** Muted labels (`--text-secondary`) are `#94A3B8` — clearly different from primary
- `[ ]` **D5** No purple-tinted backgrounds remain (check sidebar, open card, section-card)
- `[ ]` **D6** Accent color on interactive elements is `#3B82F6` (blue) — not violet/purple
- `[ ]` **D7** The attendance failure state (red) is clearly visible on the dark background
- `[ ]` **D8** All validation warning boxes (amber) are clearly readable on the dark background

---

## Section E — Light Mode Readability

- `[ ]` **E1** App background renders as `#F8FAFC` — not pure white, not purple-tinted
- `[ ]` **E2** Card surfaces render as `#FFFFFF` — clearly lighter than the background
- `[ ]` **E3** Primary text is `#0F172A` — high contrast on white card surface
- `[ ]` **E4** The blue accent `#2563EB` is visible on white card backgrounds (check contrast)
- `[ ]` **E5** Sidebar background is `#F1F5F9` (Slate 100) — distinguishable from main area
- `[ ]` **E6** No elements appear invisible or washed out (check muted text, disabled states)
- `[ ]` **E7** Grade badge gradient colors are readable on both the badge and surrounding white surface
- `[ ]` **E8** The mode badge (pink / indigo pill) is readable against white background

---

## Section F — Theme-Aware Charts

- `[ ]` **F1** Bar chart background is transparent (`fig.patch.set_facecolor('none')`) in both themes
- `[ ]` **F2** Bar chart axis labels are `--text-secondary` color — visible on both backgrounds
- `[ ]` **F3** Donut chart background is transparent in both themes
- `[ ]` **F4** Gauge chart background is transparent in both themes
- `[ ]` **F5** Chart colors adapt to theme (blue/indigo/emerald in dark; darker variants in light)
- `[ ]` **F6** Chart titles use the correct text color per theme
- `[ ]` **F7** No chart renders a colored rectangle where `st.pyplot()` container is visible

---

## Section G — Responsive Behavior

- `[ ]` **G1** At desktop width (≥ 1024px): sidebar is visible; KPI cards are in a 4-column row
- `[ ]` **G2** At 768px width: KPI cards stack in a 2×2 grid (2 cards per row)
- `[ ]` **G3** At 480px width: KPI cards stack full-width (1 per row)
- `[ ]` **G4** At 480px: opening page card padding is ≤ 24px on each side
- `[ ]` **G5** Charts do not overflow horizontally on any screen width
- `[ ]` **G6** The score breakdown table is horizontally scrollable (not clipped) on mobile

---

## Section H — Mobile Stacking

- `[ ]` **H1** Flow chips on the opening page wrap correctly on < 480px (no overflow)
- `[ ]` **H2** Team member names stack vertically on < 480px (not in a single overflowing row)
- `[ ]` **H3** The Start Calculation button is full-width and ≥ 44px tall on mobile
- `[ ]` **H4** Sidebar collapses to a hamburger icon on mobile (native Streamlit behavior)
- `[ ]` **H5** The formula explanation section does not require horizontal scrolling on mobile
- `[ ]` **H6** Grade scale rows are readable and not truncated on narrow screens

---

## Section I — Button and Input States

- `[ ]` **I1** The Start Calculation button has a visible hover state (color change or shadow)
- `[ ]` **I2** The ← Home button has a visible hover state (background tint)
- `[ ]` **I3** Sliders show the `--accent-primary` (blue) thumb color — not purple/default gray
- `[ ]` **I4** Number inputs show a blue focus ring on focus — not the browser default
- `[ ]` **I5** All interactive elements have touch targets ≥ 44 × 44 CSS px
- `[ ]` **I6** The theme radio shows which option is currently selected (visual active state)

---

## Section J — Attendance Warning Visibility

- `[ ]` **J1** The attendance failure danger box is visible in the main area (red, prominent)
- `[ ]` **J2** The attendance status pill in the sidebar changes color on failure (red vs green)
- `[ ]` **J3** The attendance eligibility banner in the sidebar is readable at its current font size
- `[ ]` **J4** When attendance fails, all score results in the KPI banner show "N/A" or "F" — not numbers

---

## Section K — Weight-Total Validation Visibility

- `[ ]` **K1** The weight total pill in the sidebar shows red when sum ≠ 100
- `[ ]` **K2** The weight validation warning box appears in the main area when weights ≠ 100
- `[ ]` **K3** All KPI cards show "—" (not numbers) when weights are invalid
- `[ ]` **K4** The amber warning box text is readable in both dark and light modes

---

## Section L — Grade and GPA Hierarchy

- `[ ]` **L1** The grade letter is the largest, most prominent element in the grade result section
- `[ ]` **L2** The GPA value (e.g., "4.5 / 4.5") is clearly secondary to the grade letter
- `[ ]` **L3** The grade badge color reflects the correct semantic tier (green A, blue B, amber C, red D/F)
- `[ ]` **L4** The score context line ("Final Score: 92.00") is muted — clearly tertiary
- `[ ]` **L5** The GPA scale reference correctly shows all 9 tiers from A+ (4.5) to F (0.0)

---

## Section M — Team Identity Accuracy

- `[ ]` **M1** The opening page shows "Created by Team WebForge" (not a single person's name)
- `[ ]` **M2** All 4 team members are listed with their correct names and IDs:
       - Muhammad Saad | 202512370
       - Parneet Kaur | 202612034
       - Abdimazhitova Aikol | 202601019
       - Nasriddinov Mukhammadzokhir | 202412350
- `[ ]` **M3** The footer includes "Team WebForge" in the credit line
- `[ ]` **M4** The footer includes all 4 member names (not just the team name)
- `[ ]` **M5** No single person is credited as the sole creator anywhere in the visible UI

---

## Section N — Reduced-Motion Compliance

- `[ ]` **N1** All `@keyframes` animations are inside `@media (prefers-reduced-motion: no-preference)`
- `[ ]` **N2** The `subtlePulse` continuous animation has been removed (was on `.open-creator`)
- `[ ]` **N3** The opening card `slideUp` animation fires only once on page load (not looping)
- `[ ]` **N4** No `animation-iteration-count: infinite` exists in any CSS block
- `[ ]` **N5** Hover transitions (0.15–0.18s) are not wrapped in reduced-motion query —
       this is intentional (hover requires user interaction, not automatic motion)

---

## Section O — HTML Integrity

- `[ ]` **O1** All `st.markdown(…, unsafe_allow_html=True)` blocks contain valid HTML
- `[ ]` **O2** All `<div>` and `<span>` tags are properly closed
- `[ ]` **O3** No raw angle brackets `<` or `>` appear as visible text in the browser
- `[ ]` **O4** HTML entities (`&amp;`, `&nbsp;`, `&gt;`) are used correctly where needed
- `[ ]` **O5** No inline `style=""` attributes contain syntax errors (missing semicolons, etc.)
- `[ ]` **O6** The `<style>` block injected via `st.markdown()` contains no duplicate selectors
       that contradict each other

---

## Section P — No Duplicate Widget Keys

- `[ ]` **P1** Run `streamlit run app.py` — no `DuplicateWidgetID` error appears in the terminal
- `[ ]` **P2** All `key=` parameters in `st.*` widget calls match the protected key list in
       `.agents/rules/project-safety.md`
- `[ ]` **P3** No new `key=` parameters have been added that shadow existing protected keys

---

## Section Q — No Calculation Changes

- `[ ]` **Q1** The `score_to_grade()` function body is unchanged
- `[ ]` **Q2** The `GRADE_SCALE` constant is unchanged (9 tiers, 4.5 GPA max)
- `[ ]` **Q3** The `performance_comment()` function body is unchanged
- `[ ]` **Q4** The attendance formula `((total_classes - missed_classes) / total_classes) * 100`
       is unchanged
- `[ ]` **Q5** The `_wa`, `_wm`, `_wf`, `_watt` weight computation is unchanged
- `[ ]` **Q6** The `required_final` formula `(target_score - current_contribution) / _wf` is unchanged
- `[ ]` **Q7** The `attendance_failed` boolean condition is unchanged
- `[ ]` **Q8** The `weights_valid` boolean condition `total_weight == 100` is unchanged

---

## Section R — Browser Review at Desktop and Mobile

- `[ ]` **R1** Screenshot taken at ≥ 1024px width — dark mode
- `[ ]` **R2** Screenshot taken at ≥ 1024px width — light mode
- `[ ]` **R3** Screenshot taken at ≤ 480px width — dark mode (mobile simulation)
- `[ ]` **R4** Screenshot taken at ≤ 480px width — light mode (mobile simulation)
- `[ ]` **R5** Opening page reviewed in browser — team block is visible and correct
- `[ ]` **R6** Dashboard reviewed in browser — KPI cards, grade section, charts all render
- `[ ]` **R7** Footer reviewed in browser — team name and members are visible

---

## Final Sign-Off

Before marking the visual task as complete, confirm:

```
[ ] All A–R checklist items are [x]
[ ] No calculation, session-state, or widget-key was changed
[ ] Both dark and light mode screenshots are captured and attached
[ ] app.py runs without error: streamlit run app.py
[ ] Footer and opening page display "Team WebForge" with all 4 members
```

---

*Smart GPA Calculator — Team WebForge — Quality Checklist v2.0*
