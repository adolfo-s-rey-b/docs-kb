[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fsampling_ops%2FBalancedPositiveNegativeSampler&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#methods)
    *   [subsample](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#subsample)
        
    *   [subsample\_indicator](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#subsample_indicator)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.sampling\_ops.BalancedPositiveNegativeSampler Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#methods)
    *   [subsample](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#subsample)
        
    *   [subsample\_indicator](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops/BalancedPositiveNegativeSampler#subsample_indicator)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/sampling_ops.py#L119-L382)

Subsamples minibatches to a desired balance of positives and negatives.

tfm.vision.sampling_ops.BalancedPositiveNegativeSampler(
        positive_fraction=0.5, is_static=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `positive_fraction` | desired fraction of positive examples (scalar in \[0,1\]) in the batch. |
| `is_static` | If True, uses an implementation with static shape guarantees. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if positive\_fraction < 0, or positive\_fraction > 1 |

Methods
-------

### `subsample`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/sampling_ops.py#L320-L382)

subsample(
        indicator, batch_size, labels, scope=None
    )

Returns subsampled minibatch.

|     |     |
| --- | --- |
| Args |     |
| `indicator` | boolean tensor of shape \[N\] whose True entries can be sampled. |
| `batch_size` | desired batch size. If None, keeps all positive samples and randomly selects negative samples so that the positive sample fraction matches self.\_positive\_fraction. It cannot be None is is\_static is True. |
| `labels` | boolean tensor of shape \[N\] denoting positive(=True) and negative (=False) examples. |
| `scope` | name scope. |

|     |     |
| --- | --- |
| Returns |     |
| `sampled_idx_indicator` | boolean tensor of shape \[N\], True for entries which are sampled. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if labels and indicator are not 1D boolean tensors. |

### `subsample_indicator`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/sampling_ops.py#L139-L167)

@staticmethod

Subsample indicator vector.

Given a boolean indicator vector with M elements set to `True`, the function assigns all but `num_samples` of these previously `True` elements to `False`. If `num_samples` is greater than M, the original indicator vector is returned.

|     |     |
| --- | --- |
| Args |     |
| `indicator` | a 1-dimensional boolean tensor indicating which elements are allowed to be sampled and which are not. |
| `num_samples` | int32 scalar tensor |

|     |
| --- |
| Returns |     |
| a boolean tensor with the same shape as input (indicator) tensor |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.