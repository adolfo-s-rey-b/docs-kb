[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2FTopology&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#methods)
    *   [cpu\_device\_name\_at\_coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#cpu_device_name_at_coordinates)
        
    *   [serialized](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#serialized)
        
    *   [task\_ordinal\_at\_coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#task_ordinal_at_coordinates)
        
    *   [tpu\_device\_name\_at\_coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#tpu_device_name_at_coordinates)
        
    *   [tpu\_device\_ordinal\_at\_coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#tpu_device_ordinal_at_coordinates)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.Topology Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#methods)
    *   [cpu\_device\_name\_at\_coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#cpu_device_name_at_coordinates)
        
    *   [serialized](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#serialized)
        
    *   [task\_ordinal\_at\_coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#task_ordinal_at_coordinates)
        
    *   [tpu\_device\_name\_at\_coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#tpu_device_name_at_coordinates)
        
    *   [tpu\_device\_ordinal\_at\_coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology#tpu_device_ordinal_at_coordinates)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/topology.py#L40-L241)

Describes a set of TPU devices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.Topology`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology)

tf.tpu.experimental.Topology(
        serialized=None, mesh_shape=None, device_coordinates=None
    )

Represents both the shape of the physical mesh, and the mapping between TensorFlow TPU devices to physical mesh coordinates.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `serialized` | A serialized `TopologyProto`, or `None`. If not `None`, the serialized proto is parsed to discover the topology. |
| `mesh_shape` | A sequence of 4 positive integers, or `None`. If not `None`, the shape of the TPU topology, in number of cores. Ignored if `serialized` is not `None`. |
| `device_coordinates` | A rank 3 numpy array that describes the mapping from TensorFlow TPU devices to TPU fabric coordinates, or `None`. If specified, array is a rank 3 int32 array with shape `[tasks, devices, axis]`. `tasks` is the number of tasks in the TPU cluster, `devices` is the number of TPU devices per task, and `axis` is the number of axes in the TPU cluster topology. Each entry gives the `axis`\-th coordinate in the topology of a task/device pair. TPU topologies are 4-dimensional, with dimensions `(x, y, z, core number)`. This arg is ignored if `serialized is not`None\`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `serialized` does not describe a well-formed topology. |
| `ValueError` | If `serialized` is `None` and `mesh_shape` is not a sequence of 4 positive integers. |
| `ValueError` | If `serialized` is `None` and `device_coordinates` is not a rank 3 numpy int32 array that describes a valid coordinate mapping. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `device_coordinates` | Describes the mapping from TPU devices to topology coordinates. |
| `mesh_rank` | Returns the number of dimensions in the mesh. |
| `mesh_shape` | A rank 1 int32 array describing the shape of the TPU topology. |
| `missing_devices` | Array of indices of missing devices. |
| `num_tasks` | Returns the number of TensorFlow tasks in the TPU slice. |
| `num_tpus_per_task` | Returns the number of TPU devices per task in the TPU slice. |

Methods
-------

### `cpu_device_name_at_coordinates`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/topology.py#L210-L213)

cpu_device_name_at_coordinates(
        device_coordinates, job=None
    )

Returns the CPU device attached to a logical core.

### `serialized`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/topology.py#L231-L241)

serialized()

Returns the serialized form of the topology.

### `task_ordinal_at_coordinates`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/topology.py#L184-L195)

task_ordinal_at_coordinates(
        device_coordinates
    )

Returns the TensorFlow task number attached to `device_coordinates`.

|     |     |
| --- | --- |
| Args |     |
| `device_coordinates` | An integer sequence describing a device's physical coordinates in the TPU fabric. |

|     |
| --- |
| Returns |     |
| Returns the TensorFlow task number that contains the TPU device with those physical coordinates. |     |

### `tpu_device_name_at_coordinates`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/topology.py#L215-L219)

tpu_device_name_at_coordinates(
        device_coordinates, job=None
    )

Returns the name of the TPU device assigned to a logical core.

### `tpu_device_ordinal_at_coordinates`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/topology.py#L197-L208)

tpu_device_ordinal_at_coordinates(
        device_coordinates
    )

Returns the TensorFlow device number at `device_coordinates`.

|     |     |
| --- | --- |
| Args |     |
| `device_coordinates` | An integer sequence describing a device's physical coordinates in the TPU fabric. |

|     |
| --- |
| Returns |     |
| Returns the TensorFlow device number within the task corresponding to attached to the device with those physical coordinates. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.