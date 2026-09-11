from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = [
    ('<div class="price"><strong>£129</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£10.75/month</strong><small>12 monthly payments · total £129</small></div>',
     '<div class="price"><strong>£132</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£11/month</strong><small>12 monthly payments · total £132</small></div>'),
    ('<div class="price"><strong>£179</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£14.92/month*</strong><small>12 monthly payments · total £179</small></div>',
     '<div class="price"><strong>£180</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£15/month</strong><small>12 monthly payments · total £180</small></div>'),
    ('<div class="price"><strong>£299</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£24.92/month*</strong><small>12 monthly payments · total £299</small></div>',
     '<div class="price"><strong>£300</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£25/month</strong><small>12 monthly payments · total £300</small></div>'),
    ('<p class="pricing-note">Choose to pay the website price once or split exactly the same total across 12 monthly payments. *Where a monthly figure rounds to the nearest penny, the final payment is adjusted by a few pence so you never pay more than the stated one-off total. Existing domain connection is included where technically possible. If you need a new custom domain, registration is charged separately at the registrar cost. A Web Wizard address such as <strong>yourbusiness.thewebdesignwizard.co.uk</strong> can be used instead. Bespoke integrations, online shops and unusually complex functionality are quoted separately before work begins.</p>',
     '<p class="pricing-note">Choose to pay the website price once or split exactly the same total across 12 monthly payments. Existing domain connection is included where technically possible. If you need a new custom domain, registration is charged separately at the registrar cost. A Web Wizard address such as <strong>yourbusiness.thewebdesignwizard.co.uk</strong> can be used instead. Bespoke integrations, online shops and unusually complex functionality are quoted separately before work begins.</p>'),
    ('<h2 class="section-title">A proper business website — without being locked out of it.</h2>',
     '<h2 class="section-title">A proper website, without being locked out of it.</h2>'),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'Expected exactly one occurrence, found {count}: {old[:100]!r}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('Simple pricing and copy update applied successfully.')