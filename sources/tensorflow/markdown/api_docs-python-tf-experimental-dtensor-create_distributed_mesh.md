[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.create\_distributed\_mesh Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/mesh_util.py#L138-L237)

Creates a distributed mesh.

tf.experimental.dtensor.create_distributed_mesh(
        mesh_dims: Union[List[Tuple[str, int]], Dict[str, int]],
        mesh_name: str = '',
        local_devices: Optional[List[Union[tf_device.DeviceSpec, str]]] = None,
        device_type: Optional[str] = None,
        use_xla_spmd: bool = layout.USE_XLA_SPMD
    ) -> tf.experimental.dtensor.Mesh

This is similar to `create_mesh`, but with a different set of arguments to create a mesh that spans evenly across a multi-client DTensor cluster.

For CPU and GPU meshes, users can choose to use fewer local devices than what is available `local_devices`.

For TPU, only meshes that uses all TPU cores is supported by the DTensor runtime.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mesh_dims` | A dict of dim\_name: dim\_size, or a list of (dim\_name, dim\_size) tuples. e.g. `{'x' : 4, 'y' : 1}` or `[('x', 4), ('y', 1)]`. |
| `mesh_name` | Name of the created mesh. Defaults to ''. |
| `local_devices` | String representations of devices to use. This is the device part of tf.DeviceSpec, e.g. 'CPU:0'. Defaults to all available local logical devices. |
| `device_type` | Type of device to build the mesh for. Defaults to 'CPU'. Supported values are 'CPU', 'GPU', 'TPU'.6 |
| `use_xla_spmd` | Boolean when True, will use XLA SPMD instead of DTensor SPMD. |

|     |
| --- |
| Returns<br>------- |     |
| A mesh that spans evenly across all DTensor clients in the cluster. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.