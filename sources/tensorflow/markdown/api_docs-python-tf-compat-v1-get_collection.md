[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#returns)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.get\_collection Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#returns)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5503-L5529)

Wrapper for [`Graph.get_collection()`](https://www.tensorflow.org/api_docs/python/tf/Graph#get_collection)
 using the default graph.

tf.compat.v1.get_collection(
        key, scope=None
    ) -> list[Any]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Validating correctness & numerical equivalence](https://www.tensorflow.org/guide/migrate/validate_correctness) | *   [Generating Images with BigBiGAN](https://www.tensorflow.org/hub/tutorials/bigbigan_with_tf_hub)<br>    <br>*   [Classify Flowers with Transfer Learning](https://www.tensorflow.org/hub/tutorials/image_feature_vector) |

See [`tf.Graph.get_collection`](https://www.tensorflow.org/api_docs/python/tf/Graph#get_collection)
 for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key` | The key for the collection. For example, the `GraphKeys` class contains many standard names for collections. |
| `scope` | (Optional.) If supplied, the resulting list is filtered to include only items whose `name` attribute matches using `re.match`. Items without a `name` attribute are never returned if a scope is supplied and the choice or `re.match` means that a `scope` without special tokens filters by prefix. |

|     |
| --- |
| Returns<br>------- |     |
| The list of values in the collection with the given `name`, or an empty list if no value has been added to that collection. The list contains the values in the order under which they were collected. |     |

eager compatibility
-------------------

Collections are not supported when eager execution is enabled.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.