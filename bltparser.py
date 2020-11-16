from arpeggio import *
from itertools import chain
from pprint import pprint

def bltfile():          return (first_line, Optional(withdrawn_line),
                                ballots, end_of_ballots,
                                quoted_names)

def comment():          return RegExMatch (r'#.*')
def first_line():       return (number, number)
def withdrawn_line():   return OneOrMore(("-"), single_preference)
def ballots():          return ZeroOrMore(ballot)
def ballot():           return (number, ZeroOrMore(preference), zero)
def end_of_ballots():   return zero

def preference():       return [equal_preference, no_preference]
def equal_preference(): return (single_preference, ZeroOrMore("=", single_preference))
def single_preference():return number
def no_preference():    return "-"

def number():           return RegExMatch (r'[1-9]\d*')
def zero():             return "0"
def quoted_names():     return OneOrMore(quoted_name)
def quoted_name():      return ('"', name, '"')
def name():             return RegExMatch (r'[^"]+')

class BLTVisitor(PTNodeVisitor): 
    def visit_bltfile(self, node, children):
        return dict(chain(children[-1], *children[:-1]))

    def visit_first_line(self, node, children):
        return [("nr_candidates", children[0]), ("nr_seats", children[1])]
    
    def visit_withdrawn_line(self, node, children):
        return [("withdrawn_candidates", children)]

    def visit_ballots(self, node, children):
        return [("ballots", children)]
    
    def visit_ballot(self, node, children):
        return {"weight": children[0], "preferences": children[1:]}

    def visit_equal_preference(self, node, children):
        return children

    def visit_single_preference(self, node, children):
        return int(node.value) - 1

    def visit_no_preference(self, node, children):
        return []
        
    def visit_number(self, node, children):
        return int(node.value)

    def visit_quoted_names(self, node, children):
        return [("title", children[-1]), ("candidates", children[:-1])]

    def visit_name(self, node, children):
        return node.value

def BLTParser():
    return ParserPython(bltfile, comment)

if __name__ == "__main__":
    parser = ParserPython(bltfile, comment)
    parse_tree = parser.parse(sys.stdin.read())
    result = visit_parse_tree(parse_tree, BLTVisitor(debug=False))
    pprint(result, sort_dicts=False)
