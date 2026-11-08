[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/applications/convnext/preprocess_input#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/applications/convnext/preprocess_input)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/applications/convnext/preprocess_input?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fapplications%2Fconvnext%2Fpreprocess_input&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/convnext/preprocess_input#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/convnext/preprocess_input#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.applications.convnext.preprocess\_input Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/convnext/preprocess_input#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/convnext/preprocess_input#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/convnext.py#L762-L781)

A placeholder method for backward compatibility.

tf.keras.applications.convnext.preprocess_input(
        x, data_format=None
    )

The preprocessing logic has been included in the convnext model implementation. Users are no longer required to call this method to normalize the input data. This method does nothing and only kept as a placeholder to align the API surface between old and new version of model.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A floating point [`numpy.array`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array)<br> or a tensor. |
| `data_format` | Optional data format of the image tensor/array. Defaults to None, in which case the global setting [`keras.backend.image_data_format()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br> is used (unless you changed it, it defaults to `"channels_last"`).{mode} |

|     |
| --- |
| Returns<br>------- |     |
| Unchanged [`numpy.array`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array)<br> or tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.