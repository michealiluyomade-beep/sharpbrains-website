#!/usr/bin/env python3
"""Generates the Sharp Brains Schools static site pages from shared head/header/footer."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Home", "home", "#3B82F6"),
    ("about.html", "About", "info", "#F97316"),
    ("academics.html", "Academics", "book", "#22C55E"),
    ("admissions.html", "Admissions", "file", "#EF4444"),
    ("gallery.html", "Gallery", "image", "#8B5CF6"),
    ("contact.html", "Contact", "mail", "#06B6D4"),
]

# Minimal lucide-style icon paths (24x24, stroke=currentColor) for the glow nav.
NAV_ICONS = {
    "home": '<path d="M3 9.5 12 3l9 6.5V21a1 1 0 0 1-1 1h-5v-7H9v7H4a1 1 0 0 1-1-1V9.5Z"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    "book": '<path d="M12 7c-2-2-5-2-8-2v13c3 0 6 0 8 2 2-2 5-2 8-2V5c-3 0-6 0-8 2Z"/><path d="M12 7v13"/>',
    "file": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"/><path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h6"/>',
    "image": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 7 10-7"/>',
    "arrow": '<path d="M7 17 17 7"/><path d="M7 7h10v10"/>',
}

def nav_icon_svg(key):
    return (
        f'<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{NAV_ICONS[key]}</svg>'
    )

def head(title, description):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Sharp Brains Schools</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
"""

def header(active):
    links = []
    for href, label, icon_key, color in NAV:
        cls = ' active' if href == active else ''
        glow = f"radial-gradient(circle, {color}33 0%, {color}14 50%, transparent 100%)"
        style = f'style="--glow:{glow};--accent:{color};"'
        links.append(
            f'<a href="{href}" class="glow-link{cls}" {style}>'
            f'{nav_icon_svg(icon_key)}<span>{label}</span></a>'
        )
    links_html = "\n        ".join(links)
    return f"""<header class="site-header">
  <div class="container nav-row">
    <a href="index.html" class="brand">
      <img src="assets/logo.jpg" alt="Sharp Brain International Schools logo" class="brand-mark">
      <div class="brand-text">
        <span class="name">Sharp Brains</span>
        <span class="sub">INTERNATIONAL SCHOOLS</span>
      </div>
    </a>
    <button class="nav-toggle" aria-label="Toggle menu">&#9776;</button>
    <nav class="nav-links glow-nav">
        {links_html}
    </nav>
    <a href="admissions.html" class="btn btn-amber">Book a Tour</a>
  </div>
</header>
"""

FOOTER = """<section class="cta-split">
  <div class="cta-split-photo">
    <img src="assets/gallery/cutout-cultural-day-girl.png" alt="Sharp Brains pupil in traditional Cultural Day attire">
  </div>
  <div class="container cta-split-inner">
    <div class="cta-split-text">
      <span class="cta-eyebrow">Let's Connect</span>
      <h2>Give Your Child a Bright Beginning</h2>
      <p>Looking to give your child a joyful, nurturing start? Sharp Brains Schools is now enrolling for the [2026/2027] academic session.</p>
      <a href="admissions.html" class="btn-cta-orange">Enroll Your Child</a>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="container">
    <div class="footer-cols">
      <div class="footer-col">
        <div class="brand">
          <img src="assets/logo.jpg" alt="Sharp Brain International Schools logo" class="brand-mark" style="width:38px;height:38px;">
          <span style="font-family:'Poppins';font-weight:700;font-size:17px;color:#fff;">Sharp Brains</span>
        </div>
        <p style="font-size:13px;line-height:1.6;color:#8890AD;">Nurturing sharp minds from Nursery through Senior Secondary in Ikosi Ketu, Lagos, Nigeria.</p>
      </div>
      <div class="footer-col">
        <h4>QUICK LINKS</h4>
        <a href="about.html">About</a>
        <a href="academics.html">Academics</a>
        <a href="admissions.html">Admissions</a>
        <a href="gallery.html">Gallery</a>
      </div>
      <div class="footer-col">
        <h4>MORE</h4>
        <a href="staff.html">Our Staff</a>
        <a href="news.html">News &amp; Events</a>
        <a href="contact.html">Contact</a>
      </div>
      <div class="footer-col">
        <h4>CONTACT</h4>
        <span>3 Aina Road, Ikosi Ketu, Agiliti Mile 12, Lagos, Nigeria</span>
        <span>0803 344 4284 (Call/WhatsApp)</span>
        <span>trustodih334@gmail.com</span>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; [2026] Sharp Brains Schools. All rights reserved.</span>
      <div class="social-row">
        <span class="social-btn" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37a4 4 0 1 1-7.914 1.173A4 4 0 0 1 16 11.37z"/><path d="M17.5 6.5h.01"/></svg></span>
        <a class="social-btn" href="https://www.facebook.com/p/SharpBrains-Intl-College-100043473537283/" target="_blank" rel="noopener" aria-label="Facebook"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
        <span class="social-btn" aria-label="WhatsApp"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.65-4.95A8.5 8.5 0 1 1 8.95 19.3z"/><path d="M8.5 9.5c0 3.5 2.5 6 6 6 .5 0 .9-.5.8-1l-.3-1.3a.8.8 0 0 0-.9-.6l-1.3.3a5 5 0 0 1-2.7-2.7l.3-1.3a.8.8 0 0 0-.6-.9L8.5 7.7c-.5-.1-1 .3-1 .8z"/></svg></span>
      </div>
    </div>
  </div>
  <div class="footer-wordmark-wrap" data-reveal>
    <span class="footer-glow-dot"></span>
    <span class="footer-wordmark">Sharp Brains</span>
  </div>
</footer>
<script src="assets/main.js"></script>
<script src="assets/footer-reveal.js"></script>
</body>
</html>
"""

def write_page(filename, title, description, active, body, extra_scripts=""):
    content = head(title, description) + header(active) + body + extra_scripts + FOOTER
    with open(os.path.join(ROOT, filename), "w") as f:
        f.write(content)
    print(f"wrote {filename}")

# ---------------------------------------------------------------- HOME ----

