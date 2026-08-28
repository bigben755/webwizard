from pathlib import Path
import re

path = Path("index.html")
html = path.read_text(encoding="utf-8")

MARKER = "/* Portfolio homepage preview cards v2 */"
if MARKER in html:
    print("Portfolio homepage preview update already applied.")
    raise SystemExit(0)

# Remove the previous one-image-per-project portfolio override.
html = re.sub(
    r'\n\s*/\* Portfolio screenshot cards \*/.*?(?=\n\s*</style>)',
    '',
    html,
    count=1,
    flags=re.S,
)

portfolio_css = r'''

    /* Portfolio homepage preview cards v2 */
    .project-art.project-homepage-preview {
      position: relative;
      min-height: 0;
      aspect-ratio: 16 / 9;
      padding: 0;
      overflow: hidden;
      background: #eceef5;
      border-bottom: 1px solid var(--line);
    }
    .project-art.project-homepage-preview::before,
    .project-art.project-homepage-preview::after { display: none; }
    .project-card:hover .project-art.project-homepage-preview { filter: none; }
    .project-preview-fallback {
      position: absolute;
      inset: 0;
      display: grid;
      place-content: center;
      gap: 5px;
      padding: 78px 24px 28px;
      text-align: center;
      color: var(--night);
      background:
        radial-gradient(circle at 80% 10%, rgba(109,74,255,.15), transparent 32%),
        linear-gradient(145deg, #f7f7fc, #e6e7f2);
    }
    .project-preview-fallback span {
      font-size: clamp(1.4rem, 3vw, 2rem);
      font-weight: 900;
      letter-spacing: -.04em;
    }
    .project-preview-fallback small { color: var(--muted); font-weight: 750; }
    .project-art.project-homepage-preview > .project-preview-image {
      position: absolute;
      inset: 0;
      z-index: 1;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      background: #fff;
      transition: transform .4s ease, filter .28s ease;
    }
    .project-card:hover .project-art.project-homepage-preview > .project-preview-image {
      transform: scale(1.018);
      filter: brightness(1.02);
    }
    .project-art.project-homepage-preview .project-domain {
      position: absolute;
      z-index: 3;
      top: 16px;
      left: 16px;
      color: #fff;
      background: rgba(17,16,42,.8);
      border-color: rgba(255,255,255,.25);
      box-shadow: 0 5px 16px rgba(0,0,0,.15);
    }
    .project-logo-badge {
      position: absolute;
      z-index: 3;
      top: 14px;
      right: 14px;
      width: 68px;
      height: 68px;
      display: grid;
      place-items: center;
      overflow: hidden;
      border: 1px solid rgba(17,16,42,.1);
      border-radius: 18px;
      background: rgba(255,255,255,.96);
      box-shadow: 0 10px 28px rgba(17,16,42,.18);
    }
    .project-logo-fallback {
      position: absolute;
      color: var(--night);
      font-size: .72rem;
      font-weight: 950;
      letter-spacing: -.02em;
    }
    .project-logo-badge img {
      position: relative;
      z-index: 1;
      width: 48px;
      height: 48px;
      object-fit: contain;
    }
    .project-info { align-items: center; }
    .project-meta { min-width: 0; }
    .project-meta h3 {
      margin: 0 0 7px;
      color: var(--night);
      font-size: 1.15rem;
      line-height: 1.15;
      letter-spacing: -.025em;
    }
    .project-meta p { margin: 0; }
    .project-card-static { cursor: default; }
    .project-card-static:hover { transform: translateY(-6px); }

    @media (max-width: 520px) {
      .project-logo-badge { width: 58px; height: 58px; border-radius: 15px; }
      .project-logo-badge img { width: 40px; height: 40px; }
      .project-art.project-homepage-preview .project-domain { top: 12px; left: 12px; }
    }
'''

html = html.replace('  </style>', portfolio_css + '\n  </style>', 1)

open_icon = '<span class="project-open" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M8 7h9v9"/></svg></span>'

def shot(url):
    return f"https://image.thum.io/get/width/1400/crop/788/noanimate/{url}"

def favicon(domain):
    return f"https://www.google.com/s2/favicons?domain={domain}&amp;sz=128"

