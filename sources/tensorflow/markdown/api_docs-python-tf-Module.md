[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/Module#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/Module)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/Module?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/Module#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/Module#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/Module#methods)
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tf/Module#with_name_scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.Module Stay organized with collections Save and categorize content based on your preferences.
================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/Module#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/Module#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/Module#methods)
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tf/Module#with_name_scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/module/module.py#L29-L313)

Base neural network module class.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)

tf.Module(
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [Logistic regression for binary classification with Core APIs](https://www.tensorflow.org/guide/core/logistic_regression_core)<br>    <br>*   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core) | *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention)<br>    <br>*   [Neural machine translation with a Transformer and Keras](https://www.tensorflow.org/text/tutorials/transformer) |

A module is a named container for [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
s, other [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
s and functions which apply to user input. For example a dense layer in a neural network might be implemented as a [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
:

    class Dense(tf.Module):

You can use the Dense layer as you would expect:

    d = Dense(input_dim=3, output_size=2)

By subclassing [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
 instead of `object` any [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 or [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
 instances assigned to object properties can be collected using the `variables`, `trainable_variables` or `submodules` property:

    d.variables

Subclasses of [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
 can also take advantage of the `_flatten` method which can be used to implement tracking of any other types.

All [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
 classes have an associated [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)
 which can be used to group operations in TensorBoard and create hierarchies for variable names which can help with debugging. We suggest using the name scope when creating nested submodules/parameters or for forward methods whose graph you might want to inspect in TensorBoard. You can enter the name scope explicitly using `with self.name_scope:` or you can annotate methods (apart from `__init__`) with [`@tf.Module.with_name_scope`](https://www.tensorflow.org/api_docs/python/tf/Module#with_name_scope)
.

    class MLP(tf.Module):

    module = MLP(input_size=5, sizes=[5, 5])

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

### `with_name_scope`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/module/module.py#L282-L313)

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

Last updated 2026-10-31 UTC.