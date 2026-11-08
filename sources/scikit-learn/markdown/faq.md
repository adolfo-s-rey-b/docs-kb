[Skip to main content](https://scikit-learn.org/stable/faq.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/faq.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/faq.html)
[1.8.0](https://scikit-learn.org/1.8/faq.html)
[1.7.2](https://scikit-learn.org/1.7/faq.html)
[1.6.1](https://scikit-learn.org/1.6/faq.html)
[1.5.2](https://scikit-learn.org/1.5/faq.html)
[1.4.2](https://scikit-learn.org/1.4/faq.html)

Frequently Asked Questions[#](https://scikit-learn.org/stable/faq.html#frequently-asked-questions "Link to this heading")

==========================================================================================================================

Here we try to give some answers to questions that regularly pop up on the mailing list.

[About the project](https://scikit-learn.org/stable/faq.html#id2)
[#](https://scikit-learn.org/stable/faq.html#about-the-project "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

### [What is the project name (a lot of people get it wrong)?](https://scikit-learn.org/stable/faq.html#id3)
[#](https://scikit-learn.org/stable/faq.html#what-is-the-project-name-a-lot-of-people-get-it-wrong "Link to this heading")

scikit-learn, but not scikit or SciKit nor sci-kit learn. Also not scikits.learn or scikits-learn, which were previously used.

### [How do you pronounce the project name?](https://scikit-learn.org/stable/faq.html#id4)
[#](https://scikit-learn.org/stable/faq.html#how-do-you-pronounce-the-project-name "Link to this heading")

sy-kit learn. sci stands for science!

### [Why scikit?](https://scikit-learn.org/stable/faq.html#id5)
[#](https://scikit-learn.org/stable/faq.html#why-scikit "Link to this heading")

There are multiple scikits, which are scientific toolboxes built around SciPy. Apart from scikit-learn, another popular one is [scikit-image](https://scikit-image.org/)
.

### [Do you support PyPy?](https://scikit-learn.org/stable/faq.html#id6)
[#](https://scikit-learn.org/stable/faq.html#do-you-support-pypy "Link to this heading")

Due to limited maintainer resources and small number of users, using scikit-learn with [PyPy](https://pypy.org/)
 (an alternative Python implementation with a built-in just-in-time compiler) is not officially supported.

### [How can I obtain permission to use the images in scikit-learn for my work?](https://scikit-learn.org/stable/faq.html#id7)
[#](https://scikit-learn.org/stable/faq.html#how-can-i-obtain-permission-to-use-the-images-in-scikit-learn-for-my-work "Link to this heading")

The images contained in the [scikit-learn repository](https://github.com/scikit-learn/scikit-learn)
 and the images generated within the [scikit-learn documentation](https://scikit-learn.org/stable/index.html)
 can be used via the [BSD 3-Clause License](https://github.com/scikit-learn/scikit-learn?tab=BSD-3-Clause-1-ov-file)
 for your work. Citations of scikit-learn are highly encouraged and appreciated. See [citing scikit-learn](https://scikit-learn.org/stable/about.html#citing-scikit-learn)
.

However, the scikit-learn logo is subject to some terms and conditions. See [Branding & Logos](https://scikit-learn.org/stable/about.html#branding-and-logos)
.

[Implementation decisions](https://scikit-learn.org/stable/faq.html#id8)
[#](https://scikit-learn.org/stable/faq.html#implementation-decisions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Why is there no support for deep or reinforcement learning? Will there be such support in the future?](https://scikit-learn.org/stable/faq.html#id9)
[#](https://scikit-learn.org/stable/faq.html#why-is-there-no-support-for-deep-or-reinforcement-learning-will-there-be-such-support-in-the-future "Link to this heading")

Deep learning and reinforcement learning both require a rich vocabulary to define an architecture, with deep learning additionally requiring GPUs for efficient computing. However, neither of these fit within the design constraints of scikit-learn. As a result, deep learning and reinforcement learning are currently out of scope for what scikit-learn seeks to achieve.

You can find more information about the addition of GPU support at [Will you add GPU support?](https://scikit-learn.org/stable/faq.html#will-you-add-gpu-support)
.

Note that scikit-learn currently implements a simple multilayer perceptron in [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
. We will only accept bug fixes for this module. If you want to implement more complex deep learning models, please turn to popular deep learning frameworks such as [tensorflow](https://www.tensorflow.org/)
, [keras](https://keras.io/)
, and [pytorch](https://pytorch.org/)
.

### [Will you add graphical models or sequence prediction to scikit-learn?](https://scikit-learn.org/stable/faq.html#id10)
[#](https://scikit-learn.org/stable/faq.html#will-you-add-graphical-models-or-sequence-prediction-to-scikit-learn "Link to this heading")

Not in the foreseeable future. scikit-learn tries to provide a unified API for the basic tasks in machine learning, with pipelines and meta-algorithms like grid search to tie everything together. The required concepts, APIs, algorithms and expertise required for structured learning are different from what scikit-learn has to offer. If we started doing arbitrary structured learning, we’d need to redesign the whole package and the project would likely collapse under its own weight.

There are two projects with API similar to scikit-learn that do structured prediction:

*   [pystruct](https://pystruct.github.io/)
     handles general structured learning (focuses on SSVMs on arbitrary graph structures with approximate inference; defines the notion of sample as an instance of the graph structure).
    
*   [seqlearn](https://larsmans.github.io/seqlearn/)
     handles sequences only (focuses on exact inference; has HMMs, but mostly for the sake of completeness; treats a feature vector as a sample and uses an offset encoding for the dependencies between feature vectors).
    

### [Why did you remove HMMs from scikit-learn?](https://scikit-learn.org/stable/faq.html#id11)
[#](https://scikit-learn.org/stable/faq.html#why-did-you-remove-hmms-from-scikit-learn "Link to this heading")

See [Will you add graphical models or sequence prediction to scikit-learn?](https://scikit-learn.org/stable/faq.html#adding-graphical-models)
.

### [Will you add GPU support?](https://scikit-learn.org/stable/faq.html#id12)
[#](https://scikit-learn.org/stable/faq.html#will-you-add-gpu-support "Link to this heading")

Adding GPU support by default would introduce heavy hardware-specific software dependencies and existing algorithms would need to be reimplemented. This would make it both harder for the average user to install scikit-learn and harder for the developers to maintain the code.

However, since 2023, a limited but growing [list of scikit-learn estimators](https://scikit-learn.org/stable/modules/array_api.html#array-api-supported)
 can already run on GPUs if the input data is provided as a PyTorch or CuPy array and if scikit-learn has been configured to accept such inputs as explained in [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
. This Array API support allows scikit-learn to run on GPUs without introducing heavy and hardware-specific software dependencies to the main package.

Most estimators that rely on NumPy for their computationally intensive operations can be considered for Array API support and therefore GPU support.

However, not all scikit-learn estimators are amenable to efficiently running on GPUs via the Array API for fundamental algorithmic reasons. For instance, tree-based models currently implemented with Cython in scikit-learn are fundamentally not array-based algorithms. Other algorithms such as k-means or k-nearest neighbors rely on array-based algorithms but are also implemented in Cython. Cython is used to manually interleave consecutive array operations to avoid introducing performance killing memory access to large intermediate arrays: this low-level algorithmic rewrite is called “kernel fusion” and cannot be expressed via the Array API for the foreseeable future.

Adding efficient GPU support to estimators that cannot be efficiently implemented with the Array API would require designing and adopting a more flexible extension system for scikit-learn. This possibility is being considered in the following GitHub issue (under discussion):

*   [scikit-learn/scikit-learn#22438](https://github.com/scikit-learn/scikit-learn/issues/22438)
    

### [Why do categorical variables need preprocessing in scikit-learn, compared to other tools?](https://scikit-learn.org/stable/faq.html#id13)
[#](https://scikit-learn.org/stable/faq.html#why-do-categorical-variables-need-preprocessing-in-scikit-learn-compared-to-other-tools "Link to this heading")

Most of scikit-learn assumes data is in NumPy arrays or SciPy sparse matrices of a single numeric dtype. These do not explicitly represent categorical variables at present. Thus, unlike R’s `data.frames` or [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v3.0.5)")
, we require explicit conversion of categorical features to numeric values, as discussed in [Encoding categorical features](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features)
. See also [Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#sphx-glr-auto-examples-compose-plot-column-transformer-mixed-types-py)
 for an example of working with heterogeneous (e.g. categorical and numeric) data.

Note that recently, [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 and [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 gained native support for categorical features through the option `categorical_features="from_dtype"`. This option relies on inferring which columns of the data are categorical based on the [`pandas.CategoricalDtype`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "(in pandas v3.0.5)")
 and `polars.datatypes.Categorical` dtypes.

### [Does scikit-learn work natively with various types of dataframes?](https://scikit-learn.org/stable/faq.html#id14)
[#](https://scikit-learn.org/stable/faq.html#does-scikit-learn-work-natively-with-various-types-of-dataframes "Link to this heading")

Scikit-learn has limited support for [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v3.0.5)")
 and `polars.DataFrame`. Scikit-learn estimators can accept both these dataframe types as input, and scikit-learn transformers can output dataframes using the `set_output` API. For more details, refer to [Pandas/Polars Output for Transformers with set\_output API](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
.

However, the internal computations in scikit-learn estimators rely on numerical operations that are more efficiently performed on homogeneous data structures such as NumPy arrays or SciPy sparse matrices. As a result, most scikit-learn estimators will internally convert dataframe inputs into these homogeneous data structures. Similarly, dataframe outputs are generated from these homogeneous data structures.

Also note that [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 makes it convenient to handle heterogeneous pandas dataframes by mapping homogeneous subsets of dataframe columns selected by name or dtype to dedicated scikit-learn transformers. Therefore [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 are often used in the first step of scikit-learn pipelines when dealing with heterogeneous dataframes (see [Pipeline: chaining estimators](https://scikit-learn.org/stable/modules/compose.html#pipeline)
 for more details).

See also [Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#sphx-glr-auto-examples-compose-plot-column-transformer-mixed-types-py)
 for an example of working with heterogeneous (e.g. categorical and numeric) data.

### [Do you plan to implement transform for target `y` in a pipeline?](https://scikit-learn.org/stable/faq.html#id15)
[#](https://scikit-learn.org/stable/faq.html#do-you-plan-to-implement-transform-for-target-y-in-a-pipeline "Link to this heading")

Currently transform only works for features `X` in a pipeline. There’s a long-standing discussion about not being able to transform `y` in a pipeline. Follow on GitHub issue [#4143](https://github.com/scikit-learn/scikit-learn/issues/4143)
. Meanwhile, you can check out [`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
, [pipegraph](https://github.com/mcasl/PipeGraph)
, and [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)
. Note that scikit-learn solved for the case where `y` has an invertible transformation applied before training and inverted after prediction. scikit-learn intends to solve for use cases where `y` should be transformed at training time and not at test time, for resampling and similar uses, like at [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)
. In general, these use cases can be solved with a custom meta estimator rather than a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
.

### [Why are there so many different estimators for linear models?](https://scikit-learn.org/stable/faq.html#id16)
[#](https://scikit-learn.org/stable/faq.html#why-are-there-so-many-different-estimators-for-linear-models "Link to this heading")

Usually, there is one classifier and one regressor per model type, e.g. [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
 and [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
. Both have similar options and both have the parameter `loss`, which is especially useful in the regression case as it enables the estimation of conditional mean as well as conditional quantiles.

For linear models, there are many estimator classes which are very close to each other. Let us have a look at

*   [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    , no penalty
    
*   [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , L2 penalty
    
*   [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    , L1 penalty (sparse models)
    
*   [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , L1 + L2 penalty (less sparse models)
    
*   [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     with `loss="squared_loss"`
    

**Maintainer perspective:** They all do in principle the same and are different only by the penalty they impose. This, however, has a large impact on the way the underlying optimization problem is solved. In the end, this amounts to usage of different methods and tricks from linear algebra. A special case is [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
 which comprises all 4 previous models and is different by the optimization procedure. A further side effect is that the different estimators favor different data layouts (`X` C-contiguous or F-contiguous, sparse csr or csc). This complexity of the seemingly simple linear models is the reason for having different estimator classes for different penalties.

**User perspective:** First, the current design is inspired by the scientific literature where linear regression models with different regularization/penalty were given different names, e.g. _ridge regression_. Having different model classes with according names makes it easier for users to find those regression models. Secondly, if all the 5 above mentioned linear models were unified into a single class, there would be parameters with a lot of options like the `solver` parameter. On top of that, there would be a lot of exclusive interactions between different parameters. For example, the possible options of the parameters `solver`, `precompute` and `selection` would depend on the chosen values of the penalty parameters `alpha` and `l1_ratio`.

[Contributing](https://scikit-learn.org/stable/faq.html#id17)
[#](https://scikit-learn.org/stable/faq.html#contributing "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

### [How can I contribute to scikit-learn?](https://scikit-learn.org/stable/faq.html#id18)
[#](https://scikit-learn.org/stable/faq.html#how-can-i-contribute-to-scikit-learn "Link to this heading")

See [Contributing](https://scikit-learn.org/stable/developers/contributing.html#contributing)
. Before wanting to add a new algorithm, which is usually a major and lengthy undertaking, it is recommended to start with [known issues](https://scikit-learn.org/stable/developers/contributing.html#new-contributors)
. Please do not contact the contributors of scikit-learn directly regarding contributing to scikit-learn.

### [Why is my pull request not getting any attention?](https://scikit-learn.org/stable/faq.html#id19)
[#](https://scikit-learn.org/stable/faq.html#why-is-my-pull-request-not-getting-any-attention "Link to this heading")

The scikit-learn review process takes a significant amount of time, and contributors should not be discouraged by a lack of activity or review on their pull request. We care a lot about getting things right the first time, as maintenance and later change comes at a high cost. We rarely release any “experimental” code, so all of our contributions will be subject to high use immediately and should be of the highest quality possible initially.

Beyond that, scikit-learn is limited in its reviewing bandwidth; many of the reviewers and core developers are working on scikit-learn on their own time. If a review of your pull request comes slowly, it is likely because the reviewers are busy. We ask for your understanding and request that you not close your pull request or discontinue your work solely because of this reason.

For tips on how to make your pull request easier to review and more likely to be reviewed quickly, see [How do I improve my issue or pull request?](https://scikit-learn.org/stable/faq.html#improve-issue-pr)
.

### [How do I improve my issue or pull request?](https://scikit-learn.org/stable/faq.html#id20)
[#](https://scikit-learn.org/stable/faq.html#how-do-i-improve-my-issue-or-pull-request "Link to this heading")

To help your issue receive attention or improve the likelihood of your pull request being reviewed, you can try:

*   follow our [contribution guidelines](https://scikit-learn.org/stable/developers/contributing.html#contributing)
    , in particular [Automated Contributions Policy](https://scikit-learn.org/stable/developers/contributing.html#automated-contributions-policy)
    , [How to make a good bug report](https://scikit-learn.org/stable/developers/contributing.html#filing-bugs)
    , [Stalled pull requests](https://scikit-learn.org/stable/developers/contributing.html#stalled-pull-request)
     and [Stalled and Unclaimed Issues](https://scikit-learn.org/stable/developers/contributing.html#stalled-unclaimed-issues)
    ,
    
*   complete all sections of the issue or pull request template provided by GitHub, including a clear description of the issue or motivation and thought process behind the pull request
    
*   ensure the title clearly describes the issue or pull request and does not include an issue number.
    

For your pull requests specifically, the following will make it easier to review:

*   ensure your PR addresses an issue for which there is clear consensus on the solution (see [Issues tagged “Needs Triage”](https://scikit-learn.org/stable/developers/contributing.html#issues-tagged-needs-triage)
    ),
    
*   ensure the PR satisfies all items in the [Pull request checklist](https://scikit-learn.org/stable/developers/contributing.html#pr-checklist)
    ,
    
*   ensure the changes are minimal and directly relevant to the described issue.
    

### [What does the “spam” label for issues or pull requests mean?](https://scikit-learn.org/stable/faq.html#id21)
[#](https://scikit-learn.org/stable/faq.html#what-does-the-spam-label-for-issues-or-pull-requests-mean "Link to this heading")

The “spam” label is an indication for reviewers that the issue or pull request may not have received sufficient effort or preparation from the author for a productive review. The maintainers are using this label as a way to deal with the increase of low value PRs and issues.

If an issue or PR was labeled as spam and simultaneously closed, the decision is final. A common reason for this happening is when people open a PR for an issue that is still under discussion. Please wait for the discussion to converge before opening a PR.

If your issue or PR was labeled as spam and not closed, see [How do I improve my issue or pull request?](https://scikit-learn.org/stable/faq.html#improve-issue-pr)
 for tips on improving your issue or pull request and increasing the likelihood of the label being removed.

### [What are the inclusion criteria for new algorithms?](https://scikit-learn.org/stable/faq.html#id22)
[#](https://scikit-learn.org/stable/faq.html#what-are-the-inclusion-criteria-for-new-algorithms "Link to this heading")

We only consider well-established algorithms for inclusion. A rule of thumb is at least 3 years since publication, 200+ citations, and wide use and usefulness. A technique that provides a clear-cut improvement (e.g. an enhanced data structure or a more efficient approximation technique) on a widely-used method will also be considered for inclusion.

From the algorithms or techniques that meet the above criteria, only those which fit well within the current API of scikit-learn, that is a `fit`, `predict/transform` interface and ordinarily having input/output that is a numpy array or sparse matrix, are accepted.

The contributor should support the importance of the proposed addition with research papers and/or implementations in other similar packages, demonstrate its usefulness via common use-cases/applications and corroborate performance improvements, if any, with benchmarks and/or plots. It is expected that the proposed algorithm should outperform the methods that are already implemented in scikit-learn at least in some areas.

Please do not propose algorithms you (your best friend, colleague or boss) created. scikit-learn is not a good venue for advertising your own work.

Inclusion of a new algorithm speeding up an existing model is easier if:

*   it does not introduce new hyper-parameters (as it makes the library more future-proof),
    
*   it is easy to document clearly when the contribution improves the speed and when it does not, for instance, “when `n_features >> n_samples`”,
    
*   benchmarks clearly show a speed up.
    

Also, note that your implementation need not be in scikit-learn to be used together with scikit-learn tools. You can implement your favorite algorithm in a scikit-learn compatible way, upload it to GitHub and let us know. We will be happy to list it under [Related Projects](https://scikit-learn.org/stable/related_projects.html#related-projects)
. If you already have a package on GitHub following the scikit-learn API, you may also be interested to look at [scikit-learn-contrib](https://scikit-learn-contrib.github.io/)
.

### [Why are you so selective on what algorithms you include in scikit-learn?](https://scikit-learn.org/stable/faq.html#id23)
[#](https://scikit-learn.org/stable/faq.html#why-are-you-so-selective-on-what-algorithms-you-include-in-scikit-learn "Link to this heading")

Code comes with maintenance cost, and we need to balance the amount of code we have with the size of the team (and add to this the fact that complexity scales non linearly with the number of features). The package relies on core developers using their free time to fix bugs, maintain code and review contributions. Any algorithm that is added needs future attention by the developers, at which point the original author might long have lost interest. See also [What are the inclusion criteria for new algorithms?](https://scikit-learn.org/stable/faq.html#new-algorithms-inclusion-criteria)
. For a great read about long-term maintenance issues in open-source software, look at [the Executive Summary of Roads and Bridges](https://www.fordfoundation.org/media/2976/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure.pdf#page=8)
.

[Using scikit-learn](https://scikit-learn.org/stable/faq.html#id24)
[#](https://scikit-learn.org/stable/faq.html#using-scikit-learn "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

### [How do I get started with scikit-learn?](https://scikit-learn.org/stable/faq.html#id25)
[#](https://scikit-learn.org/stable/faq.html#how-do-i-get-started-with-scikit-learn "Link to this heading")

If you are new to scikit-learn, or looking to strengthen your understanding, we highly recommend the **scikit-learn MOOC (Massive Open Online Course)**.

See our [External Resources, Videos and Talks page](https://scikit-learn.org/stable/presentations.html#external-resources)
 for more details.

### [What’s the best way to get help on scikit-learn usage?](https://scikit-learn.org/stable/faq.html#id26)
[#](https://scikit-learn.org/stable/faq.html#what-s-the-best-way-to-get-help-on-scikit-learn-usage "Link to this heading")

*   General machine learning questions: use [Cross Validated](https://stats.stackexchange.com/)
     with the `[machine-learning]` tag.
    
*   scikit-learn usage questions: use [Stack Overflow](https://stackoverflow.com/questions/tagged/scikit-learn)
     with the `[scikit-learn]` and `[python]` tags. You can alternatively use the [mailing list](https://mail.python.org/mailman/listinfo/scikit-learn)
    .
    

Please make sure to include a minimal reproduction code snippet (ideally shorter than 10 lines) that highlights your problem on a toy dataset (for instance from [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
 or randomly generated with functions of `numpy.random` with a fixed random seed). Please remove any line of code that is not necessary to reproduce your problem.

The problem should be reproducible by simply copy-pasting your code snippet in a Python shell with scikit-learn installed. Do not forget to include the import statements. More guidance to write good reproduction code snippets can be found at: [https://stackoverflow.com/help/mcve](https://stackoverflow.com/help/mcve)
.

If your problem raises an exception that you do not understand (even after googling it), please make sure to include the full traceback that you obtain when running the reproduction script.

For bug reports or feature requests, please make use of the [issue tracker on GitHub](https://github.com/scikit-learn/scikit-learn/issues)
.

Warning

Please do not email any authors directly to ask for assistance, report bugs, or for any other issue related to scikit-learn.

### [How should I save, export or deploy estimators for production?](https://scikit-learn.org/stable/faq.html#id27)
[#](https://scikit-learn.org/stable/faq.html#how-should-i-save-export-or-deploy-estimators-for-production "Link to this heading")

See [Model persistence](https://scikit-learn.org/stable/model_persistence.html#model-persistence)
.

### [How can I create a bunch object?](https://scikit-learn.org/stable/faq.html#id28)
[#](https://scikit-learn.org/stable/faq.html#how-can-i-create-a-bunch-object "Link to this heading")

Bunch objects are sometimes used as an output for functions and methods. They extend dictionaries by enabling values to be accessed by key, `bunch["value_key"]`, or by an attribute, `bunch.value_key`.

They should not be used as an input. Therefore you almost never need to create a [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 object, unless you are extending scikit-learn’s API.

### [How can I load my own datasets into a format usable by scikit-learn?](https://scikit-learn.org/stable/faq.html#id29)
[#](https://scikit-learn.org/stable/faq.html#how-can-i-load-my-own-datasets-into-a-format-usable-by-scikit-learn "Link to this heading")

Generally, scikit-learn works on any numeric data stored as numpy arrays or scipy sparse matrices. Other types that are convertible to numeric arrays such as [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v3.0.5)")
 are also acceptable.

For more information on loading your data files into these usable data structures, please refer to [loading external datasets](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#external-datasets)
.

### [How do I deal with string data (or trees, graphs…)?](https://scikit-learn.org/stable/faq.html#id30)
[#](https://scikit-learn.org/stable/faq.html#how-do-i-deal-with-string-data-or-trees-graphs "Link to this heading")

scikit-learn estimators assume you’ll feed them real-valued feature vectors. This assumption is hard-coded in pretty much all of the library. However, you can feed non-numerical inputs to estimators in several ways.

If you have text documents, you can use a term frequency features; see [Text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
 for the built-in _text vectorizers_. For more general feature extraction from any kind of data, see [Loading features from dicts](https://scikit-learn.org/stable/modules/feature_extraction.html#dict-feature-extraction)
 and [Feature hashing](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-hashing)
.

Another common case is when you have non-numerical data and a custom distance (or similarity) metric on these data. Examples include strings with edit distance (aka. Levenshtein distance), for instance, DNA or RNA sequences. These can be encoded as numbers, but doing so is painful and error-prone. Working with distance metrics on arbitrary data can be done in two ways.

Firstly, many estimators take precomputed distance/similarity matrices, so if the dataset is not too large, you can compute distances for all pairs of inputs. If the dataset is large, you can use feature vectors with only one “feature”, which is an index into a separate data structure, and supply a custom metric function that looks up the actual data in this data structure. For instance, to use [`dbscan`](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "sklearn.cluster.dbscan")
 with Levenshtein distances:

\>>> import numpy as np
\>>> from leven import levenshtein
\>>> from sklearn.cluster import dbscan
\>>> data \= \["ACCTCCTAGAAG", "ACCTACTAGAAGTT", "GAATATTAGGCCGA"\]
\>>> def lev\_metric(x, y):
...     i, j \= int(x\[0\]), int(y\[0\])  \# extract indices
...     return levenshtein(data\[i\], data\[j\])
...
\>>> X \= np.arange(len(data)).reshape(\-1, 1)
\>>> X
array(\[\[0\],\
       \[1\],\
       \[2\]\])
\>>> \# We need to specify algorithm='brute' as the default assumes
\>>> \# a continuous feature space.
\>>> dbscan(X, metric\=lev\_metric, eps\=5, min\_samples\=2, algorithm\='brute')
(array(\[0, 1\]), array(\[ 0,  0, -1\]))

Copy to clipboard

Note that the example above uses the third-party edit distance package [leven](https://pypi.org/project/leven/)
. Similar tricks can be used, with some care, for tree kernels, graph kernels, etc.

### [Why do I sometimes get a crash/freeze with `n_jobs > 1` under OSX or Linux?](https://scikit-learn.org/stable/faq.html#id31)
[#](https://scikit-learn.org/stable/faq.html#why-do-i-sometimes-get-a-crash-freeze-with-n-jobs-1-under-osx-or-linux "Link to this heading")

Several scikit-learn tools such as [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 and [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
 rely internally on Python’s [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.14)")
 module to parallelize execution onto several Python processes by passing `n_jobs > 1` as an argument.

The problem is that Python [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.14)")
 does a `fork` system call without following it with an `exec` system call for performance reasons. Many libraries like (some versions of) Accelerate or vecLib under OSX, (some versions of) MKL, the OpenMP runtime of GCC, nvidia’s Cuda (and probably many others), manage their own internal thread pool. Upon a call to `fork`, the thread pool state in the child process is corrupted: the thread pool believes it has many threads while only the main thread state has been forked. It is possible to change the libraries to make them detect when a fork happens and reinitialize the thread pool in that case: we did that for OpenBLAS (merged upstream in main since 0.2.10) and we contributed a [patch](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=60035)
 to GCC’s OpenMP runtime (not yet reviewed).

But in the end the real culprit is Python’s [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.14)")
 that does `fork` without `exec` to reduce the overhead of starting and using new Python processes for parallel computing. Unfortunately this is a violation of the POSIX standard and therefore some software editors like Apple refuse to consider the lack of fork-safety in Accelerate and vecLib as a bug.

In Python 3.4+ it is now possible to configure [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.14)")
 to use the `"forkserver"` or `"spawn"` start methods (instead of the default `"fork"`) to manage the process pools. To work around this issue when using scikit-learn, you can set the `JOBLIB_START_METHOD` environment variable to `"forkserver"`. However the user should be aware that using the `"forkserver"` method prevents [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
 to call function interactively defined in a shell session.

If you have custom code that uses [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.14)")
 directly instead of using it via [`joblib`](https://joblib.readthedocs.io/en/latest/index.html#module-joblib "(in joblib v1.7)")
 you can enable the `"forkserver"` mode globally for your program. Insert the following instructions in your main script:

import multiprocessing

\# other imports, custom code, load data, define model...

if \_\_name\_\_ \== "\_\_main\_\_":
    multiprocessing.set\_start\_method("forkserver")

    \# call scikit-learn utils with n\_jobs > 1 here

Copy to clipboard

You can find more details on the new start methods in the [multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods)
.

### [Why does my job use more cores than specified with `n_jobs`?](https://scikit-learn.org/stable/faq.html#id32)
[#](https://scikit-learn.org/stable/faq.html#why-does-my-job-use-more-cores-than-specified-with-n-jobs "Link to this heading")

This is because `n_jobs` only controls the number of jobs for routines that are parallelized with [`joblib`](https://joblib.readthedocs.io/en/latest/index.html#module-joblib "(in joblib v1.7)")
, but parallel code can come from other sources:

*   some routines may be parallelized with OpenMP (for code written in C or Cython),
    
*   scikit-learn relies a lot on numpy, which in turn may rely on numerical libraries like MKL, OpenBLAS or BLIS which can provide parallel implementations.
    

For more details, please refer to our [notes on parallelism](https://scikit-learn.org/stable/computing/parallelism.html#parallelism)
.

### [How do I set a `random_state` for an entire execution?](https://scikit-learn.org/stable/faq.html#id33)
[#](https://scikit-learn.org/stable/faq.html#how-do-i-set-a-random-state-for-an-entire-execution "Link to this heading")

Please refer to [Controlling randomness](https://scikit-learn.org/stable/common_pitfalls.html#randomness)
.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)