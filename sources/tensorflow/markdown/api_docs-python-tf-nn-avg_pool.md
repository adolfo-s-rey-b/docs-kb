[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Favg_pool&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.avg\_pool Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L4468-L4532)

Performs the avg pooling on the input.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.avg_pool_v2`](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool)

tf.nn.avg_pool(
        input, ksize, strides, padding, data_format=None, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Fast Style Transfer for Arbitrary Styles](https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization) |

Each entry in `output` is the mean of the corresponding size `ksize` window in `value`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape + [num_channels]` if `data_format` does not start with "NC" (default), or `[batch_size, num_channels] + input_spatial_shape` if data\_format starts with "NC". Pooling happens over the spatial dimensions only. |
| `ksize` | An int or list of `ints` that has length `1`, `N` or `N+2`. The size of the window for each dimension of the input tensor. |
| `strides` | An int or list of `ints` that has length `1`, `N` or `N+2`. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |
| `data_format` | A string. Specifies the channel dimension. For N=1 it can be either "NWC" (default) or "NCW", for N=2 it can be either "NHWC" (default) or "NCHW" and for N=3 either "NDHWC" (default) or "NCDHW". |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of format specified by `data_format`. The average pooled output tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.