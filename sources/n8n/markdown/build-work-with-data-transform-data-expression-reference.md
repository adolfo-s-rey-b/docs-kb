For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference.md)
.

These are some commonly used expressions. A more exhaustive list appears below.

In this section[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#in-this-section)

----------------------------------------------------------------------------------------------------------------

*   [Array](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array)
    : methods for working with arrays.
    
*   [BinaryFile](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile)
    : properties of binary file data.
    
*   [Boolean](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean)
    : methods for working with booleans.
    
*   [CustomData](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata)
    : methods for getting and setting custom execution data.
    
*   [Date](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date)
    : methods for converting a JavaScript Date.
    
*   [DateTime](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime)
    : methods and properties for working with Luxon DateTimes.
    
*   [ExecData](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata)
    : properties of the current execution.
    
*   [HTTPResponse](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/httpresponse)
    : properties of the last HTTP call's response.
    
*   [Item](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/item)
    : properties of the current item.
    
*   [NodeInputData](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata)
    : methods for reading the current node's input.
    
*   [NodeOutputData](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata)
    : methods for reading a node's output.
    
*   [Number](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number)
    : methods for working with numbers.
    
*   [Object](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object)
    : methods for working with objects.
    
*   [PrevNodeData](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata)
    : properties describing the node an input came from.
    
*   [Root](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root)
    : top-level variables and helper functions such as `$json` and `$now`.
    
*   [String](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string)
    : methods for working with strings.
    
*   [WorkflowData](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/workflowdata)
    : properties of the current workflow.
    

Category

Expression

Description

Access current input item data

`$json`

JSON data of the current item

`$json.fieldName`

Field of the current item

`$binary`

Binary data of current item

Access previous node data

`$("NodeName").first()`

First item in a node

`$("NodeName").item`

Linked item of a node. See [Item linking](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
 for more information.

`$("NodeName").all()`

All items of a node

`$("NodeName").last()`

Last item of a node

Date/Time

`$now`

Current date and time

`$today`

Today's date

`$now.toFormat("yyyy-MM-dd")`

Format current date as a string

Conditionals

`$if(condition, "true", "false")`

Helper function that returns a value when a condition is true or false

`condition ? true : false`

Ternary operator: returns one value if a condition is true, another if false

`$ifEmpty(value, defaultValue)`

Helper function takes two parameters and tests the first to check if it's empty, then returns either the parameter (if not empty) or the second parameter (if the first is empty). The first parameter is empty if it's `undefined`, `null`, an empty string `''`, an array where `value.length` returns `false` , or an object where `Object.keys(value).length` returns `false`

String Methods

`text.toUpperCase()`

Convert to uppercase

`text.toLowerCase()`

Convert to lowercase

`text.includes("foo")`

Check if text contains search term

`text.extractEmail()`

Extract email from text

Array Methods

`array.length`

Get array length

`array.join(", ")`

Join array elements using a comma a separator

`array.filter(x => x <= 20)`

Filter items of array based on the filtering condition

`array.map(x => x.id)`

Transform items of an array

Browse the tables below to find methods by the data type on which they act. Click a method name to read detailed documentation for it.

Array[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#array)

--------------------------------------------------------------------------------------------

*   [`_Array_`.`**append(elem1, elem2?, ..., elemN?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayappend)
    
    Adds new elements to the end of the array. Similar to `push()`, but returns the modified array. Consider using spread syntax instead (see examples).
    
*   [`_Array_`.`**average()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayaverage)
    
    Returns the average of the numbers in the array. Throws an error if there are any non-numbers.
    
*   [`_Array_`.`**chunk(length)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraychunk)
    
    Splits the array into an array of sub-arrays, each with the given length
    
*   [`_Array_`.`**compact()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraycompact)
    
    Removes any empty values from the array. `null`, `""` and `undefined` count as empty.
    
*   [`_Array_`.`**concat(array2, array3?, ... arrayN?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayconcat)
    
    Joins one or more arrays onto the end of the base array
    
*   [`_Array_`.`**difference(otherArray)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraydifference)
    
    Compares two arrays. Returns all elements in the base array that aren't present in `otherArray`.
    
*   [`_Array_`.`**filter(function(element, index?, array?), thisValue?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayfilter)
    
    Returns an array with only the elements satisfying a condition. The condition is a function that returns `true` or `false`.
    
*   [`_Array_`.`**find(function(element, index?, array?), thisValue?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayfind)
    
    Returns the first element from the array that satisfies the provided condition. The condition is a function that returns `true` or `false`. Returns `undefined` if no matches are found.
    

If you need all matching elements, use `filter()`.

*   [`_Array_`.`**first()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayfirst)
    
    Returns the first element of the array
    
*   [`_Array_`.`**includes(element, start?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayincludes)
    
    Returns `true` if the array contains the specified element
    
*   [`_Array_`.`**indexOf(element, start?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayindexof)
    
    Returns the position of the first matching element in the array, or -1 if the element isn’t found. Positions start at 0.
    
*   [`_Array_`.`**intersection(otherArray)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayintersection)
    
    Compares two arrays. Returns all elements in the base array that are also present in the other array.
    
*   [`_Array_`.`**isEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayisempty)
    
    Returns `true` if the array has no elements or is `null` or `undefined`
    
*   [`_Array_`.`**isNotEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayisnotempty)
    
    Returns `true` if the array has at least one element
    
*   [`_Array_`.`**join(separator?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayjoin)
    
    Merges all elements of the array into a single string, with an optional separator between each element.
    

The opposite of `split()`.

*   [`_Array_`.`**last()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraylast)
    
    Returns the last element of the array
    
*   [`_Array_`.`**length**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraylength)
    
    The number of elements in the array
    
*   [`_Array_`.`**map(function(element, index?, array?), thisValue?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraymap)
    
    Creates a new array by applying a function to each element of the original array
    
*   [`_Array_`.`**max()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraymax)
    
    Returns the largest number in the array. Throws an error if there are any non-numbers.
    
*   [`_Array_`.`**min()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraymin)
    
    Returns the smallest number in the array. Throws an error if there are any non-numbers.
    
*   [`_Array_`.`**pluck(fieldName1?, fieldName2?, …)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraypluck)
    
    Returns an array containing the values of the given field(s) in each Object of the array. Ignores any array elements that aren’t Objects or don’t have a key matching the field name(s) provided.
    
*   [`_Array_`.`**randomItem()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayrandomitem)
    
    Returns a randomly-chosen element from the array
    
*   [`_Array_`.`**reduce(function(prevResult, currentElem, currentIndex?, array?), initResult)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayreduce)
    
    Reduces an array to a single value by applying a function to each element. The function combines the current element with the result of reducing the previous elements, producing a new result.
    
*   [`_Array_`.`**removeDuplicates(keys?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayremoveduplicates)
    
    Removes any re-occurring elements from the array
    
*   [`_Array_`.`**renameKeys(from, to)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayrenamekeys)
    
    Changes all matching keys (field names) of any Objects in the array. Rename more than one key by adding extra arguments, i.e. `from1, to1, from2, to2, ...`.
    
*   [`_Array_`.`**reverse()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayreverse)
    
    Reverses the order of the elements in the array
    
*   [`_Array_`.`**slice(start, end)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayslice)
    
    Returns a portion of the array, from the `start` index up to (but not including) the `end` index. Indexes start at 0.
    
*   [`_Array_`.`**smartJoin(keyField, nameField)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraysmartjoin)
    
    Creates a single Object from an array of Objects. Each Object in the array provides one field for the returned Object. Each Object in the array must contain a field with the key name and a field with the value.
    
*   [`_Array_`.`**sort(compareFunction(a, b)?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraysort)
    
    Reorders the elements of the array. For sorting strings alphabetically, no parameter is required. For sorting numbers or Objects, see examples.
    
*   [`_Array_`.`**sum()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraysum)
    
    Returns the total of all the numbers in the array. Throws an error if there are any non-numbers.
    
*   [`_Array_`.`**toJsonString()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraytojsonstring)
    
    Converts the array to a JSON string. The same as JavaScript’s `JSON.stringify()`.
    
*   [`_Array_`.`**toSpliced(start, deleteCount, elem1, ....., elemN)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraytospliced)
    
    Adds and/or removes array elements at a given position.
    

See also `slice()` and `append()`.

*   [`_Array_`.`**toString()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraytostring)
    
    Converts the array to a string, with values separated by commas. To use a different separator, use `join()` instead.
    
*   [`_Array_`.`**union(otherArray)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayunion)
    
    Concatenates two arrays and then removes any duplicates
    
*   [`_Array_`.`**unique()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayunique)
    
    Removes any duplicate elements from the array
    

BinaryFile[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#binaryfile)

------------------------------------------------------------------------------------------------------

*   [`binaryFile`.`**directory**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfiledirectory)
    
    The path to the directory that the file is stored in. Useful for distinguishing between files with the same name in different directories. Not set if n8n is configured to store files in its database.
    
*   [`binaryFile`.`**fileExtension**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilefileextension)
    
    The suffix attached to the filename (e.g. `txt`)
    
*   [`binaryFile`.`**fileName**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilefilename)
    
    The name of the file, including extension
    
*   [`binaryFile`.`**fileSize**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilefilesize)
    
    A string representing the size of the file
    
*   [`binaryFile`.`**fileType**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilefiletype)
    
    A string representing the type of the file, e.g. `image`. Corresponds to the first part of the MIME type.
    
*   [`binaryFile`.`**id**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfileid)
    
    The unique ID of the file. Used to identify the file when it is stored on disk or in a storage service such as S3.
    
*   [`binaryFile`.`**mimeType**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilemimetype)
    
    A string representing the format of the file’s contents, e.g. `image/jpeg`
    

Boolean[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#boolean)

------------------------------------------------------------------------------------------------

*   [`_Boolean_`.`**isEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#booleanisempty)
    
    Returns `true` if the boolean is `false`, `null`, or `undefined`. Returns `false` if the boolean is `true`.
    
*   [`_Boolean_`.`**isNotEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#booleanisnotempty)
    
    Returns `true` if the boolean is `true`. Returns `false` if the boolean is `false`, `null`, or `undefined`. This is the inverse of `isEmpty()`.
    
*   [`_Boolean_`.`**toNumber()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#booleantonumber)
    
    Converts `true` to 1 and `false` to 0
    
*   [`_Boolean_`.`**toString()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#booleantostring)
    
    Converts `true` to the string ‘true’ and `false` to the string ‘false’
    

CustomData[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#customdata)

------------------------------------------------------------------------------------------------------

*   [`$execution.customData`.`**get(key)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#dollarexecutioncustomdataget)
    
    Returns the custom execution data stored under the given key. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [`$execution.customData`.`**getAll()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#dollarexecutioncustomdatagetall)
    
    Returns all the key-value pairs of custom data that have been set in the current execution. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [`$execution.customData`.`**set(key, value)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#dollarexecutioncustomdataset)
    
    Stores custom execution data under the key specified. Use this to easily filter executions by this data. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [`$execution.customData`.`**setAll(obj)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#dollarexecutioncustomdatasetall)
    
    Sets multiple key-value pairs of custom data for the execution. Use this to easily filter executions by this data. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    

Date[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#date)

------------------------------------------------------------------------------------------

*   [`_Date_`.`**toDateTime()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date#datetodatetime)
    
    Converts a JavaScript Date to a Luxon DateTime. The DateTime contains the same information, but is easier to manipulate.
    

DateTime[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#datetime)

--------------------------------------------------------------------------------------------------

*   [`_DateTime_`.`**day**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeday)
    
    The day of the month (1-31)
    
*   [`_DateTime_`.`**diffTo(otherDateTime, unit)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimediffto)
    
    Returns the difference between two DateTimes, in the given unit(s)
    
*   [`_DateTime_`.`**diffToNow(unit)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimedifftonow)
    
    Returns the difference between the current moment and the DateTime, in the given unit(s). For a textual representation, use `toRelative()` instead.
    
*   [`_DateTime_`.`**endOf(unit, opts)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeendof)
    
    Rounds the DateTime up to the end of one of its units, e.g. the end of the month
    
*   [`_DateTime_`.`**equals(other)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeequals)
    
    Returns `true` if the two DateTimes represent exactly the same moment and are in the same time zone. For a less strict comparison, use `hasSame()`.
    
*   [`_DateTime_`.`**extract(unit?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeextract)
    
    Extracts a part of the date or time, e.g. the month, as a number. To extract textual names instead, see `format()`.
    
*   [`_DateTime_`.`**format(fmt)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeformat)
    
    Converts the DateTime to a string, using the format specified. [Formatting guide](https://moment.github.io/luxon/#/formatting?id=table-of-tokens)
    . For common formats, `toLocaleString()` may be easier.
    
*   [`_DateTime_`.`**hasSame(otherDateTime, unit)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimehassame)
    
    Returns `true` if the two DateTimes are the same, down to the unit specified. Time zones are ignored (only local times are compared), so use `toUTC()` first if needed.
    
*   [`_DateTime_`.`**hour**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimehour)
    
    The hour of the day (0-23)
    
*   [`_DateTime_`.`**isBetween(date1, date2)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeisbetween)
    
    Returns `true` if the DateTime lies between the two moments specified
    
*   [`_DateTime_`.`**isEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeisempty)
    
    Returns `false` for all DateTimes. Returns `true` for `null` or `undefined`.
    
*   [`_DateTime_`.`**isInDST**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeisindst)
    
    Whether the DateTime is in daylight saving time
    
*   [`_DateTime_`.`**isNotEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeisnotempty)
    
    Returns `true` for all DateTimes. Returns `false` for `null` or `undefined`.
    
*   [`_DateTime_`.`**locale**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimelocale)
    
    The locale of a DateTime, such 'en-GB'. The locale is used when formatting the DateTime.
    
*   [`_DateTime_`.`**millisecond**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimemillisecond)
    
    The millisecond of the second (0-999)
    
*   [`_DateTime_`.`**minus(n, unit?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeminus)
    
    Subtracts a given period of time from the DateTime
    
*   [`_DateTime_`.`**minute**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeminute)
    
    The minute of the hour (0-59)
    
*   [`_DateTime_`.`**month**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimemonth)
    
    The month (1-12)
    
*   [`_DateTime_`.`**monthLong**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimemonthlong)
    
    The textual long month name, e.g. 'October'. Defaults to the system's locale if no locale has been specified.
    
*   [`_DateTime_`.`**monthShort**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimemonthshort)
    
    The textual abbreviated month name, e.g. 'Oct'. Defaults to the system's locale if no locale has been specified.
    
*   [`_DateTime_`.`**plus(n, unit?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeplus)
    
    Adds a given period of time to the DateTime
    
*   [`_DateTime_`.`**quarter**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimequarter)
    
    The quarter of the year (1-4)
    
*   [`_DateTime_`.`**second**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimesecond)
    
    The second of the minute (0-59)
    
*   [`_DateTime_`.`**set(values)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeset)
    
    Assigns new values to specified units of the DateTime. To round a DateTime, see also `startOf()` and `endOf()`.
    
*   [`_DateTime_`.`**setLocale(locale)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimesetlocale)
    
    Sets the locale, which determines the language and formatting for the DateTime. Useful when generating a textual representation of the DateTime, e.g. with `format()` or `toLocaleString()`.
    
*   [`_DateTime_`.`**setZone(zone, opts)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimesetzone)
    
    Converts the DateTime to the given time zone. The DateTime still represents the same moment unless specified in the options. See also `toLocal()` and `toUTC()`.
    
*   [`_DateTime_`.`**startOf(unit, opts)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimestartof)
    
    Rounds the DateTime down to the beginning of one of its units, e.g. the start of the month
    
*   [`_DateTime_`.`**toISO(opts)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetoiso)
    
    Returns an ISO 8601-compliant string representation of the DateTime
    
*   [`_DateTime_`.`**toLocal()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetolocal)
    
    Converts a DateTime to the workflow’s local time zone. The DateTime still represents the same moment unless specified in the parameters. The workflow’s time zone can be set in the workflow settings.
    
*   [`_DateTime_`.`**toLocaleString(formatOpts)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetolocalestring)
    
    Returns a localised string representing the DateTime, i.e. in the language and format corresponding to its locale. Defaults to the system's locale if none specified.
    
*   [`_DateTime_`.`**toMillis()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetomillis)
    
    Returns a Unix timestamp in milliseconds (the number elapsed since 1st Jan 1970)
    
*   [`_DateTime_`.`**toRelative(options)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetorelative)
    
    Returns a textual representation of the time relative to now, e.g. ‘in two days’. Rounds down by default.
    
*   [`_DateTime_`.`**toSeconds()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetoseconds)
    
    Returns a Unix timestamp in seconds (the number elapsed since 1st Jan 1970)
    
*   [`_DateTime_`.`**toString()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetostring)
    
    Returns a string representation of the DateTime. Similar to `toISO()`. For more formatting options, see `format()` or `toLocaleString()`.
    
*   [`_DateTime_`.`**toUTC(offset, opts)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetoutc)
    
    Converts a DateTime to the UTC time zone. The DateTime still represents the same moment unless specified in the parameters. Use `setZone()` to convert to other zones.
    
*   [`_DateTime_`.`**weekday**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeweekday)
    
    The day of the week. 1 is Monday and 7 is Sunday.
    
*   [`_DateTime_`.`**weekdayLong**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeweekdaylong)
    
    The textual long weekday name, e.g. 'Wednesday'. Defaults to the system's locale if no locale has been specified.
    
*   [`_DateTime_`.`**weekdayShort**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeweekdayshort)
    
    The textual abbreviated weekday name, e.g. 'Wed'. Defaults to the system's locale if no locale has been specified.
    
*   [`_DateTime_`.`**weekNumber**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeweeknumber)
    
    The week number of the year (1-52ish)
    
*   [`_DateTime_`.`**year**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeyear)
    
    The year
    
*   [`_DateTime_`.`**zone**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimezone)
    
    The time zone associated with the DateTime
    

ExecData[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#execdata)

--------------------------------------------------------------------------------------------------

*   [`$exec`.`**customData**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata#dollarexeccustomdata)
    
    Set and get custom execution data (e.g. to filter executions by). You can also do this with the ‘Execution Data’ node. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [`$exec`.`**id**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata#dollarexecid)
    
    The ID of the current workflow execution
    
*   [`$exec`.`**mode**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata#dollarexecmode)
    
    Can be one of 3 values: either `test` (meaning the execution was triggered by clicking a button in n8n) or `production` (meaning the execution was triggered automatically). When running workflow tests, `evaluation` is used.
    
*   [`$exec`.`**resumeFormUrl**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata#dollarexecresumeformurl)
    
    The URL to access a form generated by the [’Wait’ node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait)
    .
    
*   [`$exec`.`**resumeUrl**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata#dollarexecresumeurl)
    
    The webhook URL to call to resume a workflow waiting at a [’Wait’ node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait)
    .
    

HTTPResponse[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#httpresponse)

----------------------------------------------------------------------------------------------------------

*   [`$response`.`**body**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/httpresponse#dollarresponsebody)
    
    The body of the response object from the last HTTP call. Only available in the ‘HTTP Request’ node
    
*   [`$response`.`**headers**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/httpresponse#dollarresponseheaders)
    
    The headers returned by the last HTTP call. Only available in the ‘HTTP Request’ node.
    
*   [`$response`.`**statusCode**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/httpresponse#dollarresponsestatuscode)
    
    The HTTP status code returned by the last HTTP call. Only available in the ‘HTTP Request’ node.
    
*   [`$response`.`**statusMessage**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/httpresponse#dollarresponsestatusmessage)
    
    An optional message regarding the request status. Only available in the ‘HTTP Request’ node.
    

Item[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#item)

------------------------------------------------------------------------------------------

*   [`$item`.`**binary**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/item#dollaritembinary)
    
    Returns any binary data the item contains
    
*   [`$item`.`**json**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/item#dollaritemjson)
    
    Returns the JSON data the item contains. [More info](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
    

NodeInputData[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#nodeinputdata)

------------------------------------------------------------------------------------------------------------

*   [`$input`.`**all(branchIndex?, runIndex?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputall)
    
    Returns an array of the current node’s input items
    
*   [`$input`.`**first(branchIndex?, runIndex?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputfirst)
    
    Returns the current node’s first input item
    
*   [`$input`.`**item**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputitem)
    
    Returns the input item currently being processed
    
*   [`$input`.`**last(branchIndex?, runIndex?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputlast)
    
    Returns the current node’s last input item
    
*   [`$input`.`**params**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputparams)
    
    The configuration settings of the current node. These are the parameters you fill out within the node when configuring it (e.g. its operation).
    

NodeOutputData[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#nodeoutputdata)

--------------------------------------------------------------------------------------------------------------

*   [`$()`.`**all(branchIndex?, runIndex?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarall)
    
    Returns an array of the node’s output items
    
*   [`$()`.`**first(branchIndex?, runIndex?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarfirst)
    
    Returns the first item output by the node
    
*   [`$()`.`**isExecuted**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarisexecuted)
    
    Is `true` if the node has executed, `false` otherwise
    
*   [`$()`.`**item**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollaritem)
    
    Returns the matching item, i.e. the one used to produce the current item in the current node. [More info](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
    
*   [`$()`.`**itemMatching(currentItemIndex?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollaritemmatching)
    
    Returns the matching item, i.e. the one used to produce the item in the current node at the specified index. [More info](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
    
*   [`$()`.`**last(branchIndex?, runIndex?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarlast)
    
    Returns the last item output by the node
    
*   [`$()`.`**params**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarparams)
    
    The configuration settings of the given node. These are the parameters you fill out within the node’s UI (e.g. its operation).
    

Number[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#number)

----------------------------------------------------------------------------------------------

*   [`_Number_`.`**abs()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberabs)
    
    Returns the number’s absolute value, i.e. removes any minus sign
    
*   [`_Number_`.`**ceil()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberceil)
    
    Rounds the number up to the next whole number
    
*   [`_Number_`.`**floor()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberfloor)
    
    Rounds the number down to the nearest whole number
    
*   [`_Number_`.`**format(locale?, options?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberformat)
    
    Returns a formatted string representing the number. Useful for formatting for a specific language or currency. The same as <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Intl/NumberFormat/NumberFormat”>`Intl.NumberFormat()`.
    
*   [`_Number_`.`**isEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberisempty)
    
    Returns `true` if the number is `0`, `NaN`, `null`, or `undefined`. Returns `false` for every other number.
    
*   [`_Number_`.`**isEven()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberiseven)
    
    Returns `true` if the number is even. Throws an error if the number isn’t a whole number.
    
*   [`_Number_`.`**isInteger()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberisinteger)
    
    Returns `true` if the number is a whole number
    
*   [`_Number_`.`**isNotEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberisnotempty)
    
    Returns `true` for every number except `0` and `NaN`. Returns `false` if the number is `0`, `NaN`, `null`, or `undefined`. This is the inverse of `isEmpty()`.
    
*   [`_Number_`.`**isOdd()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberisodd)
    
    Returns `true` if the number is odd. Throws an error if the number isn’t a whole number.
    
*   [`_Number_`.`**round(decimalPlaces?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberround)
    
    Returns the number rounded to the nearest whole number (or specified number of decimal places)
    
*   [`_Number_`.`**toBoolean()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numbertoboolean)
    
    Converts the number to a boolean value. `0` becomes `false`; everything else becomes `true`.
    
*   [`_Number_`.`**toDateTime(format?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numbertodatetime)
    
    Converts a numerical timestamp into a DateTime. The format of the timestamp must be specified if it’s not in milliseconds. Uses the time zone in n8n (or in the workflow’s settings).
    
*   [`_Number_`.`**toLocaleString(locales?, options?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numbertolocalestring)
    
    Returns a localised string representing the number, i.e. in the language and format corresponding to its locale. Defaults to the system's locale if none specified.
    
*   [`_Number_`.`**toString(radix?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numbertostring)
    
    Converts the number to a simple textual representation. For more formatting options, see `toLocaleString()`.
    

Object[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#object)

----------------------------------------------------------------------------------------------

*   [`_Object_`.`**compact()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectcompact)
    
    Removes all fields that have empty values, i.e. are `null` or `""`
    
*   [`_Object_`.`**hasField(name)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objecthasfield)
    
    Returns `true` if there is a field called `name`. Only checks top-level keys. Comparison is case-sensitive.
    
*   [`_Object_`.`**isEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectisempty)
    
    Returns `true` if the Object has no keys (fields) set or is `null` or `undefined`
    
*   [`_Object_`.`**isNotEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectisnotempty)
    
    Returns `true` if the Object has at least one key (field) set
    
*   [`_Object_`.`**keepFieldsContaining(value)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectkeepfieldscontaining)
    
    Removes any fields whose values don’t at least partly match the given `value`. Comparison is case-sensitive. Fields that aren’t strings will always be removed.
    
*   [`_Object_`.`**keys()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectkeys)
    
    Returns an array with all the field names (keys) the object contains. The same as JavaScript’s `Object.keys(obj)`.
    
*   [`_Object_`.`**merge(otherObject)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectmerge)
    
    Merges the two Objects into a single one. If a key (field name) exists in both Objects, the value from the first (base) Object is used.
    
*   [`_Object_`.`**removeField(key)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectremovefield)
    
    Removes a field from the Object. The same as JavaScript’s `delete`.
    
*   [`_Object_`.`**removeFieldsContaining(value)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectremovefieldscontaining)
    
    Removes keys (fields) whose values at least partly match the given `value`. Comparison is case-sensitive. Fields that aren’t strings are always kept.
    
*   [`_Object_`.`**toJsonString()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objecttojsonstring)
    
    Converts the Object to a JSON string. Similar to JavaScript’s `JSON.stringify()`.
    
*   [`_Object_`.`**urlEncode()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objecturlencode)
    
    Generates a URL parameter string from the Object’s keys and values. Only top-level keys are supported.
    
*   [`_Object_`.`**values()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectvalues)
    
    Returns an array with all the values of the fields the Object contains. The same as JavaScript’s `Object.values(obj)`.
    

PrevNodeData[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#prevnodedata)

----------------------------------------------------------------------------------------------------------

*   [`**name**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata#name)
    
    The name of the node that the current input came from.
    

Always uses the current node’s first input connector if there is more than one (e.g. in the ‘Merge’ node).

*   [`**outputIndex**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata#outputindex)
    
    The index of the output connector that the current input came from. Use this when the previous node had multiple outputs (such as an ‘If’ or ‘Switch’ node).
    

Always uses the current node’s first input connector if there is more than one (e.g. in the ‘Merge’ node).

*   [`**runIndex**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata#runindex)
    
    The run of the previous node that generated the current input.
    

Always uses the current node’s first input connector if there is more than one (e.g. in the ‘Merge’ node).

Root[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#root)

------------------------------------------------------------------------------------------

*   [`**$(nodeName)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollar)
    
    Returns the data of the specified node
    
*   [`**$binary**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarbinary)
    
    Returns any binary input data to the current node, for the current item. Shorthand for `$input.item.binary`.
    
*   [`**$execution**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarexecution)
    
    Retrieve or set metadata for the current execution
    
*   [`**$fromAI(key, description?, type?, defaultValue?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarfromai)
    
    Use when a large language model should provide the value of a node parameter. Consider providing a description for better results.
    
*   [`**$if(condition, valueIfTrue, valueIfFalse)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarif)
    
    Returns one of two values depending on the `condition`. Similar to the `?` operator in JavaScript.
    
*   [`**$ifEmpty(value, valueIfEmpty)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarifempty)
    
    Returns the first parameter if it isn’t empty, otherwise returns the second parameter. The following count as empty: `””`, `[]`, `{}`, `null`, `undefined`
    
*   [`**$input**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarinput)
    
    The input data of the current node
    
*   [`**$itemIndex**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollaritemindex)
    
    The position of the item currently being processed in the list of input items
    
*   [`**$jmespath(obj, expression)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarjmespath)
    
    Extracts data from an object (or array of objects) using a <a href=”/code/cookbook/jmespath/”>JMESPath expression. Useful for querying complex, nested objects. Returns `undefined` if the expression is invalid.
    
*   [`**$json**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarjson)
    
    Returns the JSON input data to the current node, for the current item. Shorthand for `$input.item.json`. [More info](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
    
*   [`**$max(num1, num2, …, numN)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarmax)
    
    Returns the highest of the given numbers
    
*   [`**$min(num1, num2, …, numN)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarmin)
    
    Returns the lowest of the given numbers
    
*   [`**$nodeVersion**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarnodeversion)
    
    The version of the current node (as displayed at the bottom of the nodes’s settings pane)
    
*   [`**$now**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarnow)
    
    A DateTime representing the current moment.
    

Uses the workflow’s time zone (which can be changed in the workflow settings).

*   [`**$pageCount**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarpagecount)
    
    The number of results pages the node has fetched. Only available in the ‘HTTP Request’ node.
    
*   [`**$parameter**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarparameter)
    
    The configuration settings of the current node. These are the parameters you fill out within the node’s UI (e.g. its operation).
    
*   [`**$prevNode**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarprevnode)
    
    Information about the node that the current input came from.
    

When in a ‘Merge’ node, always uses the first input connector.

*   [`**$request**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarrequest)
    
    The request object sent during the last run of the node. Only available in the ‘HTTP Request’ node.
    
*   [`**$response**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarresponse)
    
    The response returned by the last HTTP call. Only available in the ‘HTTP Request’ node.
    
*   [`**$runIndex**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarrunindex)
    
    The index of the current run of the current node execution. Starts at 0.
    
*   [`**$secrets**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarsecrets)
    
    The secrets from an [external secrets vault](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets)
    , if configured. Secret values are never displayed to the user. Only available in credential fields.
    
*   [`**$today**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollartoday)
    
    A DateTime representing midnight at the start of the current day.
    

Uses the instance’s time zone (unless overridden in the workflow’s settings).

*   [`**$vars**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarvars)
    
    The [variables](https://docs.n8n.io/build/code-in-n8n/define-custom-variables)
     available to the workflow
    
*   [`**$workflow**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarworkflow)
    
    Information about the current workflow
    

String[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#string)

----------------------------------------------------------------------------------------------

*   [`_String_`.`**base64Encode()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringbase64decode)
    
    Converts plain text to a base64-encoded string
    
*   [`_String_`.`**base64Encode()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringbase64encode)
    
    Converts a base64-encoded string to plain text
    
*   [`_String_`.`**concat(string1, string2?, ..., stringN?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringconcat)
    
    Joins one or more strings onto the end of the base string. Alternatively, use the `+` operator (see examples).
    
*   [`_String_`.`**extractDomain()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringextractdomain)
    
    If the string is an email address or URL, returns its domain (or `undefined` if nothing found).
    

If the string also contains other content, try using `extractEmail()` or `extractUrl()` first.

*   [`_String_`.`**extractEmail()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringextractemail)
    
    Extracts the first email found in the string. Returns `undefined` if none is found.
    
*   [`_String_`.`**extractUrl()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringextracturl)
    
    Extracts the first URL found in the string. Returns `undefined` if none is found. Only recognizes full URLs, e.g. those starting with `http`.
    
*   [`_String_`.`**extractUrlPath()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringextracturlpath)
    
    Returns the part of a URL after the domain, or `undefined` if no URL found.
    

If the string also contains other content, try using `extractUrl()` first.

*   [`_String_`.`**hash(algo?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringhash)
    
    Returns the string hashed with the given algorithm. Defaults to md5 if not specified.
    
*   [`_String_`.`**includes(searchString, start?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringincludes)
    
    Returns `true` if the string contains the `searchString`. Case-sensitive.
    
*   [`_String_`.`**indexOf(searchString, start?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringindexof)
    
    Returns the index (position) of the first occurrence of `searchString` within the base string, or -1 if not found. Case-sensitive.
    
*   [`_String_`.`**isDomain()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisdomain)
    
    Returns `true` if the string is a domain
    
*   [`_String_`.`**isEmail()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisemail)
    
    Returns `true` if the string is an email
    
*   [`_String_`.`**isEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisempty)
    
    Returns `true` if the string has no characters or is `null` or `undefined`
    
*   [`_String_`.`**isNotEmpty()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisnotempty)
    
    Returns `true` if the string has at least one character
    
*   [`_String_`.`**isNumeric()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisnumeric)
    
    Returns `true` if the string represents a number
    
*   [`_String_`.`**isUrl()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisurl)
    
    Returns `true` if the string is a valid URL
    
*   [`_String_`.`**length**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringlength)
    
    The number of characters in the string
    
*   [`_String_`.`**match(regexp)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringmatch)
    
    Matches the string against a <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular\_expressions”>regular expression. Returns an array containing the first match, or all matches if the `g` flag is set in the regular expression. Returns `null` if no matches are found.
    

For checking whether text is present, consider `includes()` instead.

*   [`_String_`.`**parseJson()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringparsejson)
    
    Returns the JavaScript Object or value represented by the string, or `undefined` if the string isn’t valid JSON. Single-quoted JSON is not supported.
    
*   [`_String_`.`**quote(mark?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringquote)
    
    Wraps a string in quotation marks, and escapes any quotation marks already in the string. Useful when constructing JSON, SQL, etc.
    
*   [`_String_`.`**removeMarkdown()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringremovemarkdown)
    
    Removes any Markdown formatting from the string. Also removes HTML tags.
    
*   [`_String_`.`**removeTags()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringremovetags)
    
    Removes tags, such as HTML or XML, from the string
    
*   [`_String_`.`**replace(pattern, replacement)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringreplace)
    
    Returns a string with the first occurrence of `pattern` replaced by `replacement`.
    

To replace all occurrences, use `replaceAll()` instead.

*   [`_String_`.`**replaceAll(pattern, replacement)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringreplaceall)
    
    Returns a string with all occurrences of `pattern` replaced by `replacement`
    
*   [`_String_`.`**replaceSpecialChars()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringreplacespecialchars)
    
    Replaces special characters in the string with the closest ASCII character
    
*   [`_String_`.`**search(regexp)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringsearch)
    
    Returns the index (position) of the first occurrence of a pattern within the string, or -1 if not found. The pattern is specified using a <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular\_expressions”>regular expression. To use text instead, see `indexOf()`.
    
*   [`_String_`.`**slice(start, end?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringslice)
    
    Extracts a fragment of the string at the given position. For more advanced extraction, see `match()`.
    
*   [`_String_`.`**split(separator?, limit?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringsplit)
    
    Splits the string into an array of substrings. Each split is made at the `separator`, and the separator isn’t included in the output.
    

The opposite of using `join()` on an array.

*   [`_String_`.`**startsWith(searchString, start?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringstartswith)
    
    Returns `true` if the string starts with `searchString`. Case-sensitive.
    
*   [`_String_`.`**substring(start, end?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringsubstring)
    
    Extracts a fragment of the string at the given position. For more advanced extraction, see `match()`.
    
*   [`_String_`.`**toBoolean()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtoboolean)
    
    Converts the string to a boolean value. `0`, `false` and `no` resolve to `false`, everything else to `true`. Case-insensitive.
    
*   [`_String_`.`**toDateTime()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtodatetime)
    
    Converts the string to a DateTime. Useful for further transformation. Supported formats for the string are ISO 8601, HTTP, RFC2822, SQL and Unix timestamp in milliseconds.
    

To parse other formats, use <a href=”https://moment.github.io/luxon/api-docs/index.html#datetimefromformat”> `DateTime.fromFormat()`.

*   [`_String_`.`**toJsonString()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtojsonstring)
    
    Prepares the string to be inserted into a JSON object. Escapes any quotes and special characters (e.g. new lines), and wraps the string in quotes.
    

The same as JavaScript’s `JSON.stringify()`.

*   [`_String_`.`**toLowerCase()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtolowercase)
    
    Converts all letters in the string to lower case
    
*   [`_String_`.`**toNumber()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtonumber)
    
    Converts a string representing a number to a number. Throws an error if the string doesn’t start with a valid number.
    
*   [`_String_`.`**toSentenceCase()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtosentencecase)
    
    Changes the capitalization of the string to sentence case. The first letter of each sentence is capitalized and all others are lowercased.
    
*   [`_String_`.`**toSnakeCase()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtosnakecase)
    
    Changes the format of the string to snake case. Spaces and dashes are replaced by `_`, symbols are removed and all letters are lowercased.
    
*   [`_String_`.`**toTitleCase()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtotitlecase)
    
    Changes the capitalization of the string to title case. The first letter of each word is capitalized and the others left unchanged. Short prepositions and conjunctions aren’t capitalized (e.g. ‘a’, ‘the’).
    
*   [`_String_`.`**toUpperCase()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtouppercase)
    
    Converts all letters in the string to upper case (capitals)
    
*   [`_String_`.`**trim()**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtrim)
    
    Removes whitespace from both ends of the string. Whitespace includes new lines, tabs, spaces, etc.
    
*   [`_String_`.`**urlDecode(allChars?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringurldecode)
    
    Decodes a URL-encoded string. Replaces any character codes in the form of `%XX` with their corresponding characters.
    
*   [`_String_`.`**urlEncode(allChars?)**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringurlencode)
    
    Encodes the string so that it can be used in a URL. Spaces and special characters are replaced with codes of the form `%XX`.
    

WorkflowData[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#workflowdata)

----------------------------------------------------------------------------------------------------------

*   [`$workflow`.`**active**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/workflowdata#dollarworkflowactive)
    
    Whether the workflow is active
    
*   [`$workflow`.`**id**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/workflowdata#dollarworkflowid)
    
    The workflow ID. Can also be found in the workflow’s URL.
    
*   [`$workflow`.`**name**`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/workflowdata#dollarworkflowname)
    
    The name of the workflow, as shown at the top of the editor
    

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference#related-resources)

--------------------------------------------------------------------------------------------------------------------

*   [Transform data](https://docs.n8n.io/build/work-with-data/transform-data)
    
*   [Approaches for transforming data](https://docs.n8n.io/build/work-with-data/transform-data/approaches-for-transforming-data)
    
*   [Expressions for data transformation](https://docs.n8n.io/build/work-with-data/transform-data/expressions-for-data-transformation)
    

[PreviousExpressions for data transformation](https://docs.n8n.io/build/work-with-data/transform-data/expressions-for-data-transformation)
[NextArray](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array)

Last updated 10 days ago

Was this helpful?