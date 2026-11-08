[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ensure_shape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ensure_shape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ensure_shape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ensure_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ensure_shape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ensure_shape#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ensure\_shape Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ensure_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ensure_shape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ensure_shape#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L2226-L2367)

Updates the shape of a tensor and checks at runtime that the shape holds.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ensure_shape`](https://www.tensorflow.org/api_docs/python/tf/ensure_shape)

tf.ensure_shape(
        x, shape, name=None
    )

When executed, this operation asserts that the input tensor `x`'s shape is compatible with the `shape` argument. See [`tf.TensorShape.is_compatible_with`](https://www.tensorflow.org/api_docs/python/tf/TensorShape#is_compatible_with)
 for details.

    x = tf.constant([[1, 2, 3],\
\
Use `None` for unknown dimensions:\
\
    x = tf.ensure_shape(x, [None, 3])\
\
If the tensor's shape is not compatible with the `shape` argument, an error is raised:\
\
    x = tf.ensure_shape(x, [5])\
\
During graph construction (typically tracing a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)\
), [`tf.ensure_shape`](https://www.tensorflow.org/api_docs/python/tf/ensure_shape)\
 updates the static-shape of the **result** tensor by merging the two shapes. See [`tf.TensorShape.merge_with`](https://www.tensorflow.org/api_docs/python/tf/TensorShape#merge_with)\
 for details.\
\
This is most useful when **you** know a shape that can't be determined statically by TensorFlow.\
\
The following trivial [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)\
 prints the input tensor's static-shape before and after `ensure_shape` is applied.\
\
    @tf.function\
\
This lets you see the effect of [`tf.ensure_shape`](https://www.tensorflow.org/api_docs/python/tf/ensure_shape)\
 when the function is traced:\
\
>>> cf = f.get_concrete_function(tf.TensorSpec([None, None]))\
    Static-shape before: (None, None)\
    Static-shape after: (None, 3)\
\
    cf(tf.zeros([3, 3])) # Passes\
\
The above example raises [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)\
, because `x`'s shape, `(3,)`, is not compatible with the `shape` argument, `(None, 3)`\
\
Inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)\
 or [`v1.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)\
 context it checks both the buildtime and runtime shapes. This is stricter than [`tf.Tensor.set_shape`](https://www.tensorflow.org/api_docs/python/tf/Tensor#set_shape)\
 which only checks the buildtime shape.\
\
For example, of loading images of a known size:\
\
    @tf.function\
\
When tracing a function, no ops are being executed, shapes may be unknown. See the [Concrete Functions Guide](https://www.tensorflow.org/guide/concrete_function)\
 for details.\
\
    concrete_decode = decode_image.get_concrete_function(\
\
    image = tf.random.uniform(maxval=255, shape=[28, 28, 3], dtype=tf.int32)\
\
    image = tf.concat([image,image], axis=0)\
\
    @tf.function\
\
    image = bad_decode_image(png)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `x` | A `Tensor`. |\
| `shape` | A `TensorShape` representing the shape of this tensor, a `TensorShapeProto`, a list, a tuple, or None. |\
| `name` | A name for this operation (optional). Defaults to "EnsureShape". |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type and contents as `x`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError) | If `shape` is incompatible with the shape of `x`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.