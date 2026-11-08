[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/remove_training_nodes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/remove_training_nodes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/remove_training_nodes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fgraph_util%2Fremove_training_nodes&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/remove_training_nodes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/remove_training_nodes#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.graph\_util.remove\_training\_nodes Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/remove_training_nodes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/remove_training_nodes#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/graph_util_impl.py#L279-L376)

Prunes out nodes that aren't needed for inference. (deprecated)

tf.compat.v1.graph_util.remove_training_nodes(
        input_graph, protected_nodes=None
    )

There are nodes like Identity and CheckNumerics that are only useful during training, and can be removed in graphs that will be used for nothing but inference. Here we identify and remove them, returning an equivalent graph. To be specific, CheckNumerics nodes are always removed, and Identity nodes that aren't involved in control edges are spliced out so that their input and outputs are directly connected.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_graph` | Model to analyze and prune. |
| `protected_nodes` | An optional list of names of nodes to be kept unconditionally. This is for example useful to preserve Identity output nodes. |

|     |
| --- |
| Returns<br>------- |     |
| A list of nodes with the unnecessary ones removed. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.