[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils/make_distributed_dataset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/utils/make_distributed_dataset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/utils/make_distributed_dataset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/make_distributed_dataset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/orbit/utils/make_distributed_dataset#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.utils.make\_distributed\_dataset Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/make_distributed_dataset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/orbit/utils/make_distributed_dataset#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/common.py#L47-L90)

A utility function to help create a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
.

orbit.utils.make_distributed_dataset(
        strategy, dataset_or_fn, *args, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `strategy` | An instance of [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br>. |
| `dataset_or_fn` | A instance of [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, or a "dataset function" returning a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>. If it is a function, it may optionally have an argument named `input_context` which will be passed a [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)<br> instance. |
| `*args` | Any positional arguments to pass through to `dataset_or_fn`. |
| `**kwargs` | Any keyword arguments to pass through to `dataset_or_fn`, except that the `input_options` keyword is used to specify a [`tf.distribute.InputOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions)<br> for making the distributed dataset. |

|     |
| --- |
| Returns<br>------- |     |
| A distributed Dataset. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.