[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/barrier#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/barrier)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/barrier?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fdtensor%2Fbarrier&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/barrier#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.barrier Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/barrier#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/mesh_util.py#L243-L310)

Runs a barrier on the mesh.

tf.experimental.dtensor.barrier(
        mesh: tf.experimental.dtensor.Mesh,
        barrier_name: Optional[str] = None,
        timeout_in_ms: Optional[int] = None
    )

Upon returning from the barrier, all operations run before the barrier would have completed across all clients. Currently we allocate a fully sharded tensor with mesh shape and run an all\_reduce on it.

#### Example:

A barrier can be used before application exit to ensure completion of pending ops.

x = [1, 2, 3]
    x = dtensor.relayout(x, dtensor.Layout.batch_sharded(mesh, 'batch', 1))
    dtensor.barrier(mesh)
    
    # At this point all devices on all clients in the mesh have completed
    # operations before the barrier. Therefore it is OK to tear down the clients.
    sys.exit()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mesh` | The mesh to run the barrier on. |
| `barrier_name` | The name of the barrier. Mainly used for logging purpose. |
| `timeout_in_ms` | The timeout of the barrier in ms. If omitted, blocks indefinitely till the barrier is reached from all clients. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.