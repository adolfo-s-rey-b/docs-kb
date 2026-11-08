### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/internet.html "Internet Protocols and Support")
     |
*   [previous](https://docs.python.org/3/library/xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers")
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
*   [`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`xml.parsers.expat` — Fast XML parsing using Expat[¶](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "Link to this heading")

======================================================================================================================================================

* * *

Note

If you need to parse untrusted or unauthenticated data, see [XML security](https://docs.python.org/3/library/xml.html#xml-security)
.

The `xml.parsers.expat` module is a Python interface to the Expat non-validating XML parser. The module provides a single extension type, `xmlparser`, that represents the current state of an XML parser. After an `xmlparser` object has been created, various attributes of the object can be set to handler functions. When an XML document is then fed to the parser, the handler functions are called for the character data and markup in the XML document.

This module uses the `pyexpat` module to provide access to the Expat parser. Direct use of the `pyexpat` module is deprecated.

This module provides the following exception, type object and data items:

exception xml.parsers.expat.ExpatError[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "Link to this definition")

The exception raised when Expat reports an error. See section [ExpatError Exceptions](https://docs.python.org/3/library/pyexpat.html#expaterror-objects)
 for more information on interpreting Expat errors.

exception xml.parsers.expat.error[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.error "Link to this definition")

Alias for [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
.

xml.parsers.expat.XMLParserType[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.XMLParserType "Link to this definition")

The type of the return values from the [`ParserCreate()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ParserCreate "xml.parsers.expat.ParserCreate")
 function.

xml.parsers.expat.EXPAT\_VERSION[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.EXPAT_VERSION "Link to this definition")

The version string of the Expat library loaded by the interpreter, like `'expat_2.8.4'`.

xml.parsers.expat.version\_info[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.version_info "Link to this definition")

The version of the Expat library loaded by the interpreter, as a tuple of three integers: major, minor and micro version.

xml.parsers.expat.features[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.features "Link to this definition")

The list of the features with which the loaded Expat library was compiled, as `(name, value)` pairs. The value is only meaningful for features which have one, like `'XML_CONTEXT_BYTES'` or the default protection limits `'XML_BLAP_ACT_THRES'` and `'XML_AT_MAX_AMP'`; for other features, like `'XML_DTD'` and `'XML_NS'`, the value is `0` and only the presence of the name is significant.

The `xml.parsers.expat` module contains two functions:

xml.parsers.expat.ErrorString(_errno_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ErrorString "Link to this definition")

Returns an explanatory string for a given error number _errno_.

xml.parsers.expat.ParserCreate(_encoding\=None_, _namespace\_separator\=None_, _intern\=None_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ParserCreate "Link to this definition")

Creates and returns a new `xmlparser` object. _encoding_, if specified, must be a string naming the encoding used by the XML data. Expat doesn’t support as many encodings as Python does, and its repertoire of encodings can’t be extended; it supports UTF-8, UTF-16, ISO-8859-1 (Latin1), and ASCII. If _encoding_ [\[1\]](https://docs.python.org/3/library/pyexpat.html#id3)
 is given it will override the implicit or explicit encoding of the document.

Parsers created through `ParserCreate()` are called “root” parsers, in the sense that they do not have any parent parser attached. Non-root parsers are created by [`parser.ExternalEntityParserCreate`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityParserCreate "xml.parsers.expat.xmlparser.ExternalEntityParserCreate")
.

Expat can optionally do XML namespace processing for you, enabled by providing a value for _namespace\_separator_. The value must be a one-character string; a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 will be raised if the string has an illegal length (`None` is considered the same as omission). When namespace processing is enabled, element type names and attribute names that belong to a namespace will be expanded. The element name passed to the element handlers `StartElementHandler` and `EndElementHandler` will be the concatenation of the namespace URI, the namespace separator character, and the local part of the name. If the namespace separator is a zero byte (`chr(0)`) then the namespace URI and the local part will be concatenated without any separator.

For example, if _namespace\_separator_ is set to a space character (`' '`) and the following document is parsed:

<?xml version="1.0"?>
<root xmlns    = "http://default-namespace.org/"
      xmlns:py = "http://www.python.org/ns/"\>
  <py:elem1 />
  <elem2 xmlns="" />
</root>

`StartElementHandler` will receive the following strings for each element:

Copy

http://default\-namespace.org/ root
http://www.python.org/ns/ elem1
elem2

_intern_, if given, must be a dictionary. It is used to intern the names of elements and attributes, and is available as the [`intern`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.intern "xml.parsers.expat.xmlparser.intern")
 attribute. By default a new empty dictionary is created for every parser.

Due to limitations in the `Expat` library used by `pyexpat`, the `xmlparser` instance returned can only be used to parse a single XML document. Call `ParserCreate` for each document to provide unique parser instances.

See also

[The Expat XML Parser](http://www.libexpat.org/)

Home page of the Expat project.

XMLParser Objects[¶](https://docs.python.org/3/library/pyexpat.html#xmlparser-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------

`xmlparser` objects have the following methods:

xmlparser.Parse(_data_\[, _isfinal_\])[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.Parse "Link to this definition")

Parses the contents of _data_, calling the appropriate handler functions to process the parsed data. _data_ can be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or a string. If it is a string, the encoding declaration in the XML data is ignored, and the data is parsed as already decoded text. _isfinal_ must be true on the final call to this method; it allows the parsing of a single file in fragments, not the submission of multiple files. _data_ can be empty at any time.

xmlparser.ParseFile(_file_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ParseFile "Link to this definition")

Parse XML data reading from the object _file_. _file_ only needs to provide the `read(nbytes)` method, which returns bytes, and an empty bytes object when there’s no more data. Text files are not supported; use [`Parse()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.Parse "xml.parsers.expat.xmlparser.Parse")
 for data which is already decoded.

xmlparser.SetBase(_base_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBase "Link to this definition")

Sets the base to be used for resolving relative URIs in system identifiers in declarations. Resolving relative identifiers is left to the application: this value will be passed through as the _base_ argument to the [`ExternalEntityRefHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler")
, [`NotationDeclHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.NotationDeclHandler "xml.parsers.expat.xmlparser.NotationDeclHandler")
, and [`UnparsedEntityDeclHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler "xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler")
 functions.

xmlparser.GetBase()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.GetBase "Link to this definition")

Returns a string containing the base set by a previous call to [`SetBase()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBase "xml.parsers.expat.xmlparser.SetBase")
, or `None` if `SetBase()` hasn’t been called.

xmlparser.GetInputContext()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.GetInputContext "Link to this definition")

Returns the input data which generated the current event as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. The data is in the encoding of the entity which contains the text. It extends to the end of the currently buffered input, therefore it can contain also the data of the following events, and if the event was generated by a large amount of text, not all of it may be available. When called while an event handler is not active, the return value is `None`.

xmlparser.ExternalEntityParserCreate(_context_\[, _encoding_\])[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityParserCreate "Link to this definition")

Create a “child” parser which can be used to parse an external parsed entity referred to by content parsed by the parent parser. The _context_ parameter should be the string passed to the [`ExternalEntityRefHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler")
 handler function, described below. The child parser is created with the [`ordered_attributes`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ordered_attributes "xml.parsers.expat.xmlparser.ordered_attributes")
 and [`specified_attributes`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.specified_attributes "xml.parsers.expat.xmlparser.specified_attributes")
 set to the values of this parser.

xmlparser.SetParamEntityParsing(_flag_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetParamEntityParsing "Link to this definition")

Control parsing of parameter entities (including the external DTD subset). Possible _flag_ values are `XML_PARAM_ENTITY_PARSING_NEVER`, `XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE` and `XML_PARAM_ENTITY_PARSING_ALWAYS`. Return true if setting the flag was successful.

xmlparser.UseForeignDTD(\[_flag_\])[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.UseForeignDTD "Link to this definition")

Calling this with a true value for _flag_ (the default) will cause Expat to call the [`ExternalEntityRefHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler")
 with [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 for all arguments to allow an alternate DTD to be loaded. If the document does not contain a document type declaration, the `ExternalEntityRefHandler` will still be called, but the [`StartDoctypeDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartDoctypeDeclHandler "xml.parsers.expat.xmlparser.StartDoctypeDeclHandler")
 and [`EndDoctypeDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndDoctypeDeclHandler "xml.parsers.expat.xmlparser.EndDoctypeDeclHandler")
 will not be called.

Passing a false value for _flag_ will cancel a previous call that passed a true value, but otherwise has no effect.

This method can only be called before the [`Parse()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.Parse "xml.parsers.expat.xmlparser.Parse")
 or [`ParseFile()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ParseFile "xml.parsers.expat.xmlparser.ParseFile")
 methods are called; calling it after either of those have been called causes [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
 to be raised with the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.")
 attribute set to `errors.codes[errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING]`.

xmlparser.SetReparseDeferralEnabled(_enabled_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "Link to this definition")

Warning

Calling `SetReparseDeferralEnabled(False)` has security implications, as detailed below; please make sure to understand these consequences prior to using the `SetReparseDeferralEnabled` method.

Expat 2.6.0 introduced a security mechanism called “reparse deferral” where instead of causing denial of service through quadratic runtime from reparsing large tokens, reparsing of unfinished tokens is now delayed by default until a sufficient amount of input is reached. Due to this delay, registered handlers may — depending of the sizing of input chunks pushed to Expat — no longer be called right after pushing new input to the parser. Where immediate feedback and taking over responsibility of protecting against denial of service from large tokens are both wanted, calling `SetReparseDeferralEnabled(False)` disables reparse deferral for the current Expat parser instance, temporarily or altogether. Calling `SetReparseDeferralEnabled(True)` allows re-enabling reparse deferral.

`SetReparseDeferralEnabled()` has been backported to some prior releases of CPython as a security fix. Check for availability using [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
 if used in code running across a variety of Python versions.

Added in version 3.13.

xmlparser.GetReparseDeferralEnabled()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.GetReparseDeferralEnabled "Link to this definition")

Returns whether reparse deferral is currently enabled for the given Expat parser instance.

Added in version 3.13.

`xmlparser` objects have the following methods to tune protections against some common XML vulnerabilities.

xmlparser.SetBillionLaughsAttackProtectionActivationThreshold(_threshold_, _/_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionActivationThreshold "Link to this definition")

Sets the number of output bytes needed to activate protection against [billion laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack)
 attacks.

The number of output bytes includes amplification from entity expansion and reading DTD files.

Parser objects usually have a protection activation threshold of 8 MiB, but the actual default value depends on the underlying Expat library.

An [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
 is raised if this method is called on a [non-root](https://docs.python.org/3/library/pyexpat.html#xmlparser-non-root)
 parser. The corresponding [`lineno`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.lineno "xml.parsers.expat.ExpatError.lineno")
 and [`offset`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.offset "xml.parsers.expat.ExpatError.offset")
 should not be used as they may have no special meaning.

`SetBillionLaughsAttackProtectionActivationThreshold()` has been backported to some prior releases of CPython as a security fix. Check for availability using [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
 if used in code running across a variety of Python versions.

Note

Activation thresholds below 4 MiB are known to break support for DITA 1.3 payload and are hence not recommended.

Added in version 3.15.

xmlparser.SetBillionLaughsAttackProtectionMaximumAmplification(_max\_factor_, _/_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionMaximumAmplification "Link to this definition")

Sets the maximum tolerated amplification factor for protection against [billion laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack)
 attacks.

The amplification factor is calculated as `(direct + indirect) / direct` while parsing, where `direct` is the number of bytes read from the primary document in parsing and `indirect` is the number of bytes added by expanding entities and reading of external DTD files.

The _max\_factor_ value must be a non-NaN [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 value greater than or equal to 1.0. Peak amplifications of factor 15,000 for the entire payload and of factor 30,000 in the middle of parsing have been observed with small benign files in practice. In particular, the activation threshold should be carefully chosen to avoid false positives.

Parser objects usually have a maximum amplification factor of 100, but the actual default value depends on the underlying Expat library.

An [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
 is raised if this method is called on a [non-root](https://docs.python.org/3/library/pyexpat.html#xmlparser-non-root)
 parser or if _max\_factor_ is outside the valid range. The corresponding [`lineno`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.lineno "xml.parsers.expat.ExpatError.lineno")
 and [`offset`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.offset "xml.parsers.expat.ExpatError.offset")
 should not be used as they may have no special meaning.

`SetBillionLaughsAttackProtectionMaximumAmplification()` has been backported to some prior releases of CPython as a security fix. Check for availability using [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
 if used in code running across a variety of Python versions.

Note

The maximum amplification factor is only considered if the threshold that can be adjusted by [`SetBillionLaughsAttackProtectionActivationThreshold()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionActivationThreshold "xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionActivationThreshold")
 is exceeded.

Added in version 3.15.

xmlparser.SetAllocTrackerActivationThreshold(_threshold_, _/_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold "Link to this definition")

Sets the number of allocated bytes of dynamic memory needed to activate protection against disproportionate use of RAM.

Parser objects usually have an allocation activation threshold of 64 MiB, but the actual default value depends on the underlying Expat library.

An [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
 is raised if this method is called on a [non-root](https://docs.python.org/3/library/pyexpat.html#xmlparser-non-root)
 parser. The corresponding [`lineno`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.lineno "xml.parsers.expat.ExpatError.lineno")
 and [`offset`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.offset "xml.parsers.expat.ExpatError.offset")
 should not be used as they may have no special meaning.

`SetAllocTrackerActivationThreshold()` has been backported to some prior releases of CPython as a security fix. Check for availability using [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
 if used in code running across a variety of Python versions.

Added in version 3.15.

xmlparser.SetAllocTrackerMaximumAmplification(_max\_factor_, _/_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerMaximumAmplification "Link to this definition")

Sets the maximum amplification factor between direct input and bytes of dynamic memory allocated.

The amplification factor is calculated as `allocated / direct` while parsing, where `direct` is the number of bytes read from the primary document in parsing and `allocated` is the number of bytes of dynamic memory allocated in the parser hierarchy.

The _max\_factor_ value must be a non-NaN [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 value greater than or equal to 1.0. Amplification factors greater than 100.0 can be observed near the start of parsing even with benign files in practice. In particular, the activation threshold should be carefully chosen to avoid false positives.

Parser objects usually have a maximum amplification factor of 100, but the actual default value depends on the underlying Expat library.

An [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
 is raised if this method is called on a [non-root](https://docs.python.org/3/library/pyexpat.html#xmlparser-non-root)
 parser or if _max\_factor_ is outside the valid range. The corresponding [`lineno`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.lineno "xml.parsers.expat.ExpatError.lineno")
 and [`offset`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.offset "xml.parsers.expat.ExpatError.offset")
 should not be used as they may have no special meaning.

`SetAllocTrackerMaximumAmplification()` has been backported to some prior releases of CPython as a security fix. Check for availability using [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
 if used in code running across a variety of Python versions.

Note

The maximum amplification factor is only considered if the threshold that can be adjusted by [`SetAllocTrackerActivationThreshold()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold "xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold")
 is exceeded.

Added in version 3.15.

`xmlparser` objects have the following attributes:

xmlparser.buffer\_size[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_size "Link to this definition")

The size of the buffer used when [`buffer_text`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text")
 is true. A new buffer size can be set by assigning a new integer value to this attribute. When the size is changed, the buffer will be flushed.

xmlparser.buffer\_text[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "Link to this definition")

Setting this to true causes the `xmlparser` object to buffer textual content returned by Expat to avoid multiple calls to the [`CharacterDataHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CharacterDataHandler "xml.parsers.expat.xmlparser.CharacterDataHandler")
 callback whenever possible. This can improve performance substantially since Expat normally breaks character data into chunks at every line ending. This attribute is false by default, and may be changed at any time. Note that when it is false, data that does not contain newlines may be chunked too.

xmlparser.buffer\_used[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_used "Link to this definition")

If [`buffer_text`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text")
 is enabled, the number of bytes stored in the buffer. These bytes represent UTF-8 encoded text. This attribute has no meaningful interpretation when `buffer_text` is false.

xmlparser.ordered\_attributes[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ordered_attributes "Link to this definition")

Setting this attribute to a non-zero integer causes the attributes to be reported as a list rather than a dictionary. The attributes are presented in the order found in the document text. For each attribute, two list entries are presented: the attribute name and the attribute value. (Older versions of this module also used this format.) By default, this attribute is false; it may be changed at any time.

xmlparser.specified\_attributes[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.specified_attributes "Link to this definition")

If set to a non-zero integer, the parser will report only those attributes which were specified in the document instance and not those which were derived from attribute declarations. Applications which set this need to be especially careful to use what additional information is available from the declarations as needed to comply with the standards for the behavior of XML processors. By default, this attribute is false; it may be changed at any time.

xmlparser.intern[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.intern "Link to this definition")

The dictionary used to intern the names of elements and attributes. It is either the dictionary passed as the _intern_ argument of [`ParserCreate()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ParserCreate "xml.parsers.expat.ParserCreate")
, or a new dictionary created for this parser.

xmlparser.namespace\_prefixes[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.namespace_prefixes "Link to this definition")

If set to a true value, and namespace processing is enabled, the namespace prefix is reported as the third part of the expanded name, separated by the namespace separator. Names which have no prefix are not affected. By default, this attribute is false; it may be changed at any time.

The following attributes contain values relating to the most recent error encountered by an `xmlparser` object, and will only have correct values once a call to `Parse()` or `ParseFile()` has raised an [`xml.parsers.expat.ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
 exception.

xmlparser.ErrorByteIndex[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ErrorByteIndex "Link to this definition")

Byte index at which an error occurred.

xmlparser.ErrorCode[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ErrorCode "Link to this definition")

Numeric code specifying the problem. This value can be passed to the [`ErrorString()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ErrorString "xml.parsers.expat.ErrorString")
 function, or compared to one of the constants defined in the `errors` object.

xmlparser.ErrorColumnNumber[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ErrorColumnNumber "Link to this definition")

Column number at which an error occurred.

xmlparser.ErrorLineNumber[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ErrorLineNumber "Link to this definition")

Line number at which an error occurred.

The following attributes contain values relating to the current parse location in an `xmlparser` object. During a callback reporting a parse event they indicate the location of the first of the sequence of characters that generated the event. When called outside of a callback, the position indicated will be just past the last parse event (regardless of whether there was an associated callback).

xmlparser.CurrentByteIndex[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CurrentByteIndex "Link to this definition")

Current byte index in the parser input.

xmlparser.CurrentColumnNumber[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CurrentColumnNumber "Link to this definition")

Current column number in the parser input.

xmlparser.CurrentLineNumber[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CurrentLineNumber "Link to this definition")

Current line number in the parser input.

Here is the list of handlers that can be set. To set a handler on an `xmlparser` object _o_, use `o.handlername = func`. _handlername_ must be taken from the following list, and _func_ must be a callable object accepting the correct number of arguments. The arguments are all strings, unless otherwise stated.

xmlparser.XmlDeclHandler(_version_, _encoding_, _standalone_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.XmlDeclHandler "Link to this definition")

Called when the XML declaration is parsed. The XML declaration is the (optional) declaration of the applicable version of the XML recommendation, the encoding of the document text, and an optional “standalone” declaration. _version_ and _encoding_ will be strings, and _standalone_ will be `1` if the document is declared standalone, `0` if it is declared not to be standalone, or `-1` if the standalone clause was omitted.

xmlparser.StartDoctypeDeclHandler(_doctypeName_, _systemId_, _publicId_, _has\_internal\_subset_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartDoctypeDeclHandler "Link to this definition")

Called when Expat begins parsing the document type declaration (`<!DOCTYPE ...`). The _doctypeName_ is provided exactly as presented. The _systemId_ and _publicId_ parameters give the system and public identifiers if specified, or `None` if omitted. _has\_internal\_subset_ will be true if the document contains an internal document declaration subset.

xmlparser.EndDoctypeDeclHandler()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndDoctypeDeclHandler "Link to this definition")

Called when Expat is done parsing the document type declaration.

xmlparser.ElementDeclHandler(_name_, _model_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ElementDeclHandler "Link to this definition")

Called once for each element type declaration. _name_ is the name of the element type, and _model_ is a representation of the content model.

xmlparser.AttlistDeclHandler(_elname_, _attname_, _type_, _default_, _required_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.AttlistDeclHandler "Link to this definition")

Called for each declared attribute for an element type. If an attribute list declaration declares three attributes, this handler is called three times, once for each attribute. _elname_ is the name of the element to which the declaration applies and _attname_ is the name of the attribute declared. The The attribute type is a string passed as _type_: `'CDATA'`, `'ID'`, `'IDREF'`, `'IDREFS'`, `'ENTITY'`, `'ENTITIES'`, `'NMTOKEN'` or `'NMTOKENS'`, an enumeration like `'(x|y)'`, or a notation list like `'NOTATION(n1|n2)'`. _default_ gives the default value for the attribute used when the attribute is not specified by the document instance, or `None` if there is no default value (`#IMPLIED` values). If the attribute is required to be given in the document instance, _required_ will be true.

xmlparser.StartElementHandler(_name_, _attributes_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartElementHandler "Link to this definition")

Called for the start of every element. _name_ is a string containing the element name, and _attributes_ is the element attributes. If [`ordered_attributes`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ordered_attributes "xml.parsers.expat.xmlparser.ordered_attributes")
 is true, this is a list (see `ordered_attributes` for a full description). Otherwise it’s a dictionary mapping names to values.

xmlparser.EndElementHandler(_name_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndElementHandler "Link to this definition")

Called for the end of every element.

xmlparser.ProcessingInstructionHandler(_target_, _data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ProcessingInstructionHandler "Link to this definition")

Called for every processing instruction.

xmlparser.CharacterDataHandler(_data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CharacterDataHandler "Link to this definition")

Called for character data. This will be called for normal character data, CDATA marked content, and ignorable whitespace. Applications which must distinguish these cases can use the [`StartCdataSectionHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartCdataSectionHandler "xml.parsers.expat.xmlparser.StartCdataSectionHandler")
, [`EndCdataSectionHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndCdataSectionHandler "xml.parsers.expat.xmlparser.EndCdataSectionHandler")
, and [`ElementDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ElementDeclHandler "xml.parsers.expat.xmlparser.ElementDeclHandler")
 callbacks to collect the required information. Note that the character data may be chunked even if it is short and so you may receive more than one call to `CharacterDataHandler()`. Set the [`buffer_text`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text")
 instance attribute to `True` to avoid that.

xmlparser.UnparsedEntityDeclHandler(_entityName_, _base_, _systemId_, _publicId_, _notationName_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler "Link to this definition")

Called for unparsed (NDATA) entity declarations. If this handler is not set, such declarations are reported by [`EntityDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EntityDeclHandler "xml.parsers.expat.xmlparser.EntityDeclHandler")
, which is preferred for new code. (The underlying function in the Expat library has been declared obsolete.)

xmlparser.EntityDeclHandler(_entityName_, _is\_parameter\_entity_, _value_, _base_, _systemId_, _publicId_, _notationName_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EntityDeclHandler "Link to this definition")

Called for all entity declarations. For parameter and internal entities, _value_ will be a string giving the declared contents of the entity; this will be `None` for external entities. The _notationName_ parameter will be `None` for parsed entities, and the name of the notation for unparsed entities. _is\_parameter\_entity_ will be true if the entity is a parameter entity or false for general entities (most applications only need to be concerned with general entities).

xmlparser.NotationDeclHandler(_notationName_, _base_, _systemId_, _publicId_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.NotationDeclHandler "Link to this definition")

Called for notation declarations. _notationName_, _base_, and _systemId_, and _publicId_ are strings if given. If the public identifier is omitted, _publicId_ will be `None`.

xmlparser.StartNamespaceDeclHandler(_prefix_, _uri_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartNamespaceDeclHandler "Link to this definition")

Called when an element contains a namespace declaration. Namespace declarations are processed before the [`StartElementHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartElementHandler "xml.parsers.expat.xmlparser.StartElementHandler")
 is called for the element on which declarations are placed.

xmlparser.EndNamespaceDeclHandler(_prefix_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndNamespaceDeclHandler "Link to this definition")

Called when the closing tag is reached for an element that contained a namespace declaration. This is called once for each namespace declaration on the element in the reverse of the order for which the [`StartNamespaceDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartNamespaceDeclHandler "xml.parsers.expat.xmlparser.StartNamespaceDeclHandler")
 was called to indicate the start of each namespace declaration’s scope. Calls to this handler are made after the corresponding [`EndElementHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndElementHandler "xml.parsers.expat.xmlparser.EndElementHandler")
 for the end of the element.

xmlparser.CommentHandler(_data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CommentHandler "Link to this definition")

Called for comments. _data_ is the text of the comment, excluding the leading `'<!-``-'` and trailing `'-``->'`.

xmlparser.StartCdataSectionHandler()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartCdataSectionHandler "Link to this definition")

Called at the start of a CDATA section. This and [`EndCdataSectionHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndCdataSectionHandler "xml.parsers.expat.xmlparser.EndCdataSectionHandler")
 are needed to be able to identify the syntactical start and end for CDATA sections.

xmlparser.EndCdataSectionHandler()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndCdataSectionHandler "Link to this definition")

Called at the end of a CDATA section.

xmlparser.DefaultHandler(_data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.DefaultHandler "Link to this definition")

Called for any characters in the XML document for which no applicable handler has been specified. This means characters that are part of a construct which could be reported, but for which no handler has been supplied.

xmlparser.DefaultHandlerExpand(_data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.DefaultHandlerExpand "Link to this definition")

This is the same as the [`DefaultHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.DefaultHandler "xml.parsers.expat.xmlparser.DefaultHandler")
, but doesn’t inhibit expansion of internal entities. The entity reference will not be passed to the default handler.

xmlparser.NotStandaloneHandler()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.NotStandaloneHandler "Link to this definition")

Called if the XML document hasn’t been declared as being a standalone document. This happens when there is an external subset or a reference to a parameter entity, but the XML declaration does not set standalone to `yes` in an XML declaration. If this handler returns `0`, then the parser will raise an `XML_ERROR_NOT_STANDALONE` error. If this handler is not set, no exception is raised by the parser for this condition.

xmlparser.ExternalEntityRefHandler(_context_, _base_, _systemId_, _publicId_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "Link to this definition")

Warning

Implementing a handler that accesses local files and/or the network may create a vulnerability to [external entity attacks](https://en.wikipedia.org/wiki/XML_external_entity_attack)
 if `xmlparser` is used with user-provided XML content. Please reflect on your [threat model](https://en.wikipedia.org/wiki/Threat_model)
 before implementing this handler.

Called for references to external entities. _base_ is the current base, as set by a previous call to [`SetBase()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBase "xml.parsers.expat.xmlparser.SetBase")
. The public and system identifiers, _systemId_ and _publicId_, are strings if given; if the public identifier is not given, _publicId_ will be `None`. The _context_ value is opaque and should only be used as described below.

For external entities to be parsed, this handler must be implemented. It is responsible for creating the sub-parser using `ExternalEntityParserCreate(context)`, initializing it with the appropriate callbacks, and parsing the entity. This handler should return an integer; if it returns `0`, the parser will raise an `XML_ERROR_EXTERNAL_ENTITY_HANDLING` error, otherwise parsing will continue.

If this handler is not provided, external entities are reported by the [`DefaultHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.DefaultHandler "xml.parsers.expat.xmlparser.DefaultHandler")
 callback, if provided.

xmlparser.SkippedEntityHandler(_entityName_, _is\_parameter\_entity_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SkippedEntityHandler "Link to this definition")

Called for entity references which are not expanded, because the parser did not read the declaration of the entity. This happens when the external DTD subset or an external parameter entity is not parsed. _is\_parameter\_entity_ is true for a parameter entity and false for a general entity.

ExpatError Exceptions[¶](https://docs.python.org/3/library/pyexpat.html#expaterror-exceptions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

[`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
 exceptions have a number of interesting attributes:

ExpatError.code[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.code "Link to this definition")

Expat’s internal error number for the specific error. The [`errors.messages`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.messages "xml.parsers.expat.errors.messages")
 dictionary maps these error numbers to Expat’s error messages. For example:

Copy

from xml.parsers.expat import ParserCreate, ExpatError, errors

p \= ParserCreate()
try:
    p.Parse(some\_xml\_document)
except ExpatError as err:
    print("Error:", errors.messages\[err.code\])

The [`errors`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.errors "xml.parsers.expat.errors")
 module also provides error message constants and a dictionary [`codes`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.codes "xml.parsers.expat.errors.codes")
 mapping these messages back to the error codes, see below.

ExpatError.lineno[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.lineno "Link to this definition")

Line number on which the error was detected. The first line is numbered `1`.

ExpatError.offset[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.offset "Link to this definition")

Character offset into the line where the error occurred. The first column is numbered `0`.

Example[¶](https://docs.python.org/3/library/pyexpat.html#example "Link to this heading")

------------------------------------------------------------------------------------------

The following program defines three handlers that just print out their arguments.

Copy

import xml.parsers.expat

\# 3 handler functions
def start\_element(name, attrs):
    print('Start element:', name, attrs)
def end\_element(name):
    print('End element:', name)
def char\_data(data):
    print('Character data:', repr(data))

p \= xml.parsers.expat.ParserCreate()

p.StartElementHandler \= start\_element
p.EndElementHandler \= end\_element
p.CharacterDataHandler \= char\_data

p.Parse("""<?xml version="1.0"?>
<parent id="top"><child1 name="paul">Text goes here</child1>
<child2 name="fred">More text</child2>
</parent>""", 1)

The output from this program is:

Copy

Start element: parent {'id': 'top'}
Start element: child1 {'name': 'paul'}
Character data: 'Text goes here'
End element: child1
Character data: '\\n'
Start element: child2 {'name': 'fred'}
Character data: 'More text'
End element: child2
Character data: '\\n'
End element: parent

Content Model Descriptions[¶](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.model "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Content models are described using nested tuples. Each tuple contains four values: the type, the quantifier, the name, and a tuple of children. Children are simply additional content model descriptions.

The values of the first two fields are constants defined in the `xml.parsers.expat.model` module. These constants can be collected in two groups: the model type group and the quantifier group.

The constants in the model type group are:

xml.parsers.expat.model.XML\_CTYPE\_ANY[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CTYPE_ANY "Link to this definition")

The element named by the model name was declared to have a content model of `ANY`.

xml.parsers.expat.model.XML\_CTYPE\_CHOICE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CTYPE_CHOICE "Link to this definition")

The named element allows a choice from a number of options; this is used for content models such as `(A | B | C)`.

xml.parsers.expat.model.XML\_CTYPE\_EMPTY[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CTYPE_EMPTY "Link to this definition")

Elements which are declared to be `EMPTY` have this model type.

xml.parsers.expat.model.XML\_CTYPE\_MIXED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CTYPE_MIXED "Link to this definition")

The named element allows character data, optionally interspersed with the named children; this is used for content models such as `(#PCDATA)` and `(#PCDATA | A | B)*`.

xml.parsers.expat.model.XML\_CTYPE\_NAME[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CTYPE_NAME "Link to this definition")

The model names a single element, as for `A`.

xml.parsers.expat.model.XML\_CTYPE\_SEQ[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CTYPE_SEQ "Link to this definition")

Models which represent a series of models which follow one after the other are indicated with this model type. This is used for models such as `(A, B, C)`.

The constants in the quantifier group are:

xml.parsers.expat.model.XML\_CQUANT\_NONE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CQUANT_NONE "Link to this definition")

No modifier is given, so it can appear exactly once, as for `A`.

xml.parsers.expat.model.XML\_CQUANT\_OPT[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CQUANT_OPT "Link to this definition")

The model is optional: it can appear once or not at all, as for `A?`.

xml.parsers.expat.model.XML\_CQUANT\_PLUS[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CQUANT_PLUS "Link to this definition")

The model must occur one or more times (like `A+`).

xml.parsers.expat.model.XML\_CQUANT\_REP[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.model.XML_CQUANT_REP "Link to this definition")

The model must occur zero or more times, as for `A*`.

Expat error constants[¶](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.errors "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

The following constants are provided in the `xml.parsers.expat.errors` module. These constants are useful in interpreting some of the attributes of the `ExpatError` exception objects raised when an error has occurred. Since for backwards compatibility reasons, the constants’ value is the error _message_ and not the numeric error _code_, you do this by comparing its [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.")
 attribute with `errors.codes[errors.XML_ERROR__CONSTANT_NAME_]`.

The `errors` module has the following attributes:

xml.parsers.expat.errors.codes[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.codes "Link to this definition")

A dictionary mapping string descriptions to their error codes.

Added in version 3.2.

xml.parsers.expat.errors.messages[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.messages "Link to this definition")

A dictionary mapping numeric error codes to their string descriptions.

Added in version 3.2.

xml.parsers.expat.errors.XML\_ERROR\_ASYNC\_ENTITY[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_ASYNC_ENTITY "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_ATTRIBUTE\_EXTERNAL\_ENTITY\_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF "Link to this definition")

An entity reference in an attribute value referred to an external entity instead of an internal entity.

xml.parsers.expat.errors.XML\_ERROR\_BAD\_CHAR\_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_BAD_CHAR_REF "Link to this definition")

A character reference referred to a character which is illegal in XML (for example, character `0`, or ‘`&#0;`’).

xml.parsers.expat.errors.XML\_ERROR\_BINARY\_ENTITY\_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_BINARY_ENTITY_REF "Link to this definition")

An entity reference referred to an entity which was declared with a notation, so cannot be parsed.

xml.parsers.expat.errors.XML\_ERROR\_DUPLICATE\_ATTRIBUTE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_DUPLICATE_ATTRIBUTE "Link to this definition")

An attribute was used more than once in a start tag.

xml.parsers.expat.errors.XML\_ERROR\_INCORRECT\_ENCODING[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_INCORRECT_ENCODING "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_INVALID\_TOKEN[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_INVALID_TOKEN "Link to this definition")

Raised when an input byte could not properly be assigned to a character; for example, a NUL byte (value `0`) in a UTF-8 input stream.

xml.parsers.expat.errors.XML\_ERROR\_JUNK\_AFTER\_DOC\_ELEMENT[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_JUNK_AFTER_DOC_ELEMENT "Link to this definition")

Something other than whitespace occurred after the document element.

xml.parsers.expat.errors.XML\_ERROR\_MISPLACED\_XML\_PI[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_MISPLACED_XML_PI "Link to this definition")

An XML declaration was found somewhere other than the start of the input data.

xml.parsers.expat.errors.XML\_ERROR\_NO\_ELEMENTS[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NO_ELEMENTS "Link to this definition")

The document contains no elements (XML requires all documents to contain exactly one top-level element).

xml.parsers.expat.errors.XML\_ERROR\_NO\_MEMORY[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NO_MEMORY "Link to this definition")

Expat was not able to allocate memory internally.

xml.parsers.expat.errors.XML\_ERROR\_PARAM\_ENTITY\_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_PARAM_ENTITY_REF "Link to this definition")

A parameter entity reference was found where it was not allowed.

xml.parsers.expat.errors.XML\_ERROR\_PARTIAL\_CHAR[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_PARTIAL_CHAR "Link to this definition")

An incomplete character was found in the input.

xml.parsers.expat.errors.XML\_ERROR\_RECURSIVE\_ENTITY\_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_RECURSIVE_ENTITY_REF "Link to this definition")

An entity reference contained another reference to the same entity; possibly via a different name, and possibly indirectly.

xml.parsers.expat.errors.XML\_ERROR\_SYNTAX[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_SYNTAX "Link to this definition")

Some unspecified syntax error was encountered.

xml.parsers.expat.errors.XML\_ERROR\_TAG\_MISMATCH[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_TAG_MISMATCH "Link to this definition")

An end tag did not match the innermost open start tag.

xml.parsers.expat.errors.XML\_ERROR\_UNCLOSED\_TOKEN[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNCLOSED_TOKEN "Link to this definition")

Some token (such as a start tag) was not closed before the end of the stream or the next token was encountered.

xml.parsers.expat.errors.XML\_ERROR\_UNDEFINED\_ENTITY[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNDEFINED_ENTITY "Link to this definition")

A reference was made to an entity which was not defined.

xml.parsers.expat.errors.XML\_ERROR\_UNKNOWN\_ENCODING[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNKNOWN_ENCODING "Link to this definition")

The document encoding is not supported by Expat.

xml.parsers.expat.errors.XML\_ERROR\_UNCLOSED\_CDATA\_SECTION[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNCLOSED_CDATA_SECTION "Link to this definition")

A CDATA marked section was not closed.

xml.parsers.expat.errors.XML\_ERROR\_EXTERNAL\_ENTITY\_HANDLING[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_EXTERNAL_ENTITY_HANDLING "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_NOT\_STANDALONE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NOT_STANDALONE "Link to this definition")

The parser determined that the document was not “standalone” though it declared itself to be in the XML declaration, and the `NotStandaloneHandler` was set and returned `0`.

xml.parsers.expat.errors.XML\_ERROR\_UNEXPECTED\_STATE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNEXPECTED_STATE "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_ENTITY\_DECLARED\_IN\_PE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_ENTITY_DECLARED_IN_PE "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_FEATURE\_REQUIRES\_XML\_DTD[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_FEATURE_REQUIRES_XML_DTD "Link to this definition")

An operation was requested that requires DTD support to be compiled in, but Expat was configured without DTD support. This should never be reported by a standard build of the `xml.parsers.expat` module.

xml.parsers.expat.errors.XML\_ERROR\_CANT\_CHANGE\_FEATURE\_ONCE\_PARSING[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING "Link to this definition")

A behavioral change was requested after parsing started that can only be changed before parsing has started. This is (currently) only raised by `UseForeignDTD()`.

xml.parsers.expat.errors.XML\_ERROR\_UNBOUND\_PREFIX[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNBOUND_PREFIX "Link to this definition")

An undeclared prefix was found when namespace processing was enabled.

xml.parsers.expat.errors.XML\_ERROR\_UNDECLARING\_PREFIX[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNDECLARING_PREFIX "Link to this definition")

The document attempted to remove the namespace declaration associated with a prefix.

xml.parsers.expat.errors.XML\_ERROR\_INCOMPLETE\_PE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_INCOMPLETE_PE "Link to this definition")

A parameter entity contained incomplete markup.

xml.parsers.expat.errors.XML\_ERROR\_XML\_DECL[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_XML_DECL "Link to this definition")

There was an error parsing the XML declaration.

xml.parsers.expat.errors.XML\_ERROR\_TEXT\_DECL[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_TEXT_DECL "Link to this definition")

There was an error parsing a text declaration in an external entity.

xml.parsers.expat.errors.XML\_ERROR\_PUBLICID[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_PUBLICID "Link to this definition")

Characters were found in the public id that are not allowed.

xml.parsers.expat.errors.XML\_ERROR\_SUSPENDED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_SUSPENDED "Link to this definition")

The requested operation was made on a suspended parser, but isn’t allowed. This includes attempts to provide additional input or to stop the parser.

xml.parsers.expat.errors.XML\_ERROR\_NOT\_SUSPENDED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NOT_SUSPENDED "Link to this definition")

An attempt to resume the parser was made when the parser had not been suspended.

xml.parsers.expat.errors.XML\_ERROR\_ABORTED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_ABORTED "Link to this definition")

This should not be reported to Python applications.

xml.parsers.expat.errors.XML\_ERROR\_FINISHED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_FINISHED "Link to this definition")

The requested operation was made on a parser which was finished parsing input, but isn’t allowed. This includes attempts to provide additional input or to stop the parser.

xml.parsers.expat.errors.XML\_ERROR\_SUSPEND\_PE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_SUSPEND_PE "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_RESERVED\_PREFIX\_XML[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XML "Link to this definition")

An attempt was made to undeclare reserved namespace prefix `xml` or to bind it to another namespace URI.

xml.parsers.expat.errors.XML\_ERROR\_RESERVED\_PREFIX\_XMLNS[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XMLNS "Link to this definition")

An attempt was made to declare or undeclare reserved namespace prefix `xmlns`.

xml.parsers.expat.errors.XML\_ERROR\_RESERVED\_NAMESPACE\_URI[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_RESERVED_NAMESPACE_URI "Link to this definition")

An attempt was made to bind the URI of one the reserved namespace prefixes `xml` and `xmlns` to another namespace prefix.

xml.parsers.expat.errors.XML\_ERROR\_INVALID\_ARGUMENT[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_INVALID_ARGUMENT "Link to this definition")

This should not be reported to Python applications.

xml.parsers.expat.errors.XML\_ERROR\_NO\_BUFFER[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NO_BUFFER "Link to this definition")

This should not be reported to Python applications.

xml.parsers.expat.errors.XML\_ERROR\_AMPLIFICATION\_LIMIT\_BREACH[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_AMPLIFICATION_LIMIT_BREACH "Link to this definition")

The limit on input amplification factor (from DTD and entities) has been breached.

xml.parsers.expat.errors.XML\_ERROR\_NOT\_STARTED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NOT_STARTED "Link to this definition")

The parser was tried to be stopped or suspended before it started.

Added in version 3.14.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html#)
    *   [XMLParser Objects](https://docs.python.org/3/library/pyexpat.html#xmlparser-objects)
        
    *   [ExpatError Exceptions](https://docs.python.org/3/library/pyexpat.html#expaterror-exceptions)
        
    *   [Example](https://docs.python.org/3/library/pyexpat.html#example)
        
    *   [Content Model Descriptions](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.model)
        
    *   [Expat error constants](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.errors)
        

#### Previous topic

[`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html "previous chapter")

#### Next topic

[Internet Protocols and Support](https://docs.python.org/3/library/internet.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.parsers.expat+%E2%80%94+Fast+XML+parsing+using+Expat&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpyexpat.html&pagesource=library%2Fpyexpat.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/pyexpat.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/internet.html "Internet Protocols and Support")
     |
*   [previous](https://docs.python.org/3/library/xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers")
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
*   [`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html)
    
*    
    
    |
*   Theme Auto Light Dark |