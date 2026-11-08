[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#returns_1)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#numpy-compatibility_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.reduce\_min Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#returns_1)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min?version=stable#numpy-compatibility_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2917-L2978)

Computes the [`tf.math.minimum`](https://www.tensorflow.org/api_docs/python/tf/math/minimum)
 of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_min`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min)

tf.math.reduce_min(
        input_tensor, axis=None, keepdims=False, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [Generating Images with BigBiGAN](https://www.tensorflow.org/hub/tutorials/bigbigan_with_tf_hub)<br>    <br>*   [MoViNet for streaming action recognition](https://www.tensorflow.org/hub/tutorials/movinet)<br>    <br>*   [TensorFlow Ranking Keras pipeline for distributed training](https://www.tensorflow.org/ranking/tutorials/ranking_dnn_distributed) |

This is the reduction operation for the elementwise [`tf.math.minimum`](https://www.tensorflow.org/api_docs/python/tf/math/minimum)
 op.

Reduces `input_tensor` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each of the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single element is returned.

#### For example:

    a = tf.constant([\
\
Choosing a specific axis returns minimum element in the given axis:\
\
    b = tf.constant([[1, 2, 3], [4, 5, 6]])\
\
Setting `keepdims` to `True` retains the dimension of `input_tensor`:\
\
    tf.reduce_min(a, keepdims=True)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `input_tensor` | The tensor to reduce. Should have real numeric type. |\
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |\
| `keepdims` | If true, retains reduced dimensions with length 1. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| The reduced tensor. |     |\
\
numpy compatibility\
-------------------\
\
Equivalent to np.min\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.