import xml.etree.ElementTree as xml
books=[
    {'Title':"Pride and Prejustice",
     "Author":'Jane Austen',
     'Price':240,
     'Category':'Fiction'},
    {'Title':"The Diary of young girl",
     "Author":'Anne Frank',
     'Price':500,
     'Category':'Non-Fiction'},
    {'Title':"Five on a Treasure Island",
     "Author":'Enid Blyton0',
     'Price':250,
     'Category':'Fiction'}]

root=xml.Element("Books")
print(type(root))
for book in books:
    b_element=xml.Element('Book')
    root.append(b_element)
    b_element.set('Category',book['Category'])
    
    print(book)