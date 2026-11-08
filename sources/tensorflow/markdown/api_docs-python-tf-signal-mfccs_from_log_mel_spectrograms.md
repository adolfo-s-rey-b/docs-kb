[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsignal%2Fmfccs_from_log_mel_spectrograms&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.mfccs\_from\_log\_mel\_spectrograms Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/mfcc_ops.py#L25-L107)

Computes [MFCCs](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
 of `log_mel_spectrograms`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.mfccs_from_log_mel_spectrograms`](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms)

tf.signal.mfccs_from_log_mel_spectrograms(
        log_mel_spectrograms, name=None
    )

Implemented with GPU-compatible ops and supports gradients.

[Mel-Frequency Cepstral Coefficient (MFCC)](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
 calculation consists of taking the DCT-II of a log-magnitude mel-scale spectrogram. [HTK](https://en.wikipedia.org/wiki/HTK_(software))
's MFCCs use a particular scaling of the DCT-II which is almost orthogonal normalization. We follow this convention.

All `num_mel_bins` MFCCs are returned and it is up to the caller to select a subset of the MFCCs based on their application. For example, it is typical to only use the first few for speech recognition, as this results in an approximately pitch-invariant representation of the signal.

#### For example:

batch_size, num_samples, sample_rate = 32, 32000, 16000.0
    # A Tensor of [batch_size, num_samples] mono PCM samples in the range [-1, 1].
    pcm = tf.random.normal([batch_size, num_samples], dtype=tf.float32)
    
    # A 1024-point STFT with frames of 64 ms and 75% overlap.
    stfts = tf.signal.stft(pcm, frame_length=1024, frame_step=256,
                           fft_length=1024)
    spectrograms = tf.abs(stfts)
    
    # Warp the linear scale spectrograms into the mel-scale.
    num_spectrogram_bins = stfts.shape[-1].value
    lower_edge_hertz, upper_edge_hertz, num_mel_bins = 80.0, 7600.0, 80
    linear_to_mel_weight_matrix = tf.signal.linear_to_mel_weight_matrix(
      num_mel_bins, num_spectrogram_bins, sample_rate, lower_edge_hertz,
      upper_edge_hertz)
    mel_spectrograms = tf.tensordot(
      spectrograms, linear_to_mel_weight_matrix, 1)
    mel_spectrograms.set_shape(spectrograms.shape[:-1].concatenate(
      linear_to_mel_weight_matrix.shape[-1:]))
    
    # Compute a stabilized log to get log-magnitude mel-scale spectrograms.
    log_mel_spectrograms = tf.math.log(mel_spectrograms + 1e-6)
    
    # Compute MFCCs from log_mel_spectrograms and take the first 13.
    mfccs = tf.signal.mfccs_from_log_mel_spectrograms(
      log_mel_spectrograms)[..., :13]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `log_mel_spectrograms` | A `[..., num_mel_bins]` `float32`/`float64` `Tensor` of log-magnitude mel-scale spectrograms. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `[..., num_mel_bins]` `float32`/`float64` `Tensor` of the MFCCs of `log_mel_spectrograms`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `num_mel_bins` is not positive. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.