cards = [
    dict(tag='a', attrs='href="https://bodge-job.com/" target="_blank" rel="noopener noreferrer"',
         title='Bodge Job', domain='bodge-job.com', preview=shot('https://bodge-job.com/'), logo=favicon('bodge-job.com'), initials='BJ',
         desc='Mobile-first website design with clear service discovery and straightforward enquiry journeys.', icon=True),
    dict(tag='article', attrs='', title='TRAC', domain='TRAC', preview='assets/portfolio/trac.png', logo=None, initials='TRAC',
         desc='Professional service-led interface built around trust, clarity and confident calls to action.', icon=False),
    dict(tag='a', attrs='href="https://traindriveracademy.com/" target="_blank" rel="noopener noreferrer"',
         title='UK Train Driver Academy', domain='traindriveracademy.com', preview=shot('https://traindriveracademy.com/'), logo=favicon('traindriveracademy.com'), initials='UKTDA',
         desc='Content-led responsive design that makes specialist guidance easy to navigate.', icon=True),
    dict(tag='a', attrs='href="https://traindriverfoundation.com/" target="_blank" rel="noopener noreferrer"',
         title='Train Driver Foundation', domain='traindriverfoundation.com', preview=shot('https://traindriverfoundation.com/'), logo=favicon('traindriverfoundation.com'), initials='TDF',
         desc='Structured learning experience with clear pathways through courses, guidance and resources.', icon=True),
    dict(tag='a', attrs='href="https://traindriverpsychometrics.co.uk/" target="_blank" rel="noopener noreferrer"',
         title='Train Driver Psychometrics', domain='traindriverpsychometrics.co.uk', preview=shot('https://traindriverpsychometrics.co.uk/'), logo=favicon('traindriverpsychometrics.co.uk'), initials='TDP',
         desc='Focused assessment interface designed for clarity, confidence and distraction-free practice.', icon=True),
    dict(tag='a', attrs='href="https://railwaycareers.co.uk/" target="_blank" rel="noopener noreferrer"',
         title='Railway Careers UK', domain='railwaycareers.co.uk', preview=shot('https://railwaycareers.co.uk/'), logo=favicon('railwaycareers.co.uk'), initials='RCUK',
         desc='Search-friendly careers experience with strong information hierarchy and clear next steps.', icon=True),
    dict(tag='a', attrs='href="https://grade9ready.com/" target="_blank" rel="noopener noreferrer"',
         title='Grade 9 Ready', domain='grade9ready.com', preview=shot('https://grade9ready.com/'), logo=favicon('grade9ready.com'), initials='G9',
         desc='Bright, accessible learning interface designed around revision journeys and student confidence.', icon=True),
    dict(tag='a', attrs='href="https://1471squadron.co.uk/" target="_blank" rel="noopener noreferrer"',
         title='1471 Horwich Squadron RAFAC', domain='1471squadron.co.uk', preview=shot('https://1471squadron.co.uk/'), logo='https://1471squadron.co.uk/favicon.ico', initials='1471',
         desc='Youth-focused information site with simple navigation, recruitment messaging and mobile usability.', icon=True),
    dict(tag='a', attrs='href="https://blackrodnow.com/" target="_blank" rel="noopener noreferrer"',
         title='Blackrod Now', domain='blackrodnow.com', preview=shot('https://blackrodnow.com/'), logo=favicon('blackrodnow.com'), initials='BN',
         desc='Community-first information design that makes local updates and useful content easy to find.', icon=True),
]

parts = ['        <div class="portfolio-grid">']
for c in cards:
    static_class = ' project-card-static' if c['tag'] == 'article' else ''
    attrs = (' ' + c['attrs']) if c['attrs'] else ''
    parts.append(f'          <{c["tag"]} class="project-card{static_class} reveal"{attrs}>')
    parts.append('            <div class="project-art project-homepage-preview">')
    parts.append(f'              <div class="project-preview-fallback" aria-hidden="true"><span>{c["initials"]}</span><small>Homepage preview</small></div>')
    parts.append(f'              <img class="project-preview-image" src="{c["preview"]}" alt="{c["title"]} homepage preview" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()">')
    parts.append(f'              <span class="project-domain">{c["domain"]}</span>')
    parts.append('              <span class="project-logo-badge" aria-hidden="true">')
    parts.append(f'                <span class="project-logo-fallback">{c["initials"]}</span>')
    if c['logo']:
        parts.append(f'                <img src="{c["logo"]}" alt="" loading="lazy" onerror="this.remove()">')
    parts.append('              </span>')
    parts.append('            </div>')
    info = f'<div class="project-meta"><h3>{c["title"]}</h3><p>{c["desc"]}</p></div>' + (open_icon if c['icon'] else '')
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
print("Portfolio homepage preview update applied successfully.")
