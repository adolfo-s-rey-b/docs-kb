[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fgraph_util%2Fconvert_variables_to_constants&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.graph\_util.convert\_variables\_to\_constants Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/convert_to_constants.py#L1295-L1336)

Replaces all the variables in a graph with constants of the same values. (deprecated)

tf.compat.v1.graph_util.convert_variables_to_constants(
        sess,
        input_graph_def,
        output_node_names,
        variable_names_whitelist=None,
        variable_names_blacklist=None
    )

If you have a trained graph containing Variable ops, it can be convenient to convert them all to Const ops holding the same values. This makes it possible to describe the network fully with a single GraphDef file, and allows the removal of a lot of ops related to loading and saving the variables.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sess` | Active TensorFlow session containing the variables. |
| `input_graph_def` | GraphDef object holding the network. |
| `output_node_names` | List of name strings for the result nodes of the graph. |
| `variable_names_whitelist` | The set of variable names to convert (by default, all variables are converted). |
| `variable_names_blacklist` | The set of variable names to omit converting to constants. |

|     |
| --- |
| Returns<br>------- |     |
| GraphDef containing a simplified version of the original. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | if a DT\_RESOURCE op is found whose ancestor Variables are both denylisted AND whitelisted for freezing. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.