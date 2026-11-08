[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#args)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#methods)
    *   [get\_inference\_signatures](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#get_inference_signatures)
        
    *   [serve](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#serve)
        
    *   [serve\_examples](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#serve_examples)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.serving\_modules.MaskedLM Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#args)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#methods)
    *   [get\_inference\_signatures](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#get_inference_signatures)
        
    *   [serve](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#serve)
        
    *   [serve\_examples](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM#serve_examples)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/serving/serving_modules.py#L188-L261)

The export module for the Bert Pretrain (MaskedLM) task.

Inherits From: [`ExportModule`](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule)

tfm.nlp.serving_modules.MaskedLM(
        params, model: tf_keras.Model, inference_step=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | A dataclass for parameters to the module. |
| `model` | A model instance which contains weights and forward computation. |
| `inference_step` | An optional callable to forward-pass the model. If not specified, it creates a parital function with `model` as an required kwarg. |
| `preprocessor` | An optional callable to preprocess the inputs. |
| `postprocessor` | An optional callable to postprocess the model outputs. |

Child Classes
-------------

[`class Params`](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM/Params)

Methods
-------

### `get_inference_signatures`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/serving/serving_modules.py#L240-L261)

get_inference_signatures(
        function_keys: Dict[Text, Text]
    )

Get defined function signatures.

### `serve`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/serving/serving_modules.py#L207-L216)

@tf.function

### `serve_examples`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/serving/serving_modules.py#L218-L238)

@tf.function

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.