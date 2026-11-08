### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tarfile.html "tarfile — Read and write tar archive files")
     |
*   [previous](https://docs.python.org/3/library/lzma.html "lzma — Compression using the LZMA algorithm")
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
*   [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`zipfile` — Work with ZIP archives[¶](https://docs.python.org/3/library/zipfile.html#module-zipfile "Link to this heading")

============================================================================================================================

**Source code:** [Lib/zipfile/](https://github.com/python/cpython/tree/3.15/Lib/zipfile/)

* * *

The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file. Any advanced use of this module will require an understanding of the format, as defined in [PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)
.

This module does not handle multipart ZIP files. It can handle ZIP files that use the ZIP64 extensions (that is ZIP files that are more than 4 GiB in size). It supports decryption of encrypted files in ZIP archives, but it cannot create an encrypted file. Decryption is extremely slow as it is implemented in native Python rather than C.

Handling compressed archives requires [optional modules](https://docs.python.org/3/glossary.html#term-optional-module)
 such as [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")
, [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
, [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
, and [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.")
. If any of them are missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements)
.

The module defines the following items:

exception zipfile.BadZipFile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipFile "Link to this definition")

The error raised for bad ZIP files.

Added in version 3.2.

exception zipfile.BadZipfile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipfile "Link to this definition")

Alias of [`BadZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipFile "zipfile.BadZipFile")
, for compatibility with older Python versions.

Deprecated since version 3.2.

exception zipfile.LargeZipFile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.LargeZipFile "Link to this definition")

The error raised when a ZIP file would require ZIP64 functionality but that has not been enabled.

class zipfile.ZipFile

The class for reading and writing ZIP files. See section [ZipFile objects](https://docs.python.org/3/library/zipfile.html#zipfile-objects)
 for constructor details.

class zipfile.Path

Class that implements a subset of the interface provided by [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
, including the full [`importlib.resources.abc.Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable")
 interface.

Added in version 3.8.

class zipfile.PyZipFile

Class for creating ZIP archives containing Python libraries.

class zipfile.ZipInfo(_filename\='NoName'_, _date\_time\=(1980, 1, 1, 0, 0, 0)_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "Link to this definition")

Class used to represent information about a member of an archive. Instances of this class are returned by the [`getinfo()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.getinfo "zipfile.ZipFile.getinfo")
 and [`infolist()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist "zipfile.ZipFile.infolist")
 methods of [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile")
 objects. Most users of the `zipfile` module will not need to create these, but only use those created by this module. _filename_ should be the full name of the archive member, and _date\_time_ should be a tuple containing six fields which describe the time of the last modification to the file; the fields are described in section [ZipInfo objects](https://docs.python.org/3/library/zipfile.html#zipinfo-objects)
.

Changed in version 3.13: A public `compress_level` attribute has been added to expose the formerly protected `_compresslevel`. The older protected name continues to work as a property for backwards compatibility.

\_for\_archive(_archive_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo._for_archive "Link to this definition")

Resolve the date\_time, compression attributes, and external attributes to suitable defaults as used by [`ZipFile.writestr()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.writestr "zipfile.ZipFile.writestr")
.

Returns self for chaining.

Added in version 3.14.

zipfile.is\_zipfile(_filename_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.is_zipfile "Link to this definition")

Returns `True` if _filename_ is a valid ZIP file based on its magic number, otherwise returns `False`. _filename_ may be a file or file-like object too.

Changed in version 3.1: Support for file and file-like objects.

zipfile.ZIP\_STORED[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "Link to this definition")

The numeric constant for an uncompressed archive member.

zipfile.ZIP\_DEFLATED[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "Link to this definition")

The numeric constant for the usual ZIP compression method. This requires the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")
 module.

zipfile.ZIP\_BZIP2[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "Link to this definition")

The numeric constant for the BZIP2 compression method. This requires the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
 module.

Added in version 3.3.

zipfile.ZIP\_LZMA[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "Link to this definition")

The numeric constant for the LZMA compression method. This requires the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
 module.

Added in version 3.3.

zipfile.ZIP\_ZSTANDARD[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "Link to this definition")

The numeric constant for Zstandard compression. This requires the [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.")
 module.

Note

In APPNOTE 6.3.7, the method ID `20` was assigned to Zstandard compression. This was changed in APPNOTE 6.3.8 to method ID `93` to avoid conflicts, with method ID `20` being deprecated. For compatibility, the `zipfile` module reads both method IDs but will only write data with method ID `93`.

Added in version 3.14.

Note

The ZIP file format specification has included support for bzip2 compression since 2001, for LZMA compression since 2006, and Zstandard compression since 2020. However, some tools (including older Python releases) do not support these compression methods, and may either refuse to process the ZIP file altogether, or fail to extract individual files.

See also

[PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)

Documentation on the ZIP file format by Phil Katz, the creator of the format and algorithms used.

[Info-ZIP Home Page](https://infozip.sourceforge.net/)

Information about the Info-ZIP project’s ZIP archive programs and development libraries.

ZipFile objects[¶](https://docs.python.org/3/library/zipfile.html#zipfile-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------

class zipfile.ZipFile(_file_, _mode\='r'_, _compression\=ZIP\_STORED_, _allowZip64\=True_, _compresslevel\=None_, _\*_, _strict\_timestamps\=True_, _metadata\_encoding\=None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "Link to this definition")

Open a ZIP file, where _file_ can be a path to a file (a string), a file-like object or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

The _mode_ parameter should be `'r'` to read an existing file, `'w'` to truncate and write a new file, `'a'` to append to an existing file, or `'x'` to exclusively create and write a new file. If _mode_ is `'x'` and _file_ refers to an existing file, a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")
 will be raised. If _mode_ is `'a'` and _file_ refers to an existing ZIP file, then additional files are added to it. If _file_ does not refer to a ZIP file, then a new ZIP archive is appended to the file. This is meant for adding a ZIP archive to another file (such as `python.exe`). If _mode_ is `'a'` and the file does not exist at all, it is created. If _mode_ is `'r'` or `'a'`, the file should be seekable.

_compression_ is the ZIP compression method to use when writing the archive, and should be [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED")
, [`ZIP_DEFLATED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "zipfile.ZIP_DEFLATED")
, [`ZIP_BZIP2`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "zipfile.ZIP_BZIP2")
, [`ZIP_LZMA`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "zipfile.ZIP_LZMA")
, or [`ZIP_ZSTANDARD`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "zipfile.ZIP_ZSTANDARD")
; unrecognized values will cause [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
 to be raised. If `ZIP_DEFLATED`, `ZIP_BZIP2`, `ZIP_LZMA`, or `ZIP_ZSTANDARD` is specified but the corresponding module ([`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")
, [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
, [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
, or [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.")
) is not available, [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised. The default is `ZIP_STORED`.

If _allowZip64_ is `True` (the default) zipfile will create ZIP files that use the ZIP64 extensions when the zipfile is larger than 4 GiB. If it is `false` `zipfile` will raise an exception when the ZIP file would require ZIP64 extensions.

The _compresslevel_ parameter controls the compression level to use when writing files to the archive. When using [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED")
 or [`ZIP_LZMA`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "zipfile.ZIP_LZMA")
 it has no effect. When using [`ZIP_DEFLATED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "zipfile.ZIP_DEFLATED")
 integers `0` through `9` are accepted (see [`zlib`](https://docs.python.org/3/library/zlib.html#zlib.compressobj "zlib.compressobj")
 for more information). When using [`ZIP_BZIP2`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "zipfile.ZIP_BZIP2")
 integers `1` through `9` are accepted (see [`bz2`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
 for more information). When using [`ZIP_ZSTANDARD`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "zipfile.ZIP_ZSTANDARD")
 integers `-131072` through `22` are commonly accepted (see [`CompressionParameter.compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level")
 for more on retrieving valid values and their meaning).

The _strict\_timestamps_ argument, when set to `False`, allows to zip files older than 1980-01-01 at the cost of setting the timestamp to 1980-01-01. Similar behavior occurs with files newer than 2107-12-31, the timestamp is also set to the limit.

When mode is `'r'`, _metadata\_encoding_ may be set to the name of a codec, which will be used to decode metadata such as the names of members and ZIP comments.

If the file is created with mode `'w'`, `'x'` or `'a'` and then [`closed`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.close "zipfile.ZipFile.close")
 without adding any files to the archive, the appropriate ZIP structures for an empty archive will be written to the file.

ZipFile is also a context manager and therefore supports the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement. In the example, _myzip_ is closed after the `with` statement’s suite is finished—even if an exception occurs:

Copy

with ZipFile('spam.zip', 'w') as myzip:
    myzip.write('eggs.txt')

Note

_metadata\_encoding_ is an instance-wide setting for the ZipFile. It is not possible to set this on a per-member basis.

This attribute is a workaround for legacy implementations which produce archives with names in the current locale encoding or code page (mostly on Windows). According to the .ZIP standard, the encoding of metadata may be specified to be either IBM code page (default) or UTF-8 by a flag in the archive header. That flag takes precedence over _metadata\_encoding_, which is a Python-specific extension.

Changed in version 3.2: Added the ability to use `ZipFile` as a context manager.

Changed in version 3.3: Added support for [`bzip2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
 and [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
 compression.

Changed in version 3.4: ZIP64 extensions are enabled by default.

Changed in version 3.5: Added support for writing to unseekable streams. Added support for the `'x'` mode.

Changed in version 3.6: Previously, a plain [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 was raised for unrecognized compression values.

Changed in version 3.6.2: The _file_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.7: Add the _compresslevel_ parameter.

Changed in version 3.8: The _strict\_timestamps_ keyword-only parameter.

Changed in version 3.11: Added support for specifying member name encoding for reading metadata in the zipfile’s directory and file headers.

ZipFile.close()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.close "Link to this definition")

Close the archive file. You must call `close()` before exiting your program or essential records will not be written.

ZipFile.getinfo(_name_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.getinfo "Link to this definition")

Return a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 object with information about the archive member _name_. Calling `getinfo()` for a name not currently contained in the archive will raise a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
.

ZipFile.infolist()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist "Link to this definition")

Return a list containing a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 object for each member of the archive. The objects are in the same order as their entries in the actual ZIP file on disk if an existing archive was opened.

ZipFile.namelist()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.namelist "Link to this definition")

Return a list of archive members by name.

ZipFile.open(_name_, _mode\='r'_, _pwd\=None_, _\*_, _force\_zip64\=False_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "Link to this definition")

Access a member of the archive as a binary file-like object. _name_ can be either the name of a file within the archive or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 object. The _mode_ parameter, if included, must be `'r'` (the default) or `'w'`. _pwd_ is the password used to decrypt encrypted ZIP files as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

`open()` is also a context manager and therefore supports the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement:

Copy

with ZipFile('spam.zip') as myzip:
    with myzip.open('eggs.txt') as myfile:
        print(myfile.read())

With _mode_ `'r'` the file-like object (`ZipExtFile`) is read-only and provides the following methods: [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read")
, [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline")
, [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines")
, [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek")
, [`tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell")
, [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#container.__iter__ "container.__iter__")
, [`__next__()`](https://docs.python.org/3/builtins/stdtypes.html#iterator.__next__ "iterator.__next__")
. These objects can operate independently of the ZipFile.

With `mode='w'`, a writable file handle is returned, which supports the [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write")
 method. While a writable file handle is open, attempting to read or write other files in the ZIP file will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
.

In both cases the file-like object has also attributes `name`, which is equivalent to the name of a file within the archive, and `mode`, which is `'rb'` or `'wb'` depending on the input mode.

When writing a file, if the file size is not known in advance but may exceed 2 GiB, pass `force_zip64=True` to ensure that the header format is capable of supporting large files. If the file size is known in advance, construct a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 object with [`file_size`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.file_size "zipfile.ZipInfo.file_size")
 set, and use that as the _name_ parameter.

Note

The `open()`, [`read()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.read "zipfile.ZipFile.read")
 and [`extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract")
 methods can take a filename or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 object. You will appreciate this when trying to read a ZIP file that contains members with duplicate names.

Changed in version 3.6: Removed support of `mode='U'`. Use [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 for reading compressed text files in [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines)
 mode.

Changed in version 3.6: `ZipFile.open()` can now be used to write files into the archive with the `mode='w'` option.

Changed in version 3.6: Calling `open()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. Previously, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 was raised.

Changed in version 3.13: Added attributes `name` and `mode` for the writeable file-like object. The value of the `mode` attribute for the readable file-like object was changed from `'r'` to `'rb'`.

ZipFile.extract(_member_, _path\=None_, _pwd\=None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "Link to this definition")

Extract a member from the archive to the current working directory; _member_ must be its full name or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 object. Its file information is extracted as accurately as possible. _path_ specifies a different directory to extract to. _member_ can be a filename or a `ZipInfo` object. _pwd_ is the password used for encrypted files as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

Returns the normalized path created (a directory or new file).

Note

If a member filename is an absolute path, a drive/UNC sharepoint and leading (back)slashes will be stripped, e.g.: `///foo/bar` becomes `foo/bar` on Unix, and `C:\foo\bar` becomes `foo\bar` on Windows. And all `".."` components in a member filename will be removed, e.g.: `../../foo../../ba..r` becomes `foo../ba..r`. On Windows illegal characters (`:`, `<`, `>`, `|`, `"`, `?`, and `*`) replaced by underscore (`_`).

Changed in version 3.6: Calling `extract()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. Previously, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 was raised.

Changed in version 3.6.2: The _path_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

ZipFile.extractall(_path\=None_, _members\=None_, _pwd\=None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extractall "Link to this definition")

Extract all members from the archive to the current working directory. _path_ specifies a different directory to extract to. _members_ is optional and must be a subset of the list returned by [`namelist()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.namelist "zipfile.ZipFile.namelist")
. _pwd_ is the password used for encrypted files as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

Warning

Never extract archives from untrusted sources without prior inspection. It is possible that files are created outside of _path_, for example, members that have absolute filenames or filenames with “..” components. This module attempts to prevent that. See [`extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract")
 note.

Changed in version 3.6: Calling `extractall()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. Previously, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 was raised.

Changed in version 3.6.2: The _path_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

ZipFile.printdir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.printdir "Link to this definition")

Print a table of contents for the archive to `sys.stdout`.

ZipFile.setpassword(_pwd_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.setpassword "Link to this definition")

Set _pwd_ (a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object) as default password to extract encrypted files.

ZipFile.read(_name_, _pwd\=None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.read "Link to this definition")

Return the bytes of the file _name_ in the archive. _name_ is the name of the file in the archive, or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 object. The archive must be open for read or append. _pwd_ is the password used for encrypted files as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object and, if specified, overrides the default password set with [`setpassword()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.setpassword "zipfile.ZipFile.setpassword")
. Calling `read()` on a ZipFile that uses a compression method other than [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED")
, [`ZIP_DEFLATED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "zipfile.ZIP_DEFLATED")
, [`ZIP_BZIP2`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "zipfile.ZIP_BZIP2")
, [`ZIP_LZMA`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "zipfile.ZIP_LZMA")
, or [`ZIP_ZSTANDARD`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "zipfile.ZIP_ZSTANDARD")
 will raise a [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
. An error will also be raised if the corresponding compression module is not available.

Changed in version 3.6: Calling `read()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. Previously, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 was raised.

ZipFile.testzip()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.testzip "Link to this definition")

Read all the files in the archive and check their CRC’s and file headers. Return the name of the first bad file, or else return `None`.

Changed in version 3.6: Calling `testzip()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. Previously, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 was raised.

ZipFile.write(_filename_, _arcname\=None_, _compress\_type\=None_, _compresslevel\=None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.write "Link to this definition")

Write the file named _filename_ to the archive, giving it the archive name _arcname_ (by default, this will be the same as _filename_, but without a drive letter and with leading path separators removed). If given, _compress\_type_ overrides the value given for the _compression_ parameter to the constructor for the new entry. Similarly, _compresslevel_ will override the constructor if given. The archive must be open with mode `'w'`, `'x'` or `'a'`.

Note

The ZIP file standard historically did not specify a metadata encoding, but strongly recommended CP437 (the original IBM PC encoding) for interoperability. Recent versions allow use of UTF-8 (only). In this module, UTF-8 will automatically be used to write the member names if they contain any non-ASCII characters. It is not possible to write member names in any encoding other than ASCII or UTF-8.

Note

Archive names should be relative to the archive root, that is, they should not start with a path separator.

Note

If `arcname` (or `filename`, if `arcname` is not given) contains a null byte, the name of the file in the archive will be truncated at the null byte.

Note

A leading slash in the filename may lead to the archive being impossible to open in some zip programs on Windows systems.

Changed in version 3.6: Calling `write()` on a ZipFile created with mode `'r'` or a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. Previously, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 was raised.

ZipFile.writestr(_zinfo\_or\_arcname_, _data_, _compress\_type\=None_, _compresslevel\=None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.writestr "Link to this definition")

Write a file into the archive. The contents is _data_, which may be either a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 instance; if it is a `str`, it is encoded as UTF-8 first. _zinfo\_or\_arcname_ is either the file name it will be given in the archive, or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 instance. If it’s an instance, at least the filename, date, and time must be given. If it’s a name, the date and time is set to the current date and time. The archive must be opened with mode `'w'`, `'x'` or `'a'`.

If given, _compress\_type_ overrides the value given for the _compression_ parameter to the constructor for the new entry, or in the _zinfo\_or\_arcname_ (if that is a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 instance). Similarly, _compresslevel_ will override the constructor if given.

Note

When passing a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 instance as the _zinfo\_or\_arcname_ parameter, the compression method used will be that specified in the _compress\_type_ member of the given `ZipInfo` instance. By default, the `ZipInfo` constructor sets this member to [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED")
.

Changed in version 3.2: The _compress\_type_ argument.

Changed in version 3.6: Calling `writestr()` on a ZipFile created with mode `'r'` or a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. Previously, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 was raised.

Changed in version 3.14: Now respects the `SOURCE_DATE_EPOCH` environment variable. If set, it uses this value as the modification timestamp for the file written into the ZIP archive, instead of using the current time.

ZipFile.mkdir(_zinfo\_or\_directory_, _mode\=511_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.mkdir "Link to this definition")

Create a directory inside the archive. If _zinfo\_or\_directory_ is a string, a directory is created inside the archive with the mode that is specified in the _mode_ argument. If, however, _zinfo\_or\_directory_ is a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 instance then the _mode_ argument is ignored.

The archive must be opened with mode `'w'`, `'x'` or `'a'`.

Added in version 3.11.

The following data attributes are also available:

ZipFile.filename[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.filename "Link to this definition")

Name of the ZIP file.

ZipFile.debug[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.debug "Link to this definition")

The level of debug output to use. This may be set from `0` (the default, no output) to `3` (the most output). Debugging information is written to `sys.stdout`.

ZipFile.comment[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.comment "Link to this definition")

The comment associated with the ZIP file as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. If assigning a comment to a [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile")
 instance created with mode `'w'`, `'x'` or `'a'`, it should be no longer than 65535 bytes. Comments longer than this will be truncated.

Path objects[¶](https://docs.python.org/3/library/zipfile.html#path-objects "Link to this heading")

----------------------------------------------------------------------------------------------------

class zipfile.Path(_root_, _at\=''_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path "Link to this definition")

Construct a Path object from a `root` zipfile (which may be a [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile")
 instance or `file` suitable for passing to the `ZipFile` constructor).

`at` specifies the location of this Path within the zipfile, e.g. ‘dir/file.txt’, ‘dir/’, or ‘’. Defaults to the empty string, indicating the root.

Note

The `Path` class does not sanitize filenames within the ZIP archive. Unlike the [`ZipFile.extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract")
 and [`ZipFile.extractall()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extractall "zipfile.ZipFile.extractall")
 methods, it is the caller’s responsibility to validate or sanitize filenames to prevent path traversal vulnerabilities (for example, absolute paths or paths with “..” components). When handling untrusted archives, consider resolving filenames using [`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath")
 and checking against the target directory with [`os.path.commonpath()`](https://docs.python.org/3/library/os.path.html#os.path.commonpath "os.path.commonpath")
.

Path objects expose the following features of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
 objects:

Path objects are traversable using the `/` operator or `joinpath`.

Path.name[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.name "Link to this definition")

The final path component.

Path.open(_mode\='r'_, _\*_, _pwd_, _\*\*_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.open "Link to this definition")

Invoke [`ZipFile.open()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "zipfile.ZipFile.open")
 on the current path. Allows opening for read or write, text or binary through supported modes: ‘r’, ‘w’, ‘rb’, ‘wb’. Positional and keyword arguments are passed through to [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 when opened as text and ignored otherwise. `pwd` is the `pwd` parameter to `ZipFile.open()`.

Changed in version 3.9: Added support for text and binary modes for open. Default mode is now text.

Changed in version 3.11.2: The `encoding` parameter can be supplied as a positional argument without causing a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. As it could in 3.9. Code needing to be compatible with unpatched 3.10 and 3.11 versions must pass all [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 arguments, `encoding` included, as keywords.

Path.iterdir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.iterdir "Link to this definition")

Enumerate the children of the current directory.

Path.is\_dir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_dir "Link to this definition")

Return `True` if the current context references a directory.

Path.is\_file()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_file "Link to this definition")

Return `True` if the current context references a file.

Path.is\_symlink()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_symlink "Link to this definition")

Return `True` if the current context references a symbolic link.

Added in version 3.12.

Changed in version 3.13: Previously, `is_symlink` would unconditionally return `False`.

Path.exists()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.exists "Link to this definition")

Return `True` if the current context references a file or directory in the zip file.

Path.suffix[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.suffix "Link to this definition")

The last dot-separated portion of the final component, if any. This is commonly called the file extension.

Added in version 3.11: Added `Path.suffix` property.

Path.stem[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.stem "Link to this definition")

The final path component, without its suffix.

Added in version 3.11: Added `Path.stem` property.

Path.suffixes[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.suffixes "Link to this definition")

A list of the path’s suffixes, commonly called file extensions.

Added in version 3.11: Added `Path.suffixes` property.

Path.read\_text(_\*_, _\*\*_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.read_text "Link to this definition")

Read the current file as unicode text. Positional and keyword arguments are passed through to [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 (except `buffer`, which is implied by the context).

Changed in version 3.11.2: The `encoding` parameter can be supplied as a positional argument without causing a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. As it could in 3.9. Code needing to be compatible with unpatched 3.10 and 3.11 versions must pass all [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 arguments, `encoding` included, as keywords.

Path.read\_bytes()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.read_bytes "Link to this definition")

Read the current file as bytes.

Path.joinpath(_\*other_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.joinpath "Link to this definition")

Return a new Path object with each of the _other_ arguments joined. The following are equivalent:

Copy

\>>> Path(...).joinpath('child').joinpath('grandchild')
\>>> Path(...).joinpath('child', 'grandchild')
\>>> Path(...) / 'child' / 'grandchild'

Changed in version 3.10: Prior to 3.10, `joinpath` was undocumented and accepted exactly one parameter.

The [zipp](https://pypi.org/project/zipp/)
 project provides backports of the latest path object functionality to older Pythons. Use `zipp.Path` in place of `zipfile.Path` for early access to changes.

PyZipFile objects[¶](https://docs.python.org/3/library/zipfile.html#pyzipfile-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------

The [`PyZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile "zipfile.PyZipFile")
 constructor takes the same parameters as the [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile")
 constructor, and one additional parameter, _optimize_.

class zipfile.PyZipFile(_file_, _mode\='r'_, _compression\=ZIP\_STORED_, _allowZip64\=True_, _optimize\=\-1_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile "Link to this definition")

Changed in version 3.2: Added the _optimize_ parameter.

Changed in version 3.4: ZIP64 extensions are enabled by default.

Instances have one method in addition to those of [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile")
 objects:

writepy(_pathname_, _basename\=''_, _filterfunc\=None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile.writepy "Link to this definition")

Search for files `*.py` and add the corresponding file to the archive.

If the _optimize_ parameter to `PyZipFile` was not given or `-1`, the corresponding file is a `*.pyc` file, compiling if necessary.

If the _optimize_ parameter to `PyZipFile` was `0`, `1` or `2`, only files with that optimization level (see [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
) are added to the archive, compiling if necessary.

If _pathname_ is a file, the filename must end with `.py`, and just the (corresponding `*.pyc`) file is added at the top level (no path information). If _pathname_ is a file that does not end with `.py`, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 will be raised. If it is a directory, and the directory is not a package directory, then all the files `*.pyc` are added at the top level. If the directory is a package directory, then all `*.pyc` are added under the package name as a file path, and if any subdirectories are package directories, all of these are added recursively in sorted order.

_basename_ is intended for internal use only.

_filterfunc_, if given, must be a function taking a single string argument. It will be passed each path (including each individual full file path) before it is added to the archive. If _filterfunc_ returns a false value, the path will not be added, and if it is a directory its contents will be ignored. For example, if our test files are all either in `test` directories or start with the string `test_`, we can use a _filterfunc_ to exclude them:

Copy

\>>> zf \= PyZipFile('myprog.zip', 'w')
\>>> def notests(s):
...     fn \= os.path.basename(s)
...     return (not (fn \== 'test' or fn.startswith('test\_')))
...
\>>> zf.writepy('myprog', filterfunc\=notests)

The `writepy()` method makes archives with file names like this:

Copy

string.pyc                   \# Top level name
test/\_\_init\_\_.pyc            \# Package directory
test/testall.pyc             \# Module test.testall
test/bogus/\_\_init\_\_.pyc      \# Subpackage directory
test/bogus/myfile.pyc        \# Submodule test.bogus.myfile

Changed in version 3.4: Added the _filterfunc_ parameter.

Changed in version 3.6.2: The _pathname_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.7: Recursion sorts directory entries.

ZipInfo objects[¶](https://docs.python.org/3/library/zipfile.html#zipinfo-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------

Instances of the [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 class are returned by the [`getinfo()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.getinfo "zipfile.ZipFile.getinfo")
 and [`infolist()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist "zipfile.ZipFile.infolist")
 methods of [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile")
 objects. Each object stores information about a single member of the ZIP archive.

There is one classmethod to make a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 instance for a filesystem file:

classmethod ZipInfo.from\_file(_filename_, _arcname\=None_, _\*_, _strict\_timestamps\=True_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.from_file "Link to this definition")

Construct a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
 instance for a file on the filesystem, in preparation for adding it to a zip file.

_filename_ should be the path to a file or directory on the filesystem.

If _arcname_ is specified, it is used as the name within the archive. If _arcname_ is not specified, the name will be the same as _filename_, but with any drive letter and leading path separators removed.

The _strict\_timestamps_ argument, when set to `False`, allows to zip files older than 1980-01-01 at the cost of setting the timestamp to 1980-01-01. Similar behavior occurs with files newer than 2107-12-31, the timestamp is also set to the limit.

Added in version 3.6.

Changed in version 3.6.2: The _filename_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.8: Added the _strict\_timestamps_ keyword-only parameter.

Instances have the following methods and attributes:

ZipInfo.is\_dir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.is_dir "Link to this definition")

Return `True` if this archive member is a directory.

This uses the entry’s name: directories should always end with `/`.

Added in version 3.6.

ZipInfo.filename[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.filename "Link to this definition")

Name of the file in the archive.

ZipInfo.date\_time[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.date_time "Link to this definition")

The time and date of the last modification to the archive member. This is a tuple of six values representing the “last \[modified\] file time” and “last \[modified\] file date” fields from the ZIP file’s central directory.

The tuple contains:

| Index | Value |
| --- | --- |
| `0` | Year (>= 1980) |
| `1` | Month (one-based) |
| `2` | Day of month (one-based) |
| `3` | Hours (zero-based) |
| `4` | Minutes (zero-based) |
| `5` | Seconds (zero-based) |

Note

The ZIP format supports multiple timestamp fields in different locations (central directory, extra fields for NTFS/UNIX systems, etc.). This attribute specifically returns the timestamp from the central directory. The central directory timestamp format in ZIP files does not support timestamps before 1980. While some extra field formats (such as UNIX timestamps) can represent earlier dates, this attribute only returns the central directory timestamp.

The central directory timestamp is interpreted as representing local time, rather than UTC time, to match the behavior of other zip tools.

ZipInfo.compress\_type[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.compress_type "Link to this definition")

Type of compression for the archive member.

ZipInfo.comment[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.comment "Link to this definition")

Comment for the individual archive member as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

ZipInfo.extra[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.extra "Link to this definition")

Expansion field data. The [PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)
 contains some comments on the internal structure of the data contained in this [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

ZipInfo.create\_system[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.create_system "Link to this definition")

System which created ZIP archive.

ZipInfo.create\_version[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.create_version "Link to this definition")

PKZIP version which created ZIP archive.

ZipInfo.extract\_version[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.extract_version "Link to this definition")

PKZIP version needed to extract archive.

ZipInfo.reserved[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.reserved "Link to this definition")

Must be zero.

ZipInfo.flag\_bits[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.flag_bits "Link to this definition")

ZIP flag bits.

ZipInfo.volume[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.volume "Link to this definition")

Volume number of file header.

ZipInfo.internal\_attr[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.internal_attr "Link to this definition")

Internal attributes.

ZipInfo.external\_attr[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.external_attr "Link to this definition")

External file attributes.

ZipInfo.header\_offset[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.header_offset "Link to this definition")

Byte offset to the file header.

ZipInfo.CRC[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.CRC "Link to this definition")

CRC-32 of the uncompressed file.

ZipInfo.compress\_size[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.compress_size "Link to this definition")

Size of the compressed data.

ZipInfo.file\_size[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.file_size "Link to this definition")

Size of the uncompressed file.

Command-line interface[¶](https://docs.python.org/3/library/zipfile.html#command-line-interface "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

The `zipfile` module provides a simple command-line interface to interact with ZIP archives.

If you want to create a new ZIP archive, specify its name after the [`-c`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-c)
 option and then list the filename(s) that should be included:

Copy

$ python \-m zipfile \-c monty.zip spam.txt eggs.txt

Passing a directory is also acceptable:

Copy

$ python \-m zipfile \-c monty.zip life-of-brian\_1979/

If you want to extract a ZIP archive into the specified directory, use the [`-e`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e)
 option:

Copy

$ python \-m zipfile \-e monty.zip target-dir/

For a list of the files in a ZIP archive, use the [`-l`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l)
 option:

Copy

$ python \-m zipfile \-l monty.zip

### Command-line options[¶](https://docs.python.org/3/library/zipfile.html#command-line-options "Link to this heading")

\-l <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l "Link to this definition")

\--list <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-list "Link to this definition")

List files in a zipfile.

\-c <zipfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-c "Link to this definition")

\--create <zipfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-create "Link to this definition")

Create zipfile from source files.

\-e <zipfile> <output\_dir>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e "Link to this definition")

\--extract <zipfile> <output\_dir>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-extract "Link to this definition")

Extract zipfile into target directory.

\-t <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-t "Link to this definition")

\--test <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-test "Link to this definition")

Test whether the zipfile is valid or not.

\--metadata-encoding <encoding>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-metadata-encoding "Link to this definition")

Specify encoding of member names for [`-l`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l)
, [`-e`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e)
 and [`-t`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-t)
.

Added in version 3.11.

Decompression pitfalls[¶](https://docs.python.org/3/library/zipfile.html#decompression-pitfalls "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

The extraction in zipfile module might fail due to some pitfalls listed below.

### From file itself[¶](https://docs.python.org/3/library/zipfile.html#from-file-itself "Link to this heading")

Decompression may fail due to incorrect password / CRC checksum / ZIP format or unsupported compression method / decryption.

### File system limitations[¶](https://docs.python.org/3/library/zipfile.html#file-system-limitations "Link to this heading")

Exceeding limitations on different file systems can cause decompression failed. Such as allowable characters in the directory entries, length of the file name, length of the pathname, size of a single file, and number of files, etc.

### Resources limitations[¶](https://docs.python.org/3/library/zipfile.html#resources-limitations "Link to this heading")

The lack of memory or disk volume would lead to decompression failed. For example, decompression bombs (aka [ZIP bomb](https://en.wikipedia.org/wiki/Zip_bomb)
) apply to zipfile library that can cause disk volume exhaustion.

### Interruption[¶](https://docs.python.org/3/library/zipfile.html#interruption "Link to this heading")

Interruption during the decompression, such as pressing control-C or killing the decompression process may result in incomplete decompression of the archive.

### Default behaviors of extraction[¶](https://docs.python.org/3/library/zipfile.html#default-behaviors-of-extraction "Link to this heading")

Not knowing the default extraction behaviors can cause unexpected decompression results. For example, when extracting the same archive twice, it overwrites files without asking.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html#)
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
            

#### Previous topic

[`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html "previous chapter")

#### Next topic

[`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zipfile+%E2%80%94+Work+with+ZIP+archives&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzipfile.html&pagesource=library%2Fzipfile.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/zipfile.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tarfile.html "tarfile — Read and write tar archive files")
     |
*   [previous](https://docs.python.org/3/library/lzma.html "lzma — Compression using the LZMA algorithm")
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
*   [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
    
*    
    
    |
*   Theme Auto Light Dark |