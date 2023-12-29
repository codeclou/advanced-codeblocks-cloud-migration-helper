# Licensed under the MIT license: https://github.com/codeclou/advanced-codeblocks-cloud-migration-helper/blob/main/LICENSE

from lib.util import Util
from bs4.element import CData
import copy

class MacroStorageFormatBuilder:
    def __init__(self, extension_key_part: str, forceUUIDsZeroed: bool):
        self.extension_key_part = extension_key_part # expected something like: 9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f
        self.util = Util(forceUUIDsZeroed)
        self.soup = self.util.get_xml_parser("<root></root>")

    def format_for_test(self, el):
       return el.prettify(formatter="minimal")

    # See test_macro_storage_format_builder.py for output format
    def generate_ac_cloud_macro(self, macro_name: str, cloud_adf_attribute_local_id: str, cloud_adf_parameter_local_id: str, macro_config: str, macro_code: str, macro_param_lang: str, macro_param_enableddl: str, macro_param_globaltitle: str, macro_param_theme: str, macro_param_expand_first: str, macro_param_remotefileurl: str, macro_param_remotefilehttppassword: str, macro_param_remotefilehttpuser: str):
        adf_extension = self.soup.new_tag('ac:adf-extension')
        adf_node = self.soup.new_tag("ac:adf-node", type="extension")

        extension_key_macro_part = ""
        macro_title = ""
        if (macro_name == "advanced-single-codeblock-macro"):
            extension_key_macro_part = "/static/advancedsinglecodeblockmacro"
            macro_title = "Advanced Codeblocks Single"
        elif (macro_name == "advanced-codeblock-macro"):
            extension_key_macro_part =  "/static/advancedcodeblockmacro"
            macro_title = "Advanced Codeblocks Multi"
        elif (macro_name == "advanced-remote-codeblock-macro"):
            extension_key_macro_part =  "/static/advancedremotecodeblockmacro"
            macro_title = "Advanced Codeblocks Multi Remote"
        
        # START OF MACRO

        # <ac:adf-attribute key="extension-type">com.atlassian.ecosystem</ac:adf-attribute>
        adf_attribute_extension_type = self.soup.new_tag("ac:adf-attribute", key="extension-type")
        adf_attribute_extension_type.string = "com.atlassian.ecosystem"
        adf_node.append(adf_attribute_extension_type)

        # <ac:adf-attribute key="extension-key">9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedsinglecodeblockmacro</ac:adf-attribute>
        adf_attribute_extension_key = self.soup.new_tag("ac:adf-attribute", key="extension-key")
        adf_attribute_extension_key.string = self.extension_key_part + extension_key_macro_part
        adf_node.append(adf_attribute_extension_key)

        # <ac:adf-attribute key="parameters">
        adf_attribute_parameters = self.soup.new_tag("ac:adf-attribute", key="parameters")
        adf_node.append(adf_attribute_parameters)

        #   <ac:adf-parameter key="local-id">0235a437-0850-4427-820d-c561666c81da</ac:adf-parameter>
        adf_parameter_local_id = self.soup.new_tag("ac:adf-parameter", key="local-id")
        adf_parameter_local_id.string = cloud_adf_parameter_local_id
        adf_attribute_parameters.append(adf_parameter_local_id)

        #   <ac:adf-parameter key="extension-id">ari:cloud:ecosystem::extension/9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedsinglecodeblockmacro</ac:adf-parameter>
        adf_parameter_extension_id = self.soup.new_tag("ac:adf-parameter", key="extension-id")
        adf_parameter_extension_id.string = "ari:cloud:ecosystem::extension/" + self.extension_key_part + extension_key_macro_part
        adf_attribute_parameters.append(adf_parameter_extension_id)

        #   <ac:adf-parameter key="extension-title">Advanced Codeblocks Single</ac:adf-parameter>
        adf_parameter_extension_title = self.soup.new_tag("ac:adf-parameter", key="extension-title")
        adf_parameter_extension_title.string = macro_title
        adf_attribute_parameters.append(adf_parameter_extension_title)

        #   <ac:adf-parameter key="guest-params">
        adf_parameter_guest_params = self.soup.new_tag("ac:adf-parameter", key="guest-params")
        adf_attribute_parameters.append(adf_parameter_guest_params)

        #     <ac:adf-parameter key="globaltitle">El title</ac:adf-parameter>
        adf_parameter_guest_params_globaltitle = self.soup.new_tag("ac:adf-parameter", key="globaltitle")
        adf_parameter_guest_params_globaltitle.string = macro_param_globaltitle
        adf_parameter_guest_params.append(adf_parameter_guest_params_globaltitle)

        if (macro_name != "advanced-remote-codeblock-macro"):
            #     <ac:adf-parameter key="code">awesome code 123</ac:adf-parameter>
            adf_parameter_guest_params_code = self.soup.new_tag("ac:adf-parameter", key="code")
            adf_parameter_guest_params_code.string = CData(macro_code)
            adf_parameter_guest_params.append(adf_parameter_guest_params_code)

        if (macro_name == "advanced-codeblock-macro" or macro_name == "advanced-remote-codeblock-macro"):
            #     <ac:adf-parameter key="config">[foo]\nfoo=bar</ac:adf-parameter>
            adf_parameter_guest_params_config = self.soup.new_tag("ac:adf-parameter", key="config")
            adf_parameter_guest_params_config.string = CData(macro_config)
            adf_parameter_guest_params.append(adf_parameter_guest_params_config)

        if (macro_name == "advanced-codeblock-macro" or macro_name == "advanced-single-codeblock-macro"):
            #     <ac:adf-parameter key="enableddl"><ac:adf-parameter-value>true</ac:adf-parameter-value></ac:adf-parameter>
            adf_parameter_guest_params_enableddl = self.soup.new_tag("ac:adf-parameter", key="enableddl")
            adf_parameter_guest_params_enableddl_value = self.soup.new_tag("ac:adf-parameter-value")
            if (macro_param_enableddl == "true"):
                adf_parameter_guest_params_enableddl_value.string = "true"
                # NOTE: True  is: <ac:adf-parameter key="enableddl"><ac:adf-parameter-value>true</ac:adf-parameter-value></ac:adf-parameter>
                #       False is: <ac:adf-parameter key="enableddl"><ac:adf-parameter-value /></ac:adf-parameter>
            adf_parameter_guest_params_enableddl.append(adf_parameter_guest_params_enableddl_value)
            adf_parameter_guest_params.append(adf_parameter_guest_params_enableddl)

        if (macro_name == "advanced-codeblock-macro" or macro_name == "advanced-remote-codeblock-macro"):
            #     <ac:adf-parameter key="expandfirst"><ac:adf-parameter-value>true</ac:adf-parameter-value></ac:adf-parameter>
            adf_parameter_guest_params_expandfirst = self.soup.new_tag("ac:adf-parameter", key="expandfirst")
            adf_parameter_guest_params_expandfirst_value = self.soup.new_tag("ac:adf-parameter-value")
            if (macro_param_expand_first == "true"):
                adf_parameter_guest_params_expandfirst_value.string = "true"
                # NOTE: True  is: <ac:adf-parameter key="expandfirst"><ac:adf-parameter-value>true</ac:adf-parameter-value></ac:adf-parameter>
                #       False is: <ac:adf-parameter key="expandfirst"><ac:adf-parameter-value /></ac:adf-parameter>
            adf_parameter_guest_params_expandfirst.append(adf_parameter_guest_params_expandfirst_value)
            adf_parameter_guest_params.append(adf_parameter_guest_params_expandfirst)

        if (macro_name == "advanced-remote-codeblock-macro"):
            #     <ac:adf-parameter key="remotefileurl">https://foo</ac:adf-parameter>
            adf_parameter_guest_params_remote_url = self.soup.new_tag("ac:adf-parameter", key="remotefileurl")
            adf_parameter_guest_params_remote_url.string = macro_param_remotefileurl
            adf_parameter_guest_params.append(adf_parameter_guest_params_remote_url)
            #     <ac:adf-parameter key="remotefilehttpuser">usr</ac:adf-parameter>
            adf_parameter_guest_params_remote_user = self.soup.new_tag("ac:adf-parameter", key="remotefilehttpuser")
            adf_parameter_guest_params_remote_user.string = macro_param_remotefilehttpuser
            adf_parameter_guest_params.append(adf_parameter_guest_params_remote_user)
            #     <ac:adf-parameter key="remotefilehttppassword">s3cret</ac:adf-parameter>
            adf_parameter_guest_params_remote_password = self.soup.new_tag("ac:adf-parameter", key="remotefilehttppassword")
            adf_parameter_guest_params_remote_password.string = macro_param_remotefilehttppassword
            adf_parameter_guest_params.append(adf_parameter_guest_params_remote_password)

        #     <ac:adf-parameter key="theme">light-spring</ac:adf-parameter>
        adf_parameter_guest_params_theme = self.soup.new_tag("ac:adf-parameter", key="theme")
        adf_parameter_guest_params_theme.string = macro_param_theme
        adf_parameter_guest_params.append(adf_parameter_guest_params_theme)

        #     <ac:adf-parameter key="lang">actionscript</ac:adf-parameter>
        adf_parameter_guest_params_lang = self.soup.new_tag("ac:adf-parameter", key="lang")
        adf_parameter_guest_params_lang.string = macro_param_lang
        adf_parameter_guest_params.append(adf_parameter_guest_params_lang)

        # <ac:adf-attribute key="text">Advanced Codeblocks Single</ac:adf-attribute>
        adf_attribute_text = self.soup.new_tag("ac:adf-attribute", key="text")
        adf_attribute_text.string = macro_title
        adf_node.append(adf_attribute_text)

        # <ac:adf-attribute key="layout">default</ac:adf-attribute>
        adf_attribute_layout = self.soup.new_tag("ac:adf-attribute", key="layout")
        adf_attribute_layout.string = "default"
        adf_node.append(adf_attribute_layout)

        # <ac:adf-attribute key="local-id">2ba8fa32-cce8-4b12-bcf3-191e9bbf1469</ac:adf-attribute>
        adf_attribute_local_id = self.soup.new_tag("ac:adf-attribute", key="local-id")
        adf_attribute_local_id.string = cloud_adf_attribute_local_id
        adf_node.append(adf_attribute_local_id)

        # END OF MACRO

        # Note: We need to provide a copy of adf_node to adf_fallback at the end!
        adf_fallback = self.soup.new_tag("ac:adf-fallback")
        adf_node_copy = copy.copy(adf_node)
        adf_fallback.append(adf_node_copy)
        adf_extension.append(adf_node)
        adf_extension.append(adf_fallback)

        return adf_extension

