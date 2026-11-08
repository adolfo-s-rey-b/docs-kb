### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/zipimport.html "zipimport — Import modules from Zip archives")
     |
*   [previous](https://docs.python.org/3/library/codeop.html "codeop — Compile Python code")
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
*   [Importing Modules](https://docs.python.org/3/library/modules.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Importing Modules[¶](https://docs.python.org/3/library/modules.html#importing-modules "Link to this heading")

==============================================================================================================

The modules described in this chapter provide new ways to import other Python modules and hooks for customizing the import process.

The full list of modules described in this chapter is:

*   [`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html)
    *   [zipimporter Objects](https://docs.python.org/3/library/zipimport.html#zipimporter-objects)
        
    *   [Examples](https://docs.python.org/3/library/zipimport.html#examples)
        
*   [`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html)
    
*   [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html)
    *   [Example usage of `ModuleFinder`](https://docs.python.org/3/library/modulefinder.html#example-usage-of-modulefinder)
        
*   [`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html)
    
*   [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html)
    *   [Introduction](https://docs.python.org/3/library/importlib.html#introduction)
        
    *   [Functions](https://docs.python.org/3/library/importlib.html#functions)
        
    *   [`importlib.abc` – Abstract base classes related to import](https://docs.python.org/3/library/importlib.html#module-importlib.abc)
        
    *   [`importlib.machinery` – Importers and path hooks](https://docs.python.org/3/library/importlib.html#module-importlib.machinery)
        
    *   [`importlib.util` – Utility code for importers](https://docs.python.org/3/library/importlib.html#module-importlib.util)
        
    *   [Examples](https://docs.python.org/3/library/importlib.html#examples)
        *   [Importing programmatically](https://docs.python.org/3/library/importlib.html#importing-programmatically)
            
        *   [Checking if a module can be imported](https://docs.python.org/3/library/importlib.html#checking-if-a-module-can-be-imported)
            
        *   [Importing a source file directly](https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly)
            
        *   [Implementing lazy imports](https://docs.python.org/3/library/importlib.html#implementing-lazy-imports)
            
        *   [Setting up an importer](https://docs.python.org/3/library/importlib.html#setting-up-an-importer)
            
        *   [Approximating `importlib.import_module()`](https://docs.python.org/3/library/importlib.html#approximating-importlib-import-module)
            
*   [`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html)
    *   [Functional API](https://docs.python.org/3/library/importlib.resources.html#functional-api)
        
*   [`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html)
    
*   [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html)
    *   [Overview](https://docs.python.org/3/library/importlib.metadata.html#overview)
        
    *   [Functional API](https://docs.python.org/3/library/importlib.metadata.html#functional-api)
        *   [Entry points](https://docs.python.org/3/library/importlib.metadata.html#entry-points)
            
        *   [Distribution metadata](https://docs.python.org/3/library/importlib.metadata.html#distribution-metadata)
            
        *   [Distribution versions](https://docs.python.org/3/library/importlib.metadata.html#distribution-versions)
            
        *   [Distribution files](https://docs.python.org/3/library/importlib.metadata.html#distribution-files)
            
        *   [Distribution requirements](https://docs.python.org/3/library/importlib.metadata.html#distribution-requirements)
            
        *   [Mapping import to distribution packages](https://docs.python.org/3/library/importlib.metadata.html#mapping-import-to-distribution-packages)
            
    *   [Distributions](https://docs.python.org/3/library/importlib.metadata.html#distributions)
        
    *   [Distribution Discovery](https://docs.python.org/3/library/importlib.metadata.html#distribution-discovery)
        
    *   [Implementing Custom Providers](https://docs.python.org/3/library/importlib.metadata.html#implementing-custom-providers)
        *   [Example](https://docs.python.org/3/library/importlib.metadata.html#example)
            
*   [The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html)
    *   [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#virtual-environments)
        
    *   [\_pth files](https://docs.python.org/3/library/sys_path_init.html#pth-files)
        
    *   [Embedded Python](https://docs.python.org/3/library/sys_path_init.html#embedded-python)
        

#### Previous topic

[`codeop` — Compile Python code](https://docs.python.org/3/library/codeop.html "previous chapter")

#### Next topic

[`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Importing+Modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmodules.html&pagesource=library%2Fmodules.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/modules.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/zipimport.html "zipimport — Import modules from Zip archives")
     |
*   [previous](https://docs.python.org/3/library/codeop.html "codeop — Compile Python code")
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
*   [Importing Modules](https://docs.python.org/3/library/modules.html)
    
*    
    
    |
*   Theme Auto Light Dark |