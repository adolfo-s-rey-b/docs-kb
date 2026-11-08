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
 / [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 / Backbone

Backbone
========

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L10)

### `Backbone` class

Copied!

`keras_hub.models.Backbone(*args, dtype=None, **kwargs)`

Base class for all `Backbone` models.

A `Backbone` is the basic architecture for a given NLP model. Unlike a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
, a `Backbone` is not tailored to any specific loss function and training setup. A `Backbone` generally outputs the last hidden states of an architecture before any output predictions.

A `Backbone` can be used in one of two ways:

1.  Through a `Task` class, which will wrap and extend a `Backbone` so it can be used with high level Keras functions like `fit()`, `predict()` or `evaluate()`. `Task` classes are built with a particular training objective in mind (e.g. classification or language modeling).
2.  Directly, by extending underlying functional model with additional outputs and training setup. This is the most flexible approach, and can allow for any outputs, loss, or custom training loop.

All backbones include a `from_preset()` constructor which can be used to load a pre-trained config and weights.

**Example**

Copied!

`# Load a BERT backbone with pre-trained weights. backbone = keras_hub.models.Backbone.from_preset(     "bert_base_en", ) # Load a GPT2 backbone with pre-trained weights at bfloat16 precision. backbone = keras_hub.models.Backbone.from_preset(     "gpt2_base_en",     dtype="bfloat16",     trainable=False, )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`Backbone.from_preset(preset, load_weights=True, **kwargs)`

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

**Guides and examples using `from_preset`**

*   [Uploading Models](https://keras.io/keras_hub/guides/upload/)
    
*   [Semantic Segmentation](https://keras.io/keras_hub/guides/semantic_segmentation_deeplab_v3/)
    
*   [Object Detection Fine-tuning with KerasHub](https://keras.io/keras_hub/guides/object_detection_retinanet/)
    

* * *

### `token_embedding` property

Copied!

`keras_hub.models.Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`Backbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L226)

### `save_lora_weights` method

Copied!

`Backbone.save_lora_weights(filepath)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L255)

### `load_lora_weights` method

Copied!

`Backbone.load_lora_weights(filepath)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L179)

### `save_to_preset` method

Copied!

`Backbone.save_to_preset(preset_dir, max_shard_size=10)`

Save backbone to a preset directory.

**Arguments**

*   **preset\_dir**: The path to the local model preset directory.
*   **max\_shard\_size**: `int` or `float`. Maximum size in GB for each sharded file. If `None`, no sharding will be done. Defaults to `10`.

* * *

[Backbone](https://keras.io/keras_hub/api/base_classes/backbone/#backbone)

[`Backbone` class](https://keras.io/keras_hub/api/base_classes/backbone/#backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/base_classes/backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/base_classes/backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/base_classes/backbone/#enablelora-method)

[`save_lora_weights` method](https://keras.io/keras_hub/api/base_classes/backbone/#saveloraweights-method)

[`load_lora_weights` method](https://keras.io/keras_hub/api/base_classes/backbone/#loadloraweights-method)

[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/backbone/#savetopreset-method)