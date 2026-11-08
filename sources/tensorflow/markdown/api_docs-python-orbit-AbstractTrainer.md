[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#methods)
    *   [train](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#train)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#with_name_scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.AbstractTrainer Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#methods)
    *   [train](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#train)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer#with_name_scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/runner.py#L28-L55)

An abstract class defining the API required for training.

orbit.AbstractTrainer(
        name=None
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `train`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/runner.py#L31-L55)

@abc.abstractmethod

Implements `num_steps` steps of training.

This method will be called by the `Controller` to perform the "inner loop" of training. This inner loop amortizes the cost of bookkeeping associated with checkpointing, evaluation, and writing summaries. Additionally, the inner loop can be implemented (if desired) using TensorFlow's looping constructs (e.g. a `for` loop over a [`tf.range`](https://www.tensorflow.org/api_docs/python/tf/range)
 inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
), which can be necessary for getting optimal performance when running on TPU. For cases that don't require peak performance, a simple Python loop can be used instead for simplicity.

|     |     |
| --- | --- |
| Args |     |
| `num_steps` | The number of training steps to run. Note that it is up to the model what constitutes a "step", which may involve more than one update to model parameters (e.g., if training a GAN). |

|     |
| --- |
| Returns |     |
| Either `None`, or a dictionary mapping names to `Tensor`s or NumPy values. If a dictionary is returned, it will be written to logs and as TensorBoard summaries. The dictionary may also be nested, which will generate a hierarchy of summary directories. |     |

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