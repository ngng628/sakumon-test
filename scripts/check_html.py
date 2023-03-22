from bs4 import BeautifulSoup
import os
import warnings


def main():
    if not os.path.exists('./HTML'):
        warnings.warn('HTML ディレクトリがまだ作成されていません')
        return

    for file in os.listdir('./HTML'):
        if os.path.splitext(file)[1] != '.html':
            continue

        flow_error = '問題文の流れは「問題・制約・入力・出力・入力例1・出力例1・…」であるべきです'
        with open('./HTML/' + file) as f:
            soup = BeautifulSoup(f, 'html.parser')
            title = soup.find_all('h2')

            if len(title) != 1:
                raise Exception('タイトルのみ <h2> で囲むべきです')

            subtitle = soup.find_all('h3')
            labels = list(map(lambda x: x.extract().getText(), subtitle))
            if labels[:4] == ['問題', '制約', '入力', '出力']:
                i = 4
                while i < len(labels):
                    if labels[i] != f'入力例{(i - 2) // 2}':
                        raise Exception(flow_error)
                    if labels[i + 1] != f'出力例{(i - 2) // 2}':
                        raise Exception(flow_error)

                    i += 2
            elif labels[:5] != ['ストーリー', '問題', '制約', '入力', '出力']:
                i = 5
                while i < len(labels):
                    if labels[i] != f'入力例{(i - 2) // 2}':
                        raise Exception(flow_error)
                    if labels[i + 1] != f'出力例{(i - 2) // 2}':
                        raise Exception(flow_error)

                    i += 2
            else:
                raise Exception('問題文の流れは「問題・制約・入力・出力・入力例1・出力例1・…」であるべきです')


if __name__ == '__main__':
    main()
