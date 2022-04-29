import re
from collections import Counter

import requests
from bs4 import BeautifulSoup as BS


def get_proverbs(text: str):
    keys = text.replace(",", " ").lower().split()
    counter = Counter()

    with open("data.txt", "r", encoding="utf-8") as file:
        proverbs = file.read().split("\n")
        for key in keys:
            forms = get_forms(key)

            for proverb in proverbs:
                words = re.findall(fr'\W*(\w+)\W', proverb.lower())

                if set(words) & set(forms):
                    counter[proverb] += 1

    return [prov for prov, num in counter.most_common()]


def get_forms(word):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389'
                      '.90Safari/537.36 Edg/89.0.774.57'}
    link = 'https://uchim.org/russkij-yazyk/morfologicheskij-razbor-slova/'+word

    full_page = requests.get(link, headers=headers)
    soup = BS(full_page.content, 'html.parser')

    try:
        return soup.find(string="Формы:").parent.next_sibling.replace(',', ' ').split()
    except AttributeError:
        return []