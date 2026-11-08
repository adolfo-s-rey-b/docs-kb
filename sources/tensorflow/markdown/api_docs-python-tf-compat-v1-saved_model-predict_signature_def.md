[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.predict\_signature\_def Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/signature_def_utils_impl.py#L196-L234)

Creates prediction signature from given inputs and outputs.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.signature_def_utils.predict_signature_def`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def)

tf.compat.v1.saved_model.predict_signature_def(
        inputs, outputs
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model) |

This function produces signatures intended for use with the TensorFlow Serving Predict API (tensorflow\_serving/apis/prediction\_service.proto). This API imposes no constraints on the input and output types.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | dict of string to `Tensor`. |
| `outputs` | dict of string to `Tensor`. |

|     |
| --- |
| Returns<br>------- |     |
| A prediction-flavored signature\_def. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If inputs or outputs is `None`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.