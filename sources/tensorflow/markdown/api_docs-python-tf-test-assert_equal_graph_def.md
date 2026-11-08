[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/assert_equal_graph_def#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/assert_equal_graph_def)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/assert_equal_graph_def?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/assert_equal_graph_def#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/test/assert_equal_graph_def#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.assert\_equal\_graph\_def Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/assert_equal_graph_def#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/test/assert_equal_graph_def#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L221-L241)

Asserts that two `GraphDef`s are (mostly) the same.

tf.test.assert_equal_graph_def(
        expected: tf.compat.v1.GraphDef,
        actual: tf.compat.v1.GraphDef
    ) -> None

Compares two `GraphDef` protos for equality, ignoring versions and ordering of nodes, attrs, and control inputs. Node names are used to match up nodes between the graphs, so the naming of nodes must be consistent. This function ignores randomized attribute values that may appear in V2 checkpoints.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `expected` | The `GraphDef` we expected. |
| `actual` | The `GraphDef` we have. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `AssertionError` | If the `GraphDef`s do not match. |
| `TypeError` | If either argument is not a `GraphDef`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.