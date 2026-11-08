[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#used-in-the-notebooks_1)
    
*   [Usage example](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#usage-example_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.reduce\_max Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#used-in-the-notebooks_1)
    
*   [Usage example](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#usage-example_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3045-L3092)

Computes [`tf.math.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
 of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_max`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max)

tf.math.reduce_max(
        input_tensor, axis=None, keepdims=False, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Working with sparse tensors](https://www.tensorflow.org/guide/sparse_tensor) | *   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Preprocess data with TensorFlow Transform](https://www.tensorflow.org/tfx/tutorials/transform/simple)<br>    <br>*   [Tutorial on Multi Armed Bandits in TF-Agents](https://www.tensorflow.org/agents/tutorials/bandits_tutorial)<br>    <br>*   [A Tutorial on Multi-Armed Bandits with Per-Arm Features](https://www.tensorflow.org/agents/tutorials/per_arm_bandits_tutorial) |

This is the reduction operation for the elementwise [`tf.math.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
 op.

Reduces `input_tensor` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each of the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single element is returned.

|     |
| --- |
| Usage example<br>------------- |     |
| >>> x = tf.constant([5, 1, 2, 4])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=int32, numpy=5><br>    >>> x = tf.constant([-5, -1, -2, -4])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=int32, numpy=-1><br>    >>> x = tf.constant([4, float('nan')])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=float32, numpy=nan><br>    >>> x = tf.constant([float('nan'), float('nan')])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=float32, numpy=nan><br>    >>> x = tf.constant([float('-inf'), float('inf')])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=float32, numpy=inf> |     |

See the numpy docs for `np.amax` and `np.nanmax` behavior.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_tensor` | The tensor to reduce. Should have real numeric type. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |\
| `keepdims` | If true, retains reduced dimensions with length 1. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| The reduced tensor. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-05 UTC.