# Testimonials data, shared by the 3D marquee on the homepage.
TESTIMONIALS = [
    {
        "initials": "FA", "color": "var(--navy)",
        "name": "Mrs. Folakemi Adeyemi", "role": "Parent of JSS2 Student",
        "text": "My son was shy and struggled to speak up in class. In under a year at Sharp Brains, he's become one of the most confident pupils in his set.",
    },
    {
        "initials": "CO", "color": "var(--amber)",
        "name": "Mr. Chidi Okonkwo", "role": "Parent of Primary 4 Student",
        "text": "What stood out to me was how often the teachers reached out, not just at report card time. We always felt in the loop all through the term.",
    },
    {
        "initials": "AB", "color": "#4D5BCE",
        "name": "Mrs. Aisha Bello", "role": "Parent of SSS3 Student",
        "text": "Our daughter sat WAEC this year and the results more than justified the hours the teachers put into exam prep.",
    },
    {
        "initials": "EN", "color": "var(--navy)",
        "name": "Mr. Emeka Nwosu", "role": "Parent of Nursery 2 Student",
        "text": "As a parent dropping off a toddler every morning, safety was my biggest worry. The gate and classroom supervision put that to rest fast.",
    },
    {
        "initials": "TA", "color": "var(--amber)",
        "name": "Mrs. Temitope Adebayo", "role": "Parent of Primary 6 Student",
        "text": "The excursions make all the difference. My daughter still talks about the Badagry trip, months later.",
    },
    {
        "initials": "IY", "color": "#4D5BCE",
        "name": "Ibrahim Yusuf", "role": "Alumnus, Class of 2021",
        "text": "Sharp Brains gave me more than a certificate. The discipline I picked up there is something I still carry into university.",
    },
]

def testi_mini_card(t):
    return f"""<div class="testi-mini-card">
          <div class="testi-mini-head">
            <span class="testi-mini-avatar" style="background:{t['color']};">{t['initials']}</span>
            <div><p class="testi-mini-name">{t['name']}</p><p class="testi-mini-role">{t['role']}</p></div>
          </div>
          <p class="testi-mini-text">&ldquo;{t['text']}&rdquo;</p>
        </div>"""

def testi_column(indices, direction, duration):
    cards = "\n        ".join(testi_mini_card(TESTIMONIALS[i]) for i in indices)
    # Render the set twice back-to-back so the loop (translateY -50%) is seamless.
    return f"""<div class="testi-3d-col">
      <div class="testi-3d-track testi-3d-{direction}" style="animation-duration:{duration}s;">
        {cards}
        {cards}
      </div>
    </div>"""

def testimonial_marquee():
    return f"""<div class="container">
    <div class="testi-3d-wrap">
      <div class="testi-3d-stage">
        {testi_column([0, 1, 2], "up", 26)}
        {testi_column([3, 4, 5], "down", 30)}
        {testi_column([2, 4, 0], "up", 23)}
        {testi_column([5, 1, 3], "down", 28)}
      </div>
      <div class="testi-3d-fade testi-3d-fade-top"></div>
      <div class="testi-3d-fade testi-3d-fade-bottom"></div>
      <div class="testi-3d-fade testi-3d-fade-left"></div>
      <div class="testi-3d-fade testi-3d-fade-right"></div>
    </div>
  </div>"""

