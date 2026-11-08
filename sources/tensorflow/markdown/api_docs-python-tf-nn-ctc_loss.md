[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.ctc\_loss Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ctc_ops.py#L883-L1036)

Computes CTC (Connectionist Temporal Classification) loss.

tf.nn.ctc_loss(
        labels,
        logits,
        label_length,
        logit_length,
        logits_time_major=True,
        unique=None,
        blank_index=None,
        name=None
    )

This op implements the CTC loss as presented in [Graves et al., 2006](https://www.cs.toronto.edu/%7Egraves/icml_2006.pdf)

Connectionist temporal classification (CTC) is a type of neural network output and associated scoring function, for training recurrent neural networks (RNNs) such as LSTM networks to tackle sequence problems where the timing is variable. It can be used for tasks like on-line handwriting recognition or recognizing phones in speech audio. CTC refers to the outputs and scoring, and is independent of the underlying neural network structure.

#### Notes:

*   This class performs the softmax operation for you, so `logits` should be e.g. linear projections of outputs by an LSTM.
*   Outputs true repeated classes with blanks in between, and can also output repeated classes with no blanks in between that need to be collapsed by the decoder.
*   `labels` may be supplied as either a dense, zero-padded `Tensor` with a vector of label sequence lengths OR as a `SparseTensor`.
*   On TPU: Only dense padded `labels` are supported.
*   On CPU and GPU: Caller may use `SparseTensor` or dense padded `labels` but calling with a `SparseTensor` will be significantly faster.
*   Default blank label is `0` instead of `num_labels - 1` (where `num_labels` is the innermost dimension size of `logits`), unless overridden by `blank_index`.

    tf.random.set_seed(50)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | `Tensor` of shape `[batch_size, max_label_seq_length]` or `SparseTensor`. |
| `logits` | `Tensor` of shape `[frames, batch_size, num_labels]`. If `logits_time_major == False`, shape is `[batch_size, frames, num_labels]`. |
| `label_length` | `Tensor` of shape `[batch_size]`. None, if `labels` is a `SparseTensor`. Length of reference label sequence in `labels`. |
| `logit_length` | `Tensor` of shape `[batch_size]`. Length of input sequence in `logits`. |
| `logits_time_major` | (optional) If True (default), `logits` is shaped \[frames, batch\_size, num\_labels\]. If False, shape is `[batch_size, frames, num_labels]`. |
| `unique` | (optional) Unique label indices as computed by `ctc_unique_labels(labels)`. If supplied, enable a faster, memory efficient implementation on TPU. |
| `blank_index` | (optional) Set the class index to use for the blank label. Negative values will start from `num_labels`, ie, `-1` will reproduce the ctc\_loss behavior of using `num_labels - 1` for the blank symbol. There is some memory/performance overhead to switching from the default of 0 as an additional shifted copy of `logits` may be created. |
| `name` | A name for this `Op`. Defaults to "ctc\_loss\_dense". |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `loss` | A 1-D `float Tensor` of shape `[batch_size]`, containing negative log probabilities. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | Argument `blank_index` must be provided when `labels` is a `SparseTensor`. |

|     |
| --- |
| References<br>---------- |     |
| Connectionist Temporal Classification - Labeling Unsegmented Sequence Data with Recurrent Neural Networks: [Graves et al., 2006](https://dl.acm.org/citation.cfm?id=1143891)<br> ([pdf](http://www.cs.toronto.edu/%7Egraves/icml_2006.pdf)<br>)<br><br>[https://en.wikipedia.org/wiki/Connectionist\_temporal\_classification](https://en.wikipedia.org/wiki/Connectionist_temporal_classification) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.