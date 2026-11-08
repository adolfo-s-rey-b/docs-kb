[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.stack Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/stack?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops_stack.py#L24-L85)

Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.stack`](https://www.tensorflow.org/api_docs/python/tf/stack)

tf.stack(
        values, axis=0, name='stack'
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [TensorFlow basics](https://www.tensorflow.org/guide/basics)<br>    <br>*   [Random number generation](https://www.tensorflow.org/guide/random_numbers) | *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)<br>    <br>*   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv) |

See also [`tf.concat`](https://www.tensorflow.org/api_docs/python/tf/concat)
, [`tf.tile`](https://www.tensorflow.org/api_docs/python/tf/tile)
, [`tf.repeat`](https://www.tensorflow.org/api_docs/python/tf/repeat)
.

Packs the list of tensors in `values` into a tensor with rank one higher than each tensor in `values`, by packing them along the `axis` dimension. Given a list of length `N` of tensors of shape `(A, B, C)`;

if `axis == 0` then the `output` tensor will have the shape `(N, A, B, C)`. if `axis == 1` then the `output` tensor will have the shape `(A, N, B, C)`. Etc.

#### For example:

    x = tf.constant([1, 4])

This is the opposite of unstack. The numpy equivalent is `np.stack`

    np.array_equal(np.stack([x, y, z]), tf.stack([x, y, z]))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | A list of `Tensor` objects with the same shape and type. |
| `axis` | An `int`. The axis to stack along. Defaults to the first dimension. Negative values wrap around, so the valid range is `[-(R+1), R+1)`. |\
| `name` | A name for this operation (optional). |\
\
|     |     |\
| --- | --- |\
| Returns<br>------- |     |\
| `output` | A stacked `Tensor` with the same type as `values`. |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `axis` is out of the range \[-(R+1), R+1). |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.