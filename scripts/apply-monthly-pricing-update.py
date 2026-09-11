from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = [
    (
        ".price strong{font-size:2.7rem;line-height:.9;letter-spacing:-.06em}.price span{padding-bottom:4px;color:var(--muted);font-size:.8rem;font-weight:800}\n",
        ".price strong{font-size:2.7rem;line-height:.9;letter-spacing:-.06em}.price span{padding-bottom:4px;color:var(--muted);font-size:.8rem;font-weight:800}\n.monthly-option{display:flex;align-items:baseline;flex-wrap:wrap;gap:6px 8px;margin:-6px 0 21px;padding:11px 13px;border:1px solid rgba(109,74,255,.14);border-radius:12px;background:#faf9ff;color:var(--muted);font-size:.76rem;line-height:1.45}.monthly-option strong{color:var(--purple-dark);font-size:1rem}.monthly-option small{flex-basis:100%;font-size:.68rem;color:var(--muted)}\n"
    ),
    (
        '<div class="price"><strong>£129</strong><span>one-off</span></div>',
        '<div class="price"><strong>£129</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£10.75/month</strong><small>12 monthly payments · total £129</small></div>'
    ),
    (
        '<div class="price"><strong>£179</strong><span>one-off</span></div>',
        '<div class="price"><strong>£179</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£14.92/month*</strong><small>12 monthly payments · total £179</small></div>'
    ),
    (
        '<div class="price"><strong>£299</strong><span>one-off</span></div>',
        '<div class="price"><strong>£299</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£24.92/month*</strong><small>12 monthly payments · total £299</small></div>'
    ),
    (
        '<p class="pricing-note">Existing domain connection is included where technically possible. If you need a new custom domain, registration is charged separately at the registrar cost. A Web Wizard address such as <strong>yourbusiness.thewebdesignwizard.co.uk</strong> can be used instead. Bespoke integrations, online shops and unusually complex functionality are quoted separately before work begins.</p>',
        '<p class="pricing-note">Choose to pay the website price once or split exactly the same total across 12 monthly payments. *Where a monthly figure rounds to the nearest penny, the final payment is adjusted by a few pence so you never pay more than the stated one-off total. Existing domain connection is included where technically possible. If you need a new custom domain, registration is charged separately at the registrar cost. A Web Wizard address such as <strong>yourbusiness.thewebdesignwizard.co.uk</strong> can be used instead. Bespoke integrations, online shops and unusually complex functionality are quoted separately before work begins.</p>'
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'Expected exactly one occurrence, found {count}: {old[:100]!r}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('Monthly pricing update applied successfully.')
