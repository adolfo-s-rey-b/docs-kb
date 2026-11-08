[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/read_file#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/read_file)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/read_file?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/read_file#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/read_file#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/read_file#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.read\_file Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/read_file#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/read_file#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/read_file#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L97-L134)

Reads the contents of file.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.read_file`](https://www.tensorflow.org/api_docs/python/tf/io/read_file)
, [`tf.compat.v1.read_file`](https://www.tensorflow.org/api_docs/python/tf/io/read_file)

tf.io.read_file(
        filename, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data) | *   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer) |

This operation returns a tensor with the entire contents of the input filename. It does not do any parsing, it just returns the contents as they are. Usually, this is the first step in the input pipeline.

#### Example:

    with open("/tmp/file.txt", "w") as f:

Example of using the op in a function to read an image, decode it and reshape the tensor containing the pixel data:

    @tf.function

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filename` | string. filename to read from. |
| `name` | string. Optional name for the op. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of dtype "string", with the file contents. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.