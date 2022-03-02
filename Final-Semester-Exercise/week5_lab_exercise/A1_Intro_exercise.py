"""
You need read "dummy_xml" and output this format:
[{'id': 'bk101', 'author': 'Gambardella Matthew', 'title': 'XML Developers Guid'},
{'id': 'bk102', 'author': 'Ralls Kim', 'title': 'Midnight Rain'},
{'id': 'bk103', 'author': 'Corets Ev', 'title': 'Maeve Ascendan'},
{'id': 'bk104', 'author': 'Corets Ev', 'title': 'Oberons Legacy'}]
"""
with open("dummy_xml") as xml:
    read_xml = xml.read()
    xml_books = [i for i in read_xml.split('</book>') if i]
    books = []
    for xml_book in xml_books:
        book = {}
        lines = xml_book.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith('<book'):
                book['id'] = line[-7:-2]
            if 'id' in book and line.startswith('<author>'):
                author = line.strip('<author>').strip('</author>')
                author_clean = ''
                for char in author:
                    if char.isalpha() or char == ' ':
                        author_clean += char
            if 'id' in book and line.startswith('<title>'):
                title = line.strip('<title>').strip('</title>')
                title_clean = ''
                for char in title:
                    if char.isalpha() or char == ' ':
                        title_clean += char
                book['title'] = title_clean
        books.append(book)
    print("[" + ",\n".join(str(book) for book in books) + ']')