# Licensed under the MIT license: https://github.com/codeclou/advanced-codeblocks-cloud-migration-helper/blob/main/LICENSE

from lib.macro_storage_format_builder import MacroStorageFormatBuilder
from lib.util import Util
import re

class MacroStorageFormatParser:
    def __init__(
        self, inputfile: str, outputfile: str, extensionkey: str, forceUUIDsZeroed: bool
    ):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.extensionkey = extensionkey
        self.forceUUIDsZeroed = forceUUIDsZeroed
        self.util = Util(forceUUIDsZeroed)

    def _split_macro_body_on_content_block(self, macro_body: str) -> tuple[str, str]:
        if "[content]" in macro_body:
            splitted = re.split(r'\[content\]\s*(\r\n|\r|\n\r|\n)', macro_body, maxsplit=1)
            # re.split splits also the capturing group \n as [1]!
            return (splitted[0], splitted[2])
        return ("ERROR SPLITTING AT [CONTENT]", "ERROR: INVALID NEWLINE")

    def transform(self):
        builder = MacroStorageFormatBuilder(self.extensionkey, self.forceUUIDsZeroed)
        print("START > reading storage format file from: " + self.inputfile)
        print(" ")
        with open(self.inputfile) as file:
            xml_string = file.read()
        soup = self.util.get_xml_parser(xml_string)
        all_macros = soup.find_all("ac:structured-macro", recursive=True)
        page_has_ac_macro = False
        for macro_node in all_macros:
            #
            # STEP 1: Parse DC Advanced Codeblock Macros
            #
            if (
                macro_node.attrs["ac:name"] == "advanced-single-codeblock-macro"
                or macro_node.attrs["ac:name"] == "advanced-codeblock-macro"
                or macro_node.attrs["ac:name"] == "advanced-remote-codeblock-macro"
            ):
                page_has_ac_macro = True
                macro_name = macro_node.attrs["ac:name"]
                print(">> " + macro_name)
                # ----
                # all macros:
                #   <ac:plain-text-body><![CDATA[echo "foo"]]></ac:plain-text-body>
                macro_code = ""
                macro_config = ""
                #   <ac:parameter ac:name="lang">Apache</ac:parameter>
                #   <ac:parameter ac:name="globaltitle">AC_testsysteme_ddl</ac:parameter>
                #   <ac:parameter ac:name="theme">light-mono</ac:parameter>
                macro_param_lang = ""
                macro_param_globaltitle = ""
                macro_param_theme = "light-spring"
                #
                # multi and single only:
                #   <ac:parameter ac:name="enableddl">true</ac:parameter>
                macro_param_enableddl = "false"
                #
                # multi and remote only:
                #   <ac:parameter ac:name="expandFirst">true</ac:parameter>
                macro_param_expand_first = "false"
                #
                # remote only:
                #   <ac:parameter ac:name="remotefileurl">https://codeclou.io/file.py</ac:parameter>
                #   <ac:parameter ac:name="remotefilehttppassword">pass</ac:parameter>
                #   <ac:parameter ac:name="remotefilehttpuser">user</ac:parameter>
                macro_param_remotefileurl = ""
                macro_param_remotefilehttppassword = ""
                macro_param_remotefilehttpuser = ""
                # ----
                macro_children = macro_node.findChildren()
                for child in macro_children:
                    if child.name == "ac:plain-text-body":
                        if macro_name == "advanced-single-codeblock-macro":
                            macro_code = child.text
                            macro_config = ""
                        elif macro_name == "advanced-codeblock-macro":
                            if "[content]" not in child.text:
                                print(
                                    ">> ERROR: no [content] element in macro body found!"
                                )
                                macro_code = "ERROR - COULD NOT PARSE"
                                macro_config = "ERROR - COULD NOT PARSE"
                            else:
                                config_and_code = (
                                    self._split_macro_body_on_content_block(child.text)
                                )
                                macro_code = config_and_code[1]
                                macro_config = config_and_code[0]
                        elif macro_name == "advanced-remote-codeblock-macro":
                            macro_code = ""
                            macro_config = child.text
                        print(
                            "    macro config (shortened): "
                            + self.util.shorten_string_for_print(macro_config)
                        )
                        print(
                            "    macro code (shortened)  : "
                            + self.util.shorten_string_for_print(macro_code)
                        )
                    if child.name == "ac:parameter":
                        ac_name = child.get("ac:name")
                        if ac_name == "lang":
                            macro_param_lang = (
                                self.util.replace_server_macro_lang_with_cloud_pendant(
                                    child.text
                                )
                            )
                            print("    macro param lang        : " + macro_param_lang)
                        if ac_name == "enableddl":
                            macro_param_enableddl = child.text
                            print(
                                "    macro param enableddl   : " + macro_param_enableddl
                            )
                        if ac_name == "globaltitle":
                            macro_param_globaltitle = child.text
                            print(
                                "    macro param globaltitle : "
                                + macro_param_globaltitle
                            )
                        if ac_name == "theme":
                            macro_param_theme = child.text
                            print("    macro param theme       : " + macro_param_theme)
                        if ac_name == "expandFirst":
                            macro_param_expand_first = child.text
                            print(
                                "    macro param expand first: "
                                + macro_param_expand_first
                            )
                        if ac_name == "remotefileurl":
                            macro_param_remotefileurl = child.text
                            print(
                                "    macro param remote url  : "
                                + macro_param_remotefileurl
                            )
                        if ac_name == "remotefilehttpuser":
                            macro_param_remotefilehttpuser = child.text
                            print(
                                "    macro param remote user : "
                                + macro_param_remotefilehttpuser
                            )
                        if ac_name == "remotefilehttppassword":
                            macro_param_remotefilehttppassword = child.text
                            print(
                                "    macro param remote pass : "
                                + macro_param_remotefilehttppassword
                            )
                #
                # STEP 2: Generate Cloud Advanced Codeblock Macro storage formats
                #
                cloud_adf_attribute_local_id = self.util.generate_uuid()
                cloud_adf_parameter_local_id = self.util.generate_uuid()
                print("    macro attr local id     : " + cloud_adf_attribute_local_id)
                print("    macro param local id    : " + cloud_adf_parameter_local_id)
                cloud_macro_storage_format = builder.generate_ac_cloud_macro(
                    macro_name,
                    cloud_adf_attribute_local_id,
                    cloud_adf_parameter_local_id,
                    macro_config,
                    macro_code,
                    macro_param_lang,
                    macro_param_enableddl,
                    macro_param_globaltitle,
                    macro_param_theme,
                    macro_param_expand_first,
                    macro_param_remotefileurl,
                    macro_param_remotefilehttppassword,
                    macro_param_remotefilehttpuser,
                )
                macro_node.replaceWith(cloud_macro_storage_format)
        if not page_has_ac_macro:
            print(">> no Advanced Codeblocks macros found in page")
        #
        # STEP 3: Write outputfile
        #
        output_file_content = soup.prettify(formatter="minimal")
        f = open(self.outputfile, "w")
        f.write(output_file_content)
        f.close()
        print(" ")
        print("DONE > written transformed storage format to: " + self.outputfile)
        print(" ")
