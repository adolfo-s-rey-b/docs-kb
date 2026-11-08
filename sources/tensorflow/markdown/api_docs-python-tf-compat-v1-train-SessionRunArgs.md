[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunArgs#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunArgs)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunArgs?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunArgs#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunArgs#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.SessionRunArgs Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunArgs#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunArgs#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_run_hook.py#L185-L207)

Represents arguments to be added to a `Session.run()` call.

tf.compat.v1.train.SessionRunArgs(
        fetches, feed_dict=None, options=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fetches` | Exactly like the 'fetches' argument to Session.Run(). Can be a single tensor or op, a list of 'fetches' or a dictionary of fetches. For example: fetches = global\_step\_tensor fetches = \[train\_op, summary\_op, global\_step\_tensor\] fetches = {'step': global\_step\_tensor, 'summ': summary\_op} Note that this can recurse as expected: fetches = {'step': global\_step\_tensor, 'ops': \[train\_op, check\_nan\_op\]} |
| `feed_dict` | Exactly like the `feed_dict` argument to `Session.Run()` |
| `options` | Exactly like the `options` argument to `Session.run()`, i.e., a config\_pb2.RunOptions proto. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `fetches` | A `namedtuple` alias for field number 0 |
| `feed_dict` | A `namedtuple` alias for field number 1 |
| `options` | A `namedtuple` alias for field number 2 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.