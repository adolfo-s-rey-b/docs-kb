[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfc%2Fops%2Fsame_padding_for_kernel&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.same\_padding\_for\_kernel Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/ops/padding_ops.py#L22-L51)

Determine correct amount of padding for `same` convolution.

#### View aliases

**Main aliases**

[`tfc.same_padding_for_kernel`](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel)

tfc.ops.same_padding_for_kernel(
        shape, corr, strides_up=None
    )

To implement `'same'` convolutions, we first pad the image, and then perform a `'valid'` convolution or correlation. Given the kernel shape, this function determines the correct amount of padding so that the output of the convolution or correlation is the same size as the pre-padded input.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | Shape of the convolution kernel (without the channel dimensions). |
| `corr` | Boolean. If `True`, assume cross correlation, if `False`, convolution. |
| `strides_up` | If this is used for an upsampled convolution, specify the strides here. (For downsampled convolutions, specify `(1, 1)`: in that case, the strides don't matter.) |

|     |
| --- |
| Returns<br>------- |     |
| The amount of padding at the beginning and end for each dimension. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.