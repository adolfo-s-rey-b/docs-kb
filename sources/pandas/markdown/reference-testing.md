[Skip to main content](https://pandas.pydata.org/docs/reference/testing.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Testing[#](https://pandas.pydata.org/docs/reference/testing.html#testing "Link to this heading")

=================================================================================================

Assertion functions[#](https://pandas.pydata.org/docs/reference/testing.html#assertion-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`testing.assert_frame_equal`](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html#pandas.testing.assert_frame_equal "pandas.testing.assert_frame_equal")<br>(left, right\[, ...\]) | Check that left and right DataFrame are equal. |
| [`testing.assert_series_equal`](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_series_equal.html#pandas.testing.assert_series_equal "pandas.testing.assert_series_equal")<br>(left, right\[, ...\]) | Check that left and right Series are equal. |
| [`testing.assert_index_equal`](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_index_equal.html#pandas.testing.assert_index_equal "pandas.testing.assert_index_equal")<br>(left, right\[, ...\]) | Check that left and right Index are equal. |
| [`testing.assert_extension_array_equal`](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_extension_array_equal.html#pandas.testing.assert_extension_array_equal "pandas.testing.assert_extension_array_equal")<br>(left, right) | Check that left and right ExtensionArrays are equal. |

Exceptions and warnings[#](https://pandas.pydata.org/docs/reference/testing.html#exceptions-and-warnings "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`errors.AbstractMethodError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.AbstractMethodError.html#pandas.errors.AbstractMethodError "pandas.errors.AbstractMethodError")<br>(class\_instance\[, ...\]) | Raise this error instead of NotImplementedError for abstract methods. |
| [`errors.AttributeConflictWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.AttributeConflictWarning.html#pandas.errors.AttributeConflictWarning "pandas.errors.AttributeConflictWarning") | Warning raised when index attributes conflict when using HDFStore. |
| [`errors.CategoricalConversionWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.CategoricalConversionWarning.html#pandas.errors.CategoricalConversionWarning "pandas.errors.CategoricalConversionWarning") | Warning is raised when reading a partial labeled Stata file using an iterator. |
| [`errors.ChainedAssignmentError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.ChainedAssignmentError.html#pandas.errors.ChainedAssignmentError "pandas.errors.ChainedAssignmentError") | Warning raised when trying to set using chained assignment. |
| [`errors.ClosedFileError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.ClosedFileError.html#pandas.errors.ClosedFileError "pandas.errors.ClosedFileError") | Exception is raised when trying to perform an operation on a closed HDFStore file. |
| [`errors.CSSWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.CSSWarning.html#pandas.errors.CSSWarning "pandas.errors.CSSWarning") | Warning is raised when converting css styling fails. |
| [`errors.DatabaseError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.DatabaseError.html#pandas.errors.DatabaseError "pandas.errors.DatabaseError") | Error is raised when executing SQL with bad syntax or SQL that throws an error. |
| [`errors.DataError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.DataError.html#pandas.errors.DataError "pandas.errors.DataError") | Exception raised when performing an operation on non-numerical data. |
| [`errors.DtypeWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.DtypeWarning.html#pandas.errors.DtypeWarning "pandas.errors.DtypeWarning") | Warning raised when reading different dtypes in a column from a file. |
| [`errors.DuplicateLabelError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.DuplicateLabelError.html#pandas.errors.DuplicateLabelError "pandas.errors.DuplicateLabelError") | Error raised when an operation would introduce duplicate labels. |
| [`errors.EmptyDataError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.EmptyDataError.html#pandas.errors.EmptyDataError "pandas.errors.EmptyDataError") | Exception raised in `pd.read_csv` when empty data or header is encountered. |
| [`errors.IncompatibilityWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.IncompatibilityWarning.html#pandas.errors.IncompatibilityWarning "pandas.errors.IncompatibilityWarning") | Warning raised when trying to use where criteria on an incompatible HDF5 file. |
| [`errors.IncompatibleFrequency`](https://pandas.pydata.org/docs/reference/api/pandas.errors.IncompatibleFrequency.html#pandas.errors.IncompatibleFrequency "pandas.errors.IncompatibleFrequency") | Raised when trying to compare or operate between Periods with different frequencies. |
| [`errors.IndexingError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.IndexingError.html#pandas.errors.IndexingError "pandas.errors.IndexingError") | Exception is raised when trying to index and there is a mismatch in dimensions. |
| [`errors.InvalidColumnName`](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidColumnName.html#pandas.errors.InvalidColumnName "pandas.errors.InvalidColumnName") | Warning raised by to\_stata the column contains a non-valid stata name. |
| [`errors.InvalidComparison`](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidComparison.html#pandas.errors.InvalidComparison "pandas.errors.InvalidComparison") | Exception is raised by \_validate\_comparison\_value to indicate an invalid comparison. |
| [`errors.InvalidIndexError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidIndexError.html#pandas.errors.InvalidIndexError "pandas.errors.InvalidIndexError") | Exception raised when attempting to use an invalid index key. |
| [`errors.InvalidVersion`](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidVersion.html#pandas.errors.InvalidVersion "pandas.errors.InvalidVersion") | An invalid version was found, users should refer to PEP 440. |
| [`errors.IntCastingNaNError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.IntCastingNaNError.html#pandas.errors.IntCastingNaNError "pandas.errors.IntCastingNaNError") | Exception raised when converting (`astype`) an array with NaN to an integer type. |
| [`errors.LossySetitemError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.LossySetitemError.html#pandas.errors.LossySetitemError "pandas.errors.LossySetitemError") | Raised when trying to do a \_\_setitem\_\_ on an np.ndarray that is not lossless. |
| [`errors.MergeError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.MergeError.html#pandas.errors.MergeError "pandas.errors.MergeError") | Exception raised when merging data. |
| [`errors.NoBufferPresent`](https://pandas.pydata.org/docs/reference/api/pandas.errors.NoBufferPresent.html#pandas.errors.NoBufferPresent "pandas.errors.NoBufferPresent") | Exception is raised in \_get\_data\_buffer to signal that there is no requested buffer. |
| [`errors.NullFrequencyError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.NullFrequencyError.html#pandas.errors.NullFrequencyError "pandas.errors.NullFrequencyError") | Exception raised when a `freq` cannot be null. |
| [`errors.NumbaUtilError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumbaUtilError.html#pandas.errors.NumbaUtilError "pandas.errors.NumbaUtilError") | Error raised for unsupported Numba engine routines. |
| [`errors.NumExprClobberingError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumExprClobberingError.html#pandas.errors.NumExprClobberingError "pandas.errors.NumExprClobberingError") | Exception raised when trying to use a built-in numexpr name as a variable name. |
| [`errors.OptionError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.OptionError.html#pandas.errors.OptionError "pandas.errors.OptionError") | Exception raised for pandas.options. |
| [`errors.OutOfBoundsDatetime`](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsDatetime.html#pandas.errors.OutOfBoundsDatetime "pandas.errors.OutOfBoundsDatetime") | Raised when the datetime is outside the range that can be represented. |
| [`errors.OutOfBoundsTimedelta`](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsTimedelta.html#pandas.errors.OutOfBoundsTimedelta "pandas.errors.OutOfBoundsTimedelta") | Raised when encountering a timedelta value that cannot be represented. |
| [`errors.PandasChangeWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PandasChangeWarning.html#pandas.errors.PandasChangeWarning "pandas.errors.PandasChangeWarning") | Warning raised for any upcoming change. |
| [`errors.Pandas4Warning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.Pandas4Warning.html#pandas.errors.Pandas4Warning "pandas.errors.Pandas4Warning") | Warning raised for an upcoming change that will be enforced in pandas 4.0. |
| [`errors.Pandas5Warning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.Pandas5Warning.html#pandas.errors.Pandas5Warning "pandas.errors.Pandas5Warning") | Warning raised for an upcoming change that will be enforced in pandas 5.0. |
| [`errors.PandasPendingDeprecationWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PandasPendingDeprecationWarning.html#pandas.errors.PandasPendingDeprecationWarning "pandas.errors.PandasPendingDeprecationWarning") | Warning raised for an upcoming change that is a PendingDeprecationWarning. |
| [`errors.PandasDeprecationWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PandasDeprecationWarning.html#pandas.errors.PandasDeprecationWarning "pandas.errors.PandasDeprecationWarning") | Warning raised for an upcoming change that is a DeprecationWarning. |
| [`errors.PandasFutureWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PandasFutureWarning.html#pandas.errors.PandasFutureWarning "pandas.errors.PandasFutureWarning") | Warning raised for an upcoming change that is a FutureWarning. |
| [`errors.ParserError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserError.html#pandas.errors.ParserError "pandas.errors.ParserError") | Exception that is raised by an error encountered in parsing file contents. |
| [`errors.ParserWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserWarning.html#pandas.errors.ParserWarning "pandas.errors.ParserWarning") | Warning raised when reading a file that doesn't use the default 'c' parser. |
| [`errors.PerformanceWarning`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PerformanceWarning.html#pandas.errors.PerformanceWarning "pandas.errors.PerformanceWarning") | Warning raised when there is a possible performance impact. |
| [`errors.PossibleDataLossError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossibleDataLossError.html#pandas.errors.PossibleDataLossError "pandas.errors.PossibleDataLossError") | Exception raised when trying to open an HDFStore file when already opened. |
| [`errors.PossiblePrecisionLoss`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossiblePrecisionLoss.html#pandas.errors.PossiblePrecisionLoss "pandas.errors.PossiblePrecisionLoss") | Warning raised by to\_stata on a column with a value outside or equal to int64. |
| [`errors.PyperclipException`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PyperclipException.html#pandas.errors.PyperclipException "pandas.errors.PyperclipException") | Exception raised when clipboard functionality is unsupported. |
| [`errors.PyperclipWindowsException`](https://pandas.pydata.org/docs/reference/api/pandas.errors.PyperclipWindowsException.html#pandas.errors.PyperclipWindowsException "pandas.errors.PyperclipWindowsException")<br>(message) | Exception raised when clipboard functionality is unsupported by Windows. |
| [`errors.SpecificationError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.SpecificationError.html#pandas.errors.SpecificationError "pandas.errors.SpecificationError") | Exception raised by `agg` when the functions are ill-specified. |
| [`errors.UndefinedVariableError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.UndefinedVariableError.html#pandas.errors.UndefinedVariableError "pandas.errors.UndefinedVariableError")<br>(name\[, is\_local\]) | Exception raised by `query` or `eval` when using an undefined variable name. |
| [`errors.UnsortedIndexError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsortedIndexError.html#pandas.errors.UnsortedIndexError "pandas.errors.UnsortedIndexError") | Error raised when slicing a MultiIndex which has not been lexsorted. |
| [`errors.UnsupportedFunctionCall`](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsupportedFunctionCall.html#pandas.errors.UnsupportedFunctionCall "pandas.errors.UnsupportedFunctionCall") | Exception raised when attempting to call an unsupported numpy function. |
| [`errors.ValueLabelTypeMismatch`](https://pandas.pydata.org/docs/reference/api/pandas.errors.ValueLabelTypeMismatch.html#pandas.errors.ValueLabelTypeMismatch "pandas.errors.ValueLabelTypeMismatch") | Warning raised by to\_stata on a category column that contains non-string values. |

Bug report function[#](https://pandas.pydata.org/docs/reference/testing.html#bug-report-function "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`show_versions`](https://pandas.pydata.org/docs/reference/api/pandas.show_versions.html#pandas.show_versions "pandas.show_versions")<br>(\[as\_json\]) | Provide useful information, important for bug reports. |

Test suite runner[#](https://pandas.pydata.org/docs/reference/testing.html#test-suite-runner "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`test`](https://pandas.pydata.org/docs/reference/api/pandas.test.html#pandas.test "pandas.test")<br>(\[extra\_args, run\_doctests\]) | Run the pandas test suite using pytest. |

On this page