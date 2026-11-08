[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/ema_optimizer/maybe_merge_call#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/ema_optimizer/maybe_merge_call)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/ema_optimizer/maybe_merge_call?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/ema_optimizer/maybe_merge_call#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/ema_optimizer/maybe_merge_call#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.ema\_optimizer.maybe\_merge\_call Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/ema_optimizer/maybe_merge_call#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/ema_optimizer/maybe_merge_call#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L24-L48)

Maybe invoke `fn` via `merge_call` which may or may not be fulfilled.

tfm.optimization.ema_optimizer.maybe_merge_call(
        fn, strategy, *args, **kwargs
    )

The caller of this utility function requests to invoke `fn` via `merge_call` at [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
's best efforts. It is [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
's internal whether the request is honored, depending on the `Strategy`. See [`tf.distribute.ReplicaContext.merge_call()`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#merge_call)
 for more information.

This is adapted from tensorflow/python/distribute/merge\_call\_interim.py.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fn` | the function to be invoked. |
| `strategy` | the [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> to call `fn` with. |
| `*args` | the positional arguments to be passed in to `fn`. |
| `**kwargs` | the keyword arguments to be passed in to `fn`. |

|     |
| --- |
| Returns<br>------- |     |
| The return value of the `fn` call. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.