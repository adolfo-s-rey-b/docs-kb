[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/range#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/range)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/range?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/range#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/range#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/range#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/range#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.range Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/range#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/range#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/range#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/range#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2016-L2102)

Creates a sequence of numbers.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.range`](https://www.tensorflow.org/api_docs/python/tf/range)

tf.range(limit, delta=1, dtype=None, name='range')
    tf.range(start, limit, delta=1, dtype=None, name='range')

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator)<br>    <br>*   [Optimizers with Core APIs](https://www.tensorflow.org/guide/core/optimizers_core) | *   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load)<br>    <br>*   [Playing CartPole with the Actor-Critic method](https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic)<br>    <br>*   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input) |

Creates a sequence of numbers that begins at `start` and extends by increments of `delta` up to but not including `limit`.

The dtype of the resulting tensor is inferred from the inputs unless it is provided explicitly.

Like the Python builtin `range`, `start` defaults to 0, so that `range(n) = range(0, n)`.

#### For example:

    start = 3

    start = 3

    limit = 5

|     |     |
| --- | --- |
| Args<br>---- |     |
| `start` | A 0-D `Tensor` (scalar). Acts as first entry in the range if `limit` is not None; otherwise, acts as range limit and first entry defaults to 0. |
| `limit` | A 0-D `Tensor` (scalar). Upper limit of sequence, exclusive. If None, defaults to the value of `start` while the first entry of the range defaults to 0. |
| `delta` | A 0-D `Tensor` (scalar). Number that increments `start`. Defaults to 1. |
| `dtype` | The type of the elements of the resulting tensor. |
| `name` | A name for the operation. Defaults to "range". |

|     |
| --- |
| Returns<br>------- |     |
| An 1-D `Tensor` of type `dtype`. |     |

numpy compatibility
-------------------

Equivalent to np.arange

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.