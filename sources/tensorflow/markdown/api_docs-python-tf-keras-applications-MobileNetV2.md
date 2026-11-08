[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.applications.MobileNetV2 Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/mobilenet_v2.py#L16-L392)

Instantiates the MobileNetV2 architecture.

#### View aliases

**Main aliases**

[`tf.keras.applications.mobilenet_v2.MobileNetV2`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2)

tf.keras.applications.MobileNetV2(
        input_shape=None,
        alpha=1.0,
        include_top=True,
        weights='imagenet',
        input_tensor=None,
        pooling=None,
        classes=1000,
        classifier_activation='softmax',
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Estimators](https://www.tensorflow.org/guide/estimator) | *   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)<br>    <br>*   [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)<br>    <br>*   [Transfer learning and fine-tuning](https://www.tensorflow.org/tutorials/images/transfer_learning) |

MobileNetV2 is very similar to the original MobileNet, except that it uses inverted residual blocks with bottlenecking features. It has a drastically lower parameter count than the original MobileNet. MobileNets support any input size greater than 32 x 32, with larger image sizes offering better performance.

#### Reference:

*   [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381)
     (CVPR 2018)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_shape` | Optional shape tuple, only to be specified if `include_top` is `False` (otherwise the input shape has to be `(224, 224, 3)` (with `"channels_last"` data format) or `(3, 224, 224)` (with `"channels_first"` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(200, 200, 3)` would be one valid value. Defaults to `None`. `input_shape` will be ignored if the `input_tensor` is provided. |
| `alpha` | Controls the width of the network. This is known as the width multiplier in the MobileNet paper.<br><br>*   If `alpha < 1.0`, proportionally decreases the number of filters in each layer.<br>*   If `alpha > 1.0`, proportionally increases the number of filters in each layer.<br>*   If `alpha == 1`, default number of filters from the paper are used at each layer. Defaults to `1.0`. |
| `include_top` | Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`. |
| `weights` | One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`. |
| `input_tensor` | Optional Keras tensor (i.e. output of [`layers.Input()`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)<br>) to use as image input for the model. `input_tensor` is useful for sharing inputs between multiple different networks. Defaults to `None`. |
| `pooling` | Optional pooling mode for feature extraction when `include_top` is `False`.*   `None` (default) means that the output of the model will be the 4D tensor output of the last convolutional block.<br>*   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.<br>*   `max` means that global max pooling will be applied. |
| `classes` | Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to `1000`. |
| `classifier_activation` | A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. |
| `name` | String, the name of the model. |

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