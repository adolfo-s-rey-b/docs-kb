[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/model_to_dot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/model_to_dot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/model_to_dot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2Fmodel_to_dot&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/model_to_dot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/model_to_dot#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.model\_to\_dot Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/model_to_dot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/model_to_dot#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/model_visualization.py#L194-L406)

Convert a Keras model to dot format.

tf.keras.utils.model_to_dot(
        model,
        show_shapes=False,
        show_dtype=False,
        show_layer_names=True,
        rankdir='TB',
        expand_nested=False,
        dpi=200,
        subgraph=False,
        show_layer_activations=False,
        show_trainable=False,
        splines='ortho',
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model` | A Keras model instance. |
| `show_shapes` | whether to display shape information. |
| `show_dtype` | whether to display layer dtypes. |
| `show_layer_names` | whether to display layer names. |
| `rankdir` | `rankdir` argument passed to PyDot, a string specifying the format of the plot: `"TB"` creates a vertical plot; `"LR"` creates a horizontal plot. |
| `expand_nested` | whether to expand nested Functional models into clusters. |
| `dpi` | Image resolution in dots per inch. |
| `subgraph` | whether to return a `pydot.Cluster` instance. |
| `show_layer_activations` | Display layer activations (only for layers that have an `activation` property). |
| `show_trainable` | whether to display if a layer is trainable. |
| `splines` | Controls how edges are drawn. Defaults to `"ortho"` (right-angle lines). Other options include `"curved"`, `"polyline"`, `"spline"`, and `"line"`. |

|     |
| --- |
| Returns<br>------- |     |
| A `pydot.Dot` instance representing the Keras model or a `pydot.Cluster` instance representing nested model if `subgraph=True`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.