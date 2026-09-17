#!/usr/bin/env python3
"""TZ (.docx) hujjatini bo'limlar bo'yicha papkalarga ajratadi.

Har bir bo'lim/band uchun alohida papka va uning ichida about.md yaratiladi.
Hujjat matni o'zgartirilmaydi — faqat markdown ramkasi (jadval, ro'yxat) qo'shiladi.

Foydalanish:
    python3 split_tz.py TZ_07_07_2026.docx tz
"""
import os
import re
import shutil
import sys
import zipfile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
PKG_REL = '{http://schemas.openxmlformats.org/package/2006/relationships}'

# "1. ...", "1.1. ...", "4.1.1.1. ...", "B.1. ..." sarlavhalarini ajratadi
NUM_RE = re.compile(r'^\s*((?:\d+|[A-Z])(?:\.\d+)*)\.\s+(.+)$', re.S)


def parse_num(text):
    m = NUM_RE.match(text.strip())
    if not m:
        return None, text.strip()
    return m.group(1), m.group(2).strip()


def safe_name(name):
    name = name.replace('/', '-').replace('\\', '-').replace('\n', ' ')
    name = re.sub(r'\s+', ' ', name).strip().rstrip('.')
    return name[:150]


# ---------------------------------------------------------------- docx o'qish

def load_rels(z):
    rels = {}
    root = ET.fromstring(z.read('word/_rels/document.xml.rels'))
    for rel in root.findall(PKG_REL + 'Relationship'):
        rels[rel.get('Id')] = rel.get('Target')
    return rels


def para_parts(p, rels):
    """Abzatsni (matn, rasm) bo'laklariga ajratadi."""
    parts = []
    buf = []

    def flush():
        if buf:
            txt = ''.join(buf)
            if txt.strip():
                parts.append(('text', txt))
            buf.clear()

    for node in p.iter():
        tag = node.tag
        if tag == W + 't':
            buf.append(node.text or '')
        elif tag == W + 'tab':
            buf.append('\t')
        elif tag == W + 'br':
            buf.append('\n')
        elif tag == A + 'blip':
            rid = node.get(R + 'embed')
            target = rels.get(rid)
            if target:
                flush()
                parts.append(('image', 'word/' + target.lstrip('./')))
    flush()
    return parts


