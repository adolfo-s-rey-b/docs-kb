[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fget_collection_ref&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref#returns)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.get\_collection\_ref Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref#returns)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_collection_ref#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5479-L5500)

Wrapper for [`Graph.get_collection_ref()`](https://www.tensorflow.org/api_docs/python/tf/Graph#get_collection_ref)
 using the default graph.

tf.compat.v1.get_collection_ref(
        key
    ) -> list[Any]

See [`tf.Graph.get_collection_ref`](https://www.tensorflow.org/api_docs/python/tf/Graph#get_collection_ref)
 for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key` | The key for the collection. For example, the `GraphKeys` class contains many standard names for collections. |

|     |
| --- |
| Returns<br>------- |     |
| The list of values in the collection with the given `name`, or an empty list if no value has been added to that collection. Note that this returns the collection list itself, which can be modified in place to change the collection. |     |

eager compatibility
-------------------

Collections are not supported when eager execution is enabled.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.