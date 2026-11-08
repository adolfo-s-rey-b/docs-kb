[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#methods)
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#build)
        
    *   [coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#coordinates)
        
    *   [host\_device](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#host_device)
        
    *   [lookup\_replicas](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#lookup_replicas)
        
    *   [tpu\_device](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#tpu_device)
        
    *   [tpu\_ordinal](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#tpu_ordinal)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.DeviceAssignment Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#methods)
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#build)
        
    *   [coordinates](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#coordinates)
        
    *   [host\_device](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#host_device)
        
    *   [lookup\_replicas](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#lookup_replicas)
        
    *   [tpu\_device](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#tpu_device)
        
    *   [tpu\_ordinal](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#tpu_ordinal)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/device_assignment.py#L69-L201)

Mapping from logical cores in a computation to the physical TPU topology.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.DeviceAssignment`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment)

tf.tpu.experimental.DeviceAssignment(
        topology: tf.tpu.experimental.Topology,
        core_assignment: np.ndarray
    )

Prefer to use the [`DeviceAssignment.build()`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment#build)
 helper to construct a `DeviceAssignment`; it is easier if less flexible than constructing a `DeviceAssignment` directly.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `topology` | A `Topology` object that describes the physical TPU topology. |
| `core_assignment` | A logical to physical core mapping, represented as a rank 3 numpy array. See the description of the `core_assignment` property for more details. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `topology` is not `Topology` object. |
| `ValueError` | If `core_assignment` is not a rank 3 numpy array. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `core_assignment` | The logical to physical core mapping. |
| `num_cores_per_replica` | The number of cores per replica. |
| `num_replicas` | The number of replicas of the computation. |
| `topology` | A `Topology` that describes the TPU topology. |

Methods
-------

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/device_assignment.py#L186-L201)

@classmethod

### `coordinates`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/device_assignment.py#L141-L143)

coordinates(
        replica: int, logical_core: int
    ) -> Tuple

Returns the physical topology coordinates of a logical core.

### `host_device`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/device_assignment.py#L170-L176)

host_device(
        replica: int = 0, logical_core: int = 0, job: Optional[str] = None
    ) -> str

Returns the CPU device attached to a logical core.

### `lookup_replicas`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/device_assignment.py#L145-L163)

lookup_replicas(
        task_id: int, logical_core: int
    ) -> List[int]

Lookup replica ids by task number and logical core.

|     |     |
| --- | --- |
| Args |     |
| `task_id` | TensorFlow task number. |
| `logical_core` | An integer, identifying a logical core. |

|     |
| --- |
| Returns |     |
| A sorted list of the replicas that are attached to that task and logical\_core. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If no replica exists in the task which contains the logical core. |

### `tpu_device`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/device_assignment.py#L178-L184)

tpu_device(
        replica: int = 0, logical_core: int = 0, job: Optional[str] = None
    ) -> str

Returns the name of the TPU device assigned to a logical core.

### `tpu_ordinal`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/device_assignment.py#L165-L168)

tpu_ordinal(
        replica: int = 0, logical_core: int = 0
    ) -> int

Returns the ordinal of the TPU device assigned to a logical core.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.