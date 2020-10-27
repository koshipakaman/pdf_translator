import re
from collections import OrderedDict
import functools
from pprint import pprint

class OrderedClass(type):
# meta class

    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        
        return OrderedDict()

    def __new__(metacls, name, bases, namespace, **kwds):

        cls = type.__new__(metacls, name, bases, dict(namespace))

        cls.members = tuple(namespace)
        return cls

class Rule(metaclass=OrderedClass):
    
    def __init__(self):
        
        self.rules = []
        special_method = re.compile('__\w+__')

        for attr in self.members:
        
            if not bool(special_method.fullmatch(attr)):

                rule = eval(f"self.{attr}")
                if callable(rule): self.rules.append(rule)


class OrRule(Rule):

    def __call__(self, text):

        for method in self.rules:

            if method(text): return True

        return False


class AndRule(Rule):
    
    def __call__(self, text):

        for method in self.rules:

            if not method(text): return False

        return True


if __name__ == "__main__":

    pass
