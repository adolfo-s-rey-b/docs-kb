[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fio%2FTFRecordWriter&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#methods)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#close)
        
    *   [flush](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#flush)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#write)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.TFRecordWriter Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#methods)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#close)
        
    *   [flush](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#flush)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#write)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/tf_record.py#L211-L318)

A class to write records to a TFRecords file.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.TFRecordWriter`](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter)
, [`tf.compat.v1.python_io.TFRecordWriter`](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter)

tf.io.TFRecordWriter(
        path, options=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFRecord and tf.train.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb)<br>    <br>*   [Instance Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)<br>    <br>*   [Semantic Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation) |

[TFRecords tutorial](https://www.tensorflow.org/tutorials/load_data/tfrecord)

TFRecords is a binary format which is optimized for high throughput data retrieval, generally in conjunction with [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
. `TFRecordWriter` is used to write serialized examples to a file for later consumption. The key steps are:

Ahead of time:

*   [Convert data into a serialized format](https://www.tensorflow.org/tutorials/load_data/tfrecord#tfexample)
    
*   [Write the serialized data to one or more files](https://www.tensorflow.org/tutorials/load_data/tfrecord#tfrecord_files_in_python)
    
    During training or evaluation:
    
*   [Read serialized examples into memory](https://www.tensorflow.org/tutorials/load_data/tfrecord#reading_a_tfrecord_file)
    
*   [Parse (deserialize) examples](https://www.tensorflow.org/tutorials/load_data/tfrecord#reading_a_tfrecord_file)
    

A minimal example is given below:

    import tempfile

    # Write the records to a file.

    # Read the data back out.

    for batch in tf.data.TFRecordDataset([example_path]).map(decode_fn):

This class implements `__enter__` and `__exit__`, and can be used in `with` blocks like a normal file. (See the usage example above.)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | The path to the TFRecords file. |
| `options` | (optional) String specifying compression type, `TFRecordCompressionType`, or `TFRecordOptions` object. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `IOError` | If `path` cannot be opened for writing. |
| `ValueError` | If valid compression\_type can't be determined from `options`. |

Methods
-------

### `close`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/tf_record.py#L315-L317)

close()

Close the file.

### `flush`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/tf_record.py#L311-L313)

flush()

Flush the file.

### `write`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/tf_record.py#L303-L309)

write(
        record
    )

Write a string record to the file.

|     |     |
| --- | --- |
| Args |     |
| `record` | str |

### `__enter__`

__enter__()

**enter**(self: object) -> object

### `__exit__`

__exit__()

**exit**(self: tensorflow.python.lib.io.\_pywrap\_record\_io.RecordWriter, \*args) -> None

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.