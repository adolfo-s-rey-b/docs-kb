None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / KerasHub Tokenizers

KerasHub Tokenizers
===================

Tokenizers convert raw string input into integer input suitable for a Keras `Embedding` layer. They can also convert back from predicted integer sequences to raw string output.

All tokenizers subclass [`keras_hub.tokenizers.Tokenizer`](https://keras.io/keras_hub/api/tokenizers/tokenizer#tokenizer-class)
, which in turn subclasses `keras.layers.Layer`. Tokenizers should generally be applied inside a [tf.data.Dataset.map](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map)
 for training, and can be included inside a [`keras.Model`](https://keras.io/api/models/model#model-class)
 for inference.

### [Tokenizer](https://keras.io/keras_hub/api/tokenizers/tokenizer/)

*   [Tokenizer class](https://keras.io/keras_hub/api/tokenizers/tokenizer/#tokenizer-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/tokenizers/tokenizer/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/tokenizers/tokenizer/#save_to_preset-method)
    

### [WordPieceTokenizer](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer/)

*   [WordPieceTokenizer class](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer/#wordpiecetokenizer-class)
    
*   [tokenize method](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer/#tokenize-method)
    
*   [detokenize method](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer/#detokenize-method)
    
*   [get\_vocabulary method](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer/#get_vocabulary-method)
    
*   [vocabulary\_size method](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer/#vocabulary_size-method)
    
*   [token\_to\_id method](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer/#token_to_id-method)
    
*   [id\_to\_token method](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer/#id_to_token-method)
    

### [SentencePieceTokenizer](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/)

*   [SentencePieceTokenizer class](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#sentencepiecetokenizer-class)
    
*   [tokenize method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#tokenize-method)
    
*   [detokenize method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#detokenize-method)
    
*   [get\_vocabulary method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#get_vocabulary-method)
    
*   [vocabulary\_size method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#vocabulary_size-method)
    
*   [token\_to\_id method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#token_to_id-method)
    
*   [id\_to\_token method](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer/#id_to_token-method)
    

### [BytePairTokenizer](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/)

*   [BytePairTokenizer class](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#bytepairtokenizer-class)
    
*   [tokenize method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#tokenize-method)
    
*   [detokenize method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#detokenize-method)
    
*   [get\_vocabulary method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#get_vocabulary-method)
    
*   [vocabulary\_size method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#vocabulary_size-method)
    
*   [token\_to\_id method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#token_to_id-method)
    
*   [id\_to\_token method](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer/#id_to_token-method)
    

### [ByteTokenizer](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer/)

*   [ByteTokenizer class](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer/#bytetokenizer-class)
    
*   [tokenize method](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer/#tokenize-method)
    
*   [detokenize method](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer/#detokenize-method)
    
*   [get\_vocabulary method](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer/#get_vocabulary-method)
    
*   [vocabulary\_size method](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer/#vocabulary_size-method)
    
*   [token\_to\_id method](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer/#token_to_id-method)
    
*   [id\_to\_token method](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer/#id_to_token-method)
    

### [UnicodeCodepointTokenizer](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/)

*   [UnicodeCodepointTokenizer class](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#unicodecodepointtokenizer-class)
    
*   [tokenize method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#tokenize-method)
    
*   [detokenize method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#detokenize-method)
    
*   [get\_vocabulary method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#get_vocabulary-method)
    
*   [vocabulary\_size method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#vocabulary_size-method)
    
*   [token\_to\_id method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#token_to_id-method)
    
*   [id\_to\_token method](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer/#id_to_token-method)
    

### [compute\_word\_piece\_vocabulary function](https://keras.io/keras_hub/api/tokenizers/compute_word_piece_vocabulary/)

*   [compute\_word\_piece\_vocabulary function](https://keras.io/keras_hub/api/tokenizers/compute_word_piece_vocabulary/#compute_word_piece_vocabulary-function)
    

### [compute\_sentence\_piece\_proto function](https://keras.io/keras_hub/api/tokenizers/compute_sentence_piece_proto/)

*   [compute\_sentence\_piece\_proto function](https://keras.io/keras_hub/api/tokenizers/compute_sentence_piece_proto/#compute_sentence_piece_proto-function)
    

[KerasHub Tokenizers](https://keras.io/keras_hub/api/tokenizers/#kerashub-tokenizers)

[Tokenizer](https://keras.io/keras_hub/api/tokenizers/#tokenizer)

[WordPieceTokenizer](https://keras.io/keras_hub/api/tokenizers/#wordpiecetokenizer)

[SentencePieceTokenizer](https://keras.io/keras_hub/api/tokenizers/#sentencepiecetokenizer)

[BytePairTokenizer](https://keras.io/keras_hub/api/tokenizers/#bytepairtokenizer)

[ByteTokenizer](https://keras.io/keras_hub/api/tokenizers/#bytetokenizer)

[UnicodeCodepointTokenizer](https://keras.io/keras_hub/api/tokenizers/#unicodecodepointtokenizer)

[compute\_word\_piece\_vocabulary function](https://keras.io/keras_hub/api/tokenizers/#computewordpiecevocabulary-function)

[compute\_sentence\_piece\_proto function](https://keras.io/keras_hub/api/tokenizers/#computesentencepieceproto-function)