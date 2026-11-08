[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.ctc\_loss Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_loss#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ctc_ops.py#L71-L193)

Computes the CTC (Connectionist Temporal Classification) Loss.

tf.compat.v1.nn.ctc_loss(
        labels,
        inputs=None,
        sequence_length=None,
        preprocess_collapse_repeated=False,
        ctc_merge_repeated=True,
        ignore_longer_outputs_than_inputs=False,
        time_major=True,
        logits=None
    )

This op implements the CTC loss as presented in (Graves et al., 2006).

#### Input requirements:

sequence_length(b) <= time for all b
    
    max(labels.indices(labels.indices[:, 1] == b, 2))
      <= sequence_length(b) for all b.

#### Notes:

This class performs the softmax operation for you, so inputs should be e.g. linear projections of outputs by an LSTM.

The `inputs` Tensor's innermost dimension size, `num_classes`, represents `num_labels + 1` classes, where num\_labels is the number of true labels, and the largest value `(num_classes - 1)` is reserved for the blank label.

For example, for a vocabulary containing 3 labels `[a, b, c]`, `num_classes = 4` and the labels indexing is `{a: 0, b: 1, c: 2, blank: 3}`.

Regarding the arguments `preprocess_collapse_repeated` and `ctc_merge_repeated`:

If `preprocess_collapse_repeated` is True, then a preprocessing step runs before loss calculation, wherein repeated labels passed to the loss are merged into single labels. This is useful if the training labels come from, e.g., forced alignments and therefore have unnecessary repetitions.

If `ctc_merge_repeated` is set False, then deep within the CTC calculation, repeated non-blank labels will not be merged and are interpreted as individual labels. This is a simplified (non-standard) version of CTC.

Here is a table of the (roughly) expected first order behavior:

*   `preprocess_collapse_repeated=False`, `ctc_merge_repeated=True`
    
    Classical CTC behavior: Outputs true repeated classes with blanks in between, and can also output repeated classes with no blanks in between that need to be collapsed by the decoder.
    
*   `preprocess_collapse_repeated=True`, `ctc_merge_repeated=False`
    
    Never learns to output repeated classes, as they are collapsed in the input labels before training.
    
*   `preprocess_collapse_repeated=False`, `ctc_merge_repeated=False`
    
    Outputs repeated classes with blanks in between, but generally does not require the decoder to collapse/merge repeated classes.
    
*   `preprocess_collapse_repeated=True`, `ctc_merge_repeated=True`
    
    Untested. Very likely will not learn to output repeated classes.
    

The `ignore_longer_outputs_than_inputs` option allows to specify the behavior of the CTCLoss when dealing with sequences that have longer outputs than inputs. If true, the CTCLoss will simply return zero gradient for those items, otherwise an InvalidArgument error is returned, stopping training.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | An `int32` `SparseTensor`. `labels.indices[i, :] == [b, t]` means `labels.values[i]` stores the id for (batch b, time t). `labels.values[i]` must take on values in `[0, num_labels)`. See `core/ops/ctc_ops.cc` for more details. |\
| `inputs` | 3-D `float` `Tensor`. If time\_major == False, this will be a `Tensor` shaped: `[batch_size, max_time, num_classes]`. If time\_major == True (default), this will be a `Tensor` shaped: `[max_time, batch_size, num_classes]`. The logits. |\
| `sequence_length` | 1-D `int32` vector, size `[batch_size]`. The sequence lengths. |\
| `preprocess_collapse_repeated` | Boolean. Default: False. If True, repeated labels are collapsed prior to the CTC calculation. |\
| `ctc_merge_repeated` | Boolean. Default: True. |\
| `ignore_longer_outputs_than_inputs` | Boolean. Default: False. If True, sequences with longer outputs than inputs will be ignored. |\
| `time_major` | The shape format of the `inputs` Tensors. If True, these `Tensors` must be shaped `[max_time, batch_size, num_classes]`. If False, these `Tensors` must be shaped `[batch_size, max_time, num_classes]`. Using `time_major = True` (default) is a bit more efficient because it avoids transposes at the beginning of the ctc\_loss calculation. However, most TensorFlow data is batch-major, so by this function also accepts inputs in batch-major form. |\
| `logits` | Alias for inputs. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A 1-D `float` `Tensor`, size `[batch]`, containing the negative log probabilities. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `TypeError` | if labels is not a `SparseTensor`. |\
\
|     |\
| --- |\
| References<br>---------- |     |\
| Connectionist Temporal Classification - Labeling Unsegmented Sequence Data with Recurrent Neural Networks: [Graves et al., 2006](https://dl.acm.org/citation.cfm?id=1143891)<br> ([pdf](http://www.cs.toronto.edu/%7Egraves/icml_2006.pdf)<br>) |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.