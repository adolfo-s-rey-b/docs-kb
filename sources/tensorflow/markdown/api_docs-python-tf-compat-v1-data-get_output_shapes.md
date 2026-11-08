[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/get_output_shapes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.data.get\_output\_shapes Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L4464-L4483)

Returns the output shapes for elements of the input dataset / iterator.

tf.compat.v1.data.get_output_shapes(
        dataset_or_iterator
    )

Migrate to TF2
--------------

This is a legacy API for inspecting the type signature of dataset elements. In TF 2, you should use the [`tf.data.Dataset.element_spec`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#element_spec)
 attribute instead.

Description
-----------

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset_or_iterator` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> or [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| A (nested) structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> objects matching the structure of the dataset / iterator elements and specifying the shape of the individual components. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.