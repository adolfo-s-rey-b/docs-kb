[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_tpu_mesh#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_tpu_mesh)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_tpu_mesh?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_tpu_mesh#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.create\_tpu\_mesh Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_tpu_mesh#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/tpu_util.py#L585-L735)

Returns a distributed TPU mesh optimized for AllReduce ring reductions.

tf.experimental.dtensor.create_tpu_mesh(
        mesh_dim_names: List[str],
        mesh_shape: List[int],
        mesh_name: str,
        ring_dims: Optional[int] = None,
        ring_axes: Optional[List[str]] = None,
        ring_bounds: Optional[List[int]] = None,
        can_split_host_across_rings: bool = True,
        build_ring_across_rings: bool = False,
        rotate_ring_across_rings: bool = False,
        use_xla_spmd: bool = layout_lib.USE_XLA_SPMD
    ) -> tf.experimental.dtensor.Mesh

Only as many as leading axes specified by `ring_axes` as necessary will be used to build rings, as long as the subslice formed by these axes have enough cores to contain a ring of the required size. The leftover axes in `ring_axes` won't affect results.

This function always uses all TPU devices, and offers more customization than [`tf.experimental.dtensor.create_distributed_mesh`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mesh_dim_names` | List of mesh dimension names. |
| `mesh_shape` | Shape of the mesh. |
| `mesh_name` | A unique name for the mesh. If empty, internally generate one. |
| `ring_dims` | Optional; The number of leading (ring\_dims > 0) or trailing (ring\_dims < 0) mesh dimensions to build rings for. If unspecified, build rings for all but the first dimension. |
| `ring_axes` | Optional; A permutation of \["x", "y", "z", "core"\], specifying the order of TPU topology axes to build rings in. If unspecified, default to \["core", "x", "y", "z"\]. |
| `ring_bounds` | Optional; The maximum number of devices on each axis, in the x, y, z, core order. If unspecified, default to physical topology limits. |
| `can_split_host_across_rings` | Optional; If true, devices attached to the same host (i.e., DTensor client) may get assigned to different rings. Setting it to false may cause some combinations of arguments to be infeasible; see DeviceAssignmentTest.testCreateMesh\[No\]SplittingHosts\* for examples. |
| `build_ring_across_rings` | Optional; If true, also build a data-parallel ring across model-parallel rings. This ring could be strided. |
| `rotate_ring_across_rings` | Optional; If true, build the data-parallel ring in column-major instead of row-major order. |
| `use_xla_spmd` | Boolean when True, will use XLA SPMD instead of DTensor SPMD. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.