[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.rejection\_resample Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/resampling.py#L20-L50)

A transformation that resamples a dataset to achieve a target distribution. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.rejection_resample`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample)

tf.data.experimental.rejection_resample(
        class_func, target_dist, initial_dist=None, seed=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `class_func` | A function mapping an element of the input dataset to a scalar [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> tensor. Values should be in `[0, num_classes)`. |\
| `target_dist` | A floating point type tensor, shaped `[num_classes]`. |\
| `initial_dist` | (Optional.) A floating point type tensor, shaped `[num_classes]`. If not provided, the true class distribution is estimated live in a streaming fashion. |\
| `seed` | (Optional.) Python integer seed for the resampler. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.