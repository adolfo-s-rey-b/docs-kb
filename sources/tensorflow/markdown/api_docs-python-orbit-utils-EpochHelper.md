[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#methods)
    *   [epoch\_begin](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#epoch_begin)
        
    *   [epoch\_end](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#epoch_end)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.utils.EpochHelper Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#methods)
    *   [epoch\_begin](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#epoch_begin)
        
    *   [epoch\_end](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper#epoch_end)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/epoch_helper.py#L20-L65)

A helper class handle bookkeeping of epochs in custom training loops.

orbit.utils.EpochHelper(
        epoch_steps: int, global_step: tf.Variable
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `epoch_steps` | An integer indicating how many steps are in an epoch. |
| `global_step` | A [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> providing the current global step. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `batch_index` | Index of the next batch within the current epoch. |
| `current_epoch` |     |

Methods
-------

### `epoch_begin`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/epoch_helper.py#L36-L44)

epoch_begin()

Returns whether a new epoch should begin.

### `epoch_end`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/epoch_helper.py#L46-L56)

epoch_end()

Returns whether the current epoch should end.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.