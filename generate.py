#!/usr/bin/env python3
"""Generates the Sharp Brains Schools static site pages from shared head/header/footer."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("about.html", "About"),
    ("academics.html", "Academics"),
    ("admissions.html", "Admissions"),
    ("gallery.html", "Gallery"),
    ("contact.html", "Contact"),
]

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
    for href, label in NAV:
        cls = ' class="active"' if href == active else ''
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    links_html = "\n        ".join(links)
    return f"""<header class="site-header">
  <div class="container nav-row">
    <a href="index.html" class="brand">
      <div class="brand-mark">SB</div>
      <div class="brand-text">
        <span class="name">Sharp Brains</span>
        <span class="sub">SCHOOLS</span>
      </div>
    </a>
    <button class="nav-toggle" aria-label="Toggle menu">&#9776;</button>
    <nav class="nav-links">
        {links_html}
    </nav>
    <a href="admissions.html" class="btn btn-amber">Book a Tour</a>
  </div>
</header>
"""

FOOTER = """<section class="cta-band">
  <div class="container cta-band-inner">
    <div>
      <h2>Ready to Give Your Child a Sharp Start?</h2>
      <p>Book a campus tour or apply online in minutes.</p>
    </div>
    <div class="cta-buttons">
      <a href="contact.html" class="btn btn-navy">Book a Tour</a>
      <a href="admissions.html" class="btn btn-white">Apply Now</a>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="container">
    <div class="footer-cols">
      <div class="footer-col">
        <div class="brand">
          <div class="brand-mark" style="width:38px;height:38px;font-size:15px;">SB</div>
          <span style="font-family:'Poppins';font-weight:700;font-size:17px;color:#fff;">Sharp Brains</span>
        </div>
        <p style="font-size:13px;line-height:1.6;color:#8890AD;">Nurturing sharp minds from Nursery through Senior Secondary in [City, State], Nigeria.</p>
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
        <span>[School Address], [City], Nigeria</span>
        <span>[+234 XXX XXX XXXX] (Call/WhatsApp)</span>
        <span>[info@sharpbrains.sch.ng]</span>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; [2026] Sharp Brains Schools. All rights reserved.</span>
      <div class="social-row">
        <span>Instagram</span>
        <span>Facebook</span>
        <span>WhatsApp</span>
      </div>
    </div>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
"""

def write_page(filename, title, description, active, body, extra_scripts=""):
    content = head(title, description) + header(active) + body + extra_scripts + FOOTER
    with open(os.path.join(ROOT, filename), "w") as f:
        f.write(content)
    print(f"wrote {filename}")

# ---------------------------------------------------------------- HOME ----

home_body = """
<section class="hero">
  <div class="container hero-flex">
    <div class="hero-copy">
      <span class="eyebrow">NURSERY &middot; PRIMARY &middot; SECONDARY</span>
      <h1 style="font-size:50px;font-weight:800;line-height:1.12;color:#fff;">Where Sharp Minds Are Built &mdash; From First Steps to WAEC</h1>
      <p style="font-size:18px;line-height:1.6;color:#C7CCE6;max-width:540px;">Sharp Brains Schools nurtures confident, curious learners from Nursery through Senior Secondary, with a strong record of WAEC &amp; NECO results and a safe, structured environment parents trust.</p>
      <div style="display:flex;gap:16px;flex-wrap:wrap;padding-top:8px;">
        <a href="admissions.html" class="btn btn-amber">Apply for Admission</a>
        <a href="academics.html" class="btn btn-outline-light">Explore Our Programs</a>
      </div>
      <div class="stat-row">
        <div class="stat"><span class="num">[18]+</span><span class="label">Years of Excellence</span></div>
        <div class="stat"><span class="num">[1,200]+</span><span class="label">Students Enrolled</span></div>
        <div class="stat"><span class="num">[92]%</span><span class="label">WAEC Pass Rate</span></div>
      </div>
    </div>
    <div class="hero-art">
      <img src="assets/gallery/trip-03-badagry-gate.jpg" alt="Sharp Brains students on an educational excursion" style="width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:24px;border:1px solid rgba(255,255,255,0.15);">
    </div>
  </div>
</section>

