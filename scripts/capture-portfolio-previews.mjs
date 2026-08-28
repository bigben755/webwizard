import { chromium } from 'playwright';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const sites = [
  { slug: 'bodge-job', url: 'https://bodge-job.com/', domain: 'bodge-job.com' },
  { slug: 'train-driver-academy', url: 'https://traindriveracademy.com/', domain: 'traindriveracademy.com' },
  { slug: 'train-driver-foundation', url: 'https://traindriverfoundation.com/', domain: 'traindriverfoundation.com' },
  { slug: 'train-driver-psychometrics', url: 'https://traindriverpsychometrics.co.uk/', domain: 'traindriverpsychometrics.co.uk' },
  { slug: 'railway-careers', url: 'https://railwaycareers.co.uk/', domain: 'railwaycareers.co.uk' },
  { slug: 'grade-9-ready', url: 'https://grade9ready.com/', domain: 'grade9ready.com' },
  { slug: '1471-horwich-squadron', url: 'https://1471squadron.co.uk/', domain: '1471squadron.co.uk' },
  { slug: 'blackrod-now', url: 'https://blackrodnow.com/', domain: 'blackrodnow.com' },
];

const outDir = path.join('assets', 'portfolio-fast');
await mkdir(outDir, { recursive: true });

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1200, height: 675 },
  deviceScaleFactor: 1,
  userAgent: 'Mozilla/5.0 WebWizardPortfolioPreview/1.0',
});

for (const site of sites) {
  const page = await context.newPage();
  try {
    await page.goto(site.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(2500);
    await page.screenshot({
      path: path.join(outDir, `${site.slug}.jpg`),
      type: 'jpeg',
      quality: 74,
      fullPage: false,
    });
  } catch (err) {
    console.error(`Screenshot failed for ${site.url}:`, err.message);
  } finally {
    await page.close();
  }

  try {
    const logoUrl = `https://www.google.com/s2/favicons?domain=${encodeURIComponent(site.domain)}&sz=128`;
    const res = await fetch(logoUrl);
    if (res.ok) {
      await writeFile(path.join(outDir, `${site.slug}-logo.png`), Buffer.from(await res.arrayBuffer()));
    }
  } catch (err) {
    console.error(`Logo download failed for ${site.domain}:`, err.message);
  }
}

await browser.close();

let html = await readFile('index.html', 'utf8');

// Remove TRAC entirely and update the portfolio count.
html = html.replace(/\s*<article class="project-card project-card-static reveal">[\s\S]*?<\/article>\s*/m, '\n');
html = html.replace('<div class="proof-item"><strong>9</strong><span>projects showcased</span></div>', '<div class="proof-item"><strong>8</strong><span>projects showcased</span></div>');

// Remove the extra decorative/hidden hero logo from the top-right of the landing page.
html = html.replace(/^\s*<img\b[^>]*class="[^"]*hero-emblem[^"]*"[^>]*>\s*$/gm, '');
html = html.replace(/^\s*<[^>]+class="[^"]*hero-emblem[^"]*"[^>]*>[\s\S]*?<\/[^>]+>\s*$/gm, '');

for (const site of sites) {
  const oldPreview = new RegExp(`https:\\/\\/image\\.thum\\.io\\/get\\/width\\/1400\\/crop\\/788\\/noanimate\\/${site.url.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`,'g');
  html = html.replace(oldPreview, `assets/portfolio-fast/${site.slug}.jpg`);

  const googleLogo = new RegExp(`https:\\/\\/www\\.google\\.com\\/s2\\/favicons\\?domain=${site.domain.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}&amp;sz=128`, 'g');
  html = html.replace(googleLogo, `assets/portfolio-fast/${site.slug}-logo.png`);
}

html = html.replace('https://1471squadron.co.uk/favicon.ico', 'assets/portfolio-fast/1471-horwich-squadron-logo.png');
html = html.replace(/ referrerpolicy="no-referrer"/g, '');
html = html.replace(/class="project-preview-image" src="assets\/portfolio-fast\/([^"]+)" alt="([^"]+)" loading="lazy"/g,
  'class="project-preview-image" src="assets/portfolio-fast/$1" alt="$2" loading="lazy" decoding="async" fetchpriority="low" width="1200" height="675"');
html = html.replace(/<img src="assets\/portfolio-fast\/([^"]+-logo\.png)" alt="" loading="lazy"/g,
  '<img src="assets/portfolio-fast/$1" alt="" loading="lazy" decoding="async" width="128" height="128"');

if (html.includes('image.thum.io')) {
  throw new Error('Remote thum.io preview references remain in index.html');
}
if (html.includes('>TRAC</h3>')) {
  throw new Error('TRAC card still remains in index.html');
}

await writeFile('index.html', html, 'utf8');
console.log('Portfolio previews captured locally and index.html optimised.');
