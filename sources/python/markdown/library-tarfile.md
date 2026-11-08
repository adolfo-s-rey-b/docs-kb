### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/fileformats.html "File Formats")
     |
*   [previous](https://docs.python.org/3/library/zipfile.html "zipfile — Work with ZIP archives")
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
*   [`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tarfile` — Read and write tar archive files[¶](https://docs.python.org/3/library/tarfile.html#module-tarfile "Link to this heading")

======================================================================================================================================

**Source code:** [Lib/tarfile.py](https://github.com/python/cpython/tree/3.15/Lib/tarfile.py)

* * *

The `tarfile` module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression. Use the [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")
 module to read or write `.zip` files, or the higher-level functions in [shutil](https://docs.python.org/3/library/shutil.html#archiving-operations)
.

Some facts and figures:

*   reads and writes [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.")
    , [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
    , [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.")
    , and [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
     compressed archives if the respective modules are available.
    
    If any of these [optional modules](https://docs.python.org/3/glossary.html#term-optional-module)
     are missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements)
    .
    
*   read/write support for the POSIX.1-1988 (ustar) format.
    
*   read/write support for the GNU tar format including _longname_ and _longlink_ extensions, read-only support for all variants of the _sparse_ extension including restoration of sparse files.
    
*   read/write support for the POSIX.1-2001 (pax) format.
    
*   handles directories, regular files, hardlinks, symbolic links, fifos, character devices and block devices and is able to acquire and restore file information like timestamp, access permissions and owner.
    

Changed in version 3.3: Added support for [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
 compression.

Changed in version 3.12: Archives are extracted using a [filter](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter)
, which makes it possible to either limit surprising/dangerous features, or to acknowledge that they are expected and the archive is fully trusted.

Changed in version 3.14: Set the default extraction filter to [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter")
, which disallows some dangerous features such as links to absolute paths or paths outside of the destination. Previously, the filter strategy was equivalent to [`fully_trusted`](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter")
.

Changed in version 3.14: Added support for Zstandard compression using [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.")
.

tarfile.open(_name\=None_, _mode\='r'_, _fileobj\=None_, _bufsize\=10240_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.open "Link to this definition")

Return a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 object for the pathname _name_. For detailed information on `TarFile` objects and the keyword arguments that are allowed, see [TarFile Objects](https://docs.python.org/3/library/tarfile.html#tarfile-objects)
.

_mode_ has to be a string of the form `'filemode[:compression]'`, it defaults to `'r'`. Here is a full list of mode combinations:

| mode | action |
| --- | --- |
| `'r'` or `'r:*'` | Open for reading with transparent compression (recommended). |
| `'r:'` | Open for reading exclusively without compression. |
| `'r:gz'` | Open for reading with gzip compression. |
| `'r:bz2'` | Open for reading with bzip2 compression. |
| `'r:xz'` | Open for reading with lzma compression. |
| `'r:zst'` | Open for reading with Zstandard compression. |
| `'x'` or `'x:'` | Create a tarfile exclusively without compression. Raise a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")<br> exception if it already exists. |
| `'x:gz'` | Create a tarfile with gzip compression. Raise a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")<br> exception if it already exists. |
| `'x:bz2'` | Create a tarfile with bzip2 compression. Raise a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")<br> exception if it already exists. |
| `'x:xz'` | Create a tarfile with lzma compression. Raise a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")<br> exception if it already exists. |
| `'x:zst'` | Create a tarfile with Zstandard compression. Raise a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")<br> exception if it already exists. |
| `'a'` or `'a:'` | Open for appending with no compression. The file is created if it does not exist. |
| `'w'` or `'w:'` | Open for uncompressed writing. |
| `'w:gz'` | Open for gzip compressed writing. |
| `'w:bz2'` | Open for bzip2 compressed writing. |
| `'w:xz'` | Open for lzma compressed writing. |
| `'w:zst'` | Open for Zstandard compressed writing. |

Note that `'a:gz'`, `'a:bz2'` or `'a:xz'` is not possible. If _mode_ is not suitable to open a certain (compressed) file for reading, [`ReadError`](https://docs.python.org/3/library/tarfile.html#tarfile.ReadError "tarfile.ReadError")
 is raised. Use _mode_ `'r'` to avoid this. If a compression method is not supported, [`CompressionError`](https://docs.python.org/3/library/tarfile.html#tarfile.CompressionError "tarfile.CompressionError")
 is raised.

If _fileobj_ is specified, it is used as an alternative to a [file object](https://docs.python.org/3/glossary.html#term-file-object)
 opened in binary mode for _name_. It is supposed to be at position 0.

For modes `'w:gz'`, `'x:gz'`, `'w|gz'`, `'w:bz2'`, `'x:bz2'`, `'w|bz2'`, `tarfile.open()` accepts the keyword argument _compresslevel_ (default `6`) to specify the compression level of the file.

For modes `'w:xz'`, `'x:xz'` and `'w|xz'`, `tarfile.open()` accepts the keyword argument _preset_ to specify the compression level of the file.

For modes `'w:zst'`, `'x:zst'` and `'w|zst'`, `tarfile.open()` accepts the keyword argument _level_ to specify the compression level of the file. The keyword argument _options_ may also be passed, providing advanced Zstandard compression parameters described by [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter")
. The keyword argument _zstd\_dict_ can be passed to provide a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
, a Zstandard dictionary used to improve compression of smaller amounts of data.

For modes `'w:gz'` and `'w|gz'`, `tarfile.open()` accepts the keyword argument _mtime_ to create a gzip archive header with that mtime. By default, the mtime is set to the time of creation of the archive. Use _mtime_ `0` to generate a compressed stream that does not depend on creation time, for reproducible output.

For special purposes, there is a second format for _mode_: `'filemode|[compression]'`. `tarfile.open()` will return a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 object that processes its data as a stream of blocks. No random seeking will be done on the file. If given, _fileobj_ may be any object that has a [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read")
 or [`write()`](https://docs.python.org/3/library/io.html#io.RawIOBase.write "io.RawIOBase.write")
 method (depending on the _mode_) that works with bytes. _bufsize_ specifies the blocksize and defaults to `20 * 512` bytes. Use this variant in combination with e.g. `sys.stdin.buffer`, a socket [file object](https://docs.python.org/3/glossary.html#term-file-object)
 or a tape device. However, such a `TarFile` object is limited in that it does not allow random access, see [Examples](https://docs.python.org/3/library/tarfile.html#tar-examples)
. The currently possible modes:

| Mode | Action |
| --- | --- |
| `'r\|*'` | Open a _stream_ of tar blocks for reading with transparent compression. |
| `'r\|'` | Open a _stream_ of uncompressed tar blocks for reading. |
| `'r\|gz'` | Open a gzip compressed _stream_ for reading. |
| `'r\|bz2'` | Open a bzip2 compressed _stream_ for reading. |
| `'r\|xz'` | Open an lzma compressed _stream_ for reading. |
| `'r\|zst'` | Open a Zstandard compressed _stream_ for reading. |
| `'w\|'` | Open an uncompressed _stream_ for writing. |
| `'w\|gz'` | Open a gzip compressed _stream_ for writing. |
| `'w\|bz2'` | Open a bzip2 compressed _stream_ for writing. |
| `'w\|xz'` | Open an lzma compressed _stream_ for writing. |
| `'w\|zst'` | Open a Zstandard compressed _stream_ for writing. |

Changed in version 3.5: The `'x'` (exclusive creation) mode was added.

Changed in version 3.6: The _name_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.12: The _compresslevel_ keyword argument also works for streams.

Changed in version 3.14: The _preset_ keyword argument also works for streams.

Changed in version 3.15: The default compression level was reduced to 6 (down from 9). It is the default level used by most compression tools and a better tradeoff between speed and performance.

class tarfile.TarFile

Class for reading and writing tar archives. Do not use this class directly: use [`tarfile.open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open")
 instead. See [TarFile Objects](https://docs.python.org/3/library/tarfile.html#tarfile-objects)
.

tarfile.is\_tarfile(_name_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.is_tarfile "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if _name_ is a tar archive file, that the `tarfile` module can read. _name_ may be a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, file, or file-like object.

Changed in version 3.9: Support for file and file-like objects.

The `tarfile` module defines the following exceptions:

exception tarfile.TarError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarError "Link to this definition")

Base class for all `tarfile` exceptions.

exception tarfile.ReadError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.ReadError "Link to this definition")

Is raised when a tar archive is opened, that either cannot be handled by the `tarfile` module or is somehow invalid.

exception tarfile.CompressionError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.CompressionError "Link to this definition")

Is raised when a compression method is not supported or when the data cannot be decoded properly.

exception tarfile.StreamError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.StreamError "Link to this definition")

Is raised for the limitations that are typical for stream-like [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 objects.

exception tarfile.ExtractError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.ExtractError "Link to this definition")

Is raised for _non-fatal_ errors when using [`TarFile.extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
, but only if [`TarFile.errorlevel`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel")
`== 2`.

exception tarfile.HeaderError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.HeaderError "Link to this definition")

Is raised by [`TarInfo.frombuf()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.frombuf "tarfile.TarInfo.frombuf")
 if the buffer it gets is invalid.

exception tarfile.FilterError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "Link to this definition")

Base class for members [refused](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse)
 by filters.

tarinfo[¶](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError.tarinfo "Link to this definition")

Information about the member that the filter refused to extract, as [TarInfo](https://docs.python.org/3/library/tarfile.html#tarinfo-objects)
.

exception tarfile.AbsolutePathError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.AbsolutePathError "Link to this definition")

Raised to refuse extracting a member with an absolute path.

exception tarfile.OutsideDestinationError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.OutsideDestinationError "Link to this definition")

Raised to refuse extracting a member outside the destination directory.

exception tarfile.SpecialFileError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.SpecialFileError "Link to this definition")

Raised to refuse extracting a special file (e.g. a device or pipe).

exception tarfile.AbsoluteLinkError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.AbsoluteLinkError "Link to this definition")

Raised to refuse extracting a symbolic link with an absolute path.

exception tarfile.LinkOutsideDestinationError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.LinkOutsideDestinationError "Link to this definition")

Raised to refuse extracting a symbolic link pointing outside the destination directory.

exception tarfile.LinkFallbackError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.LinkFallbackError "Link to this definition")

Raised to refuse emulating a link (hard or symbolic) by extracting another archive member, when that member would be rejected by the filter location. The exception that was raised to reject the replacement member is available as `BaseException.__context__`.

Added in version 3.15.

The following constants are available at the module level:

tarfile.ENCODING[¶](https://docs.python.org/3/library/tarfile.html#tarfile.ENCODING "Link to this definition")

The default character encoding: `'utf-8'` on Windows, the value returned by [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
 otherwise.

tarfile.REGTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.REGTYPE "Link to this definition")

tarfile.AREGTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.AREGTYPE "Link to this definition")

A regular file [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.LNKTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.LNKTYPE "Link to this definition")

A link (inside tarfile) [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.SYMTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.SYMTYPE "Link to this definition")

A symbolic link [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.CHRTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.CHRTYPE "Link to this definition")

A character special device [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.BLKTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.BLKTYPE "Link to this definition")

A block special device [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.DIRTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.DIRTYPE "Link to this definition")

A directory [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.FIFOTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.FIFOTYPE "Link to this definition")

A FIFO special device [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.CONTTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.CONTTYPE "Link to this definition")

A contiguous file [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.GNUTYPE\_LONGNAME[¶](https://docs.python.org/3/library/tarfile.html#tarfile.GNUTYPE_LONGNAME "Link to this definition")

A GNU tar longname [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.GNUTYPE\_LONGLINK[¶](https://docs.python.org/3/library/tarfile.html#tarfile.GNUTYPE_LONGLINK "Link to this definition")

A GNU tar longlink [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

tarfile.GNUTYPE\_SPARSE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.GNUTYPE_SPARSE "Link to this definition")

A GNU tar sparse file [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type")
.

Each of the following constants defines a tar archive format that the `tarfile` module is able to create. See section [Supported tar formats](https://docs.python.org/3/library/tarfile.html#tar-formats)
 for details.

tarfile.USTAR\_FORMAT[¶](https://docs.python.org/3/library/tarfile.html#tarfile.USTAR_FORMAT "Link to this definition")

POSIX.1-1988 (ustar) format.

tarfile.GNU\_FORMAT[¶](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "Link to this definition")

GNU tar format.

tarfile.PAX\_FORMAT[¶](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "Link to this definition")

POSIX.1-2001 (pax) format.

tarfile.DEFAULT\_FORMAT[¶](https://docs.python.org/3/library/tarfile.html#tarfile.DEFAULT_FORMAT "Link to this definition")

The default format for creating archives. This is currently [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")
.

Changed in version 3.8: The default format for new archives was changed to [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")
 from [`GNU_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT")
.

See also

Module [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")

Documentation of the [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")
 standard module.

[Archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations)

Documentation of the higher-level archiving facilities provided by the standard [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
 module.

[GNU tar manual, Basic Tar Format](https://www.gnu.org/software/tar/manual/html_node/Standard.html)

Documentation for tar archive files, including GNU tar extensions.

TarFile Objects[¶](https://docs.python.org/3/library/tarfile.html#tarfile-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------

The [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 object provides an interface to a tar archive. A tar archive is a sequence of blocks. An archive member (a stored file) is made up of a header block followed by data blocks. It is possible to store a file in a tar archive several times. Each archive member is represented by a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object, see [TarInfo Objects](https://docs.python.org/3/library/tarfile.html#tarinfo-objects)
 for details.

A [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 object can be used as a context manager in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement. It will automatically be closed when the block is completed. Please note that in the event of an exception an archive opened for writing will not be finalized; only the internally used file object will be closed. See the [Examples](https://docs.python.org/3/library/tarfile.html#tar-examples)
 section for a use case.

Added in version 3.2: Added support for the context management protocol.

class tarfile.TarFile(_name\=None_, _mode\='r'_, _fileobj\=None_, _format\=DEFAULT\_FORMAT_, _tarinfo\=TarInfo_, _dereference\=False_, _ignore\_zeros\=False_, _encoding\=ENCODING_, _errors\='surrogateescape'_, _pax\_headers\=None_, _debug\=0_, _errorlevel\=1_, _stream\=False_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "Link to this definition")

All following arguments are optional and can be accessed as instance attributes as well.

_name_ is the pathname of the archive. _name_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
. It can be omitted if _fileobj_ is given. In this case, the file object’s `name` attribute is used if it exists.

_mode_ is either `'r'` to read from an existing archive, `'a'` to append data to an existing file, `'w'` to create a new file overwriting an existing one, or `'x'` to create a new file only if it does not already exist.

If _fileobj_ is given, it is used for reading or writing data. If it can be determined, _mode_ is overridden by _fileobj_’s mode. _fileobj_ will be used from position 0.

Note

_fileobj_ is not closed, when `TarFile` is closed.

_format_ controls the archive format for writing. It must be one of the constants [`USTAR_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.USTAR_FORMAT "tarfile.USTAR_FORMAT")
, [`GNU_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT")
 or [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")
 that are defined at module level. When reading, format will be automatically detected, even if different formats are present in a single archive.

The _tarinfo_ argument can be used to replace the default [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 class with a different one.

If _dereference_ is [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
, add symbolic and hard links to the archive. If it is [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
, add the content of the target files to the archive. This has no effect on systems that do not support symbolic links.

If _ignore\_zeros_ is [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
, treat an empty block as the end of the archive. If it is [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
, skip empty (and invalid) blocks and try to get as many members as possible. This is only useful for reading concatenated or damaged archives.

_debug_ can be set from `0` (no debug messages) up to `3` (all debug messages). The messages are written to `sys.stderr`.

_errorlevel_ controls how extraction errors are handled, see [`the corresponding attribute`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel")
.

The _encoding_ and _errors_ arguments define the character encoding to be used for reading or writing the archive and how conversion errors are going to be handled. The default settings will work for most users. See section [Unicode issues](https://docs.python.org/3/library/tarfile.html#tar-unicode)
 for in-depth information.

The _pax\_headers_ argument is an optional dictionary of strings which will be added as a pax global header if _format_ is [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")
.

If _stream_ is set to [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 then while reading the archive info about files in the archive are not cached, saving memory.

Changed in version 3.2: Use `'surrogateescape'` as the default for the _errors_ argument.

Changed in version 3.5: The `'x'` (exclusive creation) mode was added.

Changed in version 3.6: The _name_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.13: Add the _stream_ parameter.

classmethod TarFile.open(_..._)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.open "Link to this definition")

Alternative constructor. The [`tarfile.open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open")
 function is actually a shortcut to this classmethod.

TarFile.getmember(_name_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmember "Link to this definition")

Return a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object for member _name_. If _name_ can not be found in the archive, [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is raised.

Note

If a member occurs more than once in the archive, its last occurrence is assumed to be the most up-to-date version.

TarFile.getmembers()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "Link to this definition")

Return the members of the archive as a list of [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 objects. The list has the same order as the members in the archive.

TarFile.getnames()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getnames "Link to this definition")

Return the members as a list of their names. It has the same order as the list returned by [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers")
.

TarFile.list(_verbose\=True_, _\*_, _members\=None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.list "Link to this definition")

Print a table of contents to `sys.stdout`. If _verbose_ is [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
, only the names of the members are printed. If it is [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
, output similar to that of **ls -l** is produced. If optional _members_ is given, it must be a subset of the list returned by [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers")
.

Changed in version 3.5: Added the _members_ parameter.

TarFile.next()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.next "Link to this definition")

Return the next member of the archive as a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object, when [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 is opened for reading. Return [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 if there is no more available.

TarFile.extractall(_path\='.'_, _members\=None_, _\*_, _numeric\_owner\=False_, _filter\=None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "Link to this definition")

Extract all members from the archive to the current working directory or directory _path_. If optional _members_ is given, it must be a subset of the list returned by [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers")
. Directory information like owner, modification time and permissions are set after all members have been extracted. This is done to work around two problems: A directory’s modification time is reset each time a file is created in it. And, if a directory’s permissions do not allow writing, extracting files to it will fail.

If _numeric\_owner_ is [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
, the uid and gid numbers from the tarfile are used to set the owner/group for the extracted files. Otherwise, the named values from the tarfile are used.

The _filter_ argument specifies how `members` are modified or rejected before extraction. See [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter)
 for details. It is recommended to set this explicitly only if specific _tar_ features are required, or as `filter='data'` to support Python versions with a less secure default (3.13 and lower).

Warning

Never extract archives from untrusted sources without prior inspection.

Since Python 3.14, the default ([`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter")
) will prevent the most dangerous security issues. However, it will not prevent _all_ unintended or insecure behavior. Read the [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter)
 section for details.

Changed in version 3.5: Added the _numeric\_owner_ parameter.

Changed in version 3.6: The _path_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.12: Added the _filter_ parameter.

Changed in version 3.14: The _filter_ parameter now defaults to `'data'`.

TarFile.extract(_member_, _path\=''_, _set\_attrs\=True_, _\*_, _numeric\_owner\=False_, _filter\=None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "Link to this definition")

Extract a member from the archive to the current working directory, using its full name. Its file information is extracted as accurately as possible. _member_ may be a filename or a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object. You can specify a different directory using _path_. _path_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
. File attributes (owner, mtime, mode) are set unless _set\_attrs_ is false.

The _numeric\_owner_ and _filter_ arguments are the same as for [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
.

Note

The `extract()` method does not take care of several extraction issues. In most cases you should consider using the [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
 method.

Warning

Never extract archives from untrusted sources without prior inspection. See the warning for [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
 for details.

Changed in version 3.2: Added the _set\_attrs_ parameter.

Changed in version 3.5: Added the _numeric\_owner_ parameter.

Changed in version 3.6: The _path_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.12: Added the _filter_ parameter.

TarFile.extractfile(_member_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractfile "Link to this definition")

Extract a member from the archive as a file object. _member_ may be a filename or a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object. If _member_ is a regular file or a link, an [`io.BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader")
 object is returned. For all other existing members, [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 is returned. If _member_ does not appear in the archive, [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is raised.

Changed in version 3.3: Return an [`io.BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader")
 object.

Changed in version 3.13: The returned [`io.BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader")
 object has the `mode` attribute which is always equal to `'rb'`.

TarFile.errorlevel: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "Link to this definition")

If _errorlevel_ is `0`, errors are ignored when using [`TarFile.extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 and [`TarFile.extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
. Nevertheless, they appear as error messages in the debug output when _debug_ is greater than 0. If `1` (the default), all _fatal_ errors are raised as [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 or [`FilterError`](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "tarfile.FilterError")
 exceptions. If `2`, all _non-fatal_ errors are raised as [`TarError`](https://docs.python.org/3/library/tarfile.html#tarfile.TarError "tarfile.TarError")
 exceptions as well.

Some exceptions, e.g. ones caused by wrong argument types or data corruption, are always raised.

Custom [extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter)
 should raise [`FilterError`](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "tarfile.FilterError")
 for _fatal_ errors and [`ExtractError`](https://docs.python.org/3/library/tarfile.html#tarfile.ExtractError "tarfile.ExtractError")
 for _non-fatal_ ones.

Note that when an exception is raised, the archive may be partially extracted. It is the user’s responsibility to clean up.

TarFile.extraction\_filter[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extraction_filter "Link to this definition")

Added in version 3.12.

The [extraction filter](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter)
 used as a default for the _filter_ argument of [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
.

The attribute may be `None` or a callable. String names are not allowed for this attribute, unlike the _filter_ argument to [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
.

If `extraction_filter` is `None` (the default), extraction methods will use the [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter")
 filter by default.

The attribute may be set on instances or overridden in subclasses. It also is possible to set it on the `TarFile` class itself to set a global default, although, since it affects all uses of _tarfile_, it is best practice to only do so in top-level applications or [`site configuration`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
. To set a global default this way, a filter function needs to be wrapped in [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 to prevent injection of a `self` argument.

Changed in version 3.14: The default filter is set to [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter")
, which disallows some dangerous features such as links to absolute paths or paths outside of the destination. Previously, the default was equivalent to [`fully_trusted`](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter")
.

TarFile.add(_name_, _arcname\=None_, _recursive\=True_, _\*_, _filter\=None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "Link to this definition")

Add the file _name_ to the archive. _name_ may be any type of file (directory, fifo, symbolic link, etc.). If given, _arcname_ specifies an alternative name for the file in the archive. Directories are added recursively by default. This can be avoided by setting _recursive_ to [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
. Recursion adds entries in sorted order. If _filter_ is given, it should be a function that takes a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object argument and returns the changed `TarInfo` object. If it instead returns [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 the `TarInfo` object will be excluded from the archive. See [Examples](https://docs.python.org/3/library/tarfile.html#tar-examples)
 for an example.

Changed in version 3.2: Added the _filter_ parameter.

Changed in version 3.7: Recursion adds entries in sorted order.

TarFile.addfile(_tarinfo_, _fileobj\=None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.addfile "Link to this definition")

Add the [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object _tarinfo_ to the archive. If _tarinfo_ represents a non zero-size regular file, the _fileobj_ argument should be a [binary file](https://docs.python.org/3/glossary.html#term-binary-file)
, and `tarinfo.size` bytes are read from it and added to the archive. You can create `TarInfo` objects directly, or by using [`gettarinfo()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.gettarinfo "tarfile.TarFile.gettarinfo")
.

Changed in version 3.13: _fileobj_ must be given for non-zero-sized regular files.

TarFile.gettarinfo(_name\=None_, _arcname\=None_, _fileobj\=None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.gettarinfo "Link to this definition")

Create a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object from the result of [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 or equivalent on an existing file. The file is either named by _name_, or specified as a [file object](https://docs.python.org/3/glossary.html#term-file-object)
 _fileobj_ with a file descriptor. _name_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
. If given, _arcname_ specifies an alternative name for the file in the archive, otherwise, the name is taken from _fileobj_’s [`name`](https://docs.python.org/3/library/io.html#io.FileIO.name "io.FileIO.name")
 attribute, or the _name_ argument. The name should be a text string.

You can modify some of the [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
’s attributes before you add it using [`addfile()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.addfile "tarfile.TarFile.addfile")
. If the file object is not an ordinary file object positioned at the beginning of the file, attributes such as [`size`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.size "tarfile.TarInfo.size")
 may need modifying. This is the case for objects such as [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile")
. The [`name`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.name "tarfile.TarInfo.name")
 may also be modified, in which case _arcname_ could be a dummy string.

Changed in version 3.6: The _name_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

TarFile.close()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.close "Link to this definition")

Close the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
. In write mode, two finishing zero blocks are appended to the archive.

TarFile.pax\_headers: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.pax_headers "Link to this definition")

A dictionary containing key-value pairs of pax global headers.

TarInfo Objects[¶](https://docs.python.org/3/library/tarfile.html#tarinfo-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------

A [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object represents one member in a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
. Aside from storing all required attributes of a file (like file type, size, time, permissions, owner etc.), it provides some useful methods to determine its type. It does _not_ contain the file’s data itself.

[`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 objects are returned by [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
’s methods [`getmember()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmember "tarfile.TarFile.getmember")
, [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers")
 and [`gettarinfo()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.gettarinfo "tarfile.TarFile.gettarinfo")
.

Modifying the objects returned by [`getmember()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmember "tarfile.TarFile.getmember")
 or [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers")
 will affect all subsequent operations on the archive. For cases where this is unwanted, you can use [`copy.copy()`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")
 or call the [`replace()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.replace "tarfile.TarInfo.replace")
 method to create a modified copy in one step.

Several attributes can be set to `None` to indicate that a piece of metadata is unused or unknown. Different [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 methods handle `None` differently:

*   The [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
     or [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
     methods will ignore the corresponding metadata, leaving it set to a default.
    
*   [`addfile()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.addfile "tarfile.TarFile.addfile")
     will fail.
    
*   [`list()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.list "tarfile.TarFile.list")
     will print a placeholder string.
    

class tarfile.TarInfo(_name\=''_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "Link to this definition")

Create a `TarInfo` object.

classmethod TarInfo.frombuf(_buf_, _encoding_, _errors_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.frombuf "Link to this definition")

Create and return a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object from string buffer _buf_.

Raises [`HeaderError`](https://docs.python.org/3/library/tarfile.html#tarfile.HeaderError "tarfile.HeaderError")
 if the buffer is invalid.

classmethod TarInfo.fromtarfile(_tarfile_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.fromtarfile "Link to this definition")

Read the next member from the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 object _tarfile_ and return it as a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object.

TarInfo.tobuf(_format\=DEFAULT\_FORMAT_, _encoding\=ENCODING_, _errors\='surrogateescape'_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.tobuf "Link to this definition")

Create a string buffer from a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object. For information on the arguments see the constructor of the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 class.

Changed in version 3.2: Use `'surrogateescape'` as the default for the _errors_ argument.

A `TarInfo` object has the following public data attributes:

TarInfo.name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.name "Link to this definition")

Name of the archive member.

TarInfo.size: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.size "Link to this definition")

Size in bytes.

TarInfo.mtime: [int](https://docs.python.org/3/builtins/functions.html#int "int")
 | [float](https://docs.python.org/3/builtins/functions.html#float "float")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.mtime "Link to this definition")

Time of last modification in seconds since the [epoch](https://docs.python.org/3/library/time.html#epoch)
, as in [`os.stat_result.st_mtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "os.stat_result.st_mtime")
.

Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
, causing extraction to skip applying this attribute.

TarInfo.mode: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.mode "Link to this definition")

Permission bits, as for [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")
.

Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
, causing extraction to skip applying this attribute.

TarInfo.type[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "Link to this definition")

File type. _type_ is usually one of these constants: [`REGTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.REGTYPE "tarfile.REGTYPE")
, [`AREGTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.AREGTYPE "tarfile.AREGTYPE")
, [`LNKTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.LNKTYPE "tarfile.LNKTYPE")
, [`SYMTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.SYMTYPE "tarfile.SYMTYPE")
, [`DIRTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.DIRTYPE "tarfile.DIRTYPE")
, [`FIFOTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.FIFOTYPE "tarfile.FIFOTYPE")
, [`CONTTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.CONTTYPE "tarfile.CONTTYPE")
, [`CHRTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.CHRTYPE "tarfile.CHRTYPE")
, [`BLKTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.BLKTYPE "tarfile.BLKTYPE")
, [`GNUTYPE_SPARSE`](https://docs.python.org/3/library/tarfile.html#tarfile.GNUTYPE_SPARSE "tarfile.GNUTYPE_SPARSE")
. To determine the type of a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object more conveniently, use the `is*()` methods below.

TarInfo.linkname: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.linkname "Link to this definition")

Name of the target file name, which is only present in [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 objects of type [`LNKTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.LNKTYPE "tarfile.LNKTYPE")
 and [`SYMTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.SYMTYPE "tarfile.SYMTYPE")
.

For symbolic links (`SYMTYPE`), the _linkname_ is relative to the directory that contains the link. For hard links (`LNKTYPE`), the _linkname_ is relative to the root of the archive.

TarInfo.uid: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.uid "Link to this definition")

User ID of the user who originally stored this member.

Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
, causing extraction to skip applying this attribute.

TarInfo.gid: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.gid "Link to this definition")

Group ID of the user who originally stored this member.

Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
, causing extraction to skip applying this attribute.

TarInfo.uname: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.uname "Link to this definition")

User name.

Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
, causing extraction to skip applying this attribute.

TarInfo.gname: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.gname "Link to this definition")

Group name.

Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
, causing extraction to skip applying this attribute.

TarInfo.chksum: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.chksum "Link to this definition")

Header checksum.

TarInfo.devmajor: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.devmajor "Link to this definition")

Device major number.

TarInfo.devminor: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.devminor "Link to this definition")

Device minor number.

TarInfo.offset: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.offset "Link to this definition")

The tar header starts here.

TarInfo.offset\_data: [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.offset_data "Link to this definition")

The file’s data starts here.

TarInfo.sparse[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.sparse "Link to this definition")

Sparse member information.

TarInfo.pax\_headers: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.pax_headers "Link to this definition")

A dictionary containing key-value pairs of an associated pax extended header.

TarInfo.replace(_name\=..._, _mtime\=..._, _mode\=..._, _linkname\=..._, _uid\=..._, _gid\=..._, _uname\=..._, _gname\=..._, _deep\=True_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.replace "Link to this definition")

Added in version 3.12.

Return a _new_ copy of the `TarInfo` object with the given attributes changed. For example, to return a `TarInfo` with the group name set to `'staff'`, use:

Copy

new\_tarinfo \= old\_tarinfo.replace(gname\='staff')

By default, a deep copy is made. If _deep_ is false, the copy is shallow, i.e. `pax_headers` and any custom attributes are shared with the original `TarInfo` object.

A [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object also provides some convenient query methods:

TarInfo.isfile()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isfile "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if the [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object is a regular file.

TarInfo.isreg()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isreg "Link to this definition")

Same as [`isfile()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isfile "tarfile.TarInfo.isfile")
.

TarInfo.isdir()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isdir "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if it is a directory.

TarInfo.issym()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.issym "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if it is a symbolic link.

TarInfo.islnk()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.islnk "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if it is a hard link.

TarInfo.ischr()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.ischr "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if it is a character device.

TarInfo.isblk()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isblk "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if it is a block device.

TarInfo.isfifo()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isfifo "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if it is a FIFO.

TarInfo.isdev()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isdev "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if it is one of character device, block device or FIFO.

Extraction filters[¶](https://docs.python.org/3/library/tarfile.html#extraction-filters "Link to this heading")

----------------------------------------------------------------------------------------------------------------

Added in version 3.12.

The _tar_ format is designed to capture all details of a UNIX-like filesystem, which makes it very powerful. Unfortunately, the features make it easy to create tar files that have unintended – and possibly malicious – effects when extracted. For example, extracting a tar file can overwrite arbitrary files in various ways (e.g. by using absolute paths, `..` path components, or symlinks that affect later members).

In most cases, the full functionality is not needed. Therefore, _tarfile_ supports extraction filters: a mechanism to limit functionality, and thus mitigate some of the security issues.

Warning

None of the available filters blocks _all_ dangerous archive features. Never extract archives from untrusted sources without prior inspection. See also [Hints for further verification](https://docs.python.org/3/library/tarfile.html#tarfile-further-verification)
.

See also

[**PEP 706**](https://peps.python.org/pep-0706/)

Contains further motivation and rationale behind the design.

The _filter_ argument to [`TarFile.extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
 or [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
 can be:

*   the string `'fully_trusted'`: Honor all metadata as specified in the archive. Should be used if the user trusts the archive completely, or implements their own complex verification.
    
*   the string `'tar'`: Honor most _tar_\-specific features (i.e. features of UNIX-like filesystems), but block features that are very likely to be surprising or malicious. See [`tar_filter()`](https://docs.python.org/3/library/tarfile.html#tarfile.tar_filter "tarfile.tar_filter")
     for details.
    
*   the string `'data'`: Ignore or block most features specific to UNIX-like filesystems. Intended for extracting cross-platform data archives. See [`data_filter()`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter")
     for details.
    
*   `None` (default): Use [`TarFile.extraction_filter`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extraction_filter "tarfile.TarFile.extraction_filter")
    .
    
    If that is also `None` (the default), the `'data'` filter will be used.
    
    > Changed in version 3.14: The default filter is set to [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter")
    > . Previously, the default was equivalent to [`fully_trusted`](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter")
    > .
    
*   A callable which will be called for each extracted member with a [TarInfo](https://docs.python.org/3/library/tarfile.html#tarinfo-objects)
     describing the member and the destination path to where the archive is extracted (i.e. the same path is used for all members):
    
    Copy
    
    filter(member: TarInfo, path: str, /) \-> TarInfo | None
    
    The callable is called just before each member is extracted, so it can take the current state of the disk into account. It can:
    
    *   return a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
         object which will be used instead of the metadata in the archive, or
        
    *   return `None`, in which case the member will be skipped, or
        
    *   raise an exception to abort the operation or skip the member, depending on [`errorlevel`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel")
        . Note that when extraction is aborted, [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
         may leave the archive partially extracted. It does not attempt to clean up.
        

### Default named filters[¶](https://docs.python.org/3/library/tarfile.html#default-named-filters "Link to this heading")

The pre-defined, named filters are available as functions, so they can be reused in custom filters:

tarfile.fully\_trusted\_filter(_member_, _path_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "Link to this definition")

Return _member_ unchanged.

This implements the `'fully_trusted'` filter.

tarfile.tar\_filter(_member_, _path_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.tar_filter "Link to this definition")

Implements the `'tar'` filter.

*   Strip leading slashes (`/` and [`os.sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep")
    ) from filenames.
    
*   Normalize filenames ([`TarInfo.name`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.name "tarfile.TarInfo.name")
    ) that contain `..` components using [`os.path.normpath()`](https://docs.python.org/3/library/os.path.html#os.path.normpath "os.path.normpath")
    . Note that this removes internal `..` components, which may change the meaning of the name if it traverses symbolic links.
    
*   [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse)
     to extract files with absolute paths (in case the name is absolute even after stripping slashes, e.g. `C:/foo` on Windows) or with a drive (e.g. `C:foo` on Windows). This raises [`AbsolutePathError`](https://docs.python.org/3/library/tarfile.html#tarfile.AbsolutePathError "tarfile.AbsolutePathError")
    .
    
*   [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse)
     to extract files whose absolute path (after following symlinks) would end up outside the destination. This raises [`OutsideDestinationError`](https://docs.python.org/3/library/tarfile.html#tarfile.OutsideDestinationError "tarfile.OutsideDestinationError")
    .
    
*   [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse)
     to extract links (hard or soft) whose name refers to the destination directory itself. This raises [`OutsideDestinationError`](https://docs.python.org/3/library/tarfile.html#tarfile.OutsideDestinationError "tarfile.OutsideDestinationError")
    . Note that such files are refused even on platforms that do not support symbolic links.
    
*   Clear high mode bits (setuid, setgid, sticky) and group/other write bits ([`S_IWGRP`](https://docs.python.org/3/library/stat.html#stat.S_IWGRP "stat.S_IWGRP")
     | [`S_IWOTH`](https://docs.python.org/3/library/stat.html#stat.S_IWOTH "stat.S_IWOTH")
    ).
    

Return the modified `TarInfo` member.

Changed in version 3.15: Filenames containing `..` components are now normalized.

Changed in version 3.15.2 (unreleased): Filenames with a drive that are not absolute are now refused.

tarfile.data\_filter(_member_, _path_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "Link to this definition")

Implements the `'data'` filter. In addition to what `tar_filter` does:

*   Normalize link targets ([`TarInfo.linkname`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.linkname "tarfile.TarInfo.linkname")
    ) using [`os.path.normpath()`](https://docs.python.org/3/library/os.path.html#os.path.normpath "os.path.normpath")
    . Note that this removes internal `..` components, which may change the meaning of the link if the path in `TarInfo.linkname` traverses symbolic links.
    
*   [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse)
     to extract links (hard or soft) that link to absolute paths or to paths with a drive, or ones that link outside the destination.
    
    This raises [`AbsoluteLinkError`](https://docs.python.org/3/library/tarfile.html#tarfile.AbsoluteLinkError "tarfile.AbsoluteLinkError")
     or [`LinkOutsideDestinationError`](https://docs.python.org/3/library/tarfile.html#tarfile.LinkOutsideDestinationError "tarfile.LinkOutsideDestinationError")
    .
    
    Note that such files are refused even on platforms that do not support symbolic links.
    
*   [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse)
     to extract device files (including pipes). This raises [`SpecialFileError`](https://docs.python.org/3/library/tarfile.html#tarfile.SpecialFileError "tarfile.SpecialFileError")
    .
    
*   For regular files, including hard links:
    
    *   Set the owner read and write permissions ([`S_IRUSR`](https://docs.python.org/3/library/stat.html#stat.S_IRUSR "stat.S_IRUSR")
         | [`S_IWUSR`](https://docs.python.org/3/library/stat.html#stat.S_IWUSR "stat.S_IWUSR")
        ).
        
    *   Remove the group & other executable permission ([`S_IXGRP`](https://docs.python.org/3/library/stat.html#stat.S_IXGRP "stat.S_IXGRP")
         | [`S_IXOTH`](https://docs.python.org/3/library/stat.html#stat.S_IXOTH "stat.S_IXOTH")
        ) if the owner doesn’t have it ([`S_IXUSR`](https://docs.python.org/3/library/stat.html#stat.S_IXUSR "stat.S_IXUSR")
        ).
        
*   For other files (directories), set `mode` to `None`, so that extraction methods skip applying permission bits.
    
*   Set user and group info (`uid`, `gid`, `uname`, `gname`) to `None`, so that extraction methods skip setting it.
    

Return the modified `TarInfo` member.

Note that this filter does not block _all_ dangerous archive features. See [Hints for further verification](https://docs.python.org/3/library/tarfile.html#tarfile-further-verification)
 for details.

Changed in version 3.15: Link targets are now normalized.

Changed in version 3.15.2 (unreleased): Link targets with a drive that are not absolute are now refused.

### Filter errors[¶](https://docs.python.org/3/library/tarfile.html#filter-errors "Link to this heading")

When a filter refuses to extract a file, it will raise an appropriate exception, a subclass of [`FilterError`](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "tarfile.FilterError")
. This will abort the extraction if [`TarFile.errorlevel`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel")
 is 1 or more. With `errorlevel=0` the error will be logged and the member will be skipped, but extraction will continue.

### Hints for further verification[¶](https://docs.python.org/3/library/tarfile.html#hints-for-further-verification "Link to this heading")

Even with `filter='data'`, _tarfile_ is not suited for extracting untrusted files without prior inspection. Among other issues, the pre-defined filters do not prevent denial-of-service attacks. Users should do additional checks.

Here is an incomplete list of things to consider:

*   Extract to a [`new temporary directory`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp")
     to prevent e.g. exploiting pre-existing links, and to make it easier to clean up after a failed extraction.
    
*   Disallow symbolic links if you do not need the functionality.
    
*   When working with untrusted data, use external (e.g. OS-level) limits on disk, memory and CPU usage.
    
*   Check filenames against an allow-list of characters (to filter out control characters, confusables, foreign path separators, and so on).
    
*   Check that filenames have expected extensions (discouraging files that execute when you “click on them”, or extension-less files like Windows special device names).
    
*   Limit the number of extracted files, total size of extracted data, filename length (including symlink length), and size of individual files.
    
*   Check for files that would be shadowed on case-insensitive filesystems.
    

Also note that:

*   Tar files may contain multiple versions of the same file. Later ones are expected to overwrite any earlier ones. This feature is crucial to allow updating tape archives, but can be abused maliciously.
    
*   _tarfile_ does not protect against issues with “live” data, e.g. an attacker tinkering with the destination (or source) directory while extraction (or archiving) is in progress.
    

### Supporting older Python versions[¶](https://docs.python.org/3/library/tarfile.html#supporting-older-python-versions "Link to this heading")

Extraction filters were added to Python 3.12, but may be backported to older versions as security updates. To check whether the feature is available, use e.g. `hasattr(tarfile, 'data_filter')` rather than checking the Python version.

The following examples show how to support Python versions with and without the feature. Note that setting `extraction_filter` will affect any subsequent operations.

*   Fully trusted archive:
    
    Copy
    
    my\_tarfile.extraction\_filter \= (lambda member, path: member)
    my\_tarfile.extractall()
    
*   Use the `'data'` filter if available, but revert to Python 3.11 behavior (`'fully_trusted'`) if this feature is not available:
    
    Copy
    
    my\_tarfile.extraction\_filter \= getattr(tarfile, 'data\_filter',
                                           (lambda member, path: member))
    my\_tarfile.extractall()
    
*   Use the `'data'` filter; _fail_ if it is not available:
    
    Copy
    
    my\_tarfile.extractall(filter\=tarfile.data\_filter)
    
    or:
    
    Copy
    
    my\_tarfile.extraction\_filter \= tarfile.data\_filter
    my\_tarfile.extractall()
    
*   Use the `'data'` filter; _warn_ if it is not available:
    
    Copy
    
    if hasattr(tarfile, 'data\_filter'):
        my\_tarfile.extractall(filter\='data')
    else:
        \# remove this when no longer needed
        warn\_the\_user('Extracting may be unsafe; consider updating Python')
        my\_tarfile.extractall()
    

### Stateful extraction filter example[¶](https://docs.python.org/3/library/tarfile.html#stateful-extraction-filter-example "Link to this heading")

While _tarfile_’s extraction methods take a simple _filter_ callable, custom filters may be more complex objects with an internal state. It may be useful to write these as context managers, to be used like this:

Copy

with StatefulFilter() as filter\_func:
    tar.extractall(path, filter\=filter\_func)

Such a filter can be written as, for example:

Copy

class StatefulFilter:
    def \_\_init\_\_(self):
        self.file\_count \= 0

    def \_\_enter\_\_(self):
        return self

    def \_\_call\_\_(self, member, path):
        self.file\_count += 1
        return member

    def \_\_exit\_\_(self, \*exc\_info):
        print(f'{self.file\_count} files extracted')

Command-Line Interface[¶](https://docs.python.org/3/library/tarfile.html#command-line-interface "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Added in version 3.4.

The `tarfile` module provides a simple command-line interface to interact with tar archives.

If you want to create a new tar archive, specify its name after the [`-c`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-c)
 option and then list the filename(s) that should be included:

Copy

$ python \-m tarfile \-c monty.tar  spam.txt eggs.txt

Passing a directory is also acceptable:

Copy

$ python \-m tarfile \-c monty.tar life-of-brian\_1979/

If you want to extract a tar archive into the current directory, use the [`-e`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-e)
 option:

Copy

$ python \-m tarfile \-e monty.tar

You can also extract a tar archive into a different directory by passing the directory’s name:

Copy

$ python \-m tarfile \-e monty.tar  other-dir/

For a list of the files in a tar archive, use the [`-l`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-l)
 option:

Copy

$ python \-m tarfile \-l monty.tar

### Command-line options[¶](https://docs.python.org/3/library/tarfile.html#command-line-options "Link to this heading")

\-l <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-l "Link to this definition")

\--list <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-list "Link to this definition")

List files in a tarfile.

\-c <tarfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-c "Link to this definition")

\--create <tarfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-create "Link to this definition")

Create tarfile from source files.

\-e <tarfile> \[<output\_dir>\][¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-e "Link to this definition")

\--extract <tarfile> \[<output\_dir>\][¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-extract "Link to this definition")

Extract tarfile into the current directory if _output\_dir_ is not specified.

\-t <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-t "Link to this definition")

\--test <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-test "Link to this definition")

Test whether the tarfile is valid or not.

\-v, \--verbose[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-v "Link to this definition")

Verbose output.

\--filter <filtername>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-filter "Link to this definition")

Specifies the _filter_ for `--extract`. See [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter)
 for details. Only string names are accepted (that is, `fully_trusted`, `tar`, and `data`).

Examples[¶](https://docs.python.org/3/library/tarfile.html#examples "Link to this heading")

--------------------------------------------------------------------------------------------

### Reading examples[¶](https://docs.python.org/3/library/tarfile.html#reading-examples "Link to this heading")

How to extract an entire tar archive to the current working directory:

Copy

import tarfile
tar \= tarfile.open("sample.tar.gz")
tar.extractall(filter\='data')
tar.close()

How to extract a subset of a tar archive with [`TarFile.extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
 using a generator function instead of a list:

Copy

import os
import tarfile

def py\_files(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)\[1\] \== ".py":
            yield tarinfo

tar \= tarfile.open("sample.tar.gz")
tar.extractall(members\=py\_files(tar))
tar.close()

How to read a gzip compressed tar archive and display some member information:

Copy

import tarfile
tar \= tarfile.open("sample.tar.gz", "r:gz")
for tarinfo in tar:
    print(tarinfo.name, "is", tarinfo.size, "bytes in size and is ", end\="")
    if tarinfo.isreg():
        print("a regular file.")
    elif tarinfo.isdir():
        print("a directory.")
    else:
        print("something else.")
tar.close()

### Writing examples[¶](https://docs.python.org/3/library/tarfile.html#writing-examples "Link to this heading")

How to create an uncompressed tar archive from a list of filenames:

Copy

import tarfile
tar \= tarfile.open("sample.tar", "w")
for name in \["foo", "bar", "quux"\]:
    tar.add(name)
tar.close()

The same example using the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement:

Copy

import tarfile
with tarfile.open("sample.tar", "w") as tar:
    for name in \["foo", "bar", "quux"\]:
        tar.add(name)

How to create and write an archive to stdout using [`sys.stdout.buffer`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 in the _fileobj_ parameter in [`open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open")
:

Copy

import sys
import tarfile
with tarfile.open("sample.tar.gz", "w|gz", fileobj\=sys.stdout.buffer) as tar:
    for name in \["foo", "bar", "quux"\]:
        tar.add(name)

How to create an archive and reset the user information using the _filter_ parameter in [`TarFile.add()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "tarfile.TarFile.add")
:

Copy

import tarfile
def reset(tarinfo):
    tarinfo.uid \= tarinfo.gid \= 0
    tarinfo.uname \= tarinfo.gname \= "root"
    return tarinfo
tar \= tarfile.open("sample.tar.gz", "w:gz")
tar.add("foo", filter\=reset)
tar.close()

Supported tar formats[¶](https://docs.python.org/3/library/tarfile.html#supported-tar-formats "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

There are three tar formats that can be created with the `tarfile` module:

*   The POSIX.1-1988 ustar format ([`USTAR_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.USTAR_FORMAT "tarfile.USTAR_FORMAT")
    ). It supports filenames up to a length of at best 256 characters and linknames up to 100 characters. The maximum file size is 8 GiB. This is an old and limited but widely supported format.
    
*   The GNU tar format ([`GNU_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT")
    ). It supports long filenames and linknames, files bigger than 8 GiB and sparse files. It is the de facto standard on GNU/Linux systems. `tarfile` fully supports the GNU tar extensions for long names, sparse file support is read-only.
    
*   The POSIX.1-2001 pax format ([`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")
    ). It is the most flexible format with virtually no limits. It supports long filenames and linknames, large files and stores pathnames in a portable way. Modern tar implementations, including GNU tar, bsdtar/libarchive and star, fully support extended _pax_ features; some old or unmaintained libraries may not, but should treat _pax_ archives as if they were in the universally supported _ustar_ format. It is the current default format for new archives.
    
    It extends the existing _ustar_ format with extra headers for information that cannot be stored otherwise. There are two flavours of pax headers: Extended headers only affect the subsequent file header, global headers are valid for the complete archive and affect all following files. All the data in a pax header is encoded in _UTF-8_ for portability reasons.
    

There are some more variants of the tar format which can be read, but not created:

*   The ancient V7 format. This is the first tar format from Unix Seventh Edition, storing only regular files and directories. Names must not be longer than 100 characters, there is no user/group name information. Some archives have miscalculated header checksums in case of fields with non-ASCII characters.
    
*   The SunOS tar extended format. This format is a variant of the POSIX.1-2001 pax format, but is not compatible.
    

Unicode issues[¶](https://docs.python.org/3/library/tarfile.html#unicode-issues "Link to this heading")

--------------------------------------------------------------------------------------------------------

The tar format was originally conceived to make backups on tape drives with the main focus on preserving file system information. Nowadays tar archives are commonly used for file distribution and exchanging archives over networks. One problem of the original format (which is the basis of all other formats) is that there is no concept of supporting different character encodings. For example, an ordinary tar archive created on a _UTF-8_ system cannot be read correctly on a _Latin-1_ system if it contains non-_ASCII_ characters. Textual metadata (like filenames, linknames, user/group names) will appear damaged. Unfortunately, there is no way to autodetect the encoding of an archive. The pax format was designed to solve this problem. It stores non-ASCII metadata using the universal character encoding _UTF-8_.

The details of character conversion in `tarfile` are controlled by the _encoding_ and _errors_ keyword arguments of the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 class.

_encoding_ defines the character encoding to use for the metadata in the archive. The default value is [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
 or `'ascii'` as a fallback. Depending on whether the archive is read or written, the metadata must be either decoded or encoded. If _encoding_ is not set appropriately, this conversion may fail.

The _errors_ argument defines how characters are treated that cannot be converted. Possible values are listed in section [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers)
. The default scheme is `'surrogateescape'` which Python also uses for its file system calls, see [File Names, Command Line Arguments, and Environment Variables](https://docs.python.org/3/library/os.html#os-filenames)
.

For [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")
 archives (the default), _encoding_ is generally not needed because all the metadata is stored using _UTF-8_. _encoding_ is only used in the rare cases when binary pax headers are decoded or when strings with surrogate characters are stored.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html#)
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

[`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html "previous chapter")

#### Next topic

[File Formats](https://docs.python.org/3/library/fileformats.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tarfile+%E2%80%94+Read+and+write+tar+archive+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftarfile.html&pagesource=library%2Ftarfile.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tarfile.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/fileformats.html "File Formats")
     |
*   [previous](https://docs.python.org/3/library/zipfile.html "zipfile — Work with ZIP archives")
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
*   [`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html)
    
*    
    
    |
*   Theme Auto Light Dark |