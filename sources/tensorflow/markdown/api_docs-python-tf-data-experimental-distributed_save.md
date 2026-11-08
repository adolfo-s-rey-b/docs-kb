[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.distributed\_save Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/distributed_save_op.py#L28-L111)

Initiates the process of saving a dataset to disk using tf.data service.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.distributed_save`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save)

tf.data.experimental.distributed_save(
        dataset: tf.data.Dataset,
        path: str,
        data_service_address: str,
        compression: str = 'AUTO'
    ) -> Optional[ops.OperationType]

The op uses tf.data service ([https://www.tensorflow.org/api\_docs/python/tf/data/experimental/service](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service)
) to write a dataset snapshot. Returns immediately after submitting the request. Does not wait for the snapshot to be finished. Requires that the tf.data service run a fixed number of worker replicas.

To load the snapshot, users may optionally pass `wait=True` to [`tf.data.Dataset.load`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#load)
 so it can read snapshots as they are being written.

#### Example usage:

    import os

    # Runs tf.data service.

    # Writes dataset snapshot.

    # Loads a dataset snapshot.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | The [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> to save. |
| `path` | The directory path to save the dataset. Requires that:<br><br>*   The directory does not exist and will create the directory.<br>*   The file system supports atomic move (rename). |
| `data_service_address` | tf.data service dispatcher address. |
| `compression` | (Optional.) Whether and how to compress the `dataset` snapshot. If `"AUTO"`, the tf.data runtime decides which algorithm to use. If `"GZIP"` or `"SNAPPY"`, that specific algorithm is used. If `None`, the `dataset` snapshot is not compressed. |

|     |
| --- |
| Returns<br>------- |     |
| An operation which when executed performs the distributed save. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `dispatcher_address` is invalid. |
| [`tf.errors.AlreadyExistsError`](https://www.tensorflow.org/api_docs/python/tf/errors/AlreadyExistsError) | If the snapshot has already started or has finished. |
| [`tf.errors.FailedPreconditionError`](https://www.tensorflow.org/api_docs/python/tf/errors/FailedPreconditionError) | If the file system does not support atomic move (rename). |
| [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError) | If tf.data service is not running in the fault tolerant mode. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.