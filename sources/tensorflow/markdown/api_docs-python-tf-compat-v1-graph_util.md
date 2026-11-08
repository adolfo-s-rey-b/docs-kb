[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.graph\_util Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util#functions)
    

Public API for tf.\_api.v2.graph\_util namespace

Functions
---------

[`convert_variables_to_constants(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/convert_variables_to_constants)
: Replaces all the variables in a graph with constants of the same values. (deprecated)

[`extract_sub_graph(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/extract_sub_graph)
: Extract the subgraph that can reach any of the nodes in 'dest\_nodes'. (deprecated)

[`import_graph_def(...)`](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def)
: Imports the graph from `graph_def` into the current default `Graph`. (deprecated arguments)

[`must_run_on_cpu(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/must_run_on_cpu)
: Returns True if the given node\_def must run on CPU, otherwise False. (deprecated)

[`remove_training_nodes(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/remove_training_nodes)
: Prunes out nodes that aren't needed for inference. (deprecated)

[`tensor_shape_from_node_def_name(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/tensor_shape_from_node_def_name)
: Convenience function to get a shape from a NodeDef's input string. (deprecated)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.