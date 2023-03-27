from bs4 import BeautifulSoup
import os
import warnings
import re
from exceptions import TitleTagError, StructureOfStatementError, SpaceError


def title_check(soup):
    title = soup.find_all('h2')
    if len(title) != 1:
        raise TitleTagError()


def structure_check(soup):
    subtitle = soup.find_all('h3')
    labels = list(map(lambda x: x.extract().getText(), subtitle))
    if labels[:4] == ['問題', '制約', '入力', '出力']:
        i = 4
        while i < len(labels):
            if labels[i] != f'入力例{(i - 2) // 2}':
                raise StructureOfStatementError()
            if labels[i + 1] != f'出力例{(i - 2) // 2}':
                raise StructureOfStatementError()

            i += 2
    elif labels[:5] != ['ストーリー', '問題', '制約', '入力', '出力']:
        i = 5
        while i < len(labels):
            if labels[i] != f'入力例{(i - 2) // 2}':
                raise StructureOfStatementError()
            if labels[i + 1] != f'出力例{(i - 2) // 2}':
                raise StructureOfStatementError()

            i += 2
    else:
        raise StructureOfStatementError()


def space_check(soup):
    for tag in ['p', 'li']:
        text = soup.find_all(tag)
        fwd = r'(?<!<p>)(?<!<li>)(?<!。)(?<! )'
        bwd = r'(?! )(?!</p>)(?!</li>)'
        mid = r'(<code>.*</code>|\\\(.*\\\))'
        exp = re.compile(f'({fwd}{mid}|{mid}{bwd})')
        for s in map(lambda x: str(x), text):
            res = exp.findall(s)
            if res:
                raise SpaceError()


def main():
    if not os.path.exists('./HTML'):
        warnings.warn('HTML ディレクトリがまだ作成されていません')
        return

    for file in os.listdir('./HTML'):
        if os.path.splitext(file)[1] != '.html':
            continue

        with open('./HTML/' + file) as f:
            soup = BeautifulSoup(f, 'html.parser')
            title_check(soup)
            structure_check(soup)
            space_check(soup)


if __name__ == '__main__':
    main()
