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
 / Define a Custom TPU/GPU Kernel

Define a Custom TPU/GPU Kernel
==============================

**Author:** [jeffcarp](https://www.jeffcarp.com/)
  
**Date created:** 2025/12/18  
**Last modified:** 2025/12/18  
**Description:** Write high-performance custom Keras layers for TPUs and GPUs.

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/guides/ipynb/define_custom_kernel.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/guides/define_custom_kernel.py)

How to Write a Custom TPU or GPU Kernel in Keras
================================================

Keras has [many pre-made layers to choose from](https://keras.io/api/layers/)
, and the ability to easily [create your own](https://keras.io/guides/making_new_layers_and_models_via_subclassing/)
 if you can't find the exact one you need. However, if you have a need for speed, or otherwise need to customize the exact behavior of your model at the hardware level, you may want to look into writing a custom kernel. A good way to know if you need a custom kernel is to look at the profile of your model and see if there are any idle gaps caused by computation or memory transfer bottlenecks (see the [TensorBoard callback](https://keras.io/api/callbacks/tensorboard/)
 for how to get a profile).

This guide will explore how to write a custom kernel and add it to your Keras model. We will utilize **Pallas**, a library that lets you write kernels in Python that can run on both TPU or GPU, where they're lowered to Mosaic or Triton, respectively. You can learn more in the [Pallas docs](https://docs.jax.dev/en/latest/pallas/index.html)
.

**Compatibility note:** Pallas is only available when using the JAX backend on certain hardware:

*   TPU v4 and above
*   NVIDIA Ampere GPUs (compute capability 8.0) and above

If you're running in Colab, the v5e-1 in the free tier supports running this guide.

First, make sure you're running the latest version of `libtpu`:

Copied!

`!pip install --upgrade -q "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html`

Copied!

`from functools import partial import os import time  os.environ["KERAS_BACKEND"] = "jax"  import jax from jax.experimental import pallas as pl import jax.numpy as jnp import keras`

`[[34;49mnotice[1;39;49m][39;49m To update, run: [32;49mpip install --upgrade pip  /home/jeffcarp/venv/lib/python3.10/site-packages/jax/_src/cloud_tpu_init.py:84: UserWarning: Transparent hugepages are not enabled. TPU runtime startup and shutdown time should be significantly improved on TPU v5e and newer. If not already set, you may need to enable transparent hugepages in your VM image (sudo sh -c "echo always > /sys/kernel/mm/transparent_hugepage/enabled")   warnings.warn(`\
\
Simple Example\
==============\
\
Let's start with the example from the [Pallas quickstart](https://docs.jax.dev/en/latest/pallas/quickstart.html)\
: a simple kernel to add two vectors together.\
\
Copied!\
\
`def add_vectors_kernel(x_ref, y_ref, o_ref):     """Pallas kernel for adding two vectors together."""     x, y = x_ref[...], y_ref[...]     o_ref[...] = x + y`\
\
Now jit-compile the Pallas function into a function that can be used by JAX.\
\
Copied!\
\
`@jax.jit def add_vectors(x: jax.Array, y: jax.Array) -> jax.Array:     return pl.pallas_call(         add_vectors_kernel, out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype)     )(x, y)  add_vectors(jnp.arange(8), jnp.arange(8))`\
\
`Array([ 0,  2,  4,  6,  8, 10, 12, 14], dtype=int32)`\
\
Now we can embed the jitted `add_vectors` function containing the Pallas kernel into a Keras layer, just by calling it there.\
\
Copied!\
\
`class PallasAddLayer(keras.Layer):     def call(self, x, y):         # Reuse the JIT-compiled Pallas function         return add_vectors(x, y)  layer = PallasAddLayer()  x_data = jnp.arange(8, dtype=jnp.int32) y_data = jnp.arange(8, dtype=jnp.int32)  layer(x_data, y_data)`\
\
`Array([ 0,  2,  4,  6,  8, 10, 12, 14], dtype=int32)`\
\
That's how to integrate a Pallas kernel into a Keras layer! Now for a more in-depth example.\
\
Writing a Fused Linear Activation Layer\
=======================================\
\
Some common reasons you might want to write a custom kernel is to take advantage of **fusion** and **tiling**.\
\
**Operator fusion** is the process of combining two or more ops into one "fused" op, for example instead of calling [`keras.ops.matmul`](https://keras.io/api/ops/numpy#matmul-function)\
 then [`keras.ops.relu`](https://keras.io/api/ops/nn#relu-function)\
 sequentially, we could write a custom op that combines both into one more efficient operator. XLA already [does operator fusion when possible](https://arxiv.org/abs/2301.13062)\
 for certain use cases, but to squeeze even more performance out of the TPU or GPU, we need to write a custom op to specify the fusion exactly.\
\
**Tiling** is the ability to control how blocks of memory are loaded from the TPU or GPU's larger High Bandwidth Memory (HBM) to the smaller, extremely fast on-chip memory (called VMEM on TPU or SMEM on GPU) that the accelerator's computation units (e.g., TPU's Matrix Units or a GPU's Tensor Cores) use directly. This is critical for improving the performance of large matrix multiplications, for example those in the MLP layer at the end of Transformer blocks.\
\
In Pallas, tiling is controlled by the `BlockSpec`. Learn more in the [Pallas BlockSpec guide here](https://docs.jax.dev/en/latest/pallas/grid_blockspec.html#blockspec-a-k-a-how-to-chunk-up-inputs)\
.\
\
In this section, we'll take two operations that commonly appear together: a matrix multiplication (like in a `Dense` layer) and a ReLU activation. We will write a new op that fuses them together for better performance.\
\
* * *\
\
Original Unoptimized Implementation\
-----------------------------------\
\
Copied!\
\
`class StandardDenseReLU(keras.layers.Layer):     """Standard Matmul and ReLU implementation using keras.ops."""      def __init__(self, units, **kwargs):         super().__init__(**kwargs)         self.units = units      def build(self, input_shape):         self.w = self.add_weight(             shape=(input_shape[-1], self.units),             initializer="glorot_uniform",             trainable=True,         )      def call(self, inputs):         # The standard implementation performs two separate operations.         # Each one involves expensive data transfer with the main device memory (HBM).         # 1. Matmul: inputs (HBM) -> compute -> intermediate (HBM)         y = keras.ops.matmul(inputs, self.w)         # 2. ReLU: intermediate (HBM) -> compute -> output (HBM)         return keras.ops.relu(y)`\
\
* * *\
\
1\. Define the Fused Kernel\
---------------------------\
\
First we create an inner kernel function that defines the fused computation that combines both matmul (`pl.dot`) and activation (`jnp.maximum`).\
\
Copied!\
\
`import jax.numpy as jnp from jax.experimental import pallas as pl  def matmul_relu_kernel(a_ref, b_ref, c_ref):     """Pallas kernel for fused matmul + ReLU."""     # Perform the matrix multiplication on the local tile     # pl.dot leverages the hardware's Matrix Unit (MXU)     acc = pl.dot(a_ref[...], b_ref[...])      # Fusion happens here: apply activation while data is in VMEM     result = jnp.maximum(acc, 0)      # Write the final result to the output reference     c_ref[...] = result`\
\
* * *\
\
2\. Specify the Tiling (BlockSpec)\
----------------------------------\
\
Since the input matrices are usually too large to fit into VMEM, Pallas needs ot know how to "slice" them for loading from HBM to VMEM.\
\
We define this using `BlockSpec` - this tells the hardware: "Take a 128-row chunk of Matrix A and a 128-column chunk of Matrix B to produce a 128x128 tile of Matrix C."\
\
Copied!\
\
`@jax.jit def fused_matmul(a, b):     m, k = a.shape     _, n = b.shape      # Define tile sizes     tile_m, tile_n = 128, 128     assert (         m % tile_m == 0 and n % tile_n == 0     ), "Inputs must be multiples of 128 for this demo"      return pl.pallas_call(         matmul_relu_kernel,         # Map output indices to input blocks         out_shape=jax.ShapeDtypeStruct((m, n), a.dtype),         in_specs=[             # For each output tile, we take a slice of A of shape (tile_m, k)             pl.BlockSpec(                 index_map=lambda i, j: (i, 0), block_shape=(tile_m, k)             ),  # Matrix A             # For each output tile, we take a slice of B of shape (k, tile_n)             pl.BlockSpec(                 index_map=lambda i, j: (0, j), block_shape=(k, tile_n)             ),  # Matrix B         ],         out_specs=pl.BlockSpec(             index_map=lambda i, j: (i, j), block_shape=(tile_m, tile_n)         ),  # Matrix C         grid=(m // tile_m, n // tile_n),     )(a, b)  fused_matmul(jnp.ones((256, 256)), jnp.ones((256, 256)))`\
\
`Array([[256., 256., 256., ..., 256., 256., 256.],        [256., 256., 256., ..., 256., 256., 256.],        [256., 256., 256., ..., 256., 256., 256.],        ...,        [256., 256., 256., ..., 256., 256., 256.],        [256., 256., 256., ..., 256., 256., 256.],        [256., 256., 256., ..., 256., 256., 256.]], dtype=float32)`\
\
* * *\
\
3\. Integrating into a Keras Layer\
----------------------------------\
\
Now for the final step, call the jit-compiled `fused_matmul` kernel from a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)\
.\
\
Copied!\
\
`class FusedDense(keras.layers.Layer):     """Custom Keras layer that applies the fused Dense and ReLU op."""      def __init__(self, units, **kwargs):         super().__init__(**kwargs)         self.units = units      def build(self, input_shape):         self.w = self.add_weight(             shape=(input_shape[-1], self.units), initializer="glorot_uniform"         )      def call(self, inputs):         # Dispatch to our Pallas kernel         return fused_matmul(inputs, self.w.value)  FusedDense(256)(jnp.ones((256, 256)))`\
\
`Array([[0.        , 0.511034  , 0.19506836, ..., 0.29304314, 0.        ,         0.04899597],        [0.        , 0.511034  , 0.19506836, ..., 0.29304314, 0.        ,         0.04899597],        [0.        , 0.511034  , 0.19506836, ..., 0.29304314, 0.        ,         0.04899597],        ...,        [0.        , 0.511034  , 0.19506836, ..., 0.29304314, 0.        ,         0.04899597],        [0.        , 0.511034  , 0.19506836, ..., 0.29304314, 0.        ,         0.04899597],        [0.        , 0.511034  , 0.19506836, ..., 0.29304314, 0.        ,         0.04899597]], dtype=float32)`\
\
* * *\
\
4\. Benchmarking the Speedup\
----------------------------\
\
Copied!\
\
`# 1. Setup Data N = 8192  # Large enough to be memory bound input_data = jnp.ones((N, N), dtype="float32")  # Initialize layers standard_layer = StandardDenseReLU(units=N) pallas_layer = FusedDense(units=N)  # Build layers by calling them once standard_layer(input_data) pallas_layer(input_data)  def benchmark(layer, x, name, iterations=100):     # Warm up to ensure JIT compilation is finished     for _ in range(10):         layer(x).block_until_ready()      start_time = time.perf_counter()     for _ in range(iterations):         layer(x).block_until_ready()     end_time = time.perf_counter()      avg_time = (end_time - start_time) / iterations * 1000  # convert to ms     print(f"{name} Average Latency: {avg_time:.3f} ms")  # 2. Run Comparison print(f"Benchmarking Matrix Size: {N}x{N}\n" + "-" * 30) benchmark(standard_layer, input_data, "Standard Keras (Matmul + ReLU)") benchmark(pallas_layer, input_data, "Pallas Fused (Matmul + ReLU)")`\
\
`Benchmarking Matrix Size: 8192x8192 ------------------------------  Standard Keras (Matmul + ReLU) Average Latency: 7.811 ms  Pallas Fused (Matmul + ReLU) Average Latency: 35.039 ms`\
\
### Why this Works\
\
**Memory Bandwidth Efficiency:** By fusing the matrix multiplication and activation, we perform the ReLU computation while data is still in the chip's fast VMEM. This drastically reduces expensive read/write roundtrips to HBM.\
\
**Automatic Parallelization:** Pallas handles the "grid" execution, meaning it automatically parallelizes your defined tiles across the available hardware cores (whether TPU MXUs or GPU Tensor Cores).\
\
**Drop-in Inference Speed:** This `FusedDense` kernel can be integrated into any Keras model, giving an example of improving serving/inference performance with minimal code changes.\
\
* * *\
\
5\. Enabling Training\
---------------------\
\
In order for a Pallas kernel to be trainable, you must also supply a second kernel to define the custom backward pass, since JAX can't [AutoGrad](https://docs.jax.dev/en/latest/automatic-differentiation.html)\
 through Pallas kernels. Without it, you might see an error like this:\
\
Copied!\
\
`model = keras.Sequential([FusedDense(256)]) model.compile(optimizer="adam", loss="mse") model.fit(jnp.ones((256, 256)), jnp.ones((256, 256))) >>> Linearization failed to produce known values for all output primals. This is typically caused by attempting to differentiate a function uses an operation that does not support reverse-mode autodiff.`\
\
To extend our fused matmul example above:\
\
Copied!\
\
``# 1. Define the wrapper with `custom_vjp` using our original `fused_matmul`. @jax.custom_vjp def fused_matmul_trainable(x, w):     return fused_matmul(x, w)  # 2. Define the Forward Pass # It must return the output AND "residuals" (data needed for the backward pass) def fused_matmul_fwd(x, w):     y = fused_matmul_trainable(x, w)     # We save inputs x, w and output y for the backward calculation     return y, (x, w, y)  # 3. Define the Backward Pass # JAX gives us the residuals and the incoming gradient (g) def fused_matmul_bwd(residuals, g):     x, w, y = residuals      # Calculate the gradient of ReLU: 1 if y > 0, else 0     # g is the gradient flowing back from the next layer     grad_relu = g * (y > 0)      # Standard backprop math for matmul:     # grad_x = grad_relu @ w.T     grad_x = jnp.dot(grad_relu, w.T)      # grad_w = x.T @ grad_relu     grad_w = jnp.dot(x.T, grad_relu)      return grad_x, grad_w  # 4. Register the forward and backward functions fused_matmul_trainable.defvjp(fused_matmul_fwd, fused_matmul_bwd)  class FusedDenseTrainable(FusedDense):     """Updated layer that contains Pallas forward and backward pass."""      def call(self, inputs):         # Dispatch to our trainable Pallas kernel         return fused_matmul_trainable(inputs, self.w.value)  # Demonstrate trainability on dummy data model = keras.Sequential([FusedDenseTrainable(256)]) model.compile(optimizer="adam", loss="mse") model.fit(jnp.ones((256, 256)), jnp.ones((256, 256)), batch_size=128)``\
\
`2/2 ━━━━━━━━━━━━━━━━━━━━ 0s 65ms/step - loss: 0.6481  <keras.src.callbacks.history.History at 0x7f58a97bcac0>`\
\
Followups\
=========\
\
In this guide we covered how to define a simple custom Pallas kernel performing vector addition to include in a Keras model. Then we followed up with a more in-depth example of a fused matmul + activation kernel that you might use in a real-world model to improve performance.\
\
Please refer to the [Pallas docs](https://docs.jax.dev/en/latest/pallas/index.html#)\
 for further documentation on writing custom kernels. Additionally to explore more examples of Pallas kernels, including FlashAttention and MoE layers, check out the [Tokamax](https://github.com/openxla/tokamax)\
 library.\
\
[Define a Custom TPU/GPU Kernel](https://keras.io/guides/define_custom_kernel/#define-a-custom-tpugpu-kernel)\
\
[How to Write a Custom TPU or GPU Kernel in Keras](https://keras.io/guides/define_custom_kernel/#how-to-write-a-custom-tpu-or-gpu-kernel-in-keras)\
\
[Simple Example](https://keras.io/guides/define_custom_kernel/#simple-example)\
\
[Writing a Fused Linear Activation Layer](https://keras.io/guides/define_custom_kernel/#writing-a-fused-linear-activation-layer)\
\
[Original Unoptimized Implementation](https://keras.io/guides/define_custom_kernel/#original-unoptimized-implementation)\
\
[1\. Define the Fused Kernel](https://keras.io/guides/define_custom_kernel/#1-define-the-fused-kernel)\
\
[2\. Specify the Tiling (BlockSpec)](https://keras.io/guides/define_custom_kernel/#2-specify-the-tiling-blockspec)\
\
[3\. Integrating into a Keras Layer](https://keras.io/guides/define_custom_kernel/#3-integrating-into-a-keras-layer)\
\
[4\. Benchmarking the Speedup](https://keras.io/guides/define_custom_kernel/#4-benchmarking-the-speedup)\
\
[Why this Works](https://keras.io/guides/define_custom_kernel/#why-this-works)\
\
[5\. Enabling Training](https://keras.io/guides/define_custom_kernel/#5-enabling-training)\
\
[Followups](https://keras.io/guides/define_custom_kernel/#followups)