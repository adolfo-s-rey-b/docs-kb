### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/ast.html "ast — Abstract syntax trees")
     |
*   [previous](https://docs.python.org/3/library/sys_path_init.html "The initialization of the sys.path module search path")
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
*   [Python Language Services](https://docs.python.org/3/library/language.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Python Language Services[¶](https://docs.python.org/3/library/language.html#python-language-services "Link to this heading")

=============================================================================================================================

Python provides a number of modules to assist in working with the Python language. These modules support tokenizing, parsing, syntax analysis, bytecode disassembly, and various other facilities.

These modules include:

*   [`ast` — Abstract syntax trees](https://docs.python.org/3/library/ast.html)
    *   [Abstract grammar](https://docs.python.org/3/library/ast.html#abstract-grammar)
        
    *   [Node classes](https://docs.python.org/3/library/ast.html#node-classes)
        *   [Root nodes](https://docs.python.org/3/library/ast.html#root-nodes)
            
        *   [Literals](https://docs.python.org/3/library/ast.html#literals)
            
        *   [Variables](https://docs.python.org/3/library/ast.html#variables)
            
        *   [Expressions](https://docs.python.org/3/library/ast.html#expressions)
            *   [Subscripting](https://docs.python.org/3/library/ast.html#subscripting)
                
            *   [Comprehensions](https://docs.python.org/3/library/ast.html#comprehensions)
                
        *   [Statements](https://docs.python.org/3/library/ast.html#statements)
            *   [Imports](https://docs.python.org/3/library/ast.html#imports)
                
        *   [Control flow](https://docs.python.org/3/library/ast.html#control-flow)
            
        *   [Pattern matching](https://docs.python.org/3/library/ast.html#pattern-matching)
            
        *   [Type annotations](https://docs.python.org/3/library/ast.html#type-annotations)
            
        *   [Type parameters](https://docs.python.org/3/library/ast.html#type-parameters)
            
        *   [Function and class definitions](https://docs.python.org/3/library/ast.html#function-and-class-definitions)
            
        *   [Async and await](https://docs.python.org/3/library/ast.html#async-and-await)
            
    *   [`ast` helpers](https://docs.python.org/3/library/ast.html#ast-helpers)
        
    *   [Compiler flags](https://docs.python.org/3/library/ast.html#compiler-flags)
        
    *   [Command-line usage](https://docs.python.org/3/library/ast.html#command-line-usage)
        
*   [`symtable` — Access to the compiler’s symbol tables](https://docs.python.org/3/library/symtable.html)
    *   [Generating Symbol Tables](https://docs.python.org/3/library/symtable.html#generating-symbol-tables)
        
    *   [Examining Symbol Tables](https://docs.python.org/3/library/symtable.html#examining-symbol-tables)
        
    *   [Command-Line Usage](https://docs.python.org/3/library/symtable.html#command-line-usage)
        
*   [`token` — Constants used with Python parse trees](https://docs.python.org/3/library/token.html)
    
*   [`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html)
    
*   [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)
    *   [Tokenizing input](https://docs.python.org/3/library/tokenize.html#tokenizing-input)
        
    *   [Command-line usage](https://docs.python.org/3/library/tokenize.html#command-line-usage)
        
    *   [Examples](https://docs.python.org/3/library/tokenize.html#examples)
        
*   [`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/3/library/tabnanny.html)
    
*   [`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html)
    *   [Function Objects](https://docs.python.org/3/library/pyclbr.html#function-objects)
        
    *   [Class Objects](https://docs.python.org/3/library/pyclbr.html#class-objects)
        
*   [`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html)
    *   [Command-Line Interface](https://docs.python.org/3/library/py_compile.html#command-line-interface)
        
*   [`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html)
    *   [Command-line use](https://docs.python.org/3/library/compileall.html#command-line-use)
        
    *   [Public functions](https://docs.python.org/3/library/compileall.html#public-functions)
        
*   [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
    *   [Command-line interface](https://docs.python.org/3/library/dis.html#command-line-interface)
        
    *   [Bytecode analysis](https://docs.python.org/3/library/dis.html#bytecode-analysis)
        
    *   [Analysis functions](https://docs.python.org/3/library/dis.html#analysis-functions)
        
    *   [Python Bytecode Instructions](https://docs.python.org/3/library/dis.html#python-bytecode-instructions)
        
    *   [Opcode collections](https://docs.python.org/3/library/dis.html#opcode-collections)
        
*   [`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html)
    *   [Command-line usage](https://docs.python.org/3/library/pickletools.html#command-line-usage)
        *   [Command-line options](https://docs.python.org/3/library/pickletools.html#command-line-options)
            
    *   [Programmatic interface](https://docs.python.org/3/library/pickletools.html#programmatic-interface)
        

#### Previous topic

[The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html "previous chapter")

#### Next topic

[`ast` — Abstract syntax trees](https://docs.python.org/3/library/ast.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python+Language+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Flanguage.html&pagesource=library%2Flanguage.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/language.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/ast.html "ast — Abstract syntax trees")
     |
*   [previous](https://docs.python.org/3/library/sys_path_init.html "The initialization of the sys.path module search path")
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
*   [Python Language Services](https://docs.python.org/3/library/language.html)
    
*    
    
    |
*   Theme Auto Light Dark |