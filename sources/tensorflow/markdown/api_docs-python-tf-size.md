[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/size#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/size)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/size?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/size#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/size#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/size#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.size Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/size#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/size#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/size#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L762-L799)

Returns the size of a tensor.

tf.size(
        input, out_type=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core)<br>    <br>*   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [BERT Preprocessing with TF Text](https://www.tensorflow.org/text/guide/bert_preprocessing_guide) | *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Sending Different Data To Particular Clients With federated\_language.federated\_select](https://www.tensorflow.org/federated/tutorials/federated_select)<br>    <br>*   [Human Pose Classification with MoveNet and TensorFlow Lite](https://www.tensorflow.org/lite/tutorials/pose_classification)<br>    <br>*   [Federated Learning for Image Classification](https://www.tensorflow.org/federated/tutorials/federated_learning_for_image_classification) |

See also [`tf.shape`](https://www.tensorflow.org/api_docs/python/tf/shape)
.

Returns a 0-D `Tensor` representing the number of elements in `input` of type `out_type`. Defaults to tf.int32.

#### For example:

    t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` or `SparseTensor`. |
| `out_type` | (Optional) The specified non-quantized numeric output type of the operation. Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. (Note: there is an experimental flag, `tf_shape_default_int64` that changes the default to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. This is an unsupported, experimental setting that causes known breakages.) |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `out_type`. Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. |     |

numpy compatibility
-------------------

Equivalent to np.size()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.