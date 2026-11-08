[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/raw_ops?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/raw_ops?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/raw_ops?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fraw_ops%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/raw_ops?version=stable#functions_2)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.raw\_ops Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/raw_ops?version=stable#functions_2)
    

See Stable See Nightly

Public API for tf.\_api.v2.raw\_ops namespace

Functions
---------

[`Abort(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Abort)
: Raise a exception to abort the process when called.

[`Abs(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Abs)
: Computes the absolute value of a tensor.

[`AccumulateNV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AccumulateNV2)
: Returns the element-wise sum of a list of tensors.

[`AccumulatorApplyGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AccumulatorApplyGradient)
: Applies a gradient to a given accumulator.

[`AccumulatorNumAccumulated(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AccumulatorNumAccumulated)
: Returns the number of gradients aggregated in the given accumulators.

[`AccumulatorSetGlobalStep(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AccumulatorSetGlobalStep)
: Updates the accumulator with a new value for global\_step.

[`AccumulatorTakeGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AccumulatorTakeGradient)
: Extracts the average gradient in the given ConditionalAccumulator.

[`Acos(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Acos)
: Computes acos of x element-wise.

[`Acosh(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Acosh)
: Computes inverse hyperbolic cosine of x element-wise.

[`Add(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Add)
: Returns x + y element-wise.

[`AddManySparseToTensorsMap(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AddManySparseToTensorsMap)
: Add an `N`\-minibatch `SparseTensor` to a `SparseTensorsMap`, return `N` handles.

[`AddN(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AddN)
: Add all input tensors element wise.

[`AddSparseToTensorsMap(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AddSparseToTensorsMap)
: Add a `SparseTensor` to a `SparseTensorsMap` return its handle.

[`AddV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AddV2)
: Returns x + y element-wise.

[`AdjustContrast(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AdjustContrast)
: Deprecated. Disallowed in GraphDef version >= 2.

[`AdjustContrastv2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AdjustContrastv2)
: Adjust the contrast of one or more images.

[`AdjustHue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AdjustHue)
: Adjust the hue of one or more images.

[`AdjustSaturation(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AdjustSaturation)
: Adjust the saturation of one or more images.

[`All(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/All)
: Computes the "logical and" of elements across dimensions of a tensor.

[`AllCandidateSampler(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AllCandidateSampler)
: Generates labels for candidate sampling with a learned unigram distribution.

[`AllToAll(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AllToAll)
: An Op to exchange data across TPU replicas.

[`Angle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Angle)
: Returns the argument of a complex number.

[`AnonymousHashTable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousHashTable)
: Creates a uninitialized anonymous hash table.

[`AnonymousIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousIterator)
: A container for an iterator resource.

[`AnonymousIteratorV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousIteratorV2)
: A container for an iterator resource.

[`AnonymousIteratorV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousIteratorV3)
: A container for an iterator resource.

[`AnonymousMemoryCache(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousMemoryCache)

[`AnonymousMultiDeviceIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousMultiDeviceIterator)
: A container for a multi device iterator resource.

[`AnonymousMultiDeviceIteratorV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousMultiDeviceIteratorV3)
: A container for a multi device iterator resource.

[`AnonymousMutableDenseHashTable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousMutableDenseHashTable)
: Creates an empty anonymous mutable hash table that uses tensors as the backing store.

[`AnonymousMutableHashTable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousMutableHashTable)
: Creates an empty anonymous mutable hash table.

[`AnonymousMutableHashTableOfTensors(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousMutableHashTableOfTensors)
: Creates an empty anonymous mutable hash table of vector values.

[`AnonymousRandomSeedGenerator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousRandomSeedGenerator)

[`AnonymousSeedGenerator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AnonymousSeedGenerator)

[`Any(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Any)
: Computes the "logical or" of elements across dimensions of a tensor.

[`ApplyAdaMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyAdaMax)
: Update '\*var' according to the AdaMax algorithm.

[`ApplyAdadelta(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyAdadelta)
: Update '\*var' according to the adadelta scheme.

[`ApplyAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyAdagrad)
: Update '\*var' according to the adagrad scheme.

[`ApplyAdagradDA(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyAdagradDA)
: Update '\*var' according to the proximal adagrad scheme.

[`ApplyAdagradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyAdagradV2)
: Update '\*var' according to the adagrad scheme.

[`ApplyAdam(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyAdam)
: Update '\*var' according to the Adam algorithm.

[`ApplyAddSign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyAddSign)
: Update '\*var' according to the AddSign update.

[`ApplyCenteredRMSProp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyCenteredRMSProp)
: Update '\*var' according to the centered RMSProp algorithm.

[`ApplyFtrl(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyFtrl)
: Update '\*var' according to the Ftrl-proximal scheme.

[`ApplyFtrlV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyFtrlV2)
: Update '\*var' according to the Ftrl-proximal scheme.

[`ApplyGradientDescent(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyGradientDescent)
: Update '\*var' by subtracting 'alpha' \* 'delta' from it.

[`ApplyMomentum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyMomentum)
: Update '\*var' according to the momentum scheme.

[`ApplyPowerSign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyPowerSign)
: Update '\*var' according to the AddSign update.

[`ApplyProximalAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyProximalAdagrad)
: Update '_var' and '_accum' according to FOBOS with Adagrad learning rate.

[`ApplyProximalGradientDescent(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyProximalGradientDescent)
: Update '\*var' as FOBOS algorithm with fixed learning rate.

[`ApplyRMSProp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApplyRMSProp)
: Update '\*var' according to the RMSProp algorithm.

[`ApproxTopK(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApproxTopK)
: Returns min/max k values and their indices of the input operand in an approximate manner.

[`ApproximateEqual(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ApproximateEqual)
: Returns the truth value of abs(x-y) < tolerance element-wise.

[`ArgMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ArgMax)
: Returns the index with the largest value across dimensions of a tensor.

[`ArgMin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ArgMin)
: Returns the index with the smallest value across dimensions of a tensor.

[`AsString(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AsString)
: Converts each entry in the given tensor to strings.

[`Asin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Asin)
: Computes the trignometric inverse sine of x element-wise.

[`Asinh(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Asinh)
: Computes inverse hyperbolic sine of x element-wise.

[`Assert(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Assert)
: Asserts that the given condition is true.

[`AssertCardinalityDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssertCardinalityDataset)

[`AssertNextDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssertNextDataset)
: A transformation that asserts which transformations happen next.

[`AssertPrevDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssertPrevDataset)
: A transformation that asserts which transformations happened previously.

[`Assign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Assign)
: Update 'ref' by assigning 'value' to it.

[`AssignAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssignAdd)
: Update 'ref' by adding 'value' to it.

[`AssignAddVariableOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssignAddVariableOp)
: Adds a value to the current value of a variable.

[`AssignSub(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssignSub)
: Update 'ref' by subtracting 'value' from it.

[`AssignSubVariableOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssignSubVariableOp)
: Subtracts a value from the current value of a variable.

[`AssignVariableOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssignVariableOp)
: Assigns a new value to a variable.

[`AssignVariableXlaConcatND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AssignVariableXlaConcatND)
: Concats input tensor across all dimensions.

[`Atan(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Atan)
: Computes the trignometric inverse tangent of x element-wise.

[`Atan2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Atan2)
: Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

[`Atanh(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Atanh)
: Computes inverse hyperbolic tangent of x element-wise.

[`AudioSpectrogram(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AudioSpectrogram)
: Produces a visualization of audio data over time.

[`AudioSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AudioSummary)
: Outputs a `Summary` protocol buffer with audio.

[`AudioSummaryV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AudioSummaryV2)
: Outputs a `Summary` protocol buffer with audio.

[`AutoShardDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AutoShardDataset)
: Creates a dataset that shards the input dataset.

[`AvgPool(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AvgPool)
: Performs average pooling on the input.

[`AvgPool3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AvgPool3D)
: Performs 3D average pooling on the input.

[`AvgPool3DGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AvgPool3DGrad)
: Computes gradients of average pooling function.

[`AvgPoolGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/AvgPoolGrad)
: Computes gradients of the average pooling function.

[`BandedTriangularSolve(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BandedTriangularSolve)

[`Barrier(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Barrier)
: Defines a barrier that persists across different graph executions.

[`BarrierClose(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BarrierClose)
: Closes the given barrier.

[`BarrierIncompleteSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BarrierIncompleteSize)
: Computes the number of incomplete elements in the given barrier.

[`BarrierInsertMany(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BarrierInsertMany)
: For each key, assigns the respective value to the specified component.

[`BarrierReadySize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BarrierReadySize)
: Computes the number of complete elements in the given barrier.

[`BarrierTakeMany(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BarrierTakeMany)
: Takes the given number of completed elements from a barrier.

[`Batch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Batch)
: Batches all input tensors nondeterministically.

[`BatchCholesky(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchCholesky)

[`BatchCholeskyGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchCholeskyGrad)

[`BatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchDataset)
: Creates a dataset that batches `batch_size` elements from `input_dataset`.

[`BatchDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchDatasetV2)
: Creates a dataset that batches `batch_size` elements from `input_dataset`.

[`BatchFFT(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchFFT)

[`BatchFFT2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchFFT2D)

[`BatchFFT3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchFFT3D)

[`BatchFunction(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchFunction)
: Batches all the inputs tensors to the computation done by the function.

[`BatchIFFT(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchIFFT)

[`BatchIFFT2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchIFFT2D)

[`BatchIFFT3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchIFFT3D)

[`BatchMatMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatMul)
: Multiplies slices of two tensors in batches.

[`BatchMatMulV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatMulV2)
: Multiplies slices of two tensors in batches.

[`BatchMatMulV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatMulV3)
: Multiplies slices of two tensors in batches.

[`BatchMatrixBandPart(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixBandPart)

[`BatchMatrixDeterminant(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixDeterminant)

[`BatchMatrixDiag(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixDiag)

[`BatchMatrixDiagPart(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixDiagPart)

[`BatchMatrixInverse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixInverse)

[`BatchMatrixSetDiag(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixSetDiag)

[`BatchMatrixSolve(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixSolve)

[`BatchMatrixSolveLs(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixSolveLs)

[`BatchMatrixTriangularSolve(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchMatrixTriangularSolve)

[`BatchNormWithGlobalNormalization(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchNormWithGlobalNormalization)
: Batch normalization.

[`BatchNormWithGlobalNormalizationGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchNormWithGlobalNormalizationGrad)
: Gradients for batch normalization.

[`BatchSelfAdjointEig(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchSelfAdjointEig)

[`BatchSelfAdjointEigV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchSelfAdjointEigV2)

[`BatchSvd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchSvd)

[`BatchToSpace(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchToSpace)
: BatchToSpace for 4-D tensors of type T.

[`BatchToSpaceND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BatchToSpaceND)
: BatchToSpace for N-D tensors of type T.

[`BesselI0(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselI0)

[`BesselI0e(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselI0e)

[`BesselI1(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselI1)

[`BesselI1e(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselI1e)

[`BesselJ0(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselJ0)

[`BesselJ1(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselJ1)

[`BesselK0(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselK0)

[`BesselK0e(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselK0e)

[`BesselK1(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselK1)

[`BesselK1e(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselK1e)

[`BesselY0(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselY0)

[`BesselY1(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BesselY1)

[`Betainc(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Betainc)
: Compute the regularized incomplete beta integral Ix(a,b).

[`BiasAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BiasAdd)
: Adds `bias` to `value`.

[`BiasAddGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BiasAddGrad)
: The backward operation for "BiasAdd" on the "bias" tensor.

[`BiasAddV1(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BiasAddV1)
: Adds `bias` to `value`.

[`Bincount(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Bincount)
: Counts the number of occurrences of each value in an integer array.

[`Bitcast(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Bitcast)
: Bitcasts a tensor from one type to another without copying data.

[`BitwiseAnd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BitwiseAnd)
: Elementwise computes the bitwise AND of `x` and `y`.

[`BitwiseOr(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BitwiseOr)
: Elementwise computes the bitwise OR of `x` and `y`.

[`BitwiseXor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BitwiseXor)
: Elementwise computes the bitwise XOR of `x` and `y`.

[`BlockLSTM(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BlockLSTM)
: Computes the LSTM cell forward propagation for all the time steps.

[`BlockLSTMGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BlockLSTMGrad)
: Computes the LSTM cell backward propagation for the entire time sequence.

[`BlockLSTMGradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BlockLSTMGradV2)
: Computes the LSTM cell backward propagation for the entire time sequence.

[`BlockLSTMV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BlockLSTMV2)
: Computes the LSTM cell forward propagation for all the time steps.

[`BoostedTreesAggregateStats(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesAggregateStats)
: Aggregates the summary of accumulated stats for the batch.

[`BoostedTreesBucketize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesBucketize)
: Bucketize each feature based on bucket boundaries.

[`BoostedTreesCalculateBestFeatureSplit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesCalculateBestFeatureSplit)
: Calculates gains for each feature and returns the best possible split information for the feature.

[`BoostedTreesCalculateBestFeatureSplitV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesCalculateBestFeatureSplitV2)
: Calculates gains for each feature and returns the best possible split information for each node. However, if no split is found, then no split information is returned for that node.

[`BoostedTreesCalculateBestGainsPerFeature(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesCalculateBestGainsPerFeature)
: Calculates gains for each feature and returns the best possible split information for the feature.

[`BoostedTreesCenterBias(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesCenterBias)
: Calculates the prior from the training data (the bias) and fills in the first node with the logits' prior. Returns a boolean indicating whether to continue centering.

[`BoostedTreesCreateEnsemble(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesCreateEnsemble)
: Creates a tree ensemble model and returns a handle to it.

[`BoostedTreesCreateQuantileStreamResource(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesCreateQuantileStreamResource)
: Create the Resource for Quantile Streams.

[`BoostedTreesDeserializeEnsemble(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesDeserializeEnsemble)
: Deserializes a serialized tree ensemble config and replaces current tree

[`BoostedTreesEnsembleResourceHandleOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesEnsembleResourceHandleOp)
: Creates a handle to a BoostedTreesEnsembleResource

[`BoostedTreesExampleDebugOutputs(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesExampleDebugOutputs)
: Debugging/model interpretability outputs for each example.

[`BoostedTreesFlushQuantileSummaries(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesFlushQuantileSummaries)
: Flush the quantile summaries from each quantile stream resource.

[`BoostedTreesGetEnsembleStates(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesGetEnsembleStates)
: Retrieves the tree ensemble resource stamp token, number of trees and growing statistics.

[`BoostedTreesMakeQuantileSummaries(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesMakeQuantileSummaries)
: Makes the summary of quantiles for the batch.

[`BoostedTreesMakeStatsSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesMakeStatsSummary)
: Makes the summary of accumulated stats for the batch.

[`BoostedTreesPredict(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesPredict)
: Runs multiple additive regression ensemble predictors on input instances and

[`BoostedTreesQuantileStreamResourceAddSummaries(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesQuantileStreamResourceAddSummaries)
: Add the quantile summaries to each quantile stream resource.

[`BoostedTreesQuantileStreamResourceDeserialize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesQuantileStreamResourceDeserialize)
: Deserialize bucket boundaries and ready flag into current QuantileAccumulator.

[`BoostedTreesQuantileStreamResourceFlush(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesQuantileStreamResourceFlush)
: Flush the summaries for a quantile stream resource.

[`BoostedTreesQuantileStreamResourceGetBucketBoundaries(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesQuantileStreamResourceGetBucketBoundaries)
: Generate the bucket boundaries for each feature based on accumulated summaries.

[`BoostedTreesQuantileStreamResourceHandleOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesQuantileStreamResourceHandleOp)
: Creates a handle to a BoostedTreesQuantileStreamResource.

[`BoostedTreesSerializeEnsemble(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesSerializeEnsemble)
: Serializes the tree ensemble to a proto.

[`BoostedTreesSparseAggregateStats(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesSparseAggregateStats)
: Aggregates the summary of accumulated stats for the batch.

[`BoostedTreesSparseCalculateBestFeatureSplit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesSparseCalculateBestFeatureSplit)
: Calculates gains for each feature and returns the best possible split information for the feature.

[`BoostedTreesTrainingPredict(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesTrainingPredict)
: Runs multiple additive regression ensemble predictors on input instances and

[`BoostedTreesUpdateEnsemble(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesUpdateEnsemble)
: Updates the tree ensemble by either adding a layer to the last tree being grown

[`BoostedTreesUpdateEnsembleV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BoostedTreesUpdateEnsembleV2)
: Updates the tree ensemble by adding a layer to the last tree being grown

[`BroadcastArgs(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BroadcastArgs)
: Return the shape of s0 op s1 with broadcast.

[`BroadcastGradientArgs(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BroadcastGradientArgs)
: Return the reduction indices for computing gradients of s0 op s1 with broadcast.

[`BroadcastTo(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BroadcastTo)
: Broadcast an array for a compatible shape.

[`Bucketize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Bucketize)
: Bucketizes 'input' based on 'boundaries'.

[`BytesProducedStatsDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/BytesProducedStatsDataset)
: Records the bytes size of each element of `input_dataset` in a StatsAggregator.

[`CSRSparseMatrixComponents(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CSRSparseMatrixComponents)
: Reads out the CSR components at batch `index`.

[`CSRSparseMatrixToDense(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CSRSparseMatrixToDense)
: Convert a (possibly batched) CSRSparseMatrix to dense.

[`CSRSparseMatrixToSparseTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CSRSparseMatrixToSparseTensor)
: Converts a (possibly batched) CSRSparesMatrix to a SparseTensor.

[`CSVDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CSVDataset)

[`CSVDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CSVDatasetV2)

[`CTCBeamSearchDecoder(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CTCBeamSearchDecoder)
: Performs beam search decoding on the logits given in input.

[`CTCGreedyDecoder(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CTCGreedyDecoder)
: Performs greedy decoding on the logits given in inputs.

[`CTCLoss(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CTCLoss)
: Calculates the CTC Loss (log probability) for each batch entry.

[`CTCLossV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CTCLossV2)
: Calculates the CTC Loss (log probability) for each batch entry.

[`CacheDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CacheDataset)
: Creates a dataset that caches elements from `input_dataset`.

[`CacheDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CacheDatasetV2)

[`Case(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Case)
: An n-way switch statement which calls a single branch function.

[`Cast(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Cast)
: Cast x of type SrcT to y of DstT.

[`Ceil(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Ceil)
: Returns element-wise smallest integer not less than x.

[`CheckNumerics(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CheckNumerics)
: Checks a tensor for NaN and Inf values.

[`CheckNumericsV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CheckNumericsV2)
: Checks a tensor for NaN, -Inf and +Inf values.

[`CheckPinned(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CheckPinned)
: Checks whether a tensor is located in host memory pinned for GPU.

[`Cholesky(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Cholesky)
: Computes the Cholesky decomposition of one or more square matrices.

[`CholeskyGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CholeskyGrad)
: Computes the reverse mode backpropagated gradient of the Cholesky algorithm.

[`ChooseFastestBranchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ChooseFastestBranchDataset)

[`ChooseFastestDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ChooseFastestDataset)

[`ClipByValue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ClipByValue)
: Clips tensor values to a specified min and max.

[`CloseSummaryWriter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CloseSummaryWriter)

[`CollectiveAllToAllV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveAllToAllV2)
: Mutually exchanges multiple tensors of identical type and shape.

[`CollectiveAllToAllV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveAllToAllV3)
: Mutually exchanges multiple tensors of identical type and shape.

[`CollectiveAssignGroupV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveAssignGroupV2)
: Assign group keys based on group assignment.

[`CollectiveBcastRecv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveBcastRecv)
: Receives a tensor value broadcast from another device.

[`CollectiveBcastRecvV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveBcastRecvV2)
: Receives a tensor value broadcast from another device.

[`CollectiveBcastSend(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveBcastSend)
: Broadcasts a tensor value to one or more other devices.

[`CollectiveBcastSendV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveBcastSendV2)
: Broadcasts a tensor value to one or more other devices.

[`CollectiveGather(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveGather)
: Mutually accumulates multiple tensors of identical type and shape.

[`CollectiveGatherV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveGatherV2)
: Mutually accumulates multiple tensors of identical type and shape.

[`CollectiveInitializeCommunicator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveInitializeCommunicator)
: Initializes a group for collective operations.

[`CollectivePermute(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectivePermute)
: An Op to permute tensors across replicated TPU instances.

[`CollectiveReduce(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveReduce)
: Mutually reduces multiple tensors of identical type and shape.

[`CollectiveReduceScatterV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveReduceScatterV2)
: Mutually reduces multiple tensors of identical type and shape and scatters the result.

[`CollectiveReduceV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveReduceV2)
: Mutually reduces multiple tensors of identical type and shape.

[`CollectiveReduceV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CollectiveReduceV3)
: Mutually reduces multiple tensors of identical type and shape.

[`CombinedNonMaxSuppression(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CombinedNonMaxSuppression)
: Greedily selects a subset of bounding boxes in descending order of score,

[`Complex(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Complex)
: Converts two real numbers to a complex number.

[`ComplexAbs(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ComplexAbs)
: Computes the complex absolute value of a tensor.

[`CompositeTensorVariantFromComponents(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CompositeTensorVariantFromComponents)
: Encodes an `ExtensionType` value into a `variant` scalar Tensor.

[`CompositeTensorVariantToComponents(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CompositeTensorVariantToComponents)
: Decodes a `variant` scalar Tensor into an `ExtensionType` value.

[`CompressElement(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CompressElement)
: Compresses a dataset element.

[`ComputeAccidentalHits(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ComputeAccidentalHits)
: Computes the ids of the positions in sampled\_candidates that match true\_labels.

[`ComputeBatchSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ComputeBatchSize)
: Computes the static batch size of a dataset sans partial batches.

[`Concat(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Concat)
: Concatenates tensors along one dimension.

[`ConcatOffset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConcatOffset)
: Computes offsets of concat inputs within its output.

[`ConcatV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConcatV2)
: Concatenates tensors along one dimension.

[`ConcatenateDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConcatenateDataset)
: Creates a dataset that concatenates `input_dataset` with `another_dataset`.

[`ConditionalAccumulator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConditionalAccumulator)
: A conditional accumulator for aggregating gradients.

[`ConfigureDistributedTPU(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConfigureDistributedTPU)
: Sets up the centralized structures for a distributed TPU system.

[`ConfigureTPUEmbedding(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConfigureTPUEmbedding)
: Sets up TPUEmbedding in a distributed TPU system.

[`Conj(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conj)
: Returns the complex conjugate of a complex number.

[`ConjugateTranspose(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConjugateTranspose)
: Shuffle dimensions of x according to a permutation and conjugate the result.

[`Const(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Const)
: Returns a constant tensor.

[`ConsumeMutexLock(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConsumeMutexLock)
: This op consumes a lock created by `MutexLock`.

[`ControlTrigger(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ControlTrigger)
: Does nothing. Serves as a control trigger for scheduling.

[`Conv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv)
: Computes a N-D convolution given (N+1+batch\_dims)-D `input` and (N+2)-D `filter` tensors.

[`Conv2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv2D)
: Computes a 2-D convolution given 4-D `input` and `filter` tensors.

[`Conv2DBackpropFilter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv2DBackpropFilter)
: Computes the gradients of convolution with respect to the filter.

[`Conv2DBackpropFilterV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv2DBackpropFilterV2)
: Computes the gradients of convolution with respect to the filter.

[`Conv2DBackpropInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv2DBackpropInput)
: Computes the gradients of convolution with respect to the input.

[`Conv2DBackpropInputV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv2DBackpropInputV2)
: Computes the gradients of convolution with respect to the input.

[`Conv3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv3D)
: Computes a 3-D convolution given 5-D `input` and `filter` tensors.

[`Conv3DBackpropFilter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv3DBackpropFilter)
: Computes the gradients of 3-D convolution with respect to the filter.

[`Conv3DBackpropFilterV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv3DBackpropFilterV2)
: Computes the gradients of 3-D convolution with respect to the filter.

[`Conv3DBackpropInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv3DBackpropInput)
: Computes the gradients of 3-D convolution with respect to the input.

[`Conv3DBackpropInputV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Conv3DBackpropInputV2)
: Computes the gradients of 3-D convolution with respect to the input.

[`ConvertToCooTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConvertToCooTensor)

[`ConvertToListOfSparseCoreCooTensors(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConvertToListOfSparseCoreCooTensors)

[`ConvertToSparseCoreCsrWrappedCooTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ConvertToSparseCoreCsrWrappedCooTensor)

[`Copy(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Copy)
: Copy a tensor from CPU-to-CPU or GPU-to-GPU.

[`CopyHost(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CopyHost)
: Copy a tensor to host.

[`Cos(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Cos)
: Computes cos of x element-wise.

[`Cosh(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Cosh)
: Computes hyperbolic cosine of x element-wise.

[`CountUpTo(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CountUpTo)
: Increments 'ref' until it reaches 'limit'.

[`CreateSummaryDbWriter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CreateSummaryDbWriter)

[`CreateSummaryFileWriter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CreateSummaryFileWriter)

[`CropAndResize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CropAndResize)
: Extracts crops from the input image tensor and resizes them.

[`CropAndResizeGradBoxes(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CropAndResizeGradBoxes)
: Computes the gradient of the crop\_and\_resize op wrt the input boxes tensor.

[`CropAndResizeGradImage(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CropAndResizeGradImage)
: Computes the gradient of the crop\_and\_resize op wrt the input image tensor.

[`Cross(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Cross)
: Compute the pairwise cross product.

[`CrossReplicaSum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CrossReplicaSum)
: An Op to sum inputs across replicated TPU instances.

[`CudnnRNN(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNN)
: A RNN backed by cuDNN.

[`CudnnRNNBackprop(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNBackprop)
: Backprop step of CudnnRNN.

[`CudnnRNNBackpropV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNBackpropV2)
: Backprop step of CudnnRNN.

[`CudnnRNNBackpropV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNBackpropV3)
: Backprop step of CudnnRNNV3.

[`CudnnRNNCanonicalToParams(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNCanonicalToParams)
: Converts CudnnRNN params from canonical form to usable form.

[`CudnnRNNCanonicalToParamsV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNCanonicalToParamsV2)
: Converts CudnnRNN params from canonical form to usable form. It supports the projection in LSTM.

[`CudnnRNNParamsSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNParamsSize)
: Computes size of weights that can be used by a Cudnn RNN model.

[`CudnnRNNParamsToCanonical(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNParamsToCanonical)
: Retrieves CudnnRNN params in canonical form.

[`CudnnRNNParamsToCanonicalV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNParamsToCanonicalV2)
: Retrieves CudnnRNN params in canonical form. It supports the projection in LSTM.

[`CudnnRNNV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNV2)
: A RNN backed by cuDNN.

[`CudnnRNNV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CudnnRNNV3)
: A RNN backed by cuDNN.

[`Cumprod(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Cumprod)
: Compute the cumulative product of the tensor `x` along `axis`.

[`Cumsum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Cumsum)
: Compute the cumulative sum of the tensor `x` along `axis`.

[`CumulativeLogsumexp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/CumulativeLogsumexp)
: Compute the cumulative product of the tensor `x` along `axis`.

[`DataFormatDimMap(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DataFormatDimMap)
: Returns the dimension index in the destination data format given the one in

[`DataFormatVecPermute(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DataFormatVecPermute)
: Permute input tensor from `src_format` to `dst_format`.

[`DataServiceDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DataServiceDataset)
: Creates a dataset that reads data from the tf.data service.

[`DataServiceDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DataServiceDatasetV2)
: Creates a dataset that reads data from the tf.data service.

[`DataServiceDatasetV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DataServiceDatasetV3)
: Creates a dataset that reads data from the tf.data service.

[`DataServiceDatasetV4(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DataServiceDatasetV4)
: Creates a dataset that reads data from the tf.data service.

[`DatasetCardinality(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DatasetCardinality)
: Returns the cardinality of `input_dataset`.

[`DatasetFingerprint(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DatasetFingerprint)
: Returns the fingerprint of `input_dataset`.

[`DatasetFromGraph(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DatasetFromGraph)
: Creates a dataset from the given `graph_def`.

[`DatasetToGraph(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DatasetToGraph)
: Returns a serialized GraphDef representing `input_dataset`.

[`DatasetToGraphV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DatasetToGraphV2)
: Returns a serialized GraphDef representing `input_dataset`.

[`DatasetToSingleElement(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DatasetToSingleElement)
: Outputs the single element from the given dataset.

[`DatasetToTFRecord(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DatasetToTFRecord)
: Writes the given dataset to the given file using the TFRecord format.

[`Dawsn(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Dawsn)

[`DebugGradientIdentity(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DebugGradientIdentity)
: Identity op for gradient debugging.

[`DebugGradientRefIdentity(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DebugGradientRefIdentity)
: Identity op for gradient debugging.

[`DebugIdentity(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DebugIdentity)
: Provides an identity mapping of the non-Ref type input tensor for debugging.

[`DebugIdentityV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DebugIdentityV2)
: Debug Identity V2 Op.

[`DebugIdentityV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DebugIdentityV3)
: Provides an identity mapping of the non-Ref type input tensor for debugging.

[`DebugNanCount(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DebugNanCount)
: Debug NaN Value Counter Op.

[`DebugNumericSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DebugNumericSummary)
: Debug Numeric Summary Op.

[`DebugNumericSummaryV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DebugNumericSummaryV2)
: Debug Numeric Summary V2 Op.

[`DecodeAndCropJpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeAndCropJpeg)
: Decode and Crop a JPEG-encoded image to a uint8 tensor.

[`DecodeBase64(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeBase64)
: Decode web-safe base64-encoded strings.

[`DecodeBmp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeBmp)
: Decode the first frame of a BMP-encoded image to a uint8 tensor.

[`DecodeCSV(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeCSV)
: Convert CSV records to tensors. Each column maps to one tensor.

[`DecodeCompressed(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeCompressed)
: Decompress strings.

[`DecodeGif(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeGif)
: Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

[`DecodeImage(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeImage)
: Function for decode\_bmp, decode\_gif, decode\_jpeg, decode\_jxl, decode\_webp, and decode\_png.

[`DecodeJSONExample(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeJSONExample)
: Convert JSON-encoded Example records to binary protocol buffer strings.

[`DecodeJpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeJpeg)
: Decode a JPEG-encoded image to a uint8 tensor.

[`DecodeJxl(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeJxl)
: Decode a JPEG XL encoded image to a uint8 tensor.

[`DecodePaddedRaw(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodePaddedRaw)
: Reinterpret the bytes of a string as a vector of numbers.

[`DecodePng(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodePng)
: Decode a PNG-encoded image to a uint8 or uint16 tensor.

[`DecodeProtoV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeProtoV2)
: The op extracts fields from a serialized protocol buffers message into tensors.

[`DecodeRaw(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeRaw)
: Reinterpret the bytes of a string as a vector of numbers.

[`DecodeWav(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeWav)
: Decode a 16-bit PCM WAV file to a float tensor.

[`DecodeWebP(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DecodeWebP)
: Decode a WebP-encoded image to a uint8 tensor.

[`DeepCopy(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeepCopy)
: Makes a copy of `x`.

[`DeleteIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeleteIterator)
: A container for an iterator resource.

[`DeleteMemoryCache(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeleteMemoryCache)

[`DeleteMultiDeviceIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeleteMultiDeviceIterator)
: A container for an iterator resource.

[`DeleteRandomSeedGenerator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeleteRandomSeedGenerator)

[`DeleteSeedGenerator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeleteSeedGenerator)

[`DeleteSessionTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeleteSessionTensor)
: Delete the tensor specified by its handle in the session.

[`DenseBincount(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DenseBincount)
: Counts the number of occurrences of each value in an integer array.

[`DenseCountSparseOutput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DenseCountSparseOutput)
: Performs sparse-output bin counting for a tf.tensor input.

[`DenseToCSRSparseMatrix(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DenseToCSRSparseMatrix)
: Converts a dense tensor to a (possibly batched) CSRSparseMatrix.

[`DenseToDenseSetOperation(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DenseToDenseSetOperation)
: Applies set operation along last dimension of 2 `Tensor` inputs.

[`DenseToSparseBatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DenseToSparseBatchDataset)
: Creates a dataset that batches input elements into a SparseTensor.

[`DenseToSparseSetOperation(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DenseToSparseSetOperation)
: Applies set operation along last dimension of `Tensor` and `SparseTensor`.

[`DepthToSpace(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DepthToSpace)
: DepthToSpace for tensors of type T.

[`DepthwiseConv2dNative(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DepthwiseConv2dNative)
: Computes a 2-D depthwise convolution given 4-D `input` and `filter` tensors.

[`DepthwiseConv2dNativeBackpropFilter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DepthwiseConv2dNativeBackpropFilter)
: Computes the gradients of depthwise convolution with respect to the filter.

[`DepthwiseConv2dNativeBackpropInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DepthwiseConv2dNativeBackpropInput)
: Computes the gradients of depthwise convolution with respect to the input.

[`Dequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Dequantize)
: Dequantize the 'input' tensor into a float or bfloat16 Tensor.

[`DeserializeIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeserializeIterator)
: Converts the given variant tensor to an iterator and stores it in the given resource.

[`DeserializeManySparse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeserializeManySparse)
: Deserialize and concatenate `SparseTensors` from a serialized minibatch.

[`DeserializeSparse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeserializeSparse)
: Deserialize `SparseTensor` objects.

[`DestroyResourceOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DestroyResourceOp)
: Deletes the resource specified by the handle.

[`DestroyTemporaryVariable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DestroyTemporaryVariable)
: Destroys the temporary variable and returns its final value.

[`DeviceIndex(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DeviceIndex)
: Return the index of device the op runs.

[`Diag(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Diag)
: Returns a diagonal tensor with a given diagonal values.

[`DiagPart(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DiagPart)
: Returns the diagonal part of the tensor.

[`Digamma(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Digamma)
: Computes Psi, the derivative of Lgamma (the log of the absolute value of

[`Dilation2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Dilation2D)
: Computes the grayscale dilation of 4-D `input` and 3-D `filter` tensors.

[`Dilation2DBackpropFilter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Dilation2DBackpropFilter)
: Computes the gradient of morphological 2-D dilation with respect to the filter.

[`Dilation2DBackpropInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Dilation2DBackpropInput)
: Computes the gradient of morphological 2-D dilation with respect to the input.

[`DirectedInterleaveDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DirectedInterleaveDataset)
: A substitute for `InterleaveDataset` on a fixed list of `N` datasets.

[`DisableCopyOnRead(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DisableCopyOnRead)
: Turns off the copy-on-read mode.

[`DistributedSave(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DistributedSave)

[`Div(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Div)
: Returns x / y element-wise.

[`DivNoNan(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DivNoNan)
: Returns 0 if the denominator is zero.

[`DrawBoundingBoxes(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DrawBoundingBoxes)
: Draw bounding boxes on a batch of images.

[`DrawBoundingBoxesV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DrawBoundingBoxesV2)
: Draw bounding boxes on a batch of images.

[`DummyIterationCounter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DummyIterationCounter)

[`DummyMemoryCache(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DummyMemoryCache)

[`DummySeedGenerator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DummySeedGenerator)

[`DynamicEnqueueTPUEmbeddingArbitraryTensorBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DynamicEnqueueTPUEmbeddingArbitraryTensorBatch)
: Eases the porting of code that uses tf.nn.embedding\_lookup\_sparse().

[`DynamicEnqueueTPUEmbeddingRaggedTensorBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DynamicEnqueueTPUEmbeddingRaggedTensorBatch)

[`DynamicPartition(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DynamicPartition)
: Partitions `data` into `num_partitions` tensors using indices from `partitions`.

[`DynamicStitch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DynamicStitch)
: Interleave the values from the `data` tensors into a single tensor.

[`EagerPyFunc(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EagerPyFunc)
: Eagerly executes a python function to compute func(input)->output.

[`EditDistance(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EditDistance)
: Computes the (possibly normalized) Levenshtein Edit Distance.

[`Eig(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Eig)
: Computes the eigen decomposition of one or more square matrices.

[`Einsum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Einsum)
: Tensor contraction according to Einstein summation convention.

[`Elu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Elu)
: Computes the exponential linear function.

[`EluGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EluGrad)
: Computes gradients for the exponential linear (Elu) operation.

[`Empty(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Empty)
: Creates a tensor with the given shape.

[`EmptyTensorList(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EmptyTensorList)
: Creates and returns an empty tensor list.

[`EmptyTensorMap(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EmptyTensorMap)
: Creates and returns an empty tensor map.

[`EncodeBase64(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EncodeBase64)
: Encode strings into web-safe base64 format.

[`EncodeJpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EncodeJpeg)
: JPEG-encode an image.

[`EncodeJpegVariableQuality(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EncodeJpegVariableQuality)
: JPEG encode input image with provided compression quality.

[`EncodePng(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EncodePng)
: PNG-encode an image.

[`EncodeProto(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EncodeProto)
: The op serializes protobuf messages provided in the input tensors.

[`EncodeWav(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EncodeWav)
: Encode audio data using the WAV file format.

[`EnqueueTPUEmbeddingArbitraryTensorBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EnqueueTPUEmbeddingArbitraryTensorBatch)
: Eases the porting of code that uses tf.nn.embedding\_lookup\_sparse().

[`EnqueueTPUEmbeddingIntegerBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EnqueueTPUEmbeddingIntegerBatch)
: An op that enqueues a list of input batch tensors to TPUEmbedding.

[`EnqueueTPUEmbeddingRaggedTensorBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EnqueueTPUEmbeddingRaggedTensorBatch)
: Eases the porting of code that uses tf.nn.embedding\_lookup().

[`EnqueueTPUEmbeddingSparseBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EnqueueTPUEmbeddingSparseBatch)
: An op that enqueues TPUEmbedding input indices from a SparseTensor.

[`EnqueueTPUEmbeddingSparseTensorBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EnqueueTPUEmbeddingSparseTensorBatch)
: Eases the porting of code that uses tf.nn.embedding\_lookup\_sparse().

[`EnsureShape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EnsureShape)
: Ensures that the tensor's shape matches the expected shape.

[`Enter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Enter)
: Creates or finds a child frame, and makes `data` available to the child frame.

[`Equal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Equal)
: Returns the truth value of (x == y) element-wise.

[`Erf(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Erf)
: Computes the [Gauss error function](https://en.wikipedia.org/wiki/Error_function)
 of `x` element-wise. In statistics, for non-negative values of x, the error function has the following interpretation: for a random variable Y that is normally distributed with mean 0 and variance 1/√2, erf(x) is the probability that Y falls in the range \[−x,x\].

[`Erfc(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Erfc)
: Computes the complementary error function of `x` element-wise.

[`Erfinv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Erfinv)

[`EuclideanNorm(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/EuclideanNorm)
: Computes the euclidean norm of elements across dimensions of a tensor.

[`Exit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Exit)
: Exits the current frame to its parent frame.

[`Exp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Exp)
: Computes exponential of x element-wise. y\=ex.

[`ExpandDims(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExpandDims)
: Inserts a dimension of 1 into a tensor's shape.

[`ExperimentalAssertNextDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalAssertNextDataset)

[`ExperimentalAutoShardDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalAutoShardDataset)
: Creates a dataset that shards the input dataset.

[`ExperimentalBytesProducedStatsDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalBytesProducedStatsDataset)
: Records the bytes size of each element of `input_dataset` in a StatsAggregator.

[`ExperimentalCSVDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalCSVDataset)

[`ExperimentalChooseFastestDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalChooseFastestDataset)

[`ExperimentalDatasetCardinality(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalDatasetCardinality)
: Returns the cardinality of `input_dataset`.

[`ExperimentalDatasetToTFRecord(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalDatasetToTFRecord)
: Writes the given dataset to the given file using the TFRecord format.

[`ExperimentalDenseToSparseBatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalDenseToSparseBatchDataset)
: Creates a dataset that batches input elements into a SparseTensor.

[`ExperimentalDirectedInterleaveDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalDirectedInterleaveDataset)
: A substitute for `InterleaveDataset` on a fixed list of `N` datasets.

[`ExperimentalGroupByReducerDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalGroupByReducerDataset)
: Creates a dataset that computes a group-by on `input_dataset`.

[`ExperimentalGroupByWindowDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalGroupByWindowDataset)
: Creates a dataset that computes a windowed group-by on `input_dataset`.

[`ExperimentalIgnoreErrorsDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalIgnoreErrorsDataset)
: Creates a dataset that contains the elements of `input_dataset` ignoring errors.

[`ExperimentalIteratorGetDevice(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalIteratorGetDevice)
: Returns the name of the device on which `resource` has been placed.

[`ExperimentalLMDBDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalLMDBDataset)

[`ExperimentalLatencyStatsDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalLatencyStatsDataset)
: Records the latency of producing `input_dataset` elements in a StatsAggregator.

[`ExperimentalMapAndBatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalMapAndBatchDataset)
: Creates a dataset that fuses mapping with batching.

[`ExperimentalMapDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalMapDataset)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ExperimentalMatchingFilesDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalMatchingFilesDataset)

[`ExperimentalMaxIntraOpParallelismDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalMaxIntraOpParallelismDataset)
: Creates a dataset that overrides the maximum intra-op parallelism.

[`ExperimentalNonSerializableDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalNonSerializableDataset)

[`ExperimentalParallelInterleaveDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalParallelInterleaveDataset)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ExperimentalParseExampleDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalParseExampleDataset)
: Transforms `input_dataset` containing `Example` protos as vectors of DT\_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

[`ExperimentalPrivateThreadPoolDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalPrivateThreadPoolDataset)
: Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ExperimentalRandomDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalRandomDataset)
: Creates a Dataset that returns pseudorandom numbers.

[`ExperimentalRebatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalRebatchDataset)
: Creates a dataset that changes the batch size.

[`ExperimentalScanDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalScanDataset)
: Creates a dataset successively reduces `f` over the elements of `input_dataset`.

[`ExperimentalSetStatsAggregatorDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalSetStatsAggregatorDataset)

[`ExperimentalSleepDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalSleepDataset)

[`ExperimentalSlidingWindowDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalSlidingWindowDataset)
: Creates a dataset that passes a sliding window over `input_dataset`.

[`ExperimentalSqlDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalSqlDataset)
: Creates a dataset that executes a SQL query and emits rows of the result set.

[`ExperimentalStatsAggregatorHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalStatsAggregatorHandle)
: Creates a statistics manager resource.

[`ExperimentalStatsAggregatorSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalStatsAggregatorSummary)
: Produces a summary of any statistics recorded by the given statistics manager.

[`ExperimentalTakeWhileDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalTakeWhileDataset)
: Creates a dataset that stops iteration when predicate\` is false.

[`ExperimentalThreadPoolDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalThreadPoolDataset)
: Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ExperimentalThreadPoolHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalThreadPoolHandle)
: Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ExperimentalUnbatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalUnbatchDataset)
: A dataset that splits the elements of its input into multiple elements.

[`ExperimentalUniqueDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExperimentalUniqueDataset)
: Creates a dataset that contains the unique elements of `input_dataset`.

[`Expint(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Expint)

[`Expm1(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Expm1)
: Computes `exp(x) - 1` element-wise.

[`ExtractGlimpse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExtractGlimpse)
: Extracts a glimpse from the input tensor.

[`ExtractGlimpseV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExtractGlimpseV2)
: Extracts a glimpse from the input tensor.

[`ExtractImagePatches(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExtractImagePatches)
: Extract `patches` from `images` and put them in the "depth" output dimension.

[`ExtractJpegShape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExtractJpegShape)
: Extract the shape information of a JPEG-encoded image.

[`ExtractVolumePatches(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ExtractVolumePatches)
: Extract `patches` from `input` and put them in the `"depth"` output dimension. 3D extension of `extract_image_patches`.

[`FFT(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FFT)
: Fast Fourier transform.

[`FFT2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FFT2D)
: 2D fast Fourier transform.

[`FFT3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FFT3D)
: 3D fast Fourier transform.

[`FFTND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FFTND)
: ND fast Fourier transform.

[`FIFOQueue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FIFOQueue)
: A queue that produces elements in first-in first-out order.

[`FIFOQueueV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FIFOQueueV2)
: A queue that produces elements in first-in first-out order.

[`Fact(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Fact)
: Output a fact about factorials.

[`FakeParam(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FakeParam)
: This op is used as a placeholder in If branch functions.

[`FakeQuantWithMinMaxArgs(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FakeQuantWithMinMaxArgs)
: Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same shape and type.

[`FakeQuantWithMinMaxArgsGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FakeQuantWithMinMaxArgsGradient)
: Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`FakeQuantWithMinMaxVars(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FakeQuantWithMinMaxVars)
: Fake-quantize the 'inputs' tensor of type float via global float scalars

[`FakeQuantWithMinMaxVarsGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FakeQuantWithMinMaxVarsGradient)
: Compute gradients for a FakeQuantWithMinMaxVars operation.

[`FakeQuantWithMinMaxVarsPerChannel(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FakeQuantWithMinMaxVarsPerChannel)
: Fake-quantize the 'inputs' tensor of type float via per-channel floats

[`FakeQuantWithMinMaxVarsPerChannelGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FakeQuantWithMinMaxVarsPerChannelGradient)
: Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`FakeQueue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FakeQueue)
: Deprecated. Do not use.

[`FileSystemSetConfiguration(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FileSystemSetConfiguration)
: Set configuration of the file system.

[`Fill(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Fill)
: Creates a tensor filled with a scalar value.

[`FilterByLastComponentDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FilterByLastComponentDataset)
: Creates a dataset containing elements of first component of `input_dataset` having true in the last component.

[`FilterDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FilterDataset)
: Creates a dataset containing elements of `input_dataset` matching `predicate`.

[`FinalizeDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FinalizeDataset)
: Creates a dataset by applying [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)
 to `input_dataset`.

[`Fingerprint(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Fingerprint)
: Generates fingerprint values.

[`FixedLengthRecordDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FixedLengthRecordDataset)
: Creates a dataset that emits the records from one or more binary files.

[`FixedLengthRecordDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FixedLengthRecordDatasetV2)

[`FixedLengthRecordReader(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FixedLengthRecordReader)
: A Reader that outputs fixed-length records from a file.

[`FixedLengthRecordReaderV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FixedLengthRecordReaderV2)
: A Reader that outputs fixed-length records from a file.

[`FixedUnigramCandidateSampler(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FixedUnigramCandidateSampler)
: Generates labels for candidate sampling with a learned unigram distribution.

[`FlatMapDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FlatMapDataset)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`Floor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Floor)
: Returns element-wise largest integer not greater than x.

[`FloorDiv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FloorDiv)
: Returns x // y element-wise.

[`FloorMod(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FloorMod)
: Returns element-wise remainder of division.

[`FlushSummaryWriter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FlushSummaryWriter)

[`For(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/For)
: Applies a for loop.

[`FractionalAvgPool(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FractionalAvgPool)
: Performs fractional average pooling on the input.

[`FractionalAvgPoolGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FractionalAvgPoolGrad)
: Computes gradient of the FractionalAvgPool function.

[`FractionalMaxPool(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FractionalMaxPool)
: Performs fractional max pooling on the input.

[`FractionalMaxPoolGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FractionalMaxPoolGrad)
: Computes gradient of the FractionalMaxPool function.

[`FresnelCos(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FresnelCos)

[`FresnelSin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FresnelSin)

[`FusedBatchNorm(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FusedBatchNorm)
: Batch normalization.

[`FusedBatchNormGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FusedBatchNormGrad)
: Gradient for batch normalization.

[`FusedBatchNormGradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FusedBatchNormGradV2)
: Gradient for batch normalization.

[`FusedBatchNormGradV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FusedBatchNormGradV3)
: Gradient for batch normalization.

[`FusedBatchNormV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FusedBatchNormV2)
: Batch normalization.

[`FusedBatchNormV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FusedBatchNormV3)
: Batch normalization.

[`FusedPadConv2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FusedPadConv2D)
: Performs a padding as a preprocess during a convolution.

[`FusedResizeAndPadConv2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/FusedResizeAndPadConv2D)
: Performs a resize and padding as a preprocess during a convolution.

[`GRUBlockCell(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GRUBlockCell)
: Computes the GRU cell forward propagation for 1 time step.

[`GRUBlockCellGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GRUBlockCellGrad)
: Computes the GRU cell back-propagation for 1 time step.

[`Gather(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Gather)
: Gather slices from `params` according to `indices`.

[`GatherNd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GatherNd)
: Gather slices from `params` into a Tensor with shape specified by `indices`.

[`GatherV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GatherV2)
: Gather slices from `params` axis `axis` according to `indices`.

[`GenerateBoundingBoxProposals(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GenerateBoundingBoxProposals)
: This op produces Region of Interests from given bounding boxes(bbox\_deltas) encoded wrt anchors according to eq.2 in arXiv:1506.01497

[`GenerateVocabRemapping(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GenerateVocabRemapping)
: Given a path to new and old vocabulary files, returns a remapping Tensor of

[`GeneratorDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GeneratorDataset)
: Creates a dataset that invokes a function to generate elements.

[`GetElementAtIndex(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GetElementAtIndex)
: Gets the element at the specified index in a dataset.

[`GetMinibatchSplitsWithPhysicalReplica(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GetMinibatchSplitsWithPhysicalReplica)

[`GetMinibatchesInCsrWithPhysicalReplica(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GetMinibatchesInCsrWithPhysicalReplica)

[`GetOptions(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GetOptions)
: Returns the [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)
 attached to `input_dataset`.

[`GetSessionHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GetSessionHandle)
: Store the input tensor in the state of the current session.

[`GetSessionHandleV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GetSessionHandleV2)
: Store the input tensor in the state of the current session.

[`GetSessionTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GetSessionTensor)
: Get the value of the tensor specified by its handle.

[`GetStatsFromListOfSparseCoreCooTensors(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GetStatsFromListOfSparseCoreCooTensors)

[`GlobalIterId(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GlobalIterId)

[`GlobalShuffleDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GlobalShuffleDataset)

[`Greater(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Greater)
: Returns the truth value of (x > y) element-wise.

[`GreaterEqual(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GreaterEqual)
: Returns the truth value of (x >= y) element-wise.

[`GroupByReducerDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GroupByReducerDataset)
: Creates a dataset that computes a group-by on `input_dataset`.

[`GroupByWindowDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GroupByWindowDataset)
: Creates a dataset that computes a windowed group-by on `input_dataset`.

[`GuaranteeConst(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/GuaranteeConst)
: Gives a guarantee to the TF runtime that the input tensor is a constant.

[`HSVToRGB(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/HSVToRGB)
: Convert one or more images from HSV to RGB.

[`HashTable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/HashTable)
: Creates a non-initialized hash table.

[`HashTableV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/HashTableV2)
: Creates a non-initialized hash table.

[`HistogramFixedWidth(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/HistogramFixedWidth)
: Return histogram of values.

[`HistogramSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/HistogramSummary)
: Outputs a `Summary` protocol buffer with a histogram.

[`IFFT(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IFFT)
: Inverse fast Fourier transform.

[`IFFT2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IFFT2D)
: Inverse 2D fast Fourier transform.

[`IFFT3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IFFT3D)
: Inverse 3D fast Fourier transform.

[`IFFTND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IFFTND)
: ND inverse fast Fourier transform.

[`IRFFT(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IRFFT)
: Inverse real-valued fast Fourier transform.

[`IRFFT2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IRFFT2D)
: Inverse 2D real-valued fast Fourier transform.

[`IRFFT3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IRFFT3D)
: Inverse 3D real-valued fast Fourier transform.

[`IRFFTND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IRFFTND)
: ND inverse real fast Fourier transform.

[`Identity(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Identity)
: Return a tensor with the same shape and contents as the input tensor or value.

[`IdentityN(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IdentityN)
: Returns a list of tensors with the same shapes and contents as the input

[`IdentityReader(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IdentityReader)
: A Reader that outputs the queued work as both the key and value.

[`IdentityReaderV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IdentityReaderV2)
: A Reader that outputs the queued work as both the key and value.

[`If(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/If)
: output = cond ? then\_branch(input) : else\_branch(input)

[`Igamma(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Igamma)
: Compute the lower regularized incomplete Gamma function `P(a, x)`.

[`IgammaGradA(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IgammaGradA)
: Computes the gradient of `igamma(a, x)` wrt `a`.

[`Igammac(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Igammac)
: Compute the upper regularized incomplete Gamma function `Q(a, x)`.

[`IgnoreErrorsDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IgnoreErrorsDataset)
: Creates a dataset that contains the elements of `input_dataset` ignoring errors.

[`Imag(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Imag)
: Returns the imaginary part of a complex number.

[`ImageProjectiveTransformV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ImageProjectiveTransformV2)
: Applies the given transform to each of the images.

[`ImageProjectiveTransformV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ImageProjectiveTransformV3)
: Applies the given transform to each of the images.

[`ImageSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ImageSummary)
: Outputs a `Summary` protocol buffer with images.

[`ImmutableConst(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ImmutableConst)
: Returns immutable tensor from memory region.

[`ImportEvent(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ImportEvent)

[`InTopK(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InTopK)
: Says whether the targets are in the top `K` predictions.

[`InTopKV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InTopKV2)
: Says whether the targets are in the top `K` predictions.

[`IndexFlatMapDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IndexFlatMapDataset)

[`InfeedDequeue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InfeedDequeue)
: A placeholder op for a value that will be fed into the computation.

[`InfeedDequeueTuple(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InfeedDequeueTuple)
: Fetches multiple values from infeed as an XLA tuple.

[`InfeedEnqueue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InfeedEnqueue)
: An op which feeds a single Tensor value into the computation.

[`InfeedEnqueuePrelinearizedBuffer(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InfeedEnqueuePrelinearizedBuffer)
: An op which enqueues prelinearized buffer into TPU infeed.

[`InfeedEnqueueTuple(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InfeedEnqueueTuple)
: Feeds multiple Tensor values into the computation as an XLA tuple.

[`InitializeTable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InitializeTable)
: Table initializer that takes two tensors for keys and values respectively.

[`InitializeTableFromDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InitializeTableFromDataset)

[`InitializeTableFromTextFile(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InitializeTableFromTextFile)
: Initializes a table from a text file.

[`InitializeTableFromTextFileV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InitializeTableFromTextFileV2)
: Initializes a table from a text file.

[`InitializeTableV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InitializeTableV2)
: Table initializer that takes two tensors for keys and values respectively.

[`InplaceAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InplaceAdd)
: Adds v into specified rows of x.

[`InplaceSub(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InplaceSub)
: Subtracts `v` into specified rows of `x`.

[`InplaceUpdate(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InplaceUpdate)
: Updates specified rows 'i' with values 'v'.

[`InterleaveDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InterleaveDataset)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`Inv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Inv)
: Computes the reciprocal of x element-wise.

[`InvGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InvGrad)
: Computes the gradient for the inverse of `x` wrt its input.

[`Invert(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Invert)
: Invert (flip) each bit of supported types; for example, type `uint8` value 01010101 becomes 10101010.

[`InvertPermutation(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/InvertPermutation)
: Computes the inverse permutation of a tensor.

[`IsBoostedTreesEnsembleInitialized(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IsBoostedTreesEnsembleInitialized)
: Checks whether a tree ensemble has been initialized.

[`IsBoostedTreesQuantileStreamResourceInitialized(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IsBoostedTreesQuantileStreamResourceInitialized)
: Checks whether a quantile stream has been initialized.

[`IsFinite(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IsFinite)
: Returns which elements of x are finite.

[`IsInf(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IsInf)
: Returns which elements of x are Inf.

[`IsNan(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IsNan)
: Returns which elements of x are NaN.

[`IsTPUEmbeddingInitialized(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IsTPUEmbeddingInitialized)
: Whether TPU Embedding is initialized in a distributed TPU system.

[`IsVariableInitialized(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IsVariableInitialized)
: Checks whether a tensor has been initialized.

[`IsotonicRegression(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IsotonicRegression)
: Solves a batch of isotonic regression problems.

[`Iterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Iterator)
: A container for an iterator resource.

[`IteratorFromStringHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorFromStringHandle)
: Converts the given string representing a handle to an iterator to a resource.

[`IteratorFromStringHandleV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorFromStringHandleV2)

[`IteratorGetDevice(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorGetDevice)
: Returns the name of the device on which `resource` has been placed.

[`IteratorGetModelProto(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorGetModelProto)
: Returns the serialized model proto of an iterator resource.

[`IteratorGetNext(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorGetNext)
: Gets the next output from the given iterator .

[`IteratorGetNextAsOptional(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorGetNextAsOptional)
: Gets the next output from the given iterator as an Optional variant.

[`IteratorGetNextSync(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorGetNextSync)
: Gets the next output from the given iterator.

[`IteratorToStringHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorToStringHandle)
: Converts the given `resource_handle` representing an iterator to a string.

[`IteratorV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/IteratorV2)

[`KMC2ChainInitialization(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/KMC2ChainInitialization)
: Returns the index of a data point that should be added to the seed set.

[`KmeansPlusPlusInitialization(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/KmeansPlusPlusInitialization)
: Selects num\_to\_sample rows of input using the KMeans++ criterion.

[`L2Loss(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/L2Loss)
: L2 Loss.

[`LMDBDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LMDBDataset)
: Creates a dataset that emits the key-value pairs in one or more LMDB files.

[`LMDBReader(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LMDBReader)
: A Reader that outputs the records from a LMDB file.

[`LRN(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LRN)
: Local Response Normalization.

[`LRNGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LRNGrad)
: Gradients for Local Response Normalization.

[`LSTMBlockCell(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LSTMBlockCell)
: Computes the LSTM cell forward propagation for 1 time step.

[`LSTMBlockCellGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LSTMBlockCellGrad)
: Computes the LSTM cell backward propagation for 1 timestep.

[`LatencyStatsDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LatencyStatsDataset)
: Records the latency of producing `input_dataset` elements in a StatsAggregator.

[`LeakyRelu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LeakyRelu)
: Computes rectified linear: `max(features, features * alpha)`.

[`LeakyReluGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LeakyReluGrad)
: Computes rectified linear gradients for a LeakyRelu operation.

[`LearnedUnigramCandidateSampler(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LearnedUnigramCandidateSampler)
: Generates labels for candidate sampling with a learned unigram distribution.

[`LeftShift(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LeftShift)
: Elementwise computes the bitwise left-shift of `x` and `y`.

[`LegacyParallelInterleaveDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LegacyParallelInterleaveDatasetV2)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`Less(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Less)
: Returns the truth value of (x < y) element-wise.

[`LessEqual(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LessEqual)
: Returns the truth value of (x <= y) element-wise.

[`Lgamma(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Lgamma)
: Computes the log of the absolute value of `Gamma(x)` element-wise.

[`LinSpace(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LinSpace)
: Generates values in an interval.

[`ListDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ListDataset)
: Creates a dataset that emits each of `tensors` once.

[`ListDiff(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ListDiff)
: Computes the difference between two lists of numbers or strings.

[`ListSnapshotChunksDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ListSnapshotChunksDataset)

[`LoadAndRemapMatrix(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadAndRemapMatrix)
: Loads a 2-D (matrix) `Tensor` with name `old_tensor_name` from the checkpoint

[`LoadDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadDataset)

[`LoadTPUEmbeddingADAMParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingADAMParameters)
: Load ADAM embedding parameters.

[`LoadTPUEmbeddingAdadeltaParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingAdadeltaParameters)
: Load Adadelta embedding parameters.

[`LoadTPUEmbeddingAdagradMomentumParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingAdagradMomentumParameters)
: Load Adagrad Momentum embedding parameters.

[`LoadTPUEmbeddingAdagradParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingAdagradParameters)
: Load Adagrad embedding parameters.

[`LoadTPUEmbeddingCenteredRMSPropParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingCenteredRMSPropParameters)
: Load centered RMSProp embedding parameters.

[`LoadTPUEmbeddingFTRLParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingFTRLParameters)
: Load FTRL embedding parameters.

[`LoadTPUEmbeddingFrequencyEstimatorParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingFrequencyEstimatorParameters)
: Load frequency estimator embedding parameters.

[`LoadTPUEmbeddingMDLAdagradLightParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingMDLAdagradLightParameters)
: Load MDL Adagrad Light embedding parameters.

[`LoadTPUEmbeddingMomentumParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingMomentumParameters)
: Load Momentum embedding parameters.

[`LoadTPUEmbeddingProximalAdagradParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingProximalAdagradParameters)
: Load proximal Adagrad embedding parameters.

[`LoadTPUEmbeddingProximalYogiParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingProximalYogiParameters)

[`LoadTPUEmbeddingRMSPropParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingRMSPropParameters)
: Load RMSProp embedding parameters.

[`LoadTPUEmbeddingStochasticGradientDescentParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoadTPUEmbeddingStochasticGradientDescentParameters)
: Load SGD embedding parameters.

[`Log(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Log)
: Computes natural logarithm of x element-wise.

[`Log1p(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Log1p)
: Computes natural logarithm of (1 + x) element-wise.

[`LogMatrixDeterminant(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LogMatrixDeterminant)
: Computes the sign and the log of the absolute value of the determinant of

[`LogSoftmax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LogSoftmax)
: Computes log softmax activations.

[`LogUniformCandidateSampler(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LogUniformCandidateSampler)
: Generates labels for candidate sampling with a log-uniform distribution.

[`LogicalAnd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LogicalAnd)
: Returns the truth value of x AND y element-wise.

[`LogicalNot(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LogicalNot)
: Returns the truth value of `NOT x` element-wise.

[`LogicalOr(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LogicalOr)
: Returns the truth value of x OR y element-wise.

[`LookupTableExport(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableExport)
: Outputs all keys and values in the table.

[`LookupTableExportV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableExportV2)
: Outputs all keys and values in the table.

[`LookupTableFind(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableFind)
: Looks up keys in a table, outputs the corresponding values.

[`LookupTableFindV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableFindV2)
: Looks up keys in a table, outputs the corresponding values.

[`LookupTableImport(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableImport)
: Replaces the contents of the table with the specified keys and values.

[`LookupTableImportV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableImportV2)
: Replaces the contents of the table with the specified keys and values.

[`LookupTableInsert(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableInsert)
: Updates the table to associates keys with values.

[`LookupTableInsertV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableInsertV2)
: Updates the table to associates keys with values.

[`LookupTableRemoveV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableRemoveV2)
: Removes keys and its associated values from a table.

[`LookupTableSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableSize)
: Computes the number of elements in the given table.

[`LookupTableSizeV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LookupTableSizeV2)
: Computes the number of elements in the given table.

[`LoopCond(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LoopCond)
: Forwards the input to the output.

[`LowerBound(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/LowerBound)
: Applies lower\_bound(sorted\_search\_values, values) along each row.

[`Lu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Lu)
: Computes the LU decomposition of one or more square matrices.

[`MakeIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MakeIterator)
: Makes a new iterator from the given `dataset` and stores it in `iterator`.

[`MapAndBatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapAndBatchDataset)
: Creates a dataset that fuses mapping with batching.

[`MapClear(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapClear)
: Op removes all elements in the underlying container.

[`MapDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapDataset)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`MapDefun(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapDefun)
: Maps a function on the list of tensors unpacked from arguments on dimension 0.

[`MapIncompleteSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapIncompleteSize)
: Op returns the number of incomplete elements in the underlying container.

[`MapPeek(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapPeek)
: Op peeks at the values at the specified key.

[`MapSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapSize)
: Op returns the number of elements in the underlying container.

[`MapStage(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapStage)
: Stage (key, values) in the underlying container which behaves like a hashtable.

[`MapUnstage(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapUnstage)
: Op removes and returns the values associated with the key

[`MapUnstageNoKey(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MapUnstageNoKey)
: Op removes and returns a random (key, value)

[`MatMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatMul)
: Multiply the matrix "a" by the matrix "b".

[`MatchingFiles(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatchingFiles)
: Returns the set of files matching one or more glob patterns.

[`MatchingFilesDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatchingFilesDataset)

[`MatrixBandPart(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixBandPart)
: Copy a tensor setting everything outside a central band in each innermost matrix to zero.

[`MatrixDeterminant(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixDeterminant)
: Computes the determinant of one or more square matrices.

[`MatrixDiag(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixDiag)
: Returns a batched diagonal tensor with a given batched diagonal values.

[`MatrixDiagPart(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixDiagPart)
: Returns the batched diagonal part of a batched tensor.

[`MatrixDiagPartV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixDiagPartV2)
: Returns the batched diagonal part of a batched tensor.

[`MatrixDiagPartV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixDiagPartV3)
: Returns the batched diagonal part of a batched tensor.

[`MatrixDiagV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixDiagV2)
: Returns a batched diagonal tensor with given batched diagonal values.

[`MatrixDiagV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixDiagV3)
: Returns a batched diagonal tensor with given batched diagonal values.

[`MatrixExponential(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixExponential)
: Deprecated, use python implementation tf.linalg.matrix\_exponential.

[`MatrixInverse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixInverse)
: Computes the inverse of one or more square invertible matrices or their adjoints (conjugate transposes).

[`MatrixLogarithm(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixLogarithm)
: Computes the matrix logarithm of one or more square matrices:

[`MatrixSetDiag(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixSetDiag)
: Returns a batched matrix tensor with new batched diagonal values.

[`MatrixSetDiagV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixSetDiagV2)
: Returns a batched matrix tensor with new batched diagonal values.

[`MatrixSetDiagV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixSetDiagV3)
: Returns a batched matrix tensor with new batched diagonal values.

[`MatrixSolve(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixSolve)
: Solves systems of linear equations.

[`MatrixSolveLs(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixSolveLs)
: Solves one or more linear least-squares problems.

[`MatrixSquareRoot(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixSquareRoot)
: Computes the matrix square root of one or more square matrices:

[`MatrixTriangularSolve(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MatrixTriangularSolve)
: Solves systems of linear equations with upper or lower triangular matrices by backsubstitution.

[`Max(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Max)
: Computes the maximum of elements across dimensions of a tensor.

[`MaxIntraOpParallelismDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxIntraOpParallelismDataset)
: Creates a dataset that overrides the maximum intra-op parallelism.

[`MaxPool(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPool)
: Performs max pooling on the input.

[`MaxPool3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPool3D)
: Performs 3D max pooling on the input.

[`MaxPool3DGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPool3DGrad)
: Computes gradients of 3D max pooling function.

[`MaxPool3DGradGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPool3DGradGrad)
: Computes second-order gradients of the maxpooling function.

[`MaxPoolGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPoolGrad)
: Computes gradients of the maxpooling function.

[`MaxPoolGradGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPoolGradGrad)
: Computes second-order gradients of the maxpooling function.

[`MaxPoolGradGradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPoolGradGradV2)
: Computes second-order gradients of the maxpooling function.

[`MaxPoolGradGradWithArgmax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPoolGradGradWithArgmax)
: Computes second-order gradients of the maxpooling function.

[`MaxPoolGradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPoolGradV2)
: Computes gradients of the maxpooling function.

[`MaxPoolGradWithArgmax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPoolGradWithArgmax)
: Computes gradients of the maxpooling function.

[`MaxPoolV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPoolV2)
: Performs max pooling on the input.

[`MaxPoolWithArgmax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MaxPoolWithArgmax)
: Performs max pooling on the input and outputs both max values and indices.

[`Maximum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Maximum)
: Returns the max of x and y (i.e. x > y ? x : y) element-wise.

[`Mean(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Mean)
: Computes the mean of elements across dimensions of a tensor.

[`Merge(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Merge)
: Forwards the value of an available tensor from `inputs` to `output`.

[`MergeSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MergeSummary)
: Merges summaries.

[`MergeV2Checkpoints(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MergeV2Checkpoints)
: V2 format specific: merges the metadata files of sharded checkpoints.

[`Mfcc(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Mfcc)
: Transforms a spectrogram into a form that's useful for speech recognition.

[`Min(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Min)
: Computes the minimum of elements across dimensions of a tensor.

[`Minimum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Minimum)
: Returns the min of x and y (i.e. x < y ? x : y) element-wise.

[`MirrorPad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MirrorPad)
: Pads a tensor with mirrored values.

[`MirrorPadGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MirrorPadGrad)
: Gradient op for `MirrorPad` op. This op folds a mirror-padded tensor.

[`Mod(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Mod)
: Returns element-wise remainder of division.

[`ModelDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ModelDataset)
: Identity transformation that models performance.

[`Mul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Mul)
: Returns x \* y element-wise.

[`MulNoNan(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MulNoNan)
: Returns x \* y element-wise. Returns zero if y is zero, even if x if infinite or NaN.

[`MultiDeviceIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MultiDeviceIterator)
: Creates a MultiDeviceIterator resource.

[`MultiDeviceIteratorFromStringHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MultiDeviceIteratorFromStringHandle)
: Generates a MultiDeviceIterator resource from its provided string handle.

[`MultiDeviceIteratorGetNextFromShard(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MultiDeviceIteratorGetNextFromShard)
: Gets next element for the provided shard number.

[`MultiDeviceIteratorInit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MultiDeviceIteratorInit)
: Initializes the multi device iterator with the given dataset.

[`MultiDeviceIteratorToStringHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MultiDeviceIteratorToStringHandle)
: Produces a string handle for the given MultiDeviceIterator.

[`Multinomial(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Multinomial)
: Draws samples from a multinomial distribution.

[`MutableDenseHashTable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MutableDenseHashTable)
: Creates an empty hash table that uses tensors as the backing store.

[`MutableDenseHashTableV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MutableDenseHashTableV2)
: Creates an empty hash table that uses tensors as the backing store.

[`MutableHashTable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MutableHashTable)
: Creates an empty hash table.

[`MutableHashTableOfTensors(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MutableHashTableOfTensors)
: Creates an empty hash table.

[`MutableHashTableOfTensorsV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MutableHashTableOfTensorsV2)
: Creates an empty hash table.

[`MutableHashTableV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MutableHashTableV2)
: Creates an empty hash table.

[`MutexLock(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MutexLock)
: Locks a mutex resource.

[`MutexV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/MutexV2)
: Creates a Mutex resource that can be locked by `MutexLock`.

[`NcclAllReduce(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NcclAllReduce)
: Outputs a tensor containing the reduction across all input tensors.

[`NcclBroadcast(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NcclBroadcast)
: Sends `input` to all devices that are connected to the output.

[`NcclReduce(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NcclReduce)
: Reduces `input` from `num_devices` using `reduction` to a single device.

[`Ndtri(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Ndtri)

[`NearestNeighbors(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NearestNeighbors)
: Selects the k nearest centers for each point.

[`Neg(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Neg)
: Computes numerical negative value element-wise.

[`NextAfter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NextAfter)
: Returns the next representable value of `x1` in the direction of `x2`, element-wise.

[`NextIteration(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NextIteration)
: Makes its input available to the next iteration.

[`NoOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NoOp)
: Does nothing. Only useful as a placeholder for control edges.

[`NonDeterministicInts(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NonDeterministicInts)
: Non-deterministically generates some integers.

[`NonMaxSuppression(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NonMaxSuppression)
: Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NonMaxSuppressionV2)
: Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NonMaxSuppressionV3)
: Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionV4(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NonMaxSuppressionV4)
: Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionV5(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NonMaxSuppressionV5)
: Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionWithOverlaps(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NonMaxSuppressionWithOverlaps)
: Greedily selects a subset of bounding boxes in descending order of score,

[`NonSerializableDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NonSerializableDataset)

[`NotEqual(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NotEqual)
: Returns the truth value of (x != y) element-wise.

[`NthElement(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/NthElement)
: Finds values of the `n`\-th order statistic for the last dimension.

[`OneHot(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OneHot)
: Returns a one-hot tensor.

[`OneShotIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OneShotIterator)
: Makes a "one-shot" iterator that can be iterated only once.

[`OnesLike(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OnesLike)
: Returns a tensor of ones with the same shape and type as x.

[`OptimizeDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OptimizeDataset)
: Creates a dataset by applying optimizations to `input_dataset`.

[`OptimizeDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OptimizeDatasetV2)
: Creates a dataset by applying related optimizations to `input_dataset`.

[`OptionalFromValue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OptionalFromValue)
: Constructs an Optional variant from a tuple of tensors.

[`OptionalGetValue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OptionalGetValue)
: Returns the value stored in an Optional variant or raises an error if none exists.

[`OptionalHasValue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OptionalHasValue)
: Returns true if and only if the given Optional variant has a value.

[`OptionalNone(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OptionalNone)
: Creates an Optional variant with no value.

[`OptionsDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OptionsDataset)
: Creates a dataset by attaching tf.data.Options to `input_dataset`.

[`OrderedMapClear(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OrderedMapClear)
: Op removes all elements in the underlying container.

[`OrderedMapIncompleteSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OrderedMapIncompleteSize)
: Op returns the number of incomplete elements in the underlying container.

[`OrderedMapPeek(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OrderedMapPeek)
: Op peeks at the values at the specified key.

[`OrderedMapSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OrderedMapSize)
: Op returns the number of elements in the underlying container.

[`OrderedMapStage(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OrderedMapStage)
: Stage (key, values) in the underlying container which behaves like a ordered

[`OrderedMapUnstage(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OrderedMapUnstage)
: Op removes and returns the values associated with the key

[`OrderedMapUnstageNoKey(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OrderedMapUnstageNoKey)
: Op removes and returns the (key, value) element with the smallest

[`OutfeedDequeue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OutfeedDequeue)
: Retrieves a single tensor from the computation outfeed.

[`OutfeedDequeueTuple(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OutfeedDequeueTuple)
: Retrieve multiple values from the computation outfeed.

[`OutfeedDequeueTupleV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OutfeedDequeueTupleV2)
: Retrieve multiple values from the computation outfeed.

[`OutfeedDequeueV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OutfeedDequeueV2)
: Retrieves a single tensor from the computation outfeed.

[`OutfeedEnqueue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OutfeedEnqueue)
: Enqueue a Tensor on the computation outfeed.

[`OutfeedEnqueueTuple(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/OutfeedEnqueueTuple)
: Enqueue multiple Tensor values on the computation outfeed.

[`Pack(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Pack)
: Packs a list of `N` rank-`R` tensors into one rank-`(R+1)` tensor.

[`Pad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Pad)
: Pads a tensor with zeros.

[`PadV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PadV2)
: Pads a tensor.

[`PaddedBatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PaddedBatchDataset)
: Creates a dataset that batches and pads `batch_size` elements from the input.

[`PaddedBatchDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PaddedBatchDatasetV2)
: Creates a dataset that batches and pads `batch_size` elements from the input.

[`PaddingFIFOQueue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PaddingFIFOQueue)
: A queue that produces elements in first-in first-out order.

[`PaddingFIFOQueueV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PaddingFIFOQueueV2)
: A queue that produces elements in first-in first-out order.

[`ParallelBatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelBatchDataset)

[`ParallelConcat(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelConcat)
: Concatenates a list of `N` tensors along the first dimension.

[`ParallelDynamicStitch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelDynamicStitch)
: Interleave the values from the `data` tensors into a single tensor.

[`ParallelFilterDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelFilterDataset)
: Creates a dataset containing elements of `input_dataset` matching `predicate`.

[`ParallelInterleaveDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelInterleaveDataset)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelInterleaveDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelInterleaveDatasetV2)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelInterleaveDatasetV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelInterleaveDatasetV3)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelInterleaveDatasetV4(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelInterleaveDatasetV4)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelMapDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelMapDataset)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelMapDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParallelMapDatasetV2)
: Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParameterizedTruncatedNormal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParameterizedTruncatedNormal)
: Outputs random values from a normal distribution.

[`ParseExample(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseExample)
: Transforms a vector of brain.Example protos (as strings) into typed tensors.

[`ParseExampleDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseExampleDataset)
: Transforms `input_dataset` containing `Example` protos as vectors of DT\_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

[`ParseExampleDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseExampleDatasetV2)
: Transforms `input_dataset` containing `Example` protos as vectors of DT\_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

[`ParseExampleV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseExampleV2)
: Transforms a vector of tf.Example protos (as strings) into typed tensors.

[`ParseSequenceExample(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseSequenceExample)
: Transforms a vector of brain.SequenceExample protos (as strings) into typed tensors.

[`ParseSequenceExampleV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseSequenceExampleV2)
: Transforms a vector of tf.io.SequenceExample protos (as strings) into typed tensors.

[`ParseSingleExample(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseSingleExample)
: Transforms a tf.Example proto (as a string) into typed tensors.

[`ParseSingleSequenceExample(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseSingleSequenceExample)
: Transforms a scalar brain.SequenceExample proto (as strings) into typed tensors.

[`ParseTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ParseTensor)
: Transforms a serialized tensorflow.TensorProto proto into a Tensor.

[`PartitionedCall(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PartitionedCall)
: returns `f(inputs)`, where `f`'s body is placed and partitioned.

[`Placeholder(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Placeholder)
: A placeholder op for a value that will be fed into the computation.

[`PlaceholderV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PlaceholderV2)
: A placeholder op for a value that will be fed into the computation.

[`PlaceholderWithDefault(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PlaceholderWithDefault)
: A placeholder op that passes through `input` when its output is not fed.

[`Polygamma(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Polygamma)
: Compute the polygamma function ψ(n)(x).

[`PopulationCount(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PopulationCount)
: Computes element-wise population count (a.k.a. popcount, bitsum, bitcount).

[`Pow(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Pow)
: Computes the power of one value to another.

[`PrefetchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PrefetchDataset)
: Creates a dataset that asynchronously prefetches elements from `input_dataset`.

[`Prelinearize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Prelinearize)
: An op which linearizes one Tensor value to an opaque variant tensor.

[`PrelinearizeTuple(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PrelinearizeTuple)
: An op which linearizes multiple Tensor values to an opaque variant tensor.

[`PreventGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PreventGradient)
: An identity op that triggers an error if a gradient is requested.

[`Print(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Print)
: Prints a list of tensors.

[`PrintV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PrintV2)
: Prints a string scalar.

[`PriorityQueue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PriorityQueue)
: A queue that produces elements sorted by the first component value.

[`PriorityQueueV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PriorityQueueV2)
: A queue that produces elements sorted by the first component value.

[`PrivateThreadPoolDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PrivateThreadPoolDataset)
: Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`Prod(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Prod)
: Computes the product of elements across dimensions of a tensor.

[`PyFunc(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PyFunc)
: Invokes a python function to compute func(input)->output.

[`PyFuncStateless(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PyFuncStateless)
: A stateless version of PyFunc.

[`Qr(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Qr)
: Computes the QR decompositions of one or more matrices.

[`QuantizeAndDequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizeAndDequantize)
: Use QuantizeAndDequantizeV2 instead.

[`QuantizeAndDequantizeV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV2)
: Quantizes then dequantizes a tensor.

[`QuantizeAndDequantizeV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV3)
: Quantizes then dequantizes a tensor.

[`QuantizeAndDequantizeV4(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV4)
: Quantizes then dequantizes a tensor.

[`QuantizeAndDequantizeV4Grad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV4Grad)
: Returns the gradient of `QuantizeAndDequantizeV4`.

[`QuantizeDownAndShrinkRange(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizeDownAndShrinkRange)
: Convert the quantized 'input' tensor into a lower-precision 'output', using the

[`QuantizeV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizeV2)
: Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

[`QuantizedAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedAdd)
: Returns x + y element-wise, working on quantized buffers.

[`QuantizedAvgPool(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedAvgPool)
: Produces the average pool of the input tensor for quantized types.

[`QuantizedBatchNormWithGlobalNormalization(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedBatchNormWithGlobalNormalization)
: Quantized Batch normalization.

[`QuantizedBiasAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedBiasAdd)
: Adds Tensor 'bias' to Tensor 'input' for Quantized types.

[`QuantizedConcat(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConcat)
: Concatenates quantized tensors along one dimension.

[`QuantizedConv2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2D)
: Computes a 2D convolution given quantized 4D input and filter tensors.

[`QuantizedConv2DAndRelu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DAndRelu)

[`QuantizedConv2DAndReluAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DAndReluAndRequantize)

[`QuantizedConv2DAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DAndRequantize)

[`QuantizedConv2DPerChannel(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DPerChannel)
: Computes QuantizedConv2D per channel.

[`QuantizedConv2DWithBias(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DWithBias)

[`QuantizedConv2DWithBiasAndRelu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DWithBiasAndRelu)

[`QuantizedConv2DWithBiasAndReluAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DWithBiasAndReluAndRequantize)

[`QuantizedConv2DWithBiasAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DWithBiasAndRequantize)

[`QuantizedConv2DWithBiasSignedSumAndReluAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DWithBiasSignedSumAndReluAndRequantize)

[`QuantizedConv2DWithBiasSumAndRelu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DWithBiasSumAndRelu)

[`QuantizedConv2DWithBiasSumAndReluAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedConv2DWithBiasSumAndReluAndRequantize)

[`QuantizedDepthwiseConv2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedDepthwiseConv2D)
: Computes quantized depthwise Conv2D.

[`QuantizedDepthwiseConv2DWithBias(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedDepthwiseConv2DWithBias)
: Computes quantized depthwise Conv2D with Bias.

[`QuantizedDepthwiseConv2DWithBiasAndRelu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedDepthwiseConv2DWithBiasAndRelu)
: Computes quantized depthwise Conv2D with Bias and Relu.

[`QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize)
: Computes quantized depthwise Conv2D with Bias, Relu and Requantize.

[`QuantizedInstanceNorm(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedInstanceNorm)
: Quantized Instance normalization.

[`QuantizedMatMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedMatMul)
: Perform a quantized matrix multiplication of `a` by the matrix `b`.

[`QuantizedMatMulWithBias(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedMatMulWithBias)
: Performs a quantized matrix multiplication of `a` by the matrix `b` with bias add.

[`QuantizedMatMulWithBiasAndDequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedMatMulWithBiasAndDequantize)

[`QuantizedMatMulWithBiasAndRelu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedMatMulWithBiasAndRelu)
: Perform a quantized matrix multiplication of `a` by the matrix `b` with bias add and relu fusion.

[`QuantizedMatMulWithBiasAndReluAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedMatMulWithBiasAndReluAndRequantize)
: Perform a quantized matrix multiplication of `a` by the matrix `b` with bias add and relu and requantize fusion.

[`QuantizedMatMulWithBiasAndRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedMatMulWithBiasAndRequantize)

[`QuantizedMaxPool(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedMaxPool)
: Produces the max pool of the input tensor for quantized types.

[`QuantizedMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedMul)
: Returns x \* y element-wise, working on quantized buffers.

[`QuantizedRelu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedRelu)
: Computes Quantized Rectified Linear: `max(features, 0)`

[`QuantizedRelu6(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedRelu6)
: Computes Quantized Rectified Linear 6: `min(max(features, 0), 6)`

[`QuantizedReluX(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedReluX)
: Computes Quantized Rectified Linear X: `min(max(features, 0), max_value)`

[`QuantizedReshape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedReshape)
: Reshapes a quantized tensor as per the Reshape op.

[`QuantizedResizeBilinear(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QuantizedResizeBilinear)
: Resize quantized `images` to `size` using quantized bilinear interpolation.

[`QueueClose(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueClose)
: Closes the given queue.

[`QueueCloseV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueCloseV2)
: Closes the given queue.

[`QueueDequeue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueDequeue)
: Dequeues a tuple of one or more tensors from the given queue.

[`QueueDequeueMany(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueDequeueMany)
: Dequeues `n` tuples of one or more tensors from the given queue.

[`QueueDequeueManyV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueDequeueManyV2)
: Dequeues `n` tuples of one or more tensors from the given queue.

[`QueueDequeueUpTo(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueDequeueUpTo)
: Dequeues `n` tuples of one or more tensors from the given queue.

[`QueueDequeueUpToV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueDequeueUpToV2)
: Dequeues `n` tuples of one or more tensors from the given queue.

[`QueueDequeueV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueDequeueV2)
: Dequeues a tuple of one or more tensors from the given queue.

[`QueueEnqueue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueEnqueue)
: Enqueues a tuple of one or more tensors in the given queue.

[`QueueEnqueueMany(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueEnqueueMany)
: Enqueues zero or more tuples of one or more tensors in the given queue.

[`QueueEnqueueManyV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueEnqueueManyV2)
: Enqueues zero or more tuples of one or more tensors in the given queue.

[`QueueEnqueueV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueEnqueueV2)
: Enqueues a tuple of one or more tensors in the given queue.

[`QueueIsClosed(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueIsClosed)
: Returns true if queue is closed.

[`QueueIsClosedV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueIsClosedV2)
: Returns true if queue is closed.

[`QueueSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueSize)
: Computes the number of elements in the given queue.

[`QueueSizeV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/QueueSizeV2)
: Computes the number of elements in the given queue.

[`RFFT(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RFFT)
: Real-valued fast Fourier transform.

[`RFFT2D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RFFT2D)
: 2D real-valued fast Fourier transform.

[`RFFT3D(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RFFT3D)
: 3D real-valued fast Fourier transform.

[`RFFTND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RFFTND)
: ND fast real Fourier transform.

[`RGBToHSV(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RGBToHSV)
: Converts one or more images from RGB to HSV.

[`RaggedBincount(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedBincount)
: Counts the number of occurrences of each value in an integer array.

[`RaggedCountSparseOutput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedCountSparseOutput)
: Performs sparse-output bin counting for a ragged tensor input.

[`RaggedCross(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedCross)
: Generates a feature cross from a list of tensors, and returns it as a RaggedTensor.

[`RaggedFillEmptyRows(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedFillEmptyRows)

[`RaggedFillEmptyRowsGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedFillEmptyRowsGrad)

[`RaggedGather(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedGather)
: Gather ragged slices from `params` axis `0` according to `indices`.

[`RaggedRange(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedRange)
: Returns a `RaggedTensor` containing the specified sequences of numbers.

[`RaggedTensorFromVariant(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedTensorFromVariant)
: Decodes a `variant` Tensor into a `RaggedTensor`.

[`RaggedTensorToSparse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedTensorToSparse)
: Converts a `RaggedTensor` into a `SparseTensor` with the same values.

[`RaggedTensorToTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedTensorToTensor)
: Create a dense tensor from a ragged tensor, possibly altering its shape.

[`RaggedTensorToVariant(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedTensorToVariant)
: Encodes a `RaggedTensor` into a `variant` Tensor.

[`RaggedTensorToVariantGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RaggedTensorToVariantGradient)
: Helper used to compute the gradient for `RaggedTensorToVariant`.

[`RandomCrop(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomCrop)
: Randomly crop `image`.

[`RandomDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomDataset)
: Creates a Dataset that returns pseudorandom numbers.

[`RandomDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomDatasetV2)
: Creates a Dataset that returns pseudorandom numbers.

[`RandomGamma(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomGamma)
: Outputs random values from the Gamma distribution(s) described by alpha.

[`RandomGammaGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomGammaGrad)
: Computes the derivative of a Gamma random sample w.r.t. `alpha`.

[`RandomIndexShuffle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomIndexShuffle)
: Outputs the position of `value` in a permutation of \[0, ..., max\_index\].

[`RandomPoisson(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomPoisson)
: Use RandomPoissonV2 instead.

[`RandomPoissonV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomPoissonV2)
: Outputs random values from the Poisson distribution(s) described by rate.

[`RandomShuffle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomShuffle)
: Randomly shuffles a tensor along its first dimension.

[`RandomShuffleQueue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomShuffleQueue)
: A queue that randomizes the order of elements.

[`RandomShuffleQueueV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomShuffleQueueV2)
: A queue that randomizes the order of elements.

[`RandomStandardNormal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomStandardNormal)
: Outputs random values from a normal distribution.

[`RandomUniform(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomUniform)
: Outputs random values from a uniform distribution.

[`RandomUniformInt(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RandomUniformInt)
: Outputs random integers from a uniform distribution.

[`Range(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Range)
: Creates a sequence of numbers.

[`RangeDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RangeDataset)
: Creates a dataset with a range of values. Corresponds to python's xrange.

[`Rank(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Rank)
: Returns the rank of a tensor.

[`ReadFile(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReadFile)
: Reads and outputs the entire contents of the input filename.

[`ReadVariableOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReadVariableOp)
: Reads the value of a variable.

[`ReadVariableXlaSplitND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReadVariableXlaSplitND)
: Splits resource variable input tensor across all dimensions.

[`ReaderNumRecordsProduced(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderNumRecordsProduced)
: Returns the number of records this Reader has produced.

[`ReaderNumRecordsProducedV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderNumRecordsProducedV2)
: Returns the number of records this Reader has produced.

[`ReaderNumWorkUnitsCompleted(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderNumWorkUnitsCompleted)
: Returns the number of work units this Reader has finished processing.

[`ReaderNumWorkUnitsCompletedV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderNumWorkUnitsCompletedV2)
: Returns the number of work units this Reader has finished processing.

[`ReaderRead(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderRead)
: Returns the next record (key, value pair) produced by a Reader.

[`ReaderReadUpTo(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderReadUpTo)
: Returns up to `num_records` (key, value) pairs produced by a Reader.

[`ReaderReadUpToV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderReadUpToV2)
: Returns up to `num_records` (key, value) pairs produced by a Reader.

[`ReaderReadV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderReadV2)
: Returns the next record (key, value pair) produced by a Reader.

[`ReaderReset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderReset)
: Restore a Reader to its initial clean state.

[`ReaderResetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderResetV2)
: Restore a Reader to its initial clean state.

[`ReaderRestoreState(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderRestoreState)
: Restore a reader to a previously saved state.

[`ReaderRestoreStateV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderRestoreStateV2)
: Restore a reader to a previously saved state.

[`ReaderSerializeState(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderSerializeState)
: Produce a string tensor that encodes the state of a Reader.

[`ReaderSerializeStateV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReaderSerializeStateV2)
: Produce a string tensor that encodes the state of a Reader.

[`Real(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Real)
: Returns the real part of a complex number.

[`RealDiv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RealDiv)
: Returns x / y element-wise for real types.

[`RebatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RebatchDataset)
: Creates a dataset that changes the batch size.

[`RebatchDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RebatchDatasetV2)
: Creates a dataset that changes the batch size.

[`Reciprocal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Reciprocal)
: Computes the reciprocal of x element-wise.

[`ReciprocalGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReciprocalGrad)
: Computes the gradient for the inverse of `x` wrt its input.

[`RecordInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RecordInput)
: Emits randomized records.

[`Recv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Recv)
: Receives the named tensor from send\_device on recv\_device.

[`RecvTPUEmbeddingActivations(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RecvTPUEmbeddingActivations)
: An op that receives embedding activations on the TPU.

[`ReduceDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReduceDataset)
: Reduces the input dataset to a singleton using a reduce function.

[`ReduceJoin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReduceJoin)
: Joins a string Tensor across the given dimensions.

[`RefEnter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RefEnter)
: Creates or finds a child frame, and makes `data` available to the child frame.

[`RefExit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RefExit)
: Exits the current frame to its parent frame.

[`RefIdentity(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RefIdentity)
: Return the same ref tensor as the input ref tensor.

[`RefMerge(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RefMerge)
: Forwards the value of an available tensor from `inputs` to `output`.

[`RefNextIteration(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RefNextIteration)
: Makes its input available to the next iteration.

[`RefSelect(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RefSelect)
: Forwards the `index`th element of `inputs` to `output`.

[`RefSwitch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RefSwitch)
: Forwards the ref tensor `data` to the output port determined by `pred`.

[`RegexFullMatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RegexFullMatch)
: Check if the input matches the regex pattern.

[`RegexReplace(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RegexReplace)
: Replaces matches of the `pattern` regular expression in `input` with the replacement string provided in `rewrite`.

[`RegisterDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RegisterDataset)
: Registers a dataset with the tf.data service.

[`RegisterDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RegisterDatasetV2)
: Registers a dataset with the tf.data service.

[`Relu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Relu)
: Computes rectified linear: `max(features, 0)`.

[`Relu6(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Relu6)
: Computes rectified linear 6: `min(max(features, 0), 6)`.

[`Relu6Grad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Relu6Grad)
: Computes rectified linear 6 gradients for a Relu6 operation.

[`ReluGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReluGrad)
: Computes rectified linear gradients for a Relu operation.

[`RemoteCall(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RemoteCall)
: Runs function `f` on a remote device indicated by `target`.

[`RepeatDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RepeatDataset)
: Creates a dataset that emits the outputs of `input_dataset` `count` times.

[`RequantizationRange(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RequantizationRange)
: Computes a range that covers the actual values present in a quantized tensor.

[`RequantizationRangePerChannel(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RequantizationRangePerChannel)
: Computes requantization range per channel.

[`Requantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Requantize)
: Converts the quantized `input` tensor into a lower-precision `output`.

[`RequantizePerChannel(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RequantizePerChannel)
: Requantizes input with min and max values known per channel.

[`Reshape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Reshape)
: Reshapes a tensor.

[`ResizeArea(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResizeArea)
: Resize `images` to `size` using area interpolation.

[`ResizeBicubic(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResizeBicubic)
: Resize `images` to `size` using bicubic interpolation.

[`ResizeBicubicGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResizeBicubicGrad)
: Computes the gradient of bicubic interpolation.

[`ResizeBilinear(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResizeBilinear)
: Resize `images` to `size` using bilinear interpolation.

[`ResizeBilinearGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResizeBilinearGrad)
: Computes the gradient of bilinear interpolation.

[`ResizeNearestNeighbor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResizeNearestNeighbor)
: Resize `images` to `size` using nearest neighbor interpolation.

[`ResizeNearestNeighborGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResizeNearestNeighborGrad)
: Computes the gradient of nearest neighbor interpolation.

[`ResourceAccumulatorApplyGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceAccumulatorApplyGradient)
: Applies a gradient to a given accumulator.

[`ResourceAccumulatorNumAccumulated(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceAccumulatorNumAccumulated)
: Returns the number of gradients aggregated in the given accumulators.

[`ResourceAccumulatorSetGlobalStep(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceAccumulatorSetGlobalStep)
: Updates the accumulator with a new value for global\_step.

[`ResourceAccumulatorTakeGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceAccumulatorTakeGradient)
: Extracts the average gradient in the given ConditionalAccumulator.

[`ResourceApplyAdaMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyAdaMax)
: Update '\*var' according to the AdaMax algorithm.

[`ResourceApplyAdadelta(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyAdadelta)
: Update '\*var' according to the adadelta scheme.

[`ResourceApplyAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyAdagrad)
: Update '\*var' according to the adagrad scheme.

[`ResourceApplyAdagradDA(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyAdagradDA)
: Update '\*var' according to the proximal adagrad scheme.

[`ResourceApplyAdagradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyAdagradV2)
: Update '\*var' according to the adagrad scheme.

[`ResourceApplyAdam(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyAdam)
: Update '\*var' according to the Adam algorithm.

[`ResourceApplyAdamWithAmsgrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyAdamWithAmsgrad)
: Update '\*var' according to the Adam algorithm.

[`ResourceApplyAddSign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyAddSign)
: Update '\*var' according to the AddSign update.

[`ResourceApplyCenteredRMSProp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyCenteredRMSProp)
: Update '\*var' according to the centered RMSProp algorithm.

[`ResourceApplyFtrl(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyFtrl)
: Update '\*var' according to the Ftrl-proximal scheme.

[`ResourceApplyFtrlV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyFtrlV2)
: Update '\*var' according to the Ftrl-proximal scheme.

[`ResourceApplyGradientDescent(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyGradientDescent)
: Update '\*var' by subtracting 'alpha' \* 'delta' from it.

[`ResourceApplyKerasMomentum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyKerasMomentum)
: Update '\*var' according to the momentum scheme.

[`ResourceApplyMomentum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyMomentum)
: Update '\*var' according to the momentum scheme.

[`ResourceApplyPowerSign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyPowerSign)
: Update '\*var' according to the AddSign update.

[`ResourceApplyProximalAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyProximalAdagrad)
: Update '_var' and '_accum' according to FOBOS with Adagrad learning rate.

[`ResourceApplyProximalGradientDescent(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyProximalGradientDescent)
: Update '\*var' as FOBOS algorithm with fixed learning rate.

[`ResourceApplyRMSProp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceApplyRMSProp)
: Update '\*var' according to the RMSProp algorithm.

[`ResourceConditionalAccumulator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceConditionalAccumulator)
: A conditional accumulator for aggregating gradients.

[`ResourceCountUpTo(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceCountUpTo)
: Increments variable pointed to by 'resource' until it reaches 'limit'.

[`ResourceGather(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceGather)
: Gather slices from the variable pointed to by `resource` according to `indices`.

[`ResourceGatherNd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceGatherNd)

[`ResourceScatterAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterAdd)
: Adds sparse updates to the variable referenced by `resource`.

[`ResourceScatterDiv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterDiv)
: Divides sparse updates into the variable referenced by `resource`.

[`ResourceScatterMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterMax)
: Reduces sparse updates into the variable referenced by `resource` using the `max` operation.

[`ResourceScatterMin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterMin)
: Reduces sparse updates into the variable referenced by `resource` using the `min` operation.

[`ResourceScatterMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterMul)
: Multiplies sparse updates into the variable referenced by `resource`.

[`ResourceScatterNdAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterNdAdd)
: Applies sparse addition to individual values or slices in a Variable.

[`ResourceScatterNdMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterNdMax)

[`ResourceScatterNdMin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterNdMin)

[`ResourceScatterNdSub(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterNdSub)
: Applies sparse subtraction to individual values or slices in a Variable.

[`ResourceScatterNdUpdate(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterNdUpdate)
: Applies sparse `updates` to individual values or slices within a given

[`ResourceScatterSub(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterSub)
: Subtracts sparse updates from the variable referenced by `resource`.

[`ResourceScatterUpdate(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceScatterUpdate)
: Assigns sparse updates to the variable referenced by `resource`.

[`ResourceSparseApplyAdadelta(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyAdadelta)
: var: Should be from a Variable().

[`ResourceSparseApplyAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyAdagrad)
: Update relevant entries in '_var' and '_accum' according to the adagrad scheme.

[`ResourceSparseApplyAdagradDA(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyAdagradDA)
: Update entries in '_var' and '_accum' according to the proximal adagrad scheme.

[`ResourceSparseApplyAdagradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyAdagradV2)
: Update relevant entries in '_var' and '_accum' according to the adagrad scheme.

[`ResourceSparseApplyCenteredRMSProp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyCenteredRMSProp)
: Update '\*var' according to the centered RMSProp algorithm.

[`ResourceSparseApplyFtrl(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyFtrl)
: Update relevant entries in '\*var' according to the Ftrl-proximal scheme.

[`ResourceSparseApplyFtrlV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyFtrlV2)
: Update relevant entries in '\*var' according to the Ftrl-proximal scheme.

[`ResourceSparseApplyKerasMomentum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyKerasMomentum)
: Update relevant entries in '_var' and '_accum' according to the momentum scheme.

[`ResourceSparseApplyMomentum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyMomentum)
: Update relevant entries in '_var' and '_accum' according to the momentum scheme.

[`ResourceSparseApplyProximalAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyProximalAdagrad)
: Sparse update entries in '_var' and '_accum' according to FOBOS algorithm.

[`ResourceSparseApplyProximalGradientDescent(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyProximalGradientDescent)
: Sparse update '\*var' as FOBOS algorithm with fixed learning rate.

[`ResourceSparseApplyRMSProp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceSparseApplyRMSProp)
: Update '\*var' according to the RMSProp algorithm.

[`ResourceStridedSliceAssign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ResourceStridedSliceAssign)
: Assign `value` to the sliced l-value reference of `ref`.

[`Restore(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Restore)
: Restores a tensor from checkpoint files.

[`RestoreSlice(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RestoreSlice)
: Restores a tensor from checkpoint files.

[`RestoreV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RestoreV2)
: Restores tensors from a V2 checkpoint.

[`RetrieveTPUEmbeddingADAMParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingADAMParameters)
: Retrieve ADAM embedding parameters.

[`RetrieveTPUEmbeddingAdadeltaParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingAdadeltaParameters)
: Retrieve Adadelta embedding parameters.

[`RetrieveTPUEmbeddingAdagradMomentumParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingAdagradMomentumParameters)
: Retrieve Adagrad Momentum embedding parameters.

[`RetrieveTPUEmbeddingAdagradParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingAdagradParameters)
: Retrieve Adagrad embedding parameters.

[`RetrieveTPUEmbeddingCenteredRMSPropParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingCenteredRMSPropParameters)
: Retrieve centered RMSProp embedding parameters.

[`RetrieveTPUEmbeddingFTRLParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingFTRLParameters)
: Retrieve FTRL embedding parameters.

[`RetrieveTPUEmbeddingFrequencyEstimatorParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingFrequencyEstimatorParameters)
: Retrieve frequency estimator embedding parameters.

[`RetrieveTPUEmbeddingMDLAdagradLightParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingMDLAdagradLightParameters)
: Retrieve MDL Adagrad Light embedding parameters.

[`RetrieveTPUEmbeddingMomentumParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingMomentumParameters)
: Retrieve Momentum embedding parameters.

[`RetrieveTPUEmbeddingProximalAdagradParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingProximalAdagradParameters)
: Retrieve proximal Adagrad embedding parameters.

[`RetrieveTPUEmbeddingProximalYogiParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingProximalYogiParameters)

[`RetrieveTPUEmbeddingRMSPropParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingRMSPropParameters)
: Retrieve RMSProp embedding parameters.

[`RetrieveTPUEmbeddingStochasticGradientDescentParameters(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingStochasticGradientDescentParameters)
: Retrieve SGD embedding parameters.

[`Reverse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Reverse)
: Reverses specific dimensions of a tensor.

[`ReverseSequence(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReverseSequence)
: Reverses variable length slices.

[`ReverseV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ReverseV2)
: Reverses specific dimensions of a tensor.

[`RewriteDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RewriteDataset)

[`RightShift(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RightShift)
: Elementwise computes the bitwise right-shift of `x` and `y`.

[`Rint(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Rint)
: Returns element-wise integer closest to x.

[`RngReadAndSkip(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RngReadAndSkip)
: Advance the counter of a counter-based RNG.

[`RngSkip(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RngSkip)
: Advance the counter of a counter-based RNG.

[`Roll(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Roll)
: Rolls the elements of a tensor along an axis.

[`Round(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Round)
: Rounds the values of a tensor to the nearest integer, element-wise.

[`Rsqrt(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Rsqrt)
: Computes reciprocal of square root of x element-wise.

[`RsqrtGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/RsqrtGrad)
: Computes the gradient for the rsqrt of `x` wrt its input.

[`SampleDistortedBoundingBox(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SampleDistortedBoundingBox)
: Generate a single randomly distorted bounding box for an image.

[`SampleDistortedBoundingBoxV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SampleDistortedBoundingBoxV2)
: Generate a single randomly distorted bounding box for an image.

[`SamplingDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SamplingDataset)
: Creates a dataset that takes a Bernoulli sample of the contents of another dataset.

[`Save(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Save)
: Saves the input tensors to disk.

[`SaveDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SaveDataset)

[`SaveDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SaveDatasetV2)

[`SaveSlices(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SaveSlices)
: Saves input tensors slices to disk.

[`SaveV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SaveV2)
: Saves tensors in V2 checkpoint format.

[`ScalarSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScalarSummary)
: Outputs a `Summary` protocol buffer with scalar values.

[`ScaleAndTranslate(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScaleAndTranslate)

[`ScaleAndTranslateGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScaleAndTranslateGrad)

[`ScanDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScanDataset)
: Creates a dataset successively reduces `f` over the elements of `input_dataset`.

[`ScatterAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterAdd)
: Adds sparse updates to a variable reference.

[`ScatterDiv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterDiv)
: Divides a variable reference by sparse updates.

[`ScatterMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterMax)
: Reduces sparse updates into a variable reference using the `max` operation.

[`ScatterMin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterMin)
: Reduces sparse updates into a variable reference using the `min` operation.

[`ScatterMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterMul)
: Multiplies sparse updates into a variable reference.

[`ScatterNd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterNd)
: Scatters `updates` into a tensor of shape `shape` according to `indices`.

[`ScatterNdAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterNdAdd)
: Applies sparse addition to individual values or slices in a Variable.

[`ScatterNdMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterNdMax)
: Computes element-wise maximum.

[`ScatterNdMin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterNdMin)
: Computes element-wise minimum.

[`ScatterNdNonAliasingAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterNdNonAliasingAdd)
: Applies sparse addition to `input` using individual values or slices

[`ScatterNdSub(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterNdSub)
: Applies sparse subtraction to individual values or slices in a Variable.

[`ScatterNdUpdate(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterNdUpdate)
: Applies sparse `updates` to individual values or slices within a given

[`ScatterSub(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterSub)
: Subtracts sparse updates to a variable reference.

[`ScatterUpdate(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ScatterUpdate)
: Applies sparse updates to a variable reference.

[`SdcaFprint(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SdcaFprint)
: Computes fingerprints of the input strings.

[`SdcaOptimizer(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SdcaOptimizer)
: Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

[`SdcaOptimizerV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SdcaOptimizerV2)
: Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

[`SdcaShrinkL1(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SdcaShrinkL1)
: Applies L1 regularization shrink step on the parameters.

[`SegmentMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentMax)
: Computes the maximum along segments of a tensor.

[`SegmentMaxV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentMaxV2)
: Computes the maximum along segments of a tensor.

[`SegmentMean(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentMean)
: Computes the mean along segments of a tensor.

[`SegmentMin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentMin)
: Computes the minimum along segments of a tensor.

[`SegmentMinV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentMinV2)
: Computes the minimum along segments of a tensor.

[`SegmentProd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentProd)
: Computes the product along segments of a tensor.

[`SegmentProdV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentProdV2)
: Computes the product along segments of a tensor.

[`SegmentSum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentSum)
: Computes the sum along segments of a tensor.

[`SegmentSumV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SegmentSumV2)
: Computes the sum along segments of a tensor.

[`Select(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Select)
: Selects elements from `x` or `y`, depending on `condition`.

[`SelectV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SelectV2)

[`SelfAdjointEig(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SelfAdjointEig)
: Computes the Eigen Decomposition of a batch of square self-adjoint matrices.

[`SelfAdjointEigV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SelfAdjointEigV2)
: Computes the eigen decomposition of one or more square self-adjoint matrices.

[`Selu(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Selu)
: Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

[`SeluGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SeluGrad)
: Computes gradients for the scaled exponential linear (Selu) operation.

[`Send(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Send)
: Sends the named tensor from send\_device to recv\_device.

[`SendTPUEmbeddingGradients(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SendTPUEmbeddingGradients)
: Performs gradient updates of embedding tables.

[`SerializeIterator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SerializeIterator)
: Converts the given `resource_handle` representing an iterator to a variant tensor.

[`SerializeManySparse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SerializeManySparse)
: Serialize an `N`\-minibatch `SparseTensor` into an `[N, 3]` `Tensor` object.

[`SerializeSparse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SerializeSparse)
: Serialize a `SparseTensor` into a `[3]` `Tensor` object.

[`SerializeTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SerializeTensor)
: Transforms a Tensor into a serialized TensorProto proto.

[`SetSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SetSize)
: Number of unique elements along last dimension of input `set`.

[`SetStatsAggregatorDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SetStatsAggregatorDataset)

[`Shape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Shape)
: Returns the shape of a tensor.

[`ShapeN(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShapeN)
: Returns shape of tensors.

[`ShardDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShardDataset)
: Creates a `Dataset` that includes only 1/`num_shards` of this dataset.

[`ShardedFilename(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShardedFilename)
: Generate a sharded filename.

[`ShardedFilespec(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShardedFilespec)
: Generate a glob pattern matching all sharded file names.

[`ShuffleAndRepeatDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShuffleAndRepeatDataset)
: Creates a dataset that shuffles and repeats elements from `input_dataset`

[`ShuffleAndRepeatDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShuffleAndRepeatDatasetV2)

[`ShuffleDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShuffleDataset)
: Creates a dataset that shuffles elements from `input_dataset` pseudorandomly.

[`ShuffleDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShuffleDatasetV2)

[`ShuffleDatasetV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShuffleDatasetV3)

[`ShutdownDistributedTPU(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ShutdownDistributedTPU)
: Shuts down a running distributed TPU system.

[`Sigmoid(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Sigmoid)
: Computes sigmoid of `x` element-wise.

[`SigmoidGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SigmoidGrad)
: Computes the gradient of the sigmoid of `x` wrt its input.

[`Sign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Sign)
: Returns an element-wise indication of the sign of a number.

[`Sin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Sin)
: Computes sine of x element-wise.

[`Sinh(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Sinh)
: Computes hyperbolic sine of x element-wise.

[`Size(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Size)
: Returns the size of a tensor.

[`SkipDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SkipDataset)
: Creates a dataset that skips `count` elements from the `input_dataset`.

[`SleepDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SleepDataset)

[`Slice(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Slice)
: Return a slice from 'input'.

[`SlidingWindowDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SlidingWindowDataset)
: Creates a dataset that passes a sliding window over `input_dataset`.

[`Snapshot(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Snapshot)
: Returns a copy of the input tensor.

[`SnapshotChunkDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SnapshotChunkDataset)

[`SnapshotDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SnapshotDataset)
: Creates a dataset that will write to / read from a snapshot.

[`SnapshotDatasetReader(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SnapshotDatasetReader)

[`SnapshotDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SnapshotDatasetV2)
: Creates a dataset that will write to / read from a snapshot.

[`SnapshotNestedDatasetReader(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SnapshotNestedDatasetReader)

[`SobolSample(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SobolSample)
: Generates points from the Sobol sequence.

[`Softmax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Softmax)
: Computes softmax activations.

[`SoftmaxCrossEntropyWithLogits(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SoftmaxCrossEntropyWithLogits)
: Computes softmax cross entropy cost and gradients to backpropagate.

[`Softplus(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Softplus)

[`SoftplusGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SoftplusGrad)
: Computes softplus gradients for a softplus operation.

[`Softsign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Softsign)
: Computes softsign: `features / (abs(features) + 1)`.

[`SoftsignGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SoftsignGrad)
: Computes softsign gradients for a softsign operation.

[`SortListOfSparseCoreCooTensors(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SortListOfSparseCoreCooTensors)

[`SpaceToBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SpaceToBatch)
: SpaceToBatch for 4-D tensors of type T.

[`SpaceToBatchND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SpaceToBatchND)
: SpaceToBatch for N-D tensors of type T.

[`SpaceToDepth(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SpaceToDepth)
: SpaceToDepth for tensors of type T.

[`SparseAccumulatorApplyGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseAccumulatorApplyGradient)
: Applies a sparse gradient to a given accumulator.

[`SparseAccumulatorTakeGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseAccumulatorTakeGradient)
: Extracts the average sparse gradient in a SparseConditionalAccumulator.

[`SparseAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseAdd)
: Adds two `SparseTensor` objects to produce another `SparseTensor`.

[`SparseAddGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseAddGrad)
: The gradient operator for the SparseAdd op.

[`SparseApplyAdadelta(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyAdadelta)
: var: Should be from a Variable().

[`SparseApplyAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyAdagrad)
: Update relevant entries in '_var' and '_accum' according to the adagrad scheme.

[`SparseApplyAdagradDA(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyAdagradDA)
: Update entries in '_var' and '_accum' according to the proximal adagrad scheme.

[`SparseApplyAdagradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyAdagradV2)
: Update relevant entries in '_var' and '_accum' according to the adagrad scheme.

[`SparseApplyCenteredRMSProp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyCenteredRMSProp)
: Update '\*var' according to the centered RMSProp algorithm.

[`SparseApplyFtrl(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyFtrl)
: Update relevant entries in '\*var' according to the Ftrl-proximal scheme.

[`SparseApplyFtrlV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyFtrlV2)
: Update relevant entries in '\*var' according to the Ftrl-proximal scheme.

[`SparseApplyMomentum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyMomentum)
: Update relevant entries in '_var' and '_accum' according to the momentum scheme.

[`SparseApplyProximalAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyProximalAdagrad)
: Sparse update entries in '_var' and '_accum' according to FOBOS algorithm.

[`SparseApplyProximalGradientDescent(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyProximalGradientDescent)
: Sparse update '\*var' as FOBOS algorithm with fixed learning rate.

[`SparseApplyRMSProp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseApplyRMSProp)
: Update '\*var' according to the RMSProp algorithm.

[`SparseBincount(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseBincount)
: Counts the number of occurrences of each value in an integer array.

[`SparseConcat(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseConcat)
: Concatenates a list of `SparseTensor` along the specified dimension.

[`SparseConditionalAccumulator(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseConditionalAccumulator)
: A conditional accumulator for aggregating sparse gradients.

[`SparseCountSparseOutput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseCountSparseOutput)
: Performs sparse-output bin counting for a sparse tensor input.

[`SparseCross(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseCross)
: Generates sparse cross from a list of sparse and dense tensors.

[`SparseCrossHashed(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseCrossHashed)
: Generates sparse cross from a list of sparse and dense tensors.

[`SparseCrossV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseCrossV2)
: Generates sparse cross from a list of sparse and dense tensors.

[`SparseDenseCwiseAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseDenseCwiseAdd)
: Adds up a SparseTensor and a dense Tensor, using these special rules:

[`SparseDenseCwiseDiv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseDenseCwiseDiv)
: Component-wise divides a SparseTensor by a dense Tensor.

[`SparseDenseCwiseMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseDenseCwiseMul)
: Component-wise multiplies a SparseTensor by a dense Tensor.

[`SparseFillEmptyRows(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseFillEmptyRows)
: Fills empty rows in the input 2-D `SparseTensor` with a default value.

[`SparseFillEmptyRowsGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseFillEmptyRowsGrad)
: The gradient of SparseFillEmptyRows.

[`SparseMatMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatMul)
: Multiply matrix "a" by matrix "b".

[`SparseMatrixAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixAdd)
: Sparse addition of two CSR matrices, C = alpha \* A + beta \* B.

[`SparseMatrixMatMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixMatMul)
: Matrix-multiplies a sparse matrix with a dense matrix.

[`SparseMatrixMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixMul)
: Element-wise multiplication of a sparse matrix with a dense tensor.

[`SparseMatrixNNZ(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixNNZ)
: Returns the number of nonzeroes of `sparse_matrix`.

[`SparseMatrixOrderingAMD(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixOrderingAMD)
: Computes the Approximate Minimum Degree (AMD) ordering of `input`.

[`SparseMatrixSoftmax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixSoftmax)
: Calculates the softmax of a CSRSparseMatrix.

[`SparseMatrixSoftmaxGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixSoftmaxGrad)
: Calculates the gradient of the SparseMatrixSoftmax op.

[`SparseMatrixSparseCholesky(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixSparseCholesky)
: Computes the sparse Cholesky decomposition of `input`.

[`SparseMatrixSparseMatMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixSparseMatMul)
: Sparse-matrix-multiplies two CSR matrices `a` and `b`.

[`SparseMatrixTranspose(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixTranspose)
: Transposes the inner (matrix) dimensions of a CSRSparseMatrix.

[`SparseMatrixZeros(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseMatrixZeros)
: Creates an all-zeros CSRSparseMatrix with shape `dense_shape`.

[`SparseReduceMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseReduceMax)
: Computes the max of elements across dimensions of a SparseTensor.

[`SparseReduceMaxSparse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseReduceMaxSparse)
: Computes the max of elements across dimensions of a SparseTensor.

[`SparseReduceSum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseReduceSum)
: Computes the sum of elements across dimensions of a SparseTensor.

[`SparseReduceSumSparse(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseReduceSumSparse)
: Computes the sum of elements across dimensions of a SparseTensor.

[`SparseReorder(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseReorder)
: Reorders a SparseTensor into the canonical, row-major ordering.

[`SparseReshape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseReshape)
: Reshapes a SparseTensor to represent values in a new dense shape.

[`SparseSegmentMean(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentMean)
: Computes the mean along sparse segments of a tensor.

[`SparseSegmentMeanGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentMeanGrad)
: Computes gradients for SparseSegmentMean.

[`SparseSegmentMeanGradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentMeanGradV2)
: Computes gradients for SparseSegmentMean.

[`SparseSegmentMeanWithNumSegments(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentMeanWithNumSegments)
: Computes the mean along sparse segments of a tensor.

[`SparseSegmentSqrtN(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentSqrtN)
: Computes the sum along sparse segments of a tensor divided by the sqrt of N.

[`SparseSegmentSqrtNGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentSqrtNGrad)
: Computes gradients for SparseSegmentSqrtN.

[`SparseSegmentSqrtNGradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentSqrtNGradV2)
: Computes gradients for SparseSegmentSqrtN.

[`SparseSegmentSqrtNWithNumSegments(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentSqrtNWithNumSegments)
: Computes the sum along sparse segments of a tensor divided by the sqrt of N.

[`SparseSegmentSum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentSum)
: Computes the sum along sparse segments of a tensor.

[`SparseSegmentSumGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentSumGrad)
: Computes gradients for SparseSegmentSum.

[`SparseSegmentSumGradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentSumGradV2)
: Computes gradients for SparseSegmentSum.

[`SparseSegmentSumWithNumSegments(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSegmentSumWithNumSegments)
: Computes the sum along sparse segments of a tensor.

[`SparseSlice(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSlice)
: Slice a `SparseTensor` based on the `start` and `size`.

[`SparseSliceGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSliceGrad)
: The gradient operator for the SparseSlice op.

[`SparseSoftmax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSoftmax)
: Applies softmax to a batched N-D `SparseTensor`.

[`SparseSoftmaxCrossEntropyWithLogits(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSoftmaxCrossEntropyWithLogits)
: Computes softmax cross entropy cost and gradients to backpropagate.

[`SparseSparseMaximum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSparseMaximum)
: Returns the element-wise max of two SparseTensors.

[`SparseSparseMinimum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSparseMinimum)
: Returns the element-wise min of two SparseTensors.

[`SparseSplit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseSplit)
: Split a `SparseTensor` into `num_split` tensors along one dimension.

[`SparseTensorDenseAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseTensorDenseAdd)
: Adds up a `SparseTensor` and a dense `Tensor`, producing a dense `Tensor`.

[`SparseTensorDenseMatMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseTensorDenseMatMul)
: Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

[`SparseTensorSliceDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseTensorSliceDataset)
: Creates a dataset that splits a SparseTensor into elements row-wise.

[`SparseTensorToCSRSparseMatrix(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseTensorToCSRSparseMatrix)
: Converts a SparseTensor to a (possibly batched) CSRSparseMatrix.

[`SparseToDense(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseToDense)
: Converts a sparse representation into a dense tensor.

[`SparseToSparseSetOperation(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SparseToSparseSetOperation)
: Applies set operation along last dimension of 2 `SparseTensor` inputs.

[`Spence(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Spence)

[`Split(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Split)
: Splits a tensor into `num_split` tensors along one dimension.

[`SplitV(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SplitV)
: Splits a tensor into `num_split` tensors along one dimension.

[`SqlDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SqlDataset)
: Creates a dataset that executes a SQL query and emits rows of the result set.

[`Sqrt(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Sqrt)
: Computes square root of x element-wise.

[`SqrtGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SqrtGrad)
: Computes the gradient for the sqrt of `x` wrt its input.

[`Square(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Square)
: Computes square of x element-wise.

[`SquaredDifference(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SquaredDifference)
: Returns conj(x - y)(x - y) element-wise.

[`Squeeze(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Squeeze)
: Removes dimensions of size 1 from the shape of a tensor.

[`Stack(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Stack)
: Deprecated, use StackV2.

[`StackClose(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StackClose)
: Deprecated, use StackCloseV2.

[`StackCloseV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StackCloseV2)
: Delete the stack from its resource container.

[`StackPop(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StackPop)
: Deprecated, use StackPopV2.

[`StackPopV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StackPopV2)
: Pop the element at the top of the stack.

[`StackPush(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StackPush)
: Deprecated, use StackPushV2.

[`StackPushV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StackPushV2)
: Push an element onto the stack.

[`StackV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StackV2)
: A stack that produces elements in first-in last-out order.

[`Stage(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Stage)
: Stage values similar to a lightweight Enqueue.

[`StageClear(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StageClear)
: Op removes all elements in the underlying container.

[`StagePeek(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StagePeek)
: Op peeks at the values at the specified index.

[`StageSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StageSize)
: Op returns the number of elements in the underlying container.

[`StatefulPartitionedCall(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatefulPartitionedCall)
: returns `f(inputs)`, where `f`'s body is placed and partitioned.

[`StatefulRandomBinomial(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatefulRandomBinomial)

[`StatefulStandardNormal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatefulStandardNormal)
: Outputs random values from a normal distribution.

[`StatefulStandardNormalV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatefulStandardNormalV2)
: Outputs random values from a normal distribution.

[`StatefulTruncatedNormal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatefulTruncatedNormal)
: Outputs random values from a truncated normal distribution.

[`StatefulUniform(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatefulUniform)
: Outputs random values from a uniform distribution.

[`StatefulUniformFullInt(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatefulUniformFullInt)
: Outputs random integers from a uniform distribution.

[`StatefulUniformInt(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatefulUniformInt)
: Outputs random integers from a uniform distribution.

[`StatelessCase(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessCase)
: An n-way switch statement which calls a single branch function.

[`StatelessIf(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessIf)
: output = cond ? then\_branch(input) : else\_branch(input)

[`StatelessMultinomial(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessMultinomial)
: Draws samples from a multinomial distribution.

[`StatelessParameterizedTruncatedNormal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessParameterizedTruncatedNormal)

[`StatelessRandomBinomial(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomBinomial)
: Outputs deterministic pseudorandom random numbers from a binomial distribution.

[`StatelessRandomGammaV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomGammaV2)
: Outputs deterministic pseudorandom random numbers from a gamma distribution.

[`StatelessRandomGammaV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomGammaV3)
: Outputs deterministic pseudorandom random numbers from a gamma distribution.

[`StatelessRandomGetAlg(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomGetAlg)
: Picks the best counter-based RNG algorithm based on device.

[`StatelessRandomGetKeyCounter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomGetKeyCounter)
: Scrambles seed into key and counter, using the best algorithm based on device.

[`StatelessRandomGetKeyCounterAlg(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomGetKeyCounterAlg)
: Picks the best algorithm based on device, and scrambles seed into key and counter.

[`StatelessRandomNormal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomNormal)
: Outputs deterministic pseudorandom values from a normal distribution.

[`StatelessRandomNormalV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomNormalV2)
: Outputs deterministic pseudorandom values from a normal distribution.

[`StatelessRandomPoisson(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomPoisson)
: Outputs deterministic pseudorandom random numbers from a Poisson distribution.

[`StatelessRandomUniform(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomUniform)
: Outputs deterministic pseudorandom random values from a uniform distribution.

[`StatelessRandomUniformFullInt(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomUniformFullInt)
: Outputs deterministic pseudorandom random integers from a uniform distribution.

[`StatelessRandomUniformFullIntV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomUniformFullIntV2)
: Outputs deterministic pseudorandom random integers from a uniform distribution.

[`StatelessRandomUniformInt(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomUniformInt)
: Outputs deterministic pseudorandom random integers from a uniform distribution.

[`StatelessRandomUniformIntV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomUniformIntV2)
: Outputs deterministic pseudorandom random integers from a uniform distribution.

[`StatelessRandomUniformV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessRandomUniformV2)
: Outputs deterministic pseudorandom random values from a uniform distribution.

[`StatelessSampleDistortedBoundingBox(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessSampleDistortedBoundingBox)
: Generate a randomly distorted bounding box for an image deterministically.

[`StatelessShuffle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessShuffle)
: Randomly and deterministically shuffles a tensor along its first dimension.

[`StatelessTruncatedNormal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessTruncatedNormal)
: Outputs deterministic pseudorandom values from a truncated normal distribution.

[`StatelessTruncatedNormalV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessTruncatedNormalV2)
: Outputs deterministic pseudorandom values from a truncated normal distribution.

[`StatelessWhile(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatelessWhile)
: output = input; While (Cond(output)) { output = Body(output) }

[`StaticRegexFullMatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StaticRegexFullMatch)
: Check if the input matches the regex pattern.

[`StaticRegexReplace(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StaticRegexReplace)
: Replaces the match of pattern in input with rewrite.

[`StatsAggregatorHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatsAggregatorHandle)
: Creates a statistics manager resource.

[`StatsAggregatorHandleV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatsAggregatorHandleV2)

[`StatsAggregatorSetSummaryWriter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatsAggregatorSetSummaryWriter)
: Set a summary\_writer\_interface to record statistics using given stats\_aggregator.

[`StatsAggregatorSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StatsAggregatorSummary)
: Produces a summary of any statistics recorded by the given statistics manager.

[`StopGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StopGradient)
: Stops gradient computation.

[`StoreMinibatchStatisticsInFdo(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StoreMinibatchStatisticsInFdo)

[`StridedSlice(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StridedSlice)
: Return a strided slice from `input`.

[`StridedSliceAssign(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StridedSliceAssign)
: Assign `value` to the sliced l-value reference of `ref`.

[`StridedSliceGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StridedSliceGrad)
: Returns the gradient of `StridedSlice`.

[`StringFormat(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringFormat)
: Formats a string template using a list of tensors.

[`StringJoin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringJoin)
: Joins the strings in the given list of string tensors into one tensor;

[`StringLength(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringLength)
: String lengths of `input`.

[`StringLower(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringLower)
: Converts all uppercase characters into their respective lowercase replacements.

[`StringNGrams(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringNGrams)
: Creates ngrams from ragged string data.

[`StringSplit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringSplit)
: Split elements of `input` based on `delimiter` into a `SparseTensor`.

[`StringSplitV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringSplitV2)
: Split elements of `source` based on `sep` into a `SparseTensor`.

[`StringStrip(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringStrip)
: Strip leading and trailing whitespaces from the Tensor.

[`StringToHashBucket(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringToHashBucket)
: Converts each string in the input Tensor to its hash mod by a number of buckets.

[`StringToHashBucketFast(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringToHashBucketFast)
: Converts each string in the input Tensor to its hash mod by a number of buckets.

[`StringToHashBucketStrong(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringToHashBucketStrong)
: Converts each string in the input Tensor to its hash mod by a number of buckets.

[`StringToNumber(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringToNumber)
: Converts each string in the input Tensor to the specified numeric type.

[`StringUpper(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/StringUpper)
: Converts all lowercase characters into their respective uppercase replacements.

[`Sub(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Sub)
: Returns x - y element-wise.

[`Substr(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Substr)
: Return substrings from `Tensor` of strings.

[`Sum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Sum)
: Computes the sum of elements across dimensions of a tensor.

[`SummaryWriter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SummaryWriter)

[`Svd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Svd)
: Computes the singular value decompositions of one or more matrices.

[`Switch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Switch)
: Forwards `data` to the output port determined by `pred`.

[`SymbolicGradient(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SymbolicGradient)
: Computes the gradient function for function f via backpropagation.

[`SyncDevice(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/SyncDevice)
: Synchronizes the device this op is run on.

[`TFRecordDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TFRecordDataset)
: Creates a dataset that emits the records from one or more TFRecord files.

[`TFRecordDatasetV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TFRecordDatasetV2)
: Creates a dataset that emits the records from one or more TFRecord files.

[`TFRecordReader(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TFRecordReader)
: A Reader that outputs the records from a TensorFlow Records file.

[`TFRecordReaderV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TFRecordReaderV2)
: A Reader that outputs the records from a TensorFlow Records file.

[`TPUAnnotateTensorsWithDynamicShape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUAnnotateTensorsWithDynamicShape)

[`TPUCompilationResult(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUCompilationResult)
: Returns the result of a TPU compilation.

[`TPUCopyWithDynamicShape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUCopyWithDynamicShape)
: Op that copies host tensor to device with dynamic shape support.

[`TPUDummyInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUDummyInput)
: Generates a zero-valued tensor for use as a dummy input to a TPU.

[`TPUEmbeddingActivations(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUEmbeddingActivations)
: An op enabling differentiation of TPU Embeddings.

[`TPUOrdinalSelector(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUOrdinalSelector)
: A TPU core selector Op.

[`TPUPartitionedCall(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUPartitionedCall)
: Calls a function placed on a specified TPU device.

[`TPUPartitionedInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUPartitionedInput)
: An op that groups a list of partitioned inputs together.

[`TPUPartitionedInputV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUPartitionedInputV2)
: An op that groups a list of partitioned inputs together. Supports ND sharding.

[`TPUPartitionedOutput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUPartitionedOutput)
: An op that demultiplexes a tensor to be sharded by XLA to a list of partitioned

[`TPUPartitionedOutputV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUPartitionedOutputV2)
: An op that demultiplexes a tensor to be sharded by XLA to a list of partitioned

[`TPUReplicateMetadata(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUReplicateMetadata)
: Metadata indicating how the TPU computation should be replicated.

[`TPUReplicatedInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUReplicatedInput)
: Connects N inputs to an N-way replicated TPU computation.

[`TPUReplicatedOutput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TPUReplicatedOutput)
: Connects N outputs from an N-way replicated TPU computation.

[`TakeDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TakeDataset)
: Creates a dataset that contains `count` elements from the `input_dataset`.

[`TakeManySparseFromTensorsMap(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TakeManySparseFromTensorsMap)
: Read `SparseTensors` from a `SparseTensorsMap` and concatenate them.

[`TakeWhileDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TakeWhileDataset)
: Creates a dataset that stops iteration when predicate\` is false.

[`Tan(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Tan)
: Computes tan of x element-wise.

[`Tanh(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Tanh)
: Computes hyperbolic tangent of `x` element-wise.

[`TanhGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TanhGrad)
: Computes the gradient for the tanh of `x` wrt its input.

[`TemporaryVariable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TemporaryVariable)
: Returns a tensor that may be mutated, but only persists within a single step.

[`TensorArray(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArray)

[`TensorArrayClose(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayClose)

[`TensorArrayCloseV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayCloseV2)
: Deprecated.

[`TensorArrayCloseV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayCloseV3)
: Delete the TensorArray from its resource container.

[`TensorArrayConcat(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayConcat)

[`TensorArrayConcatV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayConcatV2)
: Deprecated.

[`TensorArrayConcatV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayConcatV3)
: Concat the elements from the TensorArray into value `value`.

[`TensorArrayGather(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayGather)

[`TensorArrayGatherV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayGatherV2)
: Deprecated.

[`TensorArrayGatherV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayGatherV3)
: Gather specific elements from the TensorArray into output `value`.

[`TensorArrayGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayGrad)

[`TensorArrayGradV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayGradV2)
: Deprecated.

[`TensorArrayGradV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayGradV3)
: Creates a TensorArray for storing the gradients of values in the given handle.

[`TensorArrayGradWithShape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayGradWithShape)
: Creates a TensorArray for storing multiple gradients of values in the given handle.

[`TensorArrayPack(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayPack)

[`TensorArrayRead(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayRead)

[`TensorArrayReadV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayReadV2)
: Deprecated.

[`TensorArrayReadV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayReadV3)
: Read an element from the TensorArray into output `value`.

[`TensorArrayScatter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayScatter)

[`TensorArrayScatterV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayScatterV2)
: Deprecated.

[`TensorArrayScatterV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayScatterV3)
: Scatter the data from the input value into specific TensorArray elements.

[`TensorArraySize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArraySize)

[`TensorArraySizeV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArraySizeV2)
: Deprecated.

[`TensorArraySizeV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArraySizeV3)
: Get the current size of the TensorArray.

[`TensorArraySplit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArraySplit)

[`TensorArraySplitV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArraySplitV2)
: Deprecated.

[`TensorArraySplitV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArraySplitV3)
: Split the data from the input value into TensorArray elements.

[`TensorArrayUnpack(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayUnpack)

[`TensorArrayV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayV2)
: Deprecated.

[`TensorArrayV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayV3)
: An array of Tensors of given size.

[`TensorArrayWrite(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayWrite)

[`TensorArrayWriteV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayWriteV2)
: Deprecated.

[`TensorArrayWriteV3(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorArrayWriteV3)
: Push an element onto the tensor\_array.

[`TensorDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorDataset)
: Creates a dataset that emits `components` as a tuple of tensors once.

[`TensorListConcat(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListConcat)
: Concats all tensors in the list along the 0th dimension.

[`TensorListConcatLists(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListConcatLists)

[`TensorListConcatV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListConcatV2)
: Concats all tensors in the list along the 0th dimension.

[`TensorListElementShape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListElementShape)
: The shape of the elements of the given list, as a tensor.

[`TensorListFromTensor(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListFromTensor)
: Creates a TensorList which, when stacked, has the value of `tensor`.

[`TensorListGather(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListGather)
: Creates a Tensor by indexing into the TensorList.

[`TensorListGetItem(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListGetItem)
: Returns the item in the list with the given index.

[`TensorListLength(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListLength)
: Returns the number of tensors in the input tensor list.

[`TensorListPopBack(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListPopBack)
: Returns the last element of the input list as well as a list with all but that element.

[`TensorListPushBack(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListPushBack)
: Returns a list which has the passed-in `Tensor` as last element and the other elements of the given list in `input_handle`.

[`TensorListPushBackBatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListPushBackBatch)

[`TensorListReserve(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListReserve)
: List of the given size with empty elements.

[`TensorListResize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListResize)
: Resizes the list.

[`TensorListScatter(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListScatter)
: Creates a TensorList by indexing into a Tensor.

[`TensorListScatterIntoExistingList(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListScatterIntoExistingList)
: Scatters tensor at indices in an input list.

[`TensorListScatterV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListScatterV2)
: Creates a TensorList by indexing into a Tensor.

[`TensorListSetItem(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListSetItem)
: Sets the index-th position of the list to contain the given tensor.

[`TensorListSplit(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListSplit)
: Splits a tensor into a list.

[`TensorListStack(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorListStack)
: Stacks all tensors in the list.

[`TensorMapErase(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorMapErase)
: Returns a tensor map with item from given key erased.

[`TensorMapHasKey(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorMapHasKey)
: Returns whether the given key exists in the map.

[`TensorMapInsert(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorMapInsert)
: Returns a map that is the 'input\_handle' with the given key-value pair inserted.

[`TensorMapLookup(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorMapLookup)
: Returns the value from a given key in a tensor map.

[`TensorMapSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorMapSize)
: Returns the number of tensors in the input tensor map.

[`TensorMapStackKeys(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorMapStackKeys)
: Returns a Tensor stack of all keys in a tensor map.

[`TensorScatterAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorScatterAdd)
: Adds sparse `updates` to an existing tensor according to `indices`.

[`TensorScatterMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorScatterMax)
: Apply a sparse update to a tensor taking the element-wise maximum.

[`TensorScatterMin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorScatterMin)

[`TensorScatterSub(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorScatterSub)
: Subtracts sparse `updates` from an existing tensor according to `indices`.

[`TensorScatterUpdate(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorScatterUpdate)
: Scatter `updates` into an existing tensor according to `indices`.

[`TensorSliceDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorSliceDataset)
: Creates a dataset that emits each dim-0 slice of `components` once.

[`TensorStridedSliceUpdate(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorStridedSliceUpdate)
: Assign `value` to the sliced l-value reference of `input`.

[`TensorSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorSummary)
: Outputs a `Summary` protocol buffer with a tensor.

[`TensorSummaryV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TensorSummaryV2)
: Outputs a `Summary` protocol buffer with a tensor and per-plugin data.

[`TextLineDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TextLineDataset)
: Creates a dataset that emits the lines of one or more text files.

[`TextLineReader(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TextLineReader)
: A Reader that outputs the lines of a file delimited by '\\n'.

[`TextLineReaderV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TextLineReaderV2)
: A Reader that outputs the lines of a file delimited by '\\n'.

[`ThreadPoolDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ThreadPoolDataset)
: Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ThreadPoolHandle(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ThreadPoolHandle)
: Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ThreadUnsafeUnigramCandidateSampler(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ThreadUnsafeUnigramCandidateSampler)
: Generates labels for candidate sampling with a learned unigram distribution.

[`Tile(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Tile)
: Constructs a tensor by tiling a given tensor.

[`TileGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TileGrad)
: Returns the gradient of `Tile`.

[`Timestamp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Timestamp)
: Provides the time since epoch in seconds.

[`ToBool(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ToBool)
: Converts a tensor to a scalar predicate.

[`TopK(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TopK)
: Finds values and indices of the `k` largest elements for the last dimension.

[`TopKV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TopKV2)
: Finds values and indices of the `k` largest elements for the last dimension.

[`Transpose(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Transpose)
: Shuffle dimensions of x according to a permutation.

[`TridiagonalMatMul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TridiagonalMatMul)
: Calculate product with tridiagonal matrix.

[`TridiagonalSolve(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TridiagonalSolve)
: Solves tridiagonal systems of equations.

[`TruncateDiv(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TruncateDiv)
: Returns x / y element-wise, rounded towards zero.

[`TruncateMod(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TruncateMod)
: Returns element-wise remainder of division.

[`TruncatedNormal(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/TruncatedNormal)
: Outputs random values from a truncated normal distribution.

[`Unbatch(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Unbatch)
: Reverses the operation of Batch for a single output Tensor.

[`UnbatchDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnbatchDataset)
: A dataset that splits the elements of its input into multiple elements.

[`UnbatchGrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnbatchGrad)
: Gradient of Unbatch.

[`UncompressElement(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UncompressElement)
: Uncompresses a compressed dataset element.

[`UnicodeDecode(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnicodeDecode)
: Decodes each string in `input` into a sequence of Unicode code points.

[`UnicodeDecodeWithOffsets(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnicodeDecodeWithOffsets)
: Decodes each string in `input` into a sequence of Unicode code points.

[`UnicodeEncode(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnicodeEncode)
: Encode a tensor of ints into unicode strings.

[`UnicodeScript(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnicodeScript)
: Determine the script codes of a given tensor of Unicode integer code points.

[`UnicodeTranscode(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnicodeTranscode)
: Transcode the input text from a source encoding to a destination encoding.

[`UniformCandidateSampler(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformCandidateSampler)
: Generates labels for candidate sampling with a uniform distribution.

[`UniformDequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformDequantize)
: Perform dequantization on the quantized Tensor `input`.

[`UniformQuantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformQuantize)
: Perform quantization on Tensor `input`.

[`UniformQuantizedAdd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformQuantizedAdd)
: Perform quantized add of quantized Tensor `lhs` and quantized Tensor `rhs` to make quantized `output`.

[`UniformQuantizedClipByValue(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformQuantizedClipByValue)
: Perform clip by value on the quantized Tensor `operand`.

[`UniformQuantizedConvolution(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformQuantizedConvolution)
: Perform quantized convolution of quantized Tensor `lhs` and quantized Tensor `rhs`. to make quantized `output`.

[`UniformQuantizedConvolutionHybrid(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformQuantizedConvolutionHybrid)
: Perform hybrid quantized convolution of float Tensor `lhs` and quantized Tensor `rhs`.

[`UniformQuantizedDot(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformQuantizedDot)
: Perform quantized dot of quantized Tensor `lhs` and quantized Tensor `rhs` to make quantized `output`.

[`UniformQuantizedDotHybrid(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformQuantizedDotHybrid)
: Perform hybrid quantized dot of float Tensor `lhs` and quantized Tensor `rhs`.

[`UniformRequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniformRequantize)
: Given quantized tensor `input`, requantize it with new quantization parameters.

[`Unique(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Unique)
: Finds unique elements in a 1-D tensor.

[`UniqueDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniqueDataset)
: Creates a dataset that contains the unique elements of `input_dataset`.

[`UniqueV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniqueV2)
: Finds unique elements along an axis of a tensor.

[`UniqueWithCounts(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniqueWithCounts)
: Finds unique elements in a 1-D tensor.

[`UniqueWithCountsV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UniqueWithCountsV2)
: Finds unique elements along an axis of a tensor.

[`Unpack(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Unpack)
: Unpacks a given dimension of a rank-`R` tensor into `num` rank-`(R-1)` tensors.

[`UnravelIndex(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnravelIndex)
: Converts an array of flat indices into a tuple of coordinate arrays.

[`UnsortedSegmentJoin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnsortedSegmentJoin)

[`UnsortedSegmentMax(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnsortedSegmentMax)
: Computes the maximum along segments of a tensor.

[`UnsortedSegmentMin(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnsortedSegmentMin)
: Computes the minimum along segments of a tensor.

[`UnsortedSegmentProd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnsortedSegmentProd)
: Computes the product along segments of a tensor.

[`UnsortedSegmentSum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnsortedSegmentSum)
: Computes the sum along segments of a tensor.

[`Unstage(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Unstage)
: Op is similar to a lightweight Dequeue.

[`UnwrapDatasetVariant(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UnwrapDatasetVariant)

[`UpperBound(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/UpperBound)
: Applies upper\_bound(sorted\_search\_values, values) along each row.

[`VarHandleOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/VarHandleOp)
: Creates a handle to a Variable resource.

[`VarIsInitializedOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/VarIsInitializedOp)
: Checks whether a resource handle-based variable has been initialized.

[`Variable(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Variable)
: Use VariableV2 instead.

[`VariableShape(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/VariableShape)
: Returns the shape of the variable pointed to by `resource`.

[`VariableV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/VariableV2)
: Holds state in the form of a tensor that persists across steps.

[`WeightedFlatMapDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WeightedFlatMapDataset)

[`Where(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Where)
: Returns locations of nonzero / true values in a tensor.

[`While(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/While)
: output = input; While (Cond(output)) { output = Body(output) }

[`WholeFileReader(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WholeFileReader)
: A Reader that outputs the entire contents of a file as a value.

[`WholeFileReaderV2(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WholeFileReaderV2)
: A Reader that outputs the entire contents of a file as a value.

[`WindowDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WindowDataset)
: Combines (nests of) input elements into a dataset of (nests of) windows.

[`WindowOp(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WindowOp)

[`WorkerHeartbeat(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WorkerHeartbeat)
: Worker heartbeat op.

[`WrapDatasetVariant(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WrapDatasetVariant)

[`WriteAudioSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WriteAudioSummary)
: Writes an audio summary.

[`WriteFile(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WriteFile)
: Writes `contents` to the file at input `filename`.

[`WriteGraphSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WriteGraphSummary)
: Writes a graph summary.

[`WriteHistogramSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WriteHistogramSummary)
: Writes a histogram summary.

[`WriteImageSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WriteImageSummary)
: Writes an image summary.

[`WriteRawProtoSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WriteRawProtoSummary)
: Writes a serialized proto summary.

[`WriteScalarSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WriteScalarSummary)
: Writes a scalar summary.

[`WriteSummary(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/WriteSummary)
: Writes a tensor summary.

[`Xdivy(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Xdivy)
: Returns 0 if x == 0, and x / y otherwise, elementwise.

[`XlaConcatND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaConcatND)
: Concats input tensor across all dimensions.

[`XlaSparseCoreAdagrad(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseCoreAdagrad)

[`XlaSparseCoreAdagradMomentum(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseCoreAdagradMomentum)

[`XlaSparseCoreAdam(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseCoreAdam)

[`XlaSparseCoreFtrl(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseCoreFtrl)

[`XlaSparseCoreSgd(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseCoreSgd)

[`XlaSparseDenseMatmul(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmul)

[`XlaSparseDenseMatmulCustomCombinerOnTcGradWithAdagradAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulCustomCombinerOnTcGradWithAdagradAndCsrInput)

[`XlaSparseDenseMatmulCustomCombinerOnTcGradWithAdagradMomentumAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulCustomCombinerOnTcGradWithAdagradMomentumAndCsrInput)

[`XlaSparseDenseMatmulCustomCombinerOnTcGradWithAdamAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulCustomCombinerOnTcGradWithAdamAndCsrInput)

[`XlaSparseDenseMatmulCustomCombinerOnTcGradWithCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulCustomCombinerOnTcGradWithCsrInput)

[`XlaSparseDenseMatmulCustomCombinerOnTcGradWithFtrlAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulCustomCombinerOnTcGradWithFtrlAndCsrInput)

[`XlaSparseDenseMatmulCustomCombinerOnTcGradWithSgdAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulCustomCombinerOnTcGradWithSgdAndCsrInput)

[`XlaSparseDenseMatmulCustomCombinerOnTcWithCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulCustomCombinerOnTcWithCsrInput)

[`XlaSparseDenseMatmulGradWithAdagradAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithAdagradAndCsrInput)

[`XlaSparseDenseMatmulGradWithAdagradAndStaticBufferSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithAdagradAndStaticBufferSize)

[`XlaSparseDenseMatmulGradWithAdagradMomentumAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithAdagradMomentumAndCsrInput)

[`XlaSparseDenseMatmulGradWithAdagradMomentumAndStaticBufferSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithAdagradMomentumAndStaticBufferSize)

[`XlaSparseDenseMatmulGradWithAdamAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithAdamAndCsrInput)

[`XlaSparseDenseMatmulGradWithAdamAndStaticBufferSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithAdamAndStaticBufferSize)

[`XlaSparseDenseMatmulGradWithCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithCsrInput)

[`XlaSparseDenseMatmulGradWithFtrlAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithFtrlAndCsrInput)

[`XlaSparseDenseMatmulGradWithFtrlAndStaticBufferSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithFtrlAndStaticBufferSize)

[`XlaSparseDenseMatmulGradWithSgdAndCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithSgdAndCsrInput)

[`XlaSparseDenseMatmulGradWithSgdAndStaticBufferSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulGradWithSgdAndStaticBufferSize)

[`XlaSparseDenseMatmulWithCsrInput(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulWithCsrInput)

[`XlaSparseDenseMatmulWithStaticBufferSize(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSparseDenseMatmulWithStaticBufferSize)

[`XlaSplitND(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/XlaSplitND)
: Splits input tensor across all dimensions.

[`Xlog1py(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Xlog1py)
: Returns 0 if x == 0, and x \* log1p(y) otherwise, elementwise.

[`Xlogy(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Xlogy)
: Returns 0 if x == 0, and x \* log(y) otherwise, elementwise.

[`ZerosLike(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ZerosLike)
: Returns a tensor of zeros with the same shape and type as x.

[`Zeta(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/Zeta)
: Compute the Hurwitz zeta function ζ(x,q).

[`ZipDataset(...)`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/ZipDataset)
: Creates a dataset that zips together `input_datasets`.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.