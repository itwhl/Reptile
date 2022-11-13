"""
XPath语法
"""
from lxml import etree

content = """
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book>
        <title lang="en">Harry Potter</title>
        <price>29.99</price>
    </book>
    <book>
        <title lang="en">Learning XML</title>
        <price>39.95</price>
    </book>
    <book>
        <title lang="zh">聊斋志异</title>
        <author>蒲松龄</author>
        <price>42.5</price>
    </book>
</bookstore>
"""
tree = etree.HTML(content)
results = tree.xpath('//book[price>30]/title')
for result in results:
    print(type(result))
    print(result.text)
