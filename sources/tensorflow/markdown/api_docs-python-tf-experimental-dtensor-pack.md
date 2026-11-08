[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fdtensor%2Fpack&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.pack Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/api.py#L191-L339)

Packs [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 components into a DTensor.

tf.experimental.dtensor.pack(
        tensors: Sequence[Any],
        layout: tf.experimental.dtensor.Layout
    ) -> Any

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview) | *   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial) |

Packing and unpacking are inverse operations:

* unpack(pack(tensors)) == tensors
    * pack(unpack(dtensor)) == dtensor

1.  For any DTensor on the mesh, `unpack` returns the raw components placed on each underlying device.
2.  Packing these raw components in the same order using `pack` returns a DTensor which should be identical to the original DTensor--both the content value and the layout.

**Shape, Rank, and Scalars**: The rank of the DTensor is the same as the rank of its raw components, i.e., rank is preserved. This leads to a consistent interpretation for packing scalar values into a DTensor. The only valid layout for a scalar value is fully replicated, and the individual components must be identical scalars.

Each input `tensors[i]` will be copied to `layout.mesh.local_device[i]` if not already on the local device. Non-local components should not be passed to `pack`; use `copy_to_mesh` and `relayout` to place tensors on all global devices on a mesh.

It is the caller's responsibility to ensure that the underlying values for `pack` adhere to the specified layout, and that only as many values are specified as there are local devices. Pack does not move data between clients. See examples below for more detail about layouts.

For example, assume we have a mesh `[X(2), Y(3)]`, which has in total 6 underlying devices. Futuremore, assume that the device location mapping is the following:

device_ID  |  location X, Y
            0     0, 0
            1     0, 1
            2     0, 2
            3     1, 0
            4     1, 1
            5     1, 2

1.  For 1-D vector DTensor with shape `[128]` with layout `[mesh.X]` and value as `range(128)`, the raw components will have shape `[64]` each, and the raw components will be:
    
    device_ID  |  raw component
                0     range(0, 64)
                1     range(0, 64)
                2     range(0, 64)
                3     range(64, 128)
                4     range(64, 128)
                5     range(64, 128)
    
    This also means for a 1-D DTensor with shape `[2]` and layout `[mesh.X]`, the raw components have shape `[1]` rather than the shape for scalar values `[]`.
    
2.  For 2-D vector DTensor with shape `[2, 3]` with layout `[mesh.X, mesh.Y]` and value as `range(6)`, this is basically a fully-sharded DTensor.
    
    From global view, the content looks like
    
    [\
          [0.0, 1.0, 2.0],\
          [3.0, 4.0, 5.0],\
        ]
    
    The raw components will have shape `[1, 1]` each, and have the following content:
    
    device_ID  |  raw component
                0     [[0.0]]
                1     [[1.0]]
                2     [[2.0]]
                3     [[3.0]]
                4     [[4.0]]
                5     [[5.0]]
    
3.  For a scalar value `123.0` DTensor, it can only have one legitimate layout `[]` (no dimension, but fully replicated).
    
    The raw components will have shape `[]` each, and have the following content:
    
    device_ID  |  raw component
                0     123.0
                1     123.0
                2     123.0
                3     123.0
                4     123.0
                5     123.0
    
    Again, caller of `pack` is expected to provide 6 identical value raw components with scalar shapes.
    
4.  For 3-D vector DTensor with shape `[2, 2, 3]` with layout `[X, unsharded, unsharded]` and value as `range(12)`,
    
    From global view, the content looks like:
    
    [\
          [\
            [0.0, 1.0, 2.0],\
            [3.0, 4.0, 5.0],\
          ],\
          [\
            [6.0, 7.0, 8.0],\
            [9.0, 10., 11.],\
          ],\
        ]
    
    The raw components will have shape `[1, 2, 3]` each, and have the following content:
    
    device_ID  |  raw component
                0     range(6).reshape([1, 2, 3])
                1     range(6).reshape([1, 2, 3])
                2     range(6).reshape([1, 2, 3])
                3     range(6, 12).reshape([1, 2, 3])
                4     range(6, 12).reshape([1, 2, 3])
                5     range(6, 12).reshape([1, 2, 3])
    

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensors` | The list of local tensor components to pack into a DTensor. |
| `layout` | The layout of the DTensor to be created. |

|     |
| --- |
| Returns<br>------- |     |
| A DTensor created from the individual component tensors. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | When `pack` is not called eagerly. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.