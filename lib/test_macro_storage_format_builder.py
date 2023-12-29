# Licensed under the MIT license: https://github.com/codeclou/advanced-codeblocks-cloud-migration-helper/blob/main/LICENSE

# https://docs.python.org/3/library/unittest.html

import unittest 
from lib.macro_storage_format_builder import MacroStorageFormatBuilder
from lib.util import Util



class TestMacroStorageFormatBuilder(unittest.TestCase):

    def test_generate_ac_cloud_macro___valid_single(self):
        self.maxDiff=None
        #
        # GIVEN
        #
        util = Util(False)
        cloud_extension_key_part = "9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f"
        cloud_adf_attribute_local_id = "2ba8fa32-cce8-4b12-bcf3-191e9bbf1469"
        cloud_adf_parameter_local_id = "0235a437-0850-4427-820d-c561666c81da"
        builder = MacroStorageFormatBuilder(cloud_extension_key_part, False)
        macro_name = "advanced-single-codeblock-macro"
        macro_param_lang = "actionscript"
        macro_param_enableddl = "true"
        macro_param_globaltitle = "Super Code"
        macro_param_theme = "light-spring"
        macro_param_expand_first = ""
        macro_param_remotefileurl = ""
        macro_param_remotefilehttpuser = ""
        macro_param_remotefilehttppassword = "" 
        macro_config = ""
        macro_code = "const foo = 'bar';"
        #
        # WHEN
        #
        res = builder.generate_ac_cloud_macro(macro_name, cloud_adf_attribute_local_id, cloud_adf_parameter_local_id, macro_config, macro_code, macro_param_lang, macro_param_enableddl, macro_param_globaltitle, macro_param_theme, macro_param_expand_first, macro_param_remotefileurl, macro_param_remotefilehttppassword, macro_param_remotefilehttpuser)
        #
        # THEN
        #
        self.assertEqual(util.format_xml_for_final_output(res),  util.format_xml_for_final_output("""<ac:adf-extension>
    <ac:adf-node type="extension">
        <ac:adf-attribute key="extension-type">com.atlassian.ecosystem</ac:adf-attribute>
        <ac:adf-attribute key="extension-key">9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedsinglecodeblockmacro</ac:adf-attribute>
        <ac:adf-attribute key="parameters">
            <ac:adf-parameter key="local-id">0235a437-0850-4427-820d-c561666c81da</ac:adf-parameter>
            <ac:adf-parameter key="extension-id">ari:cloud:ecosystem::extension/9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedsinglecodeblockmacro</ac:adf-parameter>
            <ac:adf-parameter key="extension-title">Advanced Codeblocks Single</ac:adf-parameter>
            <ac:adf-parameter key="guest-params">
                <ac:adf-parameter key="globaltitle">Super Code</ac:adf-parameter>
                <ac:adf-parameter key="code"><![CDATA[const foo = 'bar';]]></ac:adf-parameter>
                <ac:adf-parameter key="enableddl">
                    <ac:adf-parameter-value>true</ac:adf-parameter-value>
                </ac:adf-parameter>
                <ac:adf-parameter key="theme">light-spring</ac:adf-parameter>
                <ac:adf-parameter key="lang">actionscript</ac:adf-parameter>
            </ac:adf-parameter>
        </ac:adf-attribute>
        <ac:adf-attribute key="text">Advanced Codeblocks Single</ac:adf-attribute>
        <ac:adf-attribute key="layout">default</ac:adf-attribute>
        <ac:adf-attribute key="local-id">2ba8fa32-cce8-4b12-bcf3-191e9bbf1469</ac:adf-attribute>
    </ac:adf-node>
    <ac:adf-fallback>
        <ac:adf-node type="extension">
            <ac:adf-attribute key="extension-type">com.atlassian.ecosystem</ac:adf-attribute>
            <ac:adf-attribute key="extension-key">9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedsinglecodeblockmacro</ac:adf-attribute>
            <ac:adf-attribute key="parameters">
                <ac:adf-parameter key="local-id">0235a437-0850-4427-820d-c561666c81da</ac:adf-parameter>
                <ac:adf-parameter key="extension-id">ari:cloud:ecosystem::extension/9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedsinglecodeblockmacro</ac:adf-parameter>
                <ac:adf-parameter key="extension-title">Advanced Codeblocks Single</ac:adf-parameter>
                <ac:adf-parameter key="guest-params">
                    <ac:adf-parameter key="globaltitle">Super Code</ac:adf-parameter>
                    <ac:adf-parameter key="code"><![CDATA[const foo = 'bar';]]></ac:adf-parameter>
                    <ac:adf-parameter key="enableddl">
                        <ac:adf-parameter-value>true</ac:adf-parameter-value>
                    </ac:adf-parameter>
                    <ac:adf-parameter key="theme">light-spring</ac:adf-parameter>
                    <ac:adf-parameter key="lang">actionscript</ac:adf-parameter>
                </ac:adf-parameter>
            </ac:adf-attribute>
            <ac:adf-attribute key="text">Advanced Codeblocks Single</ac:adf-attribute>
            <ac:adf-attribute key="layout">default</ac:adf-attribute>
            <ac:adf-attribute key="local-id">2ba8fa32-cce8-4b12-bcf3-191e9bbf1469</ac:adf-attribute>
        </ac:adf-node>
    </ac:adf-fallback>
</ac:adf-extension>"""))



    def test_generate_ac_cloud_macro___valid_multi(self):
        self.maxDiff=None
        #
        # GIVEN
        #
        util = Util(False)
        cloud_extension_key_part = "9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f"
        cloud_adf_attribute_local_id = "2ba8fa32-cce8-4b12-bcf3-191e9bbf1469"
        cloud_adf_parameter_local_id = "0235a437-0850-4427-820d-c561666c81da"
        builder = MacroStorageFormatBuilder(cloud_extension_key_part, False)
        macro_name = "advanced-codeblock-macro"
        macro_param_lang = "Apache"
        macro_param_enableddl = "true"
        macro_param_globaltitle = "AC_testsysteme_ddl"
        macro_param_theme = "light-spring"
        macro_param_expand_first = "true"
        macro_param_remotefileurl = ""
        macro_param_remotefilehttpuser = ""
        macro_param_remotefilehttppassword = "" 
        macro_config = """
[testsystem 1]
base.url = www.myserver1.com
document.root = /www/server1

[testsystem 2]
base.url = www.myserver2.com
document.root = /www/server2

"""
        macro_code = """<VirtualHost *:80>
   DocumentRoot ${document.root}
   ServerName ${base.url}
   ...
</VirtualHost>"""
        #
        # WHEN
        #
        res = builder.generate_ac_cloud_macro(macro_name, cloud_adf_attribute_local_id, cloud_adf_parameter_local_id, macro_config, macro_code, macro_param_lang, macro_param_enableddl, macro_param_globaltitle, macro_param_theme, macro_param_expand_first, macro_param_remotefileurl, macro_param_remotefilehttppassword, macro_param_remotefilehttpuser)
        #
        # THEN
        #
        self.assertEqual(util.format_xml_for_final_output(res),  util.format_xml_for_final_output("""<ac:adf-extension>
 <ac:adf-node type="extension">
  <ac:adf-attribute key="extension-type">com.atlassian.ecosystem</ac:adf-attribute>
  <ac:adf-attribute key="extension-key">9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedcodeblockmacro</ac:adf-attribute>
  <ac:adf-attribute key="parameters">
    <ac:adf-parameter key="local-id">0235a437-0850-4427-820d-c561666c81da</ac:adf-parameter>
    <ac:adf-parameter key="extension-id">ari:cloud:ecosystem::extension/9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedcodeblockmacro</ac:adf-parameter>
    <ac:adf-parameter key="extension-title">Advanced Codeblocks Multi</ac:adf-parameter>
    <ac:adf-parameter key="guest-params">
        <ac:adf-parameter key="globaltitle">AC_testsysteme_ddl</ac:adf-parameter>
        <ac:adf-parameter key="code"><![CDATA[<VirtualHost *:80>
   DocumentRoot ${document.root}
   ServerName ${base.url}
   ...
</VirtualHost>]]></ac:adf-parameter><ac:adf-parameter key="config"><![CDATA[
[testsystem 1]
base.url = www.myserver1.com
document.root = /www/server1

[testsystem 2]
base.url = www.myserver2.com
document.root = /www/server2

]]></ac:adf-parameter>
        <ac:adf-parameter key="enableddl"><ac:adf-parameter-value>true</ac:adf-parameter-value></ac:adf-parameter>
        <ac:adf-parameter key="expandfirst"><ac:adf-parameter-value>true</ac:adf-parameter-value></ac:adf-parameter>
        <ac:adf-parameter key="theme">light-spring</ac:adf-parameter><ac:adf-parameter key="lang">Apache</ac:adf-parameter></ac:adf-parameter>
  </ac:adf-attribute>
  <ac:adf-attribute key="text">Advanced Codeblocks Multi</ac:adf-attribute>
  <ac:adf-attribute key="layout">default</ac:adf-attribute>
  <ac:adf-attribute key="local-id">2ba8fa32-cce8-4b12-bcf3-191e9bbf1469</ac:adf-attribute>
 </ac:adf-node>
 <ac:adf-fallback>
  <ac:adf-node type="extension">
   <ac:adf-attribute key="extension-type">com.atlassian.ecosystem</ac:adf-attribute>
   <ac:adf-attribute key="extension-key">9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedcodeblockmacro</ac:adf-attribute>
   <ac:adf-attribute key="parameters"><ac:adf-parameter key="local-id">0235a437-0850-4427-820d-c561666c81da</ac:adf-parameter><ac:adf-parameter key="extension-id">ari:cloud:ecosystem::extension/9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedcodeblockmacro</ac:adf-parameter><ac:adf-parameter key="extension-title">Advanced Codeblocks Multi</ac:adf-parameter><ac:adf-parameter key="guest-params"><ac:adf-parameter key="globaltitle">AC_testsysteme_ddl</ac:adf-parameter><ac:adf-parameter key="code"><![CDATA[<VirtualHost *:80>
   DocumentRoot ${document.root}
   ServerName ${base.url}
   ...
</VirtualHost>]]></ac:adf-parameter><ac:adf-parameter key="config"><![CDATA[
[testsystem 1]
base.url = www.myserver1.com
document.root = /www/server1

[testsystem 2]
base.url = www.myserver2.com
document.root = /www/server2

]]></ac:adf-parameter><ac:adf-parameter key="enableddl"><ac:adf-parameter-value>true</ac:adf-parameter-value></ac:adf-parameter><ac:adf-parameter key="expandfirst"><ac:adf-parameter-value>true</ac:adf-parameter-value></ac:adf-parameter><ac:adf-parameter key="theme">light-spring</ac:adf-parameter><ac:adf-parameter key="lang">Apache</ac:adf-parameter></ac:adf-parameter></ac:adf-attribute>
   <ac:adf-attribute key="text">Advanced Codeblocks Multi</ac:adf-attribute>
   <ac:adf-attribute key="layout">default</ac:adf-attribute>
   <ac:adf-attribute key="local-id">2ba8fa32-cce8-4b12-bcf3-191e9bbf1469</ac:adf-attribute>
  </ac:adf-node>
 </ac:adf-fallback>
</ac:adf-extension>"""))



    def test_generate_ac_cloud_macro___valid_remote(self):
        self.maxDiff=None
        #
        # GIVEN
        #
        util = Util(False)
        cloud_extension_key_part = "9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f"
        cloud_adf_attribute_local_id = "4c1c3d01-f40c-44fc-97ad-ef662a4a4023"
        cloud_adf_parameter_local_id = "e67e9607-46aa-456c-b46c-24e06bd36f1f"
        builder = MacroStorageFormatBuilder(cloud_extension_key_part, False)
        macro_name = "advanced-remote-codeblock-macro"
        macro_param_lang = "bash"
        macro_param_enableddl = ""
        macro_param_globaltitle = "ACR_testfoo"
        macro_param_theme = "light-spring"
        macro_param_expand_first = "false"
        macro_param_remotefileurl = "https://codeclou.io/test-advanced-codeblock-macro/v2.3/public/testfile.foo"
        macro_param_remotefilehttpuser = ""
        macro_param_remotefilehttppassword = "" 
        macro_config = """[foobar]
moo=wuff
"""
        macro_code = ""
        #
        # WHEN
        #
        res = builder.generate_ac_cloud_macro(macro_name, cloud_adf_attribute_local_id, cloud_adf_parameter_local_id, macro_config, macro_code, macro_param_lang, macro_param_enableddl, macro_param_globaltitle, macro_param_theme, macro_param_expand_first, macro_param_remotefileurl, macro_param_remotefilehttppassword, macro_param_remotefilehttpuser)
        #
        # THEN
        #
        self.assertEqual(util.format_xml_for_final_output(res),  util.format_xml_for_final_output("""<ac:adf-extension>
  <ac:adf-node type="extension">
    <ac:adf-attribute key="extension-type">com.atlassian.ecosystem</ac:adf-attribute>
    <ac:adf-attribute key="extension-key">9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedremotecodeblockmacro</ac:adf-attribute>
    <ac:adf-attribute key="parameters">
      <ac:adf-parameter key="local-id">e67e9607-46aa-456c-b46c-24e06bd36f1f</ac:adf-parameter>
      <ac:adf-parameter key="extension-id">ari:cloud:ecosystem::extension/9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedremotecodeblockmacro</ac:adf-parameter>
      <ac:adf-parameter key="extension-title">Advanced Codeblocks Multi Remote</ac:adf-parameter>
      <ac:adf-parameter key="guest-params">
        <ac:adf-parameter key="globaltitle">ACR_testfoo</ac:adf-parameter>
        <ac:adf-parameter key="config"><![CDATA[[foobar]
moo=wuff
]]></ac:adf-parameter>
        <ac:adf-parameter key="expandfirst">
          <ac:adf-parameter-value />
        </ac:adf-parameter>
        <ac:adf-parameter key="remotefileurl">https://codeclou.io/test-advanced-codeblock-macro/v2.3/public/testfile.foo</ac:adf-parameter>
        <ac:adf-parameter key="remotefilehttpuser"/>
        <ac:adf-parameter key="remotefilehttppassword"/>
        <ac:adf-parameter key="theme">light-spring</ac:adf-parameter>
        <ac:adf-parameter key="lang">bash</ac:adf-parameter>
      </ac:adf-parameter>
    </ac:adf-attribute>
    <ac:adf-attribute key="text">Advanced Codeblocks Multi Remote</ac:adf-attribute>
    <ac:adf-attribute key="layout">default</ac:adf-attribute>
    <ac:adf-attribute key="local-id">4c1c3d01-f40c-44fc-97ad-ef662a4a4023</ac:adf-attribute>
  </ac:adf-node>
  <ac:adf-fallback>
    <ac:adf-node type="extension">
      <ac:adf-attribute key="extension-type">com.atlassian.ecosystem</ac:adf-attribute>
      <ac:adf-attribute key="extension-key">9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedremotecodeblockmacro</ac:adf-attribute>
      <ac:adf-attribute key="parameters">
        <ac:adf-parameter key="local-id">e67e9607-46aa-456c-b46c-24e06bd36f1f</ac:adf-parameter>
        <ac:adf-parameter key="extension-id">ari:cloud:ecosystem::extension/9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedremotecodeblockmacro</ac:adf-parameter>
        <ac:adf-parameter key="extension-title">Advanced Codeblocks Multi Remote</ac:adf-parameter>
        <ac:adf-parameter key="guest-params">
          <ac:adf-parameter key="globaltitle">ACR_testfoo</ac:adf-parameter>
          <ac:adf-parameter key="config"><![CDATA[[foobar]
moo=wuff
]]></ac:adf-parameter>
          <ac:adf-parameter key="expandfirst">
            <ac:adf-parameter-value />
          </ac:adf-parameter>
          <ac:adf-parameter key="remotefileurl">https://codeclou.io/test-advanced-codeblock-macro/v2.3/public/testfile.foo</ac:adf-parameter>
          <ac:adf-parameter key="remotefilehttpuser"/>
          <ac:adf-parameter key="remotefilehttppassword"/>
          <ac:adf-parameter key="theme">light-spring</ac:adf-parameter>
          <ac:adf-parameter key="lang">bash</ac:adf-parameter>
        </ac:adf-parameter>
      </ac:adf-attribute>
      <ac:adf-attribute key="text">Advanced Codeblocks Multi Remote</ac:adf-attribute>
      <ac:adf-attribute key="layout">default</ac:adf-attribute>
      <ac:adf-attribute key="local-id">4c1c3d01-f40c-44fc-97ad-ef662a4a4023</ac:adf-attribute>
    </ac:adf-node>
  </ac:adf-fallback>
</ac:adf-extension>"""))

if __name__ == '__main__':
    unittest.main()