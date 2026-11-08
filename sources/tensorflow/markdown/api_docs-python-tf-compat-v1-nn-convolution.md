[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fnn%2Fconvolution&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.convolution Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/convolution#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L1033-L1173)

Computes sums of N-D convolutions (actually cross-correlation).

tf.compat.v1.nn.convolution(
        input,
        filter,
        padding,
        strides=None,
        dilation_rate=None,
        name=None,
        data_format=None,
        filters=None,
        dilations=None
    )

This also supports either output striding via the optional `strides` parameter or atrous convolution (also known as convolution with holes or dilated convolution, based on the French word "trous" meaning holes in English) via the optional `dilation_rate` parameter. Currently, however, output striding is not supported for atrous convolutions.

Specifically, in the case that `data_format` does not start with "NC", given a rank (N+2) `input` Tensor of shape

\[num\_batches, input\_spatial\_shape\[0\], ..., input\_spatial\_shape\[N-1\], num\_input\_channels\],

a rank (N+2) `filter` Tensor of shape

\[spatial\_filter\_shape\[0\], ..., spatial\_filter\_shape\[N-1\], num\_input\_channels, num\_output\_channels\],

an optional `dilation_rate` tensor of shape N (defaults to `[1]*N`) specifying the filter upsampling/input downsampling rate, and an optional list of N `strides` (defaults to `[1]*N`), this computes for each N-D spatial output position `(x[0], ..., x[N-1])`:

output[b, x[0], ..., x[N-1], k] =
        sum_{z[0], ..., z[N-1], q}
            filter[z[0], ..., z[N-1], q, k] *
            padded_input[b,\
                         x[0]*strides[0] + dilation_rate[0]*z[0],\
                         ...,\
                         x[N-1]*strides[N-1] + dilation_rate[N-1]*z[N-1],\
                         q]

where b is the index into the batch, k is the output channel number, q is the input channel number, and z is the N-D spatial offset within the filter. Here, `padded_input` is obtained by zero padding the input using an effective spatial filter shape of `(spatial_filter_shape-1) * dilation_rate + 1` and output striding `strides`.

In the case that `data_format` does start with `"NC"`, the `input` and output (but not the `filter`) are simply transposed as follows:

convolution(input, data_format, **kwargs) =
      tf.transpose(convolution(tf.transpose(input, [0] + range(2,N+2) + [1]),
                               **kwargs),
                   [0, N+1] + range(1, N+1))

It is required that 1 <= N <= 3.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | An (N+2)-D `Tensor` of type `T`, of shape `[batch_size] + input_spatial_shape + [in_channels]` if data\_format does not start with "NC" (default), or `[batch_size, in_channels] + input_spatial_shape` if data\_format starts with "NC". |
| `filter` | An (N+2)-D `Tensor` with the same type as `input` and shape `spatial_filter_shape + [in_channels, out_channels]`. |
| `padding` | A string, either `"VALID"` or `"SAME"`. The padding algorithm. `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input when the strides are 1. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |
| `strides` | Optional. Sequence of N ints >= 1. Specifies the output stride. Defaults to `[1]*N`. If any value of strides is > 1, then all values of dilation\_rate must be 1. |
| `dilation_rate` | Optional. Sequence of N ints >= 1. Specifies the filter upsampling/input downsampling rate. In the literature, the same parameter is sometimes called `input stride` or `dilation`. The effective filter size used for the convolution will be `spatial_filter_shape + (spatial_filter_shape - 1) * (rate - 1)`, obtained by inserting (dilation\_rate\[i\]-1) zeros between consecutive elements of the original filter in each spatial dimension i. If any value of dilation\_rate is > 1, then all values of strides must be 1. |
| `name` | Optional name for the returned tensor. |
| `data_format` | A string or None. Specifies whether the channel dimension of the `input` and output is the last dimension (default, or if `data_format` does not start with "NC"), or the second dimension (if `data_format` starts with "NC"). For N=1, the valid values are "NWC" (default) and "NCW". For N=2, the valid values are "NHWC" (default) and "NCHW". For N=3, the valid values are "NDHWC" (default) and "NCDHW". |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `input` of shape<br><br>`[batch_size] + output_spatial_shape + [out_channels]`<br><br>if data\_format is None or does not start with "NC", or<br><br>`[batch_size, out_channels] + output_spatial_shape`<br><br>if data\_format starts with "NC", where `output_spatial_shape` depends on the value of `padding`.<br><br>If padding == "SAME": output\_spatial\_shape\[i\] = ceil(input\_spatial\_shape\[i\] / strides\[i\])<br><br>If padding == "VALID": output\_spatial\_shape\[i\] = ceil((input\_spatial\_shape\[i\] - (spatial\_filter\_shape\[i\]-1) \* dilation\_rate\[i\]) / strides\[i\]). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If input/output depth does not match `filter` shape, if padding is other than `"VALID"` or `"SAME"`, or if data\_format is invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.