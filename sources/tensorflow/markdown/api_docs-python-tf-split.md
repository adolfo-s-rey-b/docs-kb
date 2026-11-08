[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/split)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/split?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/split#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/split#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/split#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.split Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/split#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/split#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/split#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1744-L1823)

Splits a tensor `value` into a list of sub tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.split`](https://www.tensorflow.org/api_docs/python/tf/split)

tf.split(
        value, num_or_size_splits, axis=0, num=None, name='split'
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding) | *   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)<br>    <br>*   [MoViNet for streaming action recognition](https://www.tensorflow.org/hub/tutorials/movinet)<br>    <br>*   [Bayesian Modeling with Joint Distribution](https://www.tensorflow.org/probability/examples/Modeling_with_JointDistribution) |

See also [`tf.unstack`](https://www.tensorflow.org/api_docs/python/tf/unstack)
.

If `num_or_size_splits` is an `int`, then it splits `value` along the dimension `axis` into `num_or_size_splits` smaller tensors. This requires that `value.shape[axis]` is divisible by `num_or_size_splits`.

If `num_or_size_splits` is a 1-D Tensor (or list), then `value` is split into `len(num_or_size_splits)` elements. The shape of the `i`\-th element has the same size as the `value` except along dimension `axis` where the size is `num_or_size_splits[i]`.

#### For example:

    x = tf.Variable(tf.random.uniform([5, 30], -1, 1))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | The `Tensor` to split. |
| `num_or_size_splits` | Either an `int` indicating the number of splits along `axis` or a 1-D integer `Tensor` or Python list containing the sizes of each output tensor along `axis`. If an `int`, then it must evenly divide `value.shape[axis]`; otherwise the sum of sizes along the split axis must match that of the `value`. |
| `axis` | An `int` or scalar `int32` `Tensor`. The dimension along which to split. Must be in the range `[-rank(value), rank(value))`. Defaults to 0. |\
| `num` | Optional, an `int`, used to specify the number of outputs when it cannot be inferred from the shape of `size_splits`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| if `num_or_size_splits` is an `int` returns a list of `num_or_size_splits` `Tensor` objects; if `num_or_size_splits` is a 1-D list or 1-D `Tensor` returns `num_or_size_splits.get_shape[0]` `Tensor` objects resulting from splitting `value`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `num` is unspecified and cannot be inferred. |\
| `ValueError` | If `num_or_size_splits` is a scalar `Tensor`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.