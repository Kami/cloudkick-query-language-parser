import parser

# Create our parser
p = parser.Parser()

queries = [
        # Simple queries
        'node:foo',
        'node:"foo"',
        'node:"foo bar"',
        '-node:foo',
        'tag:foo',
        'tag:"foo"',
        'tag:"foo bar"',
        'provider:aws',
        'provider:"aws"',
        'provider:AWS',

        # Advanced queries
        'node:foo AND tag:bar',
        'node:foo AND tag:bar AND provider:AWS',


            ]
# Parse our input
for query in queries:
    ast = p.parse(query)
    print query, '\n', ast
