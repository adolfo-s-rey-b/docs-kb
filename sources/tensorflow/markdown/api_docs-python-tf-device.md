[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/device#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/device)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/device?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/device#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/device#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/device#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/device#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.device Stay organized with collections Save and categorize content based on your preferences.
================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/device#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/device#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/device#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/device#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L4445-L4481)

Specifies the device for ops created/executed in this context.

tf.device(
        device_name
    ) -> ContextManager[None]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [NumPy API on TensorFlow](https://www.tensorflow.org/guide/tf_numpy)<br>    <br>*   [Use a GPU](https://www.tensorflow.org/guide/gpu)<br>    <br>*   [Introduction to Variables](https://www.tensorflow.org/guide/variable)<br>    <br>*   [Random number generation](https://www.tensorflow.org/guide/random_numbers)<br>    <br>*   [Use TPUs](https://www.tensorflow.org/guide/tpu) | *   [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)<br>    <br>*   [Solve GLUE tasks using BERT on TPU](https://www.tensorflow.org/text/tutorials/bert_glue) |

This function specifies the device to be used for ops created/executed in a particular context. Nested contexts will inherit and also create/execute their ops on the specified device. If a specific device is not required, consider not using this function so that a device can be automatically assigned. In general the use of this function is optional. `device_name` can be fully specified, as in "/job:worker/task:1/device:cpu:0", or partially specified, containing only a subset of the "/"-separated fields. Any fields which are specified will override device annotations from outer scopes.

#### For example:

with tf.device('/job:foo'):
      # ops created here have devices with /job:foo
      with tf.device('/job:bar/task:0/device:gpu:2'):
        # ops created here have the fully specified device above
      with tf.device('/device:gpu:1'):
        # ops created here have the device '/job:foo/device:gpu:1'

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_name` | The device name to use in the context. |

|     |
| --- |
| Returns<br>------- |     |
| A context manager that specifies the default device to use for newly created ops. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If a function is passed in. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.