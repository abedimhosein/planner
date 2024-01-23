def to_persian_digits(txt: str or int) -> str:
    if isinstance(txt, int):
        txt = str(txt)

    encoder = {
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
        '0': '۰',
        '.': '.',
        '-': '/',
        ' ': ' ',
    }
    return ''.join([encoder.get(d, d) for d in txt])


def to_english_digits(txt: str, lookup=None) -> str:
    if lookup is None:
        lookup = dict()

    encoder = {
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '۰': '0',
        '.': '.',
        ' ': ' ',
    }
    encoder.update(lookup)
    return ''.join([encoder.get(d, d) for d in txt])
