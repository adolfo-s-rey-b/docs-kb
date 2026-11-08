[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#methods)
    *   [fit\_on\_sequences](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#fit_on_sequences)
        
    *   [fit\_on\_texts](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#fit_on_texts)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#get_config)
        
    *   [sequences\_to\_matrix](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#sequences_to_matrix)
        
    *   [sequences\_to\_texts](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#sequences_to_texts)
        
    *   [sequences\_to\_texts\_generator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#sequences_to_texts_generator)
        
    *   [texts\_to\_matrix](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#texts_to_matrix)
        
    *   [texts\_to\_sequences](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#texts_to_sequences)
        
    *   [texts\_to\_sequences\_generator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#texts_to_sequences_generator)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#to_json)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.text.Tokenizer Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#methods)
    *   [fit\_on\_sequences](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#fit_on_sequences)
        
    *   [fit\_on\_texts](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#fit_on_texts)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#get_config)
        
    *   [sequences\_to\_matrix](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#sequences_to_matrix)
        
    *   [sequences\_to\_texts](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#sequences_to_texts)
        
    *   [sequences\_to\_texts\_generator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#sequences_to_texts_generator)
        
    *   [texts\_to\_matrix](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#texts_to_matrix)
        
    *   [texts\_to\_sequences](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#texts_to_sequences)
        
    *   [texts\_to\_sequences\_generator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#texts_to_sequences_generator)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#to_json)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L81-L312)

DEPRECATED.

tf.keras.preprocessing.text.Tokenizer(
        num_words=None,
        filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
        lower=True,
        split=' ',
        char_level=False,
        oov_token=None,
        analyzer=None,
        **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Wiki Talk Comments Toxicity Prediction](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_Wiki_Case_Study) |

Methods
-------

### `fit_on_sequences`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L169-L174)

fit_on_sequences(
        sequences
    )

### `fit_on_texts`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L121-L167)

fit_on_texts(
        texts
    )

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L284-L304)

get_config()

### `sequences_to_matrix`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L238-L282)

sequences_to_matrix(
        sequences, mode='binary'
    )

### `sequences_to_texts`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L213-L214)

sequences_to_texts(
        sequences
    )

### `sequences_to_texts_generator`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L216-L232)

sequences_to_texts_generator(
        sequences
    )

### `texts_to_matrix`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L234-L236)

texts_to_matrix(
        texts, mode='binary'
    )

### `texts_to_sequences`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L176-L177)

texts_to_sequences(
        texts
    )

### `texts_to_sequences_generator`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L179-L211)

texts_to_sequences_generator(
        texts
    )

### `to_json`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/text.py#L306-L312)

to_json(
        **kwargs
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.