### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/zlib.html "zlib — Compression compatible with gzip")
     |
*   [previous](https://docs.python.org/3/library/compression.html "The compression package")
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
*   [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`compression.zstd` — Compression compatible with the Zstandard format[¶](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "Link to this heading")

=================================================================================================================================================================================

Added in version 3.14.

**Source code:** [Lib/compression/zstd/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.15/Lib/compression/zstd/__init__.py)

* * *

This module provides classes and functions for compressing and decompressing data using the Zstandard (or _zstd_) compression algorithm. The [zstd manual](https://facebook.github.io/zstd/doc/api_manual_latest.html)
 describes Zstandard as “a fast lossless compression algorithm, targeting real-time compression scenarios at zlib-level and better compression ratios.” Also included is a file interface that supports reading and writing the contents of `.zst` files created by the **zstd** utility, as well as raw zstd compressed streams.

The `compression.zstd` module contains:

*   The [`open()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.open "compression.zstd.open")
     function and [`ZstdFile`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "compression.zstd.ZstdFile")
     class for reading and writing compressed files.
    
*   The [`ZstdCompressor`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor "compression.zstd.ZstdCompressor")
     and [`ZstdDecompressor`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor "compression.zstd.ZstdDecompressor")
     classes for incremental (de)compression.
    
*   The [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress "compression.zstd.compress")
     and [`decompress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.decompress "compression.zstd.decompress")
     functions for one-shot (de)compression.
    
*   The [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict")
     and [`finalize_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.finalize_dict "compression.zstd.finalize_dict")
     functions and the [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
     class to train and manage Zstandard dictionaries.
    
*   The [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter")
    , [`DecompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "compression.zstd.DecompressionParameter")
    , and [`Strategy`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy "compression.zstd.Strategy")
     classes for setting advanced (de)compression parameters.
    

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module)
. If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements)
.

Exceptions[¶](https://docs.python.org/3/library/compression.zstd.html#exceptions "Link to this heading")

---------------------------------------------------------------------------------------------------------

exception compression.zstd.ZstdError[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdError "Link to this definition")

This exception is raised when an error occurs during compression or decompression, or while initializing the (de)compressor state.

Reading and writing compressed files[¶](https://docs.python.org/3/library/compression.zstd.html#reading-and-writing-compressed-files "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

compression.zstd.open(_file_, _/_, _mode\='rb'_, _\*_, _level\=None_, _options\=None_, _zstd\_dict\=None_, _encoding\=None_, _errors\=None_, _newline\=None_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.open "Link to this definition")

Open a Zstandard-compressed file in binary or text mode, returning a [file object](https://docs.python.org/3/glossary.html#term-file-object)
.

The _file_ argument can be either a file name (given as a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object)
 object), in which case the named file is opened, or it can be an existing file object to read from or write to.

The mode argument can be either `'rb'` for reading (default), `'wb'` for overwriting, `'ab'` for appending, or `'xb'` for exclusive creation. These can equivalently be given as `'r'`, `'w'`, `'a'`, and `'x'` respectively. You may also open in text mode with `'rt'`, `'wt'`, `'at'`, and `'xt'` respectively.

When reading, the _options_ argument can be a dictionary providing advanced decompression parameters; see [`DecompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "compression.zstd.DecompressionParameter")
 for detailed information about supported parameters. The _zstd\_dict_ argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 instance to be used during decompression. When reading, if the _level_ argument is not None, a `TypeError` will be raised.

When writing, the _options_ argument can be a dictionary providing advanced compression parameters; see [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter")
 for detailed information about supported parameters. The _level_ argument is the compression level to use when writing compressed data. Only one of _level_ or _options_ may be non-None. The _zstd\_dict_ argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 instance to be used during compression.

In binary mode, this function is equivalent to the [`ZstdFile`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "compression.zstd.ZstdFile")
 constructor: `ZstdFile(file, mode, ...)`. In this case, the _encoding_, _errors_, and _newline_ parameters must not be provided.

In text mode, a [`ZstdFile`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "compression.zstd.ZstdFile")
 object is created, and wrapped in an [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 instance with the specified encoding, error handling behavior, and line endings.

class compression.zstd.ZstdFile(_file_, _/_, _mode\='rb'_, _\*_, _level\=None_, _options\=None_, _zstd\_dict\=None_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "Link to this definition")

Open a Zstandard-compressed file in binary mode.

A `ZstdFile` can wrap an already-open [file object](https://docs.python.org/3/glossary.html#term-file-object)
, or operate directly on a named file. The _file_ argument specifies either the file object to wrap, or the name of the file to open (as a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object)
 object). If wrapping an existing file object, the wrapped file will not be closed when the `ZstdFile` is closed.

The _mode_ argument can be either `'rb'` for reading (default), `'wb'` for overwriting, `'xb'` for exclusive creation, or `'ab'` for appending. These can equivalently be given as `'r'`, `'w'`, `'x'` and `'a'` respectively.

If _file_ is a file object (rather than an actual file name), a mode of `'w'` does not truncate the file, and is instead equivalent to `'a'`.

When reading, the _options_ argument can be a dictionary providing advanced decompression parameters; see [`DecompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "compression.zstd.DecompressionParameter")
 for detailed information about supported parameters. The _zstd\_dict_ argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 instance to be used during decompression. When reading, if the _level_ argument is not None, a `TypeError` will be raised.

When writing, the _options_ argument can be a dictionary providing advanced compression parameters; see [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter")
 for detailed information about supported parameters. The _level_ argument is the compression level to use when writing compressed data. Only one of _level_ or _options_ may be passed. The _zstd\_dict_ argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 instance to be used during compression.

`ZstdFile` supports all the members specified by [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
, except for [`detach()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.detach "io.BufferedIOBase.detach")
 and [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate")
. Iteration and the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement are supported.

The following method and attributes are also provided:

peek(_size\=\-1_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile.peek "Link to this definition")

Return buffered data without advancing the file position. At least one byte of data will be returned, unless EOF has been reached. The exact number of bytes returned is unspecified (the _size_ argument is ignored).

Note

While calling `peek()` does not change the file position of the `ZstdFile`, it may change the position of the underlying file object (for example, if the `ZstdFile` was constructed by passing a file object for _file_).

mode[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile.mode "Link to this definition")

`'rb'` for reading and `'wb'` for writing.

name[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile.name "Link to this definition")

The name of the Zstandard file. Equivalent to the [`name`](https://docs.python.org/3/library/io.html#io.FileIO.name "io.FileIO.name")
 attribute of the underlying [file object](https://docs.python.org/3/glossary.html#term-file-object)
.

Compressing and decompressing data in memory[¶](https://docs.python.org/3/library/compression.zstd.html#compressing-and-decompressing-data-in-memory "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

compression.zstd.compress(_data_, _level\=None_, _options\=None_, _zstd\_dict\=None_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress "Link to this definition")

Compress _data_ (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
), returning the compressed data as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

The _level_ argument is an integer controlling the level of compression. _level_ is an alternative to setting [`CompressionParameter.compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level")
 in _options_. Use [`bounds()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "compression.zstd.CompressionParameter.bounds")
 on `compression_level` to get the values that can be passed for _level_. If advanced compression options are needed, the _level_ argument must be omitted and in the _options_ dictionary the `CompressionParameter.compression_level` parameter should be set.

The _options_ argument is a Python dictionary containing advanced compression parameters. The valid keys and values for compression parameters are documented as part of the [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter")
 documentation.

The _zstd\_dict_ argument is an instance of [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 containing trained data to improve compression efficiency. The function [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict")
 can be used to generate a Zstandard dictionary.

compression.zstd.decompress(_data_, _zstd\_dict\=None_, _options\=None_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.decompress "Link to this definition")

Decompress _data_ (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
), returning the uncompressed data as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

The _options_ argument is a Python dictionary containing advanced decompression parameters. The valid keys and values for compression parameters are documented as part of the [`DecompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "compression.zstd.DecompressionParameter")
 documentation.

The _zstd\_dict_ argument is an instance of [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 containing trained data used during compression. This must be the same Zstandard dictionary used during compression.

If _data_ is the concatenation of multiple distinct compressed frames, decompress all of these frames, and return the concatenation of the results.

class compression.zstd.ZstdCompressor(_level\=None_, _options\=None_, _zstd\_dict\=None_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor "Link to this definition")

Create a compressor object, which can be used to compress data incrementally.

For a more convenient way of compressing a single chunk of data, see the module-level function [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress "compression.zstd.compress")
.

The _level_ argument is an integer controlling the level of compression. _level_ is an alternative to setting [`CompressionParameter.compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level")
 in _options_. Use [`bounds()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "compression.zstd.CompressionParameter.bounds")
 on `compression_level` to get the values that can be passed for _level_. If advanced compression options are needed, the _level_ argument must be omitted and in the _options_ dictionary the `CompressionParameter.compression_level` parameter should be set.

The _options_ argument is a Python dictionary containing advanced compression parameters. The valid keys and values for compression parameters are documented as part of the [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter")
 documentation.

The _zstd\_dict_ argument is an optional instance of [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 containing trained data to improve compression efficiency. The function [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict")
 can be used to generate a Zstandard dictionary.

compress(_data_, _mode\=ZstdCompressor.CONTINUE_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "Link to this definition")

Compress _data_ (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
), returning a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object with compressed data if possible, or otherwise an empty `bytes` object. Some of _data_ may be buffered internally, for use in later calls to `compress()` and [`flush()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.flush "compression.zstd.ZstdCompressor.flush")
. The returned data should be concatenated with the output of any previous calls to `compress()`.

The _mode_ argument is a `ZstdCompressor` attribute, either [`CONTINUE`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.CONTINUE "compression.zstd.ZstdCompressor.CONTINUE")
, [`FLUSH_BLOCK`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_BLOCK "compression.zstd.ZstdCompressor.FLUSH_BLOCK")
, or [`FLUSH_FRAME`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "compression.zstd.ZstdCompressor.FLUSH_FRAME")
.

When all data has been provided to the compressor, call the [`flush()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.flush "compression.zstd.ZstdCompressor.flush")
 method to finish the compression process. If `compress()` is called with _mode_ set to [`FLUSH_FRAME`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "compression.zstd.ZstdCompressor.FLUSH_FRAME")
, `flush()` should not be called, as it would write out a new empty frame.

flush(_mode\=ZstdCompressor.FLUSH\_FRAME_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.flush "Link to this definition")

Finish the compression process, returning a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object containing any data stored in the compressor’s internal buffers.

The _mode_ argument is a `ZstdCompressor` attribute, either [`FLUSH_BLOCK`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_BLOCK "compression.zstd.ZstdCompressor.FLUSH_BLOCK")
, or [`FLUSH_FRAME`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "compression.zstd.ZstdCompressor.FLUSH_FRAME")
.

set\_pledged\_input\_size(_size_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.set_pledged_input_size "Link to this definition")

Specify the amount of uncompressed data _size_ that will be provided for the next frame. _size_ will be written into the frame header of the next frame unless [`CompressionParameter.content_size_flag`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.content_size_flag "compression.zstd.CompressionParameter.content_size_flag")
 is `False` or `0`. A size of `0` means that the frame is empty. If _size_ is `None`, the frame header will omit the frame size. Frames that include the uncompressed data size require less memory to decompress, especially at higher compression levels.

If [`last_mode`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.last_mode "compression.zstd.ZstdCompressor.last_mode")
 is not [`FLUSH_FRAME`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "compression.zstd.ZstdCompressor.FLUSH_FRAME")
, a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised as the compressor is not at the start of a frame. If the pledged size does not match the actual size of data provided to [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress")
, future calls to `compress()` or [`flush()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.flush "compression.zstd.ZstdCompressor.flush")
 may raise [`ZstdError`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdError "compression.zstd.ZstdError")
 and the last chunk of data may be lost.

After [`flush()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.flush "compression.zstd.ZstdCompressor.flush")
 or [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress")
 are called with mode [`FLUSH_FRAME`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "compression.zstd.ZstdCompressor.FLUSH_FRAME")
, the next frame will not include the frame size into the header unless `set_pledged_input_size()` is called again.

CONTINUE[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.CONTINUE "Link to this definition")

Collect more data for compression, which may or may not generate output immediately. This mode optimizes the compression ratio by maximizing the amount of data per block and frame.

FLUSH\_BLOCK[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_BLOCK "Link to this definition")

Complete and write a block to the data stream. The data returned so far can be immediately decompressed. Past data can still be referenced in future blocks generated by calls to [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress")
, improving compression.

FLUSH\_FRAME[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "Link to this definition")

Complete and write out a frame. Future data provided to [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress")
 will be written into a new frame and _cannot_ reference past data.

last\_mode[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.last_mode "Link to this definition")

The last mode passed to either [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress")
 or [`flush()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.flush "compression.zstd.ZstdCompressor.flush")
. The value can be one of [`CONTINUE`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.CONTINUE "compression.zstd.ZstdCompressor.CONTINUE")
, [`FLUSH_BLOCK`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_BLOCK "compression.zstd.ZstdCompressor.FLUSH_BLOCK")
, or [`FLUSH_FRAME`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "compression.zstd.ZstdCompressor.FLUSH_FRAME")
. The initial value is `FLUSH_FRAME`, signifying that the compressor is at the start of a new frame.

class compression.zstd.ZstdDecompressor(_zstd\_dict\=None_, _options\=None_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor "Link to this definition")

Create a decompressor object, which can be used to decompress data incrementally.

For a more convenient way of decompressing an entire compressed stream at once, see the module-level function [`decompress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.decompress "compression.zstd.decompress")
.

The _options_ argument is a Python dictionary containing advanced decompression parameters. The valid keys and values for compression parameters are documented as part of the [`DecompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "compression.zstd.DecompressionParameter")
 documentation.

The _zstd\_dict_ argument is an instance of [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 containing trained data used during compression. This must be the same Zstandard dictionary used during compression.

Note

This class does not transparently handle inputs containing multiple compressed frames, unlike the [`decompress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.decompress "compression.zstd.decompress")
 function and [`ZstdFile`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "compression.zstd.ZstdFile")
 class. To decompress a multi-frame input, you should use `decompress()`, `ZstdFile` if working with a [file object](https://docs.python.org/3/glossary.html#term-file-object)
, or multiple `ZstdDecompressor` instances.

decompress(_data_, _max\_length\=\-1_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor.decompress "Link to this definition")

Decompress _data_ (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
), returning uncompressed data as bytes. Some of _data_ may be buffered internally, for use in later calls to `decompress()`. The returned data should be concatenated with the output of any previous calls to `decompress()`.

If _max\_length_ is non-negative, the method returns at most _max\_length_ bytes of decompressed data. If this limit is reached and further output can be produced (or EOF is reached), the [`needs_input`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor.needs_input "compression.zstd.ZstdDecompressor.needs_input")
 attribute will be set to `False`. In this case, the next call to `decompress()` may provide _data_ as `b''` to obtain more of the output. The full content can thus be read like:

Copy

process\_output(d.decompress(data, max\_length))
while not d.eof and not d.needs\_input:
    process\_output(d.decompress(b"", max\_length))

If all of the input data was decompressed and returned (either because this was less than _max\_length_ bytes, or because _max\_length_ was negative), the [`needs_input`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor.needs_input "compression.zstd.ZstdDecompressor.needs_input")
 attribute will be set to `True`.

Attempting to decompress data after the end of a frame will raise a [`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
. Any data found after the end of the frame is ignored and saved in the [`unused_data`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor.unused_data "compression.zstd.ZstdDecompressor.unused_data")
 attribute.

eof[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor.eof "Link to this definition")

`True` if the end-of-stream marker has been reached.

unused\_data[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor.unused_data "Link to this definition")

Data found after the end of the compressed stream.

Before the end of the stream is reached, this will be `b''`.

needs\_input[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor.needs_input "Link to this definition")

`False` if the [`decompress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor.decompress "compression.zstd.ZstdDecompressor.decompress")
 method can provide more decompressed data before requiring new compressed input.

Zstandard dictionaries[¶](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

compression.zstd.train\_dict(_samples_, _dict\_size_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "Link to this definition")

Train a Zstandard dictionary, returning a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 instance. Zstandard dictionaries enable more efficient compression of smaller sizes of data, which is traditionally difficult to compress due to less repetition. If you are compressing multiple similar groups of data (such as similar files), Zstandard dictionaries can improve compression ratios and speed significantly.

The _samples_ argument (an iterable of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 objects), is the population of samples used to train the Zstandard dictionary.

The _dict\_size_ argument, an integer, is the maximum size (in bytes) the Zstandard dictionary should be. The Zstandard documentation suggests an absolute maximum of no more than 100 KB, but the maximum can often be smaller depending on the data. Larger dictionaries generally slow down compression, but improve compression ratios. Smaller dictionaries lead to faster compression, but reduce the compression ratio.

compression.zstd.finalize\_dict(_zstd\_dict_, _/_, _samples_, _dict\_size_, _level_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.finalize_dict "Link to this definition")

An advanced function for converting a “raw content” Zstandard dictionary into a regular Zstandard dictionary. “Raw content” dictionaries are a sequence of bytes that do not need to follow the structure of a normal Zstandard dictionary.

The _zstd\_dict_ argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
 instance with the [`dict_content`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.dict_content "compression.zstd.ZstdDict.dict_content")
 containing the raw dictionary contents.

The _samples_ argument (an iterable of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 objects), contains sample data for generating the Zstandard dictionary.

The _dict\_size_ argument, an integer, is the maximum size (in bytes) the Zstandard dictionary should be. See [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict")
 for suggestions on the maximum dictionary size.

The _level_ argument (an integer) is the compression level expected to be passed to the compressors using this dictionary. The dictionary information varies for each compression level, so tuning for the proper compression level can make compression more efficient.

class compression.zstd.ZstdDict(_dict\_content_, _/_, _\*_, _is\_raw\=False_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "Link to this definition")

A wrapper around Zstandard dictionaries. Dictionaries can be used to improve the compression of many small chunks of data. Use [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict")
 if you need to train a new dictionary from sample data.

The _dict\_content_ argument (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
), is the already trained dictionary information.

The _is\_raw_ argument, a boolean, is an advanced parameter controlling the meaning of _dict\_content_. `True` means _dict\_content_ is a “raw content” dictionary, without any format restrictions. `False` means _dict\_content_ is an ordinary Zstandard dictionary, created from Zstandard functions, for example, [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict")
 or the external **zstd** CLI.

When passing a `ZstdDict` to a function, the `as_digested_dict` and `as_undigested_dict` attributes can control how the dictionary is loaded by passing them as the `zstd_dict` argument, for example, `compress(data, zstd_dict=zd.as_digested_dict)`. Digesting a dictionary is a costly operation that occurs when loading a Zstandard dictionary. When making multiple calls to compression or decompression, passing a digested dictionary will reduce the overhead of loading the dictionary.

> |     |     |     |
> | --- | --- | --- |Difference for compression[¶](https://docs.python.org/3/library/compression.zstd.html#id1 "Link to this table")
>    
> |     | Digested dictionary | Undigested dictionary |
> | --- | --- | --- |
> | Advanced parameters of the compressor which may be overridden by the dictionary’s parameters | `window_log`, `hash_log`, `chain_log`, `search_log`, `min_match`, `target_length`, `strategy`, `enable_long_distance_matching`, `ldm_hash_log`, `ldm_min_match`, `ldm_bucket_size_log`, `ldm_hash_rate_log`, and some non-public parameters. | None |
> | `ZstdDict` internally caches the dictionary | Yes. It’s faster when loading a digested dictionary again with the same compression level. | No. If you wish to load an undigested dictionary multiple times, consider reusing a compressor object. |

If passing a `ZstdDict` without any attribute, an undigested dictionary is passed by default when compressing and a digested dictionary is generated if necessary and passed by default when decompressing.

> dict\_content[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.dict_content "Link to this definition")
> 
> The content of the Zstandard dictionary, a `bytes` object. It’s the same as the _dict\_content_ argument in the `__init__` method. It can be used with other programs, such as the `zstd` CLI program.
> 
> dict\_id[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.dict_id "Link to this definition")
> 
> Identifier of the Zstandard dictionary, a non-negative int value.
> 
> Non-zero means the dictionary is ordinary, created by Zstandard functions and following the Zstandard format.
> 
> `0` means a “raw content” dictionary, free of any format restriction, used for advanced users.
> 
> Note
> 
> The meaning of `0` for `ZstdDict.dict_id` is different from the `dictionary_id` attribute to the [`get_frame_info()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.get_frame_info "compression.zstd.get_frame_info")
>  function.
> 
> as\_digested\_dict[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.as_digested_dict "Link to this definition")
> 
> Load as a digested dictionary.
> 
> as\_undigested\_dict[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.as_undigested_dict "Link to this definition")
> 
> Load as an undigested dictionary.

Advanced parameter control[¶](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

class compression.zstd.CompressionParameter[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "Link to this definition")

An [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum")
 containing the advanced compression parameter keys that can be used when compressing data.

The [`bounds()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "compression.zstd.CompressionParameter.bounds")
 method can be used on any attribute to get the valid values for that parameter.

Parameters are optional; any omitted parameter will have its value selected automatically.

Example getting the lower and upper bound of [`compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level")
:

Copy

lower, upper \= CompressionParameter.compression\_level.bounds()

Example setting the [`window_log`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.window_log "compression.zstd.CompressionParameter.window_log")
 to the maximum size:

Copy

\_lower, upper \= CompressionParameter.window\_log.bounds()
options \= {CompressionParameter.window\_log: upper}
compress(b'venezuelan beaver cheese', options\=options)

bounds()[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "Link to this definition")

Return the tuple of int bounds, `(lower, upper)`, of a compression parameter. This method should be called on the attribute you wish to retrieve the bounds of. For example, to get the valid values for [`compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level")
, one may check the result of `CompressionParameter.compression_level.bounds()`.

Both the lower and upper bounds are inclusive.

compression\_level[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "Link to this definition")

A high-level means of setting other compression parameters that affect the speed and ratio of compressing data.

Regular compression levels are greater than `0`. Values greater than `20` are considered “ultra” compression and require more memory than other levels. Negative values can be used to trade off faster compression for worse compression ratios.

Setting the level to zero uses [`COMPRESSION_LEVEL_DEFAULT`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.COMPRESSION_LEVEL_DEFAULT "compression.zstd.COMPRESSION_LEVEL_DEFAULT")
.

window\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.window_log "Link to this definition")

Maximum allowed back-reference distance the compressor can use when compressing data, expressed as power of two, `1 << window_log` bytes. This parameter greatly influences the memory usage of compression. Higher values require more memory but gain better compression values.

A value of zero causes the value to be selected automatically.

hash\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.hash_log "Link to this definition")

Size of the initial probe table, as a power of two. The resulting memory usage is `1 << (hash_log+2)` bytes. Larger tables improve compression ratio of strategies <= [`dfast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.dfast "compression.zstd.Strategy.dfast")
, and improve compression speed of strategies > `dfast`.

A value of zero causes the value to be selected automatically.

chain\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.chain_log "Link to this definition")

Size of the multi-probe search table, as a power of two. The resulting memory usage is `1 << (chain_log+2)` bytes. Larger tables result in better and slower compression. This parameter has no effect for the [`fast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "compression.zstd.Strategy.fast")
 strategy. It’s still useful when using [`dfast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.dfast "compression.zstd.Strategy.dfast")
 strategy, in which case it defines a secondary probe table.

A value of zero causes the value to be selected automatically.

search\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.search_log "Link to this definition")

Number of search attempts, as a power of two. More attempts result in better and slower compression. This parameter is useless for [`fast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "compression.zstd.Strategy.fast")
 and [`dfast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.dfast "compression.zstd.Strategy.dfast")
 strategies.

A value of zero causes the value to be selected automatically.

min\_match[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.min_match "Link to this definition")

Minimum size of searched matches. Larger values increase compression and decompression speed, but decrease ratio. Note that Zstandard can still find matches of smaller size, it just tweaks its search algorithm to look for this size and larger. For all strategies < [`btopt`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btopt "compression.zstd.Strategy.btopt")
, the effective minimum is `4`; for all strategies > [`fast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "compression.zstd.Strategy.fast")
, the effective maximum is `6`.

A value of zero causes the value to be selected automatically.

target\_length[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.target_length "Link to this definition")

The impact of this field depends on the selected [`Strategy`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy "compression.zstd.Strategy")
.

For strategies [`btopt`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btopt "compression.zstd.Strategy.btopt")
, [`btultra`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btultra "compression.zstd.Strategy.btultra")
 and [`btultra2`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btultra2 "compression.zstd.Strategy.btultra2")
, the value is the length of a match considered “good enough” to stop searching. Larger values make compression ratios better, but compresses slower.

For strategy [`fast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "compression.zstd.Strategy.fast")
, it is the distance between match sampling. Larger values make compression faster, but with a worse compression ratio.

A value of zero causes the value to be selected automatically.

strategy[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.strategy "Link to this definition")

The higher the value of selected strategy, the more complex the compression technique used by zstd, resulting in higher compression ratios but slower compression.

See also

[`Strategy`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy "compression.zstd.Strategy")

enable\_long\_distance\_matching[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.enable_long_distance_matching "Link to this definition")

Long distance matching can be used to improve compression for large inputs by finding large matches at greater distances. It increases memory usage and window size.

`True` or `1` enable long distance matching while `False` or `0` disable it.

Enabling this parameter increases default [`window_log`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.window_log "compression.zstd.CompressionParameter.window_log")
 to 128 MiB except when expressly set to a different value. This setting is enabled by default if `window_log` >= 128 MiB and the compression strategy >= [`btopt`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btopt "compression.zstd.Strategy.btopt")
 (compression level 16+).

ldm\_hash\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.ldm_hash_log "Link to this definition")

Size of the table for long distance matching, as a power of two. Larger values increase memory usage and compression ratio, but decrease compression speed.

A value of zero causes the value to be selected automatically.

ldm\_min\_match[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.ldm_min_match "Link to this definition")

Minimum match size for long distance matcher. Larger or too small values can often decrease the compression ratio.

A value of zero causes the value to be selected automatically.

ldm\_bucket\_size\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.ldm_bucket_size_log "Link to this definition")

Log size of each bucket in the long distance matcher hash table for collision resolution. Larger values improve collision resolution but decrease compression speed.

A value of zero causes the value to be selected automatically.

ldm\_hash\_rate\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.ldm_hash_rate_log "Link to this definition")

Frequency of inserting/looking up entries into the long distance matcher hash table. Larger values improve compression speed. Deviating far from the default value will likely result in a compression ratio decrease.

A value of zero causes the value to be selected automatically.

content\_size\_flag[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.content_size_flag "Link to this definition")

Write the size of the data to be compressed into the Zstandard frame header when known prior to compressing.

This flag only takes effect under the following scenarios:

*   Calling [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress "compression.zstd.compress")
     for one-shot compression
    
*   Providing all of the data to be compressed in the frame in a single [`ZstdCompressor.compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress")
     call, with the [`ZstdCompressor.FLUSH_FRAME`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "compression.zstd.ZstdCompressor.FLUSH_FRAME")
     mode.
    
*   Calling [`ZstdCompressor.set_pledged_input_size()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.set_pledged_input_size "compression.zstd.ZstdCompressor.set_pledged_input_size")
     with the exact amount of data that will be provided to the compressor prior to any calls to [`ZstdCompressor.compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress")
     for the current frame. `ZstdCompressor.set_pledged_input_size()` must be called for each new frame.
    

All other compression calls may not write the size information into the frame header.

`True` or `1` enable the content size flag while `False` or `0` disable it.

checksum\_flag[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.checksum_flag "Link to this definition")

A four-byte checksum using XXHash64 of the uncompressed content is written at the end of each frame. Zstandard’s decompression code verifies the checksum. If there is a mismatch a [`ZstdError`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdError "compression.zstd.ZstdError")
 exception is raised.

`True` or `1` enable checksum generation while `False` or `0` disable it.

dict\_id\_flag[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.dict_id_flag "Link to this definition")

When compressing with a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
, the dictionary’s ID is written into the frame header.

`True` or `1` enable storing the dictionary ID while `False` or `0` disable it.

nb\_workers[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.nb_workers "Link to this definition")

Select how many threads will be spawned to compress in parallel. When `nb_workers` > 0, enables multi-threaded compression, a value of `1` means “one-thread multi-threaded mode”. More workers improve speed, but also increase memory usage and slightly reduce compression ratio.

A value of zero disables multi-threading.

job\_size[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.job_size "Link to this definition")

Size of a compression job, in bytes. This value is enforced only when [`nb_workers`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.nb_workers "compression.zstd.CompressionParameter.nb_workers")
 >= 1. Each compression job is completed in parallel, so this value can indirectly impact the number of active threads.

A value of zero causes the value to be selected automatically.

overlap\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.overlap_log "Link to this definition")

Sets how much data is reloaded from previous jobs (threads) for new jobs to be used by the look behind window during compression. This value is only used when [`nb_workers`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.nb_workers "compression.zstd.CompressionParameter.nb_workers")
 >= 1. Acceptable values vary from 0 to 9.

> *   0 means dynamically set the overlap amount
>     
> *   1 means no overlap
>     
> *   9 means use a full window size from the previous job
>     

Each increment halves/doubles the overlap size. “8” means an overlap of `window_size/2`, “7” means an overlap of `window_size/4`, etc.

class compression.zstd.DecompressionParameter[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "Link to this definition")

An [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum")
 containing the advanced decompression parameter keys that can be used when decompressing data. Parameters are optional; any omitted parameter will have its value selected automatically.

The [`bounds()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter.bounds "compression.zstd.DecompressionParameter.bounds")
 method can be used on any attribute to get the valid values for that parameter.

Example setting the [`window_log_max`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter.window_log_max "compression.zstd.DecompressionParameter.window_log_max")
 to the maximum size:

Copy

data \= compress(b'Some very long buffer of bytes...')

\_lower, upper \= DecompressionParameter.window\_log\_max.bounds()

options \= {DecompressionParameter.window\_log\_max: upper}
decompress(data, options\=options)

bounds()[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter.bounds "Link to this definition")

Return the tuple of int bounds, `(lower, upper)`, of a decompression parameter. This method should be called on the attribute you wish to retrieve the bounds of.

Both the lower and upper bounds are inclusive.

window\_log\_max[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter.window_log_max "Link to this definition")

The base-two logarithm of the maximum size of the window used during decompression. This can be useful to limit the amount of memory used when decompressing data. A larger maximum window size leads to faster decompression.

A value of zero causes the value to be selected automatically.

class compression.zstd.Strategy[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy "Link to this definition")

An [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum")
 containing strategies for compression. Higher-numbered strategies correspond to more complex and slower compression.

Note

The values of attributes of `Strategy` are not necessarily stable across zstd versions. Only the ordering of the attributes may be relied upon. The attributes are listed below in order.

The following strategies are available:

fast[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "Link to this definition")

dfast[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.dfast "Link to this definition")

greedy[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.greedy "Link to this definition")

lazy[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.lazy "Link to this definition")

lazy2[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.lazy2 "Link to this definition")

btlazy2[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btlazy2 "Link to this definition")

btopt[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btopt "Link to this definition")

btultra[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btultra "Link to this definition")

btultra2[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btultra2 "Link to this definition")

Miscellaneous[¶](https://docs.python.org/3/library/compression.zstd.html#miscellaneous "Link to this heading")

---------------------------------------------------------------------------------------------------------------

compression.zstd.get\_frame\_info(_frame\_buffer_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.get_frame_info "Link to this definition")

Retrieve a [`FrameInfo`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo "compression.zstd.FrameInfo")
 object containing metadata about a Zstandard frame. Frames contain metadata related to the compressed data they hold.

class compression.zstd.FrameInfo[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo "Link to this definition")

Metadata related to a Zstandard frame.

decompressed\_size[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo.decompressed_size "Link to this definition")

The size of the decompressed contents of the frame.

dictionary\_id[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo.dictionary_id "Link to this definition")

An integer representing the Zstandard dictionary ID needed for decompressing the frame. `0` means the dictionary ID was not recorded in the frame header. This may mean that a Zstandard dictionary is not needed, or that the ID of a required dictionary was not recorded.

compression.zstd.COMPRESSION\_LEVEL\_DEFAULT[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.COMPRESSION_LEVEL_DEFAULT "Link to this definition")

The default compression level for Zstandard: `3`.

compression.zstd.zstd\_version\_info[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.zstd_version_info "Link to this definition")

Version number of the runtime zstd library as a tuple of integers (major, minor, release).

Examples[¶](https://docs.python.org/3/library/compression.zstd.html#examples "Link to this heading")

-----------------------------------------------------------------------------------------------------

Reading in a compressed file:

Copy

from compression import zstd

with zstd.open("file.zst") as f:
    file\_content \= f.read()

Creating a compressed file:

Copy

from compression import zstd

data \= b"Insert Data Here"
with zstd.open("file.zst", "w") as f:
    f.write(data)

Compressing data in memory:

Copy

from compression import zstd

data\_in \= b"Insert Data Here"
data\_out \= zstd.compress(data\_in)

Incremental compression:

Copy

from compression import zstd

comp \= zstd.ZstdCompressor()
out1 \= comp.compress(b"Some data\\n")
out2 \= comp.compress(b"Another piece of data\\n")
out3 \= comp.compress(b"Even more data\\n")
out4 \= comp.flush()
\# Concatenate all the partial results:
result \= b"".join(\[out1, out2, out3, out4\])

Writing compressed data to an already-open file:

Copy

from compression import zstd

with open("myfile", "wb") as f:
    f.write(b"This data will not be compressed\\n")
    with zstd.open(f, "w") as zstf:
        zstf.write(b"This \*will\* be compressed\\n")
    f.write(b"Not compressed\\n")

Creating a compressed file using compression parameters:

Copy

from compression import zstd

options \= {
   zstd.CompressionParameter.checksum\_flag: 1
}
with zstd.open("file.zst", "w", options\=options) as f:
    f.write(b"Mind if I squeeze in?")

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html#)
    *   [Exceptions](https://docs.python.org/3/library/compression.zstd.html#exceptions)
        
    *   [Reading and writing compressed files](https://docs.python.org/3/library/compression.zstd.html#reading-and-writing-compressed-files)
        
    *   [Compressing and decompressing data in memory](https://docs.python.org/3/library/compression.zstd.html#compressing-and-decompressing-data-in-memory)
        
    *   [Zstandard dictionaries](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries)
        
    *   [Advanced parameter control](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control)
        
    *   [Miscellaneous](https://docs.python.org/3/library/compression.zstd.html#miscellaneous)
        
    *   [Examples](https://docs.python.org/3/library/compression.zstd.html#examples)
        

#### Previous topic

[The `compression` package](https://docs.python.org/3/library/compression.html "previous chapter")

#### Next topic

[`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=compression.zstd+%E2%80%94+Compression+compatible+with+the+Zstandard+format&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcompression.zstd.html&pagesource=library%2Fcompression.zstd.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/compression.zstd.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/zlib.html "zlib — Compression compatible with gzip")
     |
*   [previous](https://docs.python.org/3/library/compression.html "The compression package")
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
*   [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html)
    
*    
    
    |
*   Theme Auto Light Dark |