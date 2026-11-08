[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#methods)
    *   [num\_records\_produced](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#num_records_produced)
        
    *   [num\_work\_units\_completed](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#num_work_units_completed)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#read)
        
    *   [read\_up\_to](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#read_up_to)
        
    *   [reset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#reset)
        
    *   [restore\_state](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#restore_state)
        
    *   [serialize\_state](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#serialize_state)
        
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.LMDBReader Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#methods)
    *   [num\_records\_produced](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#num_records_produced)
        
    *   [num\_work\_units\_completed](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#num_work_units_completed)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#read)
        
    *   [read\_up\_to](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#read_up_to)
        
    *   [reset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#reset)
        
    *   [restore\_state](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#restore_state)
        
    *   [serialize\_state](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#serialize_state)
        
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/LMDBReader#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L575-L599)

A Reader that outputs the records from a LMDB file.

Inherits From: [`ReaderBase`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ReaderBase)

tf.compat.v1.LMDBReader(
        name=None, options=None
    )

See ReaderBase for supported methods.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | A name for the operation (optional). |
| `options` | A LMDBRecordOptions object (optional). |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `reader_ref` | Op that implements the reader. |
| `supports_serialize` | Whether the Reader implementation can serialize its state. |

Methods
-------

### `num_records_produced`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L329-L347)

num_records_produced(
        name=None
    )

Returns the number of records this reader has produced.

This is the same as the number of Read executions that have succeeded.

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| An int64 Tensor. |     |

### `num_work_units_completed`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L349-L363)

num_work_units_completed(
        name=None
    )

Returns the number of work units this reader has finished processing.

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| An int64 Tensor. |     |

### `read`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L262-L289)

read(
        queue, name=None
    )

Returns the next record (key, value) pair produced by a reader.

Will dequeue a work unit from queue if necessary (e.g. when the Reader needs to start reading from a new file since it has finished with the previous file).

|     |     |
| --- | --- |
| Args |     |
| `queue` | A Queue or a mutable string Tensor representing a handle to a Queue, with string work items. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns |     |
| A tuple of Tensors (key, value). |     |
| `key` | A string scalar Tensor. |
| `value` | A string scalar Tensor. |

### `read_up_to`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L291-L327)

read_up_to(
        queue, num_records, name=None
    )

Returns up to num\_records (key, value) pairs produced by a reader.

Will dequeue a work unit from queue if necessary (e.g., when the Reader needs to start reading from a new file since it has finished with the previous file). It may return less than num\_records even before the last batch.

|     |     |
| --- | --- |
| Args |     |
| `queue` | A Queue or a mutable string Tensor representing a handle to a Queue, with string work items. |
| `num_records` | Number of records to read. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns |     |
| A tuple of Tensors (keys, values). |     |
| `keys` | A 1-D string Tensor. |
| `values` | A 1-D string Tensor. |

### `reset`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L407-L419)

reset(
        name=None
    )

Restore a reader to its initial clean state.

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| The created Operation. |     |

### `restore_state`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L382-L400)

restore_state(
        state, name=None
    )

Restore a reader to a previously saved state.

Not all Readers support being restored, so this can produce an Unimplemented error.

|     |     |
| --- | --- |
| Args |     |
| `state` | A string Tensor. Result of a SerializeState of a Reader with matching type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| The created Operation. |     |

### `serialize_state`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L365-L380)

serialize_state(
        name=None
    )

Produce a string tensor that encodes the state of a reader.

Not all Readers support being serialized, so this can produce an Unimplemented error.

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A string Tensor. |     |

eager compatibility
-------------------

Readers are not compatible with eager execution. Instead, please use [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 to get data into your model.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.