home_body = f"""
<section class="hero">
  <div class="hero-aura hero-aura-a"></div>
  <div class="hero-aura hero-aura-b"></div>
  <div class="container hero-flex">
    <div class="hero-copy">
      <span class="eyebrow hero-in" style="--d:0s">NURSERY &middot; PRIMARY &middot; SECONDARY</span>
      <h1 class="hero-in" style="--d:0.08s;font-size:50px;font-weight:800;line-height:1.12;color:#fff;">Where Sharp Minds Are Built, From First Steps to WAEC</h1>
      <p class="hero-in" style="--d:0.16s;font-size:18px;line-height:1.6;color:#C7CCE6;max-width:540px;">Sharp Brains Schools nurtures confident, curious learners from Nursery through Senior Secondary, backed by a strong WAEC and NECO track record and a safe, structured environment parents trust.</p>
      <div class="hero-in" style="--d:0.24s;display:flex;gap:16px;flex-wrap:wrap;padding-top:8px;">
        <a href="admissions.html" class="btn btn-amber">Apply for Admission</a>
        <a href="academics.html" class="btn btn-outline-light">Explore Our Programs</a>
      </div>
      <div class="stat-row hero-in" style="--d:0.32s;">
        <div class="stat"><span class="num">[18]+</span><span class="label">Years of Excellence</span></div>
        <div class="stat"><span class="num">[1,200]+</span><span class="label">Students Enrolled</span></div>
        <div class="stat"><span class="num">[92]%</span><span class="label">WAEC Pass Rate</span></div>
      </div>
    </div>
    <div class="hero-art hero-fade-in" style="--d:0.2s;" data-tilt data-tilt-max="8">
      <img src="assets/gallery/trip-03-badagry-gate.jpg" alt="Sharp Brains students on an educational excursion" style="width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:24px;border:1px solid rgba(255,255,255,0.15);">
      <div class="hero-badge">
        <span class="hero-badge-dot"></span>
        <div>
          <strong>Admissions Open</strong>
          <span>2026/2027 Session</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="background:#fff;border-bottom:1px solid var(--border);">
  <div class="container" style="padding:32px;display:flex;flex-wrap:wrap;gap:32px;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:10px;flex:1 1 200px;"><span style="font-size:20px;">&#127963;&#65039;</span><span style="font-weight:600;font-size:14px;color:#353D5C;">Lagos State Ministry of Education Approved</span></div>
    <div style="display:flex;align-items:center;gap:10px;flex:1 1 200px;"><span style="font-size:20px;">&#128221;</span><span style="font-weight:600;font-size:14px;color:#353D5C;">WAEC &amp; NECO Registered Centre</span></div>
    <div style="display:flex;align-items:center;gap:10px;flex:1 1 200px;"><span style="font-size:20px;">&#128105;&#8205;&#127979;</span><span style="font-weight:600;font-size:14px;color:#353D5C;">[15]:1 Student&ndash;Teacher Ratio</span></div>
    <div style="display:flex;align-items:center;gap:10px;flex:1 1 200px;"><span style="font-size:20px;">&#128737;&#65039;</span><span style="font-weight:600;font-size:14px;color:#353D5C;">CCTV-Monitored, Secure Campus</span></div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark">(01) OUR SCHOOL LEVELS</span>
      <h2>One School, One Journey</h2>
      <p class="muted">From a child's very first day in Nursery to their final WAEC exam, every level is built to carry learners confidently into the next.</p>
    </div>
    <div class="grid grid-3">
      <a href="academics.html" class="notch-card" data-tilt>
        <div class="notch-cover">
          <img src="assets/gallery/sports-01-pool.jpg" alt="Sharp Brains Nursery pupils at play">
          <div class="notch-badge"><span>Ages [2] &ndash; [5]</span></div>
          <div class="notch-cut"></div>
          <div class="notch-fillet a"></div>
          <div class="notch-fillet b"></div>
          <span class="notch-arrow">{nav_icon_svg('arrow')}</span>
        </div>
        <h3>Nursery</h3>
        <p class="muted notch-desc">Play-based early learning that builds language, motor skills, and social confidence.</p>
        <div class="notch-tags"><span class="notch-tag">Play-Based</span><span class="notch-tag">Early Years</span></div>
      </a>
      <a href="academics.html" class="notch-card" data-tilt>
        <div class="notch-cover">
          <img src="assets/gallery/trip-07-indoor-group.jpg" alt="Sharp Brains Primary pupils on an excursion">
          <div class="notch-badge"><span>Primary 1 &ndash; 6</span></div>
          <div class="notch-cut"></div>
          <div class="notch-fillet a"></div>
          <div class="notch-fillet b"></div>
          <span class="notch-arrow">{nav_icon_svg('arrow')}</span>
        </div>
        <h3>Primary</h3>
        <p class="muted notch-desc">A strong foundation in literacy, numeracy, and science, plus character-building activities.</p>
        <div class="notch-tags"><span class="notch-tag">Literacy</span><span class="notch-tag">Numeracy</span></div>
      </a>
      <a href="academics.html" class="notch-card" data-tilt>
        <div class="notch-cover">
          <img src="assets/gallery/grad-03-boys-group.jpg" alt="Sharp Brains Secondary students">
          <div class="notch-badge"><span>JSS1&ndash;JSS3 &middot; SSS1&ndash;SSS3</span></div>
          <div class="notch-cut"></div>
          <div class="notch-fillet a"></div>
          <div class="notch-fillet b"></div>
          <span class="notch-arrow">{nav_icon_svg('arrow')}</span>
        </div>
        <h3>Secondary</h3>
        <p class="muted notch-desc">Rigorous WAEC/NECO-aligned teaching across Science, Arts, and Commercial streams.</p>
        <div class="notch-tags"><span class="notch-tag">WAEC / NECO</span><span class="notch-tag">3 Streams</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark" style="color:var(--amber);">(02) RESULTS &amp; ACHIEVEMENTS</span>
      <h2>A Record Parents Can Trust</h2>
    </div>
    <div class="stat-band">
      <div class="stat-band-item"><span class="num">[18]+</span><span class="label">Years of Operation</span></div>
      <div class="stat-band-item"><span class="num">[92]%</span><span class="label">WAEC Pass Rate</span></div>
      <div class="stat-band-item"><span class="num">[1,200]+</span><span class="label">Students Enrolled</span></div>
      <div class="stat-band-item"><span class="num">[300]+</span><span class="label">University Placements</span></div>
    </div>
  </div>
</section>

<section class="section day-section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark">(03) A DAY AT SHARP BRAINS</span>
      <h2>One Day, Told by the Hour</h2>
      <p class="muted">Gates open at 7:00am and the last bus pulls out by 4:00pm. Drag the dot or scroll the cards; they move together.</p>
    </div>
    <div class="day-timeline">
      <div class="day-timeline-labels"><span>7:00 AM</span><span>4:00 PM</span></div>
      <div class="day-track">
        <div class="day-track-fill"></div>
        <div class="day-scrubber"></div>
      </div>
      <div class="day-cards">
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>7:00 AM</span>
          <h3>Resumption</h3>
          <p>Gates open. Uniform and hygiene check, bags dropped, one more hug at the gate.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>7:30 AM</span>
          <h3>Morning Assembly</h3>
          <p>National anthem, pledge, a short devotion, and the day's announcements.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>8:00 AM</span>
          <h3>Periods 1 &amp; 2</h3>
          <p>Core subjects while concentration is freshest: Maths, English, and the Sciences.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>9:40 AM</span>
          <h3>Short Break</h3>
          <p>A quick snack and some fresh air before the next set of lessons.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>10:00 AM</span>
          <h3>Periods 3 &amp; 4</h3>
          <p>Continued classwork across the timetable's core and elective subjects.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>12:00 PM</span>
          <h3>Lunch Break</h3>
          <p>A proper meal, then free play and catching up with friends in the yard.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>12:40 PM</span>
          <h3>Periods 5 &amp; 6</h3>
          <p>Afternoon lessons, practicals, and class exercises.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>2:00 PM</span>
          <h3>Clubs &amp; Activities</h3>
          <p>Sports, clubs, music, and other extracurricular activities.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>2:45 PM</span>
          <h3>Closing Assembly</h3>
          <p>A recap of the day, homework noted down, dismissal by class level.</p>
        </div>
        <div class="day-card">
          <span class="day-card-time"><span class="dot"></span>3:00 PM</span>
          <h3>Closing &amp; Pick-up</h3>
          <p>Buses load up, gates open for pick-up, with aftercare available on request.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark">(04) KIND WORDS</span>
      <h2>What Parents Say</h2>
      <p class="muted">Real feedback from our school community. Swap these in for the real quotes any time.</p>
    </div>
  </div>
  {testimonial_marquee()}
</section>

<section style="background:#000;">
  <div class="container" style="padding-top:64px;padding-bottom:24px;">
    <span class="eyebrow-dark" style="color:var(--amber);">(05) GALLERY PREVIEW</span>
    <h2 style="color:#fff;font-size:32px;font-weight:800;padding-top:12px;">Life at Sharp Brains, in Motion</h2>
    <p style="color:#9BA3C9;max-width:560px;padding-top:10px;font-size:15px;">A running look at campus life. Panels below are placeholders; swap in real photos any time.</p>
  </div>
  <div class="container">
    <div class="bento-grid">
      <a href="gallery.html" class="bento-item big" data-tilt data-tilt-max="6">
        <img src="assets/gallery/culture-01-group-gate.jpg" alt="Sharp Brains pupils on Cultural Day">
        <span class="bento-overlay"><span>Cultural Day</span></span>
      </a>
      <a href="gallery.html" class="bento-item wide">
        <img src="assets/gallery/sports-01-pool.jpg" alt="Sharp Brains pupils at the pool">
        <span class="bento-overlay"><span>Sports &amp; Swimming</span></span>
      </a>
      <a href="gallery.html" class="bento-item">
        <img src="assets/gallery/grad-03-boys-group.jpg" alt="Sharp Brains graduation day">
        <span class="bento-overlay"><span>Graduation Day</span></span>
      </a>
      <a href="gallery.html" class="bento-item">
        <img src="assets/gallery/event-democracy-day-2.jpg" alt="Sharp Brains Democracy Day event">
        <span class="bento-overlay"><span>Democracy Day</span></span>
      </a>
      <a href="gallery.html" class="bento-item wide">
        <img src="assets/gallery/trip-14-boat-ride-a.jpg" alt="Sharp Brains pupils on a boat ride excursion">
        <span class="bento-overlay"><span>Excursions</span></span>
      </a>
      <a href="gallery.html" class="bento-item">
        <img src="assets/gallery/trip-03-badagry-gate.jpg" alt="Sharp Brains pupils on an educational excursion">
        <span class="bento-overlay"><span>Field Trips</span></span>
      </a>
      <a href="gallery.html" class="bento-item">
        <img src="assets/gallery/grad-02-girl-sash.jpg" alt="Sharp Brains graduate in sash">
        <span class="bento-overlay"><span>Our Graduates</span></span>
      </a>
    </div>
  </div>
  <div style="text-align:center;padding:40px 24px 72px;">
    <a href="gallery.html" class="btn btn-amber">View Full Gallery</a>
  </div>
</section>
"""

