[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/recompute_grad#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/recompute_grad)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/recompute_grad?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/recompute_grad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/recompute_grad#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.recompute\_grad Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/recompute_grad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/recompute_grad#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/custom_gradient.py#L600-L770)

Defines a function as a recompute-checkpoint for the tape auto-diff.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.recompute_grad`](https://www.tensorflow.org/api_docs/python/tf/recompute_grad)

tf.recompute_grad(
        f
    )

Tape checkpointing is a technique to reduce the memory consumption of the auto-diff tape:

*   Without tape checkpointing operations and intermediate values are recorded to the tape for use in the backward pass.
    
*   With tape checkpointing, only the function call and its inputs are recorded. During back-propagation the `recompute_grad` custom gradient ([`tf.custom_gradient`](https://www.tensorflow.org/api_docs/python/tf/custom_gradient)
    ) recomputes the function under a localized Tape object. This recomputation of the function during backpropagation performs redundant calculation, but reduces the overall memory usage of the Tape.
    

    y = tf.Variable(1.0)

    def my_function(x):

    my_function_recompute = tf.recompute_grad(my_function)

    with tf.GradientTape() as tape:

    grad = tape.gradient(r, [y])

Without `recompute_grad`, the tape contains all intermitate steps, and no recomputation is performed.

    with tf.GradientTape() as tape:

    grad = tape.gradient(r, [y])

If `f` was a [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
 `Model` or `Layer` object, methods and attributes such as `f.variables` are not available on the returned function `g`. Either keep a reference of `f` , or use `g.__wrapped__` for accessing these variables and methods.

    def print_running_and_return(x):

    model = tf.keras.Sequential([\
\
    model_recompute = tf.recompute_grad(model)\
\
    with tf.GradientTape(persistent=True) as tape:\
\
    grad = tape.gradient(r, model.variables)\
\
Alternatively, use the `__wrapped__` attribute to access the original model object.\
\
    grad = tape.gradient(r, model_recompute.__wrapped__.variables)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `f` | function `f(*x)` that returns a `Tensor` or sequence of `Tensor` outputs. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A function `g` wrapping `f` that defines a custom gradient, which recomputes `f` on the backwards pass of a gradient call. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.