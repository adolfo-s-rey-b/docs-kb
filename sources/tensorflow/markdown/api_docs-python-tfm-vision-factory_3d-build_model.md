[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d/build_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d/build_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d/build_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Ffactory_3d%2Fbuild_model&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d/build_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d/build_model#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.factory\_3d.build\_model Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d/build_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d/build_model#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/factory_3d.py#L55-L76)

Builds backbone from a config.

tfm.vision.factory_3d.build_model(
        model_type: str,
        input_specs: tf_keras.layers.InputSpec,
        model_config: tfm.hyperparams.Config,
        num_classes: int,
        l2_regularizer: tf_keras.regularizers.Regularizer = None
    ) -> tf_keras.Model

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model_type` | string name of model type. It should be consistent with ModelConfig.model\_type. |
| `input_specs` | tf\_keras.layers.InputSpec. |
| `model_config` | a OneOfConfig. Model config. |
| `num_classes` | number of classes. |
| `l2_regularizer` | tf\_keras.regularizers.Regularizer instance. Default to None. |

|     |
| --- |
| Returns<br>------- |     |
| tf\_keras.Model instance of the backbone. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.