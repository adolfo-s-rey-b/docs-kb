[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.concatenate Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/concatenate#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/merging/concatenate.py#L166-L178)

Functional interface to the `Concatenate` layer.

tf.keras.layers.concatenate(
        inputs, axis=-1, **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Classify structured data using Keras preprocessing layers](https://www.tensorflow.org/tutorials/structured_data/preprocessing_layers)<br>    <br>*   [Streaming structured data from Elasticsearch using Tensorflow-IO](https://www.tensorflow.org/io/tutorials/elasticsearch)<br>    <br>*   [Tensorflow datasets from MongoDB collections](https://www.tensorflow.org/io/tutorials/mongodb)<br>    <br>*   [Quantum Convolutional Neural Network](https://www.tensorflow.org/quantum/tutorials/qcnn) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A list of input tensors. |
| `axis` | Concatenation axis. |
| `**kwargs` | Standard layer keyword arguments. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor, the concatenation of the inputs alongside axis `axis`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.