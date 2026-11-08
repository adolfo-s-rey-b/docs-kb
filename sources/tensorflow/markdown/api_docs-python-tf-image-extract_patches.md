[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.extract\_patches Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L6234-L6358)

Extract `patches` from `images`.

tf.image.extract_patches(
        images, sizes, strides, rates, padding, name=None
    )

This op collects patches from the input image, as if applying a convolution. All extracted patches are stacked in the depth (last) dimension of the output.

Specifically, the op extracts patches of shape `sizes` which are `strides` apart in the input image. The output is subsampled using the `rates` argument, in the same manner as "atrous" or "dilated" convolutions.

The result is a 4D tensor which is indexed by batch, row, and column. `output[i, x, y]` contains a flattened patch of size `sizes[1], sizes[2]` which is taken from the input starting at `images[i, x*strides[1], y*strides[2]]`.

Each output patch can be reshaped to `sizes[1], sizes[2], depth`, where `depth` is `images.shape[3]`.

The output elements are taken from the input at intervals given by the `rate` argument, as in dilated convolutions.

The `padding` argument has no effect on the size of each patch, it determines how many patches are extracted. If `VALID`, only patches which are fully contained in the input image are included. If `SAME`, all patches whose starting point is inside the input are included, and areas outside the input default to zero.

#### Example:

  n = 10
      # images is a 1 x 10 x 10 x 1 array that contains the numbers 1 through 100
      images = [[[[x * n + y + 1] for y in range(n)] for x in range(n)]]
    
      # We generate two outputs as follows:
      # 1. 3x3 patches with stride length 5
      # 2. Same as above, but the rate is increased to 2
      tf.image.extract_patches(images=images,
                               sizes=[1, 3, 3, 1],
                               strides=[1, 5, 5, 1],
                               rates=[1, 1, 1, 1],
                               padding='VALID')
    
      # Yields:
      [[[[ 1  2  3 11 12 13 21 22 23]\
         [ 6  7  8 16 17 18 26 27 28]]\
        [[51 52 53 61 62 63 71 72 73]\
         [56 57 58 66 67 68 76 77 78]]]]

If we mark the pixels in the input image which are taken for the output with `*`, we see the pattern:

   *  *  *  4  5  *  *  *  9 10
       *  *  * 14 15  *  *  * 19 20
       *  *  * 24 25  *  *  * 29 30
      31 32 33 34 35 36 37 38 39 40
      41 42 43 44 45 46 47 48 49 50
       *  *  * 54 55  *  *  * 59 60
       *  *  * 64 65  *  *  * 69 70
       *  *  * 74 75  *  *  * 79 80
      81 82 83 84 85 86 87 88 89 90
      91 92 93 94 95 96 97 98 99 100

  tf.image.extract_patches(images=images,
                               sizes=[1, 3, 3, 1],
                               strides=[1, 5, 5, 1],
                               rates=[1, 2, 2, 1],
                               padding='VALID')
    
      # Yields:
      [[[[  1   3   5  21  23  25  41  43  45]\
         [  6   8  10  26  28  30  46  48  50]]\
    \
        [[ 51  53  55  71  73  75  91  93  95]\
         [ 56  58  60  76  78  80  96  98 100]]]]

We can again draw the effect, this time using the symbols `*`, `x`, `+` and `o` to distinguish the patches:

   *  2  *  4  *  x  7  x  9  x
      11 12 13 14 15 16 17 18 19 20
       * 22  * 24  *  x 27  x 29  x
      31 32 33 34 35 36 37 38 39 40
       * 42  * 44  *  x 47  x 49  x
       + 52  + 54  +  o 57  o 59  o
      61 62 63 64 65 66 67 68 69 70
       + 72  + 74  +  o 77  o 79  o
      81 82 83 84 85 86 87 88 89 90
       + 92  + 94  +  o 97  o 99  o

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A 4-D Tensor with shape `[batch, in_rows, in_cols, depth]`. |
| `sizes` | The size of the extracted patches. Must be `[1, size_rows, size_cols, 1]`. |
| `strides` | A 1-D Tensor of length 4. How far the centers of two consecutive patches are in the images. Must be: `[1, stride_rows, stride_cols, 1]`. |
| `rates` | A 1-D Tensor of length 4. Must be: `[1, rate_rows, rate_cols, 1]`. This is the input stride, specifying how far two consecutive patch samples are in the input. Equivalent to extracting patches with `patch_sizes_eff = patch_sizes + (patch_sizes - 1) * (rates - 1)`, followed by subsampling them spatially by a factor of `rates`. This is equivalent to `rate` in dilated (a.k.a. Atrous) convolutions. |
| `padding` | The type of padding algorithm to use. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A 4-D Tensor of the same type as the input. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.