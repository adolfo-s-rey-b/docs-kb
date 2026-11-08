[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.applications.InceptionV3 Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/inception_v3.py#L19-L380)

Instantiates the Inception v3 architecture.

#### View aliases

**Main aliases**

[`tf.keras.applications.inception_v3.InceptionV3`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3)

tf.keras.applications.InceptionV3(
        include_top=True,
        weights='imagenet',
        input_tensor=None,
        input_shape=None,
        pooling=None,
        classes=1000,
        classifier_activation='softmax',
        name='inception_v3'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream) |

#### Reference:

*   [Rethinking the Inception Architecture for Computer Vision](http://arxiv.org/abs/1512.00567)
     (CVPR 2016)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `include_top` | Boolean, whether to include the fully-connected layer at the top, as the last layer of the network. Defaults to `True`. |
| `weights` | One of `None` (random initialization), `imagenet` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`. |
| `input_tensor` | Optional Keras tensor (i.e. output of [`layers.Input()`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)<br>) to use as image input for the model. `input_tensor` is useful for sharing inputs between multiple different networks. Defaults to `None`. |
| `input_shape` | Optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(299, 299, 3)` (with `channels_last` data format) or `(3, 299, 299)` (with `channels_first` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 75. E.g. `(150, 150, 3)` would be one valid value. `input_shape` will be ignored if the `input_tensor` is provided. |
| `pooling` | Optional pooling mode for feature extraction when `include_top` is `False`.<br><br>*   `None` (default) means that the output of the model will be the 4D tensor output of the last convolutional block.<br>*   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.<br>*   `max` means that global max pooling will be applied. |
| `classes` | optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000. |
| `classifier_activation` | A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. |
| `name` | The name of the model (string). |

|     |
| --- |
| Returns<br>------- |     |
| A model instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.