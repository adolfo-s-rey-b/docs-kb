[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/one_hot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/one_hot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.one\_hot Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/one_hot?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L3988-L4148)

Returns a one-hot tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.one_hot`](https://www.tensorflow.org/api_docs/python/tf/one_hot)

tf.one_hot(
        indices,
        depth,
        on_value=None,
        off_value=None,
        axis=None,
        dtype=None,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Quickstart for the TensorFlow Core APIs](https://www.tensorflow.org/guide/core/quickstart_core)<br>    <br>*   [Training & evaluation with the built-in methods](https://www.tensorflow.org/guide/keras/training_with_built_in_methods) | *   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)<br>    <br>*   [Custom Federated Algorithms, Part 2: Implementing Federated Averaging](https://www.tensorflow.org/federated/tutorials/custom_federated_algorithms_2)<br>    <br>*   [Federated Learning for Image Classification](https://www.tensorflow.org/federated/tutorials/federated_learning_for_image_classification)<br>    <br>*   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index)<br>    <br>*   [Parametrized Quantum Circuits for Reinforcement Learning](https://www.tensorflow.org/quantum/tutorials/quantum_reinforcement_learning) |

See also [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
, [`tf.eye`](https://www.tensorflow.org/api_docs/python/tf/eye)
.

The locations represented by indices in `indices` take value `on_value`, while all other locations take value `off_value`.

`on_value` and `off_value` must have matching data types. If `dtype` is also provided, they must be the same data type as specified by `dtype`.

If `on_value` is not provided, it will default to the value `1` with type `dtype`

If `off_value` is not provided, it will default to the value `0` with type `dtype`

If the input `indices` is rank `N`, the output will have rank `N+1`. The new axis is created at dimension `axis` (default: the new axis is appended at the end).

If `indices` is a scalar the output shape will be a vector of length `depth`

If `indices` is a vector of length `features`, the output shape will be:

  features x depth if axis == -1
      depth x features if axis == 0

If `indices` is a matrix (batch) with shape `[batch, features]`, the output shape will be:

  batch x features x depth if axis == -1
      batch x depth x features if axis == 1
      depth x batch x features if axis == 0

If `indices` is a RaggedTensor, the 'axis' argument must be positive and refer to a non-ragged axis. The output will be equivalent to applying 'one\_hot' on the values of the RaggedTensor, and creating a new RaggedTensor from the result.

If `dtype` is not provided, it will attempt to assume the data type of `on_value` or `off_value`, if one or both are passed in. If none of `on_value`, `off_value`, or `dtype` are provided, `dtype` will default to the value [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)
.

#### For example:

indices = [0, 1, 2]
    depth = 3
    tf.one_hot(indices, depth)  # output: [3 x 3]
    # [[1., 0., 0.],\
    #  [0., 1., 0.],\
    #  [0., 0., 1.]]
    
    indices = [0, 2, -1, 1]
    depth = 3
    tf.one_hot(indices, depth,
               on_value=5.0, off_value=0.0,
               axis=-1)  # output: [4 x 3]
    # [[5.0, 0.0, 0.0],  # one_hot(0)\
    #  [0.0, 0.0, 5.0],  # one_hot(2)\
    #  [0.0, 0.0, 0.0],  # one_hot(-1)\
    #  [0.0, 5.0, 0.0]]  # one_hot(1)
    
    indices = [[0, 2], [1, -1]]
    depth = 3
    tf.one_hot(indices, depth,
               on_value=1.0, off_value=0.0,
               axis=-1)  # output: [2 x 2 x 3]
    # [[[1.0, 0.0, 0.0],   # one_hot(0)\
    #   [0.0, 0.0, 1.0]],  # one_hot(2)\
    #  [[0.0, 1.0, 0.0],   # one_hot(1)\
    #   [0.0, 0.0, 0.0]]]  # one_hot(-1)
    
    indices = tf.ragged.constant([[0, 1], [2]])
    depth = 3
    tf.one_hot(indices, depth)  # output: [2 x None x 3]
    # [[[1., 0., 0.],\
    #   [0., 1., 0.]],\
    #  [[0., 0., 1.]]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `indices` | A `Tensor` of indices. |
| `depth` | A scalar defining the depth of the one hot dimension. |
| `on_value` | A scalar defining the value to fill in output when `indices[j] = i`. (default: 1) |
| `off_value` | A scalar defining the value to fill in output when `indices[j] != i`. (default: 0) |
| `axis` | The axis to fill (default: -1, a new inner-most axis). |
| `dtype` | The data type of the output tensor. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output` | The one-hot tensor. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If dtype of either `on_value` or `off_value` don't match `dtype` |
| `TypeError` | If dtype of `on_value` and `off_value` don't match one another |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.