HOME_EXTRA_SCRIPTS = """
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="assets/day-timeline.js"></script>
<script src="assets/tilt-3d.js"></script>
"""

write_page("index.html", "Home", "Sharp Brains Schools — Nursery, Primary & Secondary education in Nigeria.", "", home_body, extra_scripts=HOME_EXTRA_SCRIPTS)

# ------------------------------------------------------------- ABOUT ----

about_body = """
<section class="page-banner">
  <div class="container">
    <span class="eyebrow">ABOUT US</span>
    <h1 style="color:#fff;font-size:40px;font-weight:800;padding-top:12px;">Our Story</h1>
    <p style="color:#C7CCE6;max-width:560px;padding-top:12px;font-size:16px;">[Add a short paragraph here on when and why the school was founded, who founded it, and how it's grown since.]</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2">
    <div>
      <span class="eyebrow-dark">OUR MISSION</span>
      <h2 style="font-size:28px;padding-top:12px;">[Add a mission statement: what the school exists to do for its students.]</h2>
    </div>
    <div>
      <span class="eyebrow-dark">OUR VISION</span>
      <h2 style="font-size:28px;padding-top:12px;">[Add a vision statement: what the school aims to become.]</h2>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="stat-band">
      <div class="stat-band-item"><span class="num">[18]+</span><span class="label">Years of Operation</span></div>
      <div class="stat-band-item"><span class="num">[1,200]+</span><span class="label">Students Enrolled</span></div>
      <div class="stat-band-item"><span class="num">[92]%</span><span class="label">WAEC Pass Rate</span></div>
      <div class="stat-band-item"><span class="num">[40]+</span><span class="label">Teaching Staff</span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark">LEADERSHIP</span>
      <h2>Led by Educators Who Care</h2>
      <p class="muted">Meet the people guiding Sharp Brains day to day. <a href="staff.html" style="color:var(--indigo);font-weight:700;">See the full staff directory &rarr;</a></p>
    </div>
    <div class="grid grid-4">
      <div class="staff-card">
        <div class="staff-photo">[Photo]</div>
        <div class="staff-accent"></div>
        <p class="staff-name">[Principal's Name]</p>
        <p class="staff-role">Principal</p>
      </div>
      <div class="staff-card">
        <div class="staff-photo">[Photo]</div>
        <div class="staff-accent"></div>
        <p class="staff-name">[Teacher Name]</p>
        <p class="staff-role">Head of Secondary</p>
      </div>
      <div class="staff-card">
        <div class="staff-photo">[Photo]</div>
        <div class="staff-accent"></div>
        <p class="staff-name">[Teacher Name]</p>
        <p class="staff-role">Head of Primary</p>
      </div>
      <div class="staff-card">
        <div class="staff-photo">[Photo]</div>
        <div class="staff-accent"></div>
        <p class="staff-name">[Teacher Name]</p>
        <p class="staff-role">Head of Nursery</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark">ACCREDITATION</span>
      <h2>Recognized &amp; Trusted</h2>
    </div>
    <div class="grid grid-3">
      <div class="card sm">&#127963;&#65039; <strong>Lagos State Ministry of Education:</strong> approved and licensed.</div>
      <div class="card sm">&#128221; <strong>WAEC &amp; NECO:</strong> registered examination centre.</div>
      <div class="card sm">&#127942; <strong>[Award/Body Name]:</strong> [add any other recognition or membership here.]</div>
    </div>
  </div>
</section>
"""

write_page("about.html", "About Us", "The story, mission, and leadership of Sharp Brains Schools.", "about.html", about_body)

# --------------------------------------------------------- ACADEMICS ----

