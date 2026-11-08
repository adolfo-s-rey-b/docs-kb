[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#methods_2)
    *   [distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#distribute_dataset)
        
    *   [distribute\_tf\_dataset](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#distribute_tf_dataset)
        
    *   [get\_data\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#get_data_layout)
        
    *   [get\_tensor\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#get_tensor_layout)
        
    *   [get\_variable\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#get_variable_layout)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distribution.DataParallel Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#methods_2)
    *   [distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#distribute_dataset)
        
    *   [distribute\_tf\_dataset](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#distribute_tf_dataset)
        
    *   [get\_data\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#get_data_layout)
        
    *   [get\_tensor\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#get_tensor_layout)
        
    *   [get\_variable\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#get_variable_layout)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DataParallel?version=stable#scope)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L532-L625)

Distribution for data parallelism.

tf.keras.distribution.DataParallel(
        device_mesh=None, devices=None, auto_shard_dataset=True
    )

You can choose to create this instance by either specifying the `device_mesh` or `devices` arguments (but not both).

The `device_mesh` argument is expected to be a `DeviceMesh` instance, and is expected to be 1D only. In case that the mesh has multiple axes, then the first axis will be treated as the data parallel dimension (and a warning will be raised).

When a list of `devices` are provided, they will be used to construct a 1D mesh.

When both `mesh` and `devices` are absent, then `list_devices()` will be used to detect any available devices and create a 1D mesh from them.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_mesh` | Optional `DeviceMesh` instance. |
| `devices` | Optional list of devices. |
| `auto_shard_dataset` | Automatically shard the dataset amongst processes in a multi-process setting. Set to `False` if the dataset is already sharded across hosts. Defaults to `True`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `auto_shard_dataset` |     |
| `batch_dim_name` |     |
| `data_shard_id` | ID of the data shard for the current process. |
| `device_mesh` |     |
| `num_model_replicas` | Number of model replicas. |
| `num_processes` | Total number of processes in the cluster. |

Methods
-------

### `distribute_dataset`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L425-L451)

distribute_dataset(
        dataset
    )

Create a distributed dataset from the original global dataset.

|     |     |
| --- | --- |
| Args |     |
| `dataset` | the original global dataset instance. |

|     |
| --- |
| Returns |     |
| If `auto_shard_dataset` is `True`, returns a sharded dataset that only produces data for the current local worker/process. Otherwise, returns the original dataset. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if auto-sharding is requested in a multi-process setting, but the dataset type is not supported. |

### `distribute_tf_dataset`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L453-L523)

distribute_tf_dataset(
        dataset
    )

### `get_data_layout`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L610-L613)

get_data_layout(
        data_shape
    )

Retrieve the `TensorLayout` for the input data.

|     |     |
| --- | --- |
| Args |     |
| `data_shape` | shape for the input data in list or tuple format. |

|     |
| --- |
| Returns |     |
| The `TensorLayout` for the data, which can be used by `backend.distribute_value()` to redistribute a input data. |     |

### `get_tensor_layout`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L623-L625)

get_tensor_layout(
        path
    )

Retrieve the `TensorLayout` for the intermediate tensor.

|     |     |
| --- | --- |
| Args |     |
| `path` | a string path for the corresponding tensor. |

return: The `TensorLayout` for the intermediate tensor, which can be used by `backend.relayout()` to reshard the tensor. Could also return None.

### `get_variable_layout`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L615-L621)

get_variable_layout(
        variable
    )

Retrieve the `TensorLayout` for the variable.

|     |     |
| --- | --- |
| Args |     |
| `variable` | A `Variable` instance. |

return: The `TensorLayout` for the variable, which can be used by `backend.distribute_value()` to redistribute a variable.

### `scope`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L399-L407)

@contextlib.contextmanager

Context manager to make the `Distribution` current.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.