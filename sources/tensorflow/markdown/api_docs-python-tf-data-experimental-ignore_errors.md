[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.ignore\_errors Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/error_ops.py#L20-L51)

Creates a `Dataset` from another `Dataset` and silently ignores any errors. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.ignore_errors`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors)

tf.data.experimental.ignore_errors(
        log_warning=False
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image captioning with visual attention](https://www.tensorflow.org/text/tutorials/image_captioning) |

Use this transformation to produce a dataset that contains the same elements as the input, but silently drops any elements that caused an error. For example:

dataset = tf.data.Dataset.from_tensor_slices([1., 2., 0., 4.])
    
    # Computing `tf.debugging.check_numerics(1. / 0.)` will raise an
    InvalidArgumentError.
    dataset = dataset.map(lambda x: tf.debugging.check_numerics(1. / x, "error"))
    
    # Using `ignore_errors()` will drop the element that causes an error.
    dataset =
        dataset.apply(tf.data.experimental.ignore_errors())  # ==> {1., 0.5, 0.2}

Args: log\_warning: (Optional.) A 'tf.bool' scalar indicating whether ignored errors should be logged to stderr. Defaults to 'False'.

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.