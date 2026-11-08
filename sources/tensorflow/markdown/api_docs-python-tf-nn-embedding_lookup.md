[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.embedding\_lookup Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/embedding_ops.py#L375-L438)

Looks up embeddings for the given `ids` from a list of tensors.

tf.nn.embedding_lookup(
        params, ids, max_norm=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding) | *   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

This function is used to perform parallel lookups on the list of tensors in `params`. It is a generalization of [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
, where `params` is interpreted as a partitioning of a large embedding tensor.

If `len(params) > 1`, each element `id` of `ids` is partitioned between the elements of `params` according to the "div" partition strategy, which means we assign ids to partitions in a contiguous manner. For instance, 13 ids are split across 5 partitions as: `[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.

If the id space does not evenly divide the number of partitions, each of the first `(max_id + 1) % len(params)` partitions will be assigned one more id.

The results of the lookup are concatenated into a dense tensor. The returned tensor has shape `shape(ids) + shape(params)[1:]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | A single tensor representing the complete embedding tensor, or a list of tensors all of same shape except for the first dimension, representing sharded embedding tensors following "div" partition strategy. |
| `ids` | A `Tensor` with type `int32` or `int64` containing the ids to be looked up in `params`. |
| `max_norm` | If not `None`, each embedding is clipped if its l2-norm is larger than this value. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as the tensors in `params`.<br><br>For instance, if `params` is a 5x2 matrix:<br><br>[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]<br><br>or a list of matrices:<br><br>params[0]: [[1, 2], [3, 4]]<br>    params[1]: [[5, 6], [7, 8]]<br>    params[2]: [[9, 10]]<br><br>and `ids` is:<br><br>[0, 3, 4]<br><br>The output will be a 3x2 matrix:<br><br>[[1, 2], [7, 8], [9, 10]] |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `params` is empty. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.