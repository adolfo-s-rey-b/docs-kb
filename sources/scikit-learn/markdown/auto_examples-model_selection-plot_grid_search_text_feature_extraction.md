Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html#sphx-glr-download-auto-examples-model-selection-plot-grid-search-text-feature-extraction-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Sample pipeline for text feature extraction and evaluation[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html#sample-pipeline-for-text-feature-extraction-and-evaluation "Link to this heading")

=============================================================================================================================================================================================================================================================

The dataset used in this example is [The 20 newsgroups text dataset](https://scikit-learn.org/stable/datasets/real_world.html#newsgroups-dataset)
 which will be automatically downloaded, cached and reused for the document classification example.

In this example, we tune the hyperparameters of a particular classifier using a [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
. For a demo on the performance of some other classifiers, see the [Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py)
 notebook.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data loading[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html#data-loading "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

We load two categories from the training set. You can adjust the number of categories by adding their names to the list or setting `categories=None` when calling the dataset loader [`fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
 to get the 20 of them.

from sklearn.datasets import [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")

categories \= \[\
    "alt.atheism",\
    "talk.religion.misc",\
\]

data\_train \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
    subset\="train",
    categories\=categories,
    shuffle\=True,
    random\_state\=42,
    remove\=("headers", "footers", "quotes"),
)

data\_test \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
    subset\="test",
    categories\=categories,
    shuffle\=True,
    random\_state\=42,
    remove\=("headers", "footers", "quotes"),
)

print(f"Loading 20 newsgroups dataset for {len(data\_train.target\_names)} categories:")
print(data\_train.target\_names)
print(f"{len(data\_train.data)} documents")

Copy to clipboard

Loading 20 newsgroups dataset for 2 categories:
\['alt.atheism', 'talk.religion.misc'\]
857 documents

Copy to clipboard

Pipeline with hyperparameter tuning[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html#pipeline-with-hyperparameter-tuning "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We define a pipeline combining a text feature vectorizer with a simple classifier yet effective for text classification.

from sklearn.feature\_extraction.text import [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
from sklearn.naive\_bayes import [ComplementNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")

pipeline \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("vect", [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")\
()),\
        ("clf", [ComplementNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")\
()),\
    \]
)
pipeline

Copy to clipboard

Pipeline(steps=\[('vect', TfidfVectorizer()), ('clf', ComplementNB())\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('vect', ...), ('clf', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

TfidfVectorizer

[?Documentation for TfidfVectorizer](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [input input: {'filename', 'file', 'content'}, default='content'  <br>  <br>\- If \`'filename'\`, the sequence passed as an argument to fit is  <br>expected to be a list of filenames that need reading to fetch  <br>the raw content to analyze.  <br>  <br>\- If \`'file'\`, the sequence items must have a 'read' method (file-like  <br>object) that is called to fetch the bytes in memory.  <br>  <br>\- If \`'content'\`, the input is expected to be a sequence of items that  <br>can be of type string or byte.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=input,-%7B%27filename%27%2C%20%27file%27%2C%20%27content%27%7D%2C%20default%3D%27content%27) | 'content' |
|     | [encoding encoding: str, default='utf-8'  <br>  <br>If bytes or files are given to analyze, this encoding is used to  <br>decode.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=encoding,-str%2C%20default%3D%27utf-8%27) | 'utf-8' |
|     | [decode\_error decode\_error: {'strict', 'ignore', 'replace'}, default='strict'  <br>  <br>Instruction on what to do if a byte sequence is given to analyze that  <br>contains characters not of the given \`encoding\`. By default, it is  <br>'strict', meaning that a UnicodeDecodeError will be raised. Other  <br>values are 'ignore' and 'replace'.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=decode_error,-%7B%27strict%27%2C%20%27ignore%27%2C%20%27replace%27%7D%2C%20default%3D%27strict%27) | 'strict' |
|     | [strip\_accents strip\_accents: {'ascii', 'unicode'} or callable, default=None  <br>  <br>Remove accents and perform other character normalization  <br>during the preprocessing step.  <br>'ascii' is a fast method that only works on characters that have  <br>a direct ASCII mapping.  <br>'unicode' is a slightly slower method that works on any characters.  <br>None (default) means no character normalization is performed.  <br>  <br>Both 'ascii' and 'unicode' use NFKD normalization from  <br>:func:\`unicodedata.normalize\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=strip_accents,-%7B%27ascii%27%2C%20%27unicode%27%7D%20or%20callable%2C%20default%3DNone) | None |
|     | [lowercase lowercase: bool, default=True  <br>  <br>Convert all characters to lowercase before tokenizing.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=lowercase,-bool%2C%20default%3DTrue) | True |
|     | [preprocessor preprocessor: callable, default=None  <br>  <br>Override the preprocessing (string transformation) stage while  <br>preserving the tokenizing and n-grams generation steps.  <br>Only applies if \`\`analyzer\`\` is not callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=preprocessor,-callable%2C%20default%3DNone) | None |
|     | [tokenizer tokenizer: callable, default=None  <br>  <br>Override the string tokenization step while preserving the  <br>preprocessing and n-grams generation steps.  <br>Only applies if \`\`analyzer == 'word'\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=tokenizer,-callable%2C%20default%3DNone) | None |
|     | [analyzer analyzer: {'word', 'char', 'char\_wb'} or callable, default='word'  <br>  <br>Whether the feature should be made of word or character n-grams.  <br>Option 'char\_wb' creates character n-grams only from text inside  <br>word boundaries; n-grams at the edges of words are padded with space.  <br>  <br>If a callable is passed it is used to extract the sequence of features  <br>out of the raw, unprocessed input.  <br>  <br>.. versionchanged:: 0.21  <br>Since v0.21, if \`\`input\`\` is \`\`'filename'\`\` or \`\`'file'\`\`, the data  <br>is first read from the file and then passed to the given callable  <br>analyzer.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=analyzer,-%7B%27word%27%2C%20%27char%27%2C%20%27char_wb%27%7D%20or%20callable%2C%20default%3D%27word%27) | 'word' |
|     | [stop\_words stop\_words: {'english'}, list, default=None  <br>  <br>If a string, it is passed to \_check\_stop\_list and the appropriate stop  <br>list is returned. 'english' is currently the only supported string  <br>value.  <br>There are several known issues with 'english' and you should  <br>consider an alternative (see :ref:\`stop\_words\`).  <br>  <br>If a list, that list is assumed to contain stop words, all of which  <br>will be removed from the resulting tokens.  <br>Only applies if \`\`analyzer == 'word'\`\`.  <br>  <br>If None, no stop words will be used. In this case, setting \`max\_df\`  <br>to a higher value, such as in the range (0.7, 1.0), can automatically detect  <br>and filter stop words based on intra corpus document frequency of terms.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=stop_words,-%7B%27english%27%7D%2C%20list%2C%20default%3DNone) | None |
|     | [token\_pattern token\_pattern: str, default=r"(?u)\\\\b\\\\w\\\\w+\\\\b"  <br>  <br>Regular expression denoting what constitutes a "token", only used  <br>if \`\`analyzer == 'word'\`\`. The default regexp selects tokens of 2  <br>or more alphanumeric characters (punctuation is completely ignored  <br>and always treated as a token separator).  <br>  <br>If there is a capturing group in token\_pattern then the  <br>captured group content, not the entire match, becomes the token.  <br>At most one capturing group is permitted.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=token_pattern,-str%2C%20default%3Dr%22%28%3Fu%29%5C%5Cb%5C%5Cw%5C%5Cw%2B%5C%5Cb%22) | '(?u)\\\\b\\\\w\\\\w+\\\\b' |
|     | [ngram\_range ngram\_range: tuple (min\_n, max\_n), default=(1, 1)  <br>  <br>The lower and upper boundary of the range of n-values for different  <br>n-grams to be extracted. All values of n such that min\_n <= n <= max\_n  <br>will be used. For example an \`\`ngram\_range\`\` of \`\`(1, 1)\`\` means only  <br>unigrams, \`\`(1, 2)\`\` means unigrams and bigrams, and \`\`(2, 2)\`\` means  <br>only bigrams.  <br>Only applies if \`\`analyzer\`\` is not callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=ngram_range,-tuple%20%28min_n%2C%20max_n%29%2C%20default%3D%281%2C%201%29) | (1, ...) |
|     | [max\_df max\_df: float or int, default=1.0  <br>  <br>When building the vocabulary ignore terms that have a document  <br>frequency strictly higher than the given threshold (corpus-specific  <br>stop words).  <br>If float in range \[0.0, 1.0\], the parameter represents a proportion of  <br>documents, integer absolute counts.  <br>This parameter is ignored if vocabulary is not None.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=max_df,-float%20or%20int%2C%20default%3D1.0) | 1.0 |
|     | [min\_df min\_df: float or int, default=1  <br>  <br>When building the vocabulary ignore terms that have a document  <br>frequency strictly lower than the given threshold. This value is also  <br>called cut-off in the literature.  <br>If float in range of \[0.0, 1.0\], the parameter represents a proportion  <br>of documents, integer absolute counts.  <br>This parameter is ignored if vocabulary is not None.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=min_df,-float%20or%20int%2C%20default%3D1) | 1   |
|     | [max\_features max\_features: int, default=None  <br>  <br>If not None, build a vocabulary that only consider the top  <br>\`max\_features\` ordered by term frequency across the corpus.  <br>Otherwise, all features are used.  <br>  <br>This parameter is ignored if vocabulary is not None.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=max_features,-int%2C%20default%3DNone) | None |
|     | [vocabulary vocabulary: Mapping or iterable, default=None  <br>  <br>Either a Mapping (e.g., a dict) where keys are terms and values are  <br>indices in the feature matrix, or an iterable over terms. If not  <br>given, a vocabulary is determined from the input documents.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=vocabulary,-Mapping%20or%20iterable%2C%20default%3DNone) | None |
|     | [binary binary: bool, default=False  <br>  <br>If True, all non-zero term counts are set to 1. This does not mean  <br>outputs will have only 0/1 values, only that the tf term in tf-idf  <br>is binary. (Set \`binary\` to True, \`use\_idf\` to False and  <br>\`norm\` to None to get 0/1 outputs).](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=binary,-bool%2C%20default%3DFalse) | False |
|     | [dtype dtype: dtype, default=float64  <br>  <br>Type of the matrix returned by fit\_transform() or transform().](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=dtype,-dtype%2C%20default%3Dfloat64) | <class 'numpy.float64'> |
|     | [norm norm: {'l1', 'l2'} or None, default='l2'  <br>  <br>Each output row will have unit norm, either:  <br>  <br>\- 'l2': Sum of squares of vector elements is 1. The cosine  <br>similarity between two vectors is their dot product when l2 norm has  <br>been applied.  <br>\- 'l1': Sum of absolute values of vector elements is 1.  <br>See :func:\`~sklearn.preprocessing.normalize\`.  <br>\- None: No normalization.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=norm,-%7B%27l1%27%2C%20%27l2%27%7D%20or%20None%2C%20default%3D%27l2%27) | 'l2' |
|     | [use\_idf use\_idf: bool, default=True  <br>  <br>Enable inverse-document-frequency reweighting. If False, idf(t) = 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=use_idf,-bool%2C%20default%3DTrue) | True |
|     | [smooth\_idf smooth\_idf: bool, default=True  <br>  <br>Smooth idf weights by adding one to document frequencies, as if an  <br>extra document was seen containing every term in the collection  <br>exactly once. Prevents zero divisions.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=smooth_idf,-bool%2C%20default%3DTrue) | True |
|     | [sublinear\_tf sublinear\_tf: bool, default=False  <br>  <br>Apply sublinear tf scaling, i.e. replace tf with 1 + log(tf).](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#:~:text=sublinear_tf,-bool%2C%20default%3DFalse) | False |

ComplementNB

[?Documentation for ComplementNB](https://scikit-learn.org/1.9/modules/generated/sklearn.naive_bayes.ComplementNB.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [alpha alpha: float or array-like of shape (n\_features,), default=1.0  <br>  <br>Additive (Laplace/Lidstone) smoothing parameter  <br>(set alpha=0 and force\_alpha=True, for no smoothing).](https://scikit-learn.org/1.9/modules/generated/sklearn.naive_bayes.ComplementNB.html#:~:text=alpha,-float%20or%20array-like%20of%20shape%20%28n_features%2C%29%2C%20default%3D1.0) | 1.0 |
|     | [force\_alpha force\_alpha: bool, default=True  <br>  <br>If False and alpha is less than 1e-10, it will set alpha to  <br>1e-10. If True, alpha will remain unchanged. This may cause  <br>numerical errors if alpha is too close to 0.  <br>  <br>.. versionadded:: 1.2  <br>.. versionchanged:: 1.4  <br>The default value of \`force\_alpha\` changed to \`True\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.naive_bayes.ComplementNB.html#:~:text=force_alpha,-bool%2C%20default%3DTrue) | True |
|     | [fit\_prior fit\_prior: bool, default=True  <br>  <br>Only used in edge case with a single class in the training set.](https://scikit-learn.org/1.9/modules/generated/sklearn.naive_bayes.ComplementNB.html#:~:text=fit_prior,-bool%2C%20default%3DTrue) | True |
|     | [class\_prior class\_prior: array-like of shape (n\_classes,), default=None  <br>  <br>Prior probabilities of the classes. Not used.](https://scikit-learn.org/1.9/modules/generated/sklearn.naive_bayes.ComplementNB.html#:~:text=class_prior,-array-like%20of%20shape%20%28n_classes%2C%29%2C%20default%3DNone) | None |
|     | [norm norm: bool, default=False  <br>  <br>Whether or not a second normalization of the weights is performed. The  <br>default behavior mirrors the implementations found in Mahout and Weka,  <br>which do not follow the full algorithm described in Table 9 of the  <br>paper.](https://scikit-learn.org/1.9/modules/generated/sklearn.naive_bayes.ComplementNB.html#:~:text=norm,-bool%2C%20default%3DFalse) | False |

  
  

We define a grid of hyperparameters to be explored by the [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
. Using a [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 instead would explore all the possible combinations on the grid, which can be costly to compute, whereas the parameter `n_iter` of the [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
 controls the number of different random combination that are evaluated. Notice that setting `n_iter` larger than the number of possible combinations in a grid would lead to repeating already-explored combinations. We search for the best parameter combination for both the feature extraction (`vect__`) and the classifier (`clf__`).

import numpy as np

parameter\_grid \= {
    "vect\_\_max\_df": (0.2, 0.4, 0.6, 0.8, 1.0),
    "vect\_\_min\_df": (1, 3, 5, 10),
    "vect\_\_ngram\_range": ((1, 1), (1, 2)),  \# unigrams or bigrams
    "vect\_\_norm": ("l1", "l2"),
    "clf\_\_alpha": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-6, 6, 13),
}

Copy to clipboard

In this case `n_iter=40` is not an exhaustive search of the hyperparameters’ grid. In practice it would be interesting to increase the parameter `n_iter` to get a more informative analysis. As a consequence, the computional time increases. We can reduce it by taking advantage of the parallelisation over the parameter combinations evaluation by increasing the number of CPUs used via the parameter `n_jobs`.

from pprint import [pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")

from sklearn.model\_selection import [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")

random\_search \= [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
(
    estimator\=pipeline,
    param\_distributions\=parameter\_grid,
    n\_iter\=40,
    random\_state\=0,
    n\_jobs\=2,
    verbose\=1,
)

print("Performing grid search...")
print("Hyperparameters to be evaluated:")
[pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
(parameter\_grid)

Copy to clipboard

Performing grid search...
Hyperparameters to be evaluated:
{'clf\_\_alpha': array(\[1.e-06, 1.e-05, 1.e-04, 1.e-03, 1.e-02, 1.e-01, 1.e+00, 1.e+01,\
       1.e+02, 1.e+03, 1.e+04, 1.e+05, 1.e+06\]),
 'vect\_\_max\_df': (0.2, 0.4, 0.6, 0.8, 1.0),
 'vect\_\_min\_df': (1, 3, 5, 10),
 'vect\_\_ngram\_range': ((1, 1), (1, 2)),
 'vect\_\_norm': ('l1', 'l2')}

Copy to clipboard

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
random\_search.fit(data\_train.data, data\_train.target)
print(f"Done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0:.3f}s")

Copy to clipboard

Fitting 5 folds for each of 40 candidates, totalling 200 fits
Done in 23.100s

Copy to clipboard

print("Best parameters combination found:")
best\_parameters \= random\_search.best\_estimator\_.get\_params()
for param\_name in sorted(parameter\_grid.keys()):
    print(f"{param\_name}: {best\_parameters\[param\_name\]}")

Copy to clipboard

Best parameters combination found:
clf\_\_alpha: 0.01
vect\_\_max\_df: 0.2
vect\_\_min\_df: 1
vect\_\_ngram\_range: (1, 1)
vect\_\_norm: l1

Copy to clipboard

test\_accuracy \= random\_search.score(data\_test.data, data\_test.target)
print(
    "Accuracy of the best parameters using the inner CV of "
    f"the random search: {random\_search.best\_score\_:.3f}"
)
print(f"Accuracy on test set: {test\_accuracy:.3f}")

Copy to clipboard

Accuracy of the best parameters using the inner CV of the random search: 0.816
Accuracy on test set: 0.709

Copy to clipboard

The prefixes `vect` and `clf` are required to avoid possible ambiguities in the pipeline, but are not necessary for visualizing the results. Because of this, we define a function that will rename the tuned hyperparameters and improve the readability.

import pandas as pd

def shorten\_param(param\_name):
    """Remove components' prefixes in param\_name."""
    if "\_\_" in param\_name:
        return param\_name.rsplit("\_\_", 1)\[1\]
    return param\_name

cv\_results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(random\_search.cv\_results\_)
cv\_results \= cv\_results.rename(shorten\_param, axis\=1)

Copy to clipboard

We can use a [plotly.express.scatter](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html)
 to visualize the trade-off between scoring time and mean test score (i.e. “CV score”). Passing the cursor over a given point displays the corresponding parameters. Error bars correspond to one standard deviation as computed in the different folds of the cross-validation.

import plotly.express as px

param\_names \= \[shorten\_param(name) for name in parameter\_grid.keys()\]
labels \= {
    "mean\_score\_time": "CV Score time (s)",
    "mean\_test\_score": "CV score (accuracy)",
}
fig \= px.scatter(
    cv\_results,
    x\="mean\_score\_time",
    y\="mean\_test\_score",
    error\_x\="std\_score\_time",
    error\_y\="std\_test\_score",
    hover\_data\=param\_names,
    labels\=labels,
)
fig.update\_layout(
    title\={
        "text": "trade-off between scoring time and mean test score",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)
fig

Copy to clipboard

0.0150.020.0250.030.0350.040.0450.050.550.60.650.70.750.80.85

trade-off between scoring time and mean test scoreCV Score time (s)CV score (accuracy)

[plotly-logomark](https://plotly.com/)

  
  

Notice that the cluster of models in the upper-left corner of the plot have the best trade-off between accuracy and scoring time. In this case, using bigrams increases the required scoring time without improving considerably the accuracy of the pipeline.

Note

For more information on how to customize an automated tuning to maximize score and minimize scoring time, see the example notebook [Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html#sphx-glr-auto-examples-model-selection-plot-grid-search-digits-py)
.

We can also use a [plotly.express.parallel\_coordinates](https://plotly.com/python-api-reference/generated/plotly.express.parallel_coordinates.html)
 to further visualize the mean test score as a function of the tuned hyperparameters. This helps finding interactions between more than two hyperparameters and provide intuition on their relevance for improving the performance of a pipeline.

We apply a `math.log10` transformation on the `alpha` axis to spread the active range and improve the readability of the plot. A value x on said axis is to be understood as 10x.

import math

column\_results \= param\_names + \["mean\_test\_score", "mean\_score\_time"\]

transform\_funcs \= dict.fromkeys(column\_results, lambda x: x)
\# Using a logarithmic scale for alpha
transform\_funcs\["alpha"\] \= [math.log10](https://docs.python.org/3/library/math.html#math.log10 "math.log10")
\# L1 norms are mapped to index 1, and L2 norms to index 2
transform\_funcs\["norm"\] \= lambda x: 2 if x \== "l2" else 1
\# Unigrams are mapped to index 1 and bigrams to index 2
transform\_funcs\["ngram\_range"\] \= lambda x: x\[1\]

fig \= px.parallel\_coordinates(
    cv\_results\[column\_results\].apply(transform\_funcs),
    color\="mean\_test\_score",
    color\_continuous\_scale\=px.colors.sequential.Viridis\_r,
    labels\=labels,
)
fig.update\_layout(
    title\={
        "text": "Parallel coordinates plot of text classifier pipeline",
        "y": 0.99,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)
fig

Copy to clipboard

0.60.650.70.750.8CV score (accuracy)Parallel coordinates plot of text classifier pipeline0.20.30.40.50.60.70.80.91max\_df10.212345678910min\_df10111.11.21.31.41.51.61.71.81.92ngram\_range2111.11.21.31.41.51.61.71.81.92norm21−6−4−20246alpha6−60.60.650.70.750.8CV score (accuracy)0.815630.562430.020.0250.030.0350.04CV Score time (s)0.0424270.018721

[plotly-logomark](https://plotly.com/)

  
  

The parallel coordinates plot displays the values of the hyperparameters on different columns while the performance metric is color coded. It is possible to select a range of results by clicking and holding on any axis of the parallel coordinate plot. You can then slide (move) the range selection and cross two selections to see the intersections. You can undo a selection by clicking once again on the same axis.

In particular for this hyperparameter search, it is interesting to notice that the top performing models do not seem to depend on the regularization `norm`, but they do depend on a trade-off between `max_df`, `min_df` and the regularization strength `alpha`. The reason is that including noisy features (i.e. `max_df` close to 1.0 or `min_df` close to 0) tend to overfit and therefore require a stronger regularization to compensate. Having less features require less regularization and less scoring time.

The best accuracy scores are obtained when `alpha` is between 10−6 and 100, regardless of the hyperparameter `norm`.

**Total running time of the script:** (0 minutes 25.120 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_grid_search_text_feature_extraction.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_grid_search_text_feature_extraction.ipynb)

[`Download Jupyter notebook: plot_grid_search_text_feature_extraction.ipynb`](https://scikit-learn.org/stable/_downloads/3992a64e742c874f5df2ba26ae9c049b/plot_grid_search_text_feature_extraction.ipynb)

[`Download Python source code: plot_grid_search_text_feature_extraction.py`](https://scikit-learn.org/stable/_downloads/091282551e0bf11fedc96b869dfa8408/plot_grid_search_text_feature_extraction.py)

[`Download zipped: plot_grid_search_text_feature_extraction.zip`](https://scikit-learn.org/stable/_downloads/7dd63f4a8fba0f2153a1e27ffc8abc36/plot_grid_search_text_feature_extraction.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png)

[Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)

Comparing Random Forests and Histogram Gradient Boosting models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/091282551e0bf11fedc96b869dfa8408/plot_grid_search_text_feature_extraction.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/3992a64e742c874f5df2ba26ae9c049b/plot_grid_search_text_feature_extraction.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/7dd63f4a8fba0f2153a1e27ffc8abc36/plot_grid_search_text_feature_extraction.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_grid_search_text_feature_extraction.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_grid_search_text_feature_extraction.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)