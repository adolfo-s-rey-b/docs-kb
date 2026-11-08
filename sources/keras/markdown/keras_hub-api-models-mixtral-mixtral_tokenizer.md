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
 / [Mixtral](https://keras.io/keras_hub/api/models/mixtral/)
 / MixtralTokenizer

MixtralTokenizer
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mixtral/mixtral_tokenizer.py#L8)

### `MixtralTokenizer` class

Copied!

`keras_hub.tokenizers.MixtralTokenizer(proto, **kwargs)`

A SentencePiece tokenizer layer.

This layer provides an implementation of SentencePiece tokenization as described in the [SentencePiece paper](https://arxiv.org/abs/1808.06226)
 and the [SentencePiece package](https://pypi.org/project/sentencepiece/)
. The tokenization will run entirely within the Tensorflow graph, and can be saved inside a [`keras.Model`](https://keras.io/api/models/model#model-class)
.

By default, the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged after whitespace splitting and sub-word tokenizing. If `sequence_length` is set, the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 where all inputs have been padded or truncated to `sequence_length`. The output dtype can be controlled via the `dtype` argument, which should be either an integer or string type.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.
*   **sequence\_length**: If set, the output will be converted to a dense tensor and padded/trimmed so all outputs are of `sequence_length`.
*   **add\_bos**: Add beginning of sentence token to the result.
*   **add\_eos**: Add end of sentence token to the result. Token is always truncated if output is longer than specified `sequence_length`.

**References**

*   [Kudo and Richardson, 2018](https://arxiv.org/abs/1808.06226)
    

**Examples**

From bytes.

Copied!

`def train_sentence_piece_bytes(ds, size):     bytes_io = io.BytesIO()     sentencepiece.SentencePieceTrainer.train(         sentence_iterator=ds.as_numpy_iterator(),         model_writer=bytes_io,         vocab_size=size,     )     return bytes_io.getvalue()  # Train a sentencepiece proto. ds = tf.data.Dataset.from_tensor_slices(["the quick brown fox."]) proto = train_sentence_piece_bytes(ds, 20) # Tokenize inputs. tokenizer = keras_hub.tokenizers.SentencePieceTokenizer(proto=proto) ds = ds.map(tokenizer)`

From a file.

Copied!

`def train_sentence_piece_file(ds, path, size):     with open(path, "wb") as model_file:         sentencepiece.SentencePieceTrainer.train(             sentence_iterator=ds.as_numpy_iterator(),             model_writer=model_file,             vocab_size=size,         )  # Train a sentencepiece proto. ds = tf.data.Dataset.from_tensor_slices(["the quick brown fox."]) proto = train_sentence_piece_file(ds, "model.spm", 20) # Tokenize inputs. tokenizer = keras_hub.tokenizers.SentencePieceTokenizer(proto="model.spm") ds = ds.map(tokenizer)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`MixtralTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [mixtral\_8\_7b\_en](https://www.kaggle.com/models/keras/mixtral/keras/mixtral_8_7b_en/4) | 46.70B | 32-layer Mixtral MoE model with 7 billionactive parameters and 8 experts per MoE layer. |
| [mixtral\_8\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mixtral/keras/mixtral_8_instruct_7b_en/4) | 46.70B | Instruction fine-tuned 32-layer Mixtral MoE modelwith 7 billion active parameters and 8 experts per MoE layer. |

* * *

[MixtralTokenizer](https://keras.io/keras_hub/api/models/mixtral/mixtral_tokenizer/#mixtraltokenizer)

[`MixtralTokenizer` class](https://keras.io/keras_hub/api/models/mixtral/mixtral_tokenizer/#mixtraltokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mixtral/mixtral_tokenizer/#frompreset-method)