[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.entropy\_decode\_channel Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel#returns)
    

Decodes the encoded stream inside `handle`.

#### View aliases

**Main aliases**

[`tfc.entropy_decode_channel`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel)

tfc.ops.entropy_decode_channel(
        handle, shape, Tdecoded, name=None
    )

The output shape is defined as `handle.shape + MakeShape(shape)`, and therefore both `handle` and `shape` arguments determine how many symbols are decoded.

Like encoders, decoders in `handle` reference multiple distributions. The last (innermost) dimension of `value` determines which distribution is used to decode each value in the output. For example, if `decoded` is a 3-D array, then `output(i,j,k)` is decoded using the `k`\-th distribution.

`handle` controls the number of coding streams. Suppose that `index` has the shape `[2, 3, 4]` and that `handle` has shape `[2]`. Then the first output slice `[0, :, :]` of shape `[3, 4]` is decoded from `handle[0]` and the second output slice `[1, :, :]` is decoded from `handle[1]`. If `handle` has shape `[]`, then there is only one handle, and the entire output is decoded from a single stream.

The input handle may be produced by the `CreateRangeDecoder` op, or may be passed through from a different `EntropyDecode*` op.

This op modifies the input `handle`. The handle input edge to the op nodes of this type should not have other consumers in the graph.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `handle` | A `Tensor` of type `variant`. |
| `shape` | A `Tensor` of type `int32`. |
| `Tdecoded` | A [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (aliased\_handle, decoded). |     |
| `aliased_handle` | A `Tensor` of type `variant`. |
| `decoded` | A `Tensor` of type `Tdecoded`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.