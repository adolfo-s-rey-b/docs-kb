[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.create\_local\_cluster Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L4028-L4115)

Create and start local servers and return the associated `Server` objects.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.create_local_cluster`](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster)

tf.test.create_local_cluster(
        num_workers: int,
        num_ps: int,
        protocol: str = 'grpc',
        worker_config: Optional[tf.compat.v1.ConfigProto] = None,
        ps_config: Optional[tf.compat.v1.ConfigProto] = None
    ) -> tuple[list[server_lib.Server], list[server_lib.Server]]

"PS" stands for "parameter server": a task responsible for storing and updating the model's parameters. Other tasks send updates to these parameters as they work on optimizing the parameters. This particular division of labor between tasks is not required, but is common for distributed training.

Read more at [https://www.tensorflow.org/guide/extend/architecture](https://www.tensorflow.org/guide/extend/architecture)

![components](https://www.tensorflow.org/images/diag1.svg "components")

Figure illustrates the interaction of these components. "/job:worker/task:0" and "/job:ps/task:0" are both tasks with worker services.

#### Example:

workers, _ = tf.test.create_local_cluster(num_workers=2, num_ps=2)
    
    worker_sessions = [tf.compat.v1.Session(w.target) for w in workers]
    
    with tf.device("/job:ps/task:0"):
      ...
    with tf.device("/job:ps/task:1"):
      ...
    with tf.device("/job:worker/task:0"):
      ...
    with tf.device("/job:worker/task:1"):
      ...
    
    worker_sessions[0].run(...)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_workers` | Number of worker servers to start. |
| `num_ps` | Number of PS servers to start. |
| `protocol` | Communication protocol. Allowed values are documented in the documentation of [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)<br>. |
| `worker_config` | (optional) `tf.ConfigProto` to initialize workers. Can be used to instantiate multiple devices etc. |
| `ps_config` | (optional) `tf.ConfigProto` to initialize PS servers. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple `(worker_servers, ps_servers)`. `worker_servers` is a list of `num_workers` objects of type [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)<br> (all running locally); and `ps_servers` is a list of `num_ps` objects of similar type. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ImportError` | if portpicker module was not found at load time |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.