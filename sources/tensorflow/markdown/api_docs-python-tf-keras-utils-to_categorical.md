[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.to\_categorical Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/numerical_utils.py#L38-L101)

Converts a class vector (integers) to binary class matrix.

tf.keras.utils.to_categorical(
        x, num_classes=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Implement Differential Privacy with TensorFlow Privacy](https://www.tensorflow.org/responsible_ai/privacy/tutorials/classification_privacy)<br>    <br>*   [Assess privacy risks with the TensorFlow Privacy Report](https://www.tensorflow.org/responsible_ai/privacy/tutorials/privacy_report)<br>    <br>*   [On-Device Training with TensorFlow Lite](https://www.tensorflow.org/lite/examples/on_device_training/overview)<br>    <br>*   [Human Pose Classification with MoveNet and TensorFlow Lite](https://www.tensorflow.org/lite/tutorials/pose_classification)<br>    <br>*   [Classifying CIFAR-10 with XLA](https://www.tensorflow.org/xla/tf2xla/tutorials/autoclustering_xla) |

E.g. for use with `categorical_crossentropy`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Array-like with class values to be converted into a matrix (integers from 0 to `num_classes - 1`). |
| `num_classes` | Total number of classes. If `None`, this would be inferred as `max(x) + 1`. Defaults to `None`. |

|     |
| --- |
| Returns<br>------- |     |
| A binary matrix representation of the input as a NumPy array. The class axis is placed last. |     |

#### Example:

    a = keras.utils.to_categorical([0, 1, 2, 3], num_classes=4)

    b = np.array([.9, .04, .03, .03,\
\
    loss = keras.ops.categorical_crossentropy(a, a)\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.