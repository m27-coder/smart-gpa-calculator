# Reference Dossier
## Smart GPA Calculator — UX/UI Research References
### Team WebForge — Step 1 Verified Research

> These 8 references were researched live during Step 1 (2026-09-14) using
> browser sessions on Dribbble, Behance, and Streamlit Gallery. Screenshots
> were captured and stored as Step 1 artifacts. URLs pointing to search result
> pages are correct; individual shot URLs depend on Dribbble/Behance session
> state and may redirect.

---

## Reference 1 — EduSphere Academic Dashboard

| Field | Detail |
|-------|--------|
| **Exact Name** | EduSphere Academic Dashboard |
| **Source** | Dribbble |
| **Designer** | Nurina Laraswati |
| **URL** | https://dribbble.com/search/education+dashboard |
| **Note** | Top-left card in the Dribbble education dashboard search grid |

### Useful Patterns
- 4-column KPI banner immediately below the page title — instantly communicates
  the most important numbers at a glance
- Left sidebar: grouped items with icon + label; blue left-border active state;
  no decorative chrome
- Card containers: `border-radius: 12px`, `1px #E2E8F0 border`, white surface on
  Slate-50 background — creates clean depth without heavy shadows
- Section labels: 11px, ALL CAPS, `0.12em` letter-spacing, muted gray —
  professional hierarchy without heading tags
- Subject-level progress rings: compact, no legend, color per subject

### Elements to Avoid
- Decorative avatar illustrations inside metric cards — visual noise with no
  informational value
- Dense body text below 13px in table cells — contrast failure in light mode

### Streamlit Feasibility
- ✅ Native: `st.columns(4)` + `st.metric()` for KPI row
- ✅ Native: sidebar mirrors Streamlit native sidebar layout exactly
- ✅ CSS: `border-radius: 12px` + `border: 1px solid` via injected `<style>`

### Inspires
→ **KPI metric banner** (4-card row above charts) and **sidebar input group structure**

---

## Reference 2 — OAK University Dashboard

| Field | Detail |
|-------|--------|
| **Exact Name** | OAK University Academic Dashboard |
| **Source** | Dribbble |
| **Designer** | Ismail Nahid |
| **URL** | https://dribbble.com/search/education+dashboard |
| **Note** | Center card in the Dribbble education dashboard search grid |

### Useful Patterns
- Large bold number callouts at 36–40px / weight 800 on dark substrate —
  numbers read at a glance without needing to scan
- Status badge pills: "On Track" (Emerald `#10B981`) / "At Risk" (Rose `#EF4444`)
  — semantic status communication without charts
- Bar chart placed immediately adjacent to the metric it visualizes —
  tight information coupling
- Mode indicator badge: small all-caps pill in top of content area identifies
  the current calculation mode

### Elements to Avoid
- Lime-yellow / electric-teal neon accents — too vivid, inappropriate for an
  academic calculator
- Hybrid dark sidebar + lighter body area without a system-level theme —
  creates visual incoherence

### Streamlit Feasibility
- ✅ CSS: Status badge pills via `st.markdown('<span class="badge">On Track</span>')`
- ✅ Native: Bar chart via `st.columns()` adjacent to metric cards
- ✅ CSS: Mode badge pill at top of main area via `st.markdown()`

### Inspires
→ **Attendance status badge pill** in sidebar and **mode badge** (Final Score Mode
vs Prediction Mode) in dashboard header

---

## Reference 3 — Octavia Learning Dashboard (LMS)

| Field | Detail |
|-------|--------|
| **Exact Name** | Octavia Learning Dashboard |
| **Source** | Dribbble |
| **Designer** | Roohi Koohi |
| **URL** | https://dribbble.com/search/education+dashboard |
| **Note** | Top-right card in the Dribbble education dashboard search grid |

### Useful Patterns
- Identity-first opening panel: prominent title with a warm greeting — sets the
  tone before any interaction
- Horizontal tab bar (Dashboard / Schedule / Analytics / Reports) with no
  sub-levels — reduces cognitive load
- Light mode palette: white cards on `#F4F6F9` base, `#3B82F6` mid-blue primary
  accent — clean, high-contrast, academically appropriate
