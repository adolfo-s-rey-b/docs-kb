[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/applications/NASNetMobile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/applications/NASNetMobile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/applications/NASNetMobile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fapplications%2FNASNetMobile&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/NASNetMobile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/NASNetMobile#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.applications.NASNetMobile Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/NASNetMobile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/NASNetMobile#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/nasnet.py#L314-L407)

Instantiates a Mobile NASNet model in ImageNet mode.

#### View aliases

**Main aliases**

[`tf.keras.applications.nasnet.NASNetMobile`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/NASNetMobile)

tf.keras.applications.NASNetMobile(
        input_shape=None,
        include_top=True,
        weights='imagenet',
        input_tensor=None,
        pooling=None,
        classes=1000,
        classifier_activation='softmax',
        name='nasnet_mobile'
    )

#### Reference:

*   [Learning Transferable Architectures for Scalable Image Recognition](https://arxiv.org/abs/1707.07012)
     (CVPR 2018)

Optionally loads weights pre-trained on ImageNet. Note that the data format convention used by the model is the one specified in your Keras config at `~/.keras/keras.json`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_shape` | Optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(224, 224, 3)` for NASNetMobile It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(224, 224, 3)` would be one valid value. |
| `include_top` | Whether to include the fully-connected layer at the top of the network. |
| `weights` | `None` (random initialization) or `imagenet` (ImageNet weights). For loading `imagenet` weights, `input_shape` should be (224, 224, 3) |
| `input_tensor` | Optional Keras tensor (i.e. output of [`layers.Input()`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)<br>) to use as image input for the model. |
| `pooling` | Optional pooling mode for feature extraction when `include_top` is `False`.<br><br>*   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.<br>*   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.<br>*   `max` means that global max pooling will be applied. |
| `classes` | Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. |
| `classifier_activation` | A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. |
| `name` | The name of the model (string). |

|     |
| --- |
| Returns<br>------- |     |
| A Keras model instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.