[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/actions/RecoveryCondition#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/actions/RecoveryCondition)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/actions/RecoveryCondition?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/actions/RecoveryCondition#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/actions/RecoveryCondition#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.actions.RecoveryCondition Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/actions/RecoveryCondition#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/actions/RecoveryCondition#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/actions.py#L144-L175)

Recovery Condition.

tfm.core.actions.RecoveryCondition(
        global_step: tf.Variable,
        loss_upper_bound: float,
        recovery_begin_steps: int = 0,
        recovery_max_trials: int = 3
    )

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/actions.py#L158-L175)

__call__(
        outputs: orbit.runner.Output
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.