import unittest

from waxeye import ParseError
from parser import Parser

TOKEN_MAPPINGS = {
    'node_token': 'node_token',
    'tag_token': 'tag_token',
    'provider_token': 'provider_token',
    'all_token': 'all_token',

    'node_value': 'node_name',
    'node_value': 'tag_name',
    'node_value': 'provider_name',
}

token_names = [ 'node', 'tag', 'provider' ]

valid_names = [ 'foo', '"foo bar"',  'bar-*', '"test longer-nodename*"']
invalid_names = [ 'foo bar', '!!!bar', '', '"', '\'', '""', '\'\'' ]

valid_provider_names_lower = [ 'aws', 'ec2east', 'ec2eu', 'gogrid',
                               'linode', 'rackspace', 'rimu', 'slicehost',
                               'softlayer', 'vpsnet', 'private', 'agent']
valid_provider_names_upper = [ name.upper() for name in
                               valid_provider_names_lower ]

p = Parser()

class TestParser(unittest.TestCase):
    def test_simple_queries(self):
        for token_name in token_names:
            if token_name == 'provider':
                value_names = valid_provider_names_lower + valid_provider_names_upper
            else:
                value_names = valid_names

            for value_name in value_names:
               ast = p.parse('%s:%s' % (token_name, value_name))
               self.assertEqual(ast.children[0].type, TOKEN_MAPPINGS['%s_token' %
                                                      (token_name)])
               self.assertEqual(len(ast.children), 1)

    def test_invalid_queries(self):
       for token_name in token_names:
            value_names = invalid_names

            for value_name in value_names:
               ast = p.parse('%s:%s' % (token_name, value_name))
               self.assertTrue(isinstance(ast, ParseError))

    def assertChildrenContainsToken(children, token_name):
        token_name_len = len(token_name)
        children_len = len(children)

        if children_len < token_names:
            self.fail()

        for index, char in enumerate(children):
            name_char = toke_name[i]
            children_char = children[i]

            self.assertEqual(name_char, children_char)

if __name__ == '__main__':
    unittest.main()
