[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.data.experimental.make\_batched\_features\_dataset Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/make_batched_features_dataset#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/readers.py#L1100-L1120)

Returns a `Dataset` of feature dictionaries from `Example` protos.

tf.compat.v1.data.experimental.make_batched_features_dataset(
        file_pattern,
        batch_size,
        features,
        reader=None,
        label_key=None,
        reader_args=None,
        num_epochs=None,
        shuffle=True,
        shuffle_buffer_size=10000,
        shuffle_seed=None,
        prefetch_buffer_size=None,
        reader_num_threads=None,
        parser_num_threads=None,
        sloppy_ordering=False,
        drop_final_batch=False
    )

If label\_key argument is provided, returns a `Dataset` of tuple comprising of feature dictionaries and label.

#### Example:

serialized_examples = [\
      features {\
        feature { key: "age" value { int64_list { value: [ 0 ] } } }\
        feature { key: "gender" value { bytes_list { value: [ "f" ] } } }\
        feature { key: "kws" value { bytes_list { value: [ "code", "art" ] } } }\
      },\
      features {\
        feature { key: "age" value { int64_list { value: [] } } }\
        feature { key: "gender" value { bytes_list { value: [ "f" ] } } }\
        feature { key: "kws" value { bytes_list { value: [ "sports" ] } } }\
      }\
    ]

#### We can use arguments:

features: {
      "age": FixedLenFeature([], dtype=tf.int64, default_value=-1),
      "gender": FixedLenFeature([], dtype=tf.string),
      "kws": VarLenFeature(dtype=tf.string),
    }

And the expected output is:

{
      "age": [[0], [-1]],
      "gender": [["f"], ["f"]],
      "kws": SparseTensor(
        indices=[[0, 0], [0, 1], [1, 0]],
        values=["code", "art", "sports"]
        dense_shape=[2, 2]),
    }

|     |     |
| --- | --- |
| Args<br>---- |     |
| `file_pattern` | List of files or patterns of file paths containing `Example` records. See [`tf.io.gfile.glob`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob)<br> for pattern rules. |
| `batch_size` | An int representing the number of records to combine in a single batch. |
| `features` | A `dict` mapping feature keys to `FixedLenFeature` or `VarLenFeature` values. See [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)<br>. |
| `reader` | A function or class that can be called with a `filenames` tensor and (optional) `reader_args` and returns a `Dataset` of `Example` tensors. Defaults to [`tf.data.TFRecordDataset`](https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset)<br>. |
| `label_key` | (Optional) A string corresponding to the key labels are stored in `tf.Examples`. If provided, it must be one of the `features` key, otherwise results in `ValueError`. |
| `reader_args` | Additional arguments to pass to the reader class. |
| `num_epochs` | Integer specifying the number of times to read through the dataset. If None, cycles through the dataset forever. Defaults to `None`. |
| `shuffle` | A boolean, indicates whether the input should be shuffled. Defaults to `True`. |
| `shuffle_buffer_size` | Buffer size of the ShuffleDataset. A large capacity ensures better shuffling but would increase memory usage and startup time. |
| `shuffle_seed` | Randomization seed to use for shuffling. |
| `prefetch_buffer_size` | Number of feature batches to prefetch in order to improve performance. Recommended value is the number of batches consumed per training step. Defaults to auto-tune. |
| `reader_num_threads` | Number of threads used to read `Example` records. If >1, the results will be interleaved. Defaults to `1`. |
| `parser_num_threads` | Number of threads to use for parsing `Example` tensors into a dictionary of `Feature` tensors. Defaults to `2`. |
| `sloppy_ordering` | If `True`, reading performance will be improved at the cost of non-deterministic ordering. If `False`, the order of elements produced is deterministic prior to shuffling (elements are still randomized if `shuffle=True`. Note that if the seed is set, then order of elements after shuffling is deterministic). Defaults to `False`. |
| `drop_final_batch` | If `True`, and the batch size does not evenly divide the input dataset size, the final smaller batch will be dropped. Defaults to `False`. |

|     |
| --- |
| Returns<br>------- |     |
| A dataset of `dict` elements, (or a tuple of `dict` elements and label). Each `dict` maps feature keys to `Tensor` or `SparseTensor` objects. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `reader` is of the wrong type. |
| `ValueError` | If `label_key` is not one of the `features` keys. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.