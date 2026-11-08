[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/saved_model/save?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.saved\_model.save Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/saved_model/save#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/save.py#L1241-L1434)

Exports a [tf.Module](https://www.tensorflow.org/api_docs/python/tf/Module)
 (and subclasses) `obj` to [SavedModel format](https://www.tensorflow.org/guide/saved_model#the_savedmodel_format_on_disk)
.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.experimental.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
, [`tf.compat.v1.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)

tf.saved_model.save(
        obj,
        export_dir: str,
        signatures=None,
        options: tf.saved_model.SaveOptions = None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)<br>    <br>*   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [TensorFlow basics](https://www.tensorflow.org/guide/basics) | *   [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load)<br>    <br>*   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load)<br>    <br>*   [Load text](https://www.tensorflow.org/tutorials/load_data/text) |

The `obj` must inherit from the [`Trackable` class](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/trackable/base.py#L278)
.

#### Example usage:

    class Adder(tf.Module):

    model = Adder()

The resulting SavedModel is then servable with an input named "x", a scalar with dtype float32.

_Signatures_

Signatures define the input and output types for a computation. The optional save `signatures` argument controls which methods in `obj` will be available to programs which consume `SavedModel`s, for example, serving APIs. Python functions may be decorated with [`@tf.function(input_signature=...)`](https://www.tensorflow.org/api_docs/python/tf/function)
 and passed as signatures directly, or lazily with a call to `get_concrete_function` on the method decorated with [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

#### Example:

    class Adder(tf.Module):

    model = Adder()

If a [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 does not have an input signature and `get_concrete_function` is not called on that method, the function will not be directly callable in the restored SavedModel.

#### Example:

    class Adder(tf.Module):

    model = Adder()

If the `signatures` argument is omitted, `obj` will be searched for [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
\-decorated methods. If exactly one traced [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 is found, that method will be used as the default signature for the SavedModel. Else, any [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 attached to `obj` or its dependencies will be exported for use with [`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
.

When invoking a signature in an exported SavedModel, `Tensor` arguments are identified by name. These names will come from the Python function's argument names by default. They may be overridden by specifying a `name=...` argument in the corresponding [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)
 object. Explicit naming is required if multiple `Tensor`s are passed through a single argument to the Python function.

The outputs of functions used as `signatures` must either be flat lists, in which case outputs will be numbered, or a dictionary mapping string keys to `Tensor`, in which case the keys will be used to name outputs.

Signatures are available in objects returned by [`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
 as a `.signatures` attribute. This is a reserved attribute: [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
 on an object with a custom `.signatures` attribute will raise an exception.

\_Using [`tf.saved_model.save_`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
 _with Keras models_

While Keras has its own [saving and loading API](https://www.tensorflow.org/guide/keras/save_and_serialize)
, this function can be used to export Keras models. For example, exporting with a signature specified:

    class Adder(tf.keras.Model):

    model = Adder()

Exporting from a function without a fixed signature:

    class Adder(tf.keras.Model):

    model = Adder()

[`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
 instances constructed from inputs and outputs already have a signature and so do not require a [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 decorator or a `signatures` argument. If neither are specified, the model's forward pass is exported.

    x = tf.keras.layers.Input((4,), name="x")

The exported SavedModel takes "x" with shape \[None, 4\] and returns "out" with shape \[None, 5\]

_Variables and Checkpoints_

Variables must be tracked by assigning them to an attribute of a tracked object or to an attribute of `obj` directly. TensorFlow objects (e.g. layers from [`tf.keras.layers`](https://www.tensorflow.org/api_docs/python/tf/keras/layers)
, optimizers from [`tf.train`](https://www.tensorflow.org/api_docs/python/tf/train)
) track their variables automatically. This is the same tracking scheme that [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
 uses, and an exported `Checkpoint` object may be restored as a training checkpoint by pointing [`tf.train.Checkpoint.restore`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
 to the SavedModel's "variables/" subdirectory.

[`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 does not hard-code device annotations from outside the function body, instead of using the calling context's device. This means for example that exporting a model that runs on a GPU and serving it on a CPU will generally work, with some exceptions:

*   [`tf.device`](https://www.tensorflow.org/api_docs/python/tf/device)
     annotations inside the body of the function will be hard-coded in the exported model; this type of annotation is discouraged.
*   Device-specific operations, e.g. with "cuDNN" in the name or with device-specific layouts, may cause issues.
*   For `ConcreteFunctions`, active distribution strategies will cause device placements to be hard-coded in the function.

SavedModels exported with [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
 [strip default-valued attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes)
 automatically, which removes one source of incompatibilities when the consumer of a SavedModel is running an older TensorFlow version than the producer. There are however other sources of incompatibilities which are not handled automatically, such as when the exported model contains operations which the consumer does not have definitions for.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `obj` | A trackable object (e.g. tf.Module or tf.train.Checkpoint) to export. |
| `export_dir` | A directory in which to write the SavedModel. |
| `signatures` | Optional, one of three types:<br><br>*   A [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>     with an input signature specified, which will use the default serving signature key.<br>*   The result of `f.get_concrete_function` on a [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>    \-decorated function `f`, in which case `f` will be used to generate a signature for the SavedModel under the default serving signature key.<br>*   A dictionary, which maps signature keys to either [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>     instances with input signatures or concrete functions. Keys of such a dictionary may be arbitrary strings, but will typically be from the `tf.saved_model.signature_constants` module. |
| `options` | [`tf.saved_model.SaveOptions`](https://www.tensorflow.org/api_docs/python/tf/saved_model/SaveOptions)<br> object for configuring save options. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `obj` is not trackable. |

eager compatibility
-------------------

Not well supported when graph building. From TensorFlow 1.x, [`tf.compat.v1.enable_eager_execution()`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution)
 should run first. Calling tf.saved\_model.save in a loop when graph building from TensorFlow 1.x will add new save operations to the default graph each iteration.

May not be called from within a function body.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.