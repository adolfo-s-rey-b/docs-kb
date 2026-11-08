[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/edit_distance#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/edit_distance)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/edit_distance?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/edit_distance#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/edit_distance#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/edit_distance#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.edit\_distance Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/edit_distance#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/edit_distance#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/edit_distance#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L3524-L3626)

Computes the Levenshtein distance between sequences.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.edit_distance`](https://www.tensorflow.org/api_docs/python/tf/edit_distance)

tf.edit_distance(
        hypothesis, truth, normalize=True, name='edit_distance'
    )

This operation takes variable-length sequences (`hypothesis` and `truth`), each provided as a `SparseTensor`, and computes the Levenshtein distance. You can normalize the edit distance by length of `truth` by setting `normalize` to true.

#### For example:

Given the following input,

*   `hypothesis` is a [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
     of shape `[2, 1, 1]`
*   `truth` is a [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
     of shape `[2, 2, 2]`

    hypothesis = tf.SparseTensor(

The operation returns a dense Tensor of shape `[2, 2]` with edit distances normalized by `truth` lengths.

For the following inputs,

# 'hypothesis' is a tensor of shape `[2, 1]` with variable-length values:
    #   (0,0) = ["a"]
    #   (1,0) = ["b"]
    hypothesis = tf.sparse.SparseTensor(
        [[0, 0, 0],\
         [1, 0, 0]],
        ["a", "b"],
        (2, 1, 1))
    
    # 'truth' is a tensor of shape `[2, 2]` with variable-length values:
    #   (0,0) = []
    #   (0,1) = ["a"]
    #   (1,0) = ["b", "c"]
    #   (1,1) = ["a"]
    truth = tf.sparse.SparseTensor(
        [[0, 1, 0],\
         [1, 0, 0],\
         [1, 0, 1],\
         [1, 1, 0]],
        ["a", "b", "c", "a"],
        (2, 2, 2))
    
    normalize = True
    
    # The output would be a dense Tensor of shape `(2,)`, with edit distances
    normalized by 'truth' lengths.
    # output => array([0., 0.5], dtype=float32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `hypothesis` | A `SparseTensor` containing hypothesis sequences. |
| `truth` | A `SparseTensor` containing truth sequences. |
| `normalize` | A `bool`. If `True`, normalizes the Levenshtein distance by length of `truth.` |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A dense `Tensor` with rank `R - 1`, where R is the rank of the `SparseTensor` inputs `hypothesis` and `truth`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If either `hypothesis` or `truth` are not a `SparseTensor`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.