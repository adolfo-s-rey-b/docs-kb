### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.sax.utils.html "xml.sax.saxutils — SAX Utilities")
     |
*   [previous](https://docs.python.org/3/library/xml.sax.html "xml.sax — Support for SAX2 parsers")
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
*   [`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/3/library/xml.sax.handler.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`xml.sax.handler` — Base classes for SAX handlers[¶](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "Link to this heading")

===========================================================================================================================================================

**Source code:** [Lib/xml/sax/handler.py](https://github.com/python/cpython/tree/3.15/Lib/xml/sax/handler.py)

* * *

The SAX API defines five kinds of handlers: content handlers, DTD handlers, error handlers, entity resolvers and lexical handlers. Applications normally only need to implement those interfaces whose events they are interested in; they can implement the interfaces in a single object or in multiple objects. Handler implementations should inherit from the base classes provided in the module `xml.sax.handler`, so that all methods get default implementations.

class xml.sax.handler.ContentHandler[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler "Link to this definition")

This is the main callback interface in SAX, and the one most important to applications. The order of events in this interface mirrors the order of the information in the document.

class xml.sax.handler.DTDHandler[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.DTDHandler "Link to this definition")

Handle DTD events.

This interface specifies only those DTD events required for basic parsing (unparsed entities and attributes).

class xml.sax.handler.EntityResolver[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.EntityResolver "Link to this definition")

Basic interface for resolving entities. If you create an object implementing this interface, then register the object with your Parser, the parser will call the method in your object to resolve all external entities.

class xml.sax.handler.ErrorHandler[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler "Link to this definition")

Interface used by the parser to present error and warning messages to the application. The methods of this object control whether errors are immediately converted to exceptions or are handled in some other way.

class xml.sax.handler.LexicalHandler[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.LexicalHandler "Link to this definition")

Interface used by the parser to represent low frequency events which may not be of interest to many applications.

In addition to these classes, `xml.sax.handler` provides symbolic constants for the feature and property names.

xml.sax.handler.feature\_namespaces[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.feature_namespaces "Link to this definition")

value: `"http://xml.org/sax/features/namespaces"`

true: Perform Namespace processing.

false: Optionally do not perform Namespace processing (implies namespace-prefixes; default).

access: (parsing) read-only; (not parsing) read/write

xml.sax.handler.feature\_namespace\_prefixes[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.feature_namespace_prefixes "Link to this definition")

value: `"http://xml.org/sax/features/namespace-prefixes"`

true: Report the original prefixed names and attributes used for Namespace declarations.

false: Do not report attributes used for Namespace declarations, and optionally do not report original prefixed names (default).

access: (parsing) read-only; (not parsing) read/write

The parser based on [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.")
 does not support this feature.

xml.sax.handler.feature\_string\_interning[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.feature_string_interning "Link to this definition")

value: `"http://xml.org/sax/features/string-interning"`

true: All element names, prefixes, attribute names, Namespace URIs, and local names are interned in a dictionary (see [`property_interning_dict`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.property_interning_dict "xml.sax.handler.property_interning_dict")
).

false: Names are not necessarily interned, although they may be (default).

access: (parsing) read-only; (not parsing) read/write

xml.sax.handler.feature\_validation[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.feature_validation "Link to this definition")

value: `"http://xml.org/sax/features/validation"`

true: Report all validation errors (implies external-general-entities and external-parameter-entities).

false: Do not report validation errors.

access: (parsing) read-only; (not parsing) read/write

The parser based on [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.")
 does not support this feature, because Expat is a non-validating parser.

xml.sax.handler.feature\_external\_ges[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.feature_external_ges "Link to this definition")

Warning

Enabling opens a vulnerability to [external entity attacks](https://en.wikipedia.org/wiki/XML_external_entity_attack)
 if the parser is used with user-provided XML content. Please reflect on your [threat model](https://en.wikipedia.org/wiki/Threat_model)
 before enabling this feature.

value: `"http://xml.org/sax/features/external-general-entities"`

true: Include all external general (text) entities.

false: Do not include external general entities.

access: (parsing) read-only; (not parsing) read/write

xml.sax.handler.feature\_external\_pes[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.feature_external_pes "Link to this definition")

value: `"http://xml.org/sax/features/external-parameter-entities"`

true: Include all external parameter entities, including the external DTD subset.

false: Do not include any external parameter entities, even the external DTD subset.

access: (parsing) read-only; (not parsing) read/write

The parser based on [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.")
 does not support this feature.

xml.sax.handler.all\_features[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.all_features "Link to this definition")

List of all features.

xml.sax.handler.property\_lexical\_handler[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.property_lexical_handler "Link to this definition")

value: `"http://xml.org/sax/properties/lexical-handler"`

data type: [`LexicalHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.LexicalHandler "xml.sax.handler.LexicalHandler")

description: An optional extension handler for lexical events like comments.

access: read/write

xml.sax.handler.property\_declaration\_handler[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.property_declaration_handler "Link to this definition")

value: `"http://xml.org/sax/properties/declaration-handler"`

data type: an object implementing the SAX2 `DeclHandler` interface

description: An optional extension handler for DTD-related events other than notations and unparsed entities.

access: read/write

No parser in the standard library supports this property, and the standard library provides no such handler.

xml.sax.handler.property\_dom\_node[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.property_dom_node "Link to this definition")

value: `"http://xml.org/sax/properties/dom-node"`

data type: [`xml.dom.Node`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node "xml.dom.Node")

description: When parsing, the current DOM node being visited if this is a DOM iterator; when not parsing, the root DOM node for iteration.

access: (parsing) read-only; (not parsing) read/write

No parser in the standard library supports this property.

xml.sax.handler.property\_xml\_string[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.property_xml_string "Link to this definition")

value: `"http://xml.org/sax/properties/xml-string"`

data type: Bytes

description: The literal string of characters that was the source for the current event.

access: read-only, and only during a handler callback

xml.sax.handler.property\_encoding[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.property_encoding "Link to this definition")

value: `"http://www.python.org/sax/properties/encoding"`

data type: String

description: The name of the encoding to assume for input data.

access: read/write

No parser in the standard library supports this property.

xml.sax.handler.property\_interning\_dict[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.property_interning_dict "Link to this definition")

value: `"http://www.python.org/sax/properties/interning-dict"`

data type: Dictionary

description: The dictionary used to intern names, or `None` if names are not interned. Setting it enables interning, as does the [`feature_string_interning`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.feature_string_interning "xml.sax.handler.feature_string_interning")
 feature.

access: read/write

xml.sax.handler.all\_properties[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.all_properties "Link to this definition")

List of all known property names.

ContentHandler Objects[¶](https://docs.python.org/3/library/xml.sax.handler.html#contenthandler-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Users are expected to subclass [`ContentHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler")
 to support their application. The following methods are called by the parser on the appropriate events in the input document:

ContentHandler.setDocumentLocator(_locator_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.setDocumentLocator "Link to this definition")

Called by the parser to give the application a locator for locating the origin of document events.

SAX parsers are strongly encouraged (though not absolutely required) to supply a locator: if it does so, it must supply the locator to the application by invoking this method before invoking any of the other methods in the DocumentHandler interface.

The locator allows the application to determine the end position of any document-related event, even if the parser is not reporting an error. Typically, the application will use this information for reporting its own errors (such as character content that does not match an application’s business rules). The information returned by the locator is probably not sufficient for use with a search engine.

Note that the locator will return correct information only during the invocation of the events in this interface. The application should not attempt to use it at any other time.

ContentHandler.startDocument()[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startDocument "Link to this definition")

Receive notification of the beginning of a document.

The SAX parser will invoke this method only once, before any other methods in this interface or in DTDHandler (except for [`setDocumentLocator()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.setDocumentLocator "xml.sax.handler.ContentHandler.setDocumentLocator")
).

ContentHandler.endDocument()[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endDocument "Link to this definition")

Receive notification of the end of a document.

The SAX parser will invoke this method only once, and it will be the last method invoked during the parse. The parser shall not invoke this method until it has either abandoned parsing (because of an unrecoverable error) or reached the end of input.

ContentHandler.startPrefixMapping(_prefix_, _uri_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startPrefixMapping "Link to this definition")

Begin the scope of a prefix-URI Namespace mapping.

The information from this event is not necessary for normal Namespace processing: the SAX XML reader will automatically replace prefixes for element and attribute names when the `feature_namespaces` feature is enabled (the default).

There are cases, however, when applications need to use prefixes in character data or in attribute values, where they cannot safely be expanded automatically; the `startPrefixMapping()` and [`endPrefixMapping()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endPrefixMapping "xml.sax.handler.ContentHandler.endPrefixMapping")
 events supply the information to the application to expand prefixes in those contexts itself, if necessary.

Note that `startPrefixMapping()` and [`endPrefixMapping()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endPrefixMapping "xml.sax.handler.ContentHandler.endPrefixMapping")
 events are not guaranteed to be properly nested relative to each-other: all `startPrefixMapping()` events will occur before the corresponding [`startElement()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startElement "xml.sax.handler.ContentHandler.startElement")
 event, and all `endPrefixMapping()` events will occur after the corresponding [`endElement()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endElement "xml.sax.handler.ContentHandler.endElement")
 event, but their order is not guaranteed.

ContentHandler.endPrefixMapping(_prefix_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endPrefixMapping "Link to this definition")

End the scope of a prefix-URI mapping.

See [`startPrefixMapping()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startPrefixMapping "xml.sax.handler.ContentHandler.startPrefixMapping")
 for details. This event will always occur after the corresponding [`endElement()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endElement "xml.sax.handler.ContentHandler.endElement")
 event, but the order of `endPrefixMapping()` events is not otherwise guaranteed.

ContentHandler.startElement(_name_, _attrs_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startElement "Link to this definition")

Signals the start of an element in non-namespace mode.

The _name_ parameter contains the raw XML 1.0 name of the element type as a string and the _attrs_ parameter holds an object of the [Attributes](https://docs.python.org/3/library/xml.sax.reader.html#attributes-objects)
 interface containing the attributes of the element. The object passed as _attrs_ may be re-used by the parser; holding on to a reference to it is not a reliable way to keep a copy of the attributes. To keep a copy of the attributes, use the [`copy()`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")
 method of the _attrs_ object.

ContentHandler.endElement(_name_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endElement "Link to this definition")

Signals the end of an element in non-namespace mode.

The _name_ parameter contains the name of the element type, just as with the [`startElement()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startElement "xml.sax.handler.ContentHandler.startElement")
 event.

ContentHandler.startElementNS(_name_, _qname_, _attrs_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startElementNS "Link to this definition")

Signals the start of an element in namespace mode.

The _name_ parameter contains the name of the element type as a `(uri, localname)` tuple, the _qname_ parameter contains the raw XML 1.0 name used in the source document, and the _attrs_ parameter holds an instance of the [AttributesNS](https://docs.python.org/3/library/xml.sax.reader.html#attributes-ns-objects)
 interface containing the attributes of the element. If no namespace is associated with the element, the _uri_ component of _name_ will be `None`. The object passed as _attrs_ may be re-used by the parser; holding on to a reference to it is not a reliable way to keep a copy of the attributes. To keep a copy of the attributes, use the [`copy()`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")
 method of the _attrs_ object.

Parsers may set the _qname_ parameter to `None`, unless the `feature_namespace_prefixes` feature is activated.

ContentHandler.endElementNS(_name_, _qname_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endElementNS "Link to this definition")

Signals the end of an element in namespace mode.

The _name_ parameter contains the name of the element type, just as with the [`startElementNS()`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startElementNS "xml.sax.handler.ContentHandler.startElementNS")
 method, likewise the _qname_ parameter.

ContentHandler.characters(_content_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.characters "Link to this definition")

Receive notification of character data.

The Parser will call this method to report each chunk of character data. SAX parsers may return all contiguous character data in a single chunk, or they may split it into several chunks; however, all of the characters in any single event must come from the same external entity so that the Locator provides useful information.

_content_ may be a string or bytes instance; the `expat` reader module always produces strings.

Note

The earlier SAX 1 interface provided by the Python XML Special Interest Group used a more Java-like interface for this method. Since most parsers used from Python did not take advantage of the older interface, the simpler signature was chosen to replace it. To convert old code to the new interface, use _content_ instead of slicing content with the old _offset_ and _length_ parameters.

ContentHandler.ignorableWhitespace(_whitespace_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.ignorableWhitespace "Link to this definition")

Receive notification of ignorable whitespace in element content.

Validating Parsers must use this method to report each chunk of ignorable whitespace (see the W3C XML 1.0 recommendation, section 2.10): non-validating parsers may also use this method if they are capable of parsing and using content models.

SAX parsers may return all contiguous whitespace in a single chunk, or they may split it into several chunks; however, all of the characters in any single event must come from the same external entity, so that the Locator provides useful information.

ContentHandler.processingInstruction(_target_, _data_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.processingInstruction "Link to this definition")

Receive notification of a processing instruction.

The Parser will invoke this method once for each processing instruction found: note that processing instructions may occur before or after the main document element.

A SAX parser should never report an XML declaration (XML 1.0, section 2.8) or a text declaration (XML 1.0, section 4.3.1) using this method.

ContentHandler.skippedEntity(_name_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.skippedEntity "Link to this definition")

Receive notification of a skipped entity.

The Parser will invoke this method once for each entity skipped. Non-validating processors may skip entities if they have not seen the declarations (because, for example, the entity was declared in an external DTD subset). All processors may skip external entities, depending on the values of the `feature_external_ges` and the `feature_external_pes` properties.

DTDHandler Objects[¶](https://docs.python.org/3/library/xml.sax.handler.html#dtdhandler-objects "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

[`DTDHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.DTDHandler "xml.sax.handler.DTDHandler")
 instances provide the following methods:

DTDHandler.notationDecl(_name_, _publicId_, _systemId_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.DTDHandler.notationDecl "Link to this definition")

Handle a notation declaration event.

DTDHandler.unparsedEntityDecl(_name_, _publicId_, _systemId_, _ndata_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.DTDHandler.unparsedEntityDecl "Link to this definition")

Handle an unparsed entity declaration event.

EntityResolver Objects[¶](https://docs.python.org/3/library/xml.sax.handler.html#entityresolver-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

EntityResolver.resolveEntity(_publicId_, _systemId_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.EntityResolver.resolveEntity "Link to this definition")

Resolve the system identifier of an entity and return either the system identifier to read from as a string, or an InputSource to read from. The default implementation returns _systemId_.

ErrorHandler Objects[¶](https://docs.python.org/3/library/xml.sax.handler.html#errorhandler-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Objects with this interface are used to receive error and warning information from the [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader")
. If you create an object that implements this interface, then register the object with your `XMLReader`, the parser will call the methods in your object to report all warnings and errors. There are three levels of errors available: warnings, (possibly) recoverable errors, and unrecoverable errors. All methods take a [`SAXParseException`](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXParseException "xml.sax.SAXParseException")
 as the only parameter. Errors and warnings may be converted to an exception by raising the passed-in exception object.

ErrorHandler.error(_exception_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler.error "Link to this definition")

Called when the parser encounters a recoverable error. If this method does not raise an exception, parsing may continue, but further document information should not be expected by the application. Allowing the parser to continue may allow additional errors to be discovered in the input document.

ErrorHandler.fatalError(_exception_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler.fatalError "Link to this definition")

Called when the parser encounters an error it cannot recover from; parsing is expected to terminate when this method returns.

ErrorHandler.warning(_exception_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler.warning "Link to this definition")

Called when the parser presents minor warning information to the application. Parsing is expected to continue when this method returns, and document information will continue to be passed to the application. Raising an exception in this method will cause parsing to end.

LexicalHandler Objects[¶](https://docs.python.org/3/library/xml.sax.handler.html#lexicalhandler-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Optional SAX2 handler for lexical events.

This handler is used to obtain lexical information about an XML document. Lexical information includes information describing the document encoding used and XML comments embedded in the document, as well as section boundaries for the DTD and for any CDATA sections. The lexical handlers are used in the same manner as content handlers.

Set the LexicalHandler of an XMLReader by using the setProperty method with the property identifier `'http://xml.org/sax/properties/lexical-handler'`.

LexicalHandler.comment(_content_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.LexicalHandler.comment "Link to this definition")

Reports a comment anywhere in the document (including the DTD and outside the document element).

LexicalHandler.startDTD(_name_, _public\_id_, _system\_id_)[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.LexicalHandler.startDTD "Link to this definition")

Reports the start of the DTD declarations if the document has an associated DTD.

LexicalHandler.endDTD()[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.LexicalHandler.endDTD "Link to this definition")

Reports the end of DTD declaration.

LexicalHandler.startCDATA()[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.LexicalHandler.startCDATA "Link to this definition")

Reports the start of a CDATA marked section.

The contents of the CDATA marked section will be reported through the characters handler.

LexicalHandler.endCDATA()[¶](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.LexicalHandler.endCDATA "Link to this definition")

Reports the end of a CDATA marked section.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/3/library/xml.sax.handler.html#)
    *   [ContentHandler Objects](https://docs.python.org/3/library/xml.sax.handler.html#contenthandler-objects)
        
    *   [DTDHandler Objects](https://docs.python.org/3/library/xml.sax.handler.html#dtdhandler-objects)
        
    *   [EntityResolver Objects](https://docs.python.org/3/library/xml.sax.handler.html#entityresolver-objects)
        
    *   [ErrorHandler Objects](https://docs.python.org/3/library/xml.sax.handler.html#errorhandler-objects)
        
    *   [LexicalHandler Objects](https://docs.python.org/3/library/xml.sax.handler.html#lexicalhandler-objects)
        

#### Previous topic

[`xml.sax` — Support for SAX2 parsers](https://docs.python.org/3/library/xml.sax.html "previous chapter")

#### Next topic

[`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/3/library/xml.sax.utils.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.sax.handler+%E2%80%94+Base+classes+for+SAX+handlers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.sax.handler.html&pagesource=library%2Fxml.sax.handler.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/xml.sax.handler.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.sax.utils.html "xml.sax.saxutils — SAX Utilities")
     |
*   [previous](https://docs.python.org/3/library/xml.sax.html "xml.sax — Support for SAX2 parsers")
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
*   [`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/3/library/xml.sax.handler.html)
    
*    
    
    |
*   Theme Auto Light Dark |