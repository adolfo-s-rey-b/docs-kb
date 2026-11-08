[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.distributions.quantization\_offset Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/distributions/helpers.py#L104-L147)

Computes distribution-dependent quantization offset.

#### View aliases

**Main aliases**

[`tfc.quantization_offset`](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset)

tfc.distributions.quantization_offset(
        distribution
    )

For range coding of continuous random variables, the values need to be quantized first. Typically, it is beneficial for compression performance to align the centers of the quantization bins such that one of them coincides with the mode of the distribution. With `offset` being the mode of the distribution, for instance, this can be achieved simply by computing:

x_hat = tf.round(x - offset) + offset

This method tries to determine the offset in a best-effort fashion, based on which statistics the `Distribution` implements. First, a method `self._quantization_offset()` is tried. If that isn't defined, it tries in turn: `self.mode()`, `self.quantile(.5)`, then `self.mean()`. If none of these are implemented, it falls back on quantizing to integer values (i.e., an offset of zero).

Note the offset is always in the range \[-.5, .5\] as it is assumed to be combined with a round quantizer.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `distribution` | A [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)<br> object. |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> broadcastable to shape `self.batch_shape`, containing the determined quantization offsets. No gradients are allowed to flow through the return value. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.