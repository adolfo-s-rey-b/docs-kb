[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/Controller#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/Controller)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/Controller?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/Controller#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/orbit/Controller#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/Controller#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/Controller#methods)
    *   [evaluate](https://www.tensorflow.org/api_docs/python/orbit/Controller#evaluate)
        
    *   [evaluate\_continuously](https://www.tensorflow.org/api_docs/python/orbit/Controller#evaluate_continuously)
        
    *   [restore\_checkpoint](https://www.tensorflow.org/api_docs/python/orbit/Controller#restore_checkpoint)
        
    *   [save\_checkpoint](https://www.tensorflow.org/api_docs/python/orbit/Controller#save_checkpoint)
        
    *   [train](https://www.tensorflow.org/api_docs/python/orbit/Controller#train)
        
    *   [train\_and\_evaluate](https://www.tensorflow.org/api_docs/python/orbit/Controller#train_and_evaluate)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.Controller Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/Controller#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/orbit/Controller#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/Controller#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/Controller#methods)
    *   [evaluate](https://www.tensorflow.org/api_docs/python/orbit/Controller#evaluate)
        
    *   [evaluate\_continuously](https://www.tensorflow.org/api_docs/python/orbit/Controller#evaluate_continuously)
        
    *   [restore\_checkpoint](https://www.tensorflow.org/api_docs/python/orbit/Controller#restore_checkpoint)
        
    *   [save\_checkpoint](https://www.tensorflow.org/api_docs/python/orbit/Controller#save_checkpoint)
        
    *   [train](https://www.tensorflow.org/api_docs/python/orbit/Controller#train)
        
    *   [train\_and\_evaluate](https://www.tensorflow.org/api_docs/python/orbit/Controller#train_and_evaluate)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/controller.py#L60-L581)

Class that controls the outer loop of model training and evaluation.

orbit.Controller(
        *,
        global_step: tf.Variable,
        trainer: Optional[orbit.AbstractTrainer] = None,
        evaluator: Optional[orbit.AbstractEvaluator] = None,
        strategy: Optional[tf.distribute.Strategy] = None,
        train_actions: Optional[Iterable[Action]] = None,
        eval_actions: Optional[Iterable[Action]] = None,
        steps_per_loop: Optional[Union[int, Callable[[int], int]]] = None,
        checkpoint_manager: Optional[tf.train.CheckpointManager] = None,
        enable_async_checkpointing: bool = False,
        summary_interval: Optional[int] = None,
        summary_dir: Optional[str] = None,
        eval_summary_dir: Optional[str] = None,
        summary_manager: Optional[orbit.utils.SummaryManagerInterface] = None,
        eval_summary_manager: Optional[orbit.utils.SummaryManagerInterface] = None
    )

Orbit divides training and evaluation into "inner" and "outer" loops. Inner loops are implemented by users in the form of `AbstractTrainer` and `AbstractEvaluator` subclasses, and define how to run a given number of training or evaluation steps. The outer loop is provided by this `Controller`, and interleaves calls to the user-provided inner loops with additional actions such as saving checkpoints, running evaluations, writing summaries, as well as (optionally) user provided `Action`s (see below).

There are four top-level "outer loops" provided:

*   `train`, which trains until a specified number of global steps is reached;
*   `evaluate`, for one-off model evaluation;
*   `train_and_evaluate`, for interleaved training and evaluation;
*   `evaluate_continuously`, for monitoring a given directory and running evaluations on new model checkpoints.

While this class attempts to provide out-of-the-box solutions for common training and evaluation use cases, the internal details and method implementations are also intended to be simple enough to make subclassing or other custom outer loop implementations easy to achieve.

Some additional customization can be achieved by supplying `train_actions` or `eval_actions` when constructing the `Controller`. Actions arbitrary callables that are applied by the `Controller` to the output of train steps (after each inner loop of `steps_per_loop` steps) or an evaluation. This provides a hook mechanism, enabling things like reporting metrics to Vizier, model exporting, additional logging, etc. See the [`orbit.actions`](https://www.tensorflow.org/api_docs/python/orbit/actions)
 package for a small handful of predefined actions and some utility classes that may be useful in defining your own.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `global_step` | An integer [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> storing the global training step number. Usually this can be obtained from the `iterations` property of the model's optimizer (e.g. `trainer.optimizer.iterations`). In cases where multiple optimizers are used, or if one model "step" corresponds to more than one update to model parameters, users can create and increment their own global step variable as well. In this case it is recommended to create the [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> inside the distribution strategy scope, with `aggregation=tf.VariableAggregation.ONLY_FIRST_REPLICA` (see also [`orbit.utils.create_global_step()`](https://www.tensorflow.org/api_docs/python/orbit/utils/create_global_step)<br>). |
| `trainer` | An instance of [`orbit.AbstractTrainer`](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer)<br>, which implements the inner training loop. |
| `evaluator` | An instance of [`orbit.AbstractEvaluator`](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator)<br>, which implements evaluation. |
| `strategy` | An instance of [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br>. If not provided, the strategy will be initialized from the current in-scope strategy using [`tf.distribute.get_strategy()`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy)<br>. |
| `train_actions` | Optional [`orbit.Action`](https://www.tensorflow.org/api_docs/python/orbit/Action)<br>s to call after each block of `steps_per_loop` training steps are run. These will be called with the output of `trainer.train`. |
| `eval_actions` | Optional [`orbit.Action`](https://www.tensorflow.org/api_docs/python/orbit/Action)<br>s to call after each evaluation. These will be called with the output of `evaluator.evaluate`. |
| `steps_per_loop` | Optional integer to indicate the number of steps to run in each inner loop of training (passed as the `num_steps` parameter of `trainer.train`). It can be also a callable which takes the current global step value as input and returns the number of steps to run as output. |
| `checkpoint_manager` | An instance of [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br>. If provided and there are checkpoints in the associated model directory, the model will be restored from the most recent checkpoint inside this `__init__` method. If not provided, the `Controller` will not automatically save to or restore from checkpoints. |
| `enable_async_checkpointing` | Optional bool indicating whether to enable async checkpoint saving. |
| `summary_interval` | Step interval for training summaries. Note that this argument only applies to [`tf.summary`](https://www.tensorflow.org/api_docs/python/tf/summary)<br> calls inside the `trainer.train` function. Summaries written by the `Controller` (specifically "steps\_per\_second" and output from the `trainer.train` method) will always be enabled unless the `summary_dir` parameter is `None`. If set, the value must be divisible by `steps_per_loop`. |
| `summary_dir` | The directory to write summaries to. To use the same directory as for checkpointing, pass `checkpoint_manager.directory`. If `None`, no training summaries will be written. |
| `eval_summary_dir` | The directory to write eval summaries to. If `None`, it will be set to `summary_dir`. If both `summary_dir` and `eval_summary_dir` are `None`, no eval summaries will be written. |
| `summary_manager` | Instance of the summary manager. If set, the `summary_dir` will be ignored. Otherwise the summary manager will be created internally for TensorBoard summaries by default from the `summary_dir`. |
| `eval_summary_manager` | Instance of the eval summary manager. If set, the `eval_summary_dir` will be ignored. Otherwise the eval summary manager will be created internally for TensorBoard summaries by default from the `eval_summary_dir`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If both `trainer` and `evaluator` are `None`. |
| `ValueError` | If `steps_per_loop` is not a positive integer or a callable. |
| `ValueError` | If `summary_interval` is not a positive integer or is not divisible by `steps_per_loop`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `steps_per_loop` | Returns current steps\_per\_loop value in a training loop. |

Methods
-------

### `evaluate`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/controller.py#L291-L351)

evaluate(
        steps: int = -1
    ) -> Optional[runner.Output]

Runs evaluation for the given number of steps.

This method calls `self.evaluator.evaluate(steps)`, then writes the returned summaries (if any).

|     |     |
| --- | --- |
| Args |     |
| `steps` | The number of evaluation steps to run. The value `-1` is reserved as a special sentinel to indicate a "complete" evaluation that runs until the underlying dataset is exhausted. Support for this is dependent on the specific `evaluator` being used. |

|     |
| --- |
| Returns |     |
| The evaluation results as a dictionary mapping names to NumPy values. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `evaluator` was not provided to [`Controller.**init**`](https://www.tensorflow.org/api_docs/python/orbit/Controller#__init__)<br>. |
| `ValueError` | If no checkpoint is present in `checkpoint_manager.directory`. |
| `ValueError` | If `steps` is not a positive value or -1. |

### `evaluate_continuously`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/controller.py#L400-L439)

evaluate_continuously(
        steps: int = -1,
        timeout: Optional[Union[int, float]] = None,
        timeout_fn: Optional[Callable[[], bool]] = None
    ) -> Optional[runner.Output]

Continuously monitors a directory and evaluates new checkpoints in it.

This method continuously monitors a directory as specified by this Controller's CheckpointManager init arg and runs evaluation on the checkpoints found there.

|     |     |
| --- | --- |
| Args |     |
| `steps` | The number of steps to run when evaluating. If -1, this method will evaluate over the entire evaluation dataset. |
| `timeout` | The maximum number of seconds to wait between checkpoints. See tf.train.checkpoints\_iterator documentation. |
| `timeout_fn` | Optional callable to call after a timeout. If the function returns True, then it means that no new checkpoints will be generated and the iterator will exit. |

|     |
| --- |
| Returns |     |
| The evaluation results as a dictionary mapping names to NumPy values. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If no checkpoint found in `self.checkpoint_manager.directory`. |
| `ValueError` | If `evaluator` was not provided as a controller init arg. |

### `restore_checkpoint`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/controller.py#L441-L469)

restore_checkpoint(
        checkpoint_path: Optional[str] = None
    )

Restores the model from a checkpoint.

|     |     |
| --- | --- |
| Args |     |
| `checkpoint_path` | An optional string specifying the checkpoint path to restore from. If `None`, will restore from the most recent checkpoint (or initialize the model using a custom `init_fn` if no checkpoints can be found) using `self.checkpoint_manager.restore_or_initialize()`. |

|     |
| --- |
| Returns |     |
| The path to the restored checkpoint if a restore happened, or `None` if no restore occurred. |     |

### `save_checkpoint`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/controller.py#L471-L482)

save_checkpoint()

Saves the model to a checkpoint.

This method will save a checkpoint containing the current state of the model.

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If no `checkpoint_manager` was provided to [`Controller.**init**`](https://www.tensorflow.org/api_docs/python/orbit/Controller#__init__)<br>. |

### `train`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/controller.py#L257-L289)

train(
        steps: int, checkpoint_at_completion: bool = True
    )

Runs training until the specified global step count has been reached.

This method makes calls to `self.trainer.train()` until the global step count is equal to `steps`. It will additionally save checkpoints (if a `CheckpointManager` was passed to [`Controller.**init**`](https://www.tensorflow.org/api_docs/python/orbit/Controller#__init__)
) and summarize training output (if `summary_dir` is set).

When async checkpointing is enabled, a sync is triggered at the end of this method to make sure any ongoing async checkpoint saving is finished before returning.

|     |     |
| --- | --- |
| Args |     |
| `steps` | The global step count to train up to. |
| `checkpoint_at_completion` | Whether to save a checkpoint when this method returns (regardless of the checkpointing interval). Defaults to `True`. |

### `train_and_evaluate`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/controller.py#L353-L398)

train_and_evaluate(
        train_steps: int, eval_steps: int = -1, eval_interval: Optional[int] = None
    ) -> Optional[runner.Output]

Runs interleaved training and evaluation.

This method interleaves calls to `self.train()` and `self.evaluate()`, training the model until the global step count equals `train_steps`, and running an evaluation for `eval_steps` every `eval_interval` training steps. In addition, this method will run a final evaluation at the end of the training sequence.

When async checkpointing is enabled, a sync is triggered at the end of this method to make sure any ongoing async checkpoint saving is finished before returning.

|     |     |
| --- | --- |
| Args |     |
| `train_steps` | The global step count to train up to. |
| `eval_steps` | The number of steps to run during an evaluation. If -1, this method will evaluate over the entire evaluation dataset. |
| `eval_interval` | The number of training steps to run between evaluations. If set, training will always stop every `eval_interval` steps, even if this results in a shorter inner loop than specified by `steps_per_loop` setting. If None, evaluation will only be performed after training is complete. |

|     |
| --- |
| Returns |     |
| The evaluation results as a dictionary mapping names to NumPy values. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.