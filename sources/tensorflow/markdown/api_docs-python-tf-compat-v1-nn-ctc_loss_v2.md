[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss_v2#main-content)

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
    

tf.compat.v1.nn.ctc\_loss\_v2 Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ctc_ops.py#L787-L880)

Computes CTC (Connectionist Temporal Classification) loss.

tf.compat.v1.nn.ctc_loss_v2(
        labels,
        logits,
        label_length,
        logit_length,
        logits_time_major=True,
        unique=None,
        blank_index=None,
        name=None
    )

This op implements the CTC loss as presented in (Graves et al., 2006).

#### Notes:

*   Same as the "Classic CTC" in TensorFlow 1.x's tf.compat.v1.nn.ctc\_loss setting of preprocess\_collapse\_repeated=False, ctc\_merge\_repeated=True
*   Labels may be supplied as either a dense, zero-padded tensor with a vector of label sequence lengths OR as a SparseTensor.
*   On TPU and GPU: Only dense padded labels are supported.
*   On CPU: Caller may use SparseTensor or dense padded labels but calling with a SparseTensor will be significantly faster.
*   Default blank label is 0 rather num\_classes - 1, unless overridden by blank\_index.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | tensor of shape \[batch\_size, max\_label\_seq\_length\] or SparseTensor |
| `logits` | tensor of shape \[frames, batch\_size, num\_labels\], if logits\_time\_major == False, shape is \[batch\_size, frames, num\_labels\]. |
| `label_length` | tensor of shape \[batch\_size\], None if labels is SparseTensor Length of reference label sequence in labels. |
| `logit_length` | tensor of shape \[batch\_size\] Length of input sequence in logits. |
| `logits_time_major` | (optional) If True (default), logits is shaped \[time, batch, logits\]. If False, shape is \[batch, time, logits\] |
| `unique` | (optional) Unique label indices as computed by ctc\_unique\_labels(labels). If supplied, enable a faster, memory efficient implementation on TPU. |
| `blank_index` | (optional) Set the class index to use for the blank label. Negative values will start from num\_classes, ie, -1 will reproduce the ctc\_loss behavior of using num\_classes - 1 for the blank symbol. There is some memory/performance overhead to switching from the default of 0 as an additional shifted copy of the logits may be created. |
| `name` | A name for this `Op`. Defaults to "ctc\_loss\_dense". |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `loss` | tensor of shape \[batch\_size\], negative log probabilities. |

|     |
| --- |
| References<br>---------- |     |
| Connectionist Temporal Classification - Labeling Unsegmented Sequence Data with Recurrent Neural Networks: [Graves et al., 2006](https://dl.acm.org/citation.cfm?id=1143891)<br> ([pdf](http://www.cs.toronto.edu/%7Egraves/icml_2006.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.