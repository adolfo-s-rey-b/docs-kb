[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#num_accelerators)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.cluster\_resolver.GCEClusterResolver Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver#num_accelerators)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py#L30-L207)

ClusterResolver for Google Compute Engine.

Inherits From: [`ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.cluster_resolver.GCEClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver)

tf.distribute.cluster_resolver.GCEClusterResolver(
        project,
        zone,
        instance_group,
        port,
        task_type='worker',
        task_id=0,
        rpc_layer='grpc',
        credentials='default',
        service=None
    )

This is an implementation of cluster resolvers for the Google Compute Engine instance group platform. By specifying a project, zone, and instance group, this will retrieve the IP address of all the instances within the instance group and return a ClusterResolver object suitable for use for distributed TensorFlow.

Usage example with tf.distribute.Strategy:

  # On worker 0
      cluster_resolver = GCEClusterResolver("my-project", "us-west1",
                                            "my-instance-group",
                                            task_type="worker", task_id=0)
      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
          cluster_resolver=cluster_resolver)
    
      # On worker 1
      cluster_resolver = GCEClusterResolver("my-project", "us-west1",
                                            "my-instance-group",
                                            task_type="worker", task_id=1)
      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
          cluster_resolver=cluster_resolver)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `project` | Name of the GCE project. |
| `zone` | Zone of the GCE instance group. |
| `instance_group` | Name of the GCE instance group. |
| `port` | Port of the listening TensorFlow server (default: 8470) |
| `task_type` | Name of the TensorFlow job this GCE instance group of VM instances belong to. |
| `task_id` | The task index for this particular VM, within the GCE instance group. In particular, every single instance should be assigned a unique ordinal index within an instance group manually so that they can be distinguished from each other. |
| `rpc_layer` | The RPC layer TensorFlow should use to communicate across instances. |
| `credentials` | GCE Credentials. If nothing is specified, this defaults to GoogleCredentials.get\_application\_default(). |
| `service` | The GCE API object returned by the googleapiclient.discovery function. (Default: discovery.build('compute', 'v1')). If you specify a custom service object, then the credentials parameter will be ignored. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ImportError` | If the googleapiclient is not installed. |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py#L125-L168)

cluster_spec()

Returns a ClusterSpec object based on the latest instance group info.

This returns a ClusterSpec object for use based on information from the specified instance group. We will retrieve the information from the GCE APIs every time this method is called.

|     |
| --- |
| Returns |     |
| A ClusterSpec containing host information retrieved from GCE. |     |

### `master`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py#L170-L181)

master(
        task_type=None, task_id=None, rpc_layer=None
    )

Retrieves the name or URL of the session master.

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

Implementors of this function must take care in ensuring that the master returned is up-to-date at the time to calling this function. This usually means retrieving the master every time this function is invoked.

### `num_accelerators`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L130-L167)

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