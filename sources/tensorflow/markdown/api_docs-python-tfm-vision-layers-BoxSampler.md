[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.BoxSampler Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BoxSampler#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/box_sampler.py#L22-L92)

Creates a BoxSampler to sample positive and negative boxes.

tfm.vision.layers.BoxSampler(
        num_samples: int = 512, foreground_fraction: float = 0.25, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_samples` | An `int` of the number of sampled boxes per image. |
| `foreground_fraction` | A `float` in \[0, 1\], what percentage of boxes should be sampled from the positive examples. |
| `**kwargs` | Additional keyword arguments passed to Layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/box_sampler.py#L44-L85)

call(
        positive_matches: tf.Tensor,
        negative_matches: tf.Tensor,
        ignored_matches: tf.Tensor
    )

Samples and selects positive and negative instances.

|     |     |
| --- | --- |
| Args |     |
| `positive_matches` | A `bool` tensor of shape of \[batch, N\] where N is the number of instances. For each element, `True` means the instance corresponds to a positive example. |
| `negative_matches` | A `bool` tensor of shape of \[batch, N\] where N is the number of instances. For each element, `True` means the instance corresponds to a negative example. |
| `ignored_matches` | A `bool` tensor of shape of \[batch, N\] where N is the number of instances. For each element, `True` means the instance should be ignored. |

|     |
| --- |
| Returns |     |
| A `tf.tensor` of shape of \[batch\_size, K\], storing the indices of the sampled examples, where K is `num_samples`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.