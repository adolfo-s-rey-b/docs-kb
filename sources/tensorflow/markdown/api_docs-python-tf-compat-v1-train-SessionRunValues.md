[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunValues#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunValues)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunValues?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunValues#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunValues#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.SessionRunValues Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunValues#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunValues#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_run_hook.py#L262-L283)

Contains the results of `Session.run()`.

tf.compat.v1.train.SessionRunValues(
        results, options, run_metadata
    )

In the future we may use this object to add more information about result of run without changing the Hook API.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `results` | The return values from `Session.run()` corresponding to the fetches attribute returned in the RunArgs. Note that this has the same shape as the RunArgs fetches. For example: fetches = global\_step\_tensor => results = nparray(int) fetches = \[train\_op, summary\_op, global\_step\_tensor\] => results = \[None, nparray(string), nparray(int)\] fetches = {'step': global\_step\_tensor, 'summ': summary\_op} => results = {'step': nparray(int), 'summ': nparray(string)} |
| `options` | `RunOptions` from the `Session.run()` call. |
| `run_metadata` | `RunMetadata` from the `Session.run()` call. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `results` | A `namedtuple` alias for field number 0 |
| `options` | A `namedtuple` alias for field number 1 |
| `run_metadata` | A `namedtuple` alias for field number 2 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.