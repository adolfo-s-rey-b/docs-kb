[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfc%2Fops%2Fpmf_to_quantized_cdf&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.pmf\_to\_quantized\_cdf Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf#returns)
    

Converts a PMF into a quantized CDF for range coding.

#### View aliases

**Main aliases**

[`tfc.pmf_to_quantized_cdf`](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf)

tfc.ops.pmf_to_quantized_cdf(
        pmf, precision, name=None
    )

This op uses floating-point operations internally. Therefore the quantized output may not be consistent across multiple platforms. For entropy encoders and decoders to have the same quantized CDF on different platforms, the quantized CDF should be produced once and saved, then the saved quantized CDF should be used everywhere.

After quantization, if PMF does not sum to 2^precision, then some values of PMF are increased or decreased to adjust the sum to equal to 2^precision.

Note that the input PMF is pre-quantization. The input PMF is not normalized by this op prior to quantization. Therefore the user is responsible for normalizing PMF if necessary.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pmf` | A `Tensor` of type `float32`. |
| `precision` | An `int` that is `>= 1`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `int32`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.