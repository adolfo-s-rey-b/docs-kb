[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.distributions.upper\_tail Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/distributions/helpers.py#L186-L219)

Approximates upper tail quantile for range coding.

#### View aliases

**Main aliases**

[`tfc.upper_tail`](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail)

tfc.distributions.upper_tail(
        distribution, tail_mass
    )

For range coding of random variables, the distribution tails need special handling, because range coding can only handle alphabets with a finite number of symbols. This method returns a cut-off location for the upper tail, such that approximately `tail_mass` probability mass is contained in the tails (together). The tails are then handled by using the 'overflow' functionality of the range coder implementation (using an Elias gamma code).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `distribution` | A [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)<br> object. |
| `tail_mass` | Float between 0 and 1. Desired probability mass for the tails. |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> broadcastable to shape `self.batch_shape` containing the approximate upper tail quantiles for each scalar distribution. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.