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
