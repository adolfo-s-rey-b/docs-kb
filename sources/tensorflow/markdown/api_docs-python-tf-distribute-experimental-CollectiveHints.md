[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.CollectiveHints Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/collective_util.py#L168-L233)

Hints for collective operations like AllReduce.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.experimental.CollectiveHints`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints)

tf.distribute.experimental.CollectiveHints(
        bytes_per_pack=0, timeout_seconds=None
    )

This can be passed to methods like `tf.distribute.get_replica_context().all_reduce()` to optimize collective operation performance. Note that these are only hints, which may or may not change the actual behavior. Some options only apply to certain strategy and are ignored by others.

One common optimization is to break gradients all-reduce into multiple packs so that weight updates can overlap with gradient all-reduce.

#### Examples:

*   bytes\_per\_pack

hints = tf.distribute.experimental.CollectiveHints(
        bytes_per_pack=50 * 1024 * 1024)
    grads = tf.distribute.get_replica_context().all_reduce(
        'sum', grads, experimental_hints=hints)
    optimizer.apply_gradients(zip(grads, vars),
        experimental_aggregate_gradients=False)

*   timeout\_seconds

strategy = tf.distribute.MirroredStrategy()
    hints = tf.distribute.experimental.CollectiveHints(
        timeout_seconds=120.0)
    try:
      strategy.reduce("sum", v, axis=None, experimental_hints=hints)
    except tf.errors.DeadlineExceededError:
      do_something()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bytes_per_pack` | a non-negative integer. Breaks collective operations into packs of certain size. If it's zero, the value is determined automatically. This only applies to all-reduce with `MultiWorkerMirroredStrategy` currently. |
| `timeout_seconds` | a float or None, timeout in seconds. If not None, the collective raises [`tf.errors.DeadlineExceededError`](https://www.tensorflow.org/api_docs/python/tf/errors/DeadlineExceededError)<br> if it takes longer than this timeout. This can be useful when debugging hanging issues. This should only be used for debugging since it creates a new thread for each collective, i.e. an overhead of `timeout_seconds * num_collectives_per_second` more threads. This only works for [`tf.distribute.experimental.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/MultiWorkerMirroredStrategy)<br>. |

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