[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#methods)
    *   [create\_train\_loop\_fn](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#create_train_loop_fn)
        
    *   [train](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#train)
        
    *   [train\_loop\_begin](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#train_loop_begin)
        
    *   [train\_loop\_end](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#train_loop_end)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#train_step)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#with_name_scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.StandardTrainer Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#methods)
    *   [create\_train\_loop\_fn](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#create_train_loop_fn)
        
    *   [train](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#train)
        
    *   [train\_loop\_begin](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#train_loop_begin)
        
    *   [train\_loop\_end](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#train_loop_end)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#train_step)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer#with_name_scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L71-L211)

Implements standard functionality on top of the AbstractTrainer API.

Inherits From: [`AbstractTrainer`](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer)

orbit.StandardTrainer(
        train_dataset,
        options: Optional[orbit.StandardTrainerOptions] = None
    )

This class structures the training "inner loop" roughly as follows:

train_loop_begin()
    for _ in range(num_steps):
      train_step(train_iterator)
    return train_loop_end()

Calls to `train_loop_begin` and `train_loop_end` are always done in eager mode, while the loop/`train_step` may be implemented using `tf.while` and/or [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, as determined by the `options` passed to `__init__`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `train_dataset` | A [`tf.nest`](https://www.tensorflow.org/api_docs/python/tf/nest)<br>\-compatible structure of [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> or `DistributedDataset`. |
| `options` | An [`orbit.StandardTrainerOptions`](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions)<br> instance. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `train_dataset` | The current training dataset. |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `create_train_loop_fn`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L109-L126)

create_train_loop_fn()

Creates a training loop from the current step function and options.

|     |
| --- |
| Returns |     |
| The train loop function, i.e. wrapper of multiple train steps. |     |

### `train`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L128-L147)

train(
        num_steps: tf.Tensor
    ) -> Optional[runner.Output]

Implements `num_steps` steps of training.

|     |     |
| --- | --- |
| Args |     |
| `num_steps` | The number of training steps to run. This corresponds directly to the number of calls made to `train_step`. |

|     |
| --- |
| Returns |     |
| The output of `train_loop_end`. |     |

### `train_loop_begin`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L149-L157)

train_loop_begin()

Called once at the beginning of the training loop.

This method is always called in eager mode, and is a good place to reset metrics that accumulate values over multiple steps of training.

Note that this method is called before dataset iterator creation.

### `train_loop_end`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L181-L193)

train_loop_end() -> Optional[runner.Output]

Called once at the end of the training loop.

This method is always called in eager mode, and is a good place to get metric results. The value returned from this function will be returned as-is from the `train` method implementation provided by `StandardTrainer`.

|     |
| --- |
| Returns |     |
| The function may return a dictionary of `Tensors`, which will be written to logs and as TensorBoard summaries. It can also be a nested dictionary, yielding a hierarchy of summary directories. |     |

### `train_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L159-L179)

@abc.abstractmethod

Implements one step of training.

What a "step" consists of is up to the implementer. When using distribution strategies, the call to this method takes place in the "cross-replica context" for generality, to allow e.g. multiple iterator dequeues and calls to `strategy.run`.

Note that if `use_tf_function=True`, all the code inside `train_step` should be compatible with [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 tracing (and in particular, any state modifications involving `self` should be avoided). In some cases, non- [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 compatible code can be moved to `train_loop_begin` or `train_loop_end`, which always execute eagerly.

|     |     |
| --- | --- |
| Args |     |
| `iterator` | A [`tf.nest`](https://www.tensorflow.org/api_docs/python/tf/nest)<br>\-compatible structure of [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)<br> or `DistributedIterator`. The structure of this input matches the structure of `train_dataset` as passed to `__init__`. |

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