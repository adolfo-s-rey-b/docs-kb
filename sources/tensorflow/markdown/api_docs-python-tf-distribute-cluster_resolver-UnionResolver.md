[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#num_accelerators)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.cluster\_resolver.UnionResolver Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver#num_accelerators)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L418-L624)

Performs a union on underlying ClusterResolvers.

Inherits From: [`ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.cluster_resolver.UnionResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver)

tf.distribute.cluster_resolver.UnionResolver(
        *args, **kwargs
    )

This class performs a union given two or more existing ClusterResolvers. It merges the underlying ClusterResolvers, and returns one unified ClusterSpec when cluster\_spec is called. The details of the merge function is documented in the cluster\_spec function.

For additional ClusterResolver properties such as task type, task index, rpc layer, environment, etc..., we will return the value from the first ClusterResolver in the union.

An example to combine two cluster resolvers:

  cluster_0 = tf.train.ClusterSpec({"worker": ["worker0.example.com:2222",\
                                                   "worker1.example.com:2222"]})
      cluster_resolver_0 = SimpleClusterResolver(cluster, task_type="worker",
                                                 task_id=0,
                                                 rpc_layer="grpc")
    
      cluster_1 = tf.train.ClusterSpec({"ps": ["ps0.example.com:2222",\
                                               "ps1.example.com:2222"]})
      cluster_resolver_1 = SimpleClusterResolver(cluster, task_type="ps",
                                                 task_id=0,
                                                 rpc_layer="grpc")
    
      # Its task type would be "worker".
      cluster_resolver = UnionClusterResolver(cluster_resolver_0,
                                              cluster_resolver_1)

An example to override the number of GPUs in a TFConfigClusterResolver instance:

  tf_config = TFConfigClusterResolver()
      gpu_override = SimpleClusterResolver(tf_config.cluster_spec(),
                                           num_accelerators={"GPU": 1})
      cluster_resolver = UnionResolver(gpu_override, tf_config)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `*args` | `ClusterResolver` objects to be unionized. |
| `**kwargs` | rpc\_layer - (Optional) Override value for the RPC layer used by TensorFlow. task\_type - (Optional) Override value for the current task type. task\_id - (Optional) Override value for the current task index. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If any argument is not a subclass of `ClusterResolvers`. |
| `ValueError` | If there are no arguments passed. |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L495-L567)

cluster_spec()

Returns a union of all the ClusterSpecs from the ClusterResolvers.

|     |
| --- |
| Returns |     |
| A ClusterSpec containing host information merged from all the underlying ClusterResolvers. |     |

|     |     |
| --- | --- |
| Raises |     |
| `KeyError` | If there are conflicting keys detected when merging two or more dictionaries, this exception is raised. |

If _all_ underlying ClusterSpecs expose the set of workers as lists, we will concatenate the lists of workers, starting with the list of workers from the first ClusterResolver passed into the constructor.

If _any_ of the ClusterSpecs expose the set of workers as a dict, we will treat all the sets of workers as dicts (even if they are returned as lists) and will only merge them into a dict if there is no conflicting keys. If there is a conflicting key, we will raise a `KeyError`.

### `master`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L569-L589)

master(
        task_type=None, task_id=None, rpc_layer=None
    )

Returns the master address to use when creating a session.

This usually returns the master from the first ClusterResolver passed in, but you can override this by specifying the task\_type and task\_id.

|     |     |
| --- | --- |
| Args |     |
| `task_type` | (Optional) The type of the TensorFlow task of the master. |
| `task_id` | (Optional) The index of the TensorFlow task of the master. |
| `rpc_layer` | (Optional) The RPC protocol for the given cluster. |

|     |
| --- |
| Returns |     |
| The name or URL of the session master. |     |

### `num_accelerators`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L611-L616)

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