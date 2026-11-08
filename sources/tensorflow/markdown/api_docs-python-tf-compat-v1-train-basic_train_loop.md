[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/basic_train_loop#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/basic_train_loop)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/basic_train_loop?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/basic_train_loop#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.basic\_train\_loop Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/basic_train_loop#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_loops.py#L20-L61)

Basic loop to train a model.

tf.compat.v1.train.basic_train_loop(
        supervisor, train_step_fn, args=None, kwargs=None, master=''
    )

Calls `train_step_fn` in a loop to train a model. The function is called as:

train_step_fn(session, *args, **kwargs)

It is passed a [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
 in addition to `args` and `kwargs`. The function typically runs one training step in the session.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `supervisor` | [`tf.compat.v1.train.Supervisor`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Supervisor)<br> to run the training services. |
| `train_step_fn` | Callable to execute one training step. Called repeatedly as `train_step_fn(session, *args **kwargs)`. |
| `args` | Optional positional arguments passed to `train_step_fn`. |
| `kwargs` | Optional keyword arguments passed to `train_step_fn`. |
| `master` | Master to use to create the training session. Defaults to `""` which causes the session to be created in the local process. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.