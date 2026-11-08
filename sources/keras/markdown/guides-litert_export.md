None

[Developer guides](https://keras.io/guides/)

[The Functional API](https://keras.io/guides/functional_api/)
 [The Sequential model](https://keras.io/guides/sequential_model/)
 [Making new layers & models via subclassing](https://keras.io/guides/making_new_layers_and_models_via_subclassing/)
 [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
 [Customizing \`fit()\` with JAX](https://keras.io/guides/custom_train_step_in_jax/)
 [Customizing \`fit()\` with TensorFlow](https://keras.io/guides/custom_train_step_in_tensorflow/)
 [Customizing \`fit()\` with PyTorch](https://keras.io/guides/custom_train_step_in_torch/)
 [Writing a custom training loop in JAX](https://keras.io/guides/writing_a_custom_training_loop_in_jax/)
 [Writing a custom training loop in TensorFlow](https://keras.io/guides/writing_a_custom_training_loop_in_tensorflow/)
 [Writing a custom training loop in PyTorch](https://keras.io/guides/writing_a_custom_training_loop_in_torch/)
 [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
 [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)
 [Writing your own callbacks](https://keras.io/guides/writing_your_own_callbacks/)
 [Transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
 [Distributed training with JAX](https://keras.io/guides/distributed_training_with_jax/)
 [Distributed training with TensorFlow](https://keras.io/guides/distributed_training_with_tensorflow/)
 [Distributed training with PyTorch](https://keras.io/guides/distributed_training_with_torch/)
 [Distributed training with Keras 3](https://keras.io/guides/distribution/)
 [Migrating Keras 2 code to Keras 3](https://keras.io/guides/migrating_to_keras_3/)
 [How to use Keras with NNX backend](https://keras.io/guides/keras_nnx_guide/)
 [Orbax Checkpointing in Keras](https://keras.io/guides/orbax_checkpoint/)
 [Quantization in Keras](https://keras.io/guides/quantization_overview/)
 [8-bit integer quantization in Keras](https://keras.io/guides/int8_quantization_in_keras/)
 [4-bit integer quantization in Keras](https://keras.io/guides/int4_quantization_in_keras/)
 [GPTQ quantization in Keras](https://keras.io/guides/gptq_quantization_in_keras/)
 [AWQ quantization in Keras](https://keras.io/guides/awq_quantization_in_keras/)
 [Writing quantization-compatible layers in Keras](https://keras.io/guides/writing_quantization_compatible_layers/)
 [Customizing quantization in Keras](https://keras.io/guides/customizing_quantization/)
 [Exporting Keras models to LiteRT](https://keras.io/guides/litert_export/)
 [Define a Custom TPU/GPU Kernel](https://keras.io/guides/define_custom_kernel/)

► [Developer guides](https://keras.io/guides/)
 / Exporting Keras models to LiteRT

Exporting Keras models to LiteRT
================================

**Author:** [Rahul Kumar](https://github.com/pctablet505)
  
**Date created:** 2025/12/10  
**Last modified:** 2026/07/06  
**Description:** Learn how to export Keras models to LiteRT for mobile and edge deployment using the PyTorch backend.

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/guides/ipynb/litert_export.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/guides/litert_export.py)

* * *

Introduction
------------

[LiteRT](https://ai.google.dev/edge/litert)
 (formerly TensorFlow Lite) lets you run machine learning models on mobile devices, embedded systems, and browsers with low latency and small binary size.

Keras provides a built-in `model.export()` API that converts your model to the LiteRT (`.tflite`) format in a single line of code. This guide covers the complete workflow:

1.  Export a Keras model to LiteRT.
2.  Run inference with the LiteRT interpreter.
3.  Handle different model types (Sequential, Functional, subclassed, multi-input).
4.  Resize inputs at runtime.
5.  Use the signature runner for named inputs and outputs.
6.  Quantize the model for smaller size and faster inference.

We will use the **PyTorch backend** because it produces models that are fully compatible with the new LiteRT Android runtime — no flex ops, no deprecated interpreter APIs. The same `model.export(..., format="litert")` API also works with the TensorFlow backend, which we summarize in a dedicated section at the end.

* * *

Setup
-----

Install the required packages. Since LiteRT export is under active development, install Keras and KerasHub from the master branch to get the latest fixes. Also install `litert-torch` from the master branch, which is required for LiteRT export with the PyTorch backend:

Copied!

`!pip install -q git+https://github.com/keras-team/keras.git !pip install -q git+https://github.com/keras-team/keras-hub.git !pip install -q git+https://github.com/google-ai-edge/litert-torch.git !pip install -q ai-edge-litert`

  `Preparing metadata (setup.py) ... [?25l[?25hdone`\
\
Set the PyTorch backend before importing Keras:\
\
Copied!\
\
`import os  os.environ["KERAS_BACKEND"] = "torch"  import numpy as np import keras  print("Keras version:", keras.__version__)`\
\
`Keras version: 3.16.0`\
\
* * *\
\
Export a simple model\
---------------------\
\
Build a small classifier and export it to LiteRT.\
\
Copied!\
\
`# Build a simple model model = keras.Sequential(     [         keras.layers.Dense(64, activation="relu", input_shape=(10,)),         keras.layers.Dense(64, activation="relu"),         keras.layers.Dense(10, activation="softmax"),     ] ) model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")  # Build weights with a sample input sample_input = np.random.random((1, 10)).astype("float32") _ = model(sample_input)  # Export to LiteRT model.export("model.tflite", format="litert") print("Exported to model.tflite")`\
\
``/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/dense.py:107: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.   super().__init__(activity_regularizer=activity_regularizer, **kwargs)  WARNING:torchao:Failed to load /usr/local/lib/python3.12/dist-packages/torchao/_C_cutlass_90a.abi3.so: Could not load this library: /usr/local/lib/python3.12/dist-packages/torchao/_C_cutlass_90a.abi3.so  WARNING:torchao:Failed to load /usr/local/lib/python3.12/dist-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so: Could not load this library: /usr/local/lib/python3.12/dist-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so``\
\
(00:00) \[START\] LiteRT-Torch Convert\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default (+00:01)\
\
(00:01) \[START\] LiteRT-Torch Convert > Run FX Passes\
\
(00:01) \[START\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions (+00:00)\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Run FX Passes (+00:00)\
\
(00:01) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default\
\
(00:01) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:01) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:01) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module (+00:00)\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default (+00:00)\
\
(00:01) \[START\] LiteRT-Torch Convert > Merge MLIR Modules\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Merge MLIR Modules (+00:00)\
\
(00:01) \[START\] LiteRT-Torch Convert > Run LiteRT Converter Passes\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Run LiteRT Converter Passes (+00:00)\
\
(00:01) \[ DONE\] LiteRT-Torch Convert (+00:01)\
\
(00:00) \[START\] Write Model to model.tflite\
\
(00:00) \[ DONE\] Write Model to model.tflite (+00:00)\
\
`Saved artifact at 'model.tflite'.  Exported to model.tflite`\
\
* * *\
\
Run inference with the LiteRT model\
-----------------------------------\
\
Load the exported `.tflite` file with `ai_edge_litert` and run inference.\
\
> **Important:** [`tf.lite.Interpreter`](https://www.tensorflow.org/api_docs/python/tf/lite/Interpreter)\
>  is deprecated and scheduled for deletion. Always use `ai_edge_litert.interpreter.Interpreter` for new code.\
\
Copied!\
\
`from ai_edge_litert.interpreter import Interpreter  interpreter = Interpreter(model_path="model.tflite") interpreter.allocate_tensors()  input_details = interpreter.get_input_details() output_details = interpreter.get_output_details()  print("Input shape :", input_details[0]["shape"]) print("Output shape:", output_details[0]["shape"])  interpreter.set_tensor(input_details[0]["index"], sample_input) interpreter.invoke() output = interpreter.get_tensor(output_details[0]["index"]) print("Inference output shape:", output.shape)`\
\
`Input shape : [ 1 10] Output shape: [ 1 10] Inference output shape: (1, 10)`\
\
* * *\
\
Working with different model types\
----------------------------------\
\
### Subclassed models\
\
For subclassed models, you must call the model on sample data before export so that Keras can infer the input signature and build the weights.\
\
Copied!\
\
`class TinyModel(keras.Model):     def __init__(self):         super().__init__()         self.dense1 = keras.layers.Dense(16, activation="relu")         self.dense2 = keras.layers.Dense(1)      def call(self, x):         return self.dense2(self.dense1(x))  subclass_model = TinyModel() subclass_model(np.zeros((1, 10), dtype="float32")) subclass_model.export("subclass_model.tflite", format="litert") print("Subclassed model exported")`\
\
(00:00) \[START\] LiteRT-Torch Convert\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Merge MLIR Modules\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Merge MLIR Modules (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run LiteRT Converter Passes\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run LiteRT Converter Passes (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert (+00:00)\
\
(00:00) \[START\] Write Model to subclass\_model.tflite\
\
(00:00) \[ DONE\] Write Model to subclass\_model.tflite (+00:00)\
\
`Saved artifact at 'subclass_model.tflite'.  Subclassed model exported`\
\
### Models with multiple inputs\
\
Copied!\
\
`input_a = keras.Input(shape=(10,), name="input_a") input_b = keras.Input(shape=(10,), name="input_b") merged = keras.layers.Concatenate()([input_a, input_b]) output = keras.layers.Dense(1)(merged) multi_input_model = keras.Model(inputs=[input_a, input_b], outputs=output)  a = np.random.random((1, 10)).astype("float32") b = np.random.random((1, 10)).astype("float32") _ = multi_input_model([a, b])  multi_input_model.export("multi_input_model.tflite", format="litert") print("Multi-input model exported")`\
\
(00:00) \[START\] LiteRT-Torch Convert\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module (+00:00)\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default (+00:00)\
\
(00:01) \[START\] LiteRT-Torch Convert > Merge MLIR Modules\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Merge MLIR Modules (+00:00)\
\
(00:01) \[START\] LiteRT-Torch Convert > Run LiteRT Converter Passes\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Run LiteRT Converter Passes (+00:00)\
\
(00:01) \[ DONE\] LiteRT-Torch Convert (+00:01)\
\
(00:00) \[START\] Write Model to multi\_input\_model.tflite\
\
(00:00) \[ DONE\] Write Model to multi\_input\_model.tflite (+00:00)\
\
`Saved artifact at 'multi_input_model.tflite'.  Multi-input model exported`\
\
### Models with dictionary inputs\
\
Dictionary inputs are also supported natively.\
\
Copied!\
\
`input_x = keras.Input(shape=(10,), name="x") input_y = keras.Input(shape=(10,), name="y") sum_output = keras.layers.Add()([input_x, input_y]) dict_model = keras.Model(inputs={"x": input_x, "y": input_y}, outputs=sum_output)  x_val = np.random.random((1, 10)).astype("float32") y_val = np.random.random((1, 10)).astype("float32") _ = dict_model({"x": x_val, "y": y_val})  dict_model.export("dict_model.tflite", format="litert") print("Dict-input model exported")`\
\
(00:00) \[START\] LiteRT-Torch Convert\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Merge MLIR Modules\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Merge MLIR Modules (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run LiteRT Converter Passes\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run LiteRT Converter Passes (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert (+00:00)\
\
(00:00) \[START\] Write Model to dict\_model.tflite\
\
(00:00) \[ DONE\] Write Model to dict\_model.tflite (+00:00)\
\
`Saved artifact at 'dict_model.tflite'.  Dict-input model exported`\
\
* * *\
\
Dynamic shapes and runtime input resizing\
-----------------------------------------\
\
LiteRT models exported from Keras have static shapes in the graph, but the interpreter supports **runtime input resizing**. This means you can process different batch sizes with the same exported model without re-exporting.\
\
> **Warning:** The new `ai_edge_litert.interpreter.Interpreter` does **not** support graphs with dynamic shapes. Models exported with the PyTorch backend and a `dynamic_shapes` argument may fail to run with this interpreter. If you need variable input shapes, use runtime input resizing (shown below) instead. Dynamic-shape export works when using the TensorFlow backend during conversion, but the resulting model should still be executed with a TFLite interpreter that supports dynamic tensors if you do not resize inputs to a fixed shape first.\
\
Copied!\
\
`interpreter = Interpreter(model_path="model.tflite") interpreter.allocate_tensors() input_details = interpreter.get_input_details()  # Resize from batch=1 to batch=4 interpreter.resize_tensor_input(input_details[0]["index"], [4, 10]) interpreter.allocate_tensors()  batch_input = np.random.random((4, 10)).astype("float32") interpreter.set_tensor(input_details[0]["index"], batch_input) interpreter.invoke() resized_output = interpreter.get_tensor(interpreter.get_output_details()[0]["index"]) print("Resized output shape:", resized_output.shape)`\
\
`Resized output shape: (4, 10)`\
\
* * *\
\
Signature runner\
----------------\
\
Use the signature runner for cleaner inference code. You can discover the input names for a signature via `get_signature_list()`; for models exported with the PyTorch backend they are typically `args_0`, `args_0_0`, etc.\
\
Copied!\
\
`interpreter = Interpreter(model_path="model.tflite") interpreter.allocate_tensors()  # Check available signatures print("Signatures:", interpreter.get_signature_list())  # Run inference using the signature runner runner = interpreter.get_signature_runner("serving_default") sig_output = runner(args_0=sample_input) print("Signature runner output shape:", list(sig_output.values())[0].shape)`\
\
`Signatures: {'serving_default': {'inputs': ['args_0'], 'outputs': ['output_0']}} Signature runner output shape: (1, 10)`\
\
* * *\
\
Custom input signature\
----------------------\
\
You can override the inferred input signature by passing `input_signature` to `export()`. This is useful when you want to enforce specific shapes or dtypes.\
\
> **Note:** `None` in an `InputSpec` shape (e.g., `shape=(None, 10)`) tells Keras that the dimension is unknown, but the exported LiteRT graph still uses a concrete batch size (1) for tracing. Use runtime resizing (shown above) to handle variable batch sizes at inference time.\
\
Copied!\
\
`model = keras.Sequential(     [         keras.layers.Dense(64, activation="relu", input_shape=(10,)),         keras.layers.Dense(10, activation="softmax"),     ] ) model.compile() model(np.zeros((1, 10), dtype="float32"))  custom_sig = [keras.layers.InputSpec(shape=(None, 10), dtype="float32")] model.export("custom_sig_model.tflite", format="litert", input_signature=custom_sig) print("Exported with custom input signature")`\
\
``/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/dense.py:107: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.   super().__init__(activity_regularizer=activity_regularizer, **kwargs)``\
\
(00:00) \[START\] LiteRT-Torch Convert\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Merge MLIR Modules\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Merge MLIR Modules (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run LiteRT Converter Passes\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run LiteRT Converter Passes (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert (+00:00)\
\
(00:00) \[START\] Write Model to custom\_sig\_model.tflite\
\
(00:00) \[ DONE\] Write Model to custom\_sig\_model.tflite (+00:00)\
\
`Saved artifact at 'custom_sig_model.tflite'.  Exported with custom input signature`\
\
* * *\
\
Export a KerasHub model\
-----------------------\
\
The same API works for KerasHub presets. Here we export **Gemma 3 270M**, a lightweight language model that is small enough to run on edge devices.\
\
Copied!\
\
`import keras_hub  try:     preset = "gemma3_270m"     preprocessor = keras_hub.models.Gemma3CausalLMPreprocessor.from_preset(         preset, sequence_length=32     )     model = keras_hub.models.Gemma3CausalLM.from_preset(         preset, preprocessor=preprocessor     )      print(f"Loaded {preset}")      # Build weights with a sample input. Use generate_preprocess for inference.     sample_text = {"prompts": ["Hello"]}     sample_input = preprocessor.generate_preprocess(sample_text)     _ = model(sample_input)      model.export("gemma3_270m.tflite", format="litert")     print("Exported to gemma3_270m.tflite") except Exception as e:     print(f"Gemma3 export skipped: {e}")`\
\
`Gemma3 export skipped: 403 Client Error.  You don't have permission to access resource at URL: https://kaggle.com/models/keras/gemma3/keras/gemma3_270m/3 Please make sure you are authenticated if you are trying to access a private resource or a resource requiring consent.`\
\
* * *\
\
Quantization for smaller models\
-------------------------------\
\
Quantization reduces model size and can speed up inference on edge devices.\
\
### Built-in dynamic range quantization\
\
Pass `optimizations` to `model.export()`. This works on both the TensorFlow and PyTorch backends and quantizes weights to 8-bit integers while keeping activations in float32. This typically gives **~4× size reduction**.\
\
Copied!\
\
`import tensorflow as tf  model = keras.Sequential(     [         keras.layers.Dense(64, activation="relu", input_shape=(10,)),         keras.layers.Dense(64, activation="relu"),         keras.layers.Dense(10, activation="softmax"),     ] ) model.compile() model(np.zeros((1, 10), dtype="float32"))  model.export(     "model_dynamic_quant.tflite",     format="litert",     optimizations=[tf.lite.Optimize.DEFAULT], ) print("Exported dynamically quantized model")`\
\
``/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/dense.py:107: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.   super().__init__(activity_regularizer=activity_regularizer, **kwargs)``\
\
(00:00) \[START\] LiteRT-Torch Convert\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Torch Export: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes\
\
(00:00) \[START\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Run FX Passes (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
``/usr/lib/python3.12/copyreg.py:99: FutureWarning: `isinstance(treespec, LeafSpec)` is deprecated, use `isinstance(treespec, TreeSpec) and treespec.is_leaf()` instead.   return cls.__new__(cls, *args)``\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > ExportedProgram Run Decompositions (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default > Create MLIR Module (+00:00)\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Lower to MLIR: serving\_default (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Merge MLIR Modules\
\
(00:00) \[ DONE\] LiteRT-Torch Convert > Merge MLIR Modules (+00:00)\
\
(00:00) \[START\] LiteRT-Torch Convert > Run LiteRT Converter Passes\
\
(00:01) \[ DONE\] LiteRT-Torch Convert > Run LiteRT Converter Passes (+00:00)\
\
(00:01) \[ DONE\] LiteRT-Torch Convert (+00:01)\
\
(00:00) \[START\] Write Model to model\_dynamic\_quant.tflite\
\
(00:00) \[ DONE\] Write Model to model\_dynamic\_quant.tflite (+00:00)\
\
`Saved artifact at 'model_dynamic_quant.tflite'.  Exported dynamically quantized model`\
\
### Post-export quantization with ai-edge-quantizer\
\
For finer-grained control (e.g. channel-wise symmetric INT8 weights, mixed precision, or per-layer recipes), use the **AI Edge Quantizer** on the already-exported `.tflite` file. This works consistently across both backends.\
\
Install it:\
\
Copied!\
\
`pip install -q ai-edge-quantizer`\
\
Copied!\
\
`from ai_edge_quantizer import quantizer, qtyping  qt = quantizer.Quantizer("model.tflite")  # Recipe: channel-wise symmetric INT8 weights, FP32 activations. recipe = [     {         "regex": ".*",         "operation": qtyping.TFLOperationName.ALL_SUPPORTED,         "algorithm_key": quantizer.AlgorithmName.MIN_MAX_UNIFORM_QUANT,         "op_config": {             "weight_tensor_config": {                 "dtype": qtyping.TensorDataType.INT,                 "num_bits": 8,                 "granularity": qtyping.QuantGranularity.CHANNELWISE,                 "symmetric": True,             },             "compute_precision": qtyping.ComputePrecision.FLOAT,             "explicit_dequantize": False,         },     }, ]  qt.load_quantization_recipe(recipe)  # No calibration needed for this weight-only recipe. quant_result = qt.quantize() quant_result.save(".", model_name="model_aieq")  print("Exported ai-edge-quantizer model")`\
\
`Model name: model.tflite Original model size: 22.68 KiB Quantized model size: 22.66 KiB Quantization Ratio: 1.00 (1.0x smaller) Total time: 3.40 ms Exported ai-edge-quantizer model`\
\
The AI Edge Quantizer typically achieves: - **Similar file size** to TFLite dynamic-range quantization - **Better perplexity / BLEU scores** on generative tasks thanks to channel-wise symmetric scaling - **No calibration required** for weight-only recipes\
\
* * *\
\
Compare file sizes\
------------------\
\
Copied!\
\
`def file_size_mb(path):     return os.path.getsize(path) / (1024 * 1024)  print(f"\nOriginal     : {file_size_mb('model.tflite'):.1f} MB") print(f"Dynamic INT8 : {file_size_mb('model_dynamic_quant.tflite'):.1f} MB") print(f"AI Edge Quant: {file_size_mb('model_aieq.tflite'):.1f} MB")`\
\
`Original     : 0.0 MB Dynamic INT8 : 0.0 MB AI Edge Quant: 0.0 MB`\
\
* * *\
\
Android dependencies\
--------------------\
\
To use a LiteRT model in an Android app, add one of the following dependencies to your `build.gradle`:\
\
### New LiteRT runtime (recommended)\
\
Use this for models exported with the PyTorch backend. No flex ops are required.\
\
Copied!\
\
`implementation 'com.google.ai.edge.litert:litert:2.1.5'`\
\
### Legacy TensorFlow Lite runtime\
\
Use this only if you have older `.tflite` models that still require it. Note that [`tf.lite.Interpreter`](https://www.tensorflow.org/api_docs/python/tf/lite/Interpreter)\
 is deprecated.\
\
Copied!\
\
`implementation 'org.tensorflow:tensorflow-lite:2.16.1'`\
\
If your model contains flex ops (e.g. from TF backend export), also add:\
\
Copied!\
\
`implementation 'org.tensorflow:tensorflow-lite-select-tf-ops:2.16.1'`\
\
Models exported with the **PyTorch backend do not contain flex ops**, so the `select-tf-ops` dependency is not needed.\
\
* * *\
\
TensorFlow backend alternative\
------------------------------\
\
The same `model.export(..., format="litert")` API works with the TensorFlow backend. The differences are:\
\
1.  **Converter path:** Uses `tf.lite.TFLiteConverter.from_saved_model()`.\
2.  **Flex ops:** Enabled by default via `SELECT_TF_OPS`. These ops are not supported by the new LiteRT Android runtime.\
3.  **Interpreter:** The legacy [`tf.lite.Interpreter`](https://www.tensorflow.org/api_docs/python/tf/lite/Interpreter)\
     is deprecated. Use `ai_edge_litert.interpreter.Interpreter` for new code.\
4.  **Extra kwargs:** `target_spec` and `representative_dataset` are supported.\
\
Example:\
\
Copied!\
\
`import os os.environ["KERAS_BACKEND"] = "tensorflow"  import keras import tensorflow as tf  model = keras.Sequential([     keras.layers.Dense(64, activation="relu", input_shape=(10,)),     keras.layers.Dense(10, activation="softmax"), ]) model.compile() model(np.zeros((1, 10), dtype="float32"))  # Export with Float16 quantization model.export(     "model_f16.tflite",     format="litert",     optimizations=[tf.lite.Optimize.DEFAULT],     target_spec={"supported_types": [tf.float16]}, )`\
\
* * *\
\
Backend comparison\
------------------\
\
| Feature | TensorFlow backend | PyTorch backend (recommended) |\
| --- | --- | --- |\
| Converter path | [`tf.lite.TFLiteConverter`](https://www.tensorflow.org/api_docs/python/tf/lite/TFLiteConverter) | `litert-torch` via `ExportedProgram` |\
| Flex ops | Enabled by default | **Not generated** |\
| Android runtime | May crash on new LiteRT | Fully compatible |\
| Interpreter | [`tf.lite.Interpreter`](https://www.tensorflow.org/api_docs/python/tf/lite/Interpreter)<br> (deprecated) | `ai_edge_litert.interpreter.Interpreter` |\
| `optimizations` kwarg | Supported | Supported |\
| `target_spec` kwarg | Supported | **Not supported** |\
| `representative_dataset` | Supported | **Not supported** |\
| Post-export `ai-edge-quantizer` | Supported | **Supported** |\
| Runtime input resizing | Supported | **Supported** |\
\
* * *\
\
Best practices\
--------------\
\
1.  **Always test the exported model** before deploying — run inference and compare outputs with the original Keras model.\
2.  **Use the PyTorch backend** for LiteRT export to avoid flex ops and ensure compatibility with the new LiteRT Android runtime.\
3.  **Call subclassed models on sample data** before `export()` to build weights and infer the input signature.\
4.  **Use runtime input resizing** for variable batch sizes rather than `dynamic_shapes`. Graphs with dynamic shapes are not supported by the new `ai_edge_litert.interpreter.Interpreter` and may fail when exported with the PyTorch backend.\
5.  **Start with `optimizations=[tf.lite.Optimize.DEFAULT]`** for quick dynamic-range quantization on either backend.\
6.  **Use `ai-edge-quantizer`** when you need finer control (channel-wise, symmetric, mixed-precision) or when targeting the PyTorch backend with Float16.\
7.  **Keep models under 2 GB per TFLite file** — LiteRT uses a flatbuffer format with a 2 GB limit per file. If your model is larger, use the `litert-lm` / `litert-lm-builder` pipeline which shards the model into multiple sub-models inside a `.litertlm` container.\
\
* * *\
\
Troubleshooting\
---------------\
\
| Issue | Solution |\
| --- | --- |\
| `ImportError` for `ai_edge_litert` | Run `pip install ai-edge-litert` |\
| `ImportError` for `litert_torch` | Run `pip install litert-torch` |\
| Shape mismatch at inference | Verify the input shape matches what the model expects, or use `resize_tensor_input()` |\
| Subclassed model fails to export | Call the model on sample data before `export()` to build weights |\
| Unsupported ops on PyTorch | Some ops may not yet be supported by `litert-torch`; try TF backend or simplify the model |\
| Out of memory during export | Try quantization or export on a machine with more RAM |\
| Flex ops on Android | Re-export with `KERAS_BACKEND=torch` |\
\
[Exporting Keras models to LiteRT](https://keras.io/guides/litert_export/#exporting-keras-models-to-litert)\
\
[Introduction](https://keras.io/guides/litert_export/#introduction)\
\
[Setup](https://keras.io/guides/litert_export/#setup)\
\
[Export a simple model](https://keras.io/guides/litert_export/#export-a-simple-model)\
\
[Run inference with the LiteRT model](https://keras.io/guides/litert_export/#run-inference-with-the-litert-model)\
\
[Working with different model types](https://keras.io/guides/litert_export/#working-with-different-model-types)\
\
[Subclassed models](https://keras.io/guides/litert_export/#subclassed-models)\
\
[Models with multiple inputs](https://keras.io/guides/litert_export/#models-with-multiple-inputs)\
\
[Models with dictionary inputs](https://keras.io/guides/litert_export/#models-with-dictionary-inputs)\
\
[Dynamic shapes and runtime input resizing](https://keras.io/guides/litert_export/#dynamic-shapes-and-runtime-input-resizing)\
\
[Signature runner](https://keras.io/guides/litert_export/#signature-runner)\
\
[Custom input signature](https://keras.io/guides/litert_export/#custom-input-signature)\
\
[Export a KerasHub model](https://keras.io/guides/litert_export/#export-a-kerashub-model)\
\
[Quantization for smaller models](https://keras.io/guides/litert_export/#quantization-for-smaller-models)\
\
[Built-in dynamic range quantization](https://keras.io/guides/litert_export/#builtin-dynamic-range-quantization)\
\
[Post-export quantization with ai-edge-quantizer](https://keras.io/guides/litert_export/#postexport-quantization-with-aiedgequantizer)\
\
[Compare file sizes](https://keras.io/guides/litert_export/#compare-file-sizes)\
\
[Android dependencies](https://keras.io/guides/litert_export/#android-dependencies)\
\
[New LiteRT runtime (recommended)](https://keras.io/guides/litert_export/#new-litert-runtime-recommended)\
\
[Legacy TensorFlow Lite runtime](https://keras.io/guides/litert_export/#legacy-tensorflow-lite-runtime)\
\
[TensorFlow backend alternative](https://keras.io/guides/litert_export/#tensorflow-backend-alternative)\
\
[Backend comparison](https://keras.io/guides/litert_export/#backend-comparison)\
\
[Best practices](https://keras.io/guides/litert_export/#best-practices)\
\
[Troubleshooting](https://keras.io/guides/litert_export/#troubleshooting)