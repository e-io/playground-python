import requests
from lxml import html

is_test = True
print_log = False


def find_domain(href):
    local = href.find('..')
    if local != -1:
        return None

    begin = href.find('//')
    if begin != -1:
        href = href[begin+2:]

    end = href.find(':')
    if end != -1:
        href = href[:end]

    end = href.find('/')
    if end != -1:
        href = href[:end]

    return href


if is_test:
    # code from href3 is in input.txt also
    href1 = 'http://pastebin.com/raw/2mie4QYa'
    href2 = 'http://pastebin.com/raw/hfMThaGb'
    href3 = 'http://pastebin.com/raw/7543p0ns'
    href = href3
else:
    href = input().strip()

doc = requests.get(href).text
html_ = html.document_fromstring(doc)
domains = set()
for a in html_.iter('a'):
    href = a.get('href')
    if href:
        result = find_domain(href)
        if result:
            domains.add(result)
            if print_log:
                print(f'{result} from {href}')

domains = list(domains)
domains.sort()
for domain in domains:
    print(domain)
