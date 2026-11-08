[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.convert\_image\_dtype Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2385-L2567)

Convert `image` to `dtype`, scaling its values if needed.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.convert_image_dtype`](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype)

tf.image.convert_image_dtype(
        image, dtype, saturate=False, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Pruning for on-device inference w/ XNNPACK](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_for_on_device_inference) | *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Load video data](https://www.tensorflow.org/tutorials/load_data/video)<br>    <br>*   [Transfer learning for video classification with MoViNet](https://www.tensorflow.org/tutorials/video/transfer_learning_with_movinet) |

The operation supports data types (for `image` and `dtype`) of `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`, `float16`, `float32`, `float64`, `bfloat16`.

Images that are represented using floating point values are expected to have values in the range \[0,1). Image data stored in integer data types are expected to have values in the range `[0,MAX]`, where `MAX` is the largest positive representable number for the data type.\
\
This op converts between data types, scaling the values appropriately before casting.\
\
#### Usage Example:\
\
    x = [[[1, 2, 3], [4, 5, 6]],\
\
Converting integer types to floating point types returns normalized floating point values in the range \[0, 1); the values are normalized by the `MAX` value of the input dtype. Consider the following two examples:\
\
    a = [[[1], [2]], [[3], [4]]]\
\
    a_int32 = tf.convert_to_tensor(a, dtype=tf.int32)\
\
Despite having identical values of `a` and output dtype of `float32`, the outputs differ due to the different input dtypes (`int8` vs. `int32`). This is, again, because the values are normalized by the `MAX` value of the input dtype.\
\
Note that converting floating point values to integer type may lose precision. In the example below, an image tensor `b` of dtype `float32` is converted to `int8` and back to `float32`. The final output, however, is different from the original input `b` due to precision loss.\
\
    b = [[[0.12], [0.34]], [[0.56], [0.78]]]\
\
Scaling up from an integer type (input dtype) to another integer type (output dtype) will not map input dtype's `MAX` to output dtype's `MAX` but converting back and forth should result in no change. For example, as shown below, the `MAX` value of int8 (=127) is not mapped to the `MAX` value of int16 (=32,767) but, when scaled back, we get the same, original values of `c`.\
\
    c = [[[1], [2]], [[127], [127]]]\
\
Scaling down from an integer type to another integer type can be a lossy conversion. Notice in the example below that converting `int16` to `uint8` and back to `int16` has lost precision.\
\
    d = [[[1000], [2000]], [[3000], [4000]]]\
\
Note that converting from floating point inputs to integer types may lead to over/underflow problems. Set saturate to `True` to avoid such problem in problematic conversions. If enabled, saturation will clip the output into the allowed range before performing a potentially dangerous cast (and only before performing such a cast, i.e., when casting from a floating point to an integer type, and when casting from a signed to an unsigned type; `saturate` has no effect on casts between floats, or on casts that increase the type's range).\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | An image. |\
| `dtype` | A `DType` to convert `image` to. |\
| `saturate` | If `True`, clip the input before casting (if necessary). |\
| `name` | A name for this operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| `image`, converted to `dtype`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `AttributeError` | Raises an attribute error when dtype is neither float nor integer. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.