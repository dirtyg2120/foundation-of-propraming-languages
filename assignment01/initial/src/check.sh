#! /bin/sh
python3 run.py gen
python3 run.py test LexerSuite
python3 run.py test ParserSuite
