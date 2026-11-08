### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/colorsys.html "colorsys — Conversions between color systems")
     |
*   [previous](https://docs.python.org/3/library/mm.html "Multimedia Services")
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
*   [Multimedia Services](https://docs.python.org/3/library/mm.html)
     »
*   [`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`wave` — Read and write WAV files[¶](https://docs.python.org/3/library/wave.html#module-wave "Link to this heading")

=====================================================================================================================

**Source code:** [Lib/wave.py](https://github.com/python/cpython/tree/3.15/Lib/wave.py)

* * *

The `wave` module provides a convenient interface to the Waveform Audio “WAVE” (or “WAV”) file format.

The module supports uncompressed PCM and IEEE floating-point WAV formats.

Changed in version 3.12: Support for `WAVE_FORMAT_EXTENSIBLE` headers was added, provided that the extended format is `KSDATAFORMAT_SUBTYPE_PCM`.

Changed in version 3.15: Support for reading and writing `WAVE_FORMAT_IEEE_FLOAT` files was added.

The `wave` module defines the following function and exception:

wave.open(_file_, _mode\=None_)[¶](https://docs.python.org/3/library/wave.html#wave.open "Link to this definition")

If _file_ is a string, a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 or a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 open the file by that name, otherwise treat it as a file-like object. _mode_ can be:

`'rb'`

Read only mode.

`'wb'`

Write only mode.

Note that it does not allow read/write WAV files.

A _mode_ of `'rb'` returns a [`Wave_read`](https://docs.python.org/3/library/wave.html#wave.Wave_read "wave.Wave_read")
 object, while a _mode_ of `'wb'` returns a [`Wave_write`](https://docs.python.org/3/library/wave.html#wave.Wave_write "wave.Wave_write")
 object. If _mode_ is omitted and a file-like object is passed as _file_, `file.mode` is used as the default value for _mode_.

If you pass in a file-like object, the wave object will not close it when its `close()` method is called; it is the caller’s responsibility to close the file object.

The `open()` function may be used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement. When the `with` block completes, the [`Wave_read.close()`](https://docs.python.org/3/library/wave.html#wave.Wave_read.close "wave.Wave_read.close")
 or [`Wave_write.close()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.close "wave.Wave_write.close")
 method is called.

Changed in version 3.4: Added support for unseekable files.

Changed in version 3.15: Added support for [path-like objects](https://docs.python.org/3/glossary.html#term-path-like-object)
 and [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
.

exception wave.Error[¶](https://docs.python.org/3/library/wave.html#wave.Error "Link to this definition")

An error raised when something is impossible because it violates the WAV specification or hits an implementation deficiency.

wave.WAVE\_FORMAT\_PCM[¶](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_PCM "Link to this definition")

Format code for uncompressed PCM audio.

wave.WAVE\_FORMAT\_IEEE\_FLOAT[¶](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_IEEE_FLOAT "Link to this definition")

Format code for IEEE floating-point audio.

Added in version 3.15.

wave.WAVE\_FORMAT\_EXTENSIBLE[¶](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_EXTENSIBLE "Link to this definition")

Format code for WAVE extensible headers.

Added in version 3.12.

Wave\_read Objects[¶](https://docs.python.org/3/library/wave.html#wave-read-objects "Link to this heading")

------------------------------------------------------------------------------------------------------------

class wave.Wave\_read[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read "Link to this definition")

Read a WAV file.

Wave\_read objects, as returned by [`open()`](https://docs.python.org/3/library/wave.html#wave.open "wave.open")
, have the following methods:

close()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.close "Link to this definition")

Close the stream if it was opened by `wave`, and make the instance unusable. This is called automatically on object collection.

getnchannels()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.getnchannels "Link to this definition")

Returns number of audio channels (`1` for mono, `2` for stereo).

getsampwidth()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.getsampwidth "Link to this definition")

Returns sample width in bytes.

getframerate()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.getframerate "Link to this definition")

Returns sampling frequency.

getnframes()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.getnframes "Link to this definition")

Returns number of audio frames.

getformat()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.getformat "Link to this definition")

Returns the frame format code.

This is one of [`WAVE_FORMAT_PCM`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_PCM "wave.WAVE_FORMAT_PCM")
, [`WAVE_FORMAT_IEEE_FLOAT`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_IEEE_FLOAT "wave.WAVE_FORMAT_IEEE_FLOAT")
, or [`WAVE_FORMAT_EXTENSIBLE`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_EXTENSIBLE "wave.WAVE_FORMAT_EXTENSIBLE")
.

Added in version 3.15.

getcomptype()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.getcomptype "Link to this definition")

