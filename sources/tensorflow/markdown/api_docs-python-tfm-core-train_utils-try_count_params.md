[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_params#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_params)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_params?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fcore%2Ftrain_utils%2Ftry_count_params&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_params#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_params#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.train\_utils.try\_count\_params Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_params#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_params#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L491-L519)

Count the number of parameters if model is possible.

tfm.core.train_utils.try_count_params(
        model: Union[tf.Module, tf_keras.Model], trainable_only: bool = False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model` | Try to count the number of params in this model. |
| `trainable_only` | Whether to calculate trainable params only. This flag is not used when the model has `count_params` attribute. |

|     |
| --- |
| Returns<br>------- |     |
| The number of parameters or None. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.