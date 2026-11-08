[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/load#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.load Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/io.py#L108-L166)

Loads a previously saved dataset. (deprecated)

tf.data.experimental.load(
        path, element_spec=None, compression=None, reader_func=None
    )

#### Example usage:

    import tempfile

If the default option of sharding the saved dataset was used, the element order of the saved dataset will be preserved when loading it.

The `reader_func` argument can be used to specify a custom order in which elements should be loaded from the individual shards. The `reader_func` is expected to take a single argument -- a dataset of datasets, each containing elements of one of the shards -- and return a dataset of elements. For example, the order of shards can be shuffled when loading them as follows:

def custom_reader_func(datasets):
      datasets = datasets.shuffle(NUM_SHARDS)
      return datasets.interleave(lambda x: x, num_parallel_calls=AUTOTUNE)
    
    dataset = tf.data.experimental.load(
        path="/path/to/data", ..., reader_func=custom_reader_func)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | Required. A path pointing to a previously saved dataset. |
| `element_spec` | Optional. A nested structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> objects matching the structure of an element of the saved dataset and specifying the type of individual element components. If not provided, the nested structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> saved with the saved dataset is used. Note that this argument is required in graph mode. |
| `compression` | Optional. The algorithm to use to decompress the data when reading it. Supported options are `GZIP` and `NONE`. Defaults to `NONE`. |
| `reader_func` | Optional. A function to control how to read data from shards. If present, the function will be traced and executed as graph computation. |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> instance. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `FileNotFoundError` | If `element_spec` is not specified and the saved nested structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> can not be located with the saved dataset. |
| `ValueError` | If `element_spec` is not specified and the method is executed in graph mode. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.