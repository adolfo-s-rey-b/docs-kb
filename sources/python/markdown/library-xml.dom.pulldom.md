### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.sax.html "xml.sax — Support for SAX2 parsers")
     |
*   [previous](https://docs.python.org/3/library/xml.dom.minidom.html "xml.dom.minidom — Minimal DOM implementation")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html)
     »
*   [`xml.dom.pulldom` — Support for building partial DOM trees](https://docs.python.org/3/library/xml.dom.pulldom.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`xml.dom.pulldom` — Support for building partial DOM trees[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#module-xml.dom.pulldom "Link to this heading")

====================================================================================================================================================================

**Source code:** [Lib/xml/dom/pulldom.py](https://github.com/python/cpython/tree/3.15/Lib/xml/dom/pulldom.py)

* * *

The `xml.dom.pulldom` module provides a “pull parser” which can also be asked to produce DOM-accessible fragments of the document where necessary. The basic concept involves pulling “events” from a stream of incoming XML and processing them. In contrast to SAX which also employs an event-driven processing model together with callbacks, the user of a pull parser is responsible for explicitly pulling events from the stream, looping over those events until either processing is finished or an error condition occurs.

Note

If you need to parse untrusted or unauthenticated data, see [XML security](https://docs.python.org/3/library/xml.html#xml-security)
.

Changed in version 3.7.1: The SAX parser no longer processes general external entities by default to increase security by default. To enable processing of external entities, pass a custom parser instance in:

Copy

from xml.dom.pulldom import parse
from xml.sax import make\_parser
from xml.sax.handler import feature\_external\_ges

parser \= make\_parser()
parser.setFeature(feature\_external\_ges, True)
parse(filename, parser\=parser)

Example:

Copy

from xml.dom import pulldom

doc \= pulldom.parse('sales\_items.xml')
for event, node in doc:
    if event \== pulldom.START\_ELEMENT and node.tagName \== 'item':
        if int(node.getAttribute('price')) \> 50:
            doc.expandNode(node)
            print(node.toxml())

`event` is one of the following constants, and `node` is the node which the event is about. The nodes implement the [`xml.dom`](https://docs.python.org/3/library/xml.dom.html#module-xml.dom "xml.dom: Document Object Model API for Python.")
 interfaces; they are created by the DOM implementation given to [`PullDOM`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.PullDOM "xml.dom.pulldom.PullDOM")
, which is [`xml.dom.minidom`](https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom "xml.dom.minidom: Minimal Document Object Model (DOM) implementation.")
 by default.

xml.dom.pulldom.START\_DOCUMENT[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.START_DOCUMENT "Link to this definition")

xml.dom.pulldom.END\_DOCUMENT[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.END_DOCUMENT "Link to this definition")

The start and the end of the document. _node_ is the [`Document`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document "xml.dom.Document")
.

xml.dom.pulldom.START\_ELEMENT[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.START_ELEMENT "Link to this definition")

xml.dom.pulldom.END\_ELEMENT[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.END_ELEMENT "Link to this definition")

The start tag and the end tag of an element. _node_ is the [`Element`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element "xml.dom.Element")
.

xml.dom.pulldom.CHARACTERS[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.CHARACTERS "Link to this definition")

Character data. _node_ is the [`Text`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Text "xml.dom.Text")
 node.

xml.dom.pulldom.IGNORABLE\_WHITESPACE[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.IGNORABLE_WHITESPACE "Link to this definition")

White space in element content, as declared in the DTD. _node_ is the [`Text`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Text "xml.dom.Text")
 node.

xml.dom.pulldom.COMMENT[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.COMMENT "Link to this definition")

A comment. _node_ is the [`Comment`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Comment "xml.dom.Comment")
 node.

xml.dom.pulldom.PROCESSING\_INSTRUCTION[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.PROCESSING_INSTRUCTION "Link to this definition")

A processing instruction. _node_ is the [`ProcessingInstruction`](https://docs.python.org/3/library/xml.dom.html#xml.dom.ProcessingInstruction "xml.dom.ProcessingInstruction")
 node.

Since the document is treated as a “flat” stream of events, the document “tree” is implicitly traversed and the desired elements are found regardless of their depth in the tree. In other words, one does not need to consider hierarchical issues such as recursive searching of the document nodes, although if the context of elements were important, one would either need to maintain some context-related state (i.e. remembering where one is in the document at any given point) or to make use of the [`DOMEventStream.expandNode()`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream.expandNode "xml.dom.pulldom.DOMEventStream.expandNode")
 method and switch to DOM-related processing.

class xml.dom.pulldom.PullDOM(_documentFactory\=None_)[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.PullDOM "Link to this definition")

Subclass of [`xml.sax.handler.ContentHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler")
 which turns SAX events into the events of the pull parser. The nodes are created, but they are not added to the tree, unless [`expandNode()`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream.expandNode "xml.dom.pulldom.DOMEventStream.expandNode")
 is called. _documentFactory_, if given, is a DOM implementation used to create the document; by default the implementation of [`xml.dom.minidom`](https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom "xml.dom.minidom: Minimal Document Object Model (DOM) implementation.")
 is used.

class xml.dom.pulldom.SAX2DOM(_documentFactory\=None_)[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.SAX2DOM "Link to this definition")

Subclass of [`PullDOM`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.PullDOM "xml.dom.pulldom.PullDOM")
 which also adds every created node to the tree, so that the complete document is built.

xml.dom.pulldom.parse(_stream\_or\_string_, _parser\=None_, _bufsize\=None_)[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.parse "Link to this definition")

Return a [`DOMEventStream`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream "xml.dom.pulldom.DOMEventStream")
 from the given input. _stream\_or\_string_ may be either a file name, or a file-like object. _parser_, if given, must be an [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader")
 object. This function will change the document handler of the parser and activate namespace support; other parser configuration (like setting an entity resolver) must have been done in advance.

If you have XML in a string, you can use the [`parseString()`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.parseString "xml.dom.pulldom.parseString")
 function instead:

xml.dom.pulldom.parseString(_string_, _parser\=None_)[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.parseString "Link to this definition")

Return a [`DOMEventStream`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream "xml.dom.pulldom.DOMEventStream")
 that represents the _string_. _string_ must be a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 instance; to parse bytes, pass a binary file object to [`parse()`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.parse "xml.dom.pulldom.parse")
.

xml.dom.pulldom.default\_bufsize[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.default_bufsize "Link to this definition")

Default value for the _bufsize_ parameter to [`parse()`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.parse "xml.dom.pulldom.parse")
.

The value of this variable can be changed before calling [`parse()`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.parse "xml.dom.pulldom.parse")
 and the new value will take effect.

DOMEventStream Objects[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#domeventstream-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

class xml.dom.pulldom.DOMEventStream(_stream_, _parser_, _bufsize_)[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream "Link to this definition")

Produce the events for the data read from the file object _stream_ by the [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader")
 _parser_. The data is read by _bufsize_ bytes, or characters for a text stream, at a time.

Changed in version 3.11: Support for [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 method has been removed.

getEvent()[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream.getEvent "Link to this definition")

Return the next `(event, node)` tuple, or `None` at the end of the document. See above for the events and the corresponding nodes. The current node does not contain information about its children, unless [`expandNode()`](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream.expandNode "xml.dom.pulldom.DOMEventStream.expandNode")
 is called.

expandNode(_node_)[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream.expandNode "Link to this definition")

Expands all children of _node_ into _node_. Example:

Copy

from xml.dom import pulldom

xml \= '<html><title>Foo</title> <p>Some text <div>and more</div></p> </html>'
doc \= pulldom.parseString(xml)
for event, node in doc:
    if event \== pulldom.START\_ELEMENT and node.tagName \== 'p':
        \# Following statement only prints '<p/>'
        print(node.toxml())
        doc.expandNode(node)
        \# Following statement prints node with all its children '<p>Some text <div>and more</div></p>'
        print(node.toxml())

reset()[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream.reset "Link to this definition")

Discard the events which are not read yet and prepare the object for parsing a new document.

clear()[¶](https://docs.python.org/3/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream.clear "Link to this definition")

Release the parser and the document. The stream is not closed, and the object can no longer be used.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`xml.dom.pulldom` — Support for building partial DOM trees](https://docs.python.org/3/library/xml.dom.pulldom.html#)
    *   [DOMEventStream Objects](https://docs.python.org/3/library/xml.dom.pulldom.html#domeventstream-objects)
        

#### Previous topic

[`xml.dom.minidom` — Minimal DOM implementation](https://docs.python.org/3/library/xml.dom.minidom.html "previous chapter")

#### Next topic

[`xml.sax` — Support for SAX2 parsers](https://docs.python.org/3/library/xml.sax.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.dom.pulldom+%E2%80%94+Support+for+building+partial+DOM+trees&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.dom.pulldom.html&pagesource=library%2Fxml.dom.pulldom.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/xml.dom.pulldom.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.sax.html "xml.sax — Support for SAX2 parsers")
     |
*   [previous](https://docs.python.org/3/library/xml.dom.minidom.html "xml.dom.minidom — Minimal DOM implementation")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html)
     »
*   [`xml.dom.pulldom` — Support for building partial DOM trees](https://docs.python.org/3/library/xml.dom.pulldom.html)
    
*    
    
    |
*   Theme Auto Light Dark |