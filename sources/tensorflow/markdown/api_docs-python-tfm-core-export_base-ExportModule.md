[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#methods)
    *   [get\_inference\_signatures](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#get_inference_signatures)
        
    *   [serve](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#serve)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.export\_base.ExportModule Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#methods)
    *   [get\_inference\_signatures](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#get_inference_signatures)
        
    *   [serve](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule#serve)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/export_base.py#L28-L96)

Base Export Module.

tfm.core.export_base.ExportModule(
        params,
        model: Union[tf.Module, tf_keras.Model],
        inference_step: Optional[Callable[..., Any]] = None,
        *,
        preprocessor: Optional[Callable[..., Any]] = None,
        postprocessor: Optional[Callable[..., Any]] = None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | A dataclass for parameters to the module. |
| `model` | A model instance which contains weights and forward computation. |
| `inference_step` | An optional callable to forward-pass the model. If not specified, it creates a parital function with `model` as an required kwarg. |
| `preprocessor` | An optional callable to preprocess the inputs. |
| `postprocessor` | An optional callable to postprocess the model outputs. |

Methods
-------

### `get_inference_signatures`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/export_base.py#L93-L96)

@abc.abstractmethod

Get defined function signatures.

### `serve`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/export_base.py#L85-L91)

@abc.abstractmethod

The bare inference function which should run on all devices.

Expecting tensors are passed in through keyword arguments. Returns a dictionary of tensors, when the keys will be used inside the SignatureDef.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.