[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdistribution%2FModelParallel%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#methods_2)
    *   [distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#distribute_dataset)
        
    *   [distribute\_tf\_dataset](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#distribute_tf_dataset)
        
    *   [get\_data\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#get_data_layout)
        
    *   [get\_tensor\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#get_tensor_layout)
        
    *   [get\_variable\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#get_variable_layout)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distribution.ModelParallel Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#methods_2)
    *   [distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#distribute_dataset)
        
    *   [distribute\_tf\_dataset](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#distribute_tf_dataset)
        
    *   [get\_data\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#get_data_layout)
        
    *   [get\_tensor\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#get_tensor_layout)
        
    *   [get\_variable\_layout](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#get_variable_layout)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/ModelParallel?version=stable#scope)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L628-L771)

Distribution that shards model variables.

tf.keras.distribution.ModelParallel(
        *, layout_map=None, batch_dim_name=None, auto_shard_dataset=True, **kwargs
    )

Compare to `DataParallel` which replicates the variables across all devices, `ModelParallel` allows you to shard variables in addition to the input data.

To construct a `ModelParallel` distribution, you need to provide a `DeviceMesh` and a `LayoutMap`.

1.  `DeviceMesh` contains physical device information. The axis names in the mesh will be used to map the variable and data layout.
2.  `LayoutMap` contains the mapping between variable paths to their corresponding `TensorLayout`.

#### Example:

devices = list_devices()    # Assume there are 8 devices.
    
    # Create a mesh with 2 devices for data parallelism and 4 devices for
    # model parallelism.
    device_mesh = DeviceMesh(shape=(2, 4), axis_names=('batch', 'model'),
                             devices=devices)
    # Create a layout map that shard the `Dense` layer and `Conv2D`
    # layer variables on the last dimension.
    # Based on the `device_mesh`, this means the variables
    # will be split across 4 devices. Any other variable that doesn't
    # match any key in the layout map will be fully replicated.
    layout_map = LayoutMap(device_mesh)
    layout_map['.*dense.*kernel'] = (None, 'model')
    layout_map['.*dense.*bias'] = ('model',)
    layout_map['.*conv2d.*kernel'] = (None, None, None, 'model')
    layout_map['.*conv2d.*bias'] = ('model',)
    
    distribution = ModelParallel(
        layout_map=layout_map,
        batch_dim_name='batch',
    )
    
    # Set the global distribution, or via `with distribution.scope():`
    set_distribution(distribution)
    
    model = model_creation()
    model.compile()
    model.fit(data)

You can quickly update the device mesh shape to change the sharding factor of the variables. E.g.

# With only the shape change for the device mesh, the variables will be
    # sharded across 8 devices instead of 4, which further reduces the memory
    # footprint of variables on each of the device.
    device_mesh = DeviceMesh(
        shape=(1, 8),
        axis_names=('batch', 'model'),
        devices=devices,
    )

To figure out a proper layout mapping rule for all the model variables, you can first list out all the model variable paths, which will be used as the key to map the variables to `TensorLayout`.

e.g.

model = create_model()
    for v in model.variables:
        print(v.path)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `layout_map` | `LayoutMap` instance which map the variable path to the corresponding tensor layout. |
| `batch_dim_name` | Optional string, the axis name in the device mesh (of the `layout_map` object) that will be used to distribute data. If unspecified, the first axis from the device mesh will be used. |
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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L754-L757)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L770-L771)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L759-L768)

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