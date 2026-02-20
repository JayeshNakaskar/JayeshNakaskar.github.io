from pathlib import Path
p=Path('index.html').read_text(encoding='utf-8')
start=p.find('<form')
end=p.find('</form>', start)
if start==-1 or end==-1:
    print('FORM_NOT_FOUND')
else:
    fragment=p[start:end+7]
    print('FORM_FOUND LENGTH', len(fragment))
    print('HAS_INPUTS', ('<input' in fragment) or ('<textarea' in fragment))
    # print fragment for manual inspection
    print('\n---FRAGMENT---\n')
    print(fragment)