<section style="background:#fff;border-bottom:1px solid var(--border);">
  <div class="container" style="padding:32px;display:flex;flex-wrap:wrap;gap:32px;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:10px;flex:1 1 200px;"><span style="font-size:20px;">&#127963;&#65039;</span><span style="font-weight:600;font-size:14px;color:#353D5C;">[State] Ministry of Education Approved</span></div>
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
      <div class="card">
        <div class="card-icon" style="background:#FDF1DC;">&#129698;</div>
        <h3 style="font-size:20px;">Nursery</h3>
        <p style="font-size:13px;font-weight:700;color:var(--amber-dark);">Ages [2] &ndash; [5]</p>
        <p class="muted" style="font-size:14px;">Play-based early learning that builds language, motor skills, and social confidence.</p>
        <a href="academics.html" style="font-weight:700;font-size:14px;color:var(--indigo);">Learn more &rarr;</a>
      </div>
      <div class="card">
        <div class="card-icon" style="background:#E7EAFB;">&#128218;</div>
        <h3 style="font-size:20px;">Primary</h3>
        <p style="font-size:13px;font-weight:700;color:var(--amber-dark);">Primary 1 &ndash; 6</p>
        <p class="muted" style="font-size:14px;">A strong foundation in literacy, numeracy, and science, plus character-building activities.</p>
        <a href="academics.html" style="font-weight:700;font-size:14px;color:var(--indigo);">Learn more &rarr;</a>
      </div>
      <div class="card">
        <div class="card-icon" style="background:#DEE9FF;">&#127891;</div>
        <h3 style="font-size:20px;">Secondary</h3>
        <p style="font-size:13px;font-weight:700;color:var(--amber-dark);">JSS1 &ndash; JSS3 &middot; SSS1 &ndash; SSS3</p>
        <p class="muted" style="font-size:14px;">Rigorous WAEC/NECO-aligned teaching across Science, Arts, and Commercial streams.</p>
        <a href="academics.html" style="font-weight:700;font-size:14px;color:var(--indigo);">Learn more &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark" style="color:var(--amber);">(02) RESULTS &amp; ACHIEVEMENTS</span>
      <h2>A Record Parents Can Trust</h2>
    </div>
    <div class="grid grid-4">
      <div class="stat"><span class="num">[18]+</span><span class="label">Years of Operation</span></div>
      <div class="stat"><span class="num">[92]%</span><span class="label">WAEC Pass Rate</span></div>
      <div class="stat"><span class="num">[1,200]+</span><span class="label">Students Enrolled</span></div>
      <div class="stat"><span class="num">[300]+</span><span class="label">University Placements</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow-dark">(03) KIND WORDS</span>
      <h2>What Parents Say</h2>
    </div>
    <div class="grid grid-3">
      <div class="card sm">
        <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        <p style="font-size:14px;color:#353D5C;line-height:1.6;">"[Parent testimonial placeholder &mdash; how the school helped their child grow academically and socially.]"</p>
        <p style="font-weight:700;font-size:13px;color:var(--navy);">&mdash; [Parent Name], Parent of [Grade] Student</p>
      </div>
      <div class="card sm">
        <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        <p style="font-size:14px;color:#353D5C;line-height:1.6;">"[Parent testimonial placeholder &mdash; mention of teacher quality or communication.]"</p>
        <p style="font-weight:700;font-size:13px;color:var(--navy);">&mdash; [Parent Name], Parent of [Grade] Student</p>
      </div>
      <div class="card sm">
        <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        <p style="font-size:14px;color:#353D5C;line-height:1.6;">"[Parent testimonial placeholder &mdash; mention of WAEC results or admissions outcome.]"</p>
        <p style="font-weight:700;font-size:13px;color:var(--navy);">&mdash; [Parent Name], Parent of [Grade] Student</p>
      </div>
    </div>
  </div>
</section>

<section style="background:#000;">
  <div class="container" style="padding-top:64px;padding-bottom:24px;">
    <span class="eyebrow-dark" style="color:var(--amber);">(04) GALLERY PREVIEW</span>
    <h2 style="color:#fff;font-size:32px;font-weight:800;padding-top:12px;">Life at Sharp Brains, in Motion</h2>
    <p style="color:#9BA3C9;max-width:560px;padding-top:10px;font-size:15px;">A running look at campus life. Panels below are placeholders &mdash; swap in real photos any time.</p>
  </div>
  <div class="endless-root" aria-label="Scrolling photo gallery of Sharp Brains Schools">
    <div class="endless-scene">
      <div class="endless-world"></div>
    </div>
    <div class="endless-footer">
      <p class="endless-caption">See the full gallery &rarr;</p>
    </div>
  </div>
  <div style="text-align:center;padding:32px;">
    <a href="gallery.html" class="btn btn-amber">View Full Gallery</a>
  </div>
