[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fapplications%2FMobileNetV3Small&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#used-in-the-notebooks)
    
*   [The following table describes the performance of MobileNets v3:](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#the_following_table_describes_the_performance_of_mobilenets_v3)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#call-arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.applications.MobileNetV3Small Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#used-in-the-notebooks)
    
*   [The following table describes the performance of MobileNets v3:](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#the_following_table_describes_the_performance_of_mobilenets_v3)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#call-arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Small#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/mobilenet_v3.py#L406-L470)

Instantiates the MobileNetV3Small architecture.

tf.keras.applications.MobileNetV3Small(
        input_shape=None,
        alpha=1.0,
        minimalistic=False,
        include_top=True,
        weights='imagenet',
        input_tensor=None,
        classes=1000,
        pooling=None,
        dropout_rate=0.2,
        classifier_activation='softmax',
        include_preprocessing=True,
        name='MobileNetV3Small'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image captioning with visual attention](https://www.tensorflow.org/text/tutorials/image_captioning) |

#### Reference:

*   [Searching for MobileNetV3](https://arxiv.org/pdf/1905.02244.pdf)
     (ICCV 2019)

The following table describes the performance of MobileNets v3:
---------------------------------------------------------------

MACs stands for Multiply Adds

| Classification Checkpoint | MACs(M) | Parameters(M) | Top1 Accuracy | Pixel1 CPU(ms) |
| --- | --- | --- | --- | --- |
| mobilenet\_v3\_large\_1.0\_224 | 217 | 5.4 | 75.6 | 51.2 |
| mobilenet\_v3\_large\_0.75\_224 | 155 | 4.0 | 73.3 | 39.8 |
| mobilenet\_v3\_large\_minimalistic\_1.0\_224 | 209 | 3.9 | 72.3 | 44.1 |
| mobilenet\_v3\_small\_1.0\_224 | 66  | 2.9 | 68.1 | 15.8 |
| mobilenet\_v3\_small\_0.75\_224 | 44  | 2.4 | 65.4 | 12.8 |
| mobilenet\_v3\_small\_minimalistic\_1.0\_224 | 65  | 2.0 | 61.9 | 12.2 |

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_shape` | Optional shape tuple, to be specified if you would like to use a model with an input image resolution that is not `(224, 224, 3)`. It should have exactly 3 inputs channels. You can also omit this option if you would like to infer input\_shape from an input\_tensor. If you choose to include both input\_tensor and input\_shape then input\_shape will be used if they match, if the shapes do not match then we will throw an error. E.g. `(160, 160, 3)` would be one valid value. |
| `alpha` | controls the width of the network. This is known as the depth multiplier in the MobileNetV3 paper, but the name is kept for consistency with MobileNetV1 in Keras. When `weights` is `imagenet`, `alpha` can be one of `0.75` or `1.0` for non-minimalistic models, and `1.0` for minimalistic models.<br><br>*   If `alpha < 1.0`, proportionally decreases the number of filters in each layer.<br>*   If `alpha > 1.0`, proportionally increases the number of filters in each layer.<br>*   If `alpha == 1`, default number of filters from the paper are used at each layer. |
| `minimalistic` | In addition to large and small models this module also contains so-called minimalistic models, these models have the same per-layer dimensions characteristic as MobilenetV3 however, they don't utilize any of the advanced blocks (squeeze-and-excite units, hard-swish, and 5x5 convolutions). While these models are less efficient on CPU, they are much more performant on GPU/DSP. |
| `include_top` | Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`. |
| `weights` | String, one of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. |
| `input_tensor` | Optional Keras tensor (i.e. output of [`layers.Input()`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)<br>) to use as image input for the model. |
| `pooling` | String, optional pooling mode for feature extraction when `include_top` is `False`.*   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.<br>*   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.<br>*   `max` means that global max pooling will be applied. |
| `classes` | Integer, optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. |
| `dropout_rate` | fraction of the input units to drop on the last layer. |
| `classifier_activation` | A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. |
| `include_preprocessing` | Boolean, whether to include the preprocessing layer (`Rescaling`) at the bottom of the network. Defaults to `True`. |
| `name` | String, the name of the model. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | A floating point [`numpy.array`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array)<br> or backend-native tensor, 4D with 3 color channels, with values in the range `[0, 255]` if `include_preprocessing` is `True` and in the range `[-1, 1]` otherwise. |

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