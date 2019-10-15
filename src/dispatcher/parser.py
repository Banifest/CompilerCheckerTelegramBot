import re
from typing import Final
from urllib import request

from lxml import etree


class Parser:
    __XPATH_TO_COMPILER_INFO: Final[str] = "//textarea[@id='wpTextbox1']"
    __RESOURCE_URL: Final[str] = "https://en.cppreference.com/mwiki/index.php?title=cpp/compiler_support&action=edit"

    def parse(self, url: str = __RESOURCE_URL):
        if htmlDoc := request.urlopen(url).read():

            if len(parseResult := etree.XPath(self.__XPATH_TO_COMPILER_INFO)(etree.HTML(htmlDoc.decode("UTF-8")))):
                compiler_information = parseResult[0].text

                test = re.search(r"""{{compiler support\|*""", compiler_information)

                print(test)
