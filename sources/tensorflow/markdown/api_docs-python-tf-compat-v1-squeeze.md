[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.squeeze Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L4233-L4285)

Removes dimensions of size 1 from the shape of a tensor. (deprecated arguments)

tf.compat.v1.squeeze(
        input, axis=None, name=None, squeeze_dims=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Wiki40B Language Models](https://www.tensorflow.org/hub/tutorials/wiki40b_lm) |

Given a tensor `input`, this operation returns a tensor of the same type with all dimensions of size 1 removed. If you don't want to remove all size 1 dimensions, you can remove specific size 1 dimensions by specifying `axis`.

#### For example:

    # 't' is a tensor of shape [1, 2, 1, 3, 1, 1]

Or, to remove specific size 1 dimensions:

    # 't' is a tensor of shape [1, 2, 1, 3, 1, 1]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. The `input` to squeeze. |
| `axis` | An optional list of `ints`. Defaults to `[]`. If specified, only squeezes the dimensions listed. The dimension index starts at 0. It is an error to squeeze a dimension that is not 1. Must be in the range `[-rank(input), rank(input))`. Must be specified if `input` is a `RaggedTensor`. |\
| `name` | A name for the operation (optional). |\
| `squeeze_dims` | Deprecated keyword argument that is now axis. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type as `input`. Contains the same data as `input`, but has one or more dimensions of size 1 removed. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | When both `squeeze_dims` and `axis` are specified. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.