def read_items(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        rels = load_rels(z)
        body = ET.fromstring(z.read('word/document.xml')).find(W + 'body')
        media = {n: z.read(n) for n in z.namelist() if n.startswith('word/media/')}

    items = []
    for ch in body:
        if ch.tag == W + 'p':
            pPr = ch.find(W + 'pPr')
            style = None
            if pPr is not None:
                st = pPr.find(W + 'pStyle')
                style = st.get(W + 'val') if st is not None else None
            items.append({'k': 'p', 'style': style, 'parts': para_parts(ch, rels)})
        elif ch.tag == W + 'tbl':
            rows = []
            for tr in ch.findall(W + 'tr'):
                cells = []
                for tc in tr.findall(W + 'tc'):
                    cps = [''.join(t for kind, t in para_parts(p, rels) if kind == 'text')
                           for p in tc.findall(W + 'p')]
                    cells.append('\n'.join(x for x in cps if x.strip()).strip())
                rows.append(cells)
            if rows:
                items.append({'k': 'tbl', 'rows': rows})
    return items, media


def item_text(item):
    return ''.join(t for kind, t in item['parts'] if kind == 'text')


# ------------------------------------------------------------ tuzilma qurish

def node_level(item):
    """Abzats sarlavha bo'lsa uning darajasini qaytaradi, aks holda None."""
    if item['k'] != 'p':
        return None
    style = item.get('style')
    text = item_text(item).strip()
    if not text:
        return None
    if style in ('Heading1', 'Heading2', 'Heading3'):
        return int(style[-1])
    if style in (None, 'Normal'):
        # "4.1.1.1." kabi raqamlangan bandlar Word'da oddiy abzats
        num, _ = parse_num(text)
        if num and num.count('.') >= 2 and all(p.isdigit() for p in num.split('.')):
            return num.count('.') + 1
    return None


def build_tree(items):
    root = {'num': None, 'title': None, 'heading': None, 'content': [], 'children': [], 'level': 0}
    stack = [root]
    mode = 'title'  # title -> toc -> body

    for item in items:
        if item['k'] == 'p' and item.get('style') in ('TOC1', 'TOC2', 'TOC3'):
            continue

        level = node_level(item)
        text = item_text(item).strip() if item['k'] == 'p' else ''

        if level == 1 and text == 'Mundarija':
            mode = 'toc'
            continue
        if mode == 'toc' and level != 1:
            continue

        if level:
            mode = 'body'
            num, title = parse_num(text)
            node = {'num': num, 'title': title, 'heading': text,
                    'content': [], 'children': [], 'level': level}
            while stack[-1]['level'] >= level:
                stack.pop()
            stack[-1]['children'].append(node)
            stack.append(node)
        elif mode != 'toc':
            stack[-1]['content'].append(item)

    return root


def dir_name(node):
    num, title = node['num'], node['title']
    if node['level'] == 1:
        return safe_name(f'{num}.{title}' if num else title)
    return safe_name(f"{num.replace('.', '-')} {title}" if num else title)


# ------------------------------------------------------------- markdown yozish

def render_table(rows):
    width = max(len(r) for r in rows)
    def cell(c):
        return c.replace('|', '\\|').replace('\n', '<br>').strip()
    def row(cells):
        padded = list(cells) + [''] * (width - len(cells))
        return '| ' + ' | '.join(cell(c) for c in padded) + ' |'
    out = [row(rows[0]), '| ' + ' | '.join(['---'] * width) + ' |']
    out += [row(r) for r in rows[1:]]
    return '\n'.join(out)


def render(node, out_dir, media):
    lines = []
    if node['heading']:
        lines.append(node['heading'])
        lines.append('')

    img_prefix = (node['num'] or 'rasm').replace('.', '-')
    img_n = 0
    bullets = []

    def flush_bullets():
        if bullets:
            lines.extend(bullets)
            lines.append('')
            bullets.clear()

    for item in node['content']:
        if item['k'] == 'tbl':
            flush_bullets()
            lines.append(render_table(item['rows']))
            lines.append('')
            continue

        is_bullet = item.get('style') == 'ListParagraph'
        for kind, value in item['parts']:
            if kind == 'image':
                flush_bullets()
                img_n += 1
                suffix = '' if img_n == 1 else f'-{img_n}'
                fname = f'{img_prefix}-rasm{suffix}' + os.path.splitext(value)[1]
                with open(os.path.join(out_dir, fname), 'wb') as f:
                    f.write(media[value])
                lines.append(f'![{img_prefix}-rasm{suffix}]({fname})')
                lines.append('')
            else:
                text = value.strip()
                if not text:
                    continue
                if is_bullet:
                    bullets.append('- ' + text.replace('\n', ' '))
                else:
                    flush_bullets()
                    lines.append(text)
                    lines.append('')
    flush_bullets()

    while lines and lines[-1] == '':
        lines.pop()
    return '\n'.join(lines) + '\n' if lines else ''


def write_tree(node, out_dir, media, stats):
    os.makedirs(out_dir, exist_ok=True)
    body = render(node, out_dir, media)
    if body:
        with open(os.path.join(out_dir, 'about.md'), 'w', encoding='utf-8') as f:
            f.write(body)
        stats['files'] += 1
    for child in node['children']:
        child_dir = os.path.join(out_dir, dir_name(child))
        stats['dirs'] += 1
        write_tree(child, child_dir, media, stats)


def main():
    docx_path = sys.argv[1] if len(sys.argv) > 1 else 'TZ_07_07_2026.docx'
    out_root = sys.argv[2] if len(sys.argv) > 2 else 'tz'

    items, media = read_items(docx_path)
    tree = build_tree(items)

    if os.path.isdir(out_root):
        shutil.rmtree(out_root)

    stats = {'files': 0, 'dirs': 0}
    write_tree(tree, out_root, media, stats)
    print(f'{out_root}/ tayyor: {stats["dirs"]} papka, {stats["files"]} ta about.md')


if __name__ == '__main__':
    main()
