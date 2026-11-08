[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model/LoadOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.saved\_model.LoadOptions Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/load_options.py#L21-L125)

Options for loading a SavedModel.

tf.saved_model.LoadOptions(
        allow_partial_checkpoint=False,
        experimental_io_device=None,
        experimental_skip_checkpoint=False,
        experimental_variable_policy=None,
        experimental_load_function_aliases=False
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load) |

This function may be used in the `options` argument in functions that load a SavedModel ([`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
, [`tf.keras.models.load_model`](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model)
).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `allow_partial_checkpoint` | bool. Defaults to `False`. When enabled, allows the SavedModel checkpoint to not entirely match the loaded object. |
| `experimental_io_device` | string. Applies in a distributed setting. Tensorflow device to use to access the filesystem. If `None` (default) then for each variable the filesystem is accessed from the CPU:0 device of the host where that variable is assigned. If specified, the filesystem is instead accessed from that device for all variables. This is for example useful if you want to load from a local directory, such as "/tmp" when running in a distributed setting. In that case pass a device for the host where the "/tmp" directory is accessible. |
| `experimental_skip_checkpoint` | bool. Defaults to `False`. If set to `True`, checkpoints will not be restored. Note that this in the majority of cases will generate an unusable model. |
| `experimental_variable_policy` | string. The policy to apply to variables when loading. This is either a [`saved_model.experimental.VariablePolicy`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/VariablePolicy)<br> enum instance or one of its value strings (case is not important). See that enum documentation for details. A value of `None` corresponds to the default policy. |
| `experimental_load_function_aliases` | bool. Defaults to `False`. If set to `True`, a `function_aliases` attribute will be added to the loaded SavedModel object. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `allow_partial_checkpoint` |     |
| `experimental_io_device` |     |
| `experimental_load_function_aliases` |     |
| `experimental_skip_checkpoint` |     |
| `experimental_variable_policy` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.