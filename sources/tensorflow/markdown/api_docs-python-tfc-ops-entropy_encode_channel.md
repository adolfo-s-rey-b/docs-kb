[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.entropy\_encode\_channel Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel#returns)
    

Encodes each input in `value`.

#### View aliases

**Main aliases**

[`tfc.entropy_encode_channel`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel)

tfc.ops.entropy_encode_channel(
        handle, value, name=None
    )

In general, entropy encoders in `handle` reference multiple distributions. The last (innermost) dimension of `value` determines which distribution is used to encode `value`. For example, if `value` is a 3-D array, then `value(i,j,k)` is encoded using the `k`\-th distribution.

`handle` controls the number of coding streams. Suppose that `value` has the shape `[2, 3, 4]` and that `handle` has shape `[2]`. Then the first slice `[0, :, :]` of shape `[3, 4]` is encoded into `handle[0]` and the second slice `[1, :, :]` is encoded into `handle[1]`. If `handle` has shape `[]`, then there is only one handle, and the entire input is encoded into a single stream.

Values must be in the provided ranges specified when the input `handle` was originally created, unless overflow functionality was enabled. The `handle` may be produced by the `CreateRangeEncoder` op, or may be passed through from a different `EntropyEncodeChannel/EntropyEncodeIndex` op.

Because the op modifies `handle`, the corresponding input edge to the op nodes of this type should not have other consumers in the graph.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `handle` | A `Tensor` of type `variant`. |
| `value` | A `Tensor`. Must be one of the following types: `int32`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `variant`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.