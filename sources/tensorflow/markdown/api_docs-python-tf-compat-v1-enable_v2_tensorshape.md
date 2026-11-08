[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_tensorshape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_tensorshape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_tensorshape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.enable\_v2\_tensorshape Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L38-L88)

In TensorFlow 2.0, iterating over a TensorShape instance returns values.

tf.compat.v1.enable_v2_tensorshape()

This enables the new behavior.

Concretely, `tensor_shape[i]` returned a Dimension instance in V1, but it V2 it returns either an integer, or None.

#### Examples:

#######################
    # If you had this in V1:
    value = tensor_shape[i].value
    
    # Do this in V2 instead:
    value = tensor_shape[i]
    
    #######################
    # If you had this in V1:
    for dim in tensor_shape:
      value = dim.value
      print(value)
    
    # Do this in V2 instead:
    for value in tensor_shape:
      print(value)
    
    #######################
    # If you had this in V1:
    dim = tensor_shape[i]
    dim.assert_is_compatible_with(other_shape)  # or using any other shape method
    
    # Do this in V2 instead:
    if tensor_shape.rank is None:
      dim = Dimension(None)
    else:
      dim = tensor_shape.dims[i]
    dim.assert_is_compatible_with(other_shape)  # or using any other shape method
    
    # The V2 suggestion above is more explicit, which will save you from
    # the following trap (present in V1):
    # you might do in-place modifications to `dim` and expect them to be reflected
    # in `tensor_shape[i]`, but they would not be.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.