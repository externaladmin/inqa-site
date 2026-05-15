# Site Design System — Template Reference

This file documents the full design system behind this static marketing site. Use it to recreate the same visual language in a new project (Webflow, Astro, Eleventy, or raw HTML). Every pattern here is production-tested.

---

## Brand Tokens

Swap these 4–5 values and the entire site shifts to a new palette.

```css
:root {
  /* Primary accent — buttons, links, highlights */
  --coral: #F27B7B;
  --coral-dark: #993C1D;

  /* Secondary — eyebrows, icons, patina accents */
  --patina: #4A766E;
  --patina-light: #E1F5EE;
  --patina-dark: #0F6E56;

  /* Text hierarchy */
  --espresso: #3D2C2C;   /* headings, bold UI */
  --charcoal: #2D2A2A;   /* body text */
  --slate: #5C5858;      /* secondary / muted text */
  --warm-gray: #7A7170;  /* placeholder text */

  /* Backgrounds */
  --soft-blush: #FAE5E0;  /* hero bg, card fills, tinted sections */
  --warm-white: #FAF8F6;  /* page base background */

  /* Typography */
  --display: 'Montserrat', sans-serif;  /* headings, nav, buttons */
  --body: 'Open Sans', sans-serif;      /* body copy, captions */
}
```

**Google Fonts import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Open+Sans:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
```

---

## Typography Scale

| Element | Font | Weight | Size | Notes |
|---|---|---|---|---|
| `h1.hero-title` | Montserrat | 700 | 75px | line-height: 0.98, letter-spacing: -2.5px |
| `h1 .lighter` | Montserrat | 400 | 0.9em | Softer variant within the h1 |
| `h1 .accent` | — | — | — | color: var(--coral) |
| `h2.section-title` | Montserrat | 700 | 42px | line-height: 1.15, letter-spacing: -0.8px |
| `.hero-eyebrow` | Montserrat | 600 | 12px | uppercase, letter-spacing: 2.5px, color: patina |
| `.eyebrow` (sections) | Montserrat | 600 | 12px | uppercase, letter-spacing: 2.5px |
| `.section-lead` | Open Sans | 400 | 19px | color: slate, line-height: 1.6 |
| `.hero-sub` | Open Sans | 400 | 19px | italic, color: slate |
| Body / `p` | Open Sans | 400 | 17px | line-height: 1.55 |

**Eyebrow pattern** — decorative line before the text:
```css
.eyebrow::before {
  content: "";
  width: 28px;
  height: 1.5px;
  background: var(--patina);
}
```

---

## Layout

- **Max content width:** 1100–1280px centered (`max-width: 1280px; margin: 0 auto`)
- **Section padding:** `100px 56px` (desktop), `60px 24px` (mobile)
- **Hero padding:** `110px 56px 130px`
- **Card gap:** 24px
- **Grid:** CSS Grid, `grid-template-columns: 1fr 1fr` for 2-col; `58fr 42fr` for text/visual splits

---

## Component Library

### Hero Section
```html
<section class="hero">
  <div class="hero-decoration"></div>  <!-- soft radial glow, top-right -->
  <div class="hero-inner">
    <div class="hero-eyebrow">Context line — who this is for</div>
    <h1 class="hero-title">
      <span class="accent">[Brand]</span> is [value prop] <span class="lighter">— [qualifier].</span>
    </h1>
  </div>
  <!-- optional: scrolling gallery strip here -->
  <div class="hero-inner" style="margin-top: 44px;">
    <div class="cta-row">
      <a class="btn btn-primary" href="#contact">Primary CTA</a>
      <a class="btn btn-secondary" href="#how">Secondary CTA</a>
    </div>
  </div>
</section>
```

Hero background is `var(--soft-blush)`. The `.hero-decoration` is a radial gradient circle (480px, positioned top-right) for subtle depth.

---

### Buttons
```html
<a class="btn btn-primary" href="#">Primary</a>    <!-- coral fill -->
<a class="btn btn-secondary" href="#">Secondary</a> <!-- outlined -->
```

```css
.btn {
  font-family: var(--display);
  font-size: 14px;
  font-weight: 600;
  padding: 14px 26px;
  border-radius: 6px;
  letter-spacing: 0.3px;
}
.btn-primary  { background: var(--coral); color: white; }
.btn-secondary { border: 1.5px solid var(--espresso); color: var(--espresso); }
```

---

### Eyebrow + Section Title + Lead (standard section opener)
```html
<div class="eyebrow">Section label</div>
<h2 class="section-title">Main headline —<br><span class="accent">accent phrase.</span></h2>
<p class="section-lead">Supporting sentence that expands the headline. Max ~780px wide.</p>
```

---

### Before / After Diagram (two-row contrast layout)
Dark espresso card = "Today / the problem". Light patina card = "With [product] / the solution".
```html
<section class="diagram-wrapper">
  <div class="diagram-inner">
    <div class="diagram-row today">
      <div class="diagram-label">Today</div>
      <div class="flow">
        <div class="flow-node your-stuff">...</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node leak">...</div>
      </div>
      <p class="diagram-summary">Summary of the problem.</p>
    </div>
    <div class="diagram-row with-inqa">
      <div class="diagram-label">With [Brand]</div>
      ...
    </div>
  </div>
</section>
```

---

### Feature Cards (3-up grid)
```html
<div class="big3-grid">
  <div class="big3-card">
    <div class="big3-number">01</div>
    <div class="big3-icon-slot"><!-- SVG icon --></div>
    <div class="big3-card-title">Feature name</div>
    <p class="big3-card-body">Description.</p>
  </div>
