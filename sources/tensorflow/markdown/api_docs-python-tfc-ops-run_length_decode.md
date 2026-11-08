[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.run\_length\_decode Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode#returns)
    

Decodes `data` using run-length coding.

#### View aliases

**Main aliases**

[`tfc.run_length_decode`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode)

tfc.ops.run_length_decode(
        code,
        shape,
        run_length_code,
        magnitude_code,
        use_run_length_for_non_zeros,
        name=None
    )

This is the inverse operation to `RunLengthEncode`. The shape of the tensor that was encoded must be known by the caller.

This op implements a superset of RunLengthGammaDecode, which is equivalent to calling RunLengthDecode with run\_length\_code = -1, magnitude\_code = -1, and use\_run\_length\_for\_non\_zeros = false.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `code` | A `Tensor` of type `string`. An encoded scalar string as returned by `RunLengthEncode`. |
| `shape` | A `Tensor` of type `int32`. An int32 vector giving the shape of the encoded data. |
| `run_length_code` | An `int`. If >= 0, use Rice code with this parameter to decode run lengths, else use Elias gamma code. |
| `magnitude_code` | An `int`. If >= 0, use Rice code with this parameter to decode magnitudes, else use Elias gamma code. |
| `use_run_length_for_non_zeros` | A `bool`. If true, alternate between coding run lengths of zeros and non-zeros. If false, only decode run lengths of zeros, and decode non-zeros one by one. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `int32`. An int32 tensor of decoded values, with shape `shape`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.