[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html)

Collapse Sidebar Expand Sidebar

HashingVectorizer[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#hashingvectorizer "Link to this heading")

========================================================================================================================================================================

class sklearn.feature\_extraction.text.HashingVectorizer(_\*_, _input\='content'_, _encoding\='utf-8'_, _decode\_error\='strict'_, _strip\_accents\=None_, _lowercase\=True_, _preprocessor\=None_, _tokenizer\=None_, _stop\_words\=None_, _token\_pattern\='(?u)\\\\b\\\\w\\\\w+\\\\b'_, _ngram\_range\=(1_, _1)_, _analyzer\='word'_, _n\_features\=1048576_, _binary\=False_, _norm\='l2'_, _alternate\_sign\=True_, _dtype\=<class 'numpy.float64'>_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L568)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "Link to this definition")

Convert a collection of text documents to a matrix of token occurrences.

It turns a collection of text documents into a scipy.sparse matrix holding token occurrence counts (or binary occurrence information), possibly normalized as token frequencies if norm=’l1’ or projected on the euclidean unit sphere if norm=’l2’.

This text vectorizer implementation uses the hashing trick to find the token string name to feature integer index mapping.

This strategy has several advantages:

*   it is very low memory scalable to large datasets as there is no need to store a vocabulary dictionary in memory.
    
*   it is fast to pickle and un-pickle as it holds no state besides the constructor parameters.
    
*   it can be used in a streaming (partial fit) or parallel pipeline as there is no state computed during fit.
    

There are also a couple of cons (vs using a CountVectorizer with an in-memory vocabulary):

*   there is no way to compute the inverse transform (from feature indices to string feature names) which can be a problem when trying to introspect which features are most important to a model.
    
*   there can be collisions: distinct tokens can be mapped to the same feature index. However in practice this is rarely an issue if n\_features is large enough (e.g. 2 \*\* 18 for text classification problems).
    
*   no IDF weighting as this would render the transformer stateful.
    

The hash function employed is the signed 32-bit version of Murmurhash3.

