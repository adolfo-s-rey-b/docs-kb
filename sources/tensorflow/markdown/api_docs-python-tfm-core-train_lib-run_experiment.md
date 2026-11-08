[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/run_experiment#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/run_experiment)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/run_experiment?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/run_experiment#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/run_experiment#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.train\_lib.run\_experiment Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/run_experiment#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/run_experiment#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_lib.py#L307-L370)

Runs train/eval configured by the experiment params.

tfm.core.train_lib.run_experiment(
        distribution_strategy: tf.distribute.Strategy,
        task: tfm.core.base_task.Task,
        mode: str,
        params: tfm.core.base_trainer.ExperimentConfig,
        model_dir: str,
        run_post_eval: bool = False,
        save_summary: bool = True,
        train_actions: Optional[List[orbit.Action]] = None,
        eval_actions: Optional[List[orbit.Action]] = None,
        trainer: Optional[tfm.core.base_trainer.Trainer] = None,
        controller_cls=orbit.Controller,
        summary_manager: Optional[orbit.utils.SummaryManager] = None,
        eval_summary_manager: Optional[orbit.utils.SummaryManager] = None,
        enable_async_checkpointing: bool = False
    ) -> Tuple[tf_keras.Model, Mapping[str, Any]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `distribution_strategy` | A distribution distribution\_strategy. |
| `task` | A Task instance. |
| `mode` | A 'str', specifying the mode. Can be 'train', 'eval', 'train\_and\_eval' or 'continuous\_eval'. |
| `params` | ExperimentConfig instance. |
| `model_dir` | A 'str', a path to store model checkpoints and summaries. |
| `run_post_eval` | Whether to run post eval once after training, metrics logs are returned. |
| `save_summary` | Whether to save train and validation summary. |
| `train_actions` | Optional list of Orbit train actions. |
| `eval_actions` | Optional list of Orbit eval actions. |
| `trainer` | the base\_trainer.Trainer instance. It should be created within the strategy.scope(). |
| `controller_cls` | The controller class to manage the train and eval process. Must be a orbit.Controller subclass. |
| `summary_manager` | Instance of the summary manager to override default summary manager. |
| `eval_summary_manager` | Instance of the eval summary manager to override default eval summary manager. |
| `enable_async_checkpointing` | Optional boolean indicating whether to enable async checkpoint saving. |

|     |
| --- |
| Returns<br>------- |     |
| A 2-tuple of (model, eval\_logs). model: `tf_keras.Model` instance. eval\_logs: returns eval metrics logs when run\_post\_eval is set to True, otherwise, returns {}. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.