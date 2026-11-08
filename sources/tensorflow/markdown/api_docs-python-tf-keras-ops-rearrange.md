[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rearrange#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rearrange)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rearrange?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Frearrange&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rearrange#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rearrange#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.rearrange Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rearrange#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rearrange#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/einops.py#L106-L189)

Rearranges the axes of a Keras tensor according to a specified pattern, einops-style.

tf.keras.ops.rearrange(
        tensor, pattern, **axes_lengths
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | Input Keras tensor. |
| `pattern` | String describing the rearrangement in einops notation. |
| `**axes_lengths` | Keyword arguments specifying lengths of axes when axes decomposition is used. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `Tensor` | A Keras tensor with rearranged axes. |

#### Follows the logic of:

1.  If decomposition is needed, reshape to match decomposed dimensions.
2.  Permute known and inferred axes to match the form of the output.
3.  Reshape to match the desired output shape.

#### Example Usage:

> > > import numpy as np from keras.ops import rearrange images = np.random.rand(32, 30, 40, 3) # BHWC format

# Reordering to BCHW

> > > rearrange(images, 'b h w c -> b c h w').shape TensorShape(\[32, 3, 30, 40\])

# "Merge" along first axis - concat images from a batch

> > > rearrange(images, 'b h w c -> (b h) w c').shape TensorShape(\[960, 40, 3\])

# "Merge" along second axis - concat images horizontally

> > > rearrange(images, 'b h w c -> h (b w) c').shape TensorShape(\[30, 1280, 3\])

# Flatten images into a CHW vector

> > > rearrange(images, 'b h w c -> b (c h w)').shape TensorShape(\[32, 3600\])

# Decompose H and W axes into 4 smaller patches

> > > rearrange(images, 'b (h1 h) (w1 w) c -> (b h1 w1) h w c', h1=2, w1=2).shape TensorShape(\[128, 15, 20, 3\])

# Space-to-depth decomposition of input axes

> > > rearrange(images, 'b (h h1) (w w1) c -> b h w (c h1 w1)', h1=2, w1=2).shape TensorShape(\[32, 15, 20, 12\])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.