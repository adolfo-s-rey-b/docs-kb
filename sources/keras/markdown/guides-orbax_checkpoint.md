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
 / Orbax Checkpointing in Keras

Orbax Checkpointing in Keras
============================

**Author:** [Samaneh Saadat](https://github.com/SamanehSaadat/)
, [Amit Srivastava](https://github.com/amitsrivastava78)
  
**Date created:** 2025/11/20  
**Last modified:** 2026/03/04  
**Description:** Save and load Orbax checkpoints with distributed resharding.

Introduction
------------

[Orbax](https://orbax.readthedocs.io/)
 is the recommended checkpointing library for the JAX ecosystem. It provides high-level functionality for checkpoint management, composable serialization, and multi-host coordination.

Starting with Keras 3.14, the built-in [`keras.callbacks.OrbaxCheckpoint`](https://keras.io/api/callbacks/orbax_checkpoint#orbaxcheckpoint-class)
 callback makes it easy to:

*   Save and restore model checkpoints (weights, optimizer state, metrics) during training.
*   Resume training seamlessly from the latest checkpoint.
*   Use `save_best_only` monitoring (just like `ModelCheckpoint`).
*   Run in **multi-host distributed** environments with automatic coordination.
*   **Reshard** checkpoints when loading under a different distribution layout than the one used at save time.

Setup
-----

Install the Orbax checkpointing library:

Copied!

`!pip install -q -U orbax-checkpoint`

`[[34;49mnotice[1;39;49m][39;49m To update, run: [32;49mpip install --upgrade pip`\
\
Set the Keras backend to JAX, configure virtual devices for the distributed demo, and import the required libraries.\
\
Copied!\
\
`import os  os.environ["KERAS_BACKEND"] = "jax"  import shutil  import jax import keras import numpy as np  # Simulate 4 CPU devices for the distributed demo. # Remove this line if using real multi-device hardware. jax.config.update("jax_num_cpu_devices", 4)`\
\
Basic Usage\
-----------\
\
`OrbaxCheckpoint` works like `ModelCheckpoint` — pass it as a callback to `model.fit()`. No boilerplate classes or wrappers are needed.\
\
### Define a model and dataset\
\
Copied!\
\
`def get_model():     inputs = keras.Input(shape=(32,))     x = keras.layers.Dense(64, activation="relu", name="dense_1")(inputs)     outputs = keras.layers.Dense(1, name="dense_2")(x)     model = keras.Model(inputs, outputs)     model.compile(optimizer="adam", loss="mse")     return model  model = get_model() x_train = np.random.random((256, 32)) y_train = np.random.random((256, 1))`\
\
### Save a checkpoint every epoch\
\
Copied!\
\
`checkpoint_dir = "/tmp/orbax_ckpt_basic" shutil.rmtree(checkpoint_dir, ignore_errors=True)  callback = keras.callbacks.OrbaxCheckpoint(     directory=checkpoint_dir,     max_to_keep=3, )  history = model.fit(     x_train,     y_train,     batch_size=32,     epochs=3,     verbose=1,     validation_split=0.2,     callbacks=[callback], )`\
\
`Epoch 1/3  7/7 ━━━━━━━━━━━━━━━━━━━━ 3s 518ms/step - loss: 0.1514 - val_loss: 0.1539  Epoch 2/3  1/7 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 0.1336  WARNING:absl:[process=0][thread=Thread-10 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_basic/0.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 0.1314 - val_loss: 0.1384  Epoch 3/3  1/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.0898  WARNING:absl:[process=0][thread=Thread-16 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_basic/1.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 0.1183 - val_loss: 0.1264  WARNING:absl:[process=0][thread=Thread-23 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_basic/2.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,` \
\
The checkpoint directory now contains a step-directory for each saved epoch.\
\
Copied!\
\
`!ls /tmp/orbax_ckpt_basic`\
\
`/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pty.py:95: RuntimeWarning: os.fork() was called. os.fork() is incompatible with multithreaded code, and JAX is multithreaded, so this will likely lead to a deadlock.   pid, fd = os.forkpty()  0[m[m 1[m[m 2[m[m`\
\
Loading a model from an Orbax checkpoint\
----------------------------------------\
\
Use `keras.saving.load_model()` to reload a full model (config + weights + optimizer state) from an Orbax checkpoint directory.\
\
Copied!\
\
`loaded_model = keras.saving.load_model(checkpoint_dir) loaded_model.summary()`\
\
`/Users/amitsrivasta/work/keras/venv_test/lib/python3.13/site-packages/orbax/checkpoint/_src/serialization/jax_array_handlers.py:701: UserWarning: Sharding info not provided when restoring. Populating sharding info from sharding file. Please note restoration time will be slightly increased due to reading from file. Note also that this option is unsafe when restoring on a different topology than the checkpoint was saved with.   warnings.warn(`\
\
Model: "functional"\
\
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓\
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃\
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩\
│ input\_layer (InputLayer)        │ (None, 32)             │             0 │\
├─────────────────────────────────┼────────────────────────┼───────────────┤\
│ dense\_1 (Dense)                 │ (None, 64)             │         2,112 │\
├─────────────────────────────────┼────────────────────────┼───────────────┤\
│ dense\_2 (Dense)                 │ (None, 1)              │            65 │\
└─────────────────────────────────┴────────────────────────┴───────────────┘\
\
 Total params: 6,533 (25.52 KB)\
\
 Trainable params: 2,177 (8.50 KB)\
\
 Non-trainable params: 0 (0.00 B)\
\
 Optimizer params: 4,356 (17.02 KB)\
\
Loading weights only\
--------------------\
\
If you already have a model instance and just want to load the weights, use `load_weights()`:\
\
Copied!\
\
`fresh_model = get_model() fresh_model.load_weights(checkpoint_dir)  # Verify both loaded_model and fresh_model match the original. for m in [loaded_model, fresh_model]:     for orig, restored in zip(model.weights, m.weights):         np.testing.assert_allclose(orig.numpy(), restored.numpy(), atol=1e-6) print("Weights match!")`\
\
`Weights match!`\
\
Resuming training\
-----------------\
\
When you pass `OrbaxCheckpoint` to a new `fit()` call, training resumes from the correct step number. Pass `initial_epoch` to continue the epoch count from where you left off.\
\
Copied!\
\
`resumed_model = keras.saving.load_model(checkpoint_dir)  # Create a new callback pointing to the same directory. resume_callback = keras.callbacks.OrbaxCheckpoint(     directory=checkpoint_dir,     max_to_keep=5, )  # Continue training — epochs 3 and 4 (picking up from epoch 3). resumed_model.fit(     x_train,     y_train,     batch_size=32,     epochs=5,     initial_epoch=3,     verbose=1,     validation_split=0.2,     callbacks=[resume_callback], )`\
\
`Epoch 4/5  7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 64ms/step - loss: 0.1094 - val_loss: 0.1176  Epoch 5/5  1/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 0.1179  WARNING:absl:[process=0][thread=Thread-29 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_basic/3.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 0.0996 - val_loss: 0.1141  WARNING:absl:[process=0][thread=Thread-35 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_basic/4.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   <keras.src.callbacks.history.History at 0x1483120d0>`\
\
Save best only\
--------------\
\
Monitor a metric and keep only the best checkpoint:\
\
Copied!\
\
`best_dir = "/tmp/orbax_ckpt_best" shutil.rmtree(best_dir, ignore_errors=True)  best_callback = keras.callbacks.OrbaxCheckpoint(     directory=best_dir,     monitor="val_loss",     mode="min",     save_best_only=True,     max_to_keep=1, )  model_best = get_model() model_best.fit(     x_train,     y_train,     batch_size=32,     epochs=5,     verbose=1,     validation_split=0.2,     callbacks=[best_callback], )`\
\
`Epoch 1/5  7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 50ms/step - loss: 0.1190 - val_loss: 0.1004  Epoch 2/5  1/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.1280  WARNING:absl:[process=0][thread=Thread-41 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_best/0.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 0.1061 - val_loss: 0.0984  Epoch 3/5  1/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 0.1057  WARNING:absl:[process=0][thread=Thread-47 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_best/1.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 0.0967 - val_loss: 0.0876  Epoch 4/5  1/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 0.1130  WARNING:absl:[process=0][thread=Thread-52 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_best/2.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - loss: 0.0893 - val_loss: 0.0881  Epoch 5/5  7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.0861 - val_loss: 0.0797  WARNING:absl:[process=0][thread=Thread-59 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_best/4.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   <keras.src.callbacks.history.History at 0x14856aad0>`\
\
Batch-level checkpointing\
-------------------------\
\
Save every N batches instead of every epoch by setting `save_freq` to an integer:\
\
Copied!\
\
`batch_dir = "/tmp/orbax_ckpt_batch" shutil.rmtree(batch_dir, ignore_errors=True)  batch_callback = keras.callbacks.OrbaxCheckpoint(     directory=batch_dir,     save_freq=4,  # Save every 4 batches.     max_to_keep=3, )  model_batch = get_model() model_batch.fit(     x_train,     y_train,     batch_size=32,     epochs=2,     verbose=1,     callbacks=[batch_callback], )`\
\
`Epoch 1/2  1/8 ━━━━━━━━━━━━━━━━━━━━ 0s 85ms/step - loss: 0.9480  WARNING:absl:[process=0][thread=Thread-65 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_batch/4.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 0.6971  Epoch 2/2  1/8 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.3194  WARNING:absl:[process=0][thread=Thread-70 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_batch/8.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   WARNING:absl:[process=0][thread=Thread-77 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_batch/12.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 6ms/step - loss: 0.2006  WARNING:absl:[process=0][thread=Thread-82 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_batch/16.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   <keras.src.callbacks.history.History at 0x13b892060>`\
\
Distributed training with model parallelism\
-------------------------------------------\
\
`OrbaxCheckpoint` works seamlessly with the Keras Distribution API. When you set a distribution, model variables are automatically sharded according to your `LayoutMap` and checkpoints capture the distributed state.\
\
> **Note**: The example below uses virtual devices to simulate a multi-device environment. In production, use your actual accelerators (GPUs/TPUs).\
\
Copied!\
\
`devices = jax.devices() print(f"Available devices: {len(devices)}")`\
\
`Available devices: 4`\
\
### Define a layout map and distribution\
\
Copied!\
\
`mesh = keras.distribution.DeviceMesh(     shape=(2, 2),     axis_names=["data", "model"],     devices=devices, )  layout_map = keras.distribution.LayoutMap(mesh) layout_map["dense_1/kernel"] = (None, "model")  distribution = keras.distribution.ModelParallel(     layout_map=layout_map, batch_dim_name="data" ) keras.distribution.set_distribution(distribution)`\
\
### Train with distributed checkpointing\
\
Copied!\
\
`dist_dir = "/tmp/orbax_ckpt_dist" shutil.rmtree(dist_dir, ignore_errors=True) dist_model = get_model()  dist_callback = keras.callbacks.OrbaxCheckpoint(     directory=dist_dir,     max_to_keep=2, )  dist_model.fit(     x_train,     y_train,     batch_size=32,     epochs=3,     verbose=1,     validation_split=0.2,     callbacks=[dist_callback], )`\
\
`Epoch 1/3  7/7 ━━━━━━━━━━━━━━━━━━━━ 1s 83ms/step - loss: 0.3819 - val_loss: 0.1660  Epoch 2/3  WARNING:absl:[process=0][thread=Thread-89 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_dist/0.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 0.1216 - val_loss: 0.1554  Epoch 3/3  WARNING:absl:[process=0][thread=Thread-95 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_dist/1.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 0.1520 - val_loss: 0.1450  WARNING:absl:[process=0][thread=Thread-100 (_target_setting_result)] Skipping merge of OCDBT checkpoints: No per-process OCDBT checkpoint subdirs found in /tmp/orbax_ckpt_dist/2.orbax-checkpoint-tmp/model_config.orbax-checkpoint-tmp,   <keras.src.callbacks.history.History at 0x13b893ce0>`\
\
### Verify sharding\
\
After training, you can inspect the sharding of saved variables:\
\
Copied!\
\
`loaded_dist = keras.saving.load_model(dist_dir) for v in loaded_dist.trainable_variables:     print(f"{v.path}: shape={v.shape}, sharding={v.value.sharding}")`\
\
`WARNING:absl:TensorStore data files not found in checkpoint path /tmp/orbax_ckpt_dist/2. This may be a sign of a malformed checkpoint, unless your checkpoint consists entirely of strings or other non-standard PyTree leaves.  dense_1/kernel: shape=(32, 64), sharding=NamedSharding(mesh=Mesh('data': 2, 'model': 2, axis_types=(Auto, Auto)), spec=PartitionSpec(None, 'model'), memory_kind=device) dense_1/bias: shape=(64,), sharding=NamedSharding(mesh=Mesh('data': 2, 'model': 2, axis_types=(Auto, Auto)), spec=PartitionSpec(None,), memory_kind=device) dense_2/kernel: shape=(64, 1), sharding=NamedSharding(mesh=Mesh('data': 2, 'model': 2, axis_types=(Auto, Auto)), spec=PartitionSpec(None, None), memory_kind=device) dense_2/bias: shape=(1,), sharding=NamedSharding(mesh=Mesh('data': 2, 'model': 2, axis_types=(Auto, Auto)), spec=PartitionSpec(None,), memory_kind=device)`\
\
Cross-layout resharding\
-----------------------\
\
One of the most powerful features of Orbax checkpointing in Keras is the ability to load a checkpoint saved with one sharding layout and restore it under a **different** layout. Keras automatically provides the target shardings to Orbax so arrays are resharded on load.\
\
For example, a checkpoint saved with `dense_1/kernel` sharded on the `"model"` axis can be loaded with that same kernel sharded on the `"data"` axis instead:\
\
Copied!\
\
`# Clear the current distribution first. keras.distribution.set_distribution(None)  # Define a new layout that shards dense_1/kernel on a different axis. new_layout_map = keras.distribution.LayoutMap(mesh) new_layout_map["dense_1/kernel"] = ("data", None)  new_distribution = keras.distribution.ModelParallel(     layout_map=new_layout_map, batch_dim_name="data" ) keras.distribution.set_distribution(new_distribution)  # Load the checkpoint saved with the original layout. resharded_model = keras.saving.load_model(dist_dir)  print("\nResharded variable shardings:") for v in resharded_model.trainable_variables:     print(f"  {v.path}: sharding={v.value.sharding}")`\
\
`WARNING:absl:TensorStore data files not found in checkpoint path /tmp/orbax_ckpt_dist/2. This may be a sign of a malformed checkpoint, unless your checkpoint consists entirely of strings or other non-standard PyTree leaves.  Resharded variable shardings:   dense_1/kernel: sharding=NamedSharding(mesh=Mesh('data': 2, 'model': 2, axis_types=(Auto, Auto)), spec=PartitionSpec('data', None), memory_kind=device)   dense_1/bias: sharding=NamedSharding(mesh=Mesh('data': 2, 'model': 2, axis_types=(Auto, Auto)), spec=PartitionSpec(None,), memory_kind=device)   dense_2/kernel: sharding=NamedSharding(mesh=Mesh('data': 2, 'model': 2, axis_types=(Auto, Auto)), spec=PartitionSpec(None, None), memory_kind=device)   dense_2/bias: sharding=NamedSharding(mesh=Mesh('data': 2, 'model': 2, axis_types=(Auto, Auto)), spec=PartitionSpec(None,), memory_kind=device)`\
\
The `dense_1/kernel` variable was originally sharded as `(None, "model")` but is now sharded as `("data", None)`. Orbax handles the data movement automatically during loading.\
\
Callback parameters reference\
-----------------------------\
\
| Parameter | Default | Description |\
| --- | --- | --- |\
| `directory` | _(required)_ | Path to checkpoint directory. |\
| `monitor` | `"val_loss"` | Metric to monitor for `save_best_only`. |\
| `mode` | `"auto"` | `"min"`, `"max"`, or `"auto"`. |\
| `save_best_only` | `False` | Only save when monitored metric improves. |\
| `save_freq` | `"epoch"` | `"epoch"` or an integer (every N batches). |\
| `max_to_keep` | `1` | Max recent checkpoints to retain. |\
| `save_on_background` | `True` | Save asynchronously to avoid blocking. |\
| `save_weights_only` | `False` | Save only weights (no model config/assets). |\
| `initial_value_threshold` | `None` | Initial "best" value for the monitor. |\
| `verbose` | `0` | Verbosity (0 = silent, 1 = messages). |\
\
Summary\
-------\
\
*   **[`keras.callbacks.OrbaxCheckpoint`](https://keras.io/api/callbacks/orbax_checkpoint#orbaxcheckpoint-class)\
    ** is the built-in callback for Orbax checkpointing — no wrapper classes needed.\
*   Use **`keras.saving.load_model()`** or **`model.load_weights()`** to restore from an Orbax checkpoint directory.\
*   Works with **distributed training** (Keras Distribution API) and supports **cross-layout resharding** when loading under a different `LayoutMap`.\
*   Supports **multi-host** JAX environments with automatic coordination.\
*   Mirrors the `ModelCheckpoint` API: `save_best_only`, `monitor`, `mode`, `save_freq`, `max_to_keep`.\
\
Copied!\
\
`# Clean up the distribution for any subsequent cells. keras.distribution.set_distribution(None)`\
\
[Orbax Checkpointing in Keras](https://keras.io/guides/orbax_checkpoint/#orbax-checkpointing-in-keras)\
\
[Introduction](https://keras.io/guides/orbax_checkpoint/#introduction)\
\
[Setup](https://keras.io/guides/orbax_checkpoint/#setup)\
\
[Basic Usage](https://keras.io/guides/orbax_checkpoint/#basic-usage)\
\
[Define a model and dataset](https://keras.io/guides/orbax_checkpoint/#define-a-model-and-dataset)\
\
[Save a checkpoint every epoch](https://keras.io/guides/orbax_checkpoint/#save-a-checkpoint-every-epoch)\
\
[Loading a model from an Orbax checkpoint](https://keras.io/guides/orbax_checkpoint/#loading-a-model-from-an-orbax-checkpoint)\
\
[Loading weights only](https://keras.io/guides/orbax_checkpoint/#loading-weights-only)\
\
[Resuming training](https://keras.io/guides/orbax_checkpoint/#resuming-training)\
\
[Save best only](https://keras.io/guides/orbax_checkpoint/#save-best-only)\
\
[Batch-level checkpointing](https://keras.io/guides/orbax_checkpoint/#batchlevel-checkpointing)\
\
[Distributed training with model parallelism](https://keras.io/guides/orbax_checkpoint/#distributed-training-with-model-parallelism)\
\
[Define a layout map and distribution](https://keras.io/guides/orbax_checkpoint/#define-a-layout-map-and-distribution)\
\
[Train with distributed checkpointing](https://keras.io/guides/orbax_checkpoint/#train-with-distributed-checkpointing)\
\
[Verify sharding](https://keras.io/guides/orbax_checkpoint/#verify-sharding)\
\
[Cross-layout resharding](https://keras.io/guides/orbax_checkpoint/#crosslayout-resharding)\
\
[Callback parameters reference](https://keras.io/guides/orbax_checkpoint/#callback-parameters-reference)\
\
[Summary](https://keras.io/guides/orbax_checkpoint/#summary)