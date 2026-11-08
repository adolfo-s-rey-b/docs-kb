[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/fill#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/fill)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/fill?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/fill#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/fill#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/fill#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/fill#raises)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/fill#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.fill Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/fill#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/fill#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/fill#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/fill#raises)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/fill#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L204-L250)

Creates a tensor filled with a scalar value.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)

tf.fill(
        dims, value, name=None, layout=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Subword tokenizers](https://www.tensorflow.org/text/guide/subwords_tokenizer)<br>    <br>*   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) | *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Multiple changepoint detection and Bayesian model selection](https://www.tensorflow.org/probability/examples/Multiple_changepoint_detection_and_Bayesian_model_selection)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb)<br>    <br>*   [Bayesian Gaussian Mixture Model and Hamiltonian MCMC](https://www.tensorflow.org/probability/examples/Bayesian_Gaussian_Mixture_Model) |

See also [`tf.ones`](https://www.tensorflow.org/api_docs/python/tf/ones)
, [`tf.zeros`](https://www.tensorflow.org/api_docs/python/tf/zeros)
, [`tf.one_hot`](https://www.tensorflow.org/api_docs/python/tf/one_hot)
, [`tf.eye`](https://www.tensorflow.org/api_docs/python/tf/eye)
.

This operation creates a tensor of shape `dims` and fills it with `value`.

#### For example:

    tf.fill([2, 3], 9)

[`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
 evaluates at graph runtime and supports dynamic shapes based on other runtime `tf.Tensors`, unlike [`tf.constant(value, shape=dims)`](https://www.tensorflow.org/api_docs/python/tf/constant)
, which embeds the value as a `Const` node.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dims` | A 1-D sequence of non-negative numbers. Represents the shape of the output [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Entries should be of type: `int32`, `int64`. |
| `value` | A value to fill the returned [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |
| `name` | Optional string. The name of the output [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout)<br>. If provided, the result is a [DTensor](https://www.tensorflow.org/guide/dtensor_overview)<br> with the provided layout. |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> with shape `dims` and the same dtype as `value`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | `dims` contains negative entries. |
| `NotFoundError` | `dims` contains non-integer entries. |

numpy compatibility
-------------------

Similar to `np.full`. In `numpy`, more parameters are supported. Passing a number argument as the shape (`np.full(5, value)`) is valid in `numpy` for specifying a 1-D shaped result, while TensorFlow does not support this syntax.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.