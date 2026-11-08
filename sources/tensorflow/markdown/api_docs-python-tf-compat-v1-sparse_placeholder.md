[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.sparse\_placeholder Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L3083-L3192)

Inserts a placeholder for a sparse tensor that will be always fed.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.placeholder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder)

tf.compat.v1.sparse_placeholder(
        dtype, shape=None, name=None
    )

Migrate to TF2
--------------

This API is not compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. To migrate to TF2, rewrite the code to be compatible with eager execution. Check the [migration guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
 on replacing `Session.run` calls. In TF2, you can just pass tensors directly into ops and layers. If you want to explicitly set up your inputs, also see [Keras functional API](https://www.tensorflow.org/guide/keras/functional)
 on how to use [`tf.keras.Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)
 to replace [`tf.compat.v1.sparse_placeholder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder)
. [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 arguments also do the job of [`tf.compat.v1.sparse_placeholder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_placeholder)
. For more details please read [Better performance with tf.function](https://www.tensorflow.org/guide/function)
.

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Universal Sentence Encoder-Lite demo](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite) |

#### For example:

x = tf.compat.v1.sparse.placeholder(tf.float32)
    y = tf.sparse.reduce_sum(x)
    
    with tf.compat.v1.Session() as sess:
      print(sess.run(y))  # ERROR: will fail because x was not fed.
    
      indices = np.array([[3, 2, 0], [4, 5, 1]], dtype=np.int64)
      values = np.array([1.0, 2.0], dtype=np.float32)
      shape = np.array([7, 9, 2], dtype=np.int64)
      print(sess.run(y, feed_dict={
        x: tf.compat.v1.SparseTensorValue(indices, values, shape)}))  # Will
        succeed.
      print(sess.run(y, feed_dict={
        x: (indices, values, shape)}))  # Will succeed.
    
      sp = tf.sparse.SparseTensor(indices=indices, values=values,
                                  dense_shape=shape)
      sp_value = sp.eval(session=sess)
      print(sess.run(y, feed_dict={x: sp_value}))  # Will succeed.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dtype` | The type of `values` elements in the tensor to be fed. |
| `shape` | The shape of the tensor to be fed (optional). If the shape is not specified, you can feed a sparse tensor of any shape. |
| `name` | A name for prefixing the operations (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` that may be used as a handle for feeding a value, but not evaluated directly. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | if eager execution is enabled |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.