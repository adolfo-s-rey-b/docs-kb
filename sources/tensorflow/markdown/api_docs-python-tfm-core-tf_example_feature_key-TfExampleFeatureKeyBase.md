[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.tf\_example\_feature\_key.TfExampleFeatureKeyBase Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_feature_key/TfExampleFeatureKeyBase#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_feature_key.py#L28-L62)

Base dataclass for defining tf.Example proto feature keys.

tfm.core.tf_example_feature_key.TfExampleFeatureKeyBase(
        prefix: Optional[str] = None
    )

This class defines the logic of adding prefix to feature keys. Subclasses will define feature keys for a specific feature type in data fields.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `prefix` | A prefix string that will be added before the feature key string with a trailing slash '/'. |

Methods
-------

### `__eq__`

__eq__(
        other
    )

Return self==value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.