[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#cluster_spec)
        
    *   [get\_task\_info](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#get_task_info)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#num_accelerators)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.cluster\_resolver.SlurmClusterResolver Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#cluster_spec)
        
    *   [get\_task\_info](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#get_task_info)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver#num_accelerators)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py#L163-L397)

ClusterResolver for system with Slurm workload manager.

Inherits From: [`ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.cluster_resolver.SlurmClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver)

tf.distribute.cluster_resolver.SlurmClusterResolver(
        jobs=None,
        port_base=8888,
        gpus_per_node=None,
        gpus_per_task=None,
        tasks_per_node=None,
        auto_set_gpu=True,
        rpc_layer='grpc'
    )

This is an implementation of ClusterResolver for Slurm clusters. This allows the specification of jobs and task counts, number of tasks per node, number of GPUs on each node and number of GPUs for each task. It retrieves system attributes by Slurm environment variables, resolves allocated computing node names, constructs a cluster and returns a ClusterResolver object which can be used for distributed TensorFlow.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `jobs` | Dictionary with job names as key and number of tasks in the job as value. Defaults to as many 'worker's as there are (Slurm) tasks. |
| `port_base` | The first port number to start with for processes on a node. |
| `gpus_per_node` | Number of GPUs available on each node. Defaults to the number of GPUs reported by nvidia-smi |
| `gpus_per_task` | Number of GPUs to be used for each task. Default is to evenly distribute the gpus\_per\_node to tasks\_per\_node. |
| `tasks_per_node` | Number of tasks running on each node. Can be an integer if the number of tasks per node is constant or a dictionary mapping hostnames to number of tasks on that node. If not set the Slurm environment is queried for the correct mapping. |
| `auto_set_gpu` | Set the visible CUDA devices automatically while resolving the cluster by setting CUDA\_VISIBLE\_DEVICES environment variable. Defaults to True. |
| `rpc_layer` | The protocol TensorFlow used to communicate between nodes. Defaults to 'grpc'. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If requested more GPUs per node than available or requested more tasks than assigned tasks or resolving missing values from the environment failed. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `environment` | Returns the current environment which TensorFlow is running in.<br><br>There are two possible return values, "google" (when TensorFlow is running in a Google-internal environment) or an empty string (when TensorFlow is running elsewhere).<br><br>If you are implementing a ClusterResolver that works in both the Google environment and the open-source world (for instance, a TPU ClusterResolver or similar), you will have to return the appropriate string depending on the environment, which you will have to detect.<br><br>Otherwise, if you are implementing a ClusterResolver that will only work in open-source TensorFlow, you do not need to implement this property. |
| `task_id` | Returns the task id this `ClusterResolver` indicates.<br><br>In TensorFlow distributed environment, each job may have an applicable task id, which is the index of the instance within its task type. This is useful when user needs to run specific code according to task index. For example,<br><br>cluster_spec = tf.train.ClusterSpec({<br>        "ps": ["localhost:2222", "localhost:2223"],<br>        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]<br>    })<br>    <br>    # SimpleClusterResolver is used here for illustration; other cluster<br>    # resolvers may be used for other source of task type/id.<br>    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",<br>                                            task_id=0)<br>    <br>    ...<br>    <br>    if cluster_resolver.task_type == 'worker' and cluster_resolver.task_id == 0:<br>      # Perform something that's only applicable on 'worker' type, id 0. This<br>      # block will run on this particular instance since we've specified this<br>      # task to be a 'worker', id 0 in above cluster resolver.<br>    else:<br>      # Perform something that's only applicable on other ids. This block will<br>      # not run on this particular instance.<br><br>Returns `None` if such information is not available or is not applicable in the current distributed environment, such as training with [`tf.distribute.cluster_resolver.TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)<br>.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s class docstring. |
| `task_type` | Returns the task type this `ClusterResolver` indicates.<br><br>In TensorFlow distributed environment, each job may have an applicable task type. Valid task types in TensorFlow include 'chief': a worker that is designated with more responsibility, 'worker': a regular worker for training/evaluation, 'ps': a parameter server, or 'evaluator': an evaluator that evaluates the checkpoints for metrics.<br><br>See [Multi-worker configuration](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration)<br> for more information about 'chief' and 'worker' task type, which are most commonly used.<br><br>Having access to such information is useful when user needs to run specific code according to task types. For example,<br><br>cluster_spec = tf.train.ClusterSpec({<br>        "ps": ["localhost:2222", "localhost:2223"],<br>        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]<br>    })<br>    <br>    # SimpleClusterResolver is used here for illustration; other cluster<br>    # resolvers may be used for other source of task type/id.<br>    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",<br>                                            task_id=1)<br>    <br>    ...<br>    <br>    if cluster_resolver.task_type == 'worker':<br>      # Perform something that's only applicable on workers. This block<br>      # will run on this particular instance since we've specified this task to<br>      # be a worker in above cluster resolver.<br>    elif cluster_resolver.task_type == 'ps':<br>      # Perform something that's only applicable on parameter servers. This<br>      # block will not run on this particular instance.<br><br>Returns `None` if such information is not available or is not applicable in the current distributed environment, such as training with [`tf.distribute.experimental.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TPUStrategy)<br>.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s class doc. |

Methods
-------

### `cluster_spec`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py#L300-L353)

cluster_spec()

Returns a ClusterSpec object based on the latest instance group info.

This returns a ClusterSpec object for use based on information from the specified initialization parameters and Slurm environment variables. The cluster specification is resolved each time this function is called. The resolver extract hostnames of nodes by scontrol and pack tasks in that order until a node a has number of tasks that is equal to specification. GPUs on nodes are allocated to tasks by specification through setting CUDA\_VISIBLE\_DEVICES environment variable.

|     |
| --- |
| Returns |     |
| A ClusterSpec containing host information retrieved from Slurm's environment variables. |     |

### `get_task_info`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py#L355-L367)

get_task_info()

Returns job name and task\_id for the process which calls this.

This returns the job name and task index for the process which calls this function according to its rank and cluster specification. The job name and task index are set after a cluster is constructed by cluster\_spec otherwise defaults to None.

|     |
| --- |
| Returns |     |
| A string specifying job name the process belongs to and an integer specifying the task index the process belongs to in that job. |     |

### `master`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py#L369-L389)

master(
        task_type=None, task_id=None, rpc_layer=None
    )

Returns the master string for connecting to a TensorFlow master.

|     |     |
| --- | --- |
| Args |     |
| `task_type` | (Optional) Overrides the default auto-selected task type. |
| `task_id` | (Optional) Overrides the default auto-selected task index. |
| `rpc_layer` | (Optional) Overrides the default RPC protocol TensorFlow uses to communicate across nodes. |

|     |
| --- |
| Returns |     |
| A connection string for connecting to a TensorFlow master. |     |

### `num_accelerators`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py#L391-L397)

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