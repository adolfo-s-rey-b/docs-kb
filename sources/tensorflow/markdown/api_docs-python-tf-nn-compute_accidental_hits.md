[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/compute_accidental_hits#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/compute_accidental_hits)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/compute_accidental_hits?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/compute_accidental_hits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/compute_accidental_hits#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.compute\_accidental\_hits Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/compute_accidental_hits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/compute_accidental_hits#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/candidate_sampling_ops.py#L466-L513)

Compute the position ids in `sampled_candidates` matching `true_classes`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.compute_accidental_hits`](https://www.tensorflow.org/api_docs/python/tf/nn/compute_accidental_hits)

tf.nn.compute_accidental_hits(
        true_classes, sampled_candidates, num_true, seed=None, name=None
    )

In Candidate Sampling, this operation facilitates virtually removing sampled classes which happen to match target classes. This is done in Sampled Softmax and Sampled Logistic.

See our [Candidate Sampling Algorithms Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf)
.

We presuppose that the `sampled_candidates` are unique.

We call it an 'accidental hit' when one of the target classes matches one of the sampled classes. This operation reports accidental hits as triples `(index, id, weight)`, where `index` represents the row number in `true_classes`, `id` represents the position in `sampled_candidates`, and weight is `-FLOAT_MAX`.

The result of this op should be passed through a `sparse_to_dense` operation, then added to the logits of the sampled classes. This removes the contradictory effect of accidentally sampling the true target classes as noise classes for the same example.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `true_classes` | A `Tensor` of type `int64` and shape `[batch_size, num_true]`. The target classes. |
| `sampled_candidates` | A tensor of type `int64` and shape `[num_sampled]`. The sampled\_candidates output of CandidateSampler. |
| `num_true` | An `int`. The number of target classes per training example. |
| `seed` | An `int`. An operation-specific seed. Default is 0. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `indices` | A `Tensor` of type `int32` and shape `[num_accidental_hits]`. Values indicate rows in `true_classes`. |
| `ids` | A `Tensor` of type `int64` and shape `[num_accidental_hits]`. Values indicate positions in `sampled_candidates`. |
| `weights` | A `Tensor` of type `float` and shape `[num_accidental_hits]`. Each value is `-FLOAT_MAX`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.