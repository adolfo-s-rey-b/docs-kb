[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.unpack\_x\_y\_sample\_weight Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/data_adapters/data_adapter_utils.py#L11-L51)

Unpacks user-provided data tuple.

tf.keras.utils.unpack_x_y_sample_weight(
        data
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Integrating MinDiff without MinDiffModel](https://www.tensorflow.org/responsible_ai/model_remediation/min_diff/guide/integrating_min_diff_without_min_diff_model)<br>    <br>*   [Creating a custom Counterfactual Logit Pairing Dataset](https://www.tensorflow.org/responsible_ai/model_remediation/counterfactual/guide/creating_a_custom_counterfactual_dataset) |

This is a convenience utility to be used when overriding [`Model.train_step`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#train_step)
, [`Model.test_step`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#test_step)
, or [`Model.predict_step`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#predict_step)
. This utility makes it easy to support data of the form `(x,)`, `(x, y)`, or `(x, y, sample_weight)`.

#### Example:

    features_batch = ops.ones((10, 5))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A tuple of the form `(x,)`, `(x, y)`, or `(x, y, sample_weight)`. |

|     |
| --- |
| Returns<br>------- |     |
| The unpacked tuple, with `None`s for `y` and `sample_weight` if they are not provided. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.