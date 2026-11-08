### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/sys.html "Operating System Utilities")
     |
*   [previous](https://docs.python.org/3/c-api/slots.html "Definition slots")
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
    
*    
    
    |
*   Theme Auto Light Dark |

Utilities[¶](https://docs.python.org/3/c-api/utilities.html#utilities "Link to this heading")

==============================================================================================

The functions in this chapter perform various utility tasks, ranging from helping C code be more portable across platforms, using Python modules from C, and parsing function arguments and constructing Python values from C values.

*   [Operating System Utilities](https://docs.python.org/3/c-api/sys.html)
    
*   [System Functions](https://docs.python.org/3/c-api/sys.html#system-functions)
    
*   [Process Control](https://docs.python.org/3/c-api/sys.html#process-control)
    
*   [Importing Modules](https://docs.python.org/3/c-api/import.html)
    
*   [Data marshalling support](https://docs.python.org/3/c-api/marshal.html)
    
*   [Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html)
    *   [Parsing arguments](https://docs.python.org/3/c-api/arg.html#parsing-arguments)
        *   [Strings and buffers](https://docs.python.org/3/c-api/arg.html#strings-and-buffers)
            
        *   [Numbers](https://docs.python.org/3/c-api/arg.html#numbers)
            
        *   [Other objects](https://docs.python.org/3/c-api/arg.html#other-objects)
            
        *   [API Functions](https://docs.python.org/3/c-api/arg.html#api-functions)
            
    *   [Building values](https://docs.python.org/3/c-api/arg.html#building-values)
        
*   [String conversion and formatting](https://docs.python.org/3/c-api/conversion.html)
    
*   [Character classification and conversion](https://docs.python.org/3/c-api/conversion.html#character-classification-and-conversion)
    *   [Bit masks](https://docs.python.org/3/c-api/conversion.html#bit-masks)
        
*   [PyHash API](https://docs.python.org/3/c-api/hash.html)
    
*   [Reflection](https://docs.python.org/3/c-api/reflection.html)
    
*   [Codec registry and support functions](https://docs.python.org/3/c-api/codec.html)
    *   [Codec lookup API](https://docs.python.org/3/c-api/codec.html#codec-lookup-api)
        
    *   [Registry API for Unicode encoding error handlers](https://docs.python.org/3/c-api/codec.html#registry-api-for-unicode-encoding-error-handlers)
        
    *   [Codec utility variables](https://docs.python.org/3/c-api/codec.html#codec-utility-variables)
        
*   [PyTime C API](https://docs.python.org/3/c-api/time.html)
    *   [Types](https://docs.python.org/3/c-api/time.html#types)
        
    *   [Clock Functions](https://docs.python.org/3/c-api/time.html#clock-functions)
        
    *   [Raw Clock Functions](https://docs.python.org/3/c-api/time.html#raw-clock-functions)
        
    *   [Conversion functions](https://docs.python.org/3/c-api/time.html#conversion-functions)
        
*   [Support for Perf Maps](https://docs.python.org/3/c-api/perfmaps.html)
    
*   [Expat C API](https://docs.python.org/3/c-api/pyexpat.html)
    

#### Previous topic

[Definition slots](https://docs.python.org/3/c-api/slots.html "previous chapter")

#### Next topic

[Operating System Utilities](https://docs.python.org/3/c-api/sys.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Futilities.html&pagesource=c-api%2Futilities.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/utilities.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/sys.html "Operating System Utilities")
     |
*   [previous](https://docs.python.org/3/c-api/slots.html "Definition slots")
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
    
*    
    
    |
*   Theme Auto Light Dark |