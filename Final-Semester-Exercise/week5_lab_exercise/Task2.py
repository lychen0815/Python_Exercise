"""
Task 2: From the code above, we are obtaining the book id simply by getting the string from specific index range(line[-7:-2]). However, this method is not flexible at all. For the book below, we can see that the book id is not located between indices -7(inclusive) and -2(exclusive). Can you write a function that can help us retrieving the book id(or even other attributes, e.g. class, within the xml tag) correctly?

<book id="bk105" class="normal">
    <author>Corets, Eva</author>
    <title>The Sundered Grail</title>
    <genre>Fantasy</genre>
    <price>5.95</price>
    <publish_date>2001-09-10</publish_date>
    <description>The two daughters of Maeve, half-sisters, battle one another for control of England. Sequel to Oberon's Legacy.</description>
</book>
"""


def get_attr(line, attr_name) -> str or bool:
    tag_content = line.split(">")[0]

    tag_attribute = tag_content.split()

    for att in tag_attribute:
        key_values = att.split('=')
        print(key_values)
        if len(key_values) != 2:
            continue
        if key_values[0] == attr_name:
            value = key_values[1]
            value = value[1:-1]
            return value
    return False
test_string = '<book id="bk105" class="normal">This is a book</book>'
#print(f"get_attr(test_string, 'id') : {repr(get_attr(test_string, 'id'))}")
#print(f"get_attr(test_string, 'class') : {repr(get_attr(test_string, 'class'))}")
print(f"get_attr(test_string, 'random') : {repr(get_attr(test_string, 'random'))}")