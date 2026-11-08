[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient_error#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient_error)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient_error?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient_error#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient_error#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.test.compute\_gradient\_error Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient_error#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/compute_gradient_error#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/gradient_checker.py#L347-L394)

Computes the gradient error. (deprecated)

tf.compat.v1.test.compute_gradient_error(
        x,
        x_shape,
        y,
        y_shape,
        x_init_value=None,
        delta=0.001,
        init_targets=None,
        extra_feed_dict=None
    )

Computes the maximum error for dy/dx between the computed Jacobian and the numerically estimated Jacobian.

This function will modify the tensors passed in as it adds more operations and hence changing the consumers of the operations of the input tensors.

This function adds operations to the current session. To compute the error using a particular device, such as a GPU, use the standard methods for setting a device (e.g. using with sess.graph.device() or setting a device function in the session constructor).

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
| The maximum error in between the two Jacobians. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.