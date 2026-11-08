[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.create\_mesh Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/mesh_util.py#L70-L135)

Creates a single-client mesh.

tf.experimental.dtensor.create_mesh(
        mesh_dims: Optional[Union[List[Tuple[str, int]], Dict[str, int]]] = None,
        mesh_name: str = '',
        devices: Optional[List[Union[tf_device.DeviceSpec, str]]] = None,
        device_type: Optional[str] = None,
        use_xla_spmd: bool = layout.USE_XLA_SPMD
    ) -> tf.experimental.dtensor.Mesh

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution) | *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial) |

If both `mesh_dims` and `devices` are specified, they must match each otehr. As a special case, when all arguments are missing, this creates a 1D CPU mesh with an empty name, assigning all available devices to that dimension.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mesh_dims` | A dict of dim\_name: dim\_size, or a list of (dim\_name, dim\_size) tuples. Defaults to a single batch-parallel dimension called 'x' usin all devices. As a special case, a single-element mesh\_dims whose dim\_size is -1 also uses all devices. e.g. `{'x' : 4, 'y' : 1}` or `[('x', 4), ('y', 1)]`. |
| `mesh_name` | Name of the created mesh. Defaults to ''. |
| `devices` | String representations of devices to use. This is the device part of tf.DeviceSpec, e.g. 'CPU:0'. Defaults to all available logical devices. |
| `device_type` | If `devices` is missing, the type of devices to use. Defaults to 'CPU'. |
| `use_xla_spmd` | Boolean when True, will use XLA SPMD instead of DTensor SPMD. |

|     |
| --- |
| Returns<br>------- |     |
| A single-client mesh created from specified or default arguments. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.