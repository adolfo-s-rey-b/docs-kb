### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pathlib.html "pathlib — Object-oriented filesystem paths")
     |
*   [previous](https://docs.python.org/3/library/operator.html "operator — Standard operators as functions")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [File and Directory Access](https://docs.python.org/3/library/filesys.html)
    
*    
    
    |
*   Theme Auto Light Dark |

File and Directory Access[¶](https://docs.python.org/3/library/filesys.html#file-and-directory-access "Link to this heading")

==============================================================================================================================

The modules described in this chapter deal with disk files and directories. For example, there are modules for reading the properties of files, manipulating paths in a portable way, and creating temporary files. The full list of modules in this chapter is:

*   [`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
    *   [Basic use](https://docs.python.org/3/library/pathlib.html#basic-use)
        
    *   [Exceptions](https://docs.python.org/3/library/pathlib.html#exceptions)
        
    *   [Pure paths](https://docs.python.org/3/library/pathlib.html#pure-paths)
        *   [General properties](https://docs.python.org/3/library/pathlib.html#general-properties)
            
        *   [Operators](https://docs.python.org/3/library/pathlib.html#operators)
            
        *   [Accessing individual parts](https://docs.python.org/3/library/pathlib.html#accessing-individual-parts)
            
        *   [Methods and properties](https://docs.python.org/3/library/pathlib.html#methods-and-properties)
            
    *   [Concrete paths](https://docs.python.org/3/library/pathlib.html#concrete-paths)
        *   [Parsing and generating URIs](https://docs.python.org/3/library/pathlib.html#parsing-and-generating-uris)
            
        *   [Expanding and resolving paths](https://docs.python.org/3/library/pathlib.html#expanding-and-resolving-paths)
            
        *   [Querying file type and status](https://docs.python.org/3/library/pathlib.html#querying-file-type-and-status)
            
        *   [Reading and writing files](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files)
            
        *   [Reading directories](https://docs.python.org/3/library/pathlib.html#reading-directories)
            
        *   [Creating files and directories](https://docs.python.org/3/library/pathlib.html#creating-files-and-directories)
            
        *   [Copying, moving and deleting](https://docs.python.org/3/library/pathlib.html#copying-moving-and-deleting)
            
        *   [Permissions and ownership](https://docs.python.org/3/library/pathlib.html#permissions-and-ownership)
            
    *   [Pattern language](https://docs.python.org/3/library/pathlib.html#pattern-language)
        
    *   [Comparison to the `glob` module](https://docs.python.org/3/library/pathlib.html#comparison-to-the-glob-module)
        
    *   [Comparison to the `os` and `os.path` modules](https://docs.python.org/3/library/pathlib.html#comparison-to-the-os-and-os-path-modules)
        *   [Corresponding tools](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
            
    *   [Protocols](https://docs.python.org/3/library/pathlib.html#module-pathlib.types)
        
*   [`os.path` — Common pathname manipulations](https://docs.python.org/3/library/os.path.html)
    
*   [`stat` — Interpreting `stat()` results](https://docs.python.org/3/library/stat.html)
    
*   [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
    *   [The `dircmp` class](https://docs.python.org/3/library/filecmp.html#the-dircmp-class)
        
*   [`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html)
    *   [Examples](https://docs.python.org/3/library/tempfile.html#examples)
        
    *   [Deprecated functions and variables](https://docs.python.org/3/library/tempfile.html#deprecated-functions-and-variables)
        
*   [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
    *   [Examples](https://docs.python.org/3/library/glob.html#examples)
        
*   [`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)
    
*   [`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html)
    
*   [`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html)
    *   [Directory and files operations](https://docs.python.org/3/library/shutil.html#directory-and-files-operations)
        *   [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#platform-dependent-efficient-copy-operations)
            
        *   [copytree example](https://docs.python.org/3/library/shutil.html#copytree-example)
            
        *   [rmtree example](https://docs.python.org/3/library/shutil.html#rmtree-example)
            
    *   [Archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations)
        *   [Archiving example](https://docs.python.org/3/library/shutil.html#archiving-example)
            
        *   [Archiving example with _base\_dir_](https://docs.python.org/3/library/shutil.html#archiving-example-with-base-dir)
            
    *   [Querying the size of the output terminal](https://docs.python.org/3/library/shutil.html#querying-the-size-of-the-output-terminal)
        

See also

Module [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")

Operating system interfaces, including functions to work with files at a lower level than Python [file objects](https://docs.python.org/3/glossary.html#term-file-object)
.

Module [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")

Python’s built-in I/O library, including both abstract classes and some concrete classes such as file I/O.

Built-in function [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")

The standard way to open files for reading and writing with Python.

#### Previous topic

[`operator` — Standard operators as functions](https://docs.python.org/3/library/operator.html "previous chapter")

#### Next topic

[`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page-nojs.html)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/filesys.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pathlib.html "pathlib — Object-oriented filesystem paths")
     |
*   [previous](https://docs.python.org/3/library/operator.html "operator — Standard operators as functions")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [File and Directory Access](https://docs.python.org/3/library/filesys.html)
    
*    
    
    |
*   Theme Auto Light Dark |