academics_body = """
<section class="page-banner">
  <div class="container">
    <span class="eyebrow">ACADEMICS</span>
    <h1 style="color:#fff;font-size:40px;font-weight:800;padding-top:12px;">A Curriculum Built for Every Stage</h1>
    <p style="color:#C7CCE6;max-width:560px;padding-top:12px;font-size:16px;">From Nursery through SSS3, every level has a clear academic focus aimed at building confident, exam-ready students.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-3">
    <div class="card">
      <div class="card-icon" style="background:#FDF1DC;">&#129498;</div>
      <h3 style="font-size:18px;">Nursery (Ages [2]&ndash;[5])</h3>
      <p class="muted" style="font-size:14px;">Phonics, numbers, motor skills, and guided play that prepares children for formal schooling.</p>
    </div>
    <div class="card">
      <div class="card-icon" style="background:#E7EAFB;">&#128218;</div>
      <h3 style="font-size:18px;">Primary (P1&ndash;P6)</h3>
      <p class="muted" style="font-size:14px;">Core literacy, numeracy, basic science, and creative arts, building toward the Common Entrance exam.</p>
    </div>
    <div class="card">
      <div class="card-icon" style="background:#DEE9FF;">&#127891;</div>
      <h3 style="font-size:18px;">Secondary (JSS1&ndash;SSS3)</h3>
      <p class="muted" style="font-size:14px;">BECE preparation in JSS, then streamed WAEC/NECO/JAMB preparation from SSS1.</p>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container grid grid-2">
    <div>
      <span class="eyebrow-dark">JUNIOR SECONDARY (JSS1 &ndash; JSS3)</span>
      <h2 style="font-size:28px;padding-top:12px;">A Broad, Balanced Foundation</h2>
      <p class="muted" style="padding-top:12px;">Prepares students for the Basic Education Certificate Examination (BECE) and sets the foundation for senior secondary streaming.</p>
      <div class="pill-row">
        <span class="tag">Mathematics</span>
        <span class="tag">English Studies</span>
        <span class="tag">Basic Science &amp; Technology</span>
        <span class="tag">Social Studies</span>
        <span class="tag">Computer Studies</span>
        <span class="tag">French</span>
        <span class="tag">Civic Education</span>
      </div>
    </div>
    <div>
      <span class="eyebrow-dark">SENIOR SECONDARY (SSS1 &ndash; SSS3)</span>
      <h2 style="font-size:28px;padding-top:12px;">Three Streams, One Standard</h2>
      <p class="muted" style="padding-top:12px;">Students choose a stream from SSS1, with focused WAEC/NECO/JAMB preparation and regular mock exams.</p>
      <div style="display:flex;flex-direction:column;gap:12px;padding-top:12px;">
        <div class="stream-row"><span style="font-size:20px;">&#129514;</span><div><p style="font-weight:700;font-size:15px;">Science</p><p style="font-size:13px;color:var(--muted-2);">Physics, Chemistry, Biology, Further Maths</p></div></div>
        <div class="stream-row"><span style="font-size:20px;">&#127917;</span><div><p style="font-weight:700;font-size:15px;">Arts</p><p style="font-size:13px;color:var(--muted-2);">Literature, Government, History, CRS/IRS</p></div></div>
        <div class="stream-row"><span style="font-size:20px;">&#128202;</span><div><p style="font-weight:700;font-size:15px;">Commercial</p><p style="font-size:13px;color:var(--muted-2);">Accounting, Commerce, Economics, Business Studies</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark">LEARNING ENVIRONMENT</span>
      <h2>Facilities That Support the Curriculum</h2>
    </div>
    <div class="grid grid-3">
      <div class="card sm"><span style="font-size:26px;">&#128300;</span><h3 style="font-size:17px;padding-top:8px;">Science Laboratories</h3><p class="muted" style="font-size:14px;">Fully-equipped Physics, Chemistry &amp; Biology labs for hands-on learning.</p></div>
      <div class="card sm"><span style="font-size:26px;">&#128187;</span><h3 style="font-size:17px;padding-top:8px;">ICT &amp; Computer Lab</h3><p class="muted" style="font-size:14px;">Modern computers with internet access for digital literacy and coding.</p></div>
      <div class="card sm"><span style="font-size:26px;">&#128214;</span><h3 style="font-size:17px;padding-top:8px;">Library &amp; Resource Centre</h3><p class="muted" style="font-size:14px;">A quiet, well-stocked space for reading, research, and study.</p></div>
      <div class="card sm"><span style="font-size:26px;">&#9917;</span><h3 style="font-size:17px;padding-top:8px;">Sports Complex</h3><p class="muted" style="font-size:14px;">Football field, basketball &amp; volleyball courts for an active lifestyle.</p></div>
      <div class="card sm"><span style="font-size:26px;">&#127912;</span><h3 style="font-size:17px;padding-top:8px;">Art, Music &amp; Drama</h3><p class="muted" style="font-size:14px;">Creative studios where students explore talents beyond the classroom.</p></div>
      <div class="card sm"><span style="font-size:26px;">&#127973;</span><h3 style="font-size:17px;padding-top:8px;">School Clinic</h3><p class="muted" style="font-size:14px;">An on-site nurse and first-aid facility for student wellbeing.</p></div>
    </div>
  </div>
</section>
"""

write_page("academics.html", "Academics", "Curriculum details for Nursery, Primary, and Secondary (JSS/SSS) at Sharp Brains Schools.", "academics.html", academics_body)

# -------------------------------------------------------- ADMISSIONS ----

