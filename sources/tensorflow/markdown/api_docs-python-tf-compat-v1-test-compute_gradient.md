[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.test.compute\_gradient Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/gradient_checker.py#L270-L334)

Computes and returns the theoretical and numerical Jacobian. (deprecated)

tf.compat.v1.test.compute_gradient(
        x,
        x_shape,
        y,
        y_shape,
        x_init_value=None,
        delta=0.001,
        init_targets=None,
        extra_feed_dict=None
    )

If `x` or `y` is complex, the Jacobian will still be real but the corresponding Jacobian dimension(s) will be twice as large. This is required even if both input and output is complex since TensorFlow graphs are not necessarily holomorphic, and may have gradients not expressible as complex numbers. For example, if `x` is complex with shape `[m]` and `y` is complex with shape `[n]`, each Jacobian `J` will have shape `[m * 2, n * 2]` with

J[:m, :n] = d(Re y)/d(Re x)
    J[:m, n:] = d(Im y)/d(Re x)
    J[m:, :n] = d(Re y)/d(Im x)
    J[m:, n:] = d(Im y)/d(Im x)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | a tensor or list of tensors |
| `x_shape` | the dimensions of x as a tuple or an array of ints. If x is a list, then this is the list of shapes. |
| `y` | a tensor |
| `y_shape` | the dimensions of y as a tuple or an array of ints. |
| `x_init_value` | (optional) a numpy array of the same shape as "x" representing the initial value of x. If x is a list, this should be a list of numpy arrays. If this is none, the function will pick a random tensor as the initial value. |
| `delta` | (optional) the amount of perturbation. |
| `init_targets` | list of targets to run to initialize model params. |
| `extra_feed_dict` | dict that allows fixing specified tensor values during the Jacobian calculation. |

|     |
| --- |
| Returns<br>------- |     |
| Two 2-d numpy arrays representing the theoretical and numerical Jacobian for dy/dx. Each has "x\_size" rows and "y\_size" columns where "x\_size" is the number of elements in x and "y\_size" is the number of elements in y. If x is a list, returns a list of two numpy arrays. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.