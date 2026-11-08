[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconfig%2Foptimizer%2Fset_experimental_options&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.optimizer.set\_experimental\_options Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L218-L258)

Set experimental optimizer options.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.optimizer.set_experimental_options`](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options)

tf.config.optimizer.set_experimental_options(
        options
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [TensorFlow graph optimization with Grappler](https://www.tensorflow.org/guide/graph_optimization) |

Note that optimizations are only applied in graph mode, (within tf.function). In addition, as these are experimental options, the list is subject to change.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `options` | Dictionary of experimental optimizer options to configure. Valid keys:<br><br>*   layout\_optimizer: Optimize tensor layouts e.g. This will try to use NCHW layout on GPU which is faster.<br>*   constant\_folding: Fold constants Statically infer the value of tensors when possible, and materialize the result using constants.<br>*   shape\_optimization: Simplify computations made on shapes.<br>*   remapping: Remap subgraphs onto more efficient implementations.<br>*   arithmetic\_optimization: Simplify arithmetic ops with common sub-expression elimination and arithmetic simplification.<br>*   dependency\_optimization: Control dependency optimizations. Remove redundant control dependencies, which may enable other optimization. This optimizer is also essential for pruning Identity and NoOp nodes.<br>*   loop\_optimization: Loop optimizations.<br>*   function\_optimization: Function optimizations and inlining.<br>*   debug\_stripper: Strips debug-related nodes from the graph.<br>*   disable\_model\_pruning: Disable removal of unnecessary ops from the graph<br>*   scoped\_allocator\_optimization: Try to allocate some independent Op outputs contiguously in order to merge or eliminate downstream Ops.<br>*   pin\_to\_host\_optimization: Force small ops onto the CPU.<br>*   implementation\_selector: Enable the swap of kernel implementations based on the device placement.<br>*   auto\_mixed\_precision: Change certain float32 ops to float16 on Volta GPUs and above; and on CPUs with AMX FP16 support. Without the use of loss scaling, this can cause numerical underflow (see `keras.mixed_precision.experimental.LossScaleOptimizer`).<br>*   disable\_meta\_optimizer: Disable the entire meta optimizer.<br>*   min\_graph\_nodes: The minimum number of nodes in a graph to optimizer. For smaller graphs, optimization is skipped.<br>*   auto\_parallel: Automatically parallelizes graphs by splitting along the batch dimension |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.