For an efficiency comparison of the different feature extractors, see [FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#sphx-glr-auto-examples-text-plot-hashing-vs-dict-vectorizer-py)
.

For an example of document clustering and comparison with [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
, see [Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-document-clustering-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
.

Parameters:

**input**{‘filename’, ‘file’, ‘content’}, default=’content’

*   If `'filename'`, the sequence passed as an argument to fit is expected to be a list of filenames that need reading to fetch the raw content to analyze.
    
*   If `'file'`, the sequence items must have a ‘read’ method (file-like object) that is called to fetch the bytes in memory.
    
*   If `'content'`, the input is expected to be a sequence of items that can be of type string or byte.
    

**encoding**str, default=’utf-8’

If bytes or files are given to analyze, this encoding is used to decode.

**decode\_error**{‘strict’, ‘ignore’, ‘replace’}, default=’strict’

Instruction on what to do if a byte sequence is given to analyze that contains characters not of the given `encoding`. By default, it is ‘strict’, meaning that a UnicodeDecodeError will be raised. Other values are ‘ignore’ and ‘replace’.

**strip\_accents**{‘ascii’, ‘unicode’} or callable, default=None

Remove accents and perform other character normalization during the preprocessing step. ‘ascii’ is a fast method that only works on characters that have a direct ASCII mapping. ‘unicode’ is a slightly slower method that works on any character. None (default) means no character normalization is performed.

Both ‘ascii’ and ‘unicode’ use NFKD normalization from [`unicodedata.normalize`](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize "(in Python v3.14)")
.

**lowercase**bool, default=True

Convert all characters to lowercase before tokenizing.

**preprocessor**callable, default=None

Override the preprocessing (string transformation) stage while preserving the tokenizing and n-grams generation steps. Only applies if `analyzer` is not callable.

**tokenizer**callable, default=None

Override the string tokenization step while preserving the preprocessing and n-grams generation steps. Only applies if `analyzer == 'word'`.

**stop\_words**{‘english’}, list, default=None

If ‘english’, a built-in stop word list for English is used. There are several known issues with ‘english’ and you should consider an alternative (see [Using stop words](https://scikit-learn.org/stable/modules/feature_extraction.html#stop-words)
).

If a list, that list is assumed to contain stop words, all of which will be removed from the resulting tokens. Only applies if `analyzer == 'word'`.

**token\_pattern**str or None, default=r”(?u)\\b\\w\\w+\\b”

Regular expression denoting what constitutes a “token”, only used if `analyzer == 'word'`. The default regexp selects tokens of 2 or more alphanumeric characters (punctuation is completely ignored and always treated as a token separator).

If there is a capturing group in token\_pattern then the captured group content, not the entire match, becomes the token. At most one capturing group is permitted.

**ngram\_range**tuple (min\_n, max\_n), default=(1, 1)

The lower and upper boundary of the range of n-values for different n-grams to be extracted. All values of n such that min\_n <= n <= max\_n will be used. For example an `ngram_range` of `(1, 1)` means only unigrams, `(1, 2)` means unigrams and bigrams, and `(2, 2)` means only bigrams. Only applies if `analyzer` is not callable.

**analyzer**{‘word’, ‘char’, ‘char\_wb’} or callable, default=’word’

Whether the feature should be made of word or character n-grams. Option ‘char\_wb’ creates character n-grams only from text inside word boundaries; n-grams at the edges of words are padded with space.

If a callable is passed it is used to extract the sequence of features out of the raw, unprocessed input.

Changed in version 0.21: Since v0.21, if `input` is `'filename'` or `'file'`, the data is first read from the file and then passed to the given callable analyzer.

**n\_features**int, default=(2 \*\* 20)

The number of features (columns) in the output matrices. Small numbers of features are likely to cause hash collisions, but large numbers will cause larger coefficient dimensions in linear learners.

**binary**bool, default=False

If True, all non zero counts are set to 1. This is useful for discrete probabilistic models that model binary events rather than integer counts.

**norm**{‘l1’, ‘l2’}, default=’l2’

Norm used to normalize term vectors. None for no normalization.

**alternate\_sign**bool, default=True

When True, an alternating sign is added to the features as to approximately conserve the inner product in the hashed space even for small n\_features. This approach is similar to sparse random projection.

Added in version 0.19.

**dtype**type, default=np.float64

Type of the matrix returned by fit\_transform() or transform().

See also

[`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")

Convert a collection of text documents to a matrix of token counts.

[`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")

Convert a collection of raw documents to a matrix of TF-IDF features.

Notes

This estimator is [stateless](https://scikit-learn.org/stable/glossary.html#term-stateless)
 and does not need to be fitted. However, we recommend to call [`fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.fit_transform "sklearn.feature_extraction.text.HashingVectorizer.fit_transform")
 instead of [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.transform "sklearn.feature_extraction.text.HashingVectorizer.transform")
, as parameter validation is only performed in [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.fit "sklearn.feature_extraction.text.HashingVectorizer.fit")
.

Examples

\>>> from sklearn.feature\_extraction.text import HashingVectorizer
\>>> corpus \= \[\
...     'This is the first document.',\
...     'This document is the second document.',\
...     'And this is the third one.',\
...     'Is this the first document?',\
... \]
\>>> vectorizer \= HashingVectorizer(n\_features\=2\*\*4)
\>>> X \= vectorizer.fit\_transform(corpus)
\>>> print(X.shape)
(4, 16)

Copy to clipboard

build\_analyzer()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L425)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.build_analyzer "Link to this definition")

Return a callable to process input data.

The callable handles preprocessing, tokenization, and n-grams generation.

Returns:

analyzer: callable

A function to handle preprocessing, tokenization and n-grams generation.

build\_preprocessor()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L329)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.build_preprocessor "Link to this definition")

Return a function to preprocess the text before tokenization.

Returns:

preprocessor: callable

A function to preprocess the text before tokenization.

build\_tokenizer()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L356)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.build_tokenizer "Link to this definition")

Return a function that splits a string into a sequence of tokens.

Returns:

tokenizer: callable

A function to split a string into a sequence of tokens.

decode(_doc_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L216)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.decode "Link to this definition")

Decode the input into a string of unicode symbols.

The decoding strategy depends on the vectorizer parameters.

Parameters:

**doc**bytes or str

The string to decode.

Returns:

doc: str

A string of unicode symbols.

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L833)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.fit "Link to this definition")

Only validates estimator’s parameters.

This method allows to: (i) validate the estimator’s parameters and (ii) be consistent with the scikit-learn transformer API.

Parameters:

**X**ndarray of shape \[n\_samples, n\_features\]

Training data.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

HashingVectorizer instance.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L895)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.fit_transform "Link to this definition")

Transform a sequence of documents to a document-term matrix.

Parameters:

**X**iterable over raw text documents, length = n\_samples

Samples. Each sample must be a text document (either bytes or unicode strings, file name or file object depending on the constructor argument) which will be tokenized and hashed.

**y**any

Ignored. This parameter exists only for compatibility with sklearn.pipeline.Pipeline.

Returns:

**X**sparse matrix of shape (n\_samples, n\_features)

Document-term matrix.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_stop\_words()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L376)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.get_stop_words "Link to this definition")

Build or fetch the effective stop words list.

Returns:

stop\_words: list or None

A list of stop words.

partial\_fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L811)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.partial_fit "Link to this definition")

Only validates estimator’s parameters.

This method allows to: (i) validate the estimator’s parameters and (ii) be consistent with the scikit-learn transformer API.

Parameters:

**X**ndarray of shape \[n\_samples, n\_features\]

Training data.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

HashingVectorizer instance.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Added in version 1.4: `"polars"` option was added.

Returns:

**self**estimator instance

Estimator instance.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L865)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer.transform "Link to this definition")

Transform a sequence of documents to a document-term matrix.

Parameters:

**X**iterable over raw text documents, length = n\_samples

Samples. Each sample must be a text document (either bytes or unicode strings, file name or file object depending on the constructor argument) which will be tokenized and hashed.

Returns:

**X**sparse matrix of shape (n\_samples, n\_features)

Document-term matrix.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_out_of_core_classification_thumb.png)

[Out-of-core classification of text documents](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html)

Out-of-core classification of text documents

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_thumb.png)

[FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

FeatureHasher and DictVectorizer Comparison

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)