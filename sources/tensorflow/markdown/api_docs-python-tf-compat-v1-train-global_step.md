[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/global_step#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/global_step)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/global_step?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/global_step#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/global_step#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.global\_step Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/global_step#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/global_step#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/training_util.py#L39-L67)

Small helper to get the global step.

tf.compat.v1.train.global_step(
        sess, global_step_tensor
    )

# Create a variable to hold the global_step.
    global_step_tensor = tf.Variable(10, trainable=False, name='global_step')
    # Create a session.
    sess = tf.compat.v1.Session()
    # Initialize the variable
    sess.run(global_step_tensor.initializer)
    # Get the variable value.
    print('global_step: %s' % tf.compat.v1.train.global_step(sess,
    global_step_tensor))
    
    global_step: 10

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sess` | A TensorFlow `Session` object. |
| `global_step_tensor` | `Tensor` or the `name` of the operation that contains the global step. |

|     |
| --- |
| Returns<br>------- |     |
| The global step value. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.