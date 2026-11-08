[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/Server?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2FServer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#methods)
    *   [create\_local\_server](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#create_local_server)
        
    *   [join](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#join)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#start)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.Server Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#methods)
    *   [create\_local\_server](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#create_local_server)
        
    *   [join](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#join)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/distribute/Server#start)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L94-L239)

An in-process TensorFlow server, for use in distributed training.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
, [`tf.compat.v1.train.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)

tf.distribute.Server(
        server_or_cluster_def,
        job_name=None,
        task_index=None,
        protocol=None,
        config=None,
        start=True
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate multi-worker CPU/GPU training](https://www.tensorflow.org/guide/migrate/multi_worker_cpu_gpu_training) | *   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) |

A [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
 instance encapsulates a set of devices and a [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
 target that can participate in distributed training. A server belongs to a cluster (specified by a [`tf.train.ClusterSpec`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec)
), and corresponds to a particular task in a named job. The server can communicate with any other server in the same cluster.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `server_or_cluster_def` | A [`tf.train.ServerDef`](https://www.tensorflow.org/api_docs/python/tf/train/ServerDef)<br> or [`tf.train.ClusterDef`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterDef)<br> protocol buffer, or a [`tf.train.ClusterSpec`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec)<br> object, describing the server to be created and/or the cluster of which it is a member. |
| `job_name` | (Optional.) Specifies the name of the job of which the server is a member. Defaults to the value in `server_or_cluster_def`, if specified. |
| `task_index` | (Optional.) Specifies the task index of the server in its job. Defaults to the value in `server_or_cluster_def`, if specified. Otherwise defaults to 0 if the server's job has only one task. |
| `protocol` | (Optional.) Specifies the protocol to be used by the server. Acceptable values include `"grpc", "grpc+verbs"`. Defaults to the value in `server_or_cluster_def`, if specified. Otherwise defaults to `"grpc"`. |
| `config` | (Options.) A [`tf.compat.v1.ConfigProto`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto)<br> that specifies default configuration options for all sessions that run on this server. |
| `start` | (Optional.) Boolean, indicating whether to start the server after creating it. Defaults to `True`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| [`tf.errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while creating the TensorFlow server. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `server_def` | Returns the [`tf.train.ServerDef`](https://www.tensorflow.org/api_docs/python/tf/train/ServerDef)<br> for this server. |
| `target` | Returns the target for a [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)<br> to connect to this server.<br><br>To create a [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)<br> that connects to this server, use the following snippet:<br><br>server = tf.distribute.Server(...)<br>    with tf.compat.v1.Session(server.target):<br>      # ... |

Methods
-------

### `create_local_server`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L216-L239)

@staticmethod

Creates a new single-process cluster running on the local host.

This method is a convenience wrapper for creating a [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
 with a [`tf.train.ServerDef`](https://www.tensorflow.org/api_docs/python/tf/train/ServerDef)
 that specifies a single-process cluster containing a single task in a job called `"local"`.

|     |     |
| --- | --- |
| Args |     |
| `config` | (Options.) A [`tf.compat.v1.ConfigProto`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto)<br> that specifies default configuration options for all sessions that run on this server. |
| `start` | (Optional.) Boolean, indicating whether to start the server after creating it. Defaults to `True`. |

|     |
| --- |
| Returns |     |
| A local [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)<br>. |     |

### `join`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L176-L185)

join()

Blocks until the server has shut down.

This method currently blocks forever.

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while joining the TensorFlow server. |

### `start`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L167-L174)

start()

Starts this server.

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while starting the TensorFlow server. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.