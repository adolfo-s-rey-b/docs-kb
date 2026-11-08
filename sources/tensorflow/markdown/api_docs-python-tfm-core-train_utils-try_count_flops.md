[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_flops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_flops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_flops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_flops#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_flops#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.train\_utils.try\_count\_flops Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_flops#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_flops#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L522-L569)

Counts and returns model FLOPs.

tfm.core.train_utils.try_count_flops(
        model: Union[tf.Module, tf_keras.Model],
        inputs_kwargs: Optional[Dict[str, Any]] = None,
        output_path: Optional[str] = None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model` | A model instance. |
| `inputs_kwargs` | An optional dictionary of argument pairs specifying inputs' shape specifications to getting corresponding concrete function. |
| `output_path` | A file path to write the profiling results to. |

|     |
| --- |
| Returns<br>------- |     |
| The model's FLOPs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.