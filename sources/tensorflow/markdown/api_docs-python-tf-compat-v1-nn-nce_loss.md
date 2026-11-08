[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/nce_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.nce\_loss Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L2014-L2123)

Computes and returns the noise-contrastive estimation training loss.

tf.compat.v1.nn.nce_loss(
        weights,
        biases,
        labels,
        inputs,
        num_sampled,
        num_classes,
        num_true=1,
        sampled_values=None,
        remove_accidental_hits=False,
        partition_strategy='mod',
        name='nce_loss'
    )

A common use case is to use this method for training, and calculate the full sigmoid loss for evaluation or inference. In this case, you must set `partition_strategy="div"` for the two losses to be consistent, as in the following example:

if mode == "train":
      loss = tf.nn.nce_loss(
          weights=weights,
          biases=biases,
          labels=labels,
          inputs=inputs,
          ...,
          partition_strategy="div")
    elif mode == "eval":
      logits = tf.matmul(inputs, tf.transpose(weights))
      logits = tf.nn.bias_add(logits, biases)
      labels_one_hot = tf.one_hot(labels, n_classes)
      loss = tf.nn.sigmoid_cross_entropy_with_logits(
          labels=labels_one_hot,
          logits=logits)
      loss = tf.reduce_sum(loss, axis=1)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `weights` | A `Tensor` of shape `[num_classes, dim]`, or a list of `Tensor` objects whose concatenation along dimension 0 has shape \[num\_classes, dim\]. The (possibly-partitioned) class embeddings. |
| `biases` | A `Tensor` of shape `[num_classes]`. The class biases. |
| `labels` | A `Tensor` of type `int64` and shape `[batch_size, num_true]`. The target classes. |
| `inputs` | A `Tensor` of shape `[batch_size, dim]`. The forward activations of the input network. |
| `num_sampled` | An `int`. The number of negative classes to randomly sample per batch. This single sample of negative classes is evaluated for each element in the batch. |
| `num_classes` | An `int`. The number of possible classes. |
| `num_true` | An `int`. The number of target classes per training example. |
| `sampled_values` | a tuple of (`sampled_candidates`, `true_expected_count`, `sampled_expected_count`) returned by a `*_candidate_sampler` function. (if None, we default to `log_uniform_candidate_sampler`) |
| `remove_accidental_hits` | A `bool`. Whether to remove "accidental hits" where a sampled class equals one of the target classes. If set to `True`, this is a "Sampled Logistic" loss instead of NCE, and we are learning to generate log-odds instead of log probabilities. See our Candidate Sampling Algorithms Reference ([pdf](https://www.tensorflow.org/extras/candidate_sampling.pdf)<br>). Default is False. |
| `partition_strategy` | A string specifying the partitioning strategy, relevant if `len(weights) > 1`. Currently `"div"` and `"mod"` are supported. Default is `"mod"`. See `tf.nn.embedding_lookup` for more details. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `batch_size` 1-D tensor of per-example NCE losses. |     |

|     |
| --- |
| References<br>---------- |     |
| Noise-contrastive estimation - A new estimation principle for unnormalized statistical models: [Gutmann et al., 2010](http://proceedings.mlr.press/v9/gutmann10a)<br> ([pdf](http://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.