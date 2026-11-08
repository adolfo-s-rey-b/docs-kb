[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.confusion\_matrix Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/confusion_matrix.py#L199-L259)

Computes the confusion matrix from predictions and labels.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.confusion_matrix`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/confusion_matrix)

tf.compat.v1.confusion_matrix(
        labels,
        predictions,
        num_classes=None,
        dtype=tf.dtypes.int32,
        name=None,
        weights=None
    )

The matrix columns represent the prediction labels and the rows represent the real labels. The confusion matrix is always a 2-D array of shape `[n, n]`, where `n` is the number of valid labels for a given classification task. Both prediction and labels must be 1-D arrays of the same shape in order for this function to work.

If `num_classes` is `None`, then `num_classes` will be set to one plus the maximum value in either predictions or labels. Class labels are expected to start at 0. For example, if `num_classes` is 3, then the possible labels would be `[0, 1, 2]`.

If `weights` is not `None`, then each prediction contributes its corresponding weight to the total value of the confusion matrix cell.

#### For example:

  tf.math.confusion_matrix([1, 2, 4], [2, 2, 4]) ==>
          [[0 0 0 0 0]\
           [0 0 1 0 0]\
           [0 0 1 0 0]\
           [0 0 0 0 0]\
           [0 0 0 0 1]]

Note that the possible labels are assumed to be `[0, 1, 2, 3, 4]`, resulting in a 5x5 confusion matrix.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | 1-D `Tensor` of real labels for the classification task. |
| `predictions` | 1-D `Tensor` of predictions for a given classification. |
| `num_classes` | The possible number of labels the classification task can have. If this value is not provided, it will be calculated using both predictions and labels array. |
| `dtype` | Data type of the confusion matrix. |
| `name` | Scope name. |
| `weights` | An optional `Tensor` whose shape matches `predictions`. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `dtype` with shape `[n, n]` representing the confusion matrix, where `n` is the number of possible labels in the classification task. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If both predictions and labels are not 1-D vectors and have mismatched shapes, or if `weights` is not `None` and its shape doesn't match `predictions`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.