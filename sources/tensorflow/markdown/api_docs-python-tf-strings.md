[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/strings#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.strings Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/strings#functions)
    

Public API for tf.\_api.v2.strings namespace

Functions
---------

[`as_string(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/as_string)
: Converts each entry in the given tensor to strings.

[`bytes_split(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/bytes_split)
: Split string elements of `input` into bytes.

[`format(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/format)
: Formats a string template using a list of tensors.

[`join(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/join)
: Perform element-wise concatenation of a list of string tensors.

[`length(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/length)
: String lengths of `input`.

[`lower(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/lower)
: Converts all uppercase characters into their respective lowercase replacements.

[`ngrams(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams)
: Create a tensor of n-grams based on `data`.

[`reduce_join(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/reduce_join)
: Joins all strings into a single string, or joins along an axis.

[`regex_full_match(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/regex_full_match)
: Check if the input matches the regex pattern.

[`regex_replace(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/regex_replace)
: Replace elements of `input` matching regex `pattern` with `rewrite`.

[`split(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/split)
: Split elements of `input` based on `sep` into a `RaggedTensor`.

[`strip(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/strip)
: Strip leading and trailing whitespaces from the Tensor.

[`substr(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/substr)
: Return substrings from `Tensor` of strings.

[`to_hash_bucket(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket)
: Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_hash_bucket_fast(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast)
: Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_hash_bucket_strong(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong)
: Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_number(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/to_number)
: Converts each string in the input Tensor to the specified numeric type.

[`unicode_decode(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_decode)
: Decodes each string in `input` into a sequence of Unicode code points.

[`unicode_decode_with_offsets(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_decode_with_offsets)
: Decodes each string into a sequence of code points with start offsets.

[`unicode_encode(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_encode)
: Encodes each sequence of Unicode code points in `input` into a string.

[`unicode_script(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_script)
: Determine the script codes of a given tensor of Unicode integer code points.

[`unicode_split(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split)
: Splits each string in `input` into a sequence of Unicode code points.

[`unicode_split_with_offsets(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_split_with_offsets)
: Splits each string into a sequence of code points with start offsets.

[`unicode_transcode(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/unicode_transcode)
: Transcode the input text from a source encoding to a destination encoding.

[`unsorted_segment_join(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join)
: Joins the elements of `inputs` based on `segment_ids`.

[`upper(...)`](https://www.tensorflow.org/api_docs/python/tf/strings/upper)
: Converts all lowercase characters into their respective uppercase replacements.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.