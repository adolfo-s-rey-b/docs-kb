None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Layers API](https://keras.io/api/layers/)
 / [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 / TorchModuleWrapper layer

TorchModuleWrapper layer
========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/torch_utils.py#L14)

### `TorchModuleWrapper` class

Copied!

`keras.layers.TorchModuleWrapper(module, name=None, output_shape=None, **kwargs)`

Torch module wrapper layer.

`TorchModuleWrapper` is a wrapper class that can turn any `torch.nn.Module` into a Keras layer, in particular by making its parameters trackable by Keras.

`TorchModuleWrapper` is only compatible with the PyTorch backend and cannot be used with the TensorFlow or JAX backends.

**Arguments**

*   **module**: `torch.nn.Module` instance. If it's a `LazyModule` instance, then its parameters must be initialized before passing the instance to `TorchModuleWrapper` (e.g. by calling it once).
*   \_\_output\_shape \_\_:The shape of the output of this layer. It helps Keras perform automatic shape inference.
*   **name**: The name of the layer (string).

**Example**

Here's an example of how the `TorchModuleWrapper` can be used with vanilla PyTorch modules.

Copied!

``import torch import torch.nn as nn import torch.nn.functional as F  import keras from keras.layers import TorchModuleWrapper  class Classifier(keras.Model):     def __init__(self, **kwargs):         super().__init__(**kwargs)         # Wrap `torch.nn.Module`s with `TorchModuleWrapper`         # if they contain parameters         self.conv1 = TorchModuleWrapper(             nn.Conv2d(in_channels=1, out_channels=32, kernel_size=(3, 3))         )         self.conv2 = TorchModuleWrapper(             nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3))         )         self.pool = nn.MaxPool2d(kernel_size=(2, 2))         self.flatten = nn.Flatten()         self.dropout = nn.Dropout(p=0.5)         self.fc = TorchModuleWrapper(nn.Linear(1600, 10))      def call(self, inputs):         x = F.relu(self.conv1(inputs))         x = self.pool(x)         x = F.relu(self.conv2(x))         x = self.pool(x)         x = self.flatten(x)         x = self.dropout(x)         x = self.fc(x)         return F.softmax(x, dim=1)  model = Classifier() model.build((1, 28, 28)) print("# Output shape", model(torch.ones(1, 1, 28, 28).to("cuda")).shape)  model.compile(     loss="sparse_categorical_crossentropy",     optimizer="adam",     metrics=["accuracy"] ) model.fit(train_loader, epochs=5)``

* * *

[TorchModuleWrapper layer](https://keras.io/api/layers/backend_specific_layers/torch_module_wrapper/#torchmodulewrapper-layer)

[`TorchModuleWrapper` class](https://keras.io/api/layers/backend_specific_layers/torch_module_wrapper/#torchmodulewrapper-class)