import re
from typing import Final
from urllib import request

from lxml import etree


class LexicalAuto:
    def parse_code_page(self):
        pass


class Parser:
    __XPATH_TO_COMPILER_INFO: Final[str] = "//textarea[@id='wpTextbox1']"
    __RESOURCE_URL: Final[str] = "https://en.cppreference.com/mwiki/index.php?title=cpp/compiler_support&action=edit"

    def parse(self, url: str = __RESOURCE_URL):
        if htmlDoc := request.urlopen(url).read():

            if len(parseResult := etree.XPath(self.__XPATH_TO_COMPILER_INFO)(etree.HTML(htmlDoc.decode("UTF-8")))):
                compiler_information = parseResult[0].text.replace("\n", "")

                for textCompilerTable in re.split(r"""{{compiler support""", compiler_information)[1:]:
                    # todo add header table parser
                    for textCompilerRow in re.split(r"""compiler_support_row""", textCompilerTable)[1:]:

                        for paramNameValueRow in re.split(r"""\| """, textCompilerRow)[1:]:
                            [param_value, param_name] = re.split(r"""=""", paramNameValueRow)
                            print(param_name)
                            print(param_value)
