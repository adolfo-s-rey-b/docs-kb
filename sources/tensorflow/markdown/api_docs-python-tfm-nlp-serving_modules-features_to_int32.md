[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/features_to_int32#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/features_to_int32)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/features_to_int32?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Fserving_modules%2Ffeatures_to_int32&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/features_to_int32#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/features_to_int32#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Was this helpful?

tfm.nlp.serving\_modules.features\_to\_int32 Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/features_to_int32#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/features_to_int32#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/serving/serving_modules.py#L28-L45)

Converts tf.int64 features to tf.int32, keep other features the same.

tfm.nlp.serving_modules.features_to_int32(
        features: Dict[str, tf.Tensor]
    ) -> Dict[str, tf.Tensor]

tf.Example only supports tf.int64, but the TPU only supports tf.int32.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | Input tensor dictionary. |

|     |
| --- |
| Returns<br>------- |     |
| Features with tf.int64 converted to tf.int32. |     |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.