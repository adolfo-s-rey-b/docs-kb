[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fcore%2Ftrain_lib%2FOrbitExperimentRunner&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#methods)
    *   [run](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#run)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.train\_lib.OrbitExperimentRunner Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#methods)
    *   [run](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/OrbitExperimentRunner#run)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_lib.py#L34-L304)

Runs experiment with Orbit training loop.

tfm.core.train_lib.OrbitExperimentRunner(
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
    )

The default experiment runner for model garden experiments. User can customize the experiment pipeline by subclassing this class and replacing components or functions.

For example, an experiment runner with customized checkpoint manager:

class MyExpRunnerWithExporter(OrbitExperimentRunner):
      def _maybe_build_checkpoint_manager(sefl):
        # Replaces the default CheckpointManger with a customized one.
        return MyCheckpointManager(*args)
    
    # In user code, instead of the orginal
    # `OrbitExperimentRunner(..).run(mode)`, now user can do:
    MyExpRunnerWithExporter(**needed_kwargs).run(mode)

Similar override can be done to other components.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `distribution_strategy` | A distribution strategy. |
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

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_manager` | The CheckpointManager that stores the checkpoints in a train job. |
| `controller` | The Orbit controller object. |
| `model_dir` | Path to the model folder, which stores checkpoints, params, log, etc. |
| `params` | The whole experiment parameters object. |
| `trainer` | The underlying Orbit Trainer object. |

Methods
-------

### `run`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_lib.py#L253-L304)

run() -> Tuple[tf_keras.Model, Mapping[str, Any]]

Run experiments by mode.

|     |
| --- |
| Returns |     |
| A 2-tuple of (model, eval\_logs). model: `tf_keras.Model` instance. eval\_logs: returns eval metrics logs when run\_post\_eval is set to True, otherwise, returns {}. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.