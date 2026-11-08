[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.run\_length\_gamma\_encode Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode#returns)
    

Encodes `data` using run-length and Elias gamma coding.

#### View aliases

**Main aliases**

[`tfc.run_length_gamma_encode`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode)

tfc.ops.run_length_gamma_encode(
        data, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A `Tensor` of type `int32`. An int32 tensor of values to be encoded. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `string`. An encoded scalar string. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.