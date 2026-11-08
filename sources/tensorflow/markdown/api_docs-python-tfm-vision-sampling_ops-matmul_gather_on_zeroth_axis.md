[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/matmul_gather_on_zeroth_axis#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/matmul_gather_on_zeroth_axis)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/matmul_gather_on_zeroth_axis?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/matmul_gather_on_zeroth_axis#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/matmul_gather_on_zeroth_axis#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.sampling\_ops.matmul\_gather\_on\_zeroth\_axis Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/matmul_gather_on_zeroth_axis#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/matmul_gather_on_zeroth_axis#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/sampling_ops.py#L92-L116)

Matrix multiplication based implementation of tf.gather on zeroth axis.

tfm.vision.sampling_ops.matmul_gather_on_zeroth_axis(
        params, indices, scope=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | A float32 Tensor. The tensor from which to gather values. Must be at least rank 1. |
| `indices` | A Tensor. Must be one of the following types: int32, int64. Must be in range \[0, params.shape\[0\]) |\
| `scope` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A Tensor. Has the same type as params. Values from params gathered from indices given by indices, with shape indices.shape + params.shape\[1:\]. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.