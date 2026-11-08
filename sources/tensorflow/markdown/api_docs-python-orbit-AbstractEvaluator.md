[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Forbit%2FAbstractEvaluator&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#methods)
    *   [evaluate](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#evaluate)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#with_name_scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.AbstractEvaluator Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#methods)
    *   [evaluate](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#evaluate)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator#with_name_scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/runner.py#L58-L83)

An abstract class defining the API required for evaluation.

orbit.AbstractEvaluator(
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

### `evaluate`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/runner.py#L61-L83)

@abc.abstractmethod

Implements `num_steps` steps of evaluation.

This method will by called the `Controller` to perform an evaluation. The `num_steps` parameter specifies the number of steps of evaluation to run, which is specified by the user when calling one of the `Controller`'s evaluation methods. A special sentinel value of `-1` is reserved to indicate evaluation should run until the underlying data source is exhausted.

|     |     |
| --- | --- |
| Args |     |
| `num_steps` | The number of evaluation steps to run. Note that it is up to the model what constitutes a "step". Evaluations may also want to support "complete" evaluations when `num_steps == -1`, running until a given data source is exhausted. |

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