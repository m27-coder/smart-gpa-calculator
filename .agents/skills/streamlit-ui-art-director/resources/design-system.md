# Design System
## Smart GPA Calculator and Prediction System
### Team WebForge — "Academic Precision, Human Warmth"

---

## Concept

**"Academic Precision, Human Warmth"**

An authoritative yet approachable dashboard that mirrors how good professors
communicate: structured, clear, direct, but never cold. Data is always the hero.

**Reject**: glassmorphism on main cards, glow effects, neon accents, continuous
animations, particle backgrounds, gaming aesthetics, AI marketing copy,
decorative gradients on body surfaces.

**Adopt**: clean card grids, status-semantic color (not decorative), tabular
Inter numerals, purposeful hover-only micro-transitions, two fully resolved themes.

---

## 1. Color System

### 1A. Dark Mode Tokens (Default)

| Token | Hex | Tailwind Ref | Usage |
|-------|-----|-------------|-------|
| `--bg-base` | `#0F172A` | Slate 900 | App background (`.stApp`) |
| `--bg-surface` | `#1E293B` | Slate 800 | Card surfaces, metric containers |
| `--bg-elevated` | `#293548` | Slate ~750 | Sidebar, raised panels |
| `--bg-overlay` | `#0A0F1E` | Slate 950 | Deep sections, overlays |
| `--border-subtle` | `#334155` | Slate 700 | Default card borders |
| `--border-active` | `#4F6DBC` | — | Focused / active borders |
| `--border-hover` | `#64748B` | Slate 500 | Hover state borders |
| `--text-primary` | `#F1F5F9` | Slate 100 | All body text |
| `--text-secondary` | `#94A3B8` | Slate 400 | Muted labels, captions |
| `--text-tertiary` | `#475569` | Slate 600 | Placeholders, disabled |
| `--text-accent` | `#BAD0FF` | — | Highlighted numeric values |
| `--accent-primary` | `#3B82F6` | Blue 500 | CTA buttons, links, active states |
| `--accent-primary-hover` | `#2563EB` | Blue 600 | Button hover |
| `--accent-success` | `#10B981` | Emerald 500 | Pass, Grade A, Eligible |
| `--accent-warning` | `#F59E0B` | Amber 500 | Caution, Grade C, borderline |
| `--accent-danger` | `#EF4444` | Red 500 | Fail, Grade F, Failed |
| `--accent-info` | `#6366F1` | Indigo 500 | Prediction mode, neutral info |

### 1B. Light Mode Tokens

| Token | Hex | Tailwind Ref | Usage |
|-------|-----|-------------|-------|
| `--bg-base` | `#F8FAFC` | Slate 50 | App background |
| `--bg-surface` | `#FFFFFF` | White | Card surfaces |
| `--bg-elevated` | `#F1F5F9` | Slate 100 | Raised sections, sidebar |
| `--bg-overlay` | `#E2E8F0` | Slate 200 | Overlays |
| `--border-subtle` | `#E2E8F0` | Slate 200 | Default card borders |
| `--border-active` | `#2563EB` | Blue 600 | Focused / active borders |
| `--border-hover` | `#94A3B8` | Slate 400 | Hover borders |
| `--text-primary` | `#0F172A` | Slate 900 | All body text |
| `--text-secondary` | `#64748B` | Slate 500 | Muted labels |
| `--text-tertiary` | `#CBD5E1` | Slate 300 | Placeholders, disabled |
| `--text-accent` | `#1D4ED8` | Blue 700 | Highlighted values |
| `--accent-primary` | `#2563EB` | Blue 600 | CTA buttons, links |
| `--accent-primary-hover` | `#1D4ED8` | Blue 700 | Button hover |
| `--accent-success` | `#059669` | Emerald 600 | Pass, Grade A |
| `--accent-warning` | `#D97706` | Amber 600 | Caution, Grade C |
| `--accent-danger` | `#DC2626` | Red 600 | Fail, Grade F |
| `--accent-info` | `#4F46E5` | Indigo 600 | Prediction mode |

### 1C. Semantic Color Rules

Color must NEVER be the only signal. Always pair with icon + text label.

| Semantic Role | Dark Token | Light Token | Applies To |
|--------------|------------|------------|------------|
| Success | `#10B981` | `#059669` | Grade A/A+, Eligible, weights valid, target achievable |
| Warning | `#F59E0B` | `#D97706` | Grade C/C+, weights ≠ 100, required final 61–100 |
| Danger | `#EF4444` | `#DC2626` | Grade D/D+/F, attendance failed, required final > 100 |
| Info | `#6366F1` | `#4F46E5` | Prediction mode, neutral information |
| Primary | `#3B82F6` | `#2563EB` | All CTA buttons, active tabs, links |

### 1D. Grade Badge Color Map

