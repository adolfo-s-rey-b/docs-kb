[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/export#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/export)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/export?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/export#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/export#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.export\_base.export Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/export#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/export#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/export_base.py#L99-L149)

Exports to SavedModel format.

tfm.core.export_base.export(
        export_module: tfm.core.export_base.ExportModule,
        function_keys: Union[List[Text], Dict[Text, Text]],
        export_savedmodel_dir: Text,
        checkpoint_path: Optional[Text] = None,
        timestamped: bool = True,
        save_options: Optional[tf.saved_model.SaveOptions] = None,
        checkpoint: Optional[tf.train.Checkpoint] = None
    ) -> Text

|     |     |
| --- | --- |
| Args<br>---- |     |
| `export_module` | a ExportModule with the keras Model and serving tf.functions. |
| `function_keys` | a list of string keys to retrieve pre-defined serving signatures. The signaute keys will be set with defaults. If a dictionary is provided, the values will be used as signature keys. |
| `export_savedmodel_dir` | Output saved model directory. |
| `checkpoint_path` | Object-based checkpoint path or directory. |
| `timestamped` | Whether to export the savedmodel to a timestamped directory. |
| `save_options` | `SaveOptions` for [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)<br>. |
| `checkpoint` | An optional tf.train.Checkpoint. If provided, the export module will use it to read the weights. |

|     |
| --- |
| Returns<br>------- |     |
| The savedmodel directory path. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.