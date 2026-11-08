[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.actions.ExportSavedModel Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/export_saved_model.py#L138-L164)

Action that exports the given model as a SavedModel.

orbit.actions.ExportSavedModel(
        model: tf.Module,
        file_manager: orbit.actions.ExportFileManager,
        signatures,
        options: Optional[tf.saved_model.SaveOptions] = None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model` | The model to export. |
| `file_manager` | An instance of `ExportFileManager` (or a subclass), that provides file naming and cleanup functionality. |
| `signatures` | The signatures to forward to [`tf.saved_model.save()`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)<br>. |
| `options` | Optional options to forward to [`tf.saved_model.save()`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)<br>. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/export_saved_model.py#L160-L164)

__call__(
        _
    )

Exports the SavedModel.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.