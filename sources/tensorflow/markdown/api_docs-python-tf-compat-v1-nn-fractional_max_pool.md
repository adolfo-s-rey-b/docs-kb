[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.fractional\_max\_pool Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fractional_max_pool#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L6047-L6143)

Performs fractional max pooling on the input. (deprecated)

tf.compat.v1.nn.fractional_max_pool(
        value,
        pooling_ratio,
        pseudo_random=False,
        overlapping=False,
        deterministic=False,
        seed=0,
        seed2=0,
        name=None
    )

This is a deprecated version of `fractional_max_pool`.

Fractional max pooling is slightly different than regular max pooling. In regular max pooling, you downsize an input set by taking the maximum value of smaller N x N subsections of the set (often 2x2), and try to reduce the set by a factor of N, where N is an integer. Fractional max pooling, as you might expect from the word "fractional", means that the overall reduction ratio N does not have to be an integer.

The sizes of the pooling regions are generated randomly but are fairly uniform. For example, let's look at the height dimension, and the constraints on the list of rows that will be pool boundaries.

First we define the following:

1.  input\_row\_length : the number of rows from the input set
2.  output\_row\_length : which will be smaller than the input
3.  alpha = input\_row\_length / output\_row\_length : our reduction ratio
4.  K = floor(alpha)
5.  row\_pooling\_sequence : this is the result list of pool boundary rows

Then, row\_pooling\_sequence should satisfy:

1.  a\[0\] = 0 : the first value of the sequence is 0
2.  a\[end\] = input\_row\_length : the last value of the sequence is the size
3.  K <= (a\[i+1\] - a\[i\]) <= K+1 : all intervals are K or K+1 size
4.  length(row\_pooling\_sequence) = output\_row\_length+1

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A `Tensor`. 4-D with shape `[batch, height, width, channels]`. |
| `pooling_ratio` | A list of `floats` that has length >= 4. Pooling ratio for each dimension of `value`, currently only supports row and col dimension and should be >= 1.0. For example, a valid pooling ratio looks like \[1.0, 1.44, 1.73, 1.0\]. The first and last elements must be 1.0 because we don't allow pooling on batch and channels dimensions. 1.44 and 1.73 are pooling ratio on height and width dimensions respectively. |
| `pseudo_random` | An optional `bool`. Defaults to `False`. When set to `True`, generates the pooling sequence in a pseudorandom fashion, otherwise, in a random fashion. Check (Graham, 2015) for difference between pseudorandom and random. |
| `overlapping` | An optional `bool`. Defaults to `False`. When set to `True`, it means when pooling, the values at the boundary of adjacent pooling cells are used by both cells. For example: `index 0 1 2 3 4` `value 20 5 16 3 7` If the pooling sequence is \[0, 2, 4\], then 16, at index 2 will be used twice. The result would be \[20, 16\] for fractional max pooling. |
| `deterministic` | An optional `bool`. Deprecated; use `fractional_max_pool_v2` instead. |
| `seed` | An optional `int`. Defaults to `0`. If set to be non-zero, the random number generator is seeded by the given seed. Otherwise it is seeded by a random seed. |
| `seed2` | An optional `int`. Deprecated; use `fractional_max_pool_v2` instead. |
| `name` | A name for the operation (optional). |

Returns
-------

A tuple of `Tensor` objects (`output`, `row_pooling_sequence`, `col_pooling_sequence`). output: Output `Tensor` after fractional max pooling. Has the same type as `value`. row\_pooling\_sequence: A `Tensor` of type `int64`. col\_pooling\_sequence: A `Tensor` of type `int64`.

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If op determinism is enabled and either the seeds are not set or the "deterministic" argument is False. |

|     |
| --- |
| References<br>---------- |     |
| Fractional Max-Pooling: [Graham, 2015](https://arxiv.org/abs/1412.6071)<br> ([pdf](https://arxiv.org/pdf/1412.6071.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.