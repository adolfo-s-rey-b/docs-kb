[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#methods_2)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#close)
        
    *   [flush](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#flush)
        
    *   [next](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#next)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#read)
        
    *   [readline](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#readline)
        
    *   [readlines](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#readlines)
        
    *   [seek](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#seek)
        
    *   [seekable](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#seekable)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#size)
        
    *   [tell](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#tell)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#write)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#__exit__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#__iter__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.gfile.FastGFile Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#methods_2)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#close)
        
    *   [flush](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#flush)
        
    *   [next](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#next)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#read)
        
    *   [readline](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#readline)
        
    *   [readlines](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#readlines)
        
    *   [seek](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#seek)
        
    *   [seekable](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#seekable)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#size)
        
    *   [tell](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#tell)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#write)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#__exit__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile?version=stable#__iter__)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/gfile.py#L117-L130)

File I/O wrappers without thread locking.

tf.compat.v1.gfile.FastGFile(
        name, mode='r'
    )

Note, that this is somewhat like builtin Python file I/O, but there are semantic differences to make it more efficient for some backing filesystems. For example, a write mode file will not be opened until the first write call (to minimize RPC invocations in network filesystems).

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `mode` | Returns the mode in which the file was opened. |
| `name` | Returns the file name. |

Methods
-------

### `close`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L223-L242)

close()

Closes the file.

Should be called for the WritableFile to be flushed.

In general, if you use the context manager pattern, you don't need to call this directly.

    with tf.io.gfile.GFile("/tmp/x", "w") as f:

For cloud filesystems, forgetting to call `close()` might result in data loss as last write might not have been replicated.

### `flush`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L213-L221)

flush()

Flushes the Writable file.

This only ensures that the data has made its way out of the process without any guarantees on whether it's written to disk. This means that the data would survive an application crash but not necessarily an OS crash.

### `next`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L210-L211)

next()

### `read`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L104-L121)

read(
        n=-1
    )

Returns the contents of a file as a string.

Starts reading from current position in file.

|     |     |
| --- | --- |
| Args |     |
| `n` | Read `n` bytes if `n != -1`. If `n = -1`, reads to end of file. |

|     |
| --- |
| Returns |     |
| `n` bytes of the file (or whole file) in bytes mode or `n` bytes of the string if in string (regular) mode. |     |

### `readline`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L167-L170)

readline()

Reads the next line, keeping \\n. At EOF, returns ''.

### `readlines`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L172-L181)

readlines()

Returns all lines from the file in a list.

### `seek`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L123-L165)

seek(
        offset=None, whence=0, position=None
    )

Seeks to the offset in the file. (deprecated arguments)

|     |     |
| --- | --- |
| Args |     |
| `offset` | The byte count relative to the whence argument. |
| `whence` | Valid values for whence are: 0: start of the file (default) 1: relative to the current position of the file 2: relative to the end of file. `offset` is usually negative. |

### `seekable`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L244-L246)

seekable()

Returns True as FileIO supports random access ops of seek()/tell()

### `size`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L94-L96)

size()

Returns the size of the file.

### `tell`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L183-L191)

tell()

Returns the current position in the file.

### `write`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L98-L102)

write(
        file_content
    )

Writes file\_content to the file. Appends to the end of the file.

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L193-L195)

__enter__()

Make usable with "with" statement.

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L197-L199)

__exit__(
        unused_type, unused_value, unused_traceback
    )

Make usable with "with" statement.

### `__iter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L201-L202)

__iter__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-04 UTC.