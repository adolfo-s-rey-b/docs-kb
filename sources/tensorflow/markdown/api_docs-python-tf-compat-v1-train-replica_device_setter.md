[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Freplica_device_setter&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.replica\_device\_setter Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/replica_device_setter#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/device_setter.py#L128-L223)

Return a `device function` to use when building a Graph for replicas.

tf.compat.v1.train.replica_device_setter(
        ps_tasks=0,
        ps_device='/job:ps',
        worker_device='/job:worker',
        merge_devices=True,
        cluster=None,
        ps_ops=None,
        ps_strategy=None
    )

Device Functions are used in `with tf.device(device_function):` statement to automatically assign devices to `Operation` objects as they are constructed, Device constraints are added from the inner-most context first, working outwards. The merging behavior adds constraints to fields that are yet unset by a more inner context. Currently the fields are (job, task, cpu/gpu).

If `cluster` is `None`, and `ps_tasks` is 0, the returned function is a no-op. Otherwise, the value of `ps_tasks` is derived from `cluster`.

By default, only Variable ops are placed on ps tasks, and the placement strategy is round-robin over all ps tasks. A custom `ps_strategy` may be used to do more intelligent placement, such as `tf.contrib.training.GreedyLoadBalancingStrategy`.

For example,

# To build a cluster with two ps jobs on hosts ps0 and ps1, and 3 worker
    # jobs on hosts worker0, worker1 and worker2.
    cluster_spec = {
        "ps": ["ps0:2222", "ps1:2222"],
        "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]}
    with
    tf.compat.v1.device(tf.compat.v1.train.replica_device_setter(cluster=cluster_spec)):
      # Build your graph
      v1 = tf.Variable(...)  # assigned to /job:ps/task:0
      v2 = tf.Variable(...)  # assigned to /job:ps/task:1
      v3 = tf.Variable(...)  # assigned to /job:ps/task:0
    # Run compute

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ps_tasks` | Number of tasks in the `ps` job. Ignored if `cluster` is provided. |
| `ps_device` | String. Device of the `ps` job. If empty no `ps` job is used. Defaults to `ps`. |
| `worker_device` | String. Device of the `worker` job. If empty no `worker` job is used. |
| `merge_devices` | `Boolean`. If `True`, merges or only sets a device if the device constraint is completely unset. merges device specification rather than overriding them. |
| `cluster` | `ClusterDef` proto or `ClusterSpec`. |
| `ps_ops` | List of strings representing `Operation` types that need to be placed on `ps` devices. If `None`, defaults to `STANDARD_PS_OPS`. |
| `ps_strategy` | A callable invoked for every ps `Operation` (i.e. matched by `ps_ops`), that takes the `Operation` and returns the ps task index to use. If `None`, defaults to a round-robin strategy across all `ps` devices. |

|     |
| --- |
| Returns<br>------- |     |
| A function to pass to [`tf.device()`](https://www.tensorflow.org/api_docs/python/tf/device)<br>. |     |

|     |
| --- |
| Raises<br>------ |     |
| TypeError if `cluster` is not a dictionary or `ClusterDef` protocol buffer, or if `ps_strategy` is provided but not a callable. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.