- "Daily activity" sparkline in right panel: compact trend without a dedicated
  chart section

### Elements to Avoid
- Achievement badges, streak counters, XP points — gamification is unsuitable
  for a serious academic calculator
- User avatar / profile image panel — unnecessary for a single-user tool

### Streamlit Feasibility
- ✅ Native: `st.tabs()` for top-level navigation
- ✅ Native: `st.markdown()` for greeting/hero panel at top of main area
- ✅ Native: `st.progress()` for inline progress indicators

### Inspires
→ **Light mode color palette** tokens and **main navigation tabs**

---

## Reference 4 — Atayc Innovations — Academic GPA Tracker

| Field | Detail |
|-------|--------|
| **Exact Name** | Atayc Innovations — Academic GPA Tracker |
| **Source** | Dribbble |
| **Designer** | Atayc Innovations |
| **URL** | https://dribbble.com/search/GPA+tracker |
| **Note** | Top-left card in the Dribbble GPA tracker search grid |

### Useful Patterns
- Two-panel layout: left = all inputs, right = live calculated result —
  spatial separation of cause and effect
- "3.8 GPA" isolated in a large callout card with zero surrounding decoration —
  data speaks for itself
- Prediction mode toggle that hides one set of inputs and reveals another —
  clean mode switching without a separate page
- Performance trend sparkline across N semesters — compact historical view

### Elements to Avoid
- Multi-level nested modal dialogs for simple actions
- Avatar / profile image cells mixed into academic data rows

### Streamlit Feasibility
- ✅ Native: `st.columns([1, 1])` for input panel + results panel
- ✅ Native: `st.toggle()` or `st.checkbox()` for prediction mode switch
- ✅ Native: Matplotlib line chart via `st.pyplot(fig)` for trends

### Inspires
→ **Final exam / prediction mode toggle** in sidebar and **grade result callout** card design

---

## Reference 5 — Fakher Uddin — Scalable Education Platform Dashboard

| Field | Detail |
|-------|--------|
| **Exact Name** | Scalable Education Platform Dashboard |
| **Source** | Behance |
| **Designer** | Fakher Uddin |
| **URL** | https://www.behance.net/search/projects?search=education+dashboard |
| **Note** | Center card in Behance education dashboard search — UX case study multi-device mockup |

### Useful Patterns
- Full UX case study: login → hero CTA landing page → main dashboard —
  validates the opening page gate pattern
- Typography system: 32px H1 / 24px H2 / 16px card heading / 13px label —
  maximum 4 sizes in use simultaneously
- Multi-device responsive demo (desktop → tablet → phone) — confirms layout
  priorities per breakpoint
- Color system: Indigo/Blue primary `#2563EB`, neutral gray surfaces,
  Emerald `#059669` success

### Elements to Avoid
- Multi-step onboarding forms on the splash screen (login form, profile wizard)
- Course content library thumbnails — out of scope for a single-purpose calculator

### Streamlit Feasibility
- ✅ Native: `st.session_state.page` flag + `st.rerun()` for opening page gate
- ✅ Native: `st.tabs()` for view navigation post-start
- ✅ CSS: Responsive layout via native grid + `@media` query

### Inspires
→ **Opening page structure** (hero CTA, description, team identity) and **typography scale**

---

## Reference 6 — Learning Sync — Dark Mode Education Dashboard

| Field | Detail |
|-------|--------|
| **Exact Name** | Learning Sync — Dark Mode Education Dashboard |
| **Source** | Behance |
| **Designer** | SoftDoes |
| **URL** | https://www.behance.net/search/projects?search=education+dashboard |
| **Note** | Bottom-left card in Behance education dashboard search — dark dashboard with "78%" donut |

### Useful Patterns
- Dark mode three-tier surface system: `#0D1117` base / `#161B22` card /
  `#30363D` border — avoids pure black, creates perceivable depth
- Donut/ring chart for single aggregate percentage — ideal for displaying
  overall score composition
- "AI Insight" widget → visual inspiration for the performance interpretation box
  layout (left accent border + icon + text block)
- 11px ALL-CAPS section dividers with `0.08em` letter-spacing —
  professional visual rhythm

