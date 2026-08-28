from pathlib import Path
import re

path = Path("index.html")
html = path.read_text(encoding="utf-8")

if 'assets/portfolio/bodge-job.png' in html:
    print("Portfolio update already applied.")
    raise SystemExit(0)

html = html.replace(
    '<div class="proof-item"><strong>7</strong><span>projects showcased</span></div>',
    '<div class="proof-item"><strong>9</strong><span>projects showcased</span></div>',
)

html = html.replace(
    'A growing portfolio spanning specialist rail services, education, community information and youth organisations.',
    'A growing portfolio of responsive websites and digital products spanning specialist services, education, community information and youth organisations.',
)

portfolio_css = r'''

    /* Portfolio screenshot cards */
    .project-art.project-art-image {
      min-height: 225px;
      padding: 24px;
      background: var(--night);
    }
    .project-art.project-art-image > img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      transition: transform .4s ease, filter .28s ease;
    }
    .project-art.project-art-image::before {
      inset: 0;
      z-index: 1;
      width: auto;
      height: auto;
      border: 0;
      border-radius: 0;
      box-shadow: none;
      background: linear-gradient(180deg, rgba(17,16,42,.05) 18%, rgba(17,16,42,.18) 48%, rgba(17,16,42,.9) 100%);
    }
    .project-art.project-art-image::after { display: none; }
    .project-card:hover .project-art.project-art-image > img {
      transform: scale(1.025);
      filter: brightness(1.04);
    }
    .project-art.project-art-image .project-domain,
    .project-art.project-art-image h3 { z-index: 2; }
    .project-card-static { cursor: default; }
    .project-card-static:hover { transform: translateY(-6px); }
'''

html = html.replace('  </style>', portfolio_css + '\n  </style>', 1)

open_icon = '<span class="project-open" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M8 7h9v9"/></svg></span>'

cards = [
    {
        "tag": "a", "attrs": 'href="https://bodge-job.com/" target="_blank" rel="noopener noreferrer"',
        "img": "assets/portfolio/bodge-job.png", "alt": "Bodge Job website screenshot",
        "domain": "bodge-job.com", "title": "Bodge Job",
        "desc": "Mobile-first website design with clear service discovery and straightforward enquiry journeys.", "icon": True,
    },
    {
        "tag": "article", "attrs": '',
        "img": "assets/portfolio/trac.png", "alt": "TRAC website screenshot",
        "domain": "TRAC", "title": "TRAC",
        "desc": "Professional service-led interface built around trust, clarity and confident calls to action.", "icon": False,
    },
    {
        "tag": "a", "attrs": 'href="https://traindriveracademy.com/" target="_blank" rel="noopener noreferrer"',
        "img": "assets/portfolio/train-driver-academy.png", "alt": "UK Train Driver Academy website screenshot",
        "domain": "traindriveracademy.com", "title": "UK Train Driver Academy",
        "desc": "Content-led responsive design that makes specialist guidance easy to navigate.", "icon": True,
    },
    {
        "tag": "a", "attrs": 'href="https://traindriverfoundation.com/" target="_blank" rel="noopener noreferrer"',
        "img": "assets/portfolio/train-driver-foundation.png", "alt": "Train Driver Foundation website screenshot",
        "domain": "traindriverfoundation.com", "title": "Train Driver Foundation",
        "desc": "Structured learning experience with clear pathways through courses, guidance and resources.", "icon": True,
    },
    {
        "tag": "a", "attrs": 'href="https://traindriverpsychometrics.co.uk/" target="_blank" rel="noopener noreferrer"',
        "img": "assets/portfolio/train-driver-psychometrics.png", "alt": "Train Driver Psychometrics website screenshot",
        "domain": "traindriverpsychometrics.co.uk", "title": "Train Driver Psychometrics",
        "desc": "Focused assessment interface designed for clarity, confidence and distraction-free practice.", "icon": True,
    },
    {
        "tag": "a", "attrs": 'href="https://railwaycareers.co.uk/" target="_blank" rel="noopener noreferrer"',
        "img": "assets/portfolio/railway-careers.png", "alt": "Railway Careers UK website screenshot",
        "domain": "railwaycareers.co.uk", "title": "Railway Careers UK",
        "desc": "Search-friendly careers experience with strong information hierarchy and clear next steps.", "icon": True,
    },
    {
        "tag": "a", "attrs": 'href="https://grade9ready.com/" target="_blank" rel="noopener noreferrer"',
        "img": "assets/portfolio/grade-9-ready.png", "alt": "Grade 9 Ready website screenshot",
        "domain": "grade9ready.com", "title": "Grade 9 Ready",
        "desc": "Bright, accessible learning interface designed around revision journeys and student confidence.", "icon": True,
    },
    {
        "tag": "a", "attrs": 'href="https://1471squadron.co.uk/" target="_blank" rel="noopener noreferrer"',
        "img": "assets/portfolio/1471-horwich-squadron.png", "alt": "1471 Horwich Squadron website screenshot",
        "domain": "1471squadron.co.uk", "title": "1471 Horwich Squadron RAFAC",
        "desc": "Youth-focused information site with simple navigation, recruitment messaging and mobile usability.", "icon": True,
    },
    {
        "tag": "a", "attrs": 'href="https://blackrodnow.com/" target="_blank" rel="noopener noreferrer"',
        "img": None, "alt": None,
        "domain": "blackrodnow.com", "title": "Blackrod Now",
        "desc": "Community-first information design that makes local updates and useful content easy to find.", "icon": True,
    },
]

parts = ['        <div class="portfolio-grid">']
for c in cards:
    static_class = ' project-card-static' if c["tag"] == "article" else ''
    attrs = (' ' + c["attrs"]) if c["attrs"] else ''
    parts.append(f'          <{c["tag"]} class="project-card{static_class} reveal"{attrs}>')
    art_class = 'project-art project-art-image' if c["img"] else 'project-art'
    parts.append(f'            <div class="{art_class}">')
    if c["img"]:
        parts.append(f'              <img src="{c["img"]}" alt="{c["alt"]}" loading="lazy">')
    parts.append(f'              <span class="project-domain">{c["domain"]}</span>')
    parts.append(f'              <h3>{c["title"]}</h3>')
    parts.append('            </div>')
    info = f'<p>{c["desc"]}</p>' + (open_icon if c["icon"] else '')
    parts.append(f'            <div class="project-info">{info}</div>')
    parts.append(f'          </{c["tag"]}>')
    parts.append('')
parts.append('        </div>')
new_grid = '\n'.join(parts)

pattern = re.compile(
    r'        <div class="portfolio-grid">.*?        </div>\n      </div>\n    </section>\n\n    <section id="process">',
    re.S,
)
replacement = new_grid + '\n      </div>\n    </section>\n\n    <section id="process">'
html, count = pattern.subn(replacement, html, count=1)
if count != 1:
    raise RuntimeError(f"Expected to replace one portfolio grid, replaced {count}")

path.write_text(html, encoding="utf-8")
print("Portfolio update applied successfully.")
