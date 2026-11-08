[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sets/difference#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sets/difference)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sets/difference?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sets/difference#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sets/difference#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sets/difference#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sets.difference Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sets/difference#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sets/difference#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sets/difference#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sets_impl.py#L208-L286)

Compute set difference of elements in last dimension of `a` and `b`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sets.difference`](https://www.tensorflow.org/api_docs/python/tf/sets/difference)
, [`tf.compat.v1.sets.set_difference`](https://www.tensorflow.org/api_docs/python/tf/sets/difference)

tf.sets.difference(
        a, b, aminusb=True, validate_indices=True
    )

All but the last dimension of `a` and `b` must match.

#### Example:

  import tensorflow as tf
      import collections
    
      # Represent the following array of sets as a sparse tensor:
      # a = np.array([[{1, 2}, {3}], [{4}, {5, 6}]])
      a = collections.OrderedDict([\
          ((0, 0, 0), 1),\
          ((0, 0, 1), 2),\
          ((0, 1, 0), 3),\
          ((1, 0, 0), 4),\
          ((1, 1, 0), 5),\
          ((1, 1, 1), 6),\
      ])
      a = tf.sparse.SparseTensor(list(a.keys()), list(a.values()),
                                 dense_shape=[2, 2, 2])
    
      # np.array([[{1, 3}, {2}], [{4, 5}, {5, 6, 7, 8}]])
      b = collections.OrderedDict([\
          ((0, 0, 0), 1),\
          ((0, 0, 1), 3),\
          ((0, 1, 0), 2),\
          ((1, 0, 0), 4),\
          ((1, 0, 1), 5),\
          ((1, 1, 0), 5),\
          ((1, 1, 1), 6),\
          ((1, 1, 2), 7),\
          ((1, 1, 3), 8),\
      ])
      b = tf.sparse.SparseTensor(list(b.keys()), list(b.values()),
                                 dense_shape=[2, 2, 4])
    
      # `set_difference` is applied to each aligned pair of sets.
      tf.sets.difference(a, b)
    
      # The result will be equivalent to either of:
      #
      # np.array([[{2}, {3}], [{}, {}]])
      #
      # collections.OrderedDict([\
      #     ((0, 0, 0), 2),\
      #     ((0, 1, 0), 3),\
      # ])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | `Tensor` or `SparseTensor` of the same type as `b`. If sparse, indices must be sorted in row-major order. |
| `b` | `Tensor` or `SparseTensor` of the same type as `a`. If sparse, indices must be sorted in row-major order. |
| `aminusb` | Whether to subtract `b` from `a`, vs vice versa. |
| `validate_indices` | Whether to validate the order and range of sparse indices in `a` and `b`. |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` whose shape is the same rank as `a` and `b`, and all but the last dimension the same. Elements along the last dimension contain the differences. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If inputs are invalid types, or if `a` and `b` have different types. |
| `ValueError` | If `a` is sparse and `b` is dense. |
| `errors_impl.InvalidArgumentError` | If the shapes of `a` and `b` do not match in any dimension other than the last dimension. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.