[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/convert_variables_to_constants_v2_as_graph#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/convert_variables_to_constants_v2_as_graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/convert_variables_to_constants_v2_as_graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/convert_variables_to_constants_v2_as_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/convert_variables_to_constants_v2_as_graph#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.train\_utils.convert\_variables\_to\_constants\_v2\_as\_graph Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/convert_variables_to_constants_v2_as_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/convert_variables_to_constants_v2_as_graph#returns)
    

Replaces all the variables in a graph with constants of the same values.

tfm.core.train_utils.convert_variables_to_constants_v2_as_graph(
        func, lower_control_flow=True, aggressive_inlining=False
    )

This function works as same as convert\_variables\_to\_constants\_v2, but it returns the intermediate `GraphDef` as well. This `GraphDef` contains all the debug information after all the transformations in the frozen phase.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | ConcreteFunction. |
| `lower_control_flow` | Boolean indicating whether or not to lower control flow ops such as If and While. (default True) |
| `aggressive_inlining` | Boolean indicating whether or not to do aggressive function inlining (might be unsafe if function has stateful ops, not properly connected to control outputs). |

|     |
| --- |
| Returns<br>------- |     |
| ConcreteFunction containing a simplified version of the original, and also the intermediate GraphDef containing the node debug information for the transformations in the frozen phase. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.