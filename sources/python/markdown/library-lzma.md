### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/zipfile.html "zipfile — Work with ZIP archives")
     |
*   [previous](https://docs.python.org/3/library/bz2.html "bz2 — Support for bzip2 compression")
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
     »
*   [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`lzma` — Compression using the LZMA algorithm[¶](https://docs.python.org/3/library/lzma.html#module-lzma "Link to this heading")

=================================================================================================================================

Added in version 3.3.

**Source code:** [Lib/lzma.py](https://github.com/python/cpython/tree/3.15/Lib/lzma.py)

* * *

This module provides classes and convenience functions for compressing and decompressing data using the LZMA compression algorithm. Also included is a file interface supporting the `.xz` and legacy `.lzma` file formats used by the **xz** utility, as well as raw compressed streams.

The interface provided by this module is very similar to that of the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
 module. Note that [`LZMAFile`](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "lzma.LZMAFile")
 and [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
 are _not_ thread-safe, so if you need to use a single `LZMAFile` instance from multiple threads, it is necessary to protect it with a lock.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module)
. If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements)
.

exception lzma.LZMAError[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMAError "Link to this definition")

This exception is raised when an error occurs during compression or decompression, or while initializing the compressor/decompressor state.

Reading and writing compressed files[¶](https://docs.python.org/3/library/lzma.html#reading-and-writing-compressed-files "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

lzma.open(_filename_, _mode\='rb'_, _\*_, _format\=None_, _check\=\-1_, _preset\=None_, _filters\=None_, _encoding\=None_, _errors\=None_, _newline\=None_)[¶](https://docs.python.org/3/library/lzma.html#lzma.open "Link to this definition")

Open an LZMA-compressed file in binary or text mode, returning a [file object](https://docs.python.org/3/glossary.html#term-file-object)
.

The _filename_ argument can be either an actual file name (given as a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object)
 object), in which case the named file is opened, or it can be an existing file object to read from or write to.

The _mode_ argument can be any of `"r"`, `"rb"`, `"w"`, `"wb"`, `"x"`, `"xb"`, `"a"` or `"ab"` for binary mode, or `"rt"`, `"wt"`, `"xt"`, or `"at"` for text mode. The default is `"rb"`.

When opening a file for reading, the _format_ and _filters_ arguments have the same meanings as for [`LZMADecompressor`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor "lzma.LZMADecompressor")
. In this case, the _check_ and _preset_ arguments should not be used.

When opening a file for writing, the _format_, _check_, _preset_ and _filters_ arguments have the same meanings as for [`LZMACompressor`](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor "lzma.LZMACompressor")
.

For binary mode, this function is equivalent to the [`LZMAFile`](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "lzma.LZMAFile")
 constructor: `LZMAFile(filename, mode, ...)`. In this case, the _encoding_, _errors_ and _newline_ arguments must not be provided.

For text mode, a [`LZMAFile`](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "lzma.LZMAFile")
 object is created, and wrapped in an [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 instance with the specified encoding, error handling behavior, and line ending(s).

Changed in version 3.4: Added support for the `"x"`, `"xb"` and `"xt"` modes.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

class lzma.LZMAFile(_filename\=None_, _mode\='r'_, _\*_, _format\=None_, _check\=\-1_, _preset\=None_, _filters\=None_)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "Link to this definition")

Open an LZMA-compressed file in binary mode.

An `LZMAFile` can wrap an already-open [file object](https://docs.python.org/3/glossary.html#term-file-object)
, or operate directly on a named file. The _filename_ argument specifies either the file object to wrap, or the name of the file to open (as a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object)
 object). When wrapping an existing file object, the wrapped file will not be closed when the `LZMAFile` is closed.

The _mode_ argument can be either `"r"` for reading (default), `"w"` for overwriting, `"x"` for exclusive creation, or `"a"` for appending. These can equivalently be given as `"rb"`, `"wb"`, `"xb"` and `"ab"` respectively.

If _filename_ is a file object (rather than an actual file name), a mode of `"w"` does not truncate the file, and is instead equivalent to `"a"`.

When opening a file for reading, the input file may be the concatenation of multiple separate compressed streams. These are transparently decoded as a single logical stream.

When opening a file for reading, the _format_ and _filters_ arguments have the same meanings as for [`LZMADecompressor`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor "lzma.LZMADecompressor")
. In this case, the _check_ and _preset_ arguments should not be used.

When opening a file for writing, the _format_, _check_, _preset_ and _filters_ arguments have the same meanings as for [`LZMACompressor`](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor "lzma.LZMACompressor")
.

`LZMAFile` supports all the members specified by [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
, except for [`detach()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.detach "io.BufferedIOBase.detach")
 and [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate")
. Iteration and the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement are supported.

The following method and attributes are also provided:

peek(_size\=\-1_)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile.peek "Link to this definition")

Return buffered data without advancing the file position. At least one byte of data will be returned, unless EOF has been reached. The exact number of bytes returned is unspecified (the _size_ argument is ignored).

Note

While calling `peek()` does not change the file position of the `LZMAFile`, it may change the position of the underlying file object (e.g. if the `LZMAFile` was constructed by passing a file object for _filename_).

mode[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile.mode "Link to this definition")

`'rb'` for reading and `'wb'` for writing.

Added in version 3.13.

name[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile.name "Link to this definition")

The lzma file name. Equivalent to the [`name`](https://docs.python.org/3/library/io.html#io.FileIO.name "io.FileIO.name")
 attribute of the underlying [file object](https://docs.python.org/3/glossary.html#term-file-object)
.

Added in version 3.13.

Changed in version 3.4: Added support for the `"x"` and `"xb"` modes.

Changed in version 3.5: The [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read")
 method now accepts an argument of `None`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Compressing and decompressing data in memory[¶](https://docs.python.org/3/library/lzma.html#compressing-and-decompressing-data-in-memory "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

class lzma.LZMACompressor(_format\=FORMAT\_XZ_, _check\=\-1_, _preset\=None_, _filters\=None_)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor "Link to this definition")

Create a compressor object, which can be used to compress data incrementally.

For a more convenient way of compressing a single chunk of data, see [`compress()`](https://docs.python.org/3/library/lzma.html#lzma.compress "lzma.compress")
.

The _format_ argument specifies what container format should be used. Possible values are [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ")
 (the default), [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE")
 and [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW")
.

The _check_ argument specifies the type of integrity check to include in the compressed data. This check is used when decompressing, to ensure that the data has not been corrupted. Possible values are [`CHECK_NONE`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_NONE "lzma.CHECK_NONE")
, [`CHECK_CRC32`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC32 "lzma.CHECK_CRC32")
, [`CHECK_CRC64`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC64 "lzma.CHECK_CRC64")
 (the default for [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ")
) and [`CHECK_SHA256`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_SHA256 "lzma.CHECK_SHA256")
.

If the specified check is not supported, an [`LZMAError`](https://docs.python.org/3/library/lzma.html#lzma.LZMAError "lzma.LZMAError")
 is raised.

The compression settings can be specified either as a preset compression level (with the _preset_ argument), or in detail as a custom filter chain (with the _filters_ argument).

The _preset_ argument (if provided) should be an integer between `0` and `9` (inclusive), optionally OR-ed with the constant [`PRESET_EXTREME`](https://docs.python.org/3/library/lzma.html#lzma.PRESET_EXTREME "lzma.PRESET_EXTREME")
. If neither _preset_ nor _filters_ are given, the default behavior is to use [`PRESET_DEFAULT`](https://docs.python.org/3/library/lzma.html#lzma.PRESET_DEFAULT "lzma.PRESET_DEFAULT")
 (preset level `6`). Higher presets produce smaller output, but make the compression process slower.

Note

In addition to being more CPU-intensive, compression with higher presets also requires much more memory (and produces output that needs more memory to decompress). With preset `9` for example, the overhead for an `LZMACompressor` object can be as high as 800 MiB. For this reason, it is generally best to stick with the default preset.

The _filters_ argument (if provided) should be a filter chain specifier. See [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#filter-chain-specs)
 for details.

compress(_data_)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor.compress "Link to this definition")

Compress _data_ (a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object), returning a `bytes` object containing compressed data for at least part of the input. Some of _data_ may be buffered internally, for use in later calls to `compress()` and [`flush()`](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor.flush "lzma.LZMACompressor.flush")
. The returned data should be concatenated with the output of any previous calls to `compress()`.

flush()[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor.flush "Link to this definition")

Finish the compression process, returning a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object containing any data stored in the compressor’s internal buffers.

The compressor cannot be used after this method has been called.

class lzma.LZMADecompressor(_format\=FORMAT\_AUTO_, _memlimit\=None_, _filters\=None_)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor "Link to this definition")

Create a decompressor object, which can be used to decompress data incrementally.

For a more convenient way of decompressing an entire compressed stream at once, see [`decompress()`](https://docs.python.org/3/library/lzma.html#lzma.decompress "lzma.decompress")
.

The _format_ argument specifies the container format that should be used. The default is [`FORMAT_AUTO`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_AUTO "lzma.FORMAT_AUTO")
, which can decompress both `.xz` and `.lzma` files. Other possible values are [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ")
, [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE")
, and [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW")
.

The _memlimit_ argument specifies a limit (in bytes) on the amount of memory that the decompressor can use. When this argument is used, decompression will fail with an [`LZMAError`](https://docs.python.org/3/library/lzma.html#lzma.LZMAError "lzma.LZMAError")
 if it is not possible to decompress the input within the given memory limit.

The _filters_ argument specifies the filter chain that was used to create the stream being decompressed. This argument is required if _format_ is [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW")
, but should not be used for other formats. See [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#filter-chain-specs)
 for more information about filter chains.

Note

This class does not transparently handle inputs containing multiple compressed streams, unlike [`decompress()`](https://docs.python.org/3/library/lzma.html#lzma.decompress "lzma.decompress")
 and [`LZMAFile`](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "lzma.LZMAFile")
. To decompress a multi-stream input with `LZMADecompressor`, you must create a new decompressor for each stream.

decompress(_data_, _max\_length\=\-1_)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.decompress "Link to this definition")

Decompress _data_ (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
), returning uncompressed data as bytes. Some of _data_ may be buffered internally, for use in later calls to `decompress()`. The returned data should be concatenated with the output of any previous calls to `decompress()`.

If _max\_length_ is nonnegative, returns at most _max\_length_ bytes of decompressed data. If this limit is reached and further output can be produced, the [`needs_input`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.needs_input "lzma.LZMADecompressor.needs_input")
 attribute will be set to `False`. In this case, the next call to `decompress()` may provide _data_ as `b''` to obtain more of the output.

If all of the input data was decompressed and returned (either because this was less than _max\_length_ bytes, or because _max\_length_ was negative), the [`needs_input`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.needs_input "lzma.LZMADecompressor.needs_input")
 attribute will be set to `True`.

Attempting to decompress data after the end of stream is reached raises an [`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
. Any data found after the end of the stream is ignored and saved in the [`unused_data`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.unused_data "lzma.LZMADecompressor.unused_data")
 attribute.

Changed in version 3.5: Added the _max\_length_ parameter.

check[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.check "Link to this definition")

The ID of the integrity check used by the input stream. This may be [`CHECK_UNKNOWN`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_UNKNOWN "lzma.CHECK_UNKNOWN")
 until enough of the input has been decoded to determine what integrity check it uses.

eof[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.eof "Link to this definition")

`True` if the end-of-stream marker has been reached.

unused\_data[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.unused_data "Link to this definition")

Data found after the end of the compressed stream.

Before the end of the stream is reached, this will be `b""`.

needs\_input[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.needs_input "Link to this definition")

`False` if the [`decompress()`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.decompress "lzma.LZMADecompressor.decompress")
 method can provide more decompressed data before requiring new uncompressed input.

Added in version 3.5.

lzma.compress(_data_, _format\=FORMAT\_XZ_, _check\=\-1_, _preset\=None_, _filters\=None_)[¶](https://docs.python.org/3/library/lzma.html#lzma.compress "Link to this definition")

Compress _data_ (a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object), returning the compressed data as a `bytes` object.

See [`LZMACompressor`](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor "lzma.LZMACompressor")
 above for a description of the _format_, _check_, _preset_ and _filters_ arguments.

lzma.decompress(_data_, _format\=FORMAT\_AUTO_, _memlimit\=None_, _filters\=None_)[¶](https://docs.python.org/3/library/lzma.html#lzma.decompress "Link to this definition")

Decompress _data_ (a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object), returning the uncompressed data as a `bytes` object.

If _data_ is the concatenation of multiple distinct compressed streams, decompress all of these streams, and return the concatenation of the results.

See [`LZMADecompressor`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor "lzma.LZMADecompressor")
 above for a description of the _format_, _memlimit_ and _filters_ arguments.

Miscellaneous[¶](https://docs.python.org/3/library/lzma.html#miscellaneous "Link to this heading")

---------------------------------------------------------------------------------------------------

lzma.is\_check\_supported(_check_)[¶](https://docs.python.org/3/library/lzma.html#lzma.is_check_supported "Link to this definition")

Return `True` if the given integrity check is supported on this system.

[`CHECK_NONE`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_NONE "lzma.CHECK_NONE")
 and [`CHECK_CRC32`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC32 "lzma.CHECK_CRC32")
 are always supported. [`CHECK_CRC64`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC64 "lzma.CHECK_CRC64")
 and [`CHECK_SHA256`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_SHA256 "lzma.CHECK_SHA256")
 may be unavailable if you are using a version of **liblzma** that was compiled with a limited feature set.

Specifying custom filter chains[¶](https://docs.python.org/3/library/lzma.html#specifying-custom-filter-chains "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

A filter chain specifier is a sequence of dictionaries, where each dictionary contains the ID and options for a single filter. Each dictionary must contain the key `"id"`, and may contain additional keys to specify filter-dependent options. Valid filter IDs are as follows:

*   Compression filters:
    
    *   [`FILTER_LZMA1`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA1 "lzma.FILTER_LZMA1")
         (for use with [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE")
        )
        
    *   [`FILTER_LZMA2`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA2 "lzma.FILTER_LZMA2")
         (for use with [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ")
         and [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW")
        )
        
*   Delta filter:
    
    *   [`FILTER_DELTA`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_DELTA "lzma.FILTER_DELTA")
        
*   Branch-Call-Jump (BCJ) filters:
    
    *   `FILTER_X86`
        
    *   `FILTER_IA64`
        
    *   `FILTER_ARM`
        
    *   `FILTER_ARMTHUMB`
        
    *   `FILTER_POWERPC`
        
    *   `FILTER_SPARC`
        

A filter chain can consist of up to 4 filters, and cannot be empty. The last filter in the chain must be a compression filter, and any other filters must be delta or BCJ filters.

Compression filters support the following options (specified as additional entries in the dictionary representing the filter):

*   `preset`: A compression preset to use as a source of default values for options that are not specified explicitly.
    
*   `dict_size`: Dictionary size in bytes. This should be between 4 KiB and 1.5 GiB (inclusive).
    
*   `lc`: Number of literal context bits.
    
*   `lp`: Number of literal position bits. The sum `lc + lp` must be at most 4.
    
*   `pb`: Number of position bits; must be at most 4.
    
*   `mode`: [`MODE_FAST`](https://docs.python.org/3/library/lzma.html#lzma.MODE_FAST "lzma.MODE_FAST")
     or [`MODE_NORMAL`](https://docs.python.org/3/library/lzma.html#lzma.MODE_NORMAL "lzma.MODE_NORMAL")
    .
    
*   `nice_len`: What should be considered a “nice length” for a match. This should be 273 or less.
    
*   `mf`: What match finder to use – [`MF_HC3`](https://docs.python.org/3/library/lzma.html#lzma.MF_HC3 "lzma.MF_HC3")
    , [`MF_HC4`](https://docs.python.org/3/library/lzma.html#lzma.MF_HC4 "lzma.MF_HC4")
    , [`MF_BT2`](https://docs.python.org/3/library/lzma.html#lzma.MF_BT2 "lzma.MF_BT2")
    , [`MF_BT3`](https://docs.python.org/3/library/lzma.html#lzma.MF_BT3 "lzma.MF_BT3")
    , or [`MF_BT4`](https://docs.python.org/3/library/lzma.html#lzma.MF_BT4 "lzma.MF_BT4")
    .
    
*   `depth`: Maximum search depth used by match finder. 0 (default) means to select automatically based on other filter options.
    

The delta filter stores the differences between bytes, producing more repetitive input for the compressor in certain circumstances. It supports one option, `dist`. This indicates the distance between bytes to be subtracted. The default is 1, i.e. take the differences between adjacent bytes.

The BCJ filters are intended to be applied to machine code. They convert relative branches, calls and jumps in the code to use absolute addressing, with the aim of increasing the redundancy that can be exploited by the compressor. These filters support one option, `start_offset`. This specifies the address that should be mapped to the beginning of the input data. The default is 0.

Constants[¶](https://docs.python.org/3/library/lzma.html#constants "Link to this heading")

-------------------------------------------------------------------------------------------

The following module-level constants are provided for use as the _format_, _check_, _preset_ and _filters_ arguments of the classes and functions above.

Container formats:

lzma.FORMAT\_XZ[¶](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "Link to this definition")

The `.xz` container format.

lzma.FORMAT\_ALONE[¶](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "Link to this definition")

The legacy `.lzma` container format. This format is more limited than `.xz` – it does not support integrity checks or multiple filters.

lzma.FORMAT\_RAW[¶](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "Link to this definition")

A raw data stream, not using any container format. This format specifier does not support integrity checks, and requires that you always specify a custom filter chain (for both compression and decompression). Additionally, data compressed in this manner cannot be decompressed using [`FORMAT_AUTO`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_AUTO "lzma.FORMAT_AUTO")
.

lzma.FORMAT\_AUTO[¶](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_AUTO "Link to this definition")

Used for decompression only. The container format is detected automatically, so that both `.xz` and `.lzma` files can be decompressed.

Integrity checks:

lzma.CHECK\_NONE[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_NONE "Link to this definition")

No integrity check. This is the default (and the only acceptable value) for [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE")
 and [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW")
.

lzma.CHECK\_CRC32[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC32 "Link to this definition")

A 32-bit Cyclic Redundancy Check.

lzma.CHECK\_CRC64[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC64 "Link to this definition")

A 64-bit Cyclic Redundancy Check. This is the default for [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ")
.

lzma.CHECK\_SHA256[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_SHA256 "Link to this definition")

A 256-bit Secure Hash Algorithm.

lzma.CHECK\_UNKNOWN[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_UNKNOWN "Link to this definition")

The integrity check used by a stream could not yet be determined. This may be the value of the [`LZMADecompressor.check`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.check "lzma.LZMADecompressor.check")
 attribute until enough of the input has been decoded.

lzma.CHECK\_ID\_MAX[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_ID_MAX "Link to this definition")

The largest supported integrity-check ID.

Compression presets:

lzma.PRESET\_DEFAULT[¶](https://docs.python.org/3/library/lzma.html#lzma.PRESET_DEFAULT "Link to this definition")

The default compression preset, equivalent to preset level `6`.

lzma.PRESET\_EXTREME[¶](https://docs.python.org/3/library/lzma.html#lzma.PRESET_EXTREME "Link to this definition")

A flag that may be bitwise OR-ed with a preset level (`0` to `9`) to select a slower but more thorough variant of that preset.

Filter IDs and options:

lzma.FILTER\_LZMA1[¶](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA1 "Link to this definition")

lzma.FILTER\_LZMA2[¶](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA2 "Link to this definition")

The LZMA1 and LZMA2 compression filters. [`FILTER_LZMA1`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA1 "lzma.FILTER_LZMA1")
 is for use with [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE")
, while [`FILTER_LZMA2`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA2 "lzma.FILTER_LZMA2")
 is for use with [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ")
 and [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW")
.

lzma.FILTER\_DELTA[¶](https://docs.python.org/3/library/lzma.html#lzma.FILTER_DELTA "Link to this definition")

The delta filter.

lzma.MODE\_FAST[¶](https://docs.python.org/3/library/lzma.html#lzma.MODE_FAST "Link to this definition")

lzma.MODE\_NORMAL[¶](https://docs.python.org/3/library/lzma.html#lzma.MODE_NORMAL "Link to this definition")

Compression modes that may be used as the `mode` option of a filter specifier (see [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#filter-chain-specs)
).

lzma.MF\_HC3[¶](https://docs.python.org/3/library/lzma.html#lzma.MF_HC3 "Link to this definition")

lzma.MF\_HC4[¶](https://docs.python.org/3/library/lzma.html#lzma.MF_HC4 "Link to this definition")

lzma.MF\_BT2[¶](https://docs.python.org/3/library/lzma.html#lzma.MF_BT2 "Link to this definition")

lzma.MF\_BT3[¶](https://docs.python.org/3/library/lzma.html#lzma.MF_BT3 "Link to this definition")

lzma.MF\_BT4[¶](https://docs.python.org/3/library/lzma.html#lzma.MF_BT4 "Link to this definition")

Match finders that may be used as the `mf` option of a filter specifier (see [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#filter-chain-specs)
).

Examples[¶](https://docs.python.org/3/library/lzma.html#examples "Link to this heading")

-----------------------------------------------------------------------------------------

Reading in a compressed file:

Copy

import lzma
with lzma.open("file.xz") as f:
    file\_content \= f.read()

Creating a compressed file:

Copy

import lzma
data \= b"Insert Data Here"
with lzma.open("file.xz", "w") as f:
    f.write(data)

Compressing data in memory:

Copy

import lzma
data\_in \= b"Insert Data Here"
data\_out \= lzma.compress(data\_in)

Incremental compression:

Copy

import lzma
lzc \= lzma.LZMACompressor()
out1 \= lzc.compress(b"Some data\\n")
out2 \= lzc.compress(b"Another piece of data\\n")
out3 \= lzc.compress(b"Even more data\\n")
out4 \= lzc.flush()
\# Concatenate all the partial results:
result \= b"".join(\[out1, out2, out3, out4\])

Writing compressed data to an already-open file:

Copy

import lzma
with open("file.xz", "wb") as f:
    f.write(b"This data will not be compressed\\n")
    with lzma.open(f, "w") as lzf:
        lzf.write(b"This \*will\* be compressed\\n")
    f.write(b"Not compressed\\n")

Creating a compressed file using a custom filter chain:

Copy

import lzma
my\_filters \= \[\
    {"id": lzma.FILTER\_DELTA, "dist": 5},\
    {"id": lzma.FILTER\_LZMA2, "preset": 7 | lzma.PRESET\_EXTREME},\
\]
with lzma.open("file.xz", "w", filters\=my\_filters) as f:
    f.write(b"blah blah blah")

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html#)
    *   [Reading and writing compressed files](https://docs.python.org/3/library/lzma.html#reading-and-writing-compressed-files)
        
    *   [Compressing and decompressing data in memory](https://docs.python.org/3/library/lzma.html#compressing-and-decompressing-data-in-memory)
        
    *   [Miscellaneous](https://docs.python.org/3/library/lzma.html#miscellaneous)
        
    *   [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#specifying-custom-filter-chains)
        
    *   [Constants](https://docs.python.org/3/library/lzma.html#constants)
        
    *   [Examples](https://docs.python.org/3/library/lzma.html#examples)
        

#### Previous topic

[`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html "previous chapter")

#### Next topic

[`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=lzma+%E2%80%94+Compression+using+the+LZMA+algorithm&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Flzma.html&pagesource=library%2Flzma.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/lzma.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/zipfile.html "zipfile — Work with ZIP archives")
     |
*   [previous](https://docs.python.org/3/library/bz2.html "bz2 — Support for bzip2 compression")
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
     »
*   [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html)
    
*    
    
    |
*   Theme Auto Light Dark |