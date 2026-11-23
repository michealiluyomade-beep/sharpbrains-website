# Sharp Brains Schools — Website

Plain static HTML/CSS/JS. No build step, no framework — works out of the box on Vercel.

## Pages

- `index.html` — Home
- `about.html` — About / mission / leadership
- `academics.html` — Curriculum (Nursery, Primary, JSS, SSS streams) + facilities
- `admissions.html` — Admissions process, fees, FAQ
- `gallery.html` — Photo gallery
- `contact.html` — Contact details + inquiry form
- `news.html` — News & events (optional page, built but not in the main nav)
- `staff.html` — Full staff directory (optional page, built but not in the main nav)

Shared styles live in `assets/styles.css`, shared behavior (mobile nav, FAQ accordion, form handler) in `assets/main.js`.

## Deploying to Vercel

**Option A — Vercel CLI**
```
npm i -g vercel
cd sharp-brains-site
vercel
```
Follow the prompts (link/create a project). Vercel auto-detects this as a static site — no framework or build command needed.

**Option B — GitHub + Vercel dashboard**
1. Push this folder to a GitHub repo.
2. On vercel.com, "Add New Project" → import the repo.
3. Framework preset: "Other" (or leave auto-detected). Build command: none. Output directory: `.` (root).
4. Deploy.

## Before going live — replace these

- Every `[bracketed placeholder]`: stats, fees, staff names, contact info, testimonials, dates.
- `[ Photo ]` / `[ Map embed placeholder ]` blocks: swap for real photos and a real Google Maps embed.
- The inquiry form on `contact.html` doesn't submit anywhere yet (see the comment in `assets/main.js`) — wire it to GoHighLevel, Formspree, or your own backend before launch.
- Google Fonts are loaded from `fonts.googleapis.com` via `<link>` in each page's `<head>` — no action needed, just note it's an external request.

## Adding News / Staff to the main nav

Both pages exist and are linked from the footer ("MORE") and from relevant spots on other pages, but aren't in the top nav to keep it short. To add them, edit the `NAV` list in `generate.py` and re-run `python3 generate.py`, or just add the `<a>` links by hand in each page's `.nav-links` block.
