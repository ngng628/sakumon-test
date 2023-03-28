class FileNameError(Exception):
    def __init__(self, msg='おそらく入力ファイル名が *.in の形式になっていません'):
        self._msg = msg

    def __str__(self):
        return self._msg


class TitleTagError(Exception):
    def __init__(self, msg='タイトルのみ<h2>で囲むべきです'):
        self._msg = msg

    def __str__(self):
        return self._msg


class StructureOfStatementError(Exception):
    def __init__(self, msg='問題文の流れは「問題・制約・入力・出力・入力例1・出力例1・…」であるべきです'):
        self._msg = msg

    def __str__(self):
        return self._msg


class SpaceError(Exception):
    def __init__(self, msg=r'\( \) や <code> </code> の前後には空白を入れるべきです'):
        self._msg = msg

    def __str__(self):
        return self._msg
