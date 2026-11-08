[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdata%2Fexperimental%2FTFRecordWriter&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter#methods)
    *   [write](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter#write)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.data.experimental.TFRecordWriter Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter#methods)
    *   [write](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter#write)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/writers.py#L27-L126)

Writes a dataset to a TFRecord file. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.TFRecordWriter`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter)

tf.data.experimental.TFRecordWriter(
        filename, compression_type=None
    )

The elements of the dataset must be scalar strings. To serialize dataset elements as strings, you can use the [`tf.io.serialize_tensor`](https://www.tensorflow.org/api_docs/python/tf/io/serialize_tensor)
 function.

dataset = tf.data.Dataset.range(3)
    dataset = dataset.map(tf.io.serialize_tensor)
    writer = tf.data.experimental.TFRecordWriter("/path/to/file.tfrecord")
    writer.write(dataset)

To read back the elements, use `TFRecordDataset`.

dataset = tf.data.TFRecordDataset("/path/to/file.tfrecord")
    dataset = dataset.map(lambda x: tf.io.parse_tensor(x, tf.int64))

To shard a `dataset` across multiple TFRecord files:

dataset = ... # dataset to be written
    
    def reduce_func(key, dataset):
      filename = tf.strings.join([PATH_PREFIX, tf.strings.as_string(key)])
      writer = tf.data.experimental.TFRecordWriter(filename)
      writer.write(dataset.map(lambda _, x: x))
      return tf.data.Dataset.from_tensors(filename)
    
    dataset = dataset.enumerate()
    dataset = dataset.apply(tf.data.experimental.group_by_window(
      lambda i, _: i % NUM_SHARDS, reduce_func, tf.int64.max
    ))
    
    # Iterate through the dataset to trigger data writing.
    for _ in dataset:
      pass

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filename` | a string path indicating where to write the TFRecord data. |
| `compression_type` | (Optional.) a string indicating what type of compression to use when writing the file. See `tf.io.TFRecordCompressionType` for what types of compression are available. Defaults to `None`. |

Methods
-------

### `write`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/writers.py#L91-L126)

write(
        dataset
    )

Writes a dataset to a TFRecord file.

An operation that writes the content of the specified dataset to the file specified in the constructor.

If the file exists, it will be overwritten.

|     |     |
| --- | --- |
| Args |     |
| `dataset` | a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> whose elements are to be written to a file |

|     |
| --- |
| Returns |     |
| In graph mode, this returns an operation which when executed performs the write. In eager mode, the write is performed by the method itself and there is no return value. |     |

Raises TypeError: if `dataset` is not a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
. TypeError: if the elements produced by the dataset are not scalar strings.

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.