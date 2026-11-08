### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.dom.pulldom.html "xml.dom.pulldom — Support for building partial DOM trees")
     |
*   [previous](https://docs.python.org/3/library/xml.dom.html "xml.dom — The Document Object Model API")
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
*   [`xml.dom.minidom` — Minimal DOM implementation](https://docs.python.org/3/library/xml.dom.minidom.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`xml.dom.minidom` — Minimal DOM implementation[¶](https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom "Link to this heading")

========================================================================================================================================================

**Source code:** [Lib/xml/dom/minidom.py](https://github.com/python/cpython/tree/3.15/Lib/xml/dom/minidom.py)

* * *

`xml.dom.minidom` is a minimal implementation of the Document Object Model interface, with an API similar to that in other languages. It is intended to be simpler than the full DOM and also significantly smaller. Users who are not already proficient with the DOM should consider using the [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
 module for their XML processing instead.

Note

If you need to parse untrusted or unauthenticated data, see [XML security](https://docs.python.org/3/library/xml.html#xml-security)
.

DOM applications typically start by parsing some XML into a DOM. With `xml.dom.minidom`, this is done through the parse functions:

Copy

from xml.dom.minidom import parse, parseString

dom1 \= parse('c:\\\\temp\\\\mydata.xml')  \# parse an XML file by name

datasource \= open('c:\\\\temp\\\\mydata.xml')
dom2 \= parse(datasource)  \# parse an open file

dom3 \= parseString('<myxml>Some data<empty/> some more data</myxml>')

The [`parse()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.parse "xml.dom.minidom.parse")
 function can take either a filename or an open file object.

xml.dom.minidom.parse(_filename\_or\_file_, _parser\=None_, _bufsize\=None_)[¶](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.parse "Link to this definition")

Return a `Document` from the given input. _filename\_or\_file_ may be either a file name, or a file-like object. _parser_, if given, must be a SAX2 parser object. This function will change the document handler of the parser and activate namespace support; other parser configuration (like setting an entity resolver) must have been done in advance.

If you have XML in a string, you can use the [`parseString()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.parseString "xml.dom.minidom.parseString")
 function instead:

xml.dom.minidom.parseString(_string_, _parser\=None_)[¶](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.parseString "Link to this definition")

Return a `Document` that represents the _string_. This method creates an [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
 object for the string and passes that on to [`parse()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.parse "xml.dom.minidom.parse")
.

Both functions return a `Document` object representing the content of the document.

What the [`parse()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.parse "xml.dom.minidom.parse")
 and [`parseString()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.parseString "xml.dom.minidom.parseString")
 functions do is connect an XML parser with a “DOM builder” that can accept parse events from any SAX parser and convert them into a DOM tree. The names of the functions are perhaps misleading, but are easy to grasp when learning the interfaces. The parsing of the document will be completed before these functions return; it’s simply that these functions do not provide a parser implementation themselves.

You can also create a `Document` by calling a method on a “DOM Implementation” object. You can get this object either by calling the `getDOMImplementation()` function in the [`xml.dom`](https://docs.python.org/3/library/xml.dom.html#module-xml.dom "xml.dom: Document Object Model API for Python.")
 package or the `xml.dom.minidom` module. Once you have a `Document`, you can add child nodes to it to populate the DOM:

Copy

from xml.dom.minidom import getDOMImplementation

impl \= getDOMImplementation()

newdoc \= impl.createDocument(None, "some\_tag", None)
top\_element \= newdoc.documentElement
text \= newdoc.createTextNode('Some textual content.')
top\_element.appendChild(text)

Once you have a DOM document object, you can access the parts of your XML document through its properties and methods. These properties are defined in the DOM specification. The main property of the document object is the `documentElement` property. It gives you the main element in the XML document: the one that holds all others. Here is an example program:

Copy

dom3 \= parseString("<myxml>Some data</myxml>")
assert dom3.documentElement.tagName \== "myxml"

When you are finished with a DOM tree, you may optionally call the `unlink()` method to encourage early cleanup of the now-unneeded objects. `unlink()` is an `xml.dom.minidom`\-specific extension to the DOM API that renders the node and its descendants essentially useless. Otherwise, Python’s garbage collector will eventually take care of the objects in the tree.

See also

[Document Object Model (DOM) Level 1 Specification](https://www.w3.org/TR/REC-DOM-Level-1/)

The W3C recommendation for the DOM supported by `xml.dom.minidom`.

DOM Objects[¶](https://docs.python.org/3/library/xml.dom.minidom.html#dom-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------

The definition of the DOM API for Python is given as part of the [`xml.dom`](https://docs.python.org/3/library/xml.dom.html#module-xml.dom "xml.dom: Document Object Model API for Python.")
 module documentation. This section lists the differences between the API and `xml.dom.minidom`.

Node.unlink()[¶](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.unlink "Link to this definition")

Break internal references within the DOM so that it will be garbage collected on versions of Python without cyclic GC. Even when cyclic GC is available, using this can make large amounts of memory available sooner, so calling this on DOM objects as soon as they are no longer needed is good practice. This only needs to be called on the `Document` object, but may be called on child nodes to discard children of that node.

You can avoid calling this method explicitly by using the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement. The following code will automatically unlink _dom_ when the `with` block is exited:

Copy

with xml.dom.minidom.parse(datasource) as dom:
    ... \# Work with dom.

Node.writexml(_writer_, _indent\=''_, _addindent\=''_, _newl\=''_, _encoding\=None_, _standalone\=None_)[¶](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.writexml "Link to this definition")

Write XML to the writer object. The writer receives texts but not bytes as input, it should have a `write()` method which matches that of the file object interface. The _indent_ parameter is the indentation of the current node. The _addindent_ parameter is the incremental indentation to use for subnodes of the current one. The _newl_ parameter specifies the string to use to terminate newlines.

For the `Document` node, an additional keyword argument _encoding_ can be used to specify the encoding field of the XML header.

Similarly, explicitly stating the _standalone_ argument causes the standalone document declarations to be added to the prologue of the XML document. If the value is set to `True`, `standalone="yes"` is added, otherwise it is set to `"no"`. Not stating the argument will omit the declaration from the document.

Changed in version 3.8: The `writexml()` method now preserves the attribute order specified by the user.

Changed in version 3.9: The _standalone_ parameter was added.

Node.toxml(_encoding\=None_, _standalone\=None_)[¶](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.toxml "Link to this definition")

Return a string or byte string containing the XML represented by the DOM node.

With an explicit _encoding_ [\[1\]](https://docs.python.org/3/library/xml.dom.minidom.html#id3)
 argument, the result is a byte string in the specified encoding. With no _encoding_ argument, the result is a Unicode string, and the XML declaration in the resulting string does not specify an encoding. Encoding this string in an encoding other than UTF-8 is likely incorrect, since UTF-8 is the default encoding of XML.

The _standalone_ argument behaves exactly as in [`writexml()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.writexml "xml.dom.minidom.Node.writexml")
.

Changed in version 3.8: The `toxml()` method now preserves the attribute order specified by the user.

Changed in version 3.9: The _standalone_ parameter was added.

Node.toprettyxml(_indent\='\\t'_, _newl\='\\n'_, _encoding\=None_, _standalone\=None_)[¶](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.toprettyxml "Link to this definition")

Return a pretty-printed version of the document. _indent_ specifies the indentation string and defaults to a tabulator; _newl_ specifies the string emitted at the end of each line and defaults to `\n`.

The _encoding_ argument behaves like the corresponding argument of [`toxml()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.toxml "xml.dom.minidom.Node.toxml")
.

The _standalone_ argument behaves exactly as in [`writexml()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.writexml "xml.dom.minidom.Node.writexml")
.

Changed in version 3.8: The `toprettyxml()` method now preserves the attribute order specified by the user.

Changed in version 3.9: The _standalone_ parameter was added.

DOM Example[¶](https://docs.python.org/3/library/xml.dom.minidom.html#dom-example "Link to this heading")

----------------------------------------------------------------------------------------------------------

This example program is a fairly realistic example of a simple program. In this particular case, we do not take much advantage of the flexibility of the DOM.

Copy

import xml.dom.minidom

document \= """\\
<slideshow>
<title>Demo slideshow</title>
<slide><title>Slide title</title>
<point>This is a demo</point>
<point>Of a program for processing slides</point>
</slide>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>
</slideshow>
"""

dom \= xml.dom.minidom.parseString(document)

def getText(nodelist):
    rc \= \[\]
    for node in nodelist:
        if node.nodeType \== node.TEXT\_NODE:
            rc.append(node.data)
    return ''.join(rc)

def handleSlideshow(slideshow):
    print("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")\[0\])
    slides \= slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print("</html>")

def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)

def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")\[0\])
    handlePoints(slide.getElementsByTagName("point"))

def handleSlideshowTitle(title):
    print(f"<title>{getText(title.childNodes)}</title>")

def handleSlideTitle(title):
    print(f"<h2>{getText(title.childNodes)}</h2>")

def handlePoints(points):
    print("<ul>")
    for point in points:
        handlePoint(point)
    print("</ul>")

def handlePoint(point):
    print(f"<li>{getText(point.childNodes)}</li>")

def handleToc(slides):
    for slide in slides:
        title \= slide.getElementsByTagName("title")\[0\]
        print(f"<p>{getText(title.childNodes)}</p>")

handleSlideshow(dom)

minidom and the DOM standard[¶](https://docs.python.org/3/library/xml.dom.minidom.html#minidom-and-the-dom-standard "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

The `xml.dom.minidom` module is essentially a DOM 1.0-compatible DOM with some DOM 2 features (primarily namespace features).

Usage of the DOM interface in Python is straight-forward. The following mapping rules apply:

*   Interfaces are accessed through instance objects. Applications should not instantiate the classes themselves; they should use the creator functions available on the `Document` object. Derived interfaces support all operations (and attributes) from the base interfaces, plus any new operations.
    
*   Operations are used as methods. Since the DOM uses only [`in`](https://docs.python.org/3/reference/expressions.html#in)
     parameters, the arguments are passed in normal order (from left to right). There are no optional arguments. `void` operations return `None`.
    
*   IDL attributes map to instance attributes. For compatibility with the OMG IDL language mapping for Python, an attribute `foo` can also be accessed through accessor methods `_get_foo()` and `_set_foo()`. `readonly` attributes must not be changed; this is not enforced at runtime.
    
*   The types `short int`, `unsigned int`, `unsigned long long`, and `boolean` all map to Python integer objects.
    
*   The type `DOMString` maps to Python strings. `xml.dom.minidom` supports either bytes or strings, but will normally produce strings. Values of type `DOMString` may also be `None` where allowed to have the IDL `null` value by the DOM specification from the W3C.
    
*   `const` declarations map to variables in their respective scope (e.g. `xml.dom.minidom.Node.PROCESSING_INSTRUCTION_NODE`); they must not be changed.
    
*   `DOMException` is currently not supported in `xml.dom.minidom`. Instead, `xml.dom.minidom` uses standard Python exceptions such as [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     and [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
    .
    
*   Each of the [`NodeList`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NodeList "xml.dom.NodeList")
     and [`NamedNodeMap`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NamedNodeMap "xml.dom.NamedNodeMap")
     interfaces has two implementations, which provide additional methods and operations.
    
    [`childNodes`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.childNodes "xml.dom.Node.childNodes")
     is a subclass of [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
    , or, for nodes which cannot have children, a subclass of [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
    . It supports iteration, concatenation, indexing and slicing.
    
    [`attributes`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.attributes "xml.dom.Node.attributes")
     supports `len()`, the [`in`](https://docs.python.org/3/reference/expressions.html#in)
     operator, subscription by a name or by a `(namespaceURI, localName)` tuple, assignment and deletion, and the methods `get()`, `keys()`, `keysNS()`, `values()`, `items()` and `itemsNS()`. [`entities`](https://docs.python.org/3/library/xml.dom.html#xml.dom.DocumentType.entities "xml.dom.DocumentType.entities")
     and [`notations`](https://docs.python.org/3/library/xml.dom.html#xml.dom.DocumentType.notations "xml.dom.DocumentType.notations")
     are read-only and support only `len()` and subscription by a name.
    
*   [`strictErrorChecking`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.strictErrorChecking "xml.dom.Document.strictErrorChecking")
     and [`specified`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Attr.specified "xml.dom.Attr.specified")
     are always `False`.
    
*   [`removeAttribute()`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.removeAttribute "xml.dom.Element.removeAttribute")
     and [`removeAttributeNS()`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.removeAttributeNS "xml.dom.Element.removeAttributeNS")
     raise [`NotFoundErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NotFoundErr "xml.dom.NotFoundErr")
     if there is no matching attribute, while the DOM specifies that this has no effect.
    

The following interfaces have no implementation in `xml.dom.minidom`:

*   `DOMTimeStamp`
    
*   `EntityReference`
    

Most of these reflect information in the XML document that is not of general utility to most DOM users.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`xml.dom.minidom` — Minimal DOM implementation](https://docs.python.org/3/library/xml.dom.minidom.html#)
    *   [DOM Objects](https://docs.python.org/3/library/xml.dom.minidom.html#dom-objects)
        
    *   [DOM Example](https://docs.python.org/3/library/xml.dom.minidom.html#dom-example)
        
    *   [minidom and the DOM standard](https://docs.python.org/3/library/xml.dom.minidom.html#minidom-and-the-dom-standard)
        

#### Previous topic

[`xml.dom` — The Document Object Model API](https://docs.python.org/3/library/xml.dom.html "previous chapter")

#### Next topic

[`xml.dom.pulldom` — Support for building partial DOM trees](https://docs.python.org/3/library/xml.dom.pulldom.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.dom.minidom+%E2%80%94+Minimal+DOM+implementation&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.dom.minidom.html&pagesource=library%2Fxml.dom.minidom.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/xml.dom.minidom.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.dom.pulldom.html "xml.dom.pulldom — Support for building partial DOM trees")
     |
*   [previous](https://docs.python.org/3/library/xml.dom.html "xml.dom — The Document Object Model API")
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
*   [`xml.dom.minidom` — Minimal DOM implementation](https://docs.python.org/3/library/xml.dom.minidom.html)
    
*    
    
    |
*   Theme Auto Light Dark |