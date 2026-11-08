[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#methods)
    *   [create\_eval\_loop\_fn](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#create_eval_loop_fn)
        
    *   [eval\_begin](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#eval_begin)
        
    *   [eval\_end](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#eval_end)
        
    *   [eval\_reduce](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#eval_reduce)
        
    *   [eval\_step](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#eval_step)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#evaluate)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#with_name_scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.StandardEvaluator Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#methods)
    *   [create\_eval\_loop\_fn](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#create_eval_loop_fn)
        
    *   [eval\_begin](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#eval_begin)
        
    *   [eval\_end](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#eval_end)
        
    *   [eval\_reduce](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#eval_reduce)
        
    *   [eval\_step](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#eval_step)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#evaluate)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#with_name_scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L238-L450)

Implements the standard functionality of AbstractEvaluator APIs.

Inherits From: [`AbstractEvaluator`](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator)

orbit.StandardEvaluator(
        eval_dataset,
        options: Optional[orbit.StandardEvaluatorOptions] = None
    )

This class structures evaluation roughly as follows:

state = eval_begin()
    for _ in range(num_steps):
      step_outputs = eval_step(eval_iterator)
      state = eval_reduce(state, step_outputs)
    return eval_end(state)

Calls to `eval_begin` and `eval_end` are always done in eager mode, while `eval_step` may be compiled with [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 as determined by the `options` passed to `__init__`. `eval_reduce` is in eager mode if `use_tf_while_loop=False` in `StandardEvaluatorOptions`, but in graph mode if `use_tf_while_loop=True`.

This class does not support completely evaluating multiple different datasets (i.e., where every example of each dataset should be processed, as opposed to running for a fixed number of evaluation steps). A custom `AbstractEvaluator` is recommended in this case.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `eval_dataset` | A [`tf.nest`](https://www.tensorflow.org/api_docs/python/tf/nest)<br>\-compatible structure of [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> or `DistributedDataset`. On TPUs, if users want to exaust the dataset without specifying number of eval steps, it is recommended to set `drop_remainder=False` when batching the dataset, so the infrastructure can handle the last partial batch properly. |
| `options` | An [`orbit.StandardEvaluatorOptions`](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions)<br> instance. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `eval_dataset` | The current evaluation dataset. |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `create_eval_loop_fn`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L284-L307)

create_eval_loop_fn(
        has_state: bool
    )

Creates an eval loop from the current step function and options.

|     |     |
| --- | --- |
| Args |     |
| `has_state` | If the step function has state, state will be kept in the loop. |

|     |
| --- |
| Returns |     |
| The eval loop function, i.e. wrapper of multiple eval steps. |     |

### `eval_begin`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L354-L365)

eval_begin() -> Any

Called once at the beginning of the evaluation.

This method is always called in eager mode, and is a good place to reset metrics that accumulate values over the course of evaluation.

Note that this method is called before dataset iterator creation.

|     |
| --- |
| Returns |     |
| A value to pass as the `state` argument to `eval_reduce`. |     |

### `eval_end`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L392-L410)

eval_end(
        *args
    ) -> Optional[runner.Output]

Called at the end of the evaluation.

Called once at the end of evaluation.

This method is always called in eager mode, and is a good place to get metric results. The value returned from this function will be returned as-is from the `evaluate` method implementation provided by `StandardEvaluator`.

|     |     |
| --- | --- |
| Args |     |
| `*args` | The outputs from `eval_reduce` for the last eval step, if they are non-`None` (if they are `None`, nothing is passed). |

|     |
| --- |
| Returns |     |
| The function may return a dictionary of `Tensors`, which will be written to logs and as TensorBoard summaries. It can also be a nested dictionary, yielding a hierarchy of summary directories. |     |

### `eval_reduce`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L412-L432)

eval_reduce(
        state: Optional[Any] = None, step_outputs: Optional[runner.Output] = None
    ) -> Any

A function to perform per-step reduction on the evaluation outputs.

This is useful for passing state throughout evaluation, especially in cases where maintaining or accumulating state is hard to accomplish using `tf.metrics.Metric` or other [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
\-based approaches. For instance, it can be used to easily accumulate all per-example losses from the full evaluation for subsequent processing in `eval_end()`.

|     |     |
| --- | --- |
| Args |     |
| `state` | A state being maintained throughout the evaluation. |
| `step_outputs` | Outputs from the current evaluation step. |

|     |
| --- |
| Returns |     |
| An output which is passed as the `state` argument to this function for the next step. After evaluation is finished, the output from last step will be passed to `eval_end`. |     |

### `eval_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L367-L390)

@abc.abstractmethod

Implements one step of evaluation.

What a "step" consists of is up to the implementer. When using distribution strategies, the call to this method takes place in the "cross-replica context" for generality, to allow e.g. multiple iterator dequeues and calls to `strategy.run`.

Note that if `use_tf_function=True`, all the code inside `eval_step` should be compatible with [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 tracing (and in particular, any state modifications involving `self` should be avoided). In some cases, non- [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 compatible code can be moved to `eval_loop_begin`, `eval_reduce`, or `eval_loop_end`, which always execute eagerly.

|     |     |
| --- | --- |
| Args |     |
| `iterator` | A [`tf.nest`](https://www.tensorflow.org/api_docs/python/tf/nest)<br>\-compatible structure of [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)<br> or `DistributedIterator`. |

|     |
| --- |
| Returns |     |
| An output which is passed as `step_outputs` argument into `eval_reduce` function. |     |

### `evaluate`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L309-L352)

evaluate(
        num_steps: tf.Tensor
    ) -> Optional[runner.Output]

Implements `num_steps` steps of evaluation.

|     |     |
| --- | --- |
| Args |     |
| `num_steps` | The number of evaluation steps to run. When this is -1, evaluation proceeds until a call to `eval_step` raises a `StopIteration` or [`tf.errors.OutOfRangeError`](https://www.tensorflow.org/api_docs/python/tf/errors/OutOfRangeError)<br>. |

|     |
| --- |
| Returns |     |
| The output of `self.eval_end()`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `options.use_tf_while_loop` is `True` and `num_steps` is unspecified. |

### `with_name_scope`

@classmethod

Decorator to automatically enter the module name scope.

    class MyModule(tf.Module):

Using the above module would produce [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
s and [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s whose names included the module name:

    mod = MyModule()

|     |     |
| --- | --- |
| Args |     |
| `method` | The method to wrap. |

|     |
| --- |
| Returns |     |
| The original method wrapped such that it enters the module's name scope. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.