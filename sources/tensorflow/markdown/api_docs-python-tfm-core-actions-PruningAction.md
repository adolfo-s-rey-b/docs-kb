[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fcore%2Factions%2FPruningAction&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.actions.PruningAction Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/actions/PruningAction#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/actions.py#L30-L73)

Train action to updates pruning related information.

tfm.core.actions.PruningAction(
        export_dir: str,
        model: tf_keras.Model,
        optimizer: tf_keras.optimizers.Optimizer
    )

This action updates pruning steps at the end of trainig loop, and log pruning metrics to tensorboard.

This action must be used when training a pruned model to avoid pruning error.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `export_dir` | `str` for the export directory of the pruning summaries. |
| `model` | `tf_keras.Model` model instance used for training. This will be used to assign a pruning step to each prunable weight. |
| `optimizer` | `tf_keras.optimizers.Optimizer` optimizer instance used for training. This will be used to find the current training steps. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/actions.py#L66-L73)

__call__(
        output: orbit.runner.Output
    )

Update pruning step and log pruning summaries.

|     |     |
| --- | --- |
| Args |     |
| `output` | The train output. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.