[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#used-in-the-notebooks_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#methods_2)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#close)
        
    *   [flush](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#flush)
        
    *   [next](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#next)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#read)
        
    *   [readline](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#readline)
        
    *   [readlines](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#readlines)
        
    *   [seek](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#seek)
        
    *   [seekable](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#seekable)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#size)
        
    *   [tell](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#tell)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#write)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#__exit__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#__iter__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.gfile.GFile Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#used-in-the-notebooks_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#methods_2)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#close)
        
    *   [flush](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#flush)
        
    *   [next](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#next)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#read)
        
    *   [readline](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#readline)
        
    *   [readlines](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#readlines)
        
    *   [seek](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#seek)
        
    *   [seekable](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#seekable)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#size)
        
    *   [tell](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#tell)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#write)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#__exit__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile?version=stable#__iter__)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/gfile.py#L36-L114)

File I/O wrappers without thread locking.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.gfile.GFile`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile)
, [`tf.compat.v1.gfile.Open`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile)
, [`tf.compat.v1.io.gfile.GFile`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile)

tf.io.gfile.GFile(
        name, mode='r'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Generalized Linear Models](https://www.tensorflow.org/probability/examples/Generalized_Linear_Models)<br>    <br>*   [Load LM Checkpoints using Model Garden](https://www.tensorflow.org/tfmodels/nlp/load_lm_ckpts)<br>    <br>*   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan)<br>    <br>*   [Universal Sentence Encoder-Lite demo](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite)<br>    <br>*   [Avro Dataset API](https://www.tensorflow.org/io/tutorials/avro) |

The main roles of the [`tf.io.gfile`](https://www.tensorflow.org/api_docs/python/tf/io/gfile)
 module are:

1.  To provide an API that is close to Python's file I/O objects, and
2.  To provide an implementation based on TensorFlow's C++ FileSystem API.

The C++ FileSystem API supports multiple file system implementations, including local files, Google Cloud Storage (using a `gs://` prefix, and HDFS (using an `hdfs://` prefix). TensorFlow exports these as `tf.io.gfile`, so that you can use these implementations for saving and loading checkpoints, writing to TensorBoard logs, and accessing training data (among other uses). However, if all your files are local, you can use the regular Python file API without any problem.

Once you obtain a `GFile` object, you can use it in most ways as you would any Python's file object:

    with open("/tmp/x", "w") as f:

The difference is that you can specify URI schemes to use other filesystems (e.g., `gs://` for GCS, `s3://` for S3, etc.), if they are supported. Using `file://` as an example, we have:

    with tf.io.gfile.GFile("file:///tmp/x", "w") as f:

You can also read all lines of a file directly:

    with tf.io.gfile.GFile("file:///tmp/x", "w") as f:

You can iterate over the lines:

    with tf.io.gfile.GFile("file:///tmp/x", "w") as f:

Random access read is possible if the underlying filesystem supports it:

    with open("/tmp/x", "w") as f:

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