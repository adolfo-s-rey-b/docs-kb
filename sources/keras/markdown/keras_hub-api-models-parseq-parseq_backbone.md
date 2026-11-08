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
 / [PARSeq](https://keras.io/keras_hub/api/models/parseq/)
 / PARSeqBackbone model

PARSeqBackbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/parseq/parseq_backbone.py#L8)

### `PARSeqBackbone` class

Copied!

`keras_hub.models.PARSeqBackbone(     image_encoder,     vocabulary_size,     max_label_length,     decoder_hidden_dim,     num_decoder_layers,     num_decoder_heads,     decoder_mlp_dim,     dropout_rate=0.1,     attention_dropout=0.1,     dtype=None,     **kwargs )`

Scene Text Detection with PARSeq.

Performs OCR in natural scenes using the PARSeq model described in [Scene Text Recognition with Permuted Autoregressive Sequence Models](https://arxiv.org/abs/2207.06966)
. PARSeq is a ViT-based model that allows iterative decoding by performing an autoregressive decoding phase, followed by a refinement phase.

**Arguments**

*   **image\_encoder**: keras.Model. The image encoder model.
*   **vocabulary\_size**: int. The size of the vocabulary.
*   **max\_label\_length**: int. The maximum length of the label sequence.
*   **decoder\_hidden\_dim**: int. The dimension of the decoder hidden layers.
*   **num\_decoder\_layers**: int. The number of decoder layers.
*   **num\_decoder\_heads**: int. The number of attention heads in the decoder.
*   **decoder\_mlp\_dim**: int. The dimension of the decoder MLP hidden layer.
*   **dropout\_rate**: float. The dropout rate for the decoder network. Defaults to `0.1`.
*   **attention\_dropout**: float. The dropout rate for the attention weights. Defaults to `0.1`.
*   **dtype**: str. `None`, str, or `keras.mixed_precision.DTypePolicy`. The dtype to use for the computations and weights.
*   **\*\*kwargs**: Additional keyword arguments passed to the base [`keras.Model`](https://keras.io/api/models/model#model-class)
     constructor.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`PARSeqBackbone.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as a one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a ModelScope handle like `'modelscope://user/bert_base_en'`
5.  a path to a local preset directory like `'./bert_base_en'`

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Backbone.from_preset()`, or from a model class like `keras_hub.models.GemmaBackbone.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

For any `Backbone` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma backbone with pre-trained weights. model = keras_hub.models.Backbone.from_preset(     "gemma_2b_en", )  # Load a Bert backbone with a pre-trained config and random weights. model = keras_hub.models.Backbone.from_preset(     "bert_base_en",     load_weights=False, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [parseq](https://www.kaggle.com/models/keras/parseq/keras/parseq/1) | 23.83M | Permuted autoregressive sequence (PARSeq) base model for scene text recognition |

* * *

[PARSeqBackbone model](https://keras.io/keras_hub/api/models/parseq/parseq_backbone/#parseqbackbone-model)

[`PARSeqBackbone` class](https://keras.io/keras_hub/api/models/parseq/parseq_backbone/#parseqbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/parseq/parseq_backbone/#frompreset-method)