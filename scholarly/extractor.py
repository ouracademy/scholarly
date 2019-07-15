import re


def get_title(html):
    title = html.find('h3', class_='gs_rt')
    if title.find('span', class_='gs_ctu'):  # A citation
        title.span.extract()
    elif title.find('span', class_='gs_ctc'):  # A book or PDF
        title.span.extract()
    return title.text.strip()


def get_year(html):
    subtitle = html.find('div', class_='gs_a')
    text = subtitle.text if subtitle.text else ''
    match = re.search('[0-9]{4}',text)
    return match[0] if match else ''


def get_url(html):
    return html.find('a')['href'] if html.find('a') else ''


def get_author(html):
    authorinfo = html.find('div', class_='gs_a')
    return ' and '.join([i.strip() for i in authorinfo.text.split(' - ')[0].split(',')])


def get_abstract(html):
    abstract = ''
    if html.find('div', class_='gs_rs'):
        abstract = html.find('div', class_='gs_rs').text
        if abstract[0:8].lower() == 'abstract':
            abstract = abstract[9:].strip()
    return abstract

fields_by_publication = [
    ['year', get_year],
    ['title', get_title],
    ['url', get_url],
    ['author', get_author],
    ['abstract', get_abstract]
]