| Grade | Background Start | Background End | Text |
|-------|-----------------|----------------|------|
| A+ | `#047857` | `#6EE7B7` | `#022C22` |
| A | `#059669` | `#34D399` | `#022C22` |
| B+ | `#1E40AF` | `#93C5FD` | `#0C1844` |
| B | `#1D4ED8` | `#60A5FA` | `#0C1844` |
| C+ | `#B45309` | `#FDE68A` | `#451A03` |
| C | `#D97706` | `#FCD34D` | `#451A03` |
| D+ | `#B91C1C` | `#FCA5A5` | `#FFFFFF` |
| D | `#991B1B` | `#F87171` | `#FFFFFF` |
| F | `#374151` | `#9CA3AF` | `#FFFFFF` |

### 1E. Chart Color Palette

| Component | Color | Hex |
|-----------|-------|-----|
| Assignment | Blue 400 | `#60A5FA` |
| Midterm Exam | Indigo 400 | `#818CF8` |
| Attendance | Emerald 400 | `#34D399` |
| Final Exam | Pink 400 | `#F472B6` |
| Chart background | Transparent | `none` |
| Grid lines | Border-subtle @ 40% | — |
| Axis labels | `--text-secondary` | — |
| Chart titles | `--text-primary` | — |

**Rule**: Chart colors must be passed via a `dark: bool` parameter. Use:
```python
CHART_COLORS = {
    True:  {"assign": "#60A5FA", "mid": "#818CF8", "attend": "#34D399", "final": "#F472B6"},
    False: {"assign": "#2563EB", "mid": "#4F46E5", "attend": "#059669", "final": "#DB2777"},
}
```

---

## 2. Typography

### 2A. Font Families

```css
--font-ui:   'Inter', 'Segoe UI', system-ui, sans-serif;
--font-mono: 'JetBrains Mono', 'Courier New', Courier, monospace;
```

Import via `@import` at the top of the injected CSS block:
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');
```

### 2B. Type Scale (max 4 sizes visible on any single screen)

| Role | Size | Weight | Line Height | Letter Spacing | Font |
|------|------|--------|-------------|----------------|------|
| App Title (H1) | 32px | 900 | 1.2 | −0.02em | Inter |
| Section H2 | 24px | 700 | 1.3 | −0.01em | Inter |
| Card Heading (H3) | 16px | 600 | 1.4 | 0 | Inter |
| Section Label | 11px | 700 | 1.0 | +0.12em | Inter (ALL CAPS) |
| KPI Stat Value | 30px | 800 | 1.0 | −0.02em | Inter (tabular-nums) |
| KPI Label | 11px | 700 | 1.0 | +0.12em | Inter (ALL CAPS) |
| Body Text | 14px | 400 | 1.55 | 0 | Inter |
| Caption / Badge | 11px | 600 | 1.0 | +0.04em | Inter |
| Formula / Monospace | 13px | 400 | 1.9 | 0 | JetBrains Mono |

**Rules**:
- `font-variant-numeric: tabular-nums` on all digit-displaying elements
- Minimum rendered font size: **11px** (labels and captions only)
- No font weight below 400
- Gradient fills on the H1 title only (`-webkit-background-clip: text`)

---

## 3. Spacing Scale

| Token | Value | Primary Usage |
|-------|-------|---------------|
| `--sp-1` | 4px | Icon gap, inline element margin |
| `--sp-2` | 8px | Badge padding, pill internal gap |
| `--sp-3` | 12px | Sidebar item padding |
| `--sp-4` | 16px | Default card internal padding |
| `--sp-5` | 24px | Between sidebar groups |
| `--sp-6` | 32px | Between dashboard rows |
| `--sp-7` | 48px | Between major dashboard sections |
| `--sp-8` | 64px | Opening page vertical breathing |

---

## 4. Border Radii

| Context | Radius |
|---------|--------|
| Main content cards | 12px |
| Metric (KPI) cards | 14px |
| Opening page card | 24px |
| Buttons | 8px |
| Badge / pill (small) | 6px |
| Badge / pill (rounded) | 20px |
| Input fields | 8px |
| Score display pills | 10px |
| Chart containers | 12px |

---

## 5. Shadow System

| Context | Shadow |
|---------|--------|
| KPI card — dark, default | `0 2px 8px rgba(0,0,0,0.25)` |
| KPI card — dark, hover | `0 8px 24px rgba(0,0,0,0.40)` |
| KPI card — light, default | `0 2px 8px rgba(0,0,0,0.06)` |
| KPI card — light, hover | `0 8px 24px rgba(0,0,0,0.12)` |
| Opening card — dark | `0 24px 80px rgba(0,0,0,0.50)` |
| Opening card — light | `0 24px 80px rgba(0,0,0,0.10)` |
| Button hover — dark | `0 6px 20px rgba(59,130,246,0.30)` |
| Button hover — light | `0 6px 20px rgba(37,99,235,0.25)` |
| Focus ring (all) | `0 0 0 2px var(--accent-primary)` |

---

## 6. Button States

### Primary CTA (Start Calculation, Load Demo)

| State | Background | Text | Border | Shadow |
|-------|-----------|------|--------|--------|
| Default | `--accent-primary` | `#FFFFFF` | none | none |
| Hover | `--accent-primary-hover` | `#FFFFFF` | none | button hover shadow |
| Focus | `--accent-primary` | `#FFFFFF` | focus ring | focus ring shadow |
| Active | `--accent-primary-hover` | `#FFFFFF` | none | inset |
| Disabled | `--text-tertiary` | `--text-secondary` | none | none |

