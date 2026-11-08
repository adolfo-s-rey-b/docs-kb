[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_to_collections#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_to_collections)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_to_collections?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_to_collections#args)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_to_collections#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.add\_to\_collections Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_to_collections#args)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_to_collections#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5459-L5476)

Wrapper for [`Graph.add_to_collections()`](https://www.tensorflow.org/api_docs/python/tf/Graph#add_to_collections)
 using the default graph.

tf.compat.v1.add_to_collections(
        names, value
    ) -> None

See [`tf.Graph.add_to_collections`](https://www.tensorflow.org/api_docs/python/tf/Graph#add_to_collections)
 for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `names` | The key for the collections. The `GraphKeys` class contains many standard names for collections. |
| `value` | The value to add to the collections. |

eager compatibility
-------------------

Collections are only supported in eager when variables are created inside an EagerVariableStore (e.g. as part of a layer or template).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.