[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.checkpoints\_iterator Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/checkpoint_utils.py#L181-L243)

Continuously yield new checkpoint files as they appear.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.checkpoints_iterator`](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator)

tf.train.checkpoints_iterator(
        checkpoint_dir, min_interval_secs=0, timeout=None, timeout_fn=None
    )

The iterator only checks for new checkpoints when control flow has been reverted to it. This means it can miss checkpoints if your code takes longer to run between iterations than `min_interval_secs` or the interval at which new checkpoints are written.

The `timeout` argument is the maximum number of seconds to block waiting for a new checkpoint. It is used in combination with the `timeout_fn` as follows:

*   If the timeout expires and no `timeout_fn` was specified, the iterator stops yielding.
*   If a `timeout_fn` was specified, that function is called and if it returns a true boolean value the iterator stops yielding.
*   If the function returns a false boolean value then the iterator resumes the wait for new checkpoints. At this point the timeout logic applies again.

This behavior gives control to callers on what to do if checkpoints do not come fast enough or stop being generated. For example, if callers have a way to detect that the training has stopped and know that no new checkpoints will be generated, they can provide a `timeout_fn` that returns `True` when the training has stopped. If they know that the training is still going on they return `False` instead.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `checkpoint_dir` | The directory in which checkpoints are saved. |
| `min_interval_secs` | The minimum number of seconds between yielding checkpoints. |
| `timeout` | The maximum number of seconds to wait between checkpoints. If left as `None`, then the process will wait indefinitely. |
| `timeout_fn` | Optional function to call after a timeout. If the function returns True, then it means that no new checkpoints will be generated and the iterator will exit. The function is called with no arguments. |

|     |
| --- |
| Yields<br>------ |     |
| String paths to latest checkpoint files as they arrive. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.