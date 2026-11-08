[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/traverse#main-content)

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
    

tf.keras.tree.traverse Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L55-L105)

Traverses the given nested structure, applying the given function.

tf.keras.tree.traverse(
        func, structure, top_down=True
    )

The traversal is depth-first. If `top_down` is True (default), parents are returned before their children (giving the option to avoid traversing into a sub-tree).

#### Examples:

    v = []

    v = []

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | The function to be applied to each sub-nest of the structure.<br><br>When traversing top-down: If `func(subtree) is None` the traversal continues into the sub-tree. If `func(subtree) is not None` the traversal does not continue into the sub-tree. The sub-tree will be replaced by `func(subtree)` in the returned structure (to replace the sub-tree with `None`, use the special value `MAP_TO_NONE`).<br><br>When traversing bottom-up: If `func(subtree) is None` the traversed sub-tree is returned unaltered. If `func(subtree) is not None` the sub-tree will be replaced by `func(subtree)` in the returned structure (to replace the sub-tree with None, use the special value `MAP_TO_NONE`). |
| `structure` | The structure to traverse. |
| `top_down` | If True, parent structures will be visited before their children. |

|     |
| --- |
| Returns<br>------- |     |
| The structured output from the traversal. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `func` is not callable. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.