[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#from_config)
        
    *   [parameters](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#parameters)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.TorchModuleWrapper Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#from_config)
        
    *   [parameters](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TorchModuleWrapper?version=stable#parameters)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/torch_utils.py#L14-L193)

Torch module wrapper layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.TorchModuleWrapper(
        module, name=None, output_shape=None, **kwargs
    )

`TorchModuleWrapper` is a wrapper class that can turn any `torch.nn.Module` into a Keras layer, in particular by making its parameters trackable by Keras.

`TorchModuleWrapper` is only compatible with the PyTorch backend and cannot be used with the TensorFlow or JAX backends.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `module` | `torch.nn.Module` instance. If it's a `LazyModule` instance, then its parameters must be initialized before passing the instance to `TorchModuleWrapper` (e.g. by calling it once). output\_shape :The shape of the output of this layer. It helps Keras perform automatic shape inference. |
| `name` | The name of the layer (string). |

#### Example:

Here's an example of how the `TorchModuleWrapper` can be used with vanilla PyTorch modules.

import torch
    import torch.nn as nn
    import torch.nn.functional as F
    
    import keras
    from keras.layers import TorchModuleWrapper
    
    class Classifier(keras.Model):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            # Wrap `torch.nn.Module`s with `TorchModuleWrapper`
            # if they contain parameters
            self.conv1 = TorchModuleWrapper(
                nn.Conv2d(in_channels=1, out_channels=32, kernel_size=(3, 3))
            )
            self.conv2 = TorchModuleWrapper(
                nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3))
            )
            self.pool = nn.MaxPool2d(kernel_size=(2, 2))
            self.flatten = nn.Flatten()
            self.dropout = nn.Dropout(p=0.5)
            self.fc = TorchModuleWrapper(nn.Linear(1600, 10))
    
        def call(self, inputs):
            x = F.relu(self.conv1(inputs))
            x = self.pool(x)
            x = F.relu(self.conv2(x))
            x = self.pool(x)
            x = self.flatten(x)
            x = self.dropout(x)
            x = self.fc(x)
            return F.softmax(x, dim=1)
    
    
    model = Classifier()
    model.build((1, 28, 28))
    print("Output shape:", model(torch.ones(1, 1, 28, 28).to("cuda")).shape)
    
    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"]
    )
    model.fit(train_loader, epochs=5)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/torch_utils.py#L165-L193)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `parameters`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/torch_utils.py#L107-L108)

parameters(
        recurse=True
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.