</div>
```

Cards are white, border `rgba(74,118,110,0.15)`, border-radius 16px, padding 36px. Numbers are 64px Montserrat 700, color: patina.

---

### Scrolling Gallery / Marquee Strip
Auto-scrolling row of cards with edge fade. Used to show channel logos, use cases, integrations, etc.
```html
<div class="deploy-marquee-outer">
  <div class="deploy-track"> <!-- animates: marquee-scroll 44s linear infinite -->
    <div class="deploy-card">
      <div class="deploy-card-image"><!-- SVG illustration --></div>
      <div class="deploy-card-body">
        <div class="deploy-label">Label</div>
        <div class="deploy-line">Descriptor → outcome</div>
      </div>
    </div>
    <!-- duplicate cards for seamless loop -->
  </div>
</div>
```

Edge fade via CSS mask:
```css
.deploy-marquee-outer {
  -webkit-mask-image: linear-gradient(to right, transparent 0%, black 8%, black 92%, transparent 100%);
}
@keyframes marquee-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
```
Cards must be duplicated (6 + 6) so the loop is seamless.

---

### Insight / Stat Cards
Dark espresso background. Large number, label, supporting text.
```html
<div class="insight-card">
  <div class="insight-card-stat">3–4x</div>
  <div class="insight-card-label">Stat label</div>
  <p class="insight-card-body">Context sentence.</p>
</div>
```

---

### Two-Column Hero (text + visual mockup)
Used on interior pages (e.g. how-it-works):
```html
<div class="hero-inner" style="display:grid; grid-template-columns: 58fr 42fr; gap: 80px; align-items: center; max-width: 1200px;">
  <div class="hero-text">
    <div class="hero-eyebrow">...</div>
    <h1 class="hero-title" style="font-size:56px;">...</h1>
    <p class="hero-sub">...</p>
    <div class="cta-row">...</div>
  </div>
  <div class="phone-frame">
    <!-- visual mockup -->
  </div>
</div>
```

---

### CSS Phone Frame Mockup
Pure CSS — no images. A dark shell with a white inset screen.
```css
.phone-frame {
  background: var(--charcoal);
  border-radius: 52px;
  padding: 14px;
  box-shadow: 0 48px 120px rgba(61,44,44,0.22), 0 0 0 1px rgba(255,255,255,0.06);
}
/* Speaker notch via ::before, home bar via ::before on phone-home-bar */
```

---

### Contact / CTA Section (bottom of every page)
```html
<section class="contact-wrapper" id="contact">
  <div class="contact-inner">
    <div class="eyebrow">Get in touch</div>
    <h2 class="section-title">Section headline</h2>
    <p class="section-lead">...</p>
    <p style="font-style:italic; font-size:15px; color:var(--slate); margin-bottom:24px;">
      We're working with our first cohort — happy to talk about being in it.
    </p>
    <form id="contact-form" action="https://formspree.io/f/[YOUR_ID]" method="POST">
      <div class="form-row">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Work email" required>
      </div>
      <textarea name="message" placeholder="What are you working on?" rows="4"></textarea>
      <button type="submit" class="btn btn-primary">Send</button>
    </form>
  </div>
</section>
```

Replace `[YOUR_ID]` in the Formspree action URL with your project's form ID.

---

### Nav
```html
<nav>
  <a class="wordmark" href="/">brand<span class="ai">.ai</span></a>
  <ul>
    <li><a href="/how-it-works">How it works</a></li>
    <li><a href="/for-events">Events</a></li>
    <li><a href="#contact" class="btn btn-primary">Talk to us</a></li>
  </ul>
</nav>
```

Nav is `position: sticky; top: 0;` with a `::before` pseudo-element providing the background blur band.

---

## Page Structure (all 5 pages)

| File | Purpose |
|---|---|
| `index.html` | Homepage — positioning, diagram, feature cards, gallery |
| `how-it-works.html` | Product walkthrough — 2-col hero with phone mockup, step-by-step |
| `for-events.html` | Vertical landing page — Events use case |
| `for-funnels.html` | Vertical landing page — Funnels / demand gen use case |
| `about.html` | Team / company — founder portraits, problem story |

Every page shares: nav, contact form at bottom, same CSS token structure. CSS is inlined per-page (no external stylesheet).

---

## Mobile Breakpoints

All responsive rules live in a single `@media (max-width: 768px)` block at the bottom of each file's `<style>` tag.

Key mobile changes:
- Nav links hidden, hamburger optional
- Hero padding → `60px 24px 80px`
- `h1.hero-title` → `font-size: 44px; letter-spacing: -1.5px`
- `h2.section-title` → `font-size: 28px`
- 2-col grids → `grid-template-columns: 1fr`
- Phone frame mockups → `display: none` on mobile

---

## Deployment

- **Host:** Vercel (free tier, auto-deploy from GitHub `main`)
- **Config:** `vercel.json` with `cleanUrls: true` (removes `.html` from URLs)
- **Forms:** Formspree (`formspree.io`) — no backend needed, emails results

```json
{ "cleanUrls": true }
```

---

## What to Replace When Templating

1. **`:root` color tokens** — 4 hex values = full rebrand
2. **Google Fonts link** — swap Montserrat / Open Sans for new typefaces; update `--display` and `--body`
3. **Wordmark / nav links**
4. **All copy** — headlines, body, eyebrows
5. **Formspree ID** in every form action URL
6. **`<title>` tags** on each page
7. **Image assets** — founder portraits (`*_duotone.png`), any photo backgrounds

The SVG illustrations (diagram, feature cards, deploy gallery) are all inline and use brand token colors — they'll recolor automatically when you update the CSS variables.
