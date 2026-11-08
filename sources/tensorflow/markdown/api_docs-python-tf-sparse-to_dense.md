[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsparse%2Fto_dense&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.to\_dense Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L1681-L1734)

Converts a `SparseTensor` into a dense tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.to_dense`](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense)
, [`tf.compat.v1.sparse_tensor_to_dense`](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense)

tf.sparse.to_dense(
        sp_input, default_value=None, validate_indices=True, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Working with sparse tensors](https://www.tensorflow.org/guide/sparse_tensor)<br>    <br>*   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [Introduction to tensor slicing](https://www.tensorflow.org/guide/tensor_slicing) | *   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning)<br>    <br>*   [Text generation with an RNN](https://www.tensorflow.org/text/tutorials/text_generation)<br>    <br>*   [TFX Estimator Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components)<br>    <br>*   [TFX Keras Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components_keras)<br>    <br>*   [Licensed under the Apache License, Version 2.0 (the "License");](https://www.tensorflow.org/tfx/tutorials/tfx/gpt2_finetuning_and_conversion) |

For this sparse tensor with three non-empty values:

    sp_input = tf.sparse.SparseTensor(

The output will be a dense `[3, 5]` tensor with values:

    tf.sparse.to_dense(sp_input).numpy()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The input `SparseTensor`. |
| `default_value` | Scalar value to set for indices not specified in `sp_input`. Defaults to zero. |
| `validate_indices` | A boolean value. If `True`, indices are checked to make sure they are sorted in lexicographic order and that there are no repeats. |
| `name` | A name prefix for the returned tensors (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A dense tensor with shape `sp_input.dense_shape` and values specified by the non-empty values in `sp_input`. Indices not in `sp_input` are assigned `default_value`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.