[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/VocabInfo#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/VocabInfo)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/VocabInfo?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.VocabInfo Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/warm_starting_util.py#L32-L129)

Vocabulary information for warm-starting.

tf.compat.v1.train.VocabInfo(
        new_vocab,
        new_vocab_size,
        num_oov_buckets,
        old_vocab,
        old_vocab_size=-1,
        backup_initializer=None,
        axis=0
    )

See `tf.estimator.WarmStartSettings` for examples of using VocabInfo to warm-start.

Args: new\_vocab: \[Required\] A path to the new vocabulary file (used with the model to be trained). new\_vocab\_size: \[Required\] An integer indicating how many entries of the new vocabulary will used in training. num\_oov\_buckets: \[Required\] An integer indicating how many OOV buckets are associated with the vocabulary. old\_vocab: \[Required\] A path to the old vocabulary file (used with the checkpoint to be warm-started from). old\_vocab\_size: \[Optional\] An integer indicating how many entries of the old vocabulary were used in the creation of the checkpoint. If not provided, the entire old vocabulary will be used. backup\_initializer: \[Optional\] A variable initializer used for variables corresponding to new vocabulary entries and OOV. If not provided, these entries will be zero-initialized. axis: \[Optional\] Denotes what axis the vocabulary corresponds to. The default, 0, corresponds to the most common use case (embeddings or linear weights for binary classification / regression). An axis of 1 could be used for warm-starting output layers with class vocabularies.

Returns: A `VocabInfo` which represents the vocabulary information for warm-starting.

Raises: ValueError: `axis` is neither 0 or 1.

  Example Usage:

      embeddings_vocab_info = tf.VocabInfo(
              new_vocab='embeddings_vocab',
              new_vocab_size=100,
              num_oov_buckets=1,
              old_vocab='pretrained_embeddings_vocab',
              old_vocab_size=10000,
              backup_initializer=tf.compat.v1.truncated_normal_initializer(
                  mean=0.0, stddev=(1 / math.sqrt(embedding_dim))),
              axis=0)
    
          softmax_output_layer_kernel_vocab_info = tf.VocabInfo(
              new_vocab='class_vocab',
              new_vocab_size=5,
              num_oov_buckets=0,  # No OOV for classes.
              old_vocab='old_class_vocab',
              old_vocab_size=8,
              backup_initializer=tf.compat.v1.glorot_uniform_initializer(),
              axis=1)
    
          softmax_output_layer_bias_vocab_info = tf.VocabInfo(
              new_vocab='class_vocab',
              new_vocab_size=5,
              num_oov_buckets=0,  # No OOV for classes.
              old_vocab='old_class_vocab',
              old_vocab_size=8,
              backup_initializer=tf.compat.v1.zeros_initializer(),
              axis=0)
    
          #Currently, only axis=0 and axis=1 are supported.
      ```
      
    
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>
    
    <tr>
    <td>
    `new_vocab`<a id="new_vocab"></a>
    </td>
    <td>
    A `namedtuple` alias for field number 0
    </td>
    </tr><tr>
    <td>
    `new_vocab_size`<a id="new_vocab_size"></a>
    </td>
    <td>
    A `namedtuple` alias for field number 1
    </td>
    </tr><tr>
    <td>
    `num_oov_buckets`<a id="num_oov_buckets"></a>
    </td>
    <td>
    A `namedtuple` alias for field number 2
    </td>
    </tr><tr>
    <td>
    `old_vocab`<a id="old_vocab"></a>
    </td>
    <td>
    A `namedtuple` alias for field number 3
    </td>
    </tr><tr>
    <td>
    `old_vocab_size`<a id="old_vocab_size"></a>
    </td>
    <td>
    A `namedtuple` alias for field number 4
    </td>
    </tr><tr>
    <td>
    `backup_initializer`<a id="backup_initializer"></a>
    </td>
    <td>
    A `namedtuple` alias for field number 5
    </td>
    </tr><tr>
    <td>
    `axis`<a id="axis"></a>
    </td>
    <td>
    A `namedtuple` alias for field number 6
    </td>
    </tr>
    </table>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.