[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_face_recognition.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_face_recognition.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_face_recognition.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_face_recognition.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_face_recognition.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_face_recognition.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#sphx-glr-download-auto-examples-applications-plot-face-recognition-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Faces recognition example using eigenfaces and kernel approximation[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#faces-recognition-example-using-eigenfaces-and-kernel-approximation "Link to this heading")

=========================================================================================================================================================================================================================================================

This example builds a classical face recognition pipeline on the “Labeled Faces in the Wild” (LFW) dataset, a preprocessed excerpt of which is available here: [https://www.kaggle.com/datasets/jessicali9530/lfw-dataset](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)

We reduce the dimensionality of the face images with PCA (the eigenfaces), then approximate the RBF kernel with [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
 and train a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 on the resulting features. The full chain is wrapped in a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 so that cross-validation does not leak information from the test set. The hyperparameters are tuned with a successive halving search ([`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
) that minimizes the log loss. We finally evaluate the model both quantitatively, with a classification report and one-vs-rest ROC and precision-recall curves, and qualitatively, by displaying the predictions and the eigenfaces.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Loading the dataset[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#loading-the-dataset "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

We download the Labeled Faces in the Wild (LFW) dataset and load it as numpy arrays. Each sample is a flattened grayscale image; the target is the identity of the person pictured.

from sklearn.datasets import [fetch\_lfw\_people](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "sklearn.datasets.fetch_lfw_people")

lfw\_people \= [fetch\_lfw\_people](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "sklearn.datasets.fetch_lfw_people")
(min\_faces\_per\_person\=70, resize\=0.4)

\# Introspect the image arrays to find the shapes (for plotting).
n\_samples, height, width \= lfw\_people.images.shape

\# For machine learning we use the data directly (relative pixel positions are
\# ignored by this model).
X \= lfw\_people.data
n\_features \= X.shape\[1\]

\# The label to predict is the id of the person.
y \= lfw\_people.target
target\_names \= lfw\_people.target\_names
n\_classes \= target\_names.shape\[0\]

Copy to clipboard

print("Total dataset size:")
print(f"n\_samples: {n\_samples}")
print(f"n\_features: {n\_features}")
print(f"n\_classes: {n\_classes}")

Copy to clipboard

Total dataset size:
n\_samples: 1288
n\_features: 1850
n\_classes: 7

Copy to clipboard

Splitting the dataset[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#splitting-the-dataset "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

We hold out 25% of the data for testing. Preprocessing and model fitting are chained in a pipeline below so that scaling and feature extraction are learned only from the training folds during cross-validation.

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.25, random\_state\=42
)

Copy to clipboard

Building the model pipeline[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#building-the-model-pipeline "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We chain preprocessing and classification in a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
. PCA extracts eigenfaces as a compact representation; [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
 approximates the RBF feature map so that a linear [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 can model non-linear decision boundaries while scaling better than a kernel SVM. Because logistic regression outputs calibrated probabilities, we can tune the model by minimizing the log loss.

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.kernel\_approximation import [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

n\_components \= 150

model \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    steps\=\[\
        ("scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()),\
        ("pca", [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
(n\_components\=n\_components, svd\_solver\="randomized", whiten\=True)),\
        ("nystroem", [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")\
(random\_state\=42)),\
        ("logreg", [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(max\_iter\=5\_000)),\
    \]
)
model

Copy to clipboard

Pipeline(steps=\[('scaler', StandardScaler()),\
                ('pca',\
                 PCA(n\_components=150, svd\_solver='randomized', whiten=True)),\
                ('nystroem', Nystroem(random\_state=42)),\
                ('logreg', LogisticRegression(max\_iter=5000))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('scaler', ...), ('pca', ...), ...\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |

PCA

[?Documentation for PCA](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_components n\_components: int, float or 'mle', default=None  <br>  <br>Number of components to keep.  <br>if n\_components is not set all components are kept::  <br>  <br>n\_components == min(n\_samples, n\_features)  <br>  <br>If \`\`n\_components == 'mle'\`\` and \`\`svd\_solver == 'full'\`\`, Minka's  <br>MLE is used to guess the dimension. Use of \`\`n\_components == 'mle'\`\`  <br>will interpret \`\`svd\_solver == 'auto'\`\` as \`\`svd\_solver == 'full'\`\`.  <br>  <br>If \`\`0 < n\_components < 1\`\` and \`\`svd\_solver == 'full'\`\`, select the  <br>number of components such that the amount of variance that needs to be  <br>explained is greater than the percentage specified by n\_components.  <br>  <br>If \`\`svd\_solver == 'arpack'\`\`, the number of components must be  <br>strictly less than the minimum of n\_features and n\_samples.  <br>  <br>Hence, the None case results in::  <br>  <br>n\_components == min(n\_samples, n\_features) - 1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_components,-int%2C%20float%20or%20%27mle%27%2C%20default%3DNone) | 150 |
|     | [whiten whiten: bool, default=False  <br>  <br>When True (False by default) the \`components\_\` vectors are multiplied  <br>by the square root of n\_samples and then divided by the singular values  <br>to ensure uncorrelated outputs with unit component-wise variances.  <br>  <br>Whitening will remove some information from the transformed signal  <br>(the relative variance scales of the components) but can sometime  <br>improve the predictive accuracy of the downstream estimators by  <br>making their data respect some hard-wired assumptions.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=whiten,-bool%2C%20default%3DFalse) | True |
|     | [svd\_solver svd\_solver: {'auto', 'full', 'covariance\_eigh', 'arpack', 'randomized'}, default='auto'  <br>  <br>"auto" :  <br>The solver is selected by a default 'auto' policy is based on \`X.shape\` and  <br>\`n\_components\`: if the input data has fewer than 1000 features and  <br>more than 10 times as many samples, then the "covariance\_eigh"  <br>solver is used. Otherwise, if the input data is larger than 500x500  <br>and the number of components to extract is lower than 80% of the  <br>smallest dimension of the data, then the more efficient  <br>"randomized" method is selected. Otherwise the exact "full" SVD is  <br>computed and optionally truncated afterwards.  <br>"full" :  <br>Run exact full SVD calling the standard LAPACK solver via  <br>\`scipy.linalg.svd\` and select the components by postprocessing  <br>"covariance\_eigh" :  <br>Precompute the covariance matrix (on centered data), run a  <br>classical eigenvalue decomposition on the covariance matrix  <br>typically using LAPACK and select the components by postprocessing.  <br>This solver is very efficient for n\_samples >> n\_features and small  <br>n\_features. It is, however, not tractable otherwise for large  <br>n\_features (large memory footprint required to materialize the  <br>covariance matrix). Also note that compared to the "full" solver,  <br>this solver effectively doubles the condition number and is  <br>therefore less numerical stable (e.g. on input data with a large  <br>range of singular values).  <br>"arpack" :  <br>Run SVD truncated to \`n\_components\` calling ARPACK solver via  <br>\`scipy.sparse.linalg.svds\`. It requires strictly  <br>\`0 < n\_components < min(X.shape)\`  <br>"randomized" :  <br>Run randomized SVD by the method of Halko et al.  <br>  <br>.. versionadded:: 0.18.0  <br>  <br>.. versionchanged:: 1.5  <br>Added the 'covariance\_eigh' solver.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=svd_solver,-%7B%27auto%27%2C%20%27full%27%2C%20%27covariance_eigh%27%2C%20%27arpack%27%2C%20%27randomized%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27auto%27) | 'randomized' |
|     | [copy copy: bool, default=True  <br>  <br>If False, data passed to fit are overwritten and running  <br>fit(X).transform(X) will not yield the expected results,  <br>use fit\_transform(X) instead.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [tol tol: float, default=0.0  <br>  <br>Tolerance for singular values computed by svd\_solver == 'arpack'.  <br>Must be of range \[0.0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=tol,-float%2C%20default%3D0.0) | 0.0 |\
|     | [iterated\_power iterated\_power: int or 'auto', default='auto'  <br>  <br>Number of iterations for the power method computed by  <br>svd\_solver == 'randomized'.  <br>Must be of range \[0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=iterated_power,-int%20or%20%27auto%27%2C%20default%3D%27auto%27) | 'auto' |\
|     | [n\_oversamples n\_oversamples: int, default=10  <br>  <br>This parameter is only relevant when \`svd\_solver="randomized"\`.  <br>It corresponds to the additional number of random vectors to sample the  <br>range of \`X\` so as to ensure proper conditioning. See  <br>:func:\`~sklearn.utils.extmath.randomized\_svd\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_oversamples,-int%2C%20default%3D10) | 10  |\
|     | [power\_iteration\_normalizer power\_iteration\_normalizer: {'auto', 'QR', 'LU', 'none'}, default='auto'  <br>  <br>Power iteration normalizer for randomized SVD solver.  <br>Not used by ARPACK. See :func:\`~sklearn.utils.extmath.randomized\_svd\`  <br>for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=power_iteration_normalizer,-%7B%27auto%27%2C%20%27QR%27%2C%20%27LU%27%2C%20%27none%27%7D%2C%20default%3D%27auto%27) | 'auto' |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Used when the 'arpack' or 'randomized' solvers are used. Pass an int  <br>for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |\
\
Nystroem\
\
[?Documentation for Nystroem](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the uniform sampling without  <br>replacement of \`n\_components\` of the training data to construct the  <br>basis kernel.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 42  |\
|     | [kernel kernel: str or callable, default='rbf'  <br>  <br>Kernel map to be approximated. A callable should accept two arguments  <br>and the keyword arguments passed to this object as \`kernel\_params\`, and  <br>should return a floating point number.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel,-str%20or%20callable%2C%20default%3D%27rbf%27) | 'rbf' |\
|     | [gamma gamma: float, default=None  <br>  <br>Gamma parameter for the RBF, laplacian, polynomial, exponential chi2  <br>and sigmoid kernels. Interpretation of the default value is left to  <br>the kernel; see the documentation for sklearn.metrics.pairwise.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=gamma,-float%2C%20default%3DNone) | None |\
|     | [coef0 coef0: float, default=None  <br>  <br>Zero coefficient for polynomial and sigmoid kernels.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=coef0,-float%2C%20default%3DNone) | None |\
|     | [degree degree: float, default=None  <br>  <br>Degree of the polynomial kernel. Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=degree,-float%2C%20default%3DNone) | None |\
|     | [kernel\_params kernel\_params: dict, default=None  <br>  <br>Additional parameters (keyword arguments) for kernel function passed  <br>as callable object.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel_params,-dict%2C%20default%3DNone) | None |\
|     | [n\_components n\_components: int, default=100  <br>  <br>Number of features to construct.  <br>How many data points will be used to construct the mapping.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_components,-int%2C%20default%3D100) | 100 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to use for the computation. This works by breaking  <br>down the kernel matrix into \`n\_jobs\` even slices and computing them in  <br>parallel.  <br>  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 5000 |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |\
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |\
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
  \
  \
\
Tuning the pipeline with successive halving[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#tuning-the-pipeline-with-successive-halving "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We tune the `gamma` and `n_components` of the Nystroem approximation and the `C` regularization of the logistic regression with a successive halving search ([`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")\
). The search minimizes the log loss (`neg_log_loss`) and screens many candidates on small training subsets before investing compute in the most promising ones. We set `min_resources` high enough so that PCA can always extract 150 eigenfaces, even in the first halving iteration.\
\
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")\
\
from scipy.stats import [loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform")\
, [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint")\
\
from sklearn.experimental import enable\_halving\_search\_cv  \# noqa: F401\
from sklearn.model\_selection import [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")\
\
print("Fitting the classifier to the training set")\
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")\
()\
param\_distributions \= {\
    "nystroem\_\_gamma": [loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform")\
(1e-4, 1e-1),\
    "nystroem\_\_n\_components": [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint")\
(50, 200),\
    "logreg\_\_C": [loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform")\
(1e-2, 1e2),\
}\
clf \= [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")\
(\
    model,\
    param\_distributions,\
    n\_candidates\=30,\
    factor\=3,\
    min\_resources\=300,\
    scoring\="neg\_log\_loss",\
    random\_state\=42,\
)\
clf \= clf.fit(X\_train, y\_train)\
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")\
() \- t0:.3f}s")\
\
Copy to clipboard\
\
Fitting the classifier to the training set\
done in 16.830s\
\
Copy to clipboard\
\
print("Best estimator found by successive halving search:")\
clf.best\_estimator\_\
\
Copy to clipboard\
\
Best estimator found by successive halving search:\
\
Copy to clipboard\
\
Pipeline(steps=\[('scaler', StandardScaler()),\
                ('pca',\
                 PCA(n\_components=150, svd\_solver='randomized', whiten=True)),\
                ('nystroem',\
                 Nystroem(gamma=np.float64(0.0011756010900231862),\
                          n\_components=173, random\_state=42)),\
                ('logreg',\
                 LogisticRegression(C=np.float64(20.651425578959262),\
                                    max\_iter=5000))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('scaler', ...), ('pca', ...), ...\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](7,) | \[0,1,2,...,4,5,6\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 1850 |\
\
StandardScaler\
\
[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |\
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](1850,) | \[0.36,0.38,0.41,...,0.47,0.44,0.41\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 1850 |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 966 |\
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](1850,) | \[0.18,0.18,0.17,...,0.31,0.31,0.31\] |\
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](1850,) | \[0.03,0.03,0.03,...,0.09,0.09,0.09\] |\
\
100 of 1,850 features\
\
|     |\
| --- |\
| x0  |\
| x1  |\
| x2  |\
| x3  |\
| x4  |\
| x5  |\
| x6  |\
| x7  |\
| x8  |\
| x9  |\
| x10 |\
| x11 |\
| x12 |\
| x13 |\
| x14 |\
| x15 |\
| x16 |\
| x17 |\
| x18 |\
| x19 |\
| x20 |\
| x21 |\
| x22 |\
| x23 |\
| x24 |\
| x25 |\
| x26 |\
| x27 |\
| x28 |\
| x29 |\
| x30 |\
| x31 |\
| x32 |\
| x33 |\
| x34 |\
| x35 |\
| x36 |\
| x37 |\
| x38 |\
| x39 |\
| x40 |\
| x41 |\
| x42 |\
| x43 |\
| x44 |\
| x45 |\
| x46 |\
| x47 |\
| x48 |\
| x49 |\
| x50 |\
| x51 |\
| x52 |\
| x53 |\
| x54 |\
| x55 |\
| x56 |\
| x57 |\
| x58 |\
| x59 |\
| x60 |\
| x61 |\
| x62 |\
| x63 |\
| x64 |\
| x65 |\
| x66 |\
| x67 |\
| x68 |\
| x69 |\
| x70 |\
| x71 |\
| x72 |\
| x73 |\
| x74 |\
| x75 |\
| x76 |\
| x77 |\
| x78 |\
| x79 |\
| x80 |\
| x81 |\
| x82 |\
| x83 |\
| x84 |\
| x85 |\
| x86 |\
| x87 |\
| x88 |\
| x89 |\
| x90 |\
| x91 |\
| x92 |\
| x93 |\
| x94 |\
| x95 |\
| x96 |\
| x97 |\
| x98 |\
| x99 |\
\
PCA\
\
[?Documentation for PCA](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_components n\_components: int, float or 'mle', default=None  <br>  <br>Number of components to keep.  <br>if n\_components is not set all components are kept::  <br>  <br>n\_components == min(n\_samples, n\_features)  <br>  <br>If \`\`n\_components == 'mle'\`\` and \`\`svd\_solver == 'full'\`\`, Minka's  <br>MLE is used to guess the dimension. Use of \`\`n\_components == 'mle'\`\`  <br>will interpret \`\`svd\_solver == 'auto'\`\` as \`\`svd\_solver == 'full'\`\`.  <br>  <br>If \`\`0 < n\_components < 1\`\` and \`\`svd\_solver == 'full'\`\`, select the  <br>number of components such that the amount of variance that needs to be  <br>explained is greater than the percentage specified by n\_components.  <br>  <br>If \`\`svd\_solver == 'arpack'\`\`, the number of components must be  <br>strictly less than the minimum of n\_features and n\_samples.  <br>  <br>Hence, the None case results in::  <br>  <br>n\_components == min(n\_samples, n\_features) - 1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_components,-int%2C%20float%20or%20%27mle%27%2C%20default%3DNone) | 150 |\
|     | [whiten whiten: bool, default=False  <br>  <br>When True (False by default) the \`components\_\` vectors are multiplied  <br>by the square root of n\_samples and then divided by the singular values  <br>to ensure uncorrelated outputs with unit component-wise variances.  <br>  <br>Whitening will remove some information from the transformed signal  <br>(the relative variance scales of the components) but can sometime  <br>improve the predictive accuracy of the downstream estimators by  <br>making their data respect some hard-wired assumptions.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=whiten,-bool%2C%20default%3DFalse) | True |\
|     | [svd\_solver svd\_solver: {'auto', 'full', 'covariance\_eigh', 'arpack', 'randomized'}, default='auto'  <br>  <br>"auto" :  <br>The solver is selected by a default 'auto' policy is based on \`X.shape\` and  <br>\`n\_components\`: if the input data has fewer than 1000 features and  <br>more than 10 times as many samples, then the "covariance\_eigh"  <br>solver is used. Otherwise, if the input data is larger than 500x500  <br>and the number of components to extract is lower than 80% of the  <br>smallest dimension of the data, then the more efficient  <br>"randomized" method is selected. Otherwise the exact "full" SVD is  <br>computed and optionally truncated afterwards.  <br>"full" :  <br>Run exact full SVD calling the standard LAPACK solver via  <br>\`scipy.linalg.svd\` and select the components by postprocessing  <br>"covariance\_eigh" :  <br>Precompute the covariance matrix (on centered data), run a  <br>classical eigenvalue decomposition on the covariance matrix  <br>typically using LAPACK and select the components by postprocessing.  <br>This solver is very efficient for n\_samples >> n\_features and small  <br>n\_features. It is, however, not tractable otherwise for large  <br>n\_features (large memory footprint required to materialize the  <br>covariance matrix). Also note that compared to the "full" solver,  <br>this solver effectively doubles the condition number and is  <br>therefore less numerical stable (e.g. on input data with a large  <br>range of singular values).  <br>"arpack" :  <br>Run SVD truncated to \`n\_components\` calling ARPACK solver via  <br>\`scipy.sparse.linalg.svds\`. It requires strictly  <br>\`0 < n\_components < min(X.shape)\`  <br>"randomized" :  <br>Run randomized SVD by the method of Halko et al.  <br>  <br>.. versionadded:: 0.18.0  <br>  <br>.. versionchanged:: 1.5  <br>Added the 'covariance\_eigh' solver.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=svd_solver,-%7B%27auto%27%2C%20%27full%27%2C%20%27covariance_eigh%27%2C%20%27arpack%27%2C%20%27randomized%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27auto%27) | 'randomized' |\
|     | [copy copy: bool, default=True  <br>  <br>If False, data passed to fit are overwritten and running  <br>fit(X).transform(X) will not yield the expected results,  <br>use fit\_transform(X) instead.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [tol tol: float, default=0.0  <br>  <br>Tolerance for singular values computed by svd\_solver == 'arpack'.  <br>Must be of range \[0.0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=tol,-float%2C%20default%3D0.0) | 0.0 |\
|     | [iterated\_power iterated\_power: int or 'auto', default='auto'  <br>  <br>Number of iterations for the power method computed by  <br>svd\_solver == 'randomized'.  <br>Must be of range \[0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=iterated_power,-int%20or%20%27auto%27%2C%20default%3D%27auto%27) | 'auto' |\
|     | [n\_oversamples n\_oversamples: int, default=10  <br>  <br>This parameter is only relevant when \`svd\_solver="randomized"\`.  <br>It corresponds to the additional number of random vectors to sample the  <br>range of \`X\` so as to ensure proper conditioning. See  <br>:func:\`~sklearn.utils.extmath.randomized\_svd\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_oversamples,-int%2C%20default%3D10) | 10  |\
|     | [power\_iteration\_normalizer power\_iteration\_normalizer: {'auto', 'QR', 'LU', 'none'}, default='auto'  <br>  <br>Power iteration normalizer for randomized SVD solver.  <br>Not used by ARPACK. See :func:\`~sklearn.utils.extmath.randomized\_svd\`  <br>for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=power_iteration_normalizer,-%7B%27auto%27%2C%20%27QR%27%2C%20%27LU%27%2C%20%27none%27%7D%2C%20default%3D%27auto%27) | 'auto' |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Used when the 'arpack' or 'randomized' solvers are used. Pass an int  <br>for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [components\_ components\_: ndarray of shape (n\_components, n\_features)  <br>  <br>Principal axes in feature space, representing the directions of  <br>maximum variance in the data. Equivalently, the right singular  <br>vectors of the centered input data, parallel to its eigenvectors.  <br>The components are sorted by decreasing \`\`explained\_variance\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=components_,-ndarray%20of%20shape%20%28n_components%2C%20n_features%29) | ndarray\[float32\](150, 1850) | \[\[ 0.01, 0.01, 0.01,..., 0.01, 0.01, 0.01\], \[ 0.02, 0.02, 0.02,...,-0.01,-0.01,-0.01\], \[ 0.03, 0.03, 0.03,..., 0. , 0. , 0. \], ..., \[ 0.03, 0.03, 0.03,..., 0.04,-0. ,-0.05\], \[ 0.06, 0.03,-0.02,...,-0.01, 0.01, 0.03\], \[-0.03,-0.01, 0.02,...,-0.01,-0. , 0. \]\] |\
| [explained\_variance\_ explained\_variance\_: ndarray of shape (n\_components,)  <br>  <br>The amount of variance explained by each of the selected components.  <br>The variance estimation uses \`n\_samples - 1\` degrees of freedom.  <br>  <br>Equal to n\_components largest eigenvalues  <br>of the covariance matrix of X.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=explained_variance_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float32\](150,) | \[482.04,267.97,127.02,..., 0.82, 0.82, 0.81\] |\
| [explained\_variance\_ratio\_ explained\_variance\_ratio\_: ndarray of shape (n\_components,)  <br>  <br>Percentage of variance explained by each of the selected components.  <br>  <br>If \`\`n\_components\`\` is not set then all components are stored and the  <br>sum of the ratios is equal to 1.0.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=explained_variance_ratio_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float32\](150,) | \[0.26,0.14,0.07,...,0. ,0. ,0. \] |\
| [mean\_ mean\_: ndarray of shape (n\_features,)  <br>  <br>Per-feature empirical mean, estimated from the training set.  <br>  <br>Equal to \`X.mean(axis=0)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float32\](1850,) | \[-0., 0.,-0.,...,-0.,-0.,-0.\] |\
| [n\_components\_ n\_components\_: int  <br>  <br>The estimated number of components. When n\_components is set  <br>to 'mle' or a number between 0 and 1 (with svd\_solver == 'full') this  <br>number is estimated from input data. Otherwise it equals the parameter  <br>n\_components, or the lesser value of n\_features and n\_samples  <br>if n\_components is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_components_,-int) | int | 150 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_features_in_,-int) | int | 1850 |\
| [n\_samples\_ n\_samples\_: int  <br>  <br>Number of samples in the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_samples_,-int) | int | 966 |\
| [noise\_variance\_ noise\_variance\_: float  <br>  <br>The estimated noise covariance following the Probabilistic PCA model  <br>from Tipping and Bishop 1999. See "Pattern Recognition and  <br>Machine Learning" by C. Bishop, 12.2.1 p. 574 or  <br>http://www.miketipping.com/papers/met-mppca.pdf. It is required to  <br>compute the estimated data covariance and score samples.  <br>  <br>Equal to the average of (min(n\_features, n\_samples) - n\_components)  <br>smallest eigenvalues of the covariance matrix of X.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=noise_variance_,-float) | float32 | np.float32(0.12381879) |\
| [singular\_values\_ singular\_values\_: ndarray of shape (n\_components,)  <br>  <br>The singular values corresponding to each of the selected components.  <br>The singular values are equal to the 2-norms of the \`\`n\_components\`\`  <br>variables in the lower-dimensional space.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=singular_values_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float32\](150,) | \[682.03,508.52,350.11,..., 28.19, 28.11, 27.89\] |\
\
100 of 150 features\
\
|     |\
| --- |\
| pca0 |\
| pca1 |\
| pca2 |\
| pca3 |\
| pca4 |\
| pca5 |\
| pca6 |\
| pca7 |\
| pca8 |\
| pca9 |\
| pca10 |\
| pca11 |\
| pca12 |\
| pca13 |\
| pca14 |\
| pca15 |\
| pca16 |\
| pca17 |\
| pca18 |\
| pca19 |\
| pca20 |\
| pca21 |\
| pca22 |\
| pca23 |\
| pca24 |\
| pca25 |\
| pca26 |\
| pca27 |\
| pca28 |\
| pca29 |\
| pca30 |\
| pca31 |\
| pca32 |\
| pca33 |\
| pca34 |\
| pca35 |\
| pca36 |\
| pca37 |\
| pca38 |\
| pca39 |\
| pca40 |\
| pca41 |\
| pca42 |\
| pca43 |\
| pca44 |\
| pca45 |\
| pca46 |\
| pca47 |\
| pca48 |\
| pca49 |\
| pca50 |\
| pca51 |\
| pca52 |\
| pca53 |\
| pca54 |\
| pca55 |\
| pca56 |\
| pca57 |\
| pca58 |\
| pca59 |\
| pca60 |\
| pca61 |\
| pca62 |\
| pca63 |\
| pca64 |\
| pca65 |\
| pca66 |\
| pca67 |\
| pca68 |\
| pca69 |\
| pca70 |\
| pca71 |\
| pca72 |\
| pca73 |\
| pca74 |\
| pca75 |\
| pca76 |\
| pca77 |\
| pca78 |\
| pca79 |\
| pca80 |\
| pca81 |\
| pca82 |\
| pca83 |\
| pca84 |\
| pca85 |\
| pca86 |\
| pca87 |\
| pca88 |\
| pca89 |\
| pca90 |\
| pca91 |\
| pca92 |\
| pca93 |\
| pca94 |\
| pca95 |\
| pca96 |\
| pca97 |\
| pca98 |\
| pca99 |\
\
Nystroem\
\
[?Documentation for Nystroem](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [gamma gamma: float, default=None  <br>  <br>Gamma parameter for the RBF, laplacian, polynomial, exponential chi2  <br>and sigmoid kernels. Interpretation of the default value is left to  <br>the kernel; see the documentation for sklearn.metrics.pairwise.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=gamma,-float%2C%20default%3DNone) | np.float64(0....6010900231862) |\
|     | [n\_components n\_components: int, default=100  <br>  <br>Number of features to construct.  <br>How many data points will be used to construct the mapping.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_components,-int%2C%20default%3D100) | 173 |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the uniform sampling without  <br>replacement of \`n\_components\` of the training data to construct the  <br>basis kernel.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 42  |\
|     | [kernel kernel: str or callable, default='rbf'  <br>  <br>Kernel map to be approximated. A callable should accept two arguments  <br>and the keyword arguments passed to this object as \`kernel\_params\`, and  <br>should return a floating point number.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel,-str%20or%20callable%2C%20default%3D%27rbf%27) | 'rbf' |\
|     | [coef0 coef0: float, default=None  <br>  <br>Zero coefficient for polynomial and sigmoid kernels.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=coef0,-float%2C%20default%3DNone) | None |\
|     | [degree degree: float, default=None  <br>  <br>Degree of the polynomial kernel. Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=degree,-float%2C%20default%3DNone) | None |\
|     | [kernel\_params kernel\_params: dict, default=None  <br>  <br>Additional parameters (keyword arguments) for kernel function passed  <br>as callable object.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel_params,-dict%2C%20default%3DNone) | None |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to use for the computation. This works by breaking  <br>down the kernel matrix into \`n\_jobs\` even slices and computing them in  <br>parallel.  <br>  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [component\_indices\_ component\_indices\_: ndarray of shape (n\_components)  <br>  <br>Indices of \`\`components\_\`\` in the training set.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=component_indices_,-ndarray%20of%20shape%20%28n_components%29) | ndarray\[int64\](173,) | \[244,467,836,..., 65,141,266\] |\
| [components\_ components\_: ndarray of shape (n\_components, n\_features)  <br>  <br>Subset of training points used to construct the feature map.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=components_,-ndarray%20of%20shape%20%28n_components%2C%20n_features%29) | ndarray\[float32\](173, 150) | \[\[ 1.45,-0.18, 0.09,..., 1.9 , 0.87, 0.31\], \[-0.18,-0.9 , 2.32,..., 0.04,-0.16, 0.08\], \[ 1.18,-1.99,-0.16,..., 0.71, 1.93,-0.59\], ..., \[ 1.01, 0.23,-0.32,...,-0.79, 0.48, 0.3 \], \[ 2.09, 0.53,-0.95,..., 0.99, 0.14, 0.23\], \[ 0.28,-0.53, 1.28,..., 1.36,-0.46, 1.92\]\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_features_in_,-int) | int | 150 |\
| [normalization\_ normalization\_: ndarray of shape (n\_components, n\_components)  <br>  <br>Normalization matrix needed for embedding.  <br>Square root of the kernel matrix on \`\`components\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=normalization_,-ndarray%20of%20shape%20%28n_components%2C%20n_components%29) | ndarray\[float32\](173, 173) | \[\[ 2.91, 0.02,-0.11,..., 0.05,-0.15, 0.07\], \[ 0.02, 1.55, 0.02,...,-0.02,-0.01, 0.1 \], \[-0.11, 0.02, 2.4 ,..., 0.16,-0.09,-0.02\], ..., \[ 0.05,-0.02, 0.16,..., 3.14, 0.04,-0.05\], \[-0.15,-0.01,-0.09,..., 0.04, 3.66,-0.13\], \[ 0.07, 0.1 ,-0.02,...,-0.05,-0.13, 2.41\]\] |\
\
100 of 173 features\
\
|     |\
| --- |\
| nystroem0 |\
| nystroem1 |\
| nystroem2 |\
| nystroem3 |\
| nystroem4 |\
| nystroem5 |\
| nystroem6 |\
| nystroem7 |\
| nystroem8 |\
| nystroem9 |\
| nystroem10 |\
| nystroem11 |\
| nystroem12 |\
| nystroem13 |\
| nystroem14 |\
| nystroem15 |\
| nystroem16 |\
| nystroem17 |\
| nystroem18 |\
| nystroem19 |\
| nystroem20 |\
| nystroem21 |\
| nystroem22 |\
| nystroem23 |\
| nystroem24 |\
| nystroem25 |\
| nystroem26 |\
| nystroem27 |\
| nystroem28 |\
| nystroem29 |\
| nystroem30 |\
| nystroem31 |\
| nystroem32 |\
| nystroem33 |\
| nystroem34 |\
| nystroem35 |\
| nystroem36 |\
| nystroem37 |\
| nystroem38 |\
| nystroem39 |\
| nystroem40 |\
| nystroem41 |\
| nystroem42 |\
| nystroem43 |\
| nystroem44 |\
| nystroem45 |\
| nystroem46 |\
| nystroem47 |\
| nystroem48 |\
| nystroem49 |\
| nystroem50 |\
| nystroem51 |\
| nystroem52 |\
| nystroem53 |\
| nystroem54 |\
| nystroem55 |\
| nystroem56 |\
| nystroem57 |\
| nystroem58 |\
| nystroem59 |\
| nystroem60 |\
| nystroem61 |\
| nystroem62 |\
| nystroem63 |\
| nystroem64 |\
| nystroem65 |\
| nystroem66 |\
| nystroem67 |\
| nystroem68 |\
| nystroem69 |\
| nystroem70 |\
| nystroem71 |\
| nystroem72 |\
| nystroem73 |\
| nystroem74 |\
| nystroem75 |\
| nystroem76 |\
| nystroem77 |\
| nystroem78 |\
| nystroem79 |\
| nystroem80 |\
| nystroem81 |\
| nystroem82 |\
| nystroem83 |\
| nystroem84 |\
| nystroem85 |\
| nystroem86 |\
| nystroem87 |\
| nystroem88 |\
| nystroem89 |\
| nystroem90 |\
| nystroem91 |\
| nystroem92 |\
| nystroem93 |\
| nystroem94 |\
| nystroem95 |\
| nystroem96 |\
| nystroem97 |\
| nystroem98 |\
| nystroem99 |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | np.float64(20.651425578959262) |\
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 5000 |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |\
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int64\](7,) | \[0,1,2,...,4,5,6\] |\
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float32\](7, 173) | \[\[-2.98,-1.28,-0.8 ,..., 0.96, 0.96, 1.68\], \[ 1.11, 6.5 ,-2.67,...,-4.26, 3.82, 3.12\], \[ 6.07,-0.07, 6.92,...,-2.59,-2.08, 1.58\], ..., \[ 1.13,-3.01,-0.63,...,-1.13, 0.22, 0.42\], \[-0.79,-0.49,-0.44,..., 5.06,-1.09, 2.73\], \[ 0.31, 2.67,-2.44,...,-2.16, 0.61,-4.76\]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float32\](7,) | \[ 2.18, 1.62,-3.93,...,-0.81, 1.38,-1.14\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 173 |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[72\] |\
\
  \
  \
\
Quantitative evaluation[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#quantitative-evaluation "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We measure the model quality on the held-out test set with a classification report and, since the probabilities are well calibrated, one-vs-rest ROC and precision-recall curves. The pipeline handles preprocessing internally.\
\
import matplotlib.pyplot as plt\
\
from sklearn.metrics import [classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")\
from sklearn.preprocessing import [label\_binarize](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")\
\
print("Predicting people's names on the test set")\
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")\
()\
y\_pred \= clf.predict(X\_test)\
y\_score \= clf.predict\_proba(X\_test)\
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")\
() \- t0:.3f}s")\
\
print([classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")\
(y\_test, y\_pred, target\_names\=target\_names))\
\
Copy to clipboard\
\
Predicting people's names on the test set\
done in 0.011s\
                   precision    recall  f1-score   support\
\
     Ariel Sharon       0.64      0.54      0.58        13\
     Colin Powell       0.79      0.87      0.83        60\
  Donald Rumsfeld       0.77      0.63      0.69        27\
    George W Bush       0.87      0.95      0.91       146\
Gerhard Schroeder       0.68      0.68      0.68        25\
      Hugo Chavez       0.80      0.53      0.64        15\
       Tony Blair       0.90      0.72      0.80        36\
\
         accuracy                           0.83       322\
        macro avg       0.78      0.70      0.73       322\
     weighted avg       0.82      0.83      0.82       322\
\
Copy to clipboard\
\
Because the problem is multiclass, we summarize the ranking quality of the predicted probabilities with one-vs-rest curves: each identity is in turn treated as the positive class against all the others. The ROC curve relates the true positive rate to the false positive rate, while the precision-recall curve is more informative when the positive class is rare, as is the case here where each identity is a small fraction of the test set.\
\
from sklearn.metrics import PrecisionRecallDisplay, RocCurveDisplay\
\
classes \= list(range(n\_classes))\
y\_onehot\_test \= [label\_binarize](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")\
(y\_test, classes\=classes)\
\
fig, (ax\_roc, ax\_pr) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(1, 2, figsize\=(13, 6))\
\
for class\_id, name in enumerate(target\_names):\
    [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")\
(\
        y\_onehot\_test\[:, class\_id\],\
        y\_score\[:, class\_id\],\
        name\=name,\
        ax\=ax\_roc,\
        plot\_chance\_level\=(class\_id \== n\_classes \- 1),\
    )\
    [PrecisionRecallDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")\
(\
        y\_onehot\_test\[:, class\_id\],\
        y\_score\[:, class\_id\],\
        name\=name,\
        ax\=ax\_pr,\
    )\
\
ax\_roc.set\_title("One-vs-rest ROC curves")\
ax\_pr.set\_title("One-vs-rest precision-recall curves")\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![One-vs-rest ROC curves, One-vs-rest precision-recall curves](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_001.png)\
\
Qualitative evaluation[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#qualitative-evaluation "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We visualize a gallery of test portraits with their predicted and true labels to inspect the model’s mistakes at a glance.\
\
def plot\_gallery(images, titles, height, width, n\_row\=3, n\_col\=4):\
    """Plot a gallery of portraits."""\
    fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(n\_row, n\_col, figsize\=(1.8 \* n\_col, 2.4 \* n\_row))\
    fig.subplots\_adjust(bottom\=0, left\=0.01, right\=0.99, top\=0.90, hspace\=0.35)\
    for ax, image, title in zip(axs.ravel(), images, titles):\
        ax.imshow(image.reshape((height, width)), cmap\=plt.cm.gray)\
        ax.set\_title(title, size\=12)\
        ax.set\_xticks(())\
        ax.set\_yticks(())\
    return fig\
\
def make\_title(y\_pred, y\_test, target\_names, i):\
    pred\_name \= target\_names\[y\_pred\[i\]\].rsplit(" ", 1)\[\-1\]\
    true\_name \= target\_names\[y\_test\[i\]\].rsplit(" ", 1)\[\-1\]\
    return f"predicted: {pred\_name}\\ntrue:      {true\_name}"\
\
prediction\_titles \= \[\
    make\_title(y\_pred, y\_test, target\_names, i) for i in range(y\_pred.shape\[0\])\
\]\
\
plot\_gallery(X\_test, prediction\_titles, height, width)\
\
Copy to clipboard\
\
![predicted: Bush true:      Bush, predicted: Bush true:      Bush, predicted: Blair true:      Blair, predicted: Bush true:      Bush, predicted: Bush true:      Bush, predicted: Bush true:      Bush, predicted: Schroeder true:      Schroeder, predicted: Powell true:      Powell, predicted: Bush true:      Bush, predicted: Bush true:      Bush, predicted: Bush true:      Bush, predicted: Bush true:      Bush](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_002.png)\
\
<Figure size 720x720 with 12 Axes>\
\
Copy to clipboard\
\
Eigenfaces gallery[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#eigenfaces-gallery "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We display the most significant eigenfaces, i.e. the principal components that form the basis of the face representation learned by the fitted pipeline.\
\
pca \= clf.best\_estimator\_.named\_steps\["pca"\]\
eigenfaces \= pca.components\_.reshape((pca.n\_components\_, height, width))\
\
eigenface\_titles \= \[f"eigenface {i}" for i in range(eigenfaces.shape\[0\])\]\
plot\_gallery(eigenfaces, eigenface\_titles, height, width)\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![eigenface 0, eigenface 1, eigenface 2, eigenface 3, eigenface 4, eigenface 5, eigenface 6, eigenface 7, eigenface 8, eigenface 9, eigenface 10, eigenface 11](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_003.png)\
\
Conclusion[#](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#conclusion "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------\
\
This example walks through a classical face recognition pipeline in scikit-learn:\
\
*   **Eigenfaces (PCA)** reduce the high-dimensional pixel space to a compact set of uncorrelated features that capture the main variations across faces.\
    \
*   **Nystroem + LogisticRegression** approximate a non-linear RBF kernel with a linear model that scales better than a kernel SVM and is tuned to minimize the log loss.\
    \
*   **Pipeline** chains preprocessing and classification so that cross-validation does not leak information from the test set.\
    \
*   **Quantitative and qualitative evaluation** on a held-out test set confirm whether the pipeline generalizes. The one-vs-rest ROC and precision-recall curves show how well the predicted probabilities rank each identity against the others, independently of any single decision threshold.\
    \
\
In practice, face recognition is often better addressed with convolutional neural networks, but this family of models is outside the scope of the scikit-learn library. Interested readers should instead try PyTorch or TensorFlow to implement such models.\
\
**Total running time of the script:** (0 minutes 17.727 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_face_recognition.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_face_recognition.ipynb)\
\
[`Download Jupyter notebook: plot_face_recognition.ipynb`](https://scikit-learn.org/stable/_downloads/23e3d7fa2388aef4e9a60c4a6caf166d/plot_face_recognition.ipynb)\
\
[`Download Python source code: plot_face_recognition.py`](https://scikit-learn.org/stable/_downloads/b3a994b2ad66fe78bcedaf151ab78b07/plot_face_recognition.py)\
\
[`Download zipped: plot_face_recognition.zip`](https://scikit-learn.org/stable/_downloads/fac66cd1688e423f58fe5d640246cb2d/plot_face_recognition.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)\
\
[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)\
\
Precision-Recall\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)\
\
[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)\
\
Multiclass Receiver Operating Characteristic (ROC)\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)\
\
[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)\
\
Receiver Operating Characteristic (ROC) with cross validation\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)\
\
[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)\
\
Analysis of the convergence of penalized logistic regression models\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/b3a994b2ad66fe78bcedaf151ab78b07/plot_face_recognition.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/23e3d7fa2388aef4e9a60c4a6caf166d/plot_face_recognition.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/fac66cd1688e423f58fe5d640246cb2d/plot_face_recognition.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_face_recognition.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_face_recognition.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)