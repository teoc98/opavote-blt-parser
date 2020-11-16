# opavote-blt-parser
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/teoc98/opavote-blt-parser/blob/main/LICENSE)

A simple parser for the [BLT file format](https://www.opavote.com/help/overview#blt-file-format) used by [opavote.com](https://www.opavote.com). 

## Prerequisites
* [Python](https://www.python.org/) 2.7, 3.4+. Other versions might work but are not tested. 
* [Arpeggio](https://github.com/textX/Arpeggio)

## Sample usage

### Standalone
```
cat sample.blt | python3 bltparser.py
```

### As a module
```
from bltparser import BLTParser, BLTVisitor

parser = BLTParser()
parse_tree = parser.parse(sys.stdin.read())
result = visit_parse_tree(parse_tree, BLTVisitor())
pprint(result, sort_dicts=False)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
