[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/sampled_softmax_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/sampled_softmax_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/sampled_softmax_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/sampled_softmax_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/sampled_softmax_loss#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.sampled\_softmax\_loss Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/sampled_softmax_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/sampled_softmax_loss#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L2126-L2215)

Computes and returns the sampled softmax training loss.

tf.nn.sampled_softmax_loss(
        weights,
        biases,
        labels,
        inputs,
        num_sampled,
        num_classes,
        num_true=1,
        sampled_values=None,
        remove_accidental_hits=True,
        seed=None,
        name='sampled_softmax_loss'
    )

This is a faster way to train a softmax classifier over a huge number of classes.

This operation is for training only. It is generally an underestimate of the full softmax loss.

A common use case is to use this method for training, and calculate the full softmax loss for evaluation or inference as in the following example:

if mode == "train":
      loss = tf.nn.sampled_softmax_loss(
          weights=weights,
          biases=biases,
          labels=labels,
          inputs=inputs,
          ...)
    elif mode == "eval":
      logits = tf.matmul(inputs, tf.transpose(weights))
      logits = tf.nn.bias_add(logits, biases)
      labels_one_hot = tf.one_hot(labels, n_classes)
      loss = tf.nn.softmax_cross_entropy_with_logits(
          labels=labels_one_hot,
          logits=logits)

See our [Candidate Sampling Algorithms Reference](https://www.tensorflow.org/extras/candidate_sampling.pdf)

Also see Section 3 of [Jean et al., 2014](http://arxiv.org/abs/1412.2007)
 ([pdf](http://arxiv.org/pdf/1412.2007.pdf)
) for the math.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `weights` | A `Tensor` of shape `[num_classes, dim]`, or a list of `Tensor` objects whose concatenation along dimension 0 has shape \[num\_classes, dim\]. The (possibly-sharded) class embeddings. |
| `biases` | A `Tensor` of shape `[num_classes]`. The class biases. |
| `labels` | A `Tensor` of type `int64` and shape `[batch_size, num_true]`. The target classes. Note that this format differs from the `labels` argument of [`nn.softmax_cross_entropy_with_logits`](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits)<br>. |
| `inputs` | A `Tensor` of shape `[batch_size, dim]`. The forward activations of the input network. |
| `num_sampled` | An `int`. The number of classes to randomly sample per batch. |
| `num_classes` | An `int`. The number of possible classes. |
| `num_true` | An `int`. The number of target classes per training example. |
| `sampled_values` | a tuple of (`sampled_candidates`, `true_expected_count`, `sampled_expected_count`) returned by a `*_candidate_sampler` function. (if None, we default to `log_uniform_candidate_sampler`) |
| `remove_accidental_hits` | A `bool`. whether to remove "accidental hits" where a sampled class equals one of the target classes. Default is True. |
| `seed` | random seed for candidate sampling. Default to None, which doesn't set the op-level random seed for candidate sampling. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `batch_size` 1-D tensor of per-example sampled softmax losses. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.