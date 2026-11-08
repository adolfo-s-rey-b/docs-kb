[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#num_accelerators)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.cluster\_resolver.SimpleClusterResolver Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver#num_accelerators)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L288-L415)

Simple implementation of ClusterResolver that accepts all attributes.

Inherits From: [`ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.cluster_resolver.SimpleClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver)

tf.distribute.cluster_resolver.SimpleClusterResolver(
        cluster_spec,
        master='',
        task_type=None,
        task_id=None,
        environment='',
        num_accelerators=None,
        rpc_layer=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) |

Please see the base class for documentation of arguments of its constructor.

It is useful if you want to specify some or all attributes.

Usage example with [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
:

  cluster = tf.train.ClusterSpec({"worker": ["worker0.example.com:2222",\
                                                 "worker1.example.com:2222"]})
    
      # On worker 0
      cluster_resolver = SimpleClusterResolver(cluster, task_type="worker",
                                               task_id=0,
                                               num_accelerators={"GPU": 8},
                                               rpc_layer="grpc")
      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
          cluster_resolver=cluster_resolver)
    
      # On worker 1
      cluster_resolver = SimpleClusterResolver(cluster, task_type="worker",
                                               task_id=1,
                                               num_accelerators={"GPU": 8},
                                               rpc_layer="grpc")
      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
          cluster_resolver=cluster_resolver)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `environment` | Returns the current environment which TensorFlow is running in.<br><br>There are two possible return values, "google" (when TensorFlow is running in a Google-internal environment) or an empty string (when TensorFlow is running elsewhere).<br><br>If you are implementing a ClusterResolver that works in both the Google environment and the open-source world (for instance, a TPU ClusterResolver or similar), you will have to return the appropriate string depending on the environment, which you will have to detect.<br><br>Otherwise, if you are implementing a ClusterResolver that will only work in open-source TensorFlow, you do not need to implement this property. |
| `rpc_layer` |     |
| `task_id` | Returns the task id this `ClusterResolver` indicates.<br><br>In TensorFlow distributed environment, each job may have an applicable task id, which is the index of the instance within its task type. This is useful when user needs to run specific code according to task index. For example,<br><br>cluster_spec = tf.train.ClusterSpec({<br>        "ps": ["localhost:2222", "localhost:2223"],<br>        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]<br>    })<br>    <br>    # SimpleClusterResolver is used here for illustration; other cluster<br>    # resolvers may be used for other source of task type/id.<br>    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",<br>                                            task_id=0)<br>    <br>    ...<br>    <br>    if cluster_resolver.task_type == 'worker' and cluster_resolver.task_id == 0:<br>      # Perform something that's only applicable on 'worker' type, id 0. This<br>      # block will run on this particular instance since we've specified this<br>      # task to be a 'worker', id 0 in above cluster resolver.<br>    else:<br>      # Perform something that's only applicable on other ids. This block will<br>      # not run on this particular instance.<br><br>Returns `None` if such information is not available or is not applicable in the current distributed environment, such as training with [`tf.distribute.cluster_resolver.TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)<br>.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s class docstring. |
| `task_type` | Returns the task type this `ClusterResolver` indicates.<br><br>In TensorFlow distributed environment, each job may have an applicable task type. Valid task types in TensorFlow include 'chief': a worker that is designated with more responsibility, 'worker': a regular worker for training/evaluation, 'ps': a parameter server, or 'evaluator': an evaluator that evaluates the checkpoints for metrics.<br><br>See [Multi-worker configuration](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration)<br> for more information about 'chief' and 'worker' task type, which are most commonly used.<br><br>Having access to such information is useful when user needs to run specific code according to task types. For example,<br><br>cluster_spec = tf.train.ClusterSpec({<br>        "ps": ["localhost:2222", "localhost:2223"],<br>        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]<br>    })<br>    <br>    # SimpleClusterResolver is used here for illustration; other cluster<br>    # resolvers may be used for other source of task type/id.<br>    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",<br>                                            task_id=1)<br>    <br>    ...<br>    <br>    if cluster_resolver.task_type == 'worker':<br>      # Perform something that's only applicable on workers. This block<br>      # will run on this particular instance since we've specified this task to<br>      # be a worker in above cluster resolver.<br>    elif cluster_resolver.task_type == 'ps':<br>      # Perform something that's only applicable on parameter servers. This<br>      # block will not run on this particular instance.<br><br>Returns `None` if such information is not available or is not applicable in the current distributed environment, such as training with [`tf.distribute.experimental.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TPUStrategy)<br>.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s class doc. |

Methods
-------

### `cluster_spec`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L341-L343)

cluster_spec()

Returns the ClusterSpec passed into the constructor.

### `master`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L345-L366)

master(
        task_type=None, task_id=None, rpc_layer=None
    )

Returns the master address to use when creating a session.

|     |     |
| --- | --- |
| Args |     |
| `task_type` | (Optional) The type of the TensorFlow task of the master. |
| `task_id` | (Optional) The index of the TensorFlow task of the master. |
| `rpc_layer` | (Optional) The RPC used by distributed TensorFlow. |

|     |
| --- |
| Returns |     |
| The name or URL of the session master. |     |

If a task\_type and task\_id is given, this will override the `master` string passed into the initialization function.

### `num_accelerators`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L388-L407)

num_accelerators(
        task_type=None, task_id=None, config_proto=None
    )

Returns the number of accelerator cores per worker.

The SimpleClusterResolver does not do automatic detection of accelerators, and thus all arguments are unused and we simply return the value provided in the constructor.

|     |     |
| --- | --- |
| Args |     |
| `task_type` | Unused. |
| `task_id` | Unused. |
| `config_proto` | Unused. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.