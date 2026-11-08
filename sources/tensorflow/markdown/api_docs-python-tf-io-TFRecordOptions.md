[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#methods)
    *   [get\_compression\_type\_string](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#get_compression_type_string)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.TFRecordOptions Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#methods)
    *   [get\_compression\_type\_string](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#get_compression_type_string)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/tf_record.py#L35-L145)

Options used for manipulating TFRecord files.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.TFRecordOptions`](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions)
, [`tf.compat.v1.python_io.TFRecordOptions`](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions)

tf.io.TFRecordOptions(
        compression_type=None,
        flush_mode=None,
        input_buffer_size=None,
        output_buffer_size=None,
        window_bits=None,
        compression_level=None,
        compression_method=None,
        mem_level=None,
        compression_strategy=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `compression_type` | `"GZIP"`, `"ZLIB"`, or `""` (no compression). |
| `flush_mode` | flush mode or `None`, Default: Z\_NO\_FLUSH. |
| `input_buffer_size` | int or `None`. |
| `output_buffer_size` | int or `None`. |
| `window_bits` | int or `None`. |
| `compression_level` | 0 to 9, or `None`. |
| `compression_method` | compression method or `None`. |
| `mem_level` | 1 to 9, or `None`. |
| `compression_strategy` | strategy or `None`. Default: Z\_DEFAULT\_STRATEGY. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If compression\_type is invalid. |

Methods
-------

### `get_compression_type_string`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/tf_record.py#L97-L121)

@classmethod

Convert various option types to a unified string.

|     |     |
| --- | --- |
| Args |     |
| `options` | `TFRecordOption`, `TFRecordCompressionType`, or string. |

|     |
| --- |
| Returns |     |
| Compression type as string (e.g. `'ZLIB'`, `'GZIP'`, or `''`). |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If compression\_type is invalid. |

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| compression\_type\_map | {<br>     0: '',<br>     1: 'ZLIB',<br>     2: 'GZIP'<br>    } |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.