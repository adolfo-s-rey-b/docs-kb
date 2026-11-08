[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/errors#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/errors)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/errors?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ferrors&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/errors#classes)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/errors#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.errors Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/errors#classes)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/errors#other-members)
    

Public API for tf.\_api.v2.errors namespace

Classes
-------

[`class AbortedError`](https://www.tensorflow.org/api_docs/python/tf/errors/AbortedError)
: Raised when an operation was aborted, typically due to a concurrent action.

[`class AlreadyExistsError`](https://www.tensorflow.org/api_docs/python/tf/errors/AlreadyExistsError)
: Raised when an entity that we attempted to create already exists.

[`class CancelledError`](https://www.tensorflow.org/api_docs/python/tf/errors/CancelledError)
: Raised when an operation is cancelled.

[`class DataLossError`](https://www.tensorflow.org/api_docs/python/tf/errors/DataLossError)
: Raised when unrecoverable data loss or corruption is encountered.

[`class DeadlineExceededError`](https://www.tensorflow.org/api_docs/python/tf/errors/DeadlineExceededError)
: Raised when a deadline expires before an operation could complete.

[`class FailedPreconditionError`](https://www.tensorflow.org/api_docs/python/tf/errors/FailedPreconditionError)
: Raised when some prerequisites are not met when running an operation.

[`class InternalError`](https://www.tensorflow.org/api_docs/python/tf/errors/InternalError)
: Raised when the system experiences an internal error.

[`class InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)
: Raised when an operation receives an invalid argument.

[`class NotFoundError`](https://www.tensorflow.org/api_docs/python/tf/errors/NotFoundError)
: Raised when a requested entity (e.g., a file or directory) was not found.

[`class OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError)
: The base class for TensorFlow exceptions.

[`class OperatorNotAllowedInGraphError`](https://www.tensorflow.org/api_docs/python/tf/errors/OperatorNotAllowedInGraphError)
: Raised when an unsupported operator is present in Graph execution.

[`class OutOfRangeError`](https://www.tensorflow.org/api_docs/python/tf/errors/OutOfRangeError)
: Raised when an operation iterates past the valid range.

[`class PermissionDeniedError`](https://www.tensorflow.org/api_docs/python/tf/errors/PermissionDeniedError)
: Raised when the caller does not have permission to run an operation.

[`class ResourceExhaustedError`](https://www.tensorflow.org/api_docs/python/tf/errors/ResourceExhaustedError)
: Raised when some resource has been exhausted while running operation.

[`class UnauthenticatedError`](https://www.tensorflow.org/api_docs/python/tf/errors/UnauthenticatedError)
: Raised when the request does not have valid authentication credentials.

[`class UnavailableError`](https://www.tensorflow.org/api_docs/python/tf/errors/UnavailableError)
: Raised when the runtime is currently unavailable.

[`class UnimplementedError`](https://www.tensorflow.org/api_docs/python/tf/errors/UnimplementedError)
: Raised when an operation has not been implemented.

[`class UnknownError`](https://www.tensorflow.org/api_docs/python/tf/errors/UnknownError)
: Unknown error.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| ABORTED | `10` |
| ALREADY\_EXISTS | `6` |
| CANCELLED | `1` |
| DATA\_LOSS | `15` |
| DEADLINE\_EXCEEDED | `4` |
| FAILED\_PRECONDITION | `9` |
| INTERNAL | `13` |
| INVALID\_ARGUMENT | `3` |
| NOT\_FOUND | `5` |
| OK  | `0` |
| OUT\_OF\_RANGE | `11` |
| PERMISSION\_DENIED | `7` |
| RESOURCE\_EXHAUSTED | `8` |
| UNAUTHENTICATED | `16` |
| UNAVAILABLE | `14` |
| UNIMPLEMENTED | `12` |
| UNKNOWN | `2` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.