### Elements to Avoid
- Continuous animated particle or aurora backgrounds — GPU cost, distracting,
  violates animation policy
- AI-branded copy ("AI Insight", "Smart Recommendations") in a tool that does
  not use AI inference

### Streamlit Feasibility
- ✅ Native: Dark color system via `config.toml` base theme + CSS variables
- ✅ CSS: Donut via `ax.pie()` with `wedgeprops=dict(width=0.4)`
- Native: Sidebar collapse on mobile is native Streamlit behavior

### Inspires
→ **Dark mode color system** (3-tier surface tokens) and **performance interpretation box** layout

---

## Reference 7 — Streamlit Official App Gallery

| Field | Detail |
|-------|--------|
| **Exact Name** | Streamlit Official App Gallery |
| **Source** | Streamlit (official) |
| **Designer** | Streamlit team and community |
| **URL** | https://streamlit.io/gallery |
| **Note** | Gallery card grid — specifically: Seattle Weather Dashboard, Stock Peer Analysis |

### Useful Patterns
- `st.metric()` renders clean KPI cards with label, value, and delta indicator —
  native, zero CSS for basic use
- `st.tabs()` confirmed as idiomatic view separator in production Streamlit apps
- Sidebar category panel structure mirrors the grading weight settings grouping
- Native light theme used in "Seattle Weather Dashboard" is clean without heavy CSS

### Elements to Avoid
- Raw `st.dataframe()` without a containing card or styled column headers
- Full-width `st.number_input()` on wide screens without `max-width` constraint

### Streamlit Feasibility
- ✅ All components shown are standard `st.*` — 100% native Streamlit

### Inspires
→ **KPI metric card** implementation, **grading weights sidebar** grouping, **score breakdown table**

---

## Reference 8 — CORSTA AI Learning Portal

| Field | Detail |
|-------|--------|
| **Exact Name** | CORSTA AI Learning Portal |
| **Source** | Behance |
| **Designer** | CORSTA |
| **URL** | https://www.behance.net/search/projects?search=education+dashboard |
| **Note** | Bottom-right card in Behance education dashboard search — white/blue portal with "Welcome back, Hani!" |

### Useful Patterns
- "Welcome back, Hani!" header at top of content area — personalized confirmation
  the tool is loaded and ready
- Sidebar organized into named groups with divider lines: Navigation / Courses /
  Planning / Reports
- Dual-column main area: wide left for primary content, narrow right for
  secondary contextual data
- Accessibility-first: visible focus rings, labeled inputs, 44px minimum touch
  targets demonstrated

### Elements to Avoid
- Floating AI assistant chat widget — creates expectation of real AI, clutters viewport
- Decorative animated module illustrations — page weight without information value

### Streamlit Feasibility
- ✅ Native: Greeting section via `st.markdown()`
- ✅ Native: Sidebar groups with `st.markdown()` dividers
- ✅ Native: `st.columns([2, 1])` for wide main + narrow secondary layout

### Inspires
→ **Sidebar grouping structure** (named sections with dividers) and **dual-column main area**

---

## Selected Pattern Attribution Summary

| Design Area | Primary Reference | Supporting Reference |
|-------------|------------------|---------------------|
| Opening page | Fakher Uddin (Behance) | Octavia (Dribbble) |
| Navigation / UX flow | Octavia | Fakher Uddin |
| Dashboard structure | EduSphere | Atayc GPA Tracker |
| Input grouping | CORSTA | EduSphere |
| Attendance config | OAK University | CORSTA |
| Grading weights | EduSphere | Streamlit Gallery |
| Result metric cards | EduSphere | OAK University |
| Charts | Streamlit Gallery | Learning Sync |
| Light mode palette | Octavia | Fakher Uddin |
| Dark mode palette | Learning Sync | Current app direction |
| Mobile layout | Fakher Uddin | Streamlit Gallery |
| Micro-interactions | OAK University | CORSTA |

---

*Research conducted: 2026-09-14 — Step 1 (browser sessions)*
*Compiled into dossier: 2026-09-14 — Step 3 (skill creation)*
*Team WebForge — Muhammad Saad · Parneet Kaur · Abdimazhitova Aikol · Nasriddinov Mukhammadzokhir*
