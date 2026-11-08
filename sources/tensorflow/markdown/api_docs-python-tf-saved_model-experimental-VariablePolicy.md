[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/VariablePolicy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/VariablePolicy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/VariablePolicy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsaved_model%2Fexperimental%2FVariablePolicy&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/VariablePolicy#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.saved\_model.experimental.VariablePolicy Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/VariablePolicy#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/save_options.py#L27-L90)

Enum defining options for variable handling when saving.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.experimental.VariablePolicy`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/VariablePolicy)

NONE No policy applied: Distributed variables are saved as one variable, with no device attached.

SAVE\_VARIABLE\_DEVICES When saving variables, also save their device assignment. This is useful if one wants to hardcode devices in saved models, but it also makes them non-portable if soft device placement is disabled (more details in [`tf.config.set_soft_device_placement`](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement)
). This is currently not fully supported by [`saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
, and is mainly intended to be used when one will be reading the saved model at a lower API level. In the example below, the graph saved by the call to [`saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
 will have the variable devices correctly specified:

  exported = tf.train.Checkpoint()
      with tf.device('/GPU:0'):
        exported.x_gpu = tf.Variable(1.0)
      with tf.device('/CPU:0'):
        exported.x_cpu = tf.Variable(1.0)
      tf.saved_model.save(exported, export_dir,
          options = tf.saved_model.SaveOptions(
              experimental_variable_policy=
                tf.saved_model.experimental.VariablePolicy.SAVE_VARIABLE_DEVICES))

Distributed variables are still saved as one variable under this policy.

EXPAND\_DISTRIBUTED\_VARIABLES Distributed variables will be saved with information about their components, allowing for their restoration on load. Also, the saved graph will contain references to those variables. This is useful when one wants to use the model for training in environments where the original distribution strategy is not available.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| EXPAND\_DISTRIBUTED\_VARIABLES | `<VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES: 'expand_distributed_variables'>` |
| NONE | `<VariablePolicy.NONE: None>` |
| SAVE\_VARIABLE\_DEVICES | `<VariablePolicy.SAVE_VARIABLE_DEVICES: 'save_variable_devices'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.