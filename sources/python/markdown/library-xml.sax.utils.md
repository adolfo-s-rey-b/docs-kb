### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers")
     |
*   [previous](https://docs.python.org/3/library/xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers")
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
*   [`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/3/library/xml.sax.utils.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`xml.sax.saxutils` — SAX Utilities[¶](https://docs.python.org/3/library/xml.sax.utils.html#module-xml.sax.saxutils "Link to this heading")

===========================================================================================================================================

**Source code:** [Lib/xml/sax/saxutils.py](https://github.com/python/cpython/tree/3.15/Lib/xml/sax/saxutils.py)

* * *

The module `xml.sax.saxutils` contains a number of classes and functions that are commonly useful when creating SAX applications, either in direct use, or as base classes.

xml.sax.saxutils.escape(_data_, _entities\={}_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.escape "Link to this definition")

Escape `'&'`, `'<'`, and `'>'` in a string of data.

You can escape other strings of data by passing a dictionary as the optional _entities_ parameter. The keys and values must all be strings; each key will be replaced with its corresponding value. The characters `'&'`, `'<'` and `'>'` are always escaped, even if _entities_ is provided.

Note

This function should only be used to escape characters that can’t be used directly in XML. Do not use this function as a general string translation function.

xml.sax.saxutils.unescape(_data_, _entities\={}_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.unescape "Link to this definition")

Unescape `'&amp;'`, `'&lt;'`, and `'&gt;'` in a string of data.

You can unescape other strings of data by passing a dictionary as the optional _entities_ parameter. The keys and values must all be strings; each key will be replaced with its corresponding value. `'&amp;'`, `'&lt;'`, and `'&gt;'` are always unescaped, even if _entities_ is provided.

xml.sax.saxutils.quoteattr(_data_, _entities\={}_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.quoteattr "Link to this definition")

Similar to [`escape()`](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.escape "xml.sax.saxutils.escape")
, but also prepares _data_ to be used as an attribute value. The return value is a quoted version of _data_ with any additional required replacements. `quoteattr()` will select a quote character based on the content of _data_, attempting to avoid encoding any quote characters in the string. If both single- and double-quote characters are already in _data_, the double-quote characters will be encoded and _data_ will be wrapped in double-quotes. The resulting string can be used directly as an attribute value:

Copy

\>>> print("<element attr=%s\>" % quoteattr("ab ' cd \\" ef"))
<element attr="ab ' cd &quot; ef">

This function is useful when generating attribute values for HTML or any SGML using the reference concrete syntax.

class xml.sax.saxutils.XMLGenerator(_out\=None_, _encoding\='iso-8859-1'_, _short\_empty\_elements\=False_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.XMLGenerator "Link to this definition")

This class implements the [`ContentHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler")
 interface by writing SAX events back into an XML document. In other words, using an `XMLGenerator` as the content handler will reproduce the original document being parsed. _out_ should be a file-like object which will default to _sys.stdout_. _encoding_ is the encoding of the output stream which defaults to `'iso-8859-1'`. _short\_empty\_elements_ controls the formatting of elements that contain no content: if `False` (the default) they are emitted as a pair of start/end tags, if set to `True` they are emitted as a single self-closed tag.

Changed in version 3.2: Added the _short\_empty\_elements_ parameter.

class xml.sax.saxutils.XMLFilterBase(_base_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.XMLFilterBase "Link to this definition")

This class is designed to sit between an [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader")
 and the client application’s event handlers. By default, it does nothing but pass requests up to the reader and events on to the handlers unmodified, but subclasses can override specific methods to modify the event stream or the configuration requests as they pass through.

getParent()[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.XMLFilterBase.getParent "Link to this definition")

Return the parent reader, or `None` if it is not set.

setParent(_parent_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.XMLFilterBase.setParent "Link to this definition")

Set the parent reader, which the events are read from.

xml.sax.saxutils.prepare\_input\_source(_source_, _base\=''_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.prepare_input_source "Link to this definition")

This function takes an input source and an optional base URL and returns a fully resolved [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource")
 object ready for reading. The input source can be given as a string, a file-like object, or an `InputSource` object; parsers will use this function to implement the polymorphic _source_ argument to their [`parse()`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.parse "xml.sax.xmlreader.XMLReader.parse")
 method.

#### Previous topic

[`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/3/library/xml.sax.handler.html "previous chapter")

#### Next topic

[`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.sax.saxutils+%E2%80%94+SAX+Utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.sax.utils.html&pagesource=library%2Fxml.sax.utils.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/xml.sax.utils.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers")
     |
*   [previous](https://docs.python.org/3/library/xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers")
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
*   [`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/3/library/xml.sax.utils.html)
    
*    
    
    |
*   Theme Auto Light Dark |