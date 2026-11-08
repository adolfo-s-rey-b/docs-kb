[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fcluster_resolver%2FKubernetesClusterResolver&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#num_accelerators)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.cluster\_resolver.KubernetesClusterResolver Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#cluster_spec)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver#num_accelerators)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L41-L214)

ClusterResolver for Kubernetes.

Inherits From: [`ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.cluster_resolver.KubernetesClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver)

tf.distribute.cluster_resolver.KubernetesClusterResolver(
        job_to_label_mapping=None,
        tf_server_port=8470,
        rpc_layer='grpc',
        override_client=None,
        executable_location=tf.distribute.cluster_resolver.KubernetesExecutableLocation.WITHIN_CLUSTER
    )

This is an implementation of cluster resolvers for Kubernetes. When given the the Kubernetes namespace and label selector for pods, we will retrieve the pod IP addresses of all running pods matching the selector, and return a ClusterSpec based on that information.

Usage example with tf.distribute.Strategy:

  # On worker 0
      cluster_resolver = KubernetesClusterResolver(
          {"worker": ["job-name=worker-cluster-a", "job-name=worker-cluster-b"]})
      cluster_resolver.task_type = "worker"
      cluster_resolver.task_id = 0
      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
          cluster_resolver=cluster_resolver)
    
      # On worker 1
      cluster_resolver = KubernetesClusterResolver(
          {"worker": ["job-name=worker-cluster-a", "job-name=worker-cluster-b"]})
      cluster_resolver.task_type = "worker"
      cluster_resolver.task_id = 1
      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
          cluster_resolver=cluster_resolver)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `job_to_label_mapping` | A mapping of TensorFlow jobs to label selectors. This allows users to specify many TensorFlow jobs in one Cluster Resolver, and each job can have pods belong with different label selectors. For example, a sample mapping might be<br><br>{'worker': ['job-name=worker-cluster-a', 'job-name=worker-cluster-b'],<br>     'ps': ['job-name=ps-1', 'job-name=ps-2']} |
| `tf_server_port` | The port the TensorFlow server is listening on. |
| `rpc_layer` | (Optional) The RPC layer TensorFlow should use to communicate between tasks in Kubernetes. Defaults to 'grpc'. |
| `override_client` | The Kubernetes client (usually automatically retrieved using `from kubernetes import client as k8sclient`). If you pass this in, you are responsible for setting Kubernetes credentials manually and calling `k8sconfig.load_kube_config()` or `k8sconfig.load_incluster_config()` before using this ClusterResolver. |
| `executable_location` | Parameter that specifies whether or not this TensorFlow code is running from within a K8S cluster or not. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ImportError` | If the Kubernetes Python client is not installed and no `override_client` is passed in. |
| `RuntimeError` | If autoresolve\_task is not a boolean or a callable. |
| `ValueError` | If `executable_location` is not a valid value. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `environment` | Returns the current environment which TensorFlow is running in.<br><br>There are two possible return values, "google" (when TensorFlow is running in a Google-internal environment) or an empty string (when TensorFlow is running elsewhere).<br><br>If you are implementing a ClusterResolver that works in both the Google environment and the open-source world (for instance, a TPU ClusterResolver or similar), you will have to return the appropriate string depending on the environment, which you will have to detect.<br><br>Otherwise, if you are implementing a ClusterResolver that will only work in open-source TensorFlow, you do not need to implement this property. |
| `task_id` | Returns the task id this `ClusterResolver` indicates.<br><br>In TensorFlow distributed environment, each job may have an applicable task id, which is the index of the instance within its task type. This is useful when user needs to run specific code according to task index. For example,<br><br>cluster_spec = tf.train.ClusterSpec({<br>        "ps": ["localhost:2222", "localhost:2223"],<br>        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]<br>    })<br>    <br>    # SimpleClusterResolver is used here for illustration; other cluster<br>    # resolvers may be used for other source of task type/id.<br>    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",<br>                                            task_id=0)<br>    <br>    ...<br>    <br>    if cluster_resolver.task_type == 'worker' and cluster_resolver.task_id == 0:<br>      # Perform something that's only applicable on 'worker' type, id 0. This<br>      # block will run on this particular instance since we've specified this<br>      # task to be a 'worker', id 0 in above cluster resolver.<br>    else:<br>      # Perform something that's only applicable on other ids. This block will<br>      # not run on this particular instance.<br><br>Returns `None` if such information is not available or is not applicable in the current distributed environment, such as training with [`tf.distribute.cluster_resolver.TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)<br>.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s class docstring. |
| `task_type` | Returns the task type this `ClusterResolver` indicates.<br><br>In TensorFlow distributed environment, each job may have an applicable task type. Valid task types in TensorFlow include 'chief': a worker that is designated with more responsibility, 'worker': a regular worker for training/evaluation, 'ps': a parameter server, or 'evaluator': an evaluator that evaluates the checkpoints for metrics.<br><br>See [Multi-worker configuration](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration)<br> for more information about 'chief' and 'worker' task type, which are most commonly used.<br><br>Having access to such information is useful when user needs to run specific code according to task types. For example,<br><br>cluster_spec = tf.train.ClusterSpec({<br>        "ps": ["localhost:2222", "localhost:2223"],<br>        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]<br>    })<br>    <br>    # SimpleClusterResolver is used here for illustration; other cluster<br>    # resolvers may be used for other source of task type/id.<br>    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",<br>                                            task_id=1)<br>    <br>    ...<br>    <br>    if cluster_resolver.task_type == 'worker':<br>      # Perform something that's only applicable on workers. This block<br>      # will run on this particular instance since we've specified this task to<br>      # be a worker in above cluster resolver.<br>    elif cluster_resolver.task_type == 'ps':<br>      # Perform something that's only applicable on parameter servers. This<br>      # block will not run on this particular instance.<br><br>Returns `None` if such information is not available or is not applicable in the current distributed environment, such as training with [`tf.distribute.experimental.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TPUStrategy)<br>.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s class doc. |

Methods
-------

### `cluster_spec`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L173-L214)

cluster_spec()

Returns a ClusterSpec object based on the latest info from Kubernetes.

We retrieve the information from the Kubernetes master every time this method is called.

|     |
| --- |
| Returns |     |
| A ClusterSpec containing host information returned from Kubernetes. |     |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If any of the pods returned by the master is not in the `Running` phase. |

### `master`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L145-L171)

master(
        task_type=None, task_id=None, rpc_layer=None
    )

Returns the master address to use when creating a session.

You must have set the task\_type and task\_id object properties before calling this function, or pass in the `task_type` and `task_id` parameters when using this function. If you do both, the function parameters will override the object properties.

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