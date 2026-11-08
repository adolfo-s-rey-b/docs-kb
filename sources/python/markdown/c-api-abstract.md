### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/object.html "Object Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/pyexpat.html "Expat C API")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Abstract Objects Layer[¶](https://docs.python.org/3/c-api/abstract.html#abstract-objects-layer "Link to this heading")

=======================================================================================================================

The functions in this chapter interact with Python objects regardless of their type, or with wide classes of object types (e.g. all numerical types, or all sequence types). When used on object types for which they do not apply, they will raise a Python exception.

It is not possible to use these functions on objects that are not properly initialized, such as a list object that has been created by [`PyList_New()`](https://docs.python.org/3/c-api/list.html#c.PyList_New "PyList_New")
, but whose items have not been set to some non-`NULL` value yet.

*   [Object Protocol](https://docs.python.org/3/c-api/object.html)
    
*   [Call Protocol](https://docs.python.org/3/c-api/call.html)
    *   [The _tp\_call_ Protocol](https://docs.python.org/3/c-api/call.html#the-tp-call-protocol)
        
    *   [The Vectorcall Protocol](https://docs.python.org/3/c-api/call.html#the-vectorcall-protocol)
        *   [Recursion Control](https://docs.python.org/3/c-api/call.html#recursion-control)
            
        *   [Vectorcall Support API](https://docs.python.org/3/c-api/call.html#vectorcall-support-api)
            
    *   [Object Calling API](https://docs.python.org/3/c-api/call.html#object-calling-api)
        
    *   [Call Support API](https://docs.python.org/3/c-api/call.html#call-support-api)
        
*   [Number Protocol](https://docs.python.org/3/c-api/number.html)
    
*   [Sequence Protocol](https://docs.python.org/3/c-api/sequence.html)
    
*   [Mapping Protocol](https://docs.python.org/3/c-api/mapping.html)
    
*   [Iterator Protocol](https://docs.python.org/3/c-api/iter.html)
    
*   [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html)
    *   [Buffer structure](https://docs.python.org/3/c-api/buffer.html#buffer-structure)
        
    *   [Buffer request types](https://docs.python.org/3/c-api/buffer.html#buffer-request-types)
        *   [request-independent fields](https://docs.python.org/3/c-api/buffer.html#request-independent-fields)
            
        *   [readonly, format](https://docs.python.org/3/c-api/buffer.html#readonly-format)
            
        *   [shape, strides, suboffsets](https://docs.python.org/3/c-api/buffer.html#shape-strides-suboffsets)
            
        *   [contiguity requests](https://docs.python.org/3/c-api/buffer.html#contiguity-requests)
            
        *   [compound requests](https://docs.python.org/3/c-api/buffer.html#compound-requests)
            
    *   [Complex arrays](https://docs.python.org/3/c-api/buffer.html#complex-arrays)
        *   [NumPy-style: shape and strides](https://docs.python.org/3/c-api/buffer.html#numpy-style-shape-and-strides)
            
        *   [PIL-style: shape, strides and suboffsets](https://docs.python.org/3/c-api/buffer.html#pil-style-shape-strides-and-suboffsets)
            
    *   [Buffer-related functions](https://docs.python.org/3/c-api/buffer.html#buffer-related-functions)
        

#### Previous topic

[Expat C API](https://docs.python.org/3/c-api/pyexpat.html "previous chapter")

#### Next topic

[Object Protocol](https://docs.python.org/3/c-api/object.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Abstract+Objects+Layer&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fabstract.html&pagesource=c-api%2Fabstract.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/abstract.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/object.html "Object Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/pyexpat.html "Expat C API")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
    
*    
    
    |
*   Theme Auto Light Dark |