- Padding: 12px 28px · Border-radius: 8px · Min height: 44px
- Font: 15px / weight 700 · Transition: 0.15s ease on background-color, box-shadow

### Secondary Button (Home ←)

| State | Background | Text | Border |
|-------|-----------|------|--------|
| Default | transparent | `--accent-primary` | 1px solid `--border-active` |
| Hover | `--accent-primary` @ 8% | `--accent-primary` | 1px solid `--accent-primary` |
| Focus | transparent | `--accent-primary` | focus ring |

- Padding: 8px 16px · Border-radius: 8px · Font: 13px / weight 600

---

## 7. Input States

### Slider

| State | Thumb | Track (active) | Track (inactive) |
|-------|-------|---------------|-----------------|
| Default | `--accent-primary` | `--accent-primary` | `--bg-elevated` |
| Hover | `--accent-primary-hover` | `--accent-primary-hover` | `--border-hover` |
| Focus | Focus ring on thumb | — | — |

### Number Input

| State | Border | Background | Text |
|-------|--------|-----------|------|
| Default | 1px `--border-subtle` | `--bg-surface` | `--text-primary` |
| Hover | 1px `--border-hover` | `--bg-surface` | `--text-primary` |
| Focus | 1px `--border-active` + focus ring | `--bg-surface` | `--text-primary` |
| Error | 1px `--accent-danger` | `--accent-danger` @ 5% | `--text-primary` |

- Height: 40px minimum (44px touch target) · Border-radius: 8px

---

## 8. Motion and Animation Limits

### Permitted Interactions

| Interaction | Duration | Easing | Property |
|-------------|----------|--------|----------|
| Card border on hover | 0.18s | ease | border-color |
| Card shadow on hover | 0.18s | ease | box-shadow |
| KPI card lift on hover | 0.20s | ease | transform: translateY(-3px) |
| Button background on hover | 0.15s | ease | background-color |
| Button shadow on hover | 0.15s | ease | box-shadow |
| Grade row on hover | 0.18s | ease | background, transform: translateX(4px) |
| Theme switch | 0.25s | ease | background, color (`:root` only) |
| Opening card entrance | 0.45s | cubic-bezier(0.22,1,0.36,1) | opacity + translateY — **one-shot only** |

### Prohibited

- `animation-iteration-count: infinite` on any property
- Continuous `@keyframes` loops (e.g., `subtlePulse`, particle, aurora)
- `animation-duration` > 600ms on UI chrome elements
- Parallax or scroll-triggered motion
- Animated SVG path drawing

### Reduced-Motion Requirement

**All** `@keyframes` animations must be wrapped:
```css
@media (prefers-reduced-motion: no-preference) {
  .open-card { animation: slideUp 0.45s cubic-bezier(0.22,1,0.36,1) both; }
  /* … all other animations … */
}
```

---

## 9. Accessibility Standards (WCAG 2.2 AA)

| Requirement | Target |
|-------------|--------|
| Body text contrast | ≥ 4.5:1 |
| Large / bold text (≥ 18px or 14px bold) | ≥ 3.0:1 |
| Touch target size | ≥ 44 × 44 CSS px |
| Focus indicator | 2px solid `--accent-primary`, 2px offset |
| Color-only communication | Never — always pair with icon + text |
| Minimum font size | 11px |
| Heading hierarchy | Single H1 per page; H2/H3 in logical order |

---

## 10. Mobile and Responsive Behavior

Streamlit does not expose Python-level breakpoints. Use CSS-only:

```css
/* 2×2 KPI grid on tablets */
@media (max-width: 768px) {
  div[data-testid="metric-container"] {
    min-width: calc(50% - 8px);
  }
}

/* Full-width KPI cards on phones */
@media (max-width: 480px) {
  div[data-testid="metric-container"] {
    min-width: 100%;
  }
  .open-card {
    padding: 32px 20px 28px;
  }
  .open-team-members {
    flex-direction: column;
    gap: 6px;
  }
}
```

| Breakpoint | Behavior |
|-----------|---------|
| > 1024px | Sidebar visible; 4-column KPI row; 2-column chart row |
| 768–1024px | Sidebar collapsible; KPI may wrap 2+2 |
| 480–768px | Sidebar collapses; KPI cards 2×2 |
| < 480px | Single column; KPI full-width; opening card compact; members stacked |

---

*Smart GPA Calculator — Team WebForge — Design System v2.0*
