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
 / [Swin Transformer](https://keras.io/keras_hub/api/models/swin_transformer/)
 / SwinTransformerImageClassifier model

SwinTransformerImageClassifier model
====================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/swin_transformer/swin_transformer_image_classifier.py#L15)

### `SwinTransformerImageClassifier` class

Copied!

`keras_hub.models.SwinTransformerImageClassifier(     backbone,     num_classes,     preprocessor=None,     activation=None,     dropout=0.0,     head_dtype=None,     **kwargs )`

Swin Transformer image classification task.

`SwinTransformerImageClassifier` tasks wrap a [`keras_hub.models.SwinTransformerBackbone`](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_backbone#swintransformerbackbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be used for image classification. The classifier pools the backbone output over the sequence dimension and applies a dense classification head.

To fine-tune with `fit()`, pass a dataset containing tuples of `(x, y)` labels where `x` is an image and `y` is an integer from `[0, num_classes)`.\
\
**Arguments**\
\
*   **backbone**: A [`keras_hub.models.SwinTransformerBackbone`](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_backbone#swintransformerbackbone-class)\
     instance or a [`keras.Model`](https://keras.io/api/models/model#model-class)\
    .\
*   **num\_classes**: int. The number of classes to predict.\
*   **preprocessor**: `None`, a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
     instance, a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)\
     instance, or a callable. If `None` no preprocessing will be applied to the inputs.\
*   **activation**: `None`, str, or callable. The activation function to use on the `Dense` layer. Set `activation=None` to return the output logits. Defaults to `None`.\
*   **head\_dtype**: `None`, str, or `keras.mixed_precision.DTypePolicy`. The dtype to use for the classification head's computations and weights.\
*   **dropout**: float. Dropout rate applied before the classification head. Defaults to `0.0`.\
\
**Examples**\
\
Call `predict()` to run inference.\
\
Copied!\
\
`images = np.random.randint(0, 256, size=(2, 224, 224, 3)) classifier = keras_hub.models.SwinTransformerImageClassifier.from_preset(     "swin_tiny_patch4_window7_224" ) classifier.predict(images)`\
\
Call `fit()` on a single batch.\
\
Copied!\
\
`images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] classifier = keras_hub.models.SwinTransformerImageClassifier.from_preset(     "swin_tiny_patch4_window7_224" ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
Custom backbone.\
\
Copied!\
\
`images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] backbone = keras_hub.models.SwinTransformerBackbone(     image_shape=(224, 224, 3),     embed_dim=96,     depths=(2, 2, 6, 2),     num_heads=(3, 6, 12, 24),     window_size=7, ) classifier = keras_hub.models.SwinTransformerImageClassifier(     backbone=backbone,     num_classes=4, ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)\
\
### `from_preset` method\
\
Copied!\
\
`SwinTransformerImageClassifier.from_preset(preset, load_weights=True, **kwargs)`\
\
Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)\
 from a model preset.\
\
A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:\
\
1.  a built-in preset identifier like `'bert_base_en'`\
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`\
3.  a Hugging Face handle like `'hf://user/bert_base_en'`\
4.  a path to a local preset directory like `'./bert_base_en'`\
\
For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.\
\
This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.\
\
**Arguments**\
\
*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.\
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.\
\
**Examples**\
\
Copied!\
\
`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`\
\
| Preset | Parameters | Description |\
| --- | --- | --- |\
| [swin\_tiny\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_tiny_patch4_window7_224/1) | 27.52M | Swin-Tiny model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |\
| [swin\_small\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_small_patch4_window7_224/1) | 48.84M | Swin-Small model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |\
| [swin\_base\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_base_patch4_window7_224/1) | 86.74M | Swin-Base model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |\
| [swin\_base\_patch4\_window12\_384](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_base_patch4_window12_384/1) | 86.88M | Swin-Base model pre-trained on the ImageNet 1k dataset with image resolution of 384x384. |\
| [swin\_large\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_large_patch4_window7_224/1) | 195.00M | Swin-Large model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |\
| [swin\_large\_patch4\_window12\_384](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_large_patch4_window12_384/1) | 195.20M | Swin-Large model pre-trained on the ImageNet 1k dataset with image resolution of 384x384. |\
\
* * *\
\
### `backbone` property\
\
Copied!\
\
`keras_hub.models.SwinTransformerImageClassifier.backbone`\
\
A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)\
 model with the core architecture.\
\
* * *\
\
### `preprocessor` property\
\
Copied!\
\
`keras_hub.models.SwinTransformerImageClassifier.preprocessor`\
\
A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
 layer used to preprocess input.\
\
* * *\
\
[SwinTransformerImageClassifier model](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_image_classifier/#swintransformerimageclassifier-model)\
\
[`SwinTransformerImageClassifier` class](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_image_classifier/#swintransformerimageclassifier-class)\
\
[`from_preset` method](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_image_classifier/#frompreset-method)\
\
[`backbone` property](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_image_classifier/#backbone-property)\
\
[`preprocessor` property](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_image_classifier/#preprocessor-property)