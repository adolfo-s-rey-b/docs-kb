### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/compression.html "The compression package")
     |
*   [previous](https://docs.python.org/3/library/sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases")
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
*   [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Data Compression and Archiving[¶](https://docs.python.org/3/library/archiving.html#data-compression-and-archiving "Link to this heading")

==========================================================================================================================================

The modules described in this chapter support data compression with the zlib, gzip, bzip2, lzma, and zstd algorithms, and the creation of ZIP- and tar-format archives. See also [Archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations)
 provided by the [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
 module.

*   [The `compression` package](https://docs.python.org/3/library/compression.html)
    
*   [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html)
    *   [Exceptions](https://docs.python.org/3/library/compression.zstd.html#exceptions)
        
    *   [Reading and writing compressed files](https://docs.python.org/3/library/compression.zstd.html#reading-and-writing-compressed-files)
        
    *   [Compressing and decompressing data in memory](https://docs.python.org/3/library/compression.zstd.html#compressing-and-decompressing-data-in-memory)
        
    *   [Zstandard dictionaries](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries)
        
    *   [Advanced parameter control](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control)
        
    *   [Miscellaneous](https://docs.python.org/3/library/compression.zstd.html#miscellaneous)
        
    *   [Examples](https://docs.python.org/3/library/compression.zstd.html#examples)
        
*   [`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html)
    
*   [`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html)
    *   [Examples of usage](https://docs.python.org/3/library/gzip.html#examples-of-usage)
        
    *   [Command-line interface](https://docs.python.org/3/library/gzip.html#command-line-interface)
        *   [Command-line options](https://docs.python.org/3/library/gzip.html#command-line-options)
            
*   [`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html)
    *   [(De)compression of files](https://docs.python.org/3/library/bz2.html#de-compression-of-files)
        
    *   [Incremental (de)compression](https://docs.python.org/3/library/bz2.html#incremental-de-compression)
        
    *   [One-shot (de)compression](https://docs.python.org/3/library/bz2.html#one-shot-de-compression)
        
    *   [Examples of usage](https://docs.python.org/3/library/bz2.html#examples-of-usage)
        
*   [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html)
    *   [Reading and writing compressed files](https://docs.python.org/3/library/lzma.html#reading-and-writing-compressed-files)
        
    *   [Compressing and decompressing data in memory](https://docs.python.org/3/library/lzma.html#compressing-and-decompressing-data-in-memory)
        
    *   [Miscellaneous](https://docs.python.org/3/library/lzma.html#miscellaneous)
        
    *   [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#specifying-custom-filter-chains)
        
    *   [Constants](https://docs.python.org/3/library/lzma.html#constants)
        
    *   [Examples](https://docs.python.org/3/library/lzma.html#examples)
        
*   [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
    *   [ZipFile objects](https://docs.python.org/3/library/zipfile.html#zipfile-objects)
        
    *   [Path objects](https://docs.python.org/3/library/zipfile.html#path-objects)
        
    *   [PyZipFile objects](https://docs.python.org/3/library/zipfile.html#pyzipfile-objects)
        
    *   [ZipInfo objects](https://docs.python.org/3/library/zipfile.html#zipinfo-objects)
        
    *   [Command-line interface](https://docs.python.org/3/library/zipfile.html#command-line-interface)
        *   [Command-line options](https://docs.python.org/3/library/zipfile.html#command-line-options)
            
    *   [Decompression pitfalls](https://docs.python.org/3/library/zipfile.html#decompression-pitfalls)
        *   [From file itself](https://docs.python.org/3/library/zipfile.html#from-file-itself)
            
        *   [File system limitations](https://docs.python.org/3/library/zipfile.html#file-system-limitations)
            
        *   [Resources limitations](https://docs.python.org/3/library/zipfile.html#resources-limitations)
            
        *   [Interruption](https://docs.python.org/3/library/zipfile.html#interruption)
            
        *   [Default behaviors of extraction](https://docs.python.org/3/library/zipfile.html#default-behaviors-of-extraction)
            
*   [`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html)
    *   [TarFile Objects](https://docs.python.org/3/library/tarfile.html#tarfile-objects)
        
    *   [TarInfo Objects](https://docs.python.org/3/library/tarfile.html#tarinfo-objects)
        
    *   [Extraction filters](https://docs.python.org/3/library/tarfile.html#extraction-filters)
        *   [Default named filters](https://docs.python.org/3/library/tarfile.html#default-named-filters)
            
        *   [Filter errors](https://docs.python.org/3/library/tarfile.html#filter-errors)
            
        *   [Hints for further verification](https://docs.python.org/3/library/tarfile.html#hints-for-further-verification)
            
        *   [Supporting older Python versions](https://docs.python.org/3/library/tarfile.html#supporting-older-python-versions)
            
        *   [Stateful extraction filter example](https://docs.python.org/3/library/tarfile.html#stateful-extraction-filter-example)
            
    *   [Command-Line Interface](https://docs.python.org/3/library/tarfile.html#command-line-interface)
        *   [Command-line options](https://docs.python.org/3/library/tarfile.html#command-line-options)
            
    *   [Examples](https://docs.python.org/3/library/tarfile.html#examples)
        *   [Reading examples](https://docs.python.org/3/library/tarfile.html#reading-examples)
            
        *   [Writing examples](https://docs.python.org/3/library/tarfile.html#writing-examples)
            
    *   [Supported tar formats](https://docs.python.org/3/library/tarfile.html#supported-tar-formats)
        
    *   [Unicode issues](https://docs.python.org/3/library/tarfile.html#unicode-issues)
        

#### Previous topic

[`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html "previous chapter")

#### Next topic

[The `compression` package](https://docs.python.org/3/library/compression.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Data+Compression+and+Archiving&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Farchiving.html&pagesource=library%2Farchiving.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/archiving.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/compression.html "The compression package")
     |
*   [previous](https://docs.python.org/3/library/sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases")
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
*   [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html)
    
*    
    
    |
*   Theme Auto Light Dark |