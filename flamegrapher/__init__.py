from flamegrapher.config import Config
from flamegrapher.parsers import stackparser

class Flamegrapher(object):
    def __init__(self, args, **kwargs):
        print('args: ', args[1:])
        print('kwargs: ', kwargs)
        config = Config(args[1:])


def main(args):
    fg = Flamegrapher(args)
    sp = stackparser.StackParser()
    

