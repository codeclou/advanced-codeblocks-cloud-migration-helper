# Licensed under the MIT license: https://github.com/codeclou/advanced-codeblocks-cloud-migration-helper/blob/main/LICENSE

# https://docs.python.org/3/library/unittest.html

import unittest 
from lib.util import Util

class TestUtil(unittest.TestCase):

    def test_bool_to_string_for_print__true(self):
        # GIVEN
        util = Util(False)
        input = True
        # WHEN
        res = util.bool_to_string_for_print(input)
        # THEN
        self.assertEqual(res, 'true')

    def test_bool_to_string_for_print__false(self):
        # GIVEN
        util = Util(False)
        input = False
        # WHEN
        res = util.bool_to_string_for_print(input)
        # THEN
        self.assertEqual(res, 'false')

    def test_shorten_string_for_print__valid(self):
        # GIVEN
        util = Util(False)
        input = "this is a very long long long long long long long long long long long long long long long long long long long string"
        # WHEN
        res = util.shorten_string_for_print(input)
        # THEN
        self.assertEqual(res, 'this is a very long long long long long long long long long ...')

    def test_format_xml_for_final_output__valid(self):
        # GIVEN
        util = Util(False)
        input = '<xml><some attr="foo">bar</some></xml>'
        # WHEN
        res = util.format_xml_for_final_output(input)
        # THEN
        self.assertEqual(res, '<xml>\n  <some attr="foo">bar</some>\n</xml>\n')

    def test_generate_uuid__valid(self):
        # GIVEN
        util = Util(False)
        # WHEN
        res = util.generate_uuid()
        # THEN
        self.assertEqual(type(res), str)

    def test_generate_uuid__valid_zero(self):
        # GIVEN
        util = Util(True)
        # WHEN
        res = util.generate_uuid()
        # THEN
        self.assertEqual(res, "00000000-0000-0000-0000-000000000000")

    def test_get_xml_parser__valid(self):
        # GIVEN
        util = Util(False)
        input = '<xml><some attr="foo">bar</some></xml>'
        # WHEN
        res = util.get_xml_parser("<root></root>")
        new_el = res.new_tag("ac:adf-attribute", key="extension-type")
        # THEN
        self.assertEqual(str(new_el), '<ac:adf-attribute key="extension-type"></ac:adf-attribute>')

    def test_replace_server_macro_lang_with_cloud_pendant__valid(self):
        # GIVEN
        util = Util(False)
        input = 'Bash'
        # WHEN
        res = util.replace_server_macro_lang_with_cloud_pendant(input)
        # THEN
        self.assertEqual(res, 'bash')

    def test_replace_server_macro_lang_with_cloud_pendant__valid2(self):
        # GIVEN
        util = Util(False)
        input = 'ARM Assembly'
        # WHEN
        res = util.replace_server_macro_lang_with_cloud_pendant(input)
        # THEN
        self.assertEqual(res, 'armasm')

    def test_replace_server_macro_lang_with_cloud_pendant__invalid(self):
        # GIVEN
        util = Util(False)
        input = 'SomeNonLang'
        # WHEN
        res = util.replace_server_macro_lang_with_cloud_pendant(input)
        # THEN
        self.assertEqual(res, '')

if __name__ == '__main__':
    unittest.main()