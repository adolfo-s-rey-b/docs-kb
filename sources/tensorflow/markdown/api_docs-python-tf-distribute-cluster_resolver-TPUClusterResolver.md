[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#cluster_spec)
        
    *   [connect](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#connect)
        
    *   [get\_coordination\_service\_leader](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#get_coordination_service_leader)
        
    *   [get\_job\_name](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#get_job_name)
        
    *   [get\_master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#get_master)
        
    *   [get\_tpu\_system\_metadata](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#get_tpu_system_metadata)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#num_accelerators)
        
    *   [set\_tpu\_topology](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#set_tpu_topology)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.cluster\_resolver.TPUClusterResolver Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#methods)
    *   [cluster\_spec](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#cluster_spec)
        
    *   [connect](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#connect)
        
    *   [get\_coordination\_service\_leader](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#get_coordination_service_leader)
        
    *   [get\_job\_name](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#get_job_name)
        
    *   [get\_master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#get_master)
        
    *   [get\_tpu\_system\_metadata](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#get_tpu_system_metadata)
        
    *   [master](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#master)
        
    *   [num\_accelerators](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#num_accelerators)
        
    *   [set\_tpu\_topology](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#set_tpu_topology)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L95-L480)

Cluster Resolver for Google Cloud TPUs.

Inherits From: [`ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.cluster_resolver.TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)

tf.distribute.cluster_resolver.TPUClusterResolver(
        tpu=None,
        zone=None,
        project=None,
        job_name='worker',
        coordinator_name=None,
        coordinator_address=None,
        credentials='default',
        service=None,
        discovery_url=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding)<br>    <br>*   [Migrate from TPUEstimator to TPUStrategy](https://www.tensorflow.org/guide/migrate/tpu_estimator)<br>    <br>*   [Use TPUs](https://www.tensorflow.org/guide/tpu) | *   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index)<br>    <br>*   [Image classification with Model Garden](https://www.tensorflow.org/tfmodels/vision/image_classification)<br>    <br>*   [Instance Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)<br>    <br>*   [Object detection with Model Garden](https://www.tensorflow.org/tfmodels/vision/object_detection)<br>    <br>*   [Semantic Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation) |

This is an implementation of cluster resolvers for the Google Cloud TPU service.

TPUClusterResolver supports the following distinct environments: Google Compute Engine Google Kubernetes Engine Google internal

It can be passed into [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
 to support TF2 training on Cloud TPUs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tpu` | A string corresponding to the TPU to use. It can be the TPU name or TPU worker gRPC address. If not set, it will try automatically resolve the TPU address on Cloud TPUs. If set to "local", it will assume that the TPU is directly connected to the VM instead of over the network. |
| `zone` | Zone where the TPUs are located. If omitted or empty, we will assume that the zone of the TPU is the same as the zone of the GCE VM, which we will try to discover from the GCE metadata service. |
| `project` | Name of the GCP project containing Cloud TPUs. If omitted or empty, we will try to discover the project name of the GCE VM from the GCE metadata service. |
| `job_name` | Name of the TensorFlow job the TPUs belong to. |
| `coordinator_name` | The name to use for the coordinator. Set to None if the coordinator should not be included in the computed ClusterSpec. |
| `coordinator_address` | The address of the coordinator (typically an ip:port pair). If set to None, a TF server will be started. If coordinator\_name is None, a TF server will not be started even if coordinator\_address is None. |
| `credentials` | GCE Credentials. If None, then we use default credentials from the oauth2client |
| `service` | The GCE API object returned by the googleapiclient.discovery function. If you specify a custom service object, then the credentials parameter will be ignored. |
| `discovery_url` | A URL template that points to the location of the discovery service. It should have two parameters {api} and {apiVersion} that when filled in produce an absolute URL to the discovery document for that service. The environment variable 'TPU\_API\_DISCOVERY\_URL' will override this. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ImportError` | If the googleapiclient is not installed. |
| `ValueError` | If no TPUs are specified. |
| `RuntimeError` | If an empty TPU name is specified and this is running in a Google Cloud environment. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `environment` | Returns the current environment which TensorFlow is running in. |
| `task_id` | Returns the task id this `ClusterResolver` indicates.<br><br>In TensorFlow distributed environment, each job may have an applicable task id, which is the index of the instance within its task type. This is useful when user needs to run specific code according to task index. For example,<br><br>cluster_spec = tf.train.ClusterSpec({<br>        "ps": ["localhost:2222", "localhost:2223"],<br>        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]<br>    })<br>    <br>    # SimpleClusterResolver is used here for illustration; other cluster<br>    # resolvers may be used for other source of task type/id.<br>    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",<br>                                            task_id=0)<br>    <br>    ...<br>    <br>    if cluster_resolver.task_type == 'worker' and cluster_resolver.task_id == 0:<br>      # Perform something that's only applicable on 'worker' type, id 0. This<br>      # block will run on this particular instance since we've specified this<br>      # task to be a 'worker', id 0 in above cluster resolver.<br>    else:<br>      # Perform something that's only applicable on other ids. This block will<br>      # not run on this particular instance.<br><br>Returns `None` if such information is not available or is not applicable in the current distributed environment, such as training with [`tf.distribute.cluster_resolver.TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)<br>.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s class docstring. |
| `task_type` | Returns the task type this `ClusterResolver` indicates.<br><br>In TensorFlow distributed environment, each job may have an applicable task type. Valid task types in TensorFlow include 'chief': a worker that is designated with more responsibility, 'worker': a regular worker for training/evaluation, 'ps': a parameter server, or 'evaluator': an evaluator that evaluates the checkpoints for metrics.<br><br>See [Multi-worker configuration](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration)<br> for more information about 'chief' and 'worker' task type, which are most commonly used.<br><br>Having access to such information is useful when user needs to run specific code according to task types. For example,<br><br>cluster_spec = tf.train.ClusterSpec({<br>        "ps": ["localhost:2222", "localhost:2223"],<br>        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]<br>    })<br>    <br>    # SimpleClusterResolver is used here for illustration; other cluster<br>    # resolvers may be used for other source of task type/id.<br>    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",<br>                                            task_id=1)<br>    <br>    ...<br>    <br>    if cluster_resolver.task_type == 'worker':<br>      # Perform something that's only applicable on workers. This block<br>      # will run on this particular instance since we've specified this task to<br>      # be a worker in above cluster resolver.<br>    elif cluster_resolver.task_type == 'ps':<br>      # Perform something that's only applicable on parameter servers. This<br>      # block will not run on this particular instance.<br><br>Returns `None` if such information is not available or is not applicable in the current distributed environment, such as training with [`tf.distribute.experimental.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TPUStrategy)<br>.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s class doc. |
| `tpu_hardware_feature` | Returns the tpu topology info stored. |

Methods
-------

### `cluster_spec`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L351-L388)

cluster_spec()

Returns a ClusterSpec object based on the latest TPU information.

We retrieve the information from the GCE APIs every time this method is called.

|     |
| --- |
| Returns |     |
| A ClusterSpec containing host information returned from Cloud TPUs, or None. |     |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If the provided TPU is not healthy. |

### `connect`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L110-L148)

@staticmethod

Initializes TPU and returns a TPUClusterResolver.

This API will connect to remote TPU cluster and initialize the TPU hardwares. Example usage:

    resolver = tf.distribute.cluster_resolver.TPUClusterResolver.connect(

It can be viewed as convenient wrapper of the following code:

    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')

|     |     |
| --- | --- |
| Args |     |
| `tpu` | A string corresponding to the TPU to use. It can be the TPU name or TPU worker gRPC address. If not set, it will try automatically resolve the TPU address on Cloud TPUs. |
| `zone` | Zone where the TPUs are located. If omitted or empty, we will assume that the zone of the TPU is the same as the zone of the GCE VM, which we will try to discover from the GCE metadata service. |
| `project` | Name of the GCP project containing Cloud TPUs. If omitted or empty, we will try to discover the project name of the GCE VM from the GCE metadata service. |

|     |
| --- |
| Returns |     |
| An instance of TPUClusterResolver object. |     |

|     |     |
| --- | --- |
| Raises |     |
| `NotFoundError` | If no TPU devices found in eager mode. |

### `get_coordination_service_leader`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L316-L324)

get_coordination_service_leader()

Returns the location for coordination service.

The coordination service should be located on TPU worker0.

|     |
| --- |
| Returns |     |
| A string indicate the location path. |     |

### `get_job_name`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L313-L314)

get_job_name()

### `get_master`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L310-L311)

get_master()

### `get_tpu_system_metadata`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L326-L349)

get_tpu_system_metadata()

Returns the metadata of the TPU system.

Users can call this method to get some facts of the TPU system, like total number of cores, number of TPU workers and the devices. E.g.

resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tpu_system_metadata = resolver.get_tpu_system_metadata()
    num_hosts = tpu_system_metadata.num_hosts

|     |
| --- |
| Returns |     |
| A [`tf.tpu.experimental.TPUSystemMetadata`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/TPUSystemMetadata)<br> object. |     |

### `master`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L266-L308)

master(
        task_type=None, task_id=None, rpc_layer=None
    )

Get the Master string to be used for the session.

In the normal case, this returns the grpc path (grpc://1.2.3.4:8470) of first instance in the ClusterSpec returned by the cluster\_spec function.

If a non-TPU name is used when constructing a TPUClusterResolver, that will be returned instead (e.g. If the tpus argument's value when constructing this TPUClusterResolver was 'grpc://10.240.1.2:8470', 'grpc://10.240.1.2:8470' will be returned).

|     |     |
| --- | --- |
| Args |     |
| `task_type` | (Optional, string) The type of the TensorFlow task of the master. |
| `task_id` | (Optional, integer) The index of the TensorFlow task of the master. |
| `rpc_layer` | (Optional, string) The RPC protocol TensorFlow should use to communicate with TPUs. |

|     |
| --- |
| Returns |     |
| string, the connection string to use when creating a session. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If none of the TPUs specified exists. |

### `num_accelerators`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L390-L444)

num_accelerators(
        task_type=None, task_id=None, config_proto=None
    )

Returns the number of TPU cores per worker.

Connects to the master and list all the devices present in the master, and counts them up. Also verifies that the device counts per host in the cluster is the same before returning the number of TPU cores per host.

|     |     |
| --- | --- |
| Args |     |
| `task_type` | Unused. |
| `task_id` | Unused. |
| `config_proto` | Used to create a connection to a TPU master in order to retrieve the system metadata. |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If we cannot talk to a TPU worker after retrying or if the number of TPU devices per host is different. |

### `set_tpu_topology`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L446-L449)

set_tpu_topology(
        serialized_tpu_topology
    )

Sets the tpu topology info stored in this resolver.

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L260-L261)

__enter__()

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L263-L264)

__exit__(
        type, value, traceback
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.