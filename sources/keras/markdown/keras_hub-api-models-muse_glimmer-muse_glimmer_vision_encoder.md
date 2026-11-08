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
 / [MuseGlimmer](https://keras.io/keras_hub/api/models/muse_glimmer/)
 / MuseGlimmerVisionEncoder model

MuseGlimmerVisionEncoder model
==============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_vision_encoder.py#L678)

### `MuseGlimmerVisionEncoder` class

Copied!

`keras_hub.models.MuseGlimmerVisionEncoder(     num_layers,     hidden_size,     num_heads,     intermediate_size,     patch_size=14,     patch_temporal=2,     merge_size=2,     pos_emb_height=32,     pos_emb_width=32,     rope_theta=10000.0,     layer_norm_eps=1e-05,     layer_types=None,     out_hidden_size=None,     max_num_windows=None,     max_num_frames=None,     max_frame_size=None,     dtype=None,     **kwargs )`

MuseGlimmer's ViT-style perception encoder.

The encoder takes pre-extracted, pre-flattened image patches. It applies patch embedding and bilinear position embeddings. It alternates window and full attention. Window attention uses an index permutation, not a windowed attention mask. The encoder also applies axial 2D RoPE and pixel-shuffle patch merging.

Attention runs per window and per frame. With eager inputs, the encoder batches the windows and frames of the same length with no padding. This matches the HF eager attention exactly. A set cap (`max_num_windows`, `max_num_frames`, `max_frame_size`) must fit the input, or the encoder raises a `ValueError`.

Traced inputs (for example under `jax.jit`) have no concrete grid values. For these inputs, the caps set the sizes of padded slot buffers. If a cap is `None`, the encoder uses one masked attention over the full sequence. This attention needs memory quadratic in the patch count. Set the caps to get static shapes under tracing. Each call then reserves memory for the full caps. Traced inputs skip the fit check. A cap that is too small gives incorrect output.

**Arguments**

*   **num\_layers**: int. Number of transformer blocks.
*   **hidden\_size**: int. ViT hidden dimension.
*   **num\_heads**: int. Number of attention heads.
*   **intermediate\_size**: int. MLP intermediate dimension.
*   **patch\_size**: int. Spatial patch size in pixels.
*   **patch\_temporal**: int. Temporal patch size in frames.
*   **merge\_size**: int. Spatial merge (pixel-shuffle) factor.
*   **pos\_emb\_height**: int. Learned position-embedding grid height.
*   **pos\_emb\_width**: int. Learned position-embedding grid width.
*   **rope\_theta**: float. Axial RoPE base wavelength. Defaults to `10000.0`.
*   **layer\_norm\_eps**: float. Epsilon for `ln_pre` and `ln_post`. The block norms always use `1e-5`, like Hugging Face. Defaults to `1e-5`.
*   **layer\_types**: list of str or `None`. Per-layer `"window_attention"` or `"full_attention"`. Defaults to every 4th layer (and the last) being full attention.
*   **out\_hidden\_size**: int or `None`. Output dim after pixel-shuffle merge; defaults to `hidden_size * merge_size ** 2`.
*   **max\_num\_windows**: int or `None`. Optional opt-in cap for traced inputs. When set, window-attention layers put each window into a fixed `(max_num_windows, window_patches ** 2)` buffer. The value must be at least the total number of windows in one call. Defaults to `None`.
*   **max\_num\_frames**: int or `None`. Optional opt-in cap for traced inputs. Full-attention layers put each frame into a fixed `(max_num_frames, max_frame_size)` buffer. The value must be at least the total number of frames in one call. Set `max_frame_size` together with this argument. Defaults to `None`.
*   **max\_frame\_size**: int or `None`. The slot size for `max_num_frames`. The value must be at least the largest per-frame patch count (`height * width`) in one call. Defaults to `None`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Defaults to `None`.

* * *

[MuseGlimmerVisionEncoder model](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_vision_encoder/#museglimmervisionencoder-model)

[`MuseGlimmerVisionEncoder` class](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_vision_encoder/#museglimmervisionencoder-class)