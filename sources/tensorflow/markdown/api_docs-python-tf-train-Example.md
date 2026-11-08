[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/Example#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/Example)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/Example?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/Example#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/Example#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.Example Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/Example#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/Example#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/example/example.proto)

An `Example` is a standard proto storing data for training and inference.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [TFRecord and tf.train.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning)<br>    <br>*   [Licensed under the Apache License, Version 2.0 (the "License");](https://www.tensorflow.org/tfx/tutorials/tfx/gpt2_finetuning_and_conversion)<br>    <br>*   [TensorFlow Ranking Keras pipeline for distributed training](https://www.tensorflow.org/ranking/tutorials/ranking_dnn_distributed)<br>    <br>*   [FaceSSD Fairness Indicators Example Colab](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Facessd_Fairness_Indicators_Example_Colab) |

An `Example` proto is a representation of the following python type:

Dict[str,\
         Union[List[bytes],\
               List[int64],\
               List[float]]]

It contains a key-value store [`Example.features`](https://www.tensorflow.org/api_docs/python/tf/train/Example#features)
 where each key (string) maps to a [`tf.train.Feature`](https://www.tensorflow.org/api_docs/python/tf/train/Feature)
 message which contains a fixed-type list. This flexible and compact format allows the storage of large amounts of typed data, but requires that the data shape and use be determined by the configuration files and parsers that are used to read and write this format (refer to [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)
 for details).

    from google.protobuf import text_format

Use [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)
 to extract tensors from a serialized `Example` proto:

    tf.io.parse_example(

While the list of keys, and the contents of each key _could_ be different for every `Example`, TensorFlow expects a fixed list of keys, each with a fixed `tf.dtype`. A conformant `Example` dataset obeys the following conventions:

*   If a Feature `K` exists in one example with data type `T`, it must be of type `T` in all other examples when present. It may be omitted.
*   The number of instances of Feature `K` list data may vary across examples, depending on the requirements of the model.
*   If a Feature `K` doesn't exist in an example, a `K`\-specific default will be used, if configured.
*   If a Feature `K` exists in an example but contains no items, the intent is considered to be an empty tensor and no default will be used.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `features` | `Features features` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.