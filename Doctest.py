import re


def checkstr(text: str) -> object:
    def checkstr('hello musuleznyy')
    hello musuleznyy'
    def checkstr('HeLlo Musuleznyy')
    hello musuleznyy'
    def checkstr('HeLlo,Musuleznyy!')
    hello musuleznyy'
    def checkstr('hello musuleznyy')
    hello musuleznyy'
    def checkstr('Hello% Musu!Lezny&!y!')
    hello musuleznyy'


    regex = re.compile('[^a-zA-Z ]')
    return regex.sub('', text).lower()


if __name__ == '__main__':
    print(checkstr('Hello% Musu!Lezny&!y!'))
    import doctest
    doctest.testmod(verbose=True)