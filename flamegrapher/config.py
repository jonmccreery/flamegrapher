import argparse
import flamegrapher
import importlib
import inspect
import os
import pkgutil
import sys

class Config(object):
    def __init__(self, args):
        #self.argparser = argparse.ArgumentParser(
        #    prog='flamegrapher',
        #)
        self.args = self.process_args(args)
        self.stack_managers = {}
        self.discover_stack_managers()
        print(self.stack_managers)


    def process_args(self, args=sys.argv):
        parser = argparse.ArgumentParser(prog='flamegrapher', formatter_class=lambda prog: argparse.HelpFormatter(
                                            prog, max_help_position=80, width=130))
        parser.add_argument('file')
        parser.add_argument('-t', '--type', help="type of stack trace we're processing", default='stacktrace')
        parser.add_argument('-g', '--graphtype', help='type of output file to generate', default='svg')
        parser.add_argument('-o', '--output', help='name of the output file', default='fg.svg')
        args = parser.parse_args(args)
        print(args)
        
        return args

    def discover_stack_managers(self):
        for _, mod, ispkg in pkgutil.walk_packages(path=[os.path.join(os.path.dirname(__file__), 'parsers')],
                                                       prefix='flamegrapher.parsers.'):
            print('in the plugin finder')
            parser = importlib.import_module('{}'.format(mod))
            for name, object in inspect.getmembers(parser):
                print('name: {}, object: {}'.format(name,object))
                if inspect.isclass(object) and issubclass(object, flamegrapher.parsers.baseparser.BaseParser):
                    self.stack_managers[name] = object

