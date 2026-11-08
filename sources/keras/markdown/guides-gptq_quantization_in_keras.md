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
 / GPTQ Quantization in Keras

GPTQ Quantization in Keras
==========================

**Author:** [Jyotinder Singh](https://x.com/Jyotinder_Singh)
  
**Date created:** 2025/10/16  
**Last modified:** 2025/10/16  
**Description:** How to run weight-only GPTQ quantization for Keras & KerasHub models.

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/guides/ipynb/gptq_quantization_in_keras.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/guides/gptq_quantization_in_keras.py)

* * *

What is GPTQ?
-------------

GPTQ ("Generative Pre-Training Quantization") is a post-training, weight-only quantization method that uses a second-order approximation of the loss (via a Hessian estimate) to minimize the error introduced when compressing weights to lower precision, typically 4-bit integers.

Unlike standard post-training techniques, GPTQ keeps activations in higher-precision and only quantizes the weights. This often preserves model quality in low bit-width settings while still providing large storage and memory savings.

Keras supports GPTQ quantization for KerasHub models via the [`keras.quantizers.GPTQConfig`](https://keras.io/api/quantizers/quantizer_classes#gptqconfig-class)
 class.

* * *

Load a KerasHub model
---------------------

This guide uses the `Gemma3CausalLM` model from KerasHub, a small (1B parameter) causal language model.

Copied!

`from datasets import load_dataset import keras from keras_hub.models import Gemma3CausalLM  prompt = "Keras is a"  model = Gemma3CausalLM.from_preset("gemma3_1b")  outputs = model.generate(prompt, max_length=30) print(outputs)`

`Keras is a deep learning library for Python. It is a high-level API for neural networks. It is a Python library for deep learning`

* * *

Configure & run GPTQ quantization
---------------------------------

You can configure GPTQ quantization via the [`keras.quantizers.GPTQConfig`](https://keras.io/api/quantizers/quantizer_classes#gptqconfig-class)
 class.

The GPTQ configuration requires a calibration dataset and tokenizer, which it uses to estimate the Hessian and quantization error. Here, we use a small slice of the WikiText-2 dataset for calibration.

You can tune several parameters to trade off speed, memory, and accuracy. The most important of these are `weight_bits` (the bit-width to quantize weights to) and `group_size` (the number of weights to quantize together). The group size controls the granularity of quantization: smaller groups typically yield better accuracy but are slower to quantize and may use more memory. A good starting point is `group_size=128` for 4-bit quantization (`weight_bits=4`).

In this example, we first prepare a tiny calibration set, and then run GPTQ on the model using the `.quantize(...)` API.

Copied!

`# Calibration slice (use a larger/representative set in practice) texts = load_dataset("wikitext", "wikitext-2-raw-v1", split="train[:1%]")["text"]  calibration_dataset = [     s + "." for text in texts for s in map(str.strip, text.split(".")) if s ]  gptq_config = keras.quantizers.GPTQConfig(     dataset=calibration_dataset,     tokenizer=model.preprocessor.tokenizer,     weight_bits=4,     group_size=128,     num_samples=256,     sequence_length=256,     hessian_damping=0.01,     symmetric=False,     activation_order=False, )  model.quantize("gptq", config=gptq_config)  outputs = model.generate(prompt, max_length=30) print(outputs)`

`Keras is a Python library for deep learning. It is a high-level interface to the TensorFlow library.  Keras is a great library`

* * *

Model Export
------------

The GPTQ quantized model can be saved to a preset and reloaded elsewhere, just like any other KerasHub model.

Copied!

`model.save_to_preset("gemma3_gptq_w4gs128_preset") model_from_preset = Gemma3CausalLM.from_preset("gemma3_gptq_w4gs128_preset") output = model_from_preset.generate(prompt, max_length=30) print(output)`

`Keras is a Python library for deep learning. It is a high-level interface to the TensorFlow library.  Keras is a great library`

* * *

Performance & Benchmarking
--------------------------

Micro-benchmarks collected on a single NVIDIA 4070 Ti Super (16 GB). Baselines are FP32.

Dataset: WikiText-2.

| Model (preset) | Perplexity Increase % (↓ better) | Disk Storage Reduction Δ % (↓ better) | VRAM Reduction Δ % (↓ better) | First-token Latency Δ % (↓ better) | Throughput Δ % (↑ better) |
| --- | --- | --- | --- | --- | --- |
| GPT2 (gpt2\_base\_en\_cnn\_dailymail) | 1.0% | \-50.1% ↓ | \-41.1% ↓ | +0.7% ↑ | +20.1% ↑ |
| OPT (opt\_125m\_en) | 10.0% | \-49.8% ↓ | \-47.0% ↓ | +6.7% ↑ | \-15.7% ↓ |
| Bloom (bloom\_1.1b\_multi) | 7.0% | \-47.0% ↓ | \-54.0% ↓ | +1.8% ↑ | \-15.7% ↓ |
| Gemma3 (gemma3\_1b) | 3.0% | \-51.5% ↓ | \-51.8% ↓ | +39.5% ↑ | +5.7% ↑ |

Detailed benchmarking numbers and scripts are available [here](https://github.com/keras-team/keras/pull/21641)
.

### Analysis

There is notable reduction in disk space and VRAM usage across all models, with disk space savings around 50% and VRAM savings ranging from 41% to 54%. The reported disk savings understate the true weight compression because presets also include non-weight assets.

Perplexity increases only marginally, indicating model quality is largely preserved after quantization.

* * *

GPTQ vs AWQ?
------------

Both GPTQ and AWQ are weight-only quantization methods that require calibration data. Here's how to choose between them:

| Aspect | GPTQ | AWQ |
| --- | --- | --- |
| **Algorithm** | Hessian-based second-order optimization | Grid search for activation-aware scales |
| **Quantization speed** | Slower (requires Hessian estimation) | Faster (no Hessian computation) |
| **Bit-widths supported** | 2/3/4/8-bit | 4-bit |
| **Accuracy** | Often slightly better on decoder LLMs | Competitive, especially on encoder models |
| **Memory during quantization** | Higher (Hessian storage) | Lower |
| **Calibration sensitivity** | May overfit calibration set, affecting out-of-distribution performance | Less prone to overfitting |

**Choose GPTQ when:**

*   You need bit-widths other than 4 (e.g., 2-bit or 8-bit).
*   Maximum accuracy is critical and you can afford longer quantization time.
*   You're working with decoder-only LLMs where GPTQ may have a slight edge.

**Choose AWQ when:**

*   You need faster quantization (AWQ is typically 2-3x faster than GPTQ).
*   Memory during quantization is constrained.
*   4-bit is sufficient for your use case.
*   Your model will be used on diverse/out-of-distribution data (AWQ is less prone to overfitting on calibration data).

* * *

Practical tips
--------------

*   GPTQ is a post-training technique; training after quantization is not supported.
*   Always use the model's own tokenizer for calibration.
*   Use a representative calibration set; small slices are only for demos.
*   Start with W4 group\_size=128; tune per model/task.

[GPTQ Quantization in Keras](https://keras.io/guides/gptq_quantization_in_keras/#gptq-quantization-in-keras)

[What is GPTQ?](https://keras.io/guides/gptq_quantization_in_keras/#what-is-gptq)

[Load a KerasHub model](https://keras.io/guides/gptq_quantization_in_keras/#load-a-kerashub-model)

[Configure & run GPTQ quantization](https://keras.io/guides/gptq_quantization_in_keras/#configure-amp-run-gptq-quantization)

[Model Export](https://keras.io/guides/gptq_quantization_in_keras/#model-export)

[Performance & Benchmarking](https://keras.io/guides/gptq_quantization_in_keras/#performance-amp-benchmarking)

[Analysis](https://keras.io/guides/gptq_quantization_in_keras/#analysis)

[GPTQ vs AWQ?](https://keras.io/guides/gptq_quantization_in_keras/#gptq-vs-awq)

[Practical tips](https://keras.io/guides/gptq_quantization_in_keras/#practical-tips)