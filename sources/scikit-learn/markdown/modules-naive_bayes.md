[Skip to main content](https://scikit-learn.org/stable/modules/naive_bayes.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/naive_bayes.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/naive_bayes.html)
[1.8.0](https://scikit-learn.org/1.8/modules/naive_bayes.html)
[1.7.2](https://scikit-learn.org/1.7/modules/naive_bayes.html)
[1.6.1](https://scikit-learn.org/1.6/modules/naive_bayes.html)
[1.5.2](https://scikit-learn.org/1.5/modules/naive_bayes.html)
[1.4.2](https://scikit-learn.org/1.4/modules/naive_bayes.html)

Collapse Sidebar Expand Sidebar

1.9. Naive Bayes[#](https://scikit-learn.org/stable/modules/naive_bayes.html#naive-bayes "Link to this heading")

=================================================================================================================

Naive Bayes methods are a set of supervised learning algorithms based on applying Bayes’ theorem with the “naive” assumption of conditional independence between every pair of features given the value of the class variable. Bayes’ theorem states the following relationship, given class variable y and dependent feature vector x1 through xn:

P(y∣x1,…,xn)\=P(y)P(x1,…,xn∣y)P(x1,…,xn)

Using the naive conditional independence assumption that

P(xi|y,x1,…,xi−1,xi+1,…,xn)\=P(xi|y),

for all i, this relationship is simplified to

P(y∣x1,…,xn)\=P(y)∏i\=1nP(xi∣y)P(x1,…,xn)

Since P(x1,…,xn) is constant given the input, we can use the following classification rule:

P(y∣x1,…,xn)∝P(y)∏i\=1nP(xi∣y)⇓y^\=arg⁡maxyP(y)∏i\=1nP(xi∣y),

and we can use Maximum A Posteriori (MAP) estimation to estimate P(y) and P(xi∣y); the former is then the relative frequency of class y in the training set.

The different naive Bayes classifiers differ mainly by the assumptions they make regarding the distribution of P(xi∣y).

In spite of their apparently over-simplified assumptions, naive Bayes classifiers have worked quite well in many real-world situations, famously document classification and spam filtering. They require a small amount of training data to estimate the necessary parameters. (For theoretical reasons why naive Bayes works well, and on which types of data it does, see the references below.)

Naive Bayes learners and classifiers can be extremely fast compared to more sophisticated methods. The decoupling of the class conditional feature distributions means that each distribution can be independently estimated as a one-dimensional distribution. This in turn helps to alleviate problems stemming from the curse of dimensionality.

On the flip side, although naive Bayes is known as a decent classifier, it is known to be a bad estimator, so the probability outputs from `predict_proba` are not to be taken too seriously.

References[#](https://scikit-learn.org/stable/modules/naive_bayes.html#references "Link to this dropdown")

*   H. Zhang (2004). [The optimality of Naive Bayes.](https://www.cs.unb.ca/~hzhang/publications/FLAIRS04ZhangH.pdf)
     Proc. FLAIRS.
    

1.9.1. Gaussian Naive Bayes[#](https://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

[`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
 implements the Gaussian Naive Bayes algorithm for classification. The likelihood of the features is assumed to be Gaussian:

P(xi∣y)\=12πσy2exp⁡(−(xi−μy)22σy2)

The parameters σy and μy are estimated using maximum likelihood.

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.naive\_bayes import GaussianNB
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y, test\_size\=0.5, random\_state\=0)
\>>> gnb \= GaussianNB()
\>>> y\_pred \= gnb.fit(X\_train, y\_train).predict(X\_test)
\>>> print("Number of mislabeled points out of a total %d points : %d"
...       % (X\_test.shape\[0\], (y\_test != y\_pred).sum()))
Number of mislabeled points out of a total 75 points : 4

Copy to clipboard

1.9.2. Multinomial Naive Bayes[#](https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

[`MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
 implements the naive Bayes algorithm for multinomially distributed data, and is one of the two classic naive Bayes variants used in text classification (where the data are typically represented as word vector counts, although tf-idf vectors are also known to work well in practice). The distribution is parametrized by vectors θy\=(θy1,…,θyn) for each class y, where n is the number of features (in text classification, the size of the vocabulary) and θyi is the probability P(xi∣y) of feature i appearing in a sample belonging to class y.

The parameters θy are estimated by a smoothed version of maximum likelihood, i.e. relative frequency counting:

θ^yi\=Nyi+αNy+αn

where Nyi\=∑x∈Txi is the number of times feature i appears in all samples of class y in the training set T, and Ny\=∑i\=1nNyi is the total count of all features for class y.

The smoothing priors α≥0 account for features not present in the learning samples and prevent zero probabilities in further computations. Setting α\=1 is called Laplace smoothing, while α<1 is called Lidstone smoothing.

1.9.3. Complement Naive Bayes[#](https://scikit-learn.org/stable/modules/naive_bayes.html#complement-naive-bayes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

[`ComplementNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")
 implements the complement naive Bayes (CNB) algorithm. CNB is an adaptation of the standard multinomial naive Bayes (MNB) algorithm that is particularly suited for imbalanced data sets. Specifically, CNB uses statistics from the _complement_ of each class to compute the model’s weights. The inventors of CNB show empirically that the parameter estimates for CNB are more stable than those for MNB. Further, CNB regularly outperforms MNB (often by a considerable margin) on text classification tasks.

Weights calculation[#](https://scikit-learn.org/stable/modules/naive_bayes.html#weights-calculation "Link to this dropdown")

The procedure for calculating the weights is as follows:

θ^ci\=αi+∑j:yj≠cdijα+∑j:yj≠c∑kdkjwci\=log⁡θ^ciwci\=wci∑j|wcj|

where the summations are over all documents j not in class c, dij is either the count or tf-idf value of term i in document j, αi is a smoothing hyperparameter like that found in MNB, and α\=∑iαi. The second normalization addresses the tendency for longer documents to dominate parameter estimates in MNB. The classification rule is:

c^\=arg⁡minc∑itiwci

i.e., a document is assigned to the class that is the _poorest_ complement match.

References[#](https://scikit-learn.org/stable/modules/naive_bayes.html#references-2 "Link to this dropdown")

*   Rennie, J. D., Shih, L., Teevan, J., & Karger, D. R. (2003). [Tackling the poor assumptions of naive bayes text classifiers.](https://people.csail.mit.edu/jrennie/papers/icml03-nb.pdf)
     In ICML (Vol. 3, pp. 616-623).
    

1.9.4. Bernoulli Naive Bayes[#](https://scikit-learn.org/stable/modules/naive_bayes.html#bernoulli-naive-bayes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

[`BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
 implements the naive Bayes training and classification algorithms for data that is distributed according to multivariate Bernoulli distributions; i.e., there may be multiple features but each one is assumed to be a binary-valued (Bernoulli, boolean) variable. Therefore, this class requires samples to be represented as binary-valued feature vectors; if handed any other kind of data, a [`BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
 instance may binarize its input (depending on the `binarize` parameter).

The decision rule for Bernoulli naive Bayes is based on

P(xi∣y)\=P(xi\=1∣y)xi+(1−P(xi\=1∣y))(1−xi)

which differs from multinomial NB’s rule in that it explicitly penalizes the non-occurrence of a feature i that is an indicator for class y, where the multinomial variant would simply ignore a non-occurring feature.

In the case of text classification, word occurrence vectors (rather than word count vectors) may be used to train and use this classifier. [`BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
 might perform better on some datasets, especially those with shorter documents. It is advisable to evaluate both models, if time permits.

References[#](https://scikit-learn.org/stable/modules/naive_bayes.html#references-3 "Link to this dropdown")

*   C.D. Manning, P. Raghavan and H. Schütze (2008). Introduction to Information Retrieval. Cambridge University Press, pp. 234-265.
    
*   A. McCallum and K. Nigam (1998). [A comparison of event models for Naive Bayes text classification.](https://cdn.aaai.org/Workshops/1998/WS-98-05/WS98-05-007.pdf)
     Proc. AAAI/ICML-98 Workshop on Learning for Text Categorization, pp. 41-48.
    
*   V. Metsis, I. Androutsopoulos and G. Paliouras (2006). [Spam filtering with Naive Bayes – Which Naive Bayes?](https://www2.aueb.gr/users/ion/docs/ceas2006_paper.pdf)
     3rd Conf. on Email and Anti-Spam (CEAS).
    

1.9.5. Categorical Naive Bayes[#](https://scikit-learn.org/stable/modules/naive_bayes.html#categorical-naive-bayes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

[`CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
 implements the categorical naive Bayes algorithm for categorically distributed data. It assumes that each feature, which is described by the index i, has its own categorical distribution.

For each feature i in the training set X, [`CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
 estimates a categorical distribution for each feature i of X conditioned on the class y. The index set of the samples is defined as J\={1,…,m}, with m as the number of samples.

Probability calculation[#](https://scikit-learn.org/stable/modules/naive_bayes.html#probability-calculation "Link to this dropdown")

The probability of category t in feature i given class c is estimated as:

P(xi\=t∣y\=c;α)\=Ntic+αNc+αni,

where Ntic\=|{j∈J∣xij\=t,yj\=c}| is the number of times category t appears in the samples xi, which belong to class c, Nc\=|{j∈J∣yj\=c}| is the number of samples with class c, α is a smoothing parameter and ni is the number of available categories of feature i.

[`CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
 assumes that the sample matrix X is encoded (for instance with the help of [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
) such that all categories for each feature i are represented with numbers 0,...,ni−1 where ni is the number of available categories of feature i.

1.9.6. Out-of-core naive Bayes model fitting[#](https://scikit-learn.org/stable/modules/naive_bayes.html#out-of-core-naive-bayes-model-fitting "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Naive Bayes models can be used to tackle large scale classification problems for which the full training set might not fit in memory. To handle this case, [`MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
, [`BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
, and [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
 expose a `partial_fit` method that can be used incrementally as done with other classifiers as demonstrated in [Out-of-core classification of text documents](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#sphx-glr-auto-examples-applications-plot-out-of-core-classification-py)
. All naive Bayes classifiers support sample weighting.

Contrary to the `fit` method, the first call to `partial_fit` needs to be passed the list of all the expected class labels.

For an overview of available strategies in scikit-learn, see also the [out-of-core learning](https://scikit-learn.org/stable/computing/scaling_strategies.html#scaling-strategies)
 documentation.

Note

The `partial_fit` method call of naive Bayes models introduces some computational overhead. It is recommended to use data chunk sizes that are as large as possible, that is as the available RAM allows.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)