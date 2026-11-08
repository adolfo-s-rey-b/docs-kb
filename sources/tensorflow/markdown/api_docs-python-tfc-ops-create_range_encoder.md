[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfc%2Fops%2Fcreate_range_encoder&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.create\_range\_encoder Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder#returns)
    

Creates range encoder objects to be used by `EntropyEncode*` ops.

#### View aliases

**Main aliases**

[`tfc.create_range_encoder`](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder)

tfc.ops.create_range_encoder(
        shape, lookup, name=None
    )

The output `handle` has the shape specified by the input `shape`. Each element in `handle` is an independent range encoder object, and `EntropyEncode*` processes as many concurrent code streams as contained in `handle`.

This op expects `lookup` to be either a concatenation (1-D) or stack (2-D) of CDFs, where each CDF is preceded by a corresponding precision value. In case of a stack:

   lookup[..., 0] = precision in [1, 16],
       lookup[..., 1] / 2^precision = Pr(X < 0) = 0,
       lookup[..., 2] / 2^precision = Pr(X < 1),
       lookup[..., 3] / 2^precision = Pr(X < 2),
       ...
       lookup[..., -1] / 2^precision = 1,

Subsequent values in each CDF may be equal, indicating a symbol with zero probability. Attempting to encode such a symbol will result in undefined behavior. However, any number of trailing zero-probability symbols will be interpreted as padding, and attempting to use those will result in an encoding error (unless overflow functionality is used).

Overflow functionality can be enabled by negating the precision value in `lookup`. In that case, the last non-zero probability symbol in the CDF is used as an escape code, allowing negative integers and integers greater or equal to the last non-zero probability symbol to be encoded using an Elias gamma code, which is interleaved into the code stream. Attempting to encode a zero-probability symbol within the valid range still causes undefined behavior.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A `Tensor` of type `int32`. |
| `lookup` | A `Tensor` of type `int32`. |
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