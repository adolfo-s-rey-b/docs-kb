[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fplaceholder&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.placeholder Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L2976-L3028)

Inserts a placeholder for a tensor that will be always fed.

tf.compat.v1.placeholder(
        dtype, shape=None, name=None
    )

Migrate to TF2
--------------

This API is not compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. To migrate to TF2, rewrite the code to be compatible with eager execution. Check the [migration guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
 on replacing `Session.run` calls. In TF2, you can just pass tensors directly into ops and layers. If you want to explicitly set up your inputs, also see [Keras functional API](https://www.tensorflow.org/guide/keras/functional)
 on how to use [`tf.keras.Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)
 to replace [`tf.compat.v1.placeholder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder)
. [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 arguments also do the job of [`tf.compat.v1.placeholder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder)
. For more details please read [Better performance with tf.function](https://www.tensorflow.org/guide/function)
.

Description
-----------

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging)<br>    <br>*   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model)<br>    <br>*   [Migrating your TFLite code to TF2](https://www.tensorflow.org/guide/migrate/tflite) | *   [Generating Images with BigBiGAN](https://www.tensorflow.org/hub/tutorials/bigbigan_with_tf_hub)<br>    <br>*   [Classify Flowers with Transfer Learning](https://www.tensorflow.org/hub/tutorials/image_feature_vector)<br>    <br>*   [Generating Images with Little Data Using S3GAN](https://www.tensorflow.org/hub/tutorials/s3gan_generation_with_tf_hub)<br>    <br>*   [Generating Images with BigGAN](https://www.tensorflow.org/hub/tutorials/biggan_generation_with_tf_hub)<br>    <br>*   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings) |

#### For example:

x = tf.compat.v1.placeholder(tf.float32, shape=(1024, 1024))
    y = tf.matmul(x, x)
    
    with tf.compat.v1.Session() as sess:
      print(sess.run(y))  # ERROR: will fail because x was not fed.
    
      rand_array = np.random.rand(1024, 1024)
      print(sess.run(y, feed_dict={x: rand_array}))  # Will succeed.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dtype` | The type of elements in the tensor to be fed. |
| `shape` | The shape of the tensor to be fed (optional). If the shape is not specified, you can feed a tensor of any shape. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` that may be used as a handle for feeding a value, but not evaluated directly. |     |

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