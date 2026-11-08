[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#num_accelerators)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.cluster\_resolver.TFConfigClusterResolver Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver#num_accelerators)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L47-L200)

Implementation of a ClusterResolver which reads the TF\_CONFIG EnvVar.

Inherits From: [`ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.cluster_resolver.TFConfigClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver)

tf.distribute.cluster_resolver.TFConfigClusterResolver(
        task_type=None, task_id=None, rpc_layer=None, environment=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate multi-worker CPU/GPU training](https://www.tensorflow.org/guide/migrate/multi_worker_cpu_gpu_training) |

This is an implementation of cluster resolvers when using TF\_CONFIG to set information about the cluster. The cluster spec returned will be initialized from the TF\_CONFIG environment variable.

An example to set TF\_CONFIG is:

  os.environ['TF_CONFIG'] = json.dumps({
        'cluster': {
            'worker': ["localhost:12345", "localhost:23456"]
        },
        'task': {'type': 'worker', 'index': 0}
      })

However, sometimes the container orchestration framework will set TF\_CONFIG for you. In this case, you can just create an instance without passing in any arguments. You can find an example here to let Kuburnetes set TF\_CONFIG for you: https://github.com/tensorflow/ecosystem/tree/master/kubernetes. Then you can use it with [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
 as:

  # `TFConfigClusterResolver` is already the default one in the following
      # strategy.
      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
          cluster_resolver=TFConfigClusterResolver())

|     |     |
| --- | --- |
| Args<br>---- |     |
| `task_type` | (String, optional) Overrides the task type specified in the TF\_CONFIG environment variable. |
| `task_id` | (Integer, optional) Overrides the task index specified in the TF\_CONFIG environment variable. |
| `rpc_layer` | (String, optional) Overrides the rpc layer TensorFlow uses. |
| `environment` | (String, optional) Overrides the environment TensorFlow operates in. |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L149-L158)

cluster_spec()

Returns a ClusterSpec based on the TF\_CONFIG environment variable.

|     |
| --- |
| Returns |     |
| A ClusterSpec with information from the TF\_CONFIG environment variable. |     |

### `master`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L160-L200)

master(
        task_type=None, task_id=None, rpc_layer=None
    )

Returns the master address to use when creating a TensorFlow session.

|     |     |
| --- | --- |
| Args |     |
| `task_type` | (String, optional) Overrides and sets the task\_type of the master. |
| `task_id` | (Integer, optional) Overrides and sets the task id of the master. |
| `rpc_layer` | (String, optional) Overrides and sets the protocol over which TensorFlow nodes communicate with each other. |

|     |
| --- |
| Returns |     |
| The address of the master. |     |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If the task\_type or task\_id is not specified and the `TF_CONFIG` environment variable does not contain a task section. |

### `num_accelerators`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L140-L147)

num_accelerators(
        task_type=None, task_id=None, config_proto=None
    )

Returns the number of accelerator cores per worker.

This returns the number of accelerator cores (such as GPUs and TPUs) available per worker.

Optionally, we allow callers to specify the task\_type, and task\_id, for if they want to target a specific TensorFlow task to query the number of accelerators. This is to support heterogenous environments, where the number of accelerators cores per host is different.

|     |     |
| --- | --- |
| Args |     |
| `task_type` | (Optional) The type of the TensorFlow task of the machine we want to query. |
| `task_id` | (Optional) The index of the TensorFlow task of the machine we want to query. |
| `config_proto` | (Optional) Configuration for starting a new session to query how many accelerator cores it has. |

|     |
| --- |
| Returns |     |
| A map of accelerator types to number of cores. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.