admissions_body = """
<section class="page-banner">
  <div class="container">
    <span class="eyebrow">ADMISSIONS</span>
    <h1 style="color:#fff;font-size:40px;font-weight:800;padding-top:12px;">How to Enroll</h1>
    <p style="color:#C7CCE6;max-width:560px;padding-top:12px;font-size:16px;">Admission for the [20XX/20XX] session is open. Here's how the process works.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-4">
    <div>
      <span style="font-family:'Poppins';font-weight:800;font-size:26px;color:var(--amber-dark);">01</span>
      <h3 style="font-size:16px;padding-top:10px;">Submit Inquiry</h3>
      <p class="muted" style="font-size:13px;padding-top:6px;">Fill the enquiry form or visit the school office.</p>
    </div>
    <div>
      <span style="font-family:'Poppins';font-weight:800;font-size:26px;color:var(--amber-dark);">02</span>
      <h3 style="font-size:16px;padding-top:10px;">Entrance Assessment</h3>
      <p class="muted" style="font-size:13px;padding-top:6px;">A short placement test in English &amp; Mathematics.</p>
    </div>
    <div>
      <span style="font-family:'Poppins';font-weight:800;font-size:26px;color:var(--amber-dark);">03</span>
      <h3 style="font-size:16px;padding-top:10px;">Interview</h3>
      <p class="muted" style="font-size:13px;padding-top:6px;">A short meeting with the student and parent(s).</p>
    </div>
    <div>
      <span style="font-family:'Poppins';font-weight:800;font-size:26px;color:var(--amber-dark);">04</span>
      <h3 style="font-size:16px;padding-top:10px;">Offer &amp; Enrollment</h3>
      <p class="muted" style="font-size:13px;padding-top:6px;">Pay fees and complete registration paperwork.</p>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark">SCHOOL FEES</span>
      <h2>Fees Per Term</h2>
      <p class="muted">Figures below are placeholders. Replace with actual fee amounts before publishing.</p>
    </div>
    <div class="grid grid-3">
      <div class="fee-card">
        <div class="fee-icon">&#129498;</div>
        <h3 class="fee-level">Nursery</h3>
        <p class="fee-price">[&#8358;XX,XXX]</p>
        <p class="fee-term">per term</p>
        <div class="fee-divider"></div>
        <p class="fee-includes">Includes tuition, workbooks &amp; activity fees.</p>
      </div>
      <div class="fee-card">
        <div class="fee-icon">&#128218;</div>
        <h3 class="fee-level">Primary</h3>
        <p class="fee-price">[&#8358;XX,XXX]</p>
        <p class="fee-term">per term</p>
        <div class="fee-divider"></div>
        <p class="fee-includes">Includes tuition, textbooks &amp; activity fees.</p>
      </div>
      <div class="fee-card">
        <div class="fee-icon">&#127891;</div>
        <h3 class="fee-level">Secondary</h3>
        <p class="fee-price">[&#8358;XX,XXX]</p>
        <p class="fee-term">per term</p>
        <div class="fee-divider"></div>
        <p class="fee-includes">Includes tuition, textbooks, labs &amp; WAEC/NECO prep.</p>
      </div>
    </div>
    <div style="padding-top:24px;text-align:center;">
      <a href="contact.html" class="btn btn-amber">Request Full Fee Schedule</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:860px;">
    <div class="section-head center">
      <span class="eyebrow-dark">FAQ</span>
      <h2>Common Questions</h2>
    </div>
    <div class="liquid-faq" data-tone="light">
      <span class="lf-pool" aria-hidden="true"></span>
      <div class="lf-item">
        <h3 class="lf-h"><button class="lf-q" aria-expanded="false">
          <span class="lf-qt">Do you offer both day and boarding options?</span><span class="lf-ico" aria-hidden="true"></span>
        </button></h3>
        <div class="lf-panel"><div class="lf-inner"><div class="lf-a">[Add an answer here: describe day/boarding options, hostel facilities, and pickup arrangements.]</div></div></div>
      </div>
      <div class="lf-item">
        <h3 class="lf-h"><button class="lf-q" aria-expanded="false">
          <span class="lf-qt">What exam boards do you prepare students for?</span><span class="lf-ico" aria-hidden="true"></span>
        </button></h3>
        <div class="lf-panel"><div class="lf-inner"><div class="lf-a">[Add an answer here: e.g. WAEC, NECO, and JAMB, with mock exam schedule details.]</div></div></div>
      </div>
      <div class="lf-item">
        <h3 class="lf-h"><button class="lf-q" aria-expanded="false">
          <span class="lf-qt">Is there an entrance exam for new students?</span><span class="lf-ico" aria-hidden="true"></span>
        </button></h3>
        <div class="lf-panel"><div class="lf-inner"><div class="lf-a">[Add an answer here: describe the assessment subjects and format for each level.]</div></div></div>
      </div>
      <div class="lf-item">
        <h3 class="lf-h"><button class="lf-q" aria-expanded="false">
          <span class="lf-qt">What is the school's fee payment structure?</span><span class="lf-ico" aria-hidden="true"></span>
        </button></h3>
        <div class="lf-panel"><div class="lf-inner"><div class="lf-a">[Add an answer here: termly or annual payment, installment options, and accepted payment methods.]</div></div></div>
      </div>
      <div class="lf-item">
        <h3 class="lf-h"><button class="lf-q" aria-expanded="false">
          <span class="lf-qt">Do you provide transportation (school bus) services?</span><span class="lf-ico" aria-hidden="true"></span>
        </button></h3>
        <div class="lf-panel"><div class="lf-inner"><div class="lf-a">[Add an answer here: list routes and whether it's included in fees or optional.]</div></div></div>
      </div>
    </div>
  </div>
</section>
"""

ADMISSIONS_EXTRA_SCRIPTS = """
<script src="assets/liquid-faq.js"></script>
"""

write_page("admissions.html", "Admissions", "How to enroll at Sharp Brains Schools: process, fees, and FAQs.", "admissions.html", admissions_body, extra_scripts=ADMISSIONS_EXTRA_SCRIPTS)

# ----------------------------------------------------------- GALLERY ----

def gallery_grid(n, colors):
    items = []
    for i in range(n):
        c = colors[i % len(colors)]
        items.append(f'<div class="gallery-item" style="background:{c};display:flex;align-items:center;justify-content:center;color:var(--muted-2);font-size:12px;font-weight:600;">[Photo]</div>')
    return "\n      ".join(items)

def photo_grid(paths, alt):
    items = []
    for p in paths:
        items.append(f'<div class="gallery-item" style="overflow:hidden;"><img src="{p}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;"></div>')
    return "\n      ".join(items)

colors = ["#E7EAFB", "#DEE9FF", "#FDF1DC"]

