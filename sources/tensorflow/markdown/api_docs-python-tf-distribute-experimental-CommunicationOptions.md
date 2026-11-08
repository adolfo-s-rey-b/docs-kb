[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fexperimental%2FCommunicationOptions&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.CommunicationOptions Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/collective_util.py#L50-L114)

Options for cross device communications like All-reduce.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)

tf.distribute.experimental.CommunicationOptions(
        bytes_per_pack=0,
        timeout_seconds=None,
        implementation=tf.distribute.experimental.CollectiveCommunication.AUTO
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training) |

This can be passed to methods like `tf.distribute.get_replica_context().all_reduce()` to optimize collective operation performance. Note that these are only hints, which may or may not change the actual behavior. Some options only apply to certain strategy and are ignored by others.

One common optimization is to break gradients all-reduce into multiple packs so that weight updates can overlap with gradient all-reduce.

#### Examples:

options = tf.distribute.experimental.CommunicationOptions(
        bytes_per_pack=50 * 1024 * 1024,
        timeout_seconds=120.0,
        implementation=tf.distribute.experimental.CommunicationImplementation.NCCL
    )
    grads = tf.distribute.get_replica_context().all_reduce(
        'sum', grads, options=options)
    optimizer.apply_gradients(zip(grads, vars),
        experimental_aggregate_gradients=False)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bytes_per_pack` | a non-negative integer. Breaks collective operations into packs of certain size. If it's zero, the value is determined automatically. This hint is respected by all multi-replica strategies except `TPUStrategy`. |
| `timeout_seconds` | a float or None, timeout in seconds. If not None, the collective raises [`tf.errors.DeadlineExceededError`](https://www.tensorflow.org/api_docs/python/tf/errors/DeadlineExceededError)<br> if it takes longer than this timeout. Zero disables timeout. This can be useful when debugging hanging issues. This should only be used for debugging since it creates a new thread for each collective, i.e. an overhead of `timeout_seconds * num_collectives_per_second` more threads. This only works for [`tf.distribute.experimental.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/MultiWorkerMirroredStrategy)<br>. |
| `implementation` | a [`tf.distribute.experimental.CommunicationImplementation`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation)<br>. This is a hint on the preferred communication implementation. Possible values include `AUTO`, `RING`, and `NCCL`. NCCL is generally more performant for GPU, but doesn't work for CPU. This only works for [`tf.distribute.experimental.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/MultiWorkerMirroredStrategy)<br>. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | When arguments have invalid value. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.