[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#methods)
    *   [as\_cluster\_def](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#as_cluster_def)
        
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#as_dict)
        
    *   [job\_tasks](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#job_tasks)
        
    *   [num\_tasks](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#num_tasks)
        
    *   [task\_address](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#task_address)
        
    *   [task\_indices](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#task_indices)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#__ne__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#__nonzero__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.ClusterSpec Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#methods)
    *   [as\_cluster\_def](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#as_cluster_def)
        
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#as_dict)
        
    *   [job\_tasks](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#job_tasks)
        
    *   [num\_tasks](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#num_tasks)
        
    *   [task\_address](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#task_address)
        
    *   [task\_indices](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#task_indices)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#__ne__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec#__nonzero__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L242-L492)

Represents a cluster as a set of "tasks", organized into "jobs".

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.ClusterSpec`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec)

tf.train.ClusterSpec(
        cluster
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) |

A [`tf.train.ClusterSpec`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec)
 represents the set of processes that participate in a distributed TensorFlow computation. Every [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
 is constructed in a particular cluster.

To create a cluster with two jobs and five tasks, you specify the mapping from job names to lists of network addresses (typically hostname-port pairs).

cluster = tf.train.ClusterSpec({"worker": ["worker0.example.com:2222",\
                                               "worker1.example.com:2222",\
                                               "worker2.example.com:2222"],
                                    "ps": ["ps0.example.com:2222",\
                                           "ps1.example.com:2222"]})

Each job may also be specified as a sparse mapping from task indices to network addresses. This enables a server to be configured without needing to know the identity of (for example) all other worker tasks:

cluster = tf.train.ClusterSpec({"worker": {1: "worker1.example.com:2222"},
                                    "ps": ["ps0.example.com:2222",\
                                           "ps1.example.com:2222"]})

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cluster` | A dictionary mapping one or more job names to (i) a list of network addresses, or (ii) a dictionary mapping integer task indices to network addresses; or a [`tf.train.ClusterDef`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterDef)<br> protocol buffer. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `cluster` is not a dictionary mapping strings to lists of strings, and not a [`tf.train.ClusterDef`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterDef)<br> protobuf. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `jobs` | Returns a list of job names in this cluster. |

Methods
-------

### `as_cluster_def`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L364-L366)

as_cluster_def()

Returns a [`tf.train.ClusterDef`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterDef)
 protocol buffer based on this cluster.

### `as_dict`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L337-L362)

as_dict()

Returns a dictionary from job names to their tasks.

For each job, if the task index space is dense, the corresponding value will be a list of network addresses; otherwise it will be a dictionary mapping (sparse) task indices to the corresponding addresses.

|     |
| --- |
| Returns |     |
| A dictionary mapping job names to lists or dictionaries describing the tasks in those jobs. |     |

### `job_tasks`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L438-L465)

job_tasks(
        job_name
    )

Returns a mapping from task ID to address in the given job.

|     |     |
| --- | --- |
| Args |     |
| `job_name` | The string name of a job in this cluster. |

|     |
| --- |
| Returns |     |
| A list of task addresses, where the index in the list corresponds to the task index of each task. The list may contain `None` if the job was defined with a sparse set of task indices. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `job_name` does not name a job in this cluster. |

### `num_tasks`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L377-L393)

num_tasks(
        job_name
    )

Returns the number of tasks defined in the given job.

|     |     |
| --- | --- |
| Args |     |
| `job_name` | The string name of a job in this cluster. |

|     |
| --- |
| Returns |     |
| The number of tasks defined in the given job. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `job_name` does not name a job in this cluster. |

### `task_address`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L414-L436)

task_address(
        job_name, task_index
    )

Returns the address of the given task in the given job.

|     |     |
| --- | --- |
| Args |     |
| `job_name` | The string name of a job in this cluster. |
| `task_index` | A non-negative integer. |

|     |
| --- |
| Returns |     |
| The address of the given task in the given job. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `job_name` does not name a job in this cluster, or no task with index `task_index` is defined in that job. |

### `task_indices`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L395-L412)

task_indices(
        job_name
    )

Returns a list of valid task indices in the given job.

|     |     |
| --- | --- |
| Args |     |
| `job_name` | The string name of a job in this cluster. |

|     |
| --- |
| Returns |     |
| A list of valid task indices in the given job. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `job_name` does not name a job in this cluster, or no task with index `task_index` is defined in that job. |

### `__bool__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L318-L319)

__bool__()

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L324-L325)

__eq__(
        other
    )

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L327-L328)

__ne__(
        other
    )

Return self!=value.

### `__nonzero__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L318-L319)

__nonzero__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.