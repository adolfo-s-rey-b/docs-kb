[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.plot\_model Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/model_visualization.py#L409-L529)

Converts a Keras model to dot format and save to a file.

tf.keras.utils.plot_model(
        model,
        to_file='model.png',
        show_shapes=False,
        show_dtype=False,
        show_layer_names=False,
        rankdir='TB',
        expand_nested=False,
        dpi=200,
        show_layer_activations=False,
        show_trainable=False,
        splines='ortho',
        **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Load a pandas DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)<br>    <br>*   [Load text](https://www.tensorflow.org/tutorials/load_data/text)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation) |

#### Example:

inputs = ...
    outputs = ...
    model = keras.Model(inputs=inputs, outputs=outputs)
    
    dot_img_file = '/tmp/model_1.png'
    keras.utils.plot_model(model, to_file=dot_img_file, show_shapes=True)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model` | A Keras model instance |
| `to_file` | File name of the plot image. |
| `show_shapes` | whether to display shape information. |
| `show_dtype` | whether to display layer dtypes. |
| `show_layer_names` | whether to display layer names. |
| `rankdir` | `rankdir` argument passed to PyDot, a string specifying the format of the plot: `"TB"` creates a vertical plot; `"LR"` creates a horizontal plot. |
| `expand_nested` | whether to expand nested Functional models into clusters. |
| `dpi` | Image resolution in dots per inch. |
| `show_layer_activations` | Display layer activations (only for layers that have an `activation` property). |
| `show_trainable` | whether to display if a layer is trainable. |
| `splines` | Controls how edges are drawn. Defaults to `"ortho"` (right-angle lines). Other options include `"curved"`, `"polyline"`, `"spline"`, and `"line"`. |

|     |
| --- |
| Returns<br>------- |     |
| A Jupyter notebook Image object if Jupyter is installed. This enables in-line display of the model plots in notebooks. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.