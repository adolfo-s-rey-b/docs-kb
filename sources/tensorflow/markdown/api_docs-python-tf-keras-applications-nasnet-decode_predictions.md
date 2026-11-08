[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fapplications%2Fnasnet%2Fdecode_predictions&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.applications.nasnet.decode\_predictions Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/applications/nasnet/decode_predictions#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/nasnet.py#L859-L861)

Decodes the prediction of an ImageNet model.

tf.keras.applications.nasnet.decode_predictions(
        preds, top=5
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `preds` | NumPy array encoding a batch of predictions. |
| `top` | Integer, how many top-guesses to return. Defaults to `5`. |

|     |
| --- |
| Returns<br>------- |     |
| A list of lists of top class prediction tuples `(class_name, class_description, score)`. One list of tuples per sample in batch input. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | In case of invalid shape of the `pred` array (must be 2D). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.