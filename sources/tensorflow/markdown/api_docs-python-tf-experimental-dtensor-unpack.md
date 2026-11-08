[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/unpack#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.unpack Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/api.py#L342-L372)

Unpacks a DTensor into [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 components.

tf.experimental.dtensor.unpack(
        tensor: Any
    ) -> Sequence[Any]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview) |

Packing and unpacking are inverse operations:

* unpack(pack(tensors)) == tensors
    * pack(unpack(dtensor)) == dtensor

1.  For any DTensor on the mesh, `unpack` returns the raw components placed on each underlying device.
2.  Packing these raw components in the same order using `pack` returns a DTensor which should be identical to the original DTensor--both the content value and the layout.

See the documentation for `pack` for more information about how packing and unpacking works.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | The DTensor to unpack. |

|     |
| --- |
| Returns<br>------- |     |
| The individual component tensors of the DTensor. This will include only the client-local components, i.e. the components placed on the local devices. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | When `unpack` is not called eagerly. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.