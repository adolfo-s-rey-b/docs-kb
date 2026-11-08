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
 / [Model Architectures](https://keras.io/keras_hub/api/models/)
 / [T5](https://keras.io/keras_hub/api/models/t5/)
 / T5Tokenizer

T5Tokenizer
===========

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5/t5_tokenizer.py#L8)

### `T5Tokenizer` class

Copied!

`keras_hub.tokenizers.T5Tokenizer(proto, **kwargs)`

T5 tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by T5 models and provides a `from_preset()` method to automatically download a matching vocabulary for a T5 preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.

**Examples**

Copied!

`bytes_io = io.BytesIO() ds = tf.data.Dataset.from_tensor_slices(["The quick brown fox jumped."]) sentencepiece.SentencePieceTrainer.train(     sentence_iterator=ds.as_numpy_iterator(),     model_writer=bytes_io,     vocab_size=8,     model_type="WORD",     bos_id=-1,     pad_id=0,     eos_id=1,     unk_id=2,     pad_piece="<pad>",     eos_piece="</s>",     unk_piece="<unk>", ) tokenizer = keras_hub.models.T5Tokenizer(     proto=bytes_io.getvalue(), ) tokenizer("The quick brown fox jumped.")  # Batched inputs. tokenizer(["the quick brown fox", "the earth is round"])  # Unbatched inputs. tokenizer("the quick brown fox")  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`T5Tokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

Instantiate a `keras_hub.models.Tokenizer` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Tokenizer` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Tokenizer.from_preset()`, or from a model class like `keras_hub.models.GemmaTokenizer.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a preset tokenizer. tokenizer = keras_hub.tokenizer.Tokenizer.from_preset("bert_base_en")  # Tokenize some input. tokenizer("The quick brown fox tripped.")  # Detokenize some input. tokenizer.detokenize([5, 6, 7, 8, 9])`

| Preset | Parameters | Description |
| --- | --- | --- |
| [blip2\_opt\_2.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_2.7b/1) | 3.74B | BLIP-2 model using OPT-2.7B as the frozen language model. |
| [blip2\_flan\_t5\_xl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xl/1) | 3.94B | BLIP-2 model using Flan-T5-XL (~3B) as the frozen language model. |
| [blip2\_opt\_6.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_6.7b/1) | 7.75B | BLIP-2 model using OPT-6.7B as the frozen language model. |
| [blip2\_flan\_t5\_xxl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xxl/1) | 12.23B | BLIP-2 model using Flan-T5-XXL (~11B) as the frozen language model. |
| [t5\_small\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_small_multi/3) | 60.51M | 6-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_small](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_small/2) | 60.51M |     |
| [flan\_small\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_small_multi/3) | 76.96M | 8-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_base\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_base_multi/3) | 222.90M | 12-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_base](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_base/2) | 247.58M |     |
| [flan\_base\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_base_multi/3) | 247.58M | 12-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_large\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_large_multi/3) | 737.67M | 24-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_large](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_large/2) | 750.25M |     |
| [flan\_large\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_large_multi/3) | 783.15M | 24-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_xl](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_xl/2) | 2.85B |     |
| [t5\_1.1\_xxl](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_xxl/2) | 11.14B |     |

* * *

[T5Tokenizer](https://keras.io/keras_hub/api/models/t5/t5_tokenizer/#t5tokenizer)

[`T5Tokenizer` class](https://keras.io/keras_hub/api/models/t5/t5_tokenizer/#t5tokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5/t5_tokenizer/#frompreset-method)