[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.max\_pool Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L4710-L4850)

Performs max pooling on the input.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.max_pool_v2`](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool)

tf.nn.max_pool(
        input, ksize, strides, padding, data_format=None, name=None
    )

For a given window of `ksize`, takes the maximum value within that window. Used for reducing computation and preventing overfitting.

Consider an example of pooling with 2x2, non-overlapping windows:

    matrix = tf.constant([\
\
We can adjust the window size using the `ksize` parameter. For example, if we were to expand the window to 3:\
\
    tf.nn.max_pool(reshaped, ksize=3, strides=2, padding="SAME")\
\
We've now picked up two additional large numbers (5 and 9) in two of the pooled spots.\
\
Note that our windows are now overlapping, since we're still moving by 2 units on each iteration. This is causing us to see the same 9 repeated twice, since it is part of two overlapping windows.\
\
We can adjust how far we move our window with each iteration using the `strides` parameter. Updating this to the same value as our window size eliminates the overlap:\
\
    tf.nn.max_pool(reshaped, ksize=3, strides=3, padding="SAME")\
\
Because the window does not neatly fit into our input, padding is added around the edges, giving us the same result as when we used a 2x2 window. We can skip padding altogether and simply drop the windows that do not fully fit into our input by instead passing `"VALID"` to the `padding` argument:\
\
    tf.nn.max_pool(reshaped, ksize=3, strides=3, padding="VALID")\
\
Now we've grabbed the largest value in the 3x3 window starting from the upper- left corner. Since no other windows fit in our input, they are dropped.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `input` | Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape + [num_channels]` if `data_format` does not start with "NC" (default), or `[batch_size, num_channels] + input_spatial_shape` if data\_format starts with "NC". Pooling happens over the spatial dimensions only. |\
| `ksize` | An int or list of `ints` that has length `1`, `N` or `N+2`. The size of the window for each dimension of the input tensor. |\
| `strides` | An int or list of `ints` that has length `1`, `N` or `N+2`. The stride of the sliding window for each dimension of the input tensor. |\
| `padding` | Either the `string` `"SAME"` or `"VALID"` indicating the type of padding algorithm to use, or a list indicating the explicit paddings at the start and end of each dimension. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. When explicit padding is used and data\_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used and data\_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`. When using explicit padding, the size of the paddings cannot be greater than the sliding window size. |\
| `data_format` | A string. Specifies the channel dimension. For N=1 it can be either "NWC" (default) or "NCW", for N=2 it can be either "NHWC" (default) or "NCHW" and for N=3 either "NDHWC" (default) or "NCDHW". |\
| `name` | Optional name for the operation. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor` of format specified by `data_format`. The max pooled output tensor. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If<br><br>*   explicit padding is used with an input tensor of rank 5.<br>*   explicit padding is used with data\_format='NCHW\_VECT\_C'. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.