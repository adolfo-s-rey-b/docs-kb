[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/add_n#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/add_n)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/add_n?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/add_n#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/add_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/add_n#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/add_n#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.add\_n Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/add_n#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/add_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/add_n#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/add_n#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3997-L4054)

Returns the element-wise sum of a list of tensors.

#### View aliases

**Main aliases**

[`tf.add_n`](https://www.tensorflow.org/api_docs/python/tf/math/add_n)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.add_n`](https://www.tensorflow.org/api_docs/python/tf/math/add_n)
, [`tf.compat.v1.math.add_n`](https://www.tensorflow.org/api_docs/python/tf/math/add_n)

tf.math.add_n(
        inputs, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Validating correctness & numerical equivalence](https://www.tensorflow.org/guide/migrate/validate_correctness)<br>    <br>*   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping)<br>    <br>*   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training)<br>    <br>*   [Use a GPU](https://www.tensorflow.org/guide/gpu) | *   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)<br>    <br>*   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit) |

All inputs in the list must have the same shape. This op does not [broadcast](https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)
 its inputs. If you need broadcasting, use [`tf.math.add`](https://www.tensorflow.org/api_docs/python/tf/math/add)
 (or the `+` operator) instead.

#### For example:

    a = tf.constant([[3, 5], [4, 8]])

#### See Also:

*   [`tf.reduce_sum(inputs, axis=0)`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_sum)
     - This performs the same mathematical operation, but [`tf.add_n`](https://www.tensorflow.org/api_docs/python/tf/math/add_n)
     may be more efficient because it sums the tensors directly. `reduce_sum` on the other hand calls [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)
     on the list of tensors, unnecessarily stacking them into a single tensor before summing.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> objects, each with the same shape and type. [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> objects will be converted into dense tensors prior to adding. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the same shape and type as the elements of `inputs`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `inputs` don't all have same shape and dtype or the shape cannot be inferred. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.