EXCURSION_PHOTOS = [
    "assets/gallery/trip-01-museum-group.jpg",
    "assets/gallery/trip-02-horse-ride.jpg",
    "assets/gallery/trip-03-badagry-gate.jpg",
    "assets/gallery/trip-04-baracoon-group.jpg",
    "assets/gallery/trip-05-beach-group.jpg",
    "assets/gallery/trip-06-aquarium-visit.jpg",
    "assets/gallery/trip-07-indoor-group.jpg",
    "assets/gallery/trip-08-bamboo-forest-a.jpg",
    "assets/gallery/trip-08-bamboo-forest-b.jpg",
    "assets/gallery/trip-09-pond-lineup.jpg",
    "assets/gallery/trip-10-badagry-monument.jpg",
    "assets/gallery/trip-11-horse-ride-b.jpg",
    "assets/gallery/trip-12-horse-ride-c.jpg",
    "assets/gallery/trip-13-horse-ride-d.jpg",
    "assets/gallery/trip-14-boat-ride-a.jpg",
    "assets/gallery/trip-15-boat-ride-b.jpg",
    "assets/gallery/trip-16-boat-ride-c.jpg",
]

CELEBRATION_PHOTOS = [
    "assets/gallery/event-democracy-day-1.jpg",
    "assets/gallery/event-democracy-day-2.jpg",
    "assets/gallery/event-democracy-day-3.jpg",
]

CULTURE_PHOTOS = [
    "assets/gallery/culture-01-group-gate.jpg",
    "assets/gallery/culture-02-four-girls.jpg",
    "assets/gallery/culture-03-studio-girl.jpg",
    "assets/gallery/culture-04-group-indoor.jpg",
    "assets/gallery/culture-05-dance.jpg",
]

GRADUATION_PHOTOS = [
    "assets/gallery/grad-01-boys-native.jpg",
    "assets/gallery/grad-02-girl-sash.jpg",
    "assets/gallery/grad-03-boys-group.jpg",
    "assets/gallery/grad-04-girls-purple.jpg",
]

SPORTS_PHOTOS = [
    "assets/gallery/sports-01-pool.jpg",
    "assets/gallery/sports-02-house-trophy.jpg",
]

STAFF_CANDID_PHOTOS = [
    "assets/gallery/staff-01-gallery-visit.jpg",
    "assets/gallery/staff-02-beach.jpg",
]

gallery_body = f"""
<section class="page-banner">
  <div class="container">
    <span class="eyebrow">GALLERY</span>
    <h1 style="color:#fff;font-size:40px;font-weight:800;padding-top:12px;">Life at Sharp Brains</h1>
    <p style="color:#C7CCE6;max-width:560px;padding-top:12px;font-size:16px;">Excursions, celebrations, and everyday moments from around the school.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Videos</h2>
    <div class="grid grid-2">
      <div class="video-card">
        <video controls preload="metadata" poster="assets/videos/video-01-poster.jpg">
          <source src="assets/videos/video-01.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-card">
        <video controls preload="metadata" poster="assets/videos/video-02-poster.jpg">
          <source src="assets/videos/video-02.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-card">
        <video controls preload="metadata" poster="assets/videos/video-03-poster.jpg">
          <source src="assets/videos/video-03.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-card">
        <video controls preload="metadata" poster="assets/videos/video-04-poster.jpg">
          <source src="assets/videos/video-04.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Educational Excursions</h2>
    <div class="grid grid-4">
      {photo_grid(EXCURSION_PHOTOS, "Sharp Brains students on an educational excursion")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Celebrations</h2>
    <div class="grid grid-3">
      {photo_grid(CELEBRATION_PHOTOS, "Sharp Brains students celebrating Democracy Day")}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Cultural Day</h2>
    <div class="grid grid-3">
      {photo_grid(CULTURE_PHOTOS, "Sharp Brains students in traditional attire on Cultural Day")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Graduation Day</h2>
    <div class="grid grid-4">
      {photo_grid(GRADUATION_PHOTOS, "Sharp Brains graduation day")}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Campus &amp; Classrooms</h2>
    <p class="muted" style="padding-bottom:24px;">More photos coming soon.</p>
    <div class="grid grid-4">
      {gallery_grid(4, colors)}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Sports &amp; Activities</h2>
    <div class="grid grid-3">
      {photo_grid(SPORTS_PHOTOS, "Sharp Brains students in sports and pool activities")}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Our Team, In Action</h2>
    <div class="grid grid-3">
      {photo_grid(STAFF_CANDID_PHOTOS, "Sharp Brains staff on an excursion")}
    </div>
  </div>
</section>
"""

write_page("gallery.html", "Gallery", "Photos of campus life, classrooms, sports, and events at Sharp Brains Schools.", "gallery.html", gallery_body)

# ----------------------------------------------------------- CONTACT ----

contact_body = """
<section class="page-banner">
  <div class="container">
    <span class="eyebrow">CONTACT</span>
    <h1 style="color:#fff;font-size:40px;font-weight:800;padding-top:12px;">Get in Touch</h1>
    <p style="color:#C7CCE6;max-width:560px;padding-top:12px;font-size:16px;">Questions about admissions, fees, or a campus visit? Reach out any time.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2">
    <div style="display:flex;flex-direction:column;gap:24px;">
      <div class="card sm">
        <h3 style="font-size:16px;">&#128205; Address</h3>
        <p class="muted" style="font-size:14px;padding-top:6px;">3 Aina Road, Ikosi Ketu, Agiliti Mile 12, Lagos, Nigeria</p>
      </div>
      <div class="card sm">
        <h3 style="font-size:16px;">&#128222; Phone / WhatsApp</h3>
        <p class="muted" style="font-size:14px;padding-top:6px;">0803 344 4284</p>
      </div>
      <div class="card sm">
        <h3 style="font-size:16px;">&#9993;&#65039; Email</h3>
        <p class="muted" style="font-size:14px;padding-top:6px;">trustodih334@gmail.com</p>
      </div>
      <div class="card sm">
        <h3 style="font-size:16px;">&#128337; Office Hours</h3>
        <p class="muted" style="font-size:14px;padding-top:6px;">Mon &ndash; Fri, [8:00 AM] &ndash; [4:00 PM]</p>
      </div>
      <div class="placeholder-block light" style="aspect-ratio:16/9;">[ Map embed placeholder ]</div>
    </div>

    <form id="inquiry-form" style="display:flex;flex-direction:column;gap:16px;background:var(--bg-alt);padding:32px;border-radius:20px;">
      <h3 style="font-size:18px;">Send an Inquiry</h3>
      <div class="field">
        <label for="parent-name">Parent / Guardian Name</label>
        <input id="parent-name" type="text" name="parent_name" required>
      </div>
      <div class="field">
        <label for="phone">Phone Number</label>
        <input id="phone" type="tel" name="phone" required>
      </div>
      <div class="field">
        <label for="level">Level of Interest</label>
        <select id="level" name="level">
          <option>Nursery</option>
          <option>Primary</option>
          <option>Secondary (JSS)</option>
          <option>Secondary (SSS)</option>
        </select>
      </div>
      <div class="field">
        <label for="message">Message</label>
        <textarea id="message" name="message" placeholder="Tell us a bit about your child and what you'd like to know."></textarea>
      </div>
      <button type="submit" class="btn btn-amber">Send Inquiry</button>
      <p id="form-note" class="muted" style="display:none;font-size:13px;"></p>
    </form>
  </div>
</section>
"""

