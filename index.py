# Licensed under the MIT license: https://github.com/codeclou/advanced-codeblocks-cloud-migration-helper/blob/main/LICENSE

from argparse import ArgumentParser
from lib.macro_storage_format_parser import MacroStorageFormatParser

print("======================================")
print(" ADVANCED CODEBLOCKS MIGRATION HELPER")
print("======================================")
print(" ")

#
# COMMANDLINE ARGUMENTS
#
parser = ArgumentParser()
parser.add_argument("-if", "--inputfile", dest="inputfile",
                    help="the inputfile, a confluence page in storage format XML", metavar="INPUTFILE", required=True)
parser.add_argument("-of", "--outputfile", dest="outputfile",
                    help="the outputfile, a confluence page in storage format XML", metavar="OUTPUTFILE", required=True)
parser.add_argument("-ek", "--extension-key", dest="extensionkey",
                    help="the extension key, TODO ", metavar="EXTENSIONKEY", required=True)
args = parser.parse_args()

#
# RUN TRANSFORMER
#
print("extension key part: " + args.extensionkey)
print(" ")
parser = MacroStorageFormatParser(args.inputfile, args.outputfile, args.extensionkey, False)
parser.transform();