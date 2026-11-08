[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.snapshot Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/snapshot.py#L189-L276)

API to persist the output of the input dataset. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.snapshot`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot)

tf.data.experimental.snapshot(
        path, compression='AUTO', reader_func=None, shard_func=None
    )

The snapshot API allows users to transparently persist the output of their preprocessing pipeline to disk, and materialize the pre-processed data on a different training run.

This API enables repeated preprocessing steps to be consolidated, and allows re-use of already processed data, trading off disk storage and network bandwidth for freeing up more valuable CPU resources and accelerator compute time.

[https://github.com/tensorflow/community/blob/master/rfcs/20200107-tf-data-snapshot.md](https://github.com/tensorflow/community/blob/master/rfcs/20200107-tf-data-snapshot.md)
 has detailed design documentation of this feature.

Users can specify various options to control the behavior of snapshot, including how snapshots are read from and written to by passing in user-defined functions to the `reader_func` and `shard_func` parameters.

`shard_func` is a user specified function that maps input elements to snapshot shards.

Users may want to specify this function to control how snapshot files should be written to disk. Below is an example of how a potential shard\_func could be written.

dataset = ...
    dataset = dataset.enumerate()
    dataset = dataset.apply(tf.data.Dataset.snapshot("/path/to/snapshot/dir",
        shard_func=lambda x, y: x % NUM_SHARDS, ...))
    dataset = dataset.map(lambda x, y: y)

`reader_func` is a user specified function that accepts a single argument: (1) a Dataset of Datasets, each representing a "split" of elements of the original dataset. The cardinality of the input dataset matches the number of the shards specified in the `shard_func` (see above). The function should return a Dataset of elements of the original dataset.

Users may want specify this function to control how snapshot files should be read from disk, including the amount of shuffling and parallelism.

Here is an example of a standard reader function a user can define. This function enables both dataset shuffling and parallel reading of datasets:

def user_reader_func(datasets):
      # shuffle the datasets splits
      datasets = datasets.shuffle(NUM_CORES)
      # read datasets in parallel and interleave their elements
      return datasets.interleave(lambda x: x, num_parallel_calls=AUTOTUNE)
    
    dataset = dataset.apply(tf.data.Dataset.snapshot("/path/to/snapshot/dir",
        reader_func=user_reader_func))

By default, snapshot parallelizes reads by the number of cores available on the system, but will not attempt to shuffle the data.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | Required. A directory to use for storing / loading the snapshot to / from. |
| `compression` | Optional. The type of compression to apply to the snapshot written to disk. Supported options are `GZIP`, `SNAPPY`, `AUTO` or None. Defaults to AUTO, which attempts to pick an appropriate compression algorithm for the dataset. |
| `reader_func` | Optional. A function to control how to read data from snapshot shards. |
| `shard_func` | Optional. A function to control how to shard data when writing a snapshot. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.