Returns compression type (`'NONE'` is the only supported type).

getcompname()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.getcompname "Link to this definition")

Human-readable version of [`getcomptype()`](https://docs.python.org/3/library/wave.html#wave.Wave_read.getcomptype "wave.Wave_read.getcomptype")
. Usually `'not compressed'` parallels `'NONE'`.

getparams()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.getparams "Link to this definition")

Returns a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
 `(nchannels, sampwidth, framerate, nframes, comptype, compname)`, equivalent to output of the `get*()` methods.

readframes(_n_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.readframes "Link to this definition")

Reads and returns at most _n_ frames of audio, as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

rewind()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.rewind "Link to this definition")

Rewind the file pointer to the beginning of the audio stream.

The following two methods define a term “position” which is compatible between them, and is otherwise implementation dependent.

setpos(_pos_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.setpos "Link to this definition")

Set the file pointer to the specified position.

tell()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_read.tell "Link to this definition")

Return current file pointer position.

Wave\_write Objects[¶](https://docs.python.org/3/library/wave.html#wave-write-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------

class wave.Wave\_write[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write "Link to this definition")

Write a WAV file.

Wave\_write objects, as returned by [`open()`](https://docs.python.org/3/library/wave.html#wave.open "wave.open")
.

For seekable output streams, the `wave` header will automatically be updated to reflect the number of frames actually written. For unseekable streams, the _nframes_ value must be accurate when the first frame data is written. An accurate _nframes_ value can be achieved either by calling [`setnframes()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.setnframes "wave.Wave_write.setnframes")
 or [`setparams()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.setparams "wave.Wave_write.setparams")
 with the number of frames that will be written before [`close()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.close "wave.Wave_write.close")
 is called and then using [`writeframesraw()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.writeframesraw "wave.Wave_write.writeframesraw")
 to write the frame data, or by calling [`writeframes()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.writeframes "wave.Wave_write.writeframes")
 with all of the frame data to be written. In the latter case `writeframes()` will calculate the number of frames in the data and set _nframes_ accordingly before writing the frame data.

Changed in version 3.4: Added support for unseekable files.

Wave\_write objects have the following methods:

close()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.close "Link to this definition")

Make sure _nframes_ is correct, and close the file if it was opened by `wave`. This method is called upon object collection. It will raise an exception if the output stream is not seekable and _nframes_ does not match the number of frames actually written.

setnchannels(_n_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.setnchannels "Link to this definition")

Set the number of channels.

getnchannels()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.getnchannels "Link to this definition")

Return the number of channels.

setsampwidth(_n_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.setsampwidth "Link to this definition")

Set the sample width to _n_ bytes.

For [`WAVE_FORMAT_IEEE_FLOAT`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_IEEE_FLOAT "wave.WAVE_FORMAT_IEEE_FLOAT")
, only 4-byte (32-bit) and 8-byte (64-bit) sample widths are supported.

getsampwidth()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.getsampwidth "Link to this definition")

Return the sample width in bytes.

setframerate(_n_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.setframerate "Link to this definition")

Set the frame rate to _n_.

Changed in version 3.2: A non-integral input to this method is rounded to the nearest integer.

getframerate()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.getframerate "Link to this definition")

Return the frame rate.

setnframes(_n_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.setnframes "Link to this definition")

Set the number of frames to _n_. This will be changed later if the number of frames actually written is different (this update attempt will raise an error if the output stream is not seekable).

getnframes()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.getnframes "Link to this definition")

Return the number of audio frames written so far.

setcomptype(_type_, _name_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.setcomptype "Link to this definition")

Set the compression type and description. At the moment, only compression type `NONE` is supported, meaning no compression.

getcomptype()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.getcomptype "Link to this definition")

Return the compression type (`'NONE'`).

getcompname()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.getcompname "Link to this definition")

Return the human-readable compression type name.

setformat(_format_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.setformat "Link to this definition")

Set the frame format code.

Supported values are [`WAVE_FORMAT_PCM`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_PCM "wave.WAVE_FORMAT_PCM")
 and [`WAVE_FORMAT_IEEE_FLOAT`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_IEEE_FLOAT "wave.WAVE_FORMAT_IEEE_FLOAT")
.

When setting [`WAVE_FORMAT_IEEE_FLOAT`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_IEEE_FLOAT "wave.WAVE_FORMAT_IEEE_FLOAT")
, the sample width must be 4 or 8 bytes.

Added in version 3.15.

getformat()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.getformat "Link to this definition")

Return the current frame format code.

Added in version 3.15.

setparams(_tuple_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.setparams "Link to this definition")

The _tuple_ should be `(nchannels, sampwidth, framerate, nframes, comptype, compname, format)`, with values valid for the `set*()` methods. Sets all parameters.

For backwards compatibility, a 6-item tuple without _format_ is also accepted and defaults to [`WAVE_FORMAT_PCM`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_PCM "wave.WAVE_FORMAT_PCM")
.

For `format=WAVE_FORMAT_IEEE_FLOAT`, _sampwidth_ must be 4 or 8.

Changed in version 3.15: Added optional item _format_ to the _tuple_.

getparams()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.getparams "Link to this definition")

Return a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
 `(nchannels, sampwidth, framerate, nframes, comptype, compname)` containing the current output parameters.

tell()[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.tell "Link to this definition")

Return current position in the file, with the same disclaimer for the [`Wave_read.tell()`](https://docs.python.org/3/library/wave.html#wave.Wave_read.tell "wave.Wave_read.tell")
 and [`Wave_read.setpos()`](https://docs.python.org/3/library/wave.html#wave.Wave_read.setpos "wave.Wave_read.setpos")
 methods.

writeframesraw(_data_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.writeframesraw "Link to this definition")

Write audio frames, without correcting _nframes_.

Changed in version 3.4: Any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 is now accepted.

writeframes(_data_)[¶](https://docs.python.org/3/library/wave.html#wave.Wave_write.writeframes "Link to this definition")

Write audio frames and make sure _nframes_ is correct. It will raise an error if the output stream is not seekable and the total number of frames that have been written after _data_ has been written does not match the previously set value for _nframes_.

Changed in version 3.4: Any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 is now accepted.

Note that it is invalid to set any parameters after calling `writeframes()` or [`writeframesraw()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.writeframesraw "wave.Wave_write.writeframesraw")
, and any attempt to do so will raise [`wave.Error`](https://docs.python.org/3/library/wave.html#wave.Error "wave.Error")
.

For [`WAVE_FORMAT_IEEE_FLOAT`](https://docs.python.org/3/library/wave.html#wave.WAVE_FORMAT_IEEE_FLOAT "wave.WAVE_FORMAT_IEEE_FLOAT")
 output, a `fact` chunk is written as required by the WAVE specification for non-PCM formats.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html#)
    *   [Wave\_read Objects](https://docs.python.org/3/library/wave.html#wave-read-objects)
        
    *   [Wave\_write Objects](https://docs.python.org/3/library/wave.html#wave-write-objects)
        

#### Previous topic

[Multimedia Services](https://docs.python.org/3/library/mm.html "previous chapter")

#### Next topic

[`colorsys` — Conversions between color systems](https://docs.python.org/3/library/colorsys.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=wave+%E2%80%94+Read+and+write+WAV+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fwave.html&pagesource=library%2Fwave.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/wave.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/colorsys.html "colorsys — Conversions between color systems")
     |
*   [previous](https://docs.python.org/3/library/mm.html "Multimedia Services")
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
*   [Multimedia Services](https://docs.python.org/3/library/mm.html)
     »
*   [`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html)
    
*    
    
    |
*   Theme Auto Light Dark |