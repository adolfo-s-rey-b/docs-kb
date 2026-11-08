[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.compute\_gradient Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/gradient_checker_v2.py#L296-L345)

Computes the theoretical and numeric Jacobian of `f`.

tf.test.compute_gradient(
        f, x, delta=None
    )

With y = f(x), computes the theoretical and numeric Jacobian dy/dx.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `f` | the function. |
| `x` | the arguments for the function as a list or tuple of values convertible to a Tensor. |
| `delta` | (optional) perturbation used to compute numeric Jacobian. |

|     |
| --- |
| Returns<br>------- |     |
| A pair of lists, where the first is a list of 2-d numpy arrays representing the theoretical Jacobians for each argument, and the second list is the numerical ones. Each 2-d array has "y\_size" rows and "x\_size" columns where "x\_size" is the number of elements in the corresponding argument and "y\_size" is the number of elements in f(x). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If result is empty but the gradient is nonzero. |
| `ValueError` | If x is not list, but any other type. |

#### Example:

    @tf.function

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.