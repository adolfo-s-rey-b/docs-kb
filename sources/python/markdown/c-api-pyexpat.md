### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/abstract.html "Abstract Objects Layer")
     |
*   [previous](https://docs.python.org/3/c-api/perfmaps.html "Support for Perf Maps")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Expat C API](https://docs.python.org/3/c-api/pyexpat.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Expat C API[¶](https://docs.python.org/3/c-api/pyexpat.html#expat-c-api "Link to this heading")

================================================================================================

The [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.")
 module exposes selected Expat functions through its `expat_CAPI` capsule. This allows extension modules to use the same Expat library as Python. The interface is declared in `pyexpat.h`, which must be included after Expat’s `expat.h` header.

PyExpat\_CAPSULE\_NAME[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPSULE_NAME "Link to this definition")
  

The name of the capsule containing the Expat C API: `"pyexpat.expat_CAPI"`. Pass this to [`PyCapsule_Import()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Import "PyCapsule_Import")
 to obtain a pointer to a [`PyExpat_CAPI`](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI "PyExpat_CAPI")
.

PyExpat\_CAPI\_MAGIC[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI_MAGIC "Link to this definition")
  

The string identifying the layout of [`PyExpat_CAPI`](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI "PyExpat_CAPI")
. Before using the function pointers in the structure, check that its `magic` member compares equal to this string using `strcmp()` and its `size` member is at least sizeof(struct [PyExpat\_CAPI](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI "PyExpat_CAPI")
).

struct PyExpat\_CAPI[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI "Link to this definition")
  

Table of function pointers exported by [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.")
. The capsule owns this structure: treat it as read-only and do not free it. Keep a strong reference to the capsule while using the table.

Check the compatibility fields as described under [`PyExpat_CAPI_MAGIC`](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI_MAGIC "PyExpat_CAPI_MAGIC")
 before using the function pointers.

char \*magic[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.magic "Link to this definition")
  

Interface identifier, set to [`PyExpat_CAPI_MAGIC`](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI_MAGIC "PyExpat_CAPI_MAGIC")
.

int size[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.size "Link to this definition")
  

Size of the structure in bytes, set to `sizeof(struct PyExpat_CAPI)` by the [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.")
 module that created the capsule.

int MAJOR\_VERSION[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.MAJOR_VERSION "Link to this definition")
  

int MINOR\_VERSION[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.MINOR_VERSION "Link to this definition")
  

int MICRO\_VERSION[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.MICRO_VERSION "Link to this definition")
  

Major, minor, and micro version numbers of the Expat library used by [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.")
.

void (\*SetUnknownEncodingHandler)(XML\_Parser parser, XML\_UnknownEncodingHandler handler, void \*encodingHandlerData)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetUnknownEncodingHandler "Link to this definition")
  

Pointer to [XML\_SetUnknownEncodingHandler](https://libexpat.github.io/doc/api/latest/#XML_SetUnknownEncodingHandler)
. The handler may set a Python exception on failure. The caller must check for a Python exception after parsing.

int (\*DefaultUnknownEncodingHandler)(void \*encodingHandlerData, const XML\_Char \*name, XML\_Encoding \*info)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.DefaultUnknownEncodingHandler "Link to this definition")
  

Python’s unknown-encoding handler for Expat, used with `XML_SetUnknownEncodingHandler`. It uses Python’s codec registry to fill _info_. The _encodingHandlerData_ argument is unused. Calling this handler requires an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

Pointers to the corresponding Expat functions, or `NULL` if not available in the Expat version used by [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.")
, are listed below.

Member names omit the `XML_` prefix; for example, `SetHashSalt` exposes Expat’s `XML_SetHashSalt` function. See the [Expat API reference](https://libexpat.github.io/doc/api/latest/)
 for their behavior and the minimum Expat version they appear in.

const XML\_LChar \*(\*ErrorString)(enum XML\_Error code)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.ErrorString "Link to this definition")
  

enum XML\_Error (\*GetErrorCode)(XML\_Parser parser)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.GetErrorCode "Link to this definition")
  

XML\_Size (\*GetErrorColumnNumber)(XML\_Parser parser)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.GetErrorColumnNumber "Link to this definition")
  

XML\_Size (\*GetErrorLineNumber)(XML\_Parser parser)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.GetErrorLineNumber "Link to this definition")
  

enum XML\_Status (\*Parse)(XML\_Parser parser, const char \*s, int len, int isFinal)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.Parse "Link to this definition")
  

XML\_Parser (\*ParserCreate\_MM)(const XML\_Char \*encoding, const XML\_Memory\_Handling\_Suite \*memsuite, const XML\_Char \*namespaceSeparator)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.ParserCreate_MM "Link to this definition")
  

void (\*ParserFree)(XML\_Parser parser)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.ParserFree "Link to this definition")
  

void (\*SetCharacterDataHandler)(XML\_Parser parser, XML\_CharacterDataHandler handler)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetCharacterDataHandler "Link to this definition")
  

void (\*SetCommentHandler)(XML\_Parser parser, XML\_CommentHandler handler)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetCommentHandler "Link to this definition")
  

void (\*SetDefaultHandlerExpand)(XML\_Parser parser, XML\_DefaultHandler handler)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetDefaultHandlerExpand "Link to this definition")
  

void (\*SetElementHandler)(XML\_Parser parser, XML\_StartElementHandler start, XML\_EndElementHandler end)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetElementHandler "Link to this definition")
  

void (\*SetNamespaceDeclHandler)(XML\_Parser parser, XML\_StartNamespaceDeclHandler start, XML\_EndNamespaceDeclHandler end)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetNamespaceDeclHandler "Link to this definition")
  

void (\*SetProcessingInstructionHandler)(XML\_Parser parser, XML\_ProcessingInstructionHandler handler)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetProcessingInstructionHandler "Link to this definition")
  

void (\*SetUserData)(XML\_Parser parser, void \*userData)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetUserData "Link to this definition")
  

void (\*SetStartDoctypeDeclHandler)(XML\_Parser parser, XML\_StartDoctypeDeclHandler start)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetStartDoctypeDeclHandler "Link to this definition")
  

enum XML\_Status (\*SetEncoding)(XML\_Parser parser, const XML\_Char \*encoding)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetEncoding "Link to this definition")
  

int (\*SetHashSalt)(XML\_Parser parser, unsigned long hash\_salt)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetHashSalt "Link to this definition")
  

XML\_Bool (\*SetReparseDeferralEnabled)(XML\_Parser parser, XML\_Bool enabled)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetReparseDeferralEnabled "Link to this definition")
  

XML\_Bool (\*SetAllocTrackerActivationThreshold)(XML\_Parser parser, unsigned long long activationThresholdBytes)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetAllocTrackerActivationThreshold "Link to this definition")
  

XML\_Bool (\*SetAllocTrackerMaximumAmplification)(XML\_Parser parser, float maxAmplificationFactor)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetAllocTrackerMaximumAmplification "Link to this definition")
  

XML\_Bool (\*SetBillionLaughsAttackProtectionActivationThreshold)(XML\_Parser parser, unsigned long long activationThresholdBytes)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetBillionLaughsAttackProtectionActivationThreshold "Link to this definition")
  

XML\_Bool (\*SetBillionLaughsAttackProtectionMaximumAmplification)(XML\_Parser parser, float maxAmplificationFactor)[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetBillionLaughsAttackProtectionMaximumAmplification "Link to this definition")
  

XML\_Bool (\*SetHashSalt16Bytes)(XML\_Parser parser, const uint8\_t entropy\[16\])[¶](https://docs.python.org/3/c-api/pyexpat.html#c.PyExpat_CAPI.SetHashSalt16Bytes "Link to this definition")
  

See the [Expat API reference](https://libexpat.github.io/doc/api/latest/)
.

#### Previous topic

[Support for Perf Maps](https://docs.python.org/3/c-api/perfmaps.html "previous chapter")

#### Next topic

[Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Expat+C+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fpyexpat.html&pagesource=c-api%2Fpyexpat.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/pyexpat.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/abstract.html "Abstract Objects Layer")
     |
*   [previous](https://docs.python.org/3/c-api/perfmaps.html "Support for Perf Maps")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Expat C API](https://docs.python.org/3/c-api/pyexpat.html)
    
*    
    
    |
*   Theme Auto Light Dark |