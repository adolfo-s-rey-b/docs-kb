[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.nlp.layers Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/__init__.py)

Layers are the fundamental building blocks for NLP models.

They can be used to assemble new [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
 layers or models.

Modules
-------

[`util`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/util)
 module: Keras-based transformer block layer.

Classes
-------

[`class BertPackInputs`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs)
: Packs tokens into model inputs for BERT.

[`class BertTokenizer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer)
: Wraps TF.Text's BertTokenizer with pre-defined vocab as a Keras Layer.

[`class BigBirdAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BigBirdAttention)
: BigBird, a sparse attention mechanism.

[`class BigBirdMasks`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BigBirdMasks)
: Creates bigbird attention masks.

[`class BlockDiagFeedforward`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockDiagFeedforward)
: Block diagonal feedforward layer.

[`class BlockSparseAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention)
: Multi-head block sparse attention layer.

[`class CachedAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/CachedAttention)
: Attention layer with cache used for autoregressive decoding.

[`class ClassificationHead`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead)
: Pooling head for sentence-level classification tasks.

[`class ExpertsChooseMaskedRouter`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter)
: Masked matmul router using experts choose tokens assignment.

[`class FactorizedEmbedding`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FactorizedEmbedding)
: A factorized embeddings layer for supporting larger embeddings.

[`class FastWordpieceBertTokenizer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer)
: A bert tokenizer keras layer using text.FastWordpieceTokenizer.

[`class FeedForwardExperts`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts)
: Feed-forward layer with multiple experts.

[`class FourierTransformLayer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FourierTransformLayer)
: Fourier Transform layer.

[`class GatedFeedforward`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GatedFeedforward)
: Gated linear feedforward layer.

[`class GaussianProcessClassificationHead`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead)
: Gaussian process-based pooling head for sentence classification.

[`class HartleyTransformLayer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/HartleyTransformLayer)
: Hartley Transform layer.

[`class KernelAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention)
: A variant of efficient transformers which replaces softmax with kernels.

[`class KernelMask`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelMask)
: Creates kernel attention mask.

[`class LinearTransformLayer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer)
: Dense, linear transformation layer.

[`class MaskedLM`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MaskedLM)
: Masked language model network head for BERT modeling.

[`class MaskedSoftmax`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MaskedSoftmax)
: Performs a softmax with optional masking on a tensor.

[`class MatMulWithMargin`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MatMulWithMargin)
: This layer computs a dot product matrix given two encoded inputs.

[`class MixingMechanism`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MixingMechanism)
: Determines the type of mixing layer.

[`class MobileBertEmbedding`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding)
: Performs an embedding lookup for MobileBERT.

[`class MobileBertMaskedLM`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM)
: Masked language model network head for BERT modeling.

[`class MobileBertTransformer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer)
: Transformer block for MobileBERT.

[`class MoeLayer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer)
: Sparse MoE layer with per-token routing.

[`class MoeLayerWithBackbone`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone)
: Sparse MoE layer plus a FeedForward layer evaluated for all tokens.

[`class MultiChannelAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MultiChannelAttention)
: Multi-channel Attention layer.

[`class MultiClsHeads`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MultiClsHeads)
: Pooling heads sharing the same pooling stem.

[`class MultiHeadRelativeAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MultiHeadRelativeAttention)
: A multi-head attention layer with relative attention + position encoding.

[`class MultiQueryAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MultiQueryAttention)
: Multi-query attention layer.

[`class OnDeviceEmbedding`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/OnDeviceEmbedding)
: Performs an embedding lookup suitable for accelerator devices.

[`class PackBertEmbeddings`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PackBertEmbeddings)
: Performs packing tricks for BERT inputs to improve TPU utilization.

[`class PerDimScaleAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerDimScaleAttention)
: Learn scales for individual dims.

[`class PerQueryDenseHead`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead)
: Pooling head used for EncT5 style models.

[`class PositionEmbedding`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PositionEmbedding)
: Creates a positional embedding.

[`class RandomFeatureGaussianProcess`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RandomFeatureGaussianProcess)
: Gaussian process layer with random feature approximation \[1\].

[`class ReZeroTransformer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReZeroTransformer)
: Transformer layer with ReZero.

[`class RelativePositionBias`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionBias)
: Relative position embedding via per-head bias in T5 style.

[`class RelativePositionEmbedding`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding)
: Creates a positional embedding.

[`class ReuseMultiHeadAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention)
: MultiHeadAttention layer.

[`class ReuseTransformer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer)
: Transformer layer.

[`class SelectTopK`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SelectTopK)
: Select top-k + random-k tokens according to importance.

[`class SelfAttentionMask`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SelfAttentionMask)
: Create 3D attention mask from a 2D tensor mask.

[`class SentencepieceTokenizer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer)
: Wraps `tf_text.SentencepieceTokenizer` as a Keras Layer.

[`class SpectralNormalization`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SpectralNormalization)
: Implements spectral normalization for Dense layer.

[`class SpectralNormalizationConv2D`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SpectralNormalizationConv2D)
: Implements spectral normalization for Conv2D layer based on \[3\].

[`class StridedReZeroTransformer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/StridedReZeroTransformer)
: ReZeroTransformer for packing optimization to stride over inputs.

[`class StridedTransformerEncoderBlock`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/StridedTransformerEncoderBlock)
: Transformer layer for packing optimization to stride over inputs.

[`class StridedTransformerScaffold`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/StridedTransformerScaffold)
: TransformerScaffold for packing optimization to stride over inputs.

[`class TNTransformerExpandCondense`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense)
: Transformer layer using tensor network Expand-Condense layer.

[`class TalkingHeadsAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TalkingHeadsAttention)
: Implements Talking-Heads Attention.

[`class TokenImportanceWithMovingAvg`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TokenImportanceWithMovingAvg)
: Routing based on per-token importance value.

[`class Transformer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer)
: Transformer layer.

[`class TransformerDecoderBlock`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerDecoderBlock)
: Single transformer layer for decoder.

[`class TransformerEncoderBlock`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock)
: TransformerEncoderBlock layer.

[`class TransformerScaffold`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerScaffold)
: Transformer scaffold layer.

[`class TransformerXL`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL)
: Transformer XL.

[`class TransformerXLBlock`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock)
: Transformer XL block.

[`class TwoStreamRelativeAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention)
: Two-stream relative self-attention for XLNet.

[`class VotingAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/VotingAttention)
: Voting Attention layer.

Functions
---------

[`extract_gp_layer_kwargs(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/extract_gp_layer_kwargs)
: Extracts Gaussian process layer configs from a given kwarg.

[`extract_spec_norm_kwargs(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/extract_spec_norm_kwargs)
: Extracts spectral normalization configs from a given kwarg.

[`get_mask(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/get_mask)
: Gets a 3D self-attention mask.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.