<img src="https://user-images.githubusercontent.com/12599965/56864901-501d8b80-69c8-11e9-9e87-c7e687615a0a.png" align="right" />

# Advanced Codeblocks for Confluence

## :rocket: Cloud Migration Helper

This migration helper transforms a Server/DataCenter Confluence page in <a href="https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html">Storage Format</a> to
Cloud Confluence Storage Format. It will convert the <a href="https://marketplace.atlassian.com/apps/1211159/advanced-codeblocks-for-confluence?hosting=datacenter&tab=overview">Advanced Codeblocks for Confluence</a> macros to their Cloud forge app equivalent.

- :book: **[Read the complete migration guide here](https://codeclou.github.io/advanced-codeblocks-cloud-migration-helper)**

For example a Data Center Confluence page containing the Advanced Codeblocks Single Macro will look like this:

```
<p>some text</p>
<ac:structured-macro ac:name="advanced-single-codeblock-macro" ac:schema-version="1" ac:macro-id="0a76fb27-ee70-41a4-bead-063a0908804d">
  <ac:parameter ac:name="enableddl">true</ac:parameter>
  <ac:parameter ac:name="theme">light-mono</ac:parameter>
  <ac:parameter ac:name="lang">Bash</ac:parameter>
  <ac:parameter ac:name="globaltitle">test</ac:parameter>
  <ac:plain-text-body><![CDATA[echo "foo"]]></ac:plain-text-body>
</ac:structured-macro>
```

The Cloud App equivalent will look like this:

```
<p>some text</p>
<ac:adf-extension>
  <ac:adf-node type="extension">
    <ac:adf-attribute key="extension-type">com.atlassian.ecosystem</ac:adf-attribute>
    <ac:adf-attribute key="extension-key">9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedsinglecodeblockmacro</ac:adf-attribute>
    <ac:adf-attribute key="parameters">
      <ac:adf-parameter key="local-id">0658e817-aaf6-7e1d-8000-36a917095fd3</ac:adf-parameter>
      <ac:adf-parameter key="extension-id">ari:cloud:ecosystem::extension/9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f/static/advancedsinglecodeblockmacro</ac:adf-parameter>
      <ac:adf-parameter key="extension-title">Advanced Codeblocks Single</ac:adf-parameter>
      <ac:adf-parameter key="guest-params">
        <ac:adf-parameter key="globaltitle">test</ac:adf-parameter>
        <ac:adf-parameter key="code">echo "foo"</ac:adf-parameter>
        <ac:adf-parameter key="enableddl">
          <ac:adf-parameter-value>true</ac:adf-parameter-value>
        </ac:adf-parameter>
        <ac:adf-parameter key="theme">light-mono</ac:adf-parameter>
        <ac:adf-parameter key="lang">Bash</ac:adf-parameter>
      </ac:adf-parameter>
    </ac:adf-attribute>
    <ac:adf-attribute key="text">Advanced Codeblocks Single</ac:adf-attribute>
    <ac:adf-attribute key="layout">default</ac:adf-attribute>
    <ac:adf-attribute key="local-id">0658e817-aaf6-7d86-8000-4dd60f28b018</ac:adf-attribute>
  </ac:adf-node>
  <ac:adf-fallback>
    <!-- shortened ... -->
  </ac:adf-fallback>
</ac:adf-extension>
```

&nbsp;

---

&nbsp;

### Installation

```
git clone https://github.com/codeclou/advanced-codeblocks-cloud-migration-helper.git
cd advanced-codeblocks-cloud-migration-helper
pip3 install -r requirements.txt
```

&nbsp;

---

&nbsp;

### Disclaimer

**:bangbang: Please check the output storage file for errors before submitting it into your Confluence page. codeclou GmbH is not responsible for damages to your Confluence installation and/or content. Please test the output on a test instance first. This tool is provided as an example on how to transform your storage format from server to cloud. It might need further adaption to your specific needs.**

&nbsp;

---

&nbsp;

### Run transformer

The extension key must be extracted from the cloud page, see the documentation for details.

```
# single macro
python3 index.py -ek 9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f \
                 -if ./lib/input/ac-single-test1.input.storage \
                 -of ./lib/output/ac-single-test1.output.storage

# multi macro
python3 index.py -ek 9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f \
                 -if ./lib/input/ac-multi-test1.input.storage \
                 -of ./lib/output/ac-multi-test1.output.storage

# multi remote macro
python3 index.py -ek 9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f \
                 -if ./lib/input/ac-remote-test1.input.storage \
                 -of ./lib/output/ac-remote-test1.output.storage
```

Will produce an output like this:

```
======================================
 ADVANCED CODEBLOCKS MIGRATION HELPER
======================================

extension key part: 9a81c16f-31e6-4be7-be6e-dfc872fe4155/35d2082a-431b-46b7-90da-75a526882f2f

START > reading storage format file from: ./lib/input/ac-single-test1.input.storage

>> advanced-single-codeblock-macro
    macro param lang        : Bash
    macro param enableddl   : true
    macro param globaltitle : test
    macro param theme       : light-mono
    macro body (shortened)  : echo "foo"
    macro attr local id     : 0658e829-ab6b-7f11-8000-c612fa7cbd38
    macro param local id    : 0658e829-ab6b-7fa8-8000-1b5180ffb326

DONE > written transformed storage format to: ./lib/output/ac-single-test1.output.storage
```

The local ids will be auto generated using uuid v7. The classic server/DC macro-id is not used in Cloud and will be discarded.

&nbsp;

---

&nbsp;

### Run tests

you might need to add pytest to $PATH first, then:

```
pytest
```

---

&nbsp;

### License

[MIT](./LICENSE) © [codeclou GmbH](https://github.com/codeclou)