write_page("contact.html", "Contact", "Contact Sharp Brains Schools for admissions inquiries, fees, or a campus visit.", "contact.html", contact_body)

# -------------------------------------------------------------- NEWS ----

news_body = """
<section class="page-banner">
  <div class="container">
    <span class="eyebrow">NEWS &amp; EVENTS</span>
    <h1 style="color:#fff;font-size:40px;font-weight:800;padding-top:12px;">What's Happening at Sharp Brains</h1>
    <p style="color:#C7CCE6;max-width:560px;padding-top:12px;font-size:16px;">Updates, announcements, and upcoming events from around the school.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-3">
    <div class="card" style="padding:0;overflow:hidden;">
      <img src="assets/gallery/event-democracy-day-1.jpg" alt="Sharp Brains Democracy Day celebration" style="width:100%;aspect-ratio:4/3;object-fit:cover;">
      <div style="padding:24px;">
        <span class="tag">June 12</span>
        <h3 style="font-size:17px;padding-top:10px;">Happy Democracy Day, Nigeria!</h3>
        <p class="muted" style="font-size:14px;">Students marked Democracy Day with a celebration of freedom, unity, and the power of every voice: one nation, one future.</p>
      </div>
    </div>
    <div class="card" style="padding:0;overflow:hidden;">
      <div class="placeholder-block light" style="aspect-ratio:4/3;border-radius:0;">[Photo]</div>
      <div style="padding:24px;">
        <span class="tag">[Date]</span>
        <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
        <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
      </div>
    </div>
    <div class="card" style="padding:0;overflow:hidden;">
      <div class="placeholder-block light" style="aspect-ratio:4/3;border-radius:0;">[Photo]</div>
      <div style="padding:24px;">
        <span class="tag">[Date]</span>
        <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
        <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
      </div>
    </div>
    <div class="card" style="padding:0;overflow:hidden;">
      <div class="placeholder-block light" style="aspect-ratio:4/3;border-radius:0;">[Photo]</div>
      <div style="padding:24px;">
        <span class="tag">[Date]</span>
        <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
        <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
      </div>
    </div>
    <div class="card" style="padding:0;overflow:hidden;">
      <div class="placeholder-block light" style="aspect-ratio:4/3;border-radius:0;">[Photo]</div>
      <div style="padding:24px;">
        <span class="tag">[Date]</span>
        <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
        <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
      </div>
    </div>
    <div class="card" style="padding:0;overflow:hidden;">
      <div class="placeholder-block light" style="aspect-ratio:4/3;border-radius:0;">[Photo]</div>
      <div style="padding:24px;">
        <span class="tag">[Date]</span>
        <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
        <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
      </div>
    </div>
  </div>
</section>
"""

write_page("news.html", "News & Events", "Latest news, announcements, and upcoming events at Sharp Brains Schools.", "news.html", news_body)

# ------------------------------------------------------------- STAFF ----

staff_body = """
<section class="page-banner">
  <div class="container">
    <span class="eyebrow">OUR TEAM</span>
    <h1 style="color:#fff;font-size:40px;font-weight:800;padding-top:12px;">Meet the Staff</h1>
    <p style="color:#C7CCE6;max-width:560px;padding-top:12px;font-size:16px;">The educators and administrators behind Sharp Brains Schools.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Leadership</h2>
    <div class="grid grid-4">
      <div class="staff-card"><div class="staff-photo">[Photo]</div><div class="staff-accent"></div><p class="staff-name">[Principal's Name]</p><p class="staff-role">Principal</p></div>
      <div class="staff-card"><div class="staff-photo">[Photo]</div><div class="staff-accent"></div><p class="staff-name">[Vice Principal's Name]</p><p class="staff-role">Vice Principal</p></div>
      <div class="staff-card"><div class="staff-photo">[Photo]</div><div class="staff-accent"></div><p class="staff-name">[Name]</p><p class="staff-role">Head of Secondary</p></div>
      <div class="staff-card"><div class="staff-photo">[Photo]</div><div class="staff-accent"></div><p class="staff-name">[Name]</p><p class="staff-role">Head of Primary</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Teaching Staff</h2>
    <div class="grid grid-4">
      <div class="staff-card"><div class="staff-photo">[Photo]</div><div class="staff-accent"></div><p class="staff-name">[Teacher Name]</p><p class="staff-role">[Subject]</p></div>
      <div class="staff-card"><div class="staff-photo">[Photo]</div><div class="staff-accent"></div><p class="staff-name">[Teacher Name]</p><p class="staff-role">[Subject]</p></div>
      <div class="staff-card"><div class="staff-photo">[Photo]</div><div class="staff-accent"></div><p class="staff-name">[Teacher Name]</p><p class="staff-role">[Subject]</p></div>
      <div class="staff-card"><div class="staff-photo">[Photo]</div><div class="staff-accent"></div><p class="staff-name">[Teacher Name]</p><p class="staff-role">[Subject]</p></div>
    </div>
  </div>
</section>
"""

write_page("staff.html", "Our Staff", "Meet the leadership and teaching staff at Sharp Brains Schools.", "staff.html", staff_body)

print("Done.")
