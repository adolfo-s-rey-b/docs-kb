[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.QuantizationConfig Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L1254-L1315)

Settings for simulated quantization of the tpu embedding table.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.QuantizationConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig)

tf.tpu.experimental.embedding.QuantizationConfig(
        num_buckets: int, lower: float, upper: float
    )

When simulated quantization is enabled, the results of the embedding lookup are clipped and quantized according to the settings here before the combiner is applied.

For example, to quantize `input` the following is done:

if input < lower
      input = lower
    if input > upper
      input = upper
    quantum = (upper - lower) / (num_buckets - 1)
    input = math.floor((input - lower) / quantum + 0.5) * quantum + lower

See tensorflow/core/protobuf/tpu/optimization\_parameters.proto for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_buckets` | The number of quantization buckets, must be atleast 2. |
| `lower` | The lower bound for the quantization range. |
| `upper` | The upper bound for the quantization range. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `num_buckets` is less than 2. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.