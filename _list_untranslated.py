import polib
po = polib.pofile('locale/en/LC_MESSAGES/django.po')
with open('_untranslated.txt', 'w', encoding='utf-8') as f:
    for e in po:
        if not e.msgstr.strip():
            f.write(e.msgid + '\n---\n')
print(f"Untranslated: {sum(1 for e in po if not e.msgstr.strip())}")
