[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/count_nonzero#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/count_nonzero)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/count_nonzero?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/count_nonzero#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/count_nonzero#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.count\_nonzero Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/count_nonzero#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/count_nonzero#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2428-L2501)

Computes number of nonzero elements across dimensions of a tensor.

tf.math.count_nonzero(
        input,
        axis=None,
        keepdims=None,
        dtype=tf.dtypes.int64,
        name=None
    )

Reduces `input` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in `axis`. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` has no entries, all dimensions are reduced, and a tensor with a single element is returned.

#### For example:

x = tf.constant([[0, 1, 0], [1, 1, 0]])
    tf.math.count_nonzero(x)  # 3
    tf.math.count_nonzero(x, 0)  # [1, 2, 0]
    tf.math.count_nonzero(x, 1)  # [1, 2]
    tf.math.count_nonzero(x, 1, keepdims=True)  # [[1], [2]]
    tf.math.count_nonzero(x, [0, 1])  # 3

#### For example:

x = tf.constant(["", "a", "  ", "b", ""])
    tf.math.count_nonzero(x) # 3, with "a", "  ", and "b" as nonzero strings.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | The tensor to reduce. Should be of numeric type, `bool`, or `string`. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input), rank(input))`. |\
| `keepdims` | If true, retains reduced dimensions with length 1. |\
| `dtype` | The output dtype; defaults to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| The reduced tensor (number of nonzero values). |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.