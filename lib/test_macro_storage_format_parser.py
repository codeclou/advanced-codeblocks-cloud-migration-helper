# Licensed under the MIT license: https://github.com/codeclou/advanced-codeblocks-cloud-migration-helper/blob/main/LICENSE

# https://docs.python.org/3/library/unittest.html

import unittest

from lib.macro_storage_format_parser import MacroStorageFormatParser


class TestMacroStorageFormatParser(unittest.TestCase):
    def test_transform___valid_multi(self):
        self.maxDiff = None
        # GIVEN
        input_file = "./lib/input/ac-multi-test1.input.storage"
        output_file = "./lib/output/ac-multi-test1.output.storage"
        expected_output_file = "./lib/output-expected/ac-multi-test1.output.storage"
        extension_key = (
            "9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f"
        )
        # WHEN
        parser = MacroStorageFormatParser(input_file, output_file, extension_key, True)
        parser.transform()
        # THEN
        self.assertListEqual(list(open(output_file)), list(open(expected_output_file)))

    def test_transform___invalid_multi(self):
        self.maxDiff = None
        # GIVEN
        input_file = "./lib/input/ac-multi-test2.input.storage"
        output_file = "./lib/output/ac-multi-test2.output.storage"
        expected_output_file = "./lib/output-expected/ac-multi-test2.output.storage"
        extension_key = (
            "9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f"
        )
        # WHEN
        parser = MacroStorageFormatParser(input_file, output_file, extension_key, True)
        parser.transform()
        # THEN
        self.assertListEqual(list(open(output_file)), list(open(expected_output_file)))

    def test_transform___valid_single(self):
        self.maxDiff = None
        # GIVEN
        input_file = "./lib/input/ac-single-test1.input.storage"
        output_file = "./lib/output/ac-single-test1.output.storage"
        expected_output_file = "./lib/output-expected/ac-single-test1.output.storage"
        extension_key = (
            "9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f"
        )
        # WHEN
        parser = MacroStorageFormatParser(input_file, output_file, extension_key, True)
        parser.transform()
        # THEN
        self.assertListEqual(list(open(output_file)), list(open(expected_output_file)))

    def test_transform___valid_remote(self):
        self.maxDiff = None
        # GIVEN
        input_file = "./lib/input/ac-remote-test1.input.storage"
        output_file = "./lib/output/ac-remote-test1.output.storage"
        expected_output_file = "./lib/output-expected/ac-remote-test1.output.storage"
        extension_key = (
            "9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f"
        )
        # WHEN
        parser = MacroStorageFormatParser(input_file, output_file, extension_key, True)
        parser.transform()
        # THEN
        self.assertListEqual(list(open(output_file)), list(open(expected_output_file)))

    def test_transform___newlines(self):
        self.maxDiff = None
        # INIT
        input_file = "./lib/input/ac-remote-test1.input.storage"
        output_file = "./lib/output/ac-remote-test1.output.storage"
        extension_key = (
            "9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f"
        )
        parser = MacroStorageFormatParser(input_file, output_file, extension_key, True)
        # ###########################################################################
        # CASE1: \r\n
        #
        # GIVEN
        macro_body1 = "foo\n[content]\r\nbar"
        # WHEN
        result1 = parser._split_macro_body_on_content_block(macro_body1)
        # THEN
        self.assertTrue(isinstance(result1, tuple))
        self.assertEqual(result1[0], "foo\n")
        self.assertEqual(result1[1], "bar")
        # ###########################################################################
        # CASE2: \r
        #
        # GIVEN
        macro_body2 = "foo\r[content]\rbar"
        # WHEN
        result2 = parser._split_macro_body_on_content_block(macro_body2)
        # THEN
        self.assertTrue(isinstance(result2, tuple))
        self.assertEqual(result2[0], "foo\r")
        self.assertEqual(result2[1], "bar")
        # ###########################################################################
        # CASE3: \r\n
        #
        # GIVEN
        macro_body3 = "foo\r[content]\r\nbar"
        # WHEN
        result3 = parser._split_macro_body_on_content_block(macro_body3)
        # THEN
        self.assertTrue(isinstance(result3, tuple))
        self.assertEqual(result3[0], "foo\r")
        self.assertEqual(result3[1], "bar")
        # ###########################################################################
        # CASE4: \n
        #
        # GIVEN
        macro_body4 = "foo\n[content]\nbar"
        # WHEN
        result4 = parser._split_macro_body_on_content_block(macro_body4)
        # THEN
        self.assertTrue(isinstance(result4, tuple))
        self.assertEqual(result4[0], "foo\n")
        self.assertEqual(result4[1], "bar")