</section>
"""

HOME_EXTRA_SCRIPTS = """
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="assets/endless-gallery.js"></script>
"""

write_page("index.html", "Home", "Sharp Brains Schools — Nursery, Primary & Secondary education in Nigeria.", "", home_body, extra_scripts=HOME_EXTRA_SCRIPTS)

# ------------------------------------------------------------- ABOUT ----

about_body = """
<section class="page-banner">
  <div class="container">
    <span class="eyebrow">ABOUT US</span>
    <h1 style="color:#fff;font-size:40px;font-weight:800;padding-top:12px;">Our Story</h1>
    <p style="color:#C7CCE6;max-width:560px;padding-top:12px;font-size:16px;">[Placeholder: a paragraph on when and why the school was founded, its founders, and its journey to today.]</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2">
    <div>
      <span class="eyebrow-dark">OUR MISSION</span>
      <h2 style="font-size:28px;padding-top:12px;">[Placeholder mission statement &mdash; what the school exists to do for its students.]</h2>
    </div>
    <div>
      <span class="eyebrow-dark">OUR VISION</span>
      <h2 style="font-size:28px;padding-top:12px;">[Placeholder vision statement &mdash; what the school aims to become.]</h2>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container grid grid-4">
    <div class="stat"><span class="num">[18]+</span><span class="label">Years of Operation</span></div>
    <div class="stat"><span class="num">[1,200]+</span><span class="label">Students Enrolled</span></div>
    <div class="stat"><span class="num">[92]%</span><span class="label">WAEC Pass Rate</span></div>
    <div class="stat"><span class="num">[40]+</span><span class="label">Teaching Staff</span></div>
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
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div>
        <p style="font-weight:700;font-size:15px;">[Principal's Name]</p>
        <p style="font-size:13px;color:var(--muted-2);">Principal</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div>
        <p style="font-weight:700;font-size:15px;">[Teacher Name]</p>
        <p style="font-size:13px;color:var(--muted-2);">Head of Secondary</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div>
        <p style="font-weight:700;font-size:15px;">[Teacher Name]</p>
        <p style="font-size:13px;color:var(--muted-2);">Head of Primary</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div>
        <p style="font-weight:700;font-size:15px;">[Teacher Name]</p>
        <p style="font-size:13px;color:var(--muted-2);">Head of Nursery</p>
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
      <div class="card sm">&#127963;&#65039; <strong>[State] Ministry of Education</strong> &mdash; Approved and licensed.</div>
      <div class="card sm">&#128221; <strong>WAEC &amp; NECO</strong> &mdash; Registered examination centre.</div>
      <div class="card sm">&#127942; <strong>[Award/Body Name]</strong> &mdash; [Placeholder recognition or membership.]</div>
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
      <p class="muted">Figures below are placeholders &mdash; replace with actual fee amounts before publishing.</p>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <h3 style="font-size:18px;">Nursery</h3>
        <p style="font-family:'Poppins';font-weight:800;font-size:26px;color:var(--navy);padding-top:8px;">[&#8358;XX,XXX]</p>
        <p class="muted" style="font-size:13px;">per term</p>
      </div>
      <div class="card">
        <h3 style="font-size:18px;">Primary</h3>
        <p style="font-family:'Poppins';font-weight:800;font-size:26px;color:var(--navy);padding-top:8px;">[&#8358;XX,XXX]</p>
        <p class="muted" style="font-size:13px;">per term</p>
      </div>
      <div class="card">
        <h3 style="font-size:18px;">Secondary</h3>
        <p style="font-family:'Poppins';font-weight:800;font-size:26px;color:var(--navy);padding-top:8px;">[&#8358;XX,XXX]</p>
        <p class="muted" style="font-size:13px;">per term</p>
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
    <div class="faq-wrap">
      <div class="faq-item">
        <button class="faq-q"><span>Do you offer both day and boarding options?</span><span class="faq-symbol">+</span></button>
        <p class="faq-a">[Placeholder answer &mdash; describe day/boarding options, hostel facilities, and pickup arrangements.]</p>
      </div>
      <div class="faq-item">
        <button class="faq-q"><span>What exam boards do you prepare students for?</span><span class="faq-symbol">+</span></button>
        <p class="faq-a">[Placeholder answer &mdash; e.g. WAEC, NECO, and JAMB, with mock exam schedule details.]</p>
      </div>
      <div class="faq-item">
        <button class="faq-q"><span>Is there an entrance exam for new students?</span><span class="faq-symbol">+</span></button>
        <p class="faq-a">[Placeholder answer &mdash; describe the assessment subjects and format for each level.]</p>
      </div>
      <div class="faq-item">
        <button class="faq-q"><span>What is the school's fee payment structure?</span><span class="faq-symbol">+</span></button>
        <p class="faq-a">[Placeholder answer &mdash; termly or annual payment, installment options, and accepted payment methods.]</p>
      </div>
      <div class="faq-item">
        <button class="faq-q"><span>Do you provide transportation (school bus) services?</span><span class="faq-symbol">+</span></button>
        <p class="faq-a">[Placeholder answer &mdash; list routes and whether it is included in fees or optional.]</p>
      </div>
    </div>
  </div>
</section>
"""

write_page("admissions.html", "Admissions", "How to enroll at Sharp Brains Schools: process, fees, and FAQs.", "admissions.html", admissions_body)

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
]

CELEBRATION_PHOTOS = [
    "assets/gallery/event-democracy-day-1.jpg",
    "assets/gallery/event-democracy-day-2.jpg",
    "assets/gallery/event-democracy-day-3.jpg",
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
    <h2 style="font-size:22px;padding-bottom:24px;">Educational Excursions</h2>
    <div class="grid grid-4">
      {photo_grid(EXCURSION_PHOTOS, "Sharp Brains students on an educational excursion")}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Celebrations</h2>
    <div class="grid grid-3">
      {photo_grid(CELEBRATION_PHOTOS, "Sharp Brains students celebrating Democracy Day")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Campus &amp; Classrooms</h2>
    <p class="muted" style="padding-bottom:24px;">More photos coming soon.</p>
    <div class="grid grid-4">
      {gallery_grid(4, colors)}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Sports &amp; Activities</h2>
    <p class="muted" style="padding-bottom:24px;">More photos coming soon.</p>
    <div class="grid grid-4">
      {gallery_grid(4, colors)}
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
        <p class="muted" style="font-size:14px;padding-top:6px;">[School Address], [City], [State], Nigeria</p>
      </div>
      <div class="card sm">
        <h3 style="font-size:16px;">&#128222; Phone / WhatsApp</h3>
        <p class="muted" style="font-size:14px;padding-top:6px;">[+234 XXX XXX XXXX]</p>
      </div>
      <div class="card sm">
        <h3 style="font-size:16px;">&#9993;&#65039; Email</h3>
        <p class="muted" style="font-size:14px;padding-top:6px;">[info@sharpbrains.sch.ng]</p>
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
        <p class="muted" style="font-size:14px;">Students marked Democracy Day with a celebration of freedom, unity, and the power of every voice &mdash; one nation, one future.</p>
      </div>
    </div>
    <div class="card">
      <span class="tag">[Date]</span>
      <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
      <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
    </div>
    <div class="card">
      <span class="tag">[Date]</span>
      <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
      <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
    </div>
    <div class="card">
      <span class="tag">[Date]</span>
      <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
      <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
    </div>
    <div class="card">
      <span class="tag">[Date]</span>
      <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
      <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
    </div>
    <div class="card">
      <span class="tag">[Date]</span>
      <h3 style="font-size:17px;padding-top:10px;">[News headline placeholder]</h3>
      <p class="muted" style="font-size:14px;">[A short excerpt describing the news item or event, two to three sentences.]</p>
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
      <div style="display:flex;flex-direction:column;gap:12px;"><div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div><p style="font-weight:700;font-size:15px;">[Principal's Name]</p><p class="muted" style="font-size:13px;">Principal</p></div>
      <div style="display:flex;flex-direction:column;gap:12px;"><div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div><p style="font-weight:700;font-size:15px;">[Vice Principal's Name]</p><p class="muted" style="font-size:13px;">Vice Principal</p></div>
      <div style="display:flex;flex-direction:column;gap:12px;"><div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div><p style="font-weight:700;font-size:15px;">[Name]</p><p class="muted" style="font-size:13px;">Head of Secondary</p></div>
      <div style="display:flex;flex-direction:column;gap:12px;"><div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div><p style="font-weight:700;font-size:15px;">[Name]</p><p class="muted" style="font-size:13px;">Head of Primary</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 style="font-size:22px;padding-bottom:24px;">Teaching Staff</h2>
    <div class="grid grid-4">
      <div style="display:flex;flex-direction:column;gap:12px;"><div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div><p style="font-weight:700;font-size:15px;">[Teacher Name]</p><p class="muted" style="font-size:13px;">[Subject]</p></div>
      <div style="display:flex;flex-direction:column;gap:12px;"><div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div><p style="font-weight:700;font-size:15px;">[Teacher Name]</p><p class="muted" style="font-size:13px;">[Subject]</p></div>
      <div style="display:flex;flex-direction:column;gap:12px;"><div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div><p style="font-weight:700;font-size:15px;">[Teacher Name]</p><p class="muted" style="font-size:13px;">[Subject]</p></div>
      <div style="display:flex;flex-direction:column;gap:12px;"><div class="placeholder-block light" style="aspect-ratio:1/1;">[Photo]</div><p style="font-weight:700;font-size:15px;">[Teacher Name]</p><p class="muted" style="font-size:13px;">[Subject]</p></div>
    </div>
  </div>
</section>
"""

write_page("staff.html", "Our Staff", "Meet the leadership and teaching staff at Sharp Brains Schools.", "staff.html", staff_body)

print("Done.")
