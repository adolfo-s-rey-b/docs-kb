[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.all\_candidate\_sampler Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/candidate_sampling_ops.py#L430-L463)

Generate the set of all classes.

#### View aliases

**Main aliases**

[`tf.nn.all_candidate_sampler`](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.all_candidate_sampler`](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler)
, [`tf.compat.v1.random.all_candidate_sampler`](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler)

tf.random.all_candidate_sampler(
        true_classes, num_true, num_sampled, unique, seed=None, name=None
    )

Deterministically generates and returns the set of all possible classes. For testing purposes. There is no need to use this, since you might as well use full softmax or full logistic regression.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `true_classes` | A `Tensor` of type `int64` and shape `[batch_size, num_true]`. The target classes. |
| `num_true` | An `int`. The number of target classes per training example. |
| `num_sampled` | An `int`. The number of possible classes. |
| `unique` | A `bool`. Ignored. unique. |
| `seed` | An `int`. An operation-specific seed. Default is 0. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `sampled_candidates` | A tensor of type `int64` and shape `[num_sampled]`. This operation deterministically returns the entire range `[0, num_sampled]`. |
| `true_expected_count` | A tensor of type `float`. Same shape as `true_classes`. The expected counts under the sampling distribution of each of `true_classes`. All returned values are 1.0. |
| `sampled_expected_count` | A tensor of type `float`. Same shape as `sampled_candidates`. The expected counts under the sampling distribution of each of `sampled_candidates`. All returned values are 1.0. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.