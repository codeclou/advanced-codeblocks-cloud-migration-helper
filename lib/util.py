# Licensed under the MIT license: https://github.com/codeclou/advanced-codeblocks-cloud-migration-helper/blob/main/LICENSE

from bs4 import BeautifulSoup
from uuid_extensions import uuid7str
import lxml.etree as etree

class Util:
    def __init__(self, forceUUIDsZeroed: bool):
        self.forceUUIDsZeroed = forceUUIDsZeroed
        self.zeroUUID = "00000000-0000-0000-0000-000000000000"
        self.shortLength = 60

    def shorten_string_for_print(self, input: str) -> str:
        return (input[:self.shortLength] + '...') if len(input) > self.shortLength else input

    def bool_to_string_for_print(self, input: bool) -> str:
        return f'{input}'.lower()

    def get_xml_parser(self, xml_string: str):
        return BeautifulSoup(xml_string, 'html.parser', preserve_whitespace_tags=["p","ac:parameter", "ac:adf-attribute", "ac:adf-parameter-value"])
    
    def generate_uuid(self):
        if (self.forceUUIDsZeroed == True):
            return self.zeroUUID
        else:
            return uuid7str()
    
    # WARN: Do not use this method on the final page, since it is no real XML but XHTML sort of ...
    # Only use this to format the macro itself to compare in unit tests
    def format_xml_for_final_output(self, xml_string: str) -> str:
        # only lxml can work around the missing namespace <ac:... errors with recover=True
        parser = etree.XMLParser(recover=True, remove_blank_text=True, strip_cdata=False)
        res = etree.fromstring(str(xml_string), parser)
        # we need to decode byte string to string
        return etree.tostring(res, pretty_print=True, encoding='UTF-8').decode("utf-8")
    

    def replace_server_macro_lang_with_cloud_pendant(self, lang_server: str) -> str:
        replacement_dict = {"1C": "1c","ABNF": "abnf","Access logs": "accesslog","Ada": "ada","ARM Assembly": "armasm","AVR Assembler": "avrasm","ActionScript": "actionscript","Apache": "apache","AppleScript": "applescript","AsciiDoc": "asciidoc","AspectJ": "aspectj","AutoHotkey": "autohotkey","AutoIt": "autoit","Awk": "awk","Axapta": "axapta","Bash": "bash","Basic": "basic","BNF": "bnf","Brainfuck": "brainf*ck","Brainf*ck": "brainf*ck","C#": "cs","C++": "cpp","C/AL": "cal","Cache Object Script": "cos","CMake": "cmake","Coq": "coq","CSP": "csp","CSS": "css","Cap’n Proto": "capnproto","Ceylon": "ceylon","Clojure": "clojure","Clojure REPL": "clojure-repl","CoffeeScript": "coffeescript","Crmsh": "crmsh","Crystal": "crystal","D": "d","DNS Zone file": "dns","DOS .bat": "dos","Dart": "dart","Delphi": "delphi","Diff": "diff","Django": "django","Dockerfile": "dockerfile","dsconfig": "dsconfig","DTS (Device Tree)": "dts","Dust": "dust","EBNF": "ebnf","Elixir": "elixir","Elm": "elm","ERB (Embedded Ruby)": "erb","Erlang": "erlang","Erlang REPL": "erlang-repl","Excel": "excel","F#": "fsharp","FIX": "fix","Fortran": "fortran","G-code (ISO 6983)": "gcode","Gams": "gams","GAUSS": "gauss","Gherkin": "gherkin","Go": "go","Golo": "golo","GLSL": "glsl","Gradle": "gradle","Groovy": "groovy","HTML, XML": "html","HTTP": "http","Haml": "haml","Handlebars": "handlebars","Haskell": "haskell","Haxe": "haxe","Hy": "hy","Ini": "ini","Inform 7": "inform7","Intel x86 Assembly": "x86asm","IRPF90": "irpf90","Java": "java","JavaScript": "javascript","JSON": "json","Julia": "julia","Kotlin": "kotlin","Lasso": "lasso","LDIF": "ldif","Leaf": "leaf","Less": "less","Lisp": "lisp","LiveCode": "livecodeserver","LiveScript": "livescript","Lua": "lua","Makefile": "makefile","Markdown": "markdown","Mathematica": "mathematica","Matlab": "matlab","Maxima": "maxima","MEL": "mel","Mercury": "mercury","Mizar": "mizar","Mojolicious": "mojolicious","Monkey": "monkey","Moonscript": "moonscript","N1QL": "n1ql","NSIS": "nsis","Nginx": "nginx","Nimrod": "nimrod","Nix": "nix","Objective C": "objectivec","OCaml": "ocaml","OpenGL Shading Language": "glsl","OpenSCAD": "openscad","Oracle Rules Language": "ruleslanguage","Oxygene": "oxygene","Parser3": "parser3","Perl": "perl","pf": "pf","PHP": "php","Pony": "pony","PowerShell": "powershell","Processing": "processing","Prolog": "prolog","Protocol Buffers": "protobuf","Puppet": "puppet","Python": "python","Python profile": "profile","Q": "k","QML": "qml","R": "r","RenderMan RIB": "rib","RenderMan RSL": "rsl","Roboconf": "graph","Ruby": "ruby","Rust": "rust","Scala": "scala","Scheme": "scheme","Scilab": "scilab","SCSS": "scss","Shell": "shell","Smali": "smali","Smalltalk": "smalltalk","SML": "sml","SQL": "sql","Stan": "stan","Stata": "stata","STEP Part 21 (ISO 10303-21)": "p21","Stylus": "stylus","SubUnit": "subunit","Swift": "swift","Tcl": "tcl","Test Anything Protocol": "tap","TeX": "tex","Thrift": "thrift","TP": "tp","Twig": "twig","TypeScript": "typescript","Vala": "vala","VB.NET": "vbnet","VBScript": "vbscript","VBScript in HTML": "vbscript-html","Verilog": "verilog","VHDL": "vhdl","Vim Script": "vim","XL": "xl","XML": "xml","XQuery": "xpath","Zephir": "zephir","bsh": "bash","c": "cpp","cc": "cpp","cpp": "cpp","cs": "cs","csh": "bash","cyc": "","cv": "","htm": "xml","html": "xml","java": "java","js": "javascript","m": "","mxml": "","perl": "perl","pl": "perl","pm": "perl","py": "python","rb": "ruby","sh": "bash","xhtml": "xml","xml": "xml","xsl": "xml"}
        if (lang_server in replacement_dict):
            return replacement_dict[lang_server]
        else:
            return ""