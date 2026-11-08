[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fget_replica_context&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.get\_replica\_context Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L453-L498)

Returns the current [`tf.distribute.ReplicaContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext)
 or `None`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.get_replica_context`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context)

tf.distribute.get_replica_context()

Returns `None` if in a cross-replica context.

#### Note that execution:

1.  starts in the default (single-replica) replica context (this function will return the default `ReplicaContext` object);
2.  switches to cross-replica context (in which case this will return `None`) when entering a `with tf.distribute.Strategy.scope():` block;
3.  switches to a (non-default) replica context inside `strategy.run(fn, ...)`;
4.  if `fn` calls `get_replica_context().merge_call(merge_fn, ...)`, then inside `merge_fn` you are back in the cross-replica context (and again this function will return `None`).

Most [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
 methods may only be executed in a cross-replica context, in a replica context you should use the API of the [`tf.distribute.ReplicaContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext)
 object returned by this method instead.

assert tf.distribute.get_replica_context() is not None  # default
    with strategy.scope():
      assert tf.distribute.get_replica_context() is None
    
      def f():
        replica_context = tf.distribute.get_replica_context()  # for strategy
        assert replica_context is not None
        tf.print("Replica id: ", replica_context.replica_id_in_sync_group,
                 " of ", replica_context.num_replicas_in_sync)
    
      strategy.run(f)

|     |
| --- |
| Returns<br>------- |     |
| The current [`tf.distribute.ReplicaContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext)<br> object when in a replica context scope, else `None`.<br><br>Within a particular block, exactly one of these two things will be true:<br><br>*   `get_replica_context()` returns non-`None`, or<br>*   `tf.distribute.is_cross_replica_context()` returns True. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.