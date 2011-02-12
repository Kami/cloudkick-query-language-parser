all:
	make javascript
	make python

javascript:
	waxeye --debug -g javascript . query_language.waxeye

python:
	waxeye --debug -g python . query_language.waxeye

tests:
	python tests.py

clean:
	rm parser.py
	rm parser.js
