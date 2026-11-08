[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.actions.EMACheckpointing Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/actions/EMACheckpointing#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/actions.py#L76-L123)

Eval action to save checkpoint with average weights when EMA is used.

tfm.core.actions.EMACheckpointing(
        export_dir: str,
        optimizer: tf_keras.optimizers.Optimizer,
        checkpoint: tf.train.Checkpoint,
        max_to_keep: int = 1
    )

This action swaps the weights of the model with the average weights, then it saves the checkpoint under export\_dir/ema\_checkpoints. Checkpointing is expensive for large models, so doing this action in eval is more efficient than training.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `export_dir` | `str` for the export directory of the EMA average weights. |
| `optimizer` | `tf_keras.optimizers.Optimizer` optimizer instance used for training. This will be used to swap the model weights with the average weigths. |
| `checkpoint` | [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> instance. |
| `max_to_keep` | `int` for max checkpoints to keep in ema\_checkpoints subdir. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/actions.py#L115-L123)

__call__(
        output: orbit.runner.Output
    )

Swaps model weights, and saves the checkpoint.

|     |     |
| --- | --- |
| Args |     |
| `output` | The train or eval output. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.