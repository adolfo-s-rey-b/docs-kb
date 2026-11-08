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
 / [ViT](https://keras.io/keras_hub/api/models/vit/)
 / ViTImageClassifier model

ViTImageClassifier model
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/vit/vit_image_classifier.py#L13)

### `ViTImageClassifier` class

Copied!

`keras_hub.models.ViTImageClassifier(     backbone,     num_classes,     preprocessor=None,     pooling="token",     intermediate_dim=None,     activation=None,     dropout=0.0,     head_dtype=None,     **kwargs )`

ViT image classification task.

`ViTImageClassifier` tasks wrap a [`keras_hub.models.ViTBackbone`](https://keras.io/keras_hub/api/models/vit/vit_backbone#vitbackbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be used for image classification. `ViTImageClassifier` tasks take an additional `num_classes` argument, controlling the number of predicted output classes.

To fine-tune with `fit()`, pass a dataset containing tuples of `(x, y)` labels where `x` is a string and `y` is an integer from `[0, num_classes)`.\
\
Note that unlike `keras_hub.model.ImageClassifier`, the `ViTImageClassifier` we pluck out `cls_token` which is first seqence from the backbone.\
\
**Arguments**\
\
*   **backbone**: A [`keras_hub.models.ViTBackbone`](https://keras.io/keras_hub/api/models/vit/vit_backbone#vitbackbone-class)\
     instance or a [`keras.Model`](https://keras.io/api/models/model#model-class)\
    .\
*   **num\_classes**: int. The number of classes to predict.\
*   **preprocessor**: `None`, a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
     instance, a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)\
     instance, or a callable. If `None` no preprocessing will be applied to the inputs.\
*   **pooling**: String specifying the classification strategy. The choice impacts the dimensionality and nature of the feature vector used for classification. `"token"`: A single vector (class token) representing the overall image features. `"gap"`: A single vector representing the average features across the spatial dimensions.\
*   **intermediate\_dim**: Optional dimensionality of the intermediate representation layer before the final classification layer. If `None`, the output of the transformer is directly used. Defaults to `None`.\
*   **activation**: `None`, str, or callable. The activation function to use on the `Dense` layer. Set `activation=None` to return the output logits. Defaults to `"softmax"`.\
*   **head\_dtype**: `None`, str, or `keras.mixed_precision.DTypePolicy`. The dtype to use for the classification head's computations and weights.\
\
**Examples**\
\
Call `predict()` to run inference.\
\
Copied!\
\
`# Load preset and train images = np.random.randint(0, 256, size=(2, 224, 224, 3)) classifier = keras_hub.models.ViTImageClassifier.from_preset(     "vgg_16_imagenet" ) classifier.predict(images)`\
\
Call `fit()` on a single batch.\
\
Copied!\
\
`# Load preset and train images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] classifier = keras_hub.models.VGGImageClassifier.from_preset(     "vit_base_patch16_224" ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
Call `fit()` with custom loss, optimizer and backbone.\
\
Copied!\
\
`classifier = keras_hub.models.VGGImageClassifier.from_preset(     "vit_base_patch16_224" ) classifier.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5), ) classifier.backbone.trainable = False classifier.fit(x=images, y=labels, batch_size=2)`\
\
Custom backbone.\
\
Copied!\
\
`images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] model = keras_hub.models.ViTBackbone(     image_shape = (224, 224, 3),     patch_size=16,     num_layers=6,     num_heads=3,     hidden_dim=768,     mlp_dim=2048 ) classifier = keras_hub.models.ViTImageClassifier(     backbone=backbone,     num_classes=4, ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)\
\
### `from_preset` method\
\
Copied!\
\
`ViTImageClassifier.from_preset(preset, load_weights=True, **kwargs)`\
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
| [vit\_base\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch16_224_imagenet/4) | 85.80M | ViT-B16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |\
| [vit\_base\_patch16\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch16_224_imagenet21k/3) | 85.80M | ViT-B16 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [vit\_base\_patch16\_384\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch16_384_imagenet/4) | 86.09M | ViT-B16 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [vit\_base\_patch32\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch32_224_imagenet21k/3) | 87.46M | ViT-B32 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [vit\_base\_patch32\_384\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch32_384_imagenet/3) | 87.53M | ViT-B32 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [vit\_large\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch16_224_imagenet/4) | 303.30M | ViT-L16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |\
| [vit\_large\_patch16\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch16_224_imagenet21k/3) | 303.30M | ViT-L16 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [vit\_large\_patch16\_384\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch16_384_imagenet/4) | 303.69M | ViT-L16 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [vit\_large\_patch32\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch32_224_imagenet21k/3) | 305.51M | ViT-L32 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [vit\_large\_patch32\_384\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch32_384_imagenet/3) | 305.61M | ViT-L32 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [vit\_huge\_patch14\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_huge_patch14_224_imagenet21k/3) | 630.76M | ViT-H14 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
\
* * *\
\
### `backbone` property\
\
Copied!\
\
`keras_hub.models.ViTImageClassifier.backbone`\
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
`keras_hub.models.ViTImageClassifier.preprocessor`\
\
A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
 layer used to preprocess input.\
\
* * *\
\
[ViTImageClassifier model](https://keras.io/keras_hub/api/models/vit/vit_image_classifier/#vitimageclassifier-model)\
\
[`ViTImageClassifier` class](https://keras.io/keras_hub/api/models/vit/vit_image_classifier/#vitimageclassifier-class)\
\
[`from_preset` method](https://keras.io/keras_hub/api/models/vit/vit_image_classifier/#frompreset-method)\
\
[`backbone` property](https://keras.io/keras_hub/api/models/vit/vit_image_classifier/#backbone-property)\
\
[`preprocessor` property](https://keras.io/keras_hub/api/models/vit/vit_image_classifier/#preprocessor-property)