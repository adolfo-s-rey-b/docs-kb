[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdata%2Fexperimental%2Fsave&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.save Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/io.py#L26-L105)

Saves the content of the given dataset. (deprecated)

tf.data.experimental.save(
        dataset, path, compression=None, shard_func=None, checkpoint_args=None
    )

#### Example usage:

    import tempfile

The saved dataset is saved in multiple file "shards". By default, the dataset output is divided to shards in a round-robin fashion but custom sharding can be specified via the `shard_func` function. For example, you can save the dataset to using a single shard as follows:

dataset = make_dataset()
    def custom_shard_func(element):
      return np.int64(0)
    dataset = tf.data.experimental.save(
        path="/path/to/data", ..., shard_func=custom_shard_func)

To enable checkpointing, pass in `checkpoint_args` to the `save` method as follows:

dataset = tf.data.Dataset.range(100)
    save_dir = "..."
    checkpoint_prefix = "..."
    step_counter = tf.Variable(0, trainable=False)
    checkpoint_args = {
      "checkpoint_interval": 50,
      "step_counter": step_counter,
      "directory": checkpoint_prefix,
      "max_to_keep": 20,
    }
    dataset.save(dataset, save_dir, checkpoint_args=checkpoint_args)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | The dataset to save. |
| `path` | Required. A directory to use for saving the dataset. |
| `compression` | Optional. The algorithm to use to compress data when writing it. Supported options are `GZIP` and `NONE`. Defaults to `NONE`. |
| `shard_func` | Optional. A function to control the mapping of dataset elements to file shards. The function is expected to map elements of the input dataset to int64 shard IDs. If present, the function will be traced and executed as graph computation. |
| `checkpoint_args` | Optional args for checkpointing which will be passed into the [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br>. If `checkpoint_args` are not specified, then checkpointing will not be performed. The `save()` implementation creates a [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> object internally, so users should not set the `checkpoint` argument in `checkpoint_args`. |

|     |
| --- |
| Returns<br>------- |     |
| An operation which when executed performs the save. When writing checkpoints, returns None. The return value is useful in unit tests. |     |

|     |
| --- |
| Raises<br>------ |     |
| ValueError if `checkpoint` is passed into `checkpoint_args`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.