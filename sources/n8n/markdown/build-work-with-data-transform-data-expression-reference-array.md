For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array.md)
.

`_Array_`.`**append()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayappend)

---------------------------------------------------------------------------------------------------------------------------

**Description:** Adds new elements to the end of the array. Similar to `push()`, but returns the modified array. Consider using spread syntax instead (see examples).

**Syntax:** `_Array_`.append(elem1, elem2?, ..., elemN?)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `elem1` (any) - The first element to append
    
*   `elem2` (any) - optional - The second element to append
    
*   `elemN` (any) - optional - The Nth element to append
    

**Examples:**

Copy

    // arr = ['forget', 'me']
    arr.append('not') //=> arr = ['forget', 'me', 'not']

Copy

    // arr = [9, 0, 2]
    arr.append(1, 0) //=> [9, 0, 2, 1, 0]
    
    // Consider using spread syntax instead
    [...arr, 1, 0]  //=> [9, 0, 2, 1, 0]

`_Array_`.`**average()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayaverage)

-----------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the average of the numbers in the array. Throws an error if there are any non-numbers.

**Syntax:** `_Array_`.average()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = [12, 1, 5]
    arr.average() //=> 6

`_Array_`.`**chunk()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraychunk)

-------------------------------------------------------------------------------------------------------------------------

**Description:** Splits the array into an array of sub-arrays, each with the given length

**Syntax:** `_Array_`.chunk(length)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `length` (Number) - The number of elements in each chunk
    

**Examples:**

Copy

    // arr = [1, 2, 3, 4, 5, 6]
    arr.chunk(2) //=> [ [1,2], [3,4], [5,6] ]

`_Array_`.`**compact()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraycompact)

-----------------------------------------------------------------------------------------------------------------------------

**Description:** Removes any empty values from the array. `null`, `""` and `undefined` count as empty.

**Syntax:** `_Array_`.compact()

**Returns:** Array

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = [2, null, 1, ""]
    arr.compact() //=> [2, 1]

`_Array_`.`**concat()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayconcat)

---------------------------------------------------------------------------------------------------------------------------

**Description:** Joins one or more arrays onto the end of the base array

**Syntax:** `_Array_`.concat(array2, array3?, ... arrayN?)

**Returns:** Array

**Source:** JavaScript function

**Parameters:**

*   `array2` (Array) - The first array to be joined on the end of the base array
    
*   `array3` (Array) - optional - The second array to be joined on to the end of the base array
    
*   `arrayN` (Array) - optional - The Nth array to be joined on to the end of the base array
    

**Examples:**

Copy

    // arr1 = ['Nathan', 'Jan']
    arr1.concat(['Steve', 'Bill']) // ['Nathan', 'Jan', 'Steve', 'Bill']

Copy

    // arr1 = [5, 4]
    // arr2 = [100, 101]
    // arr3 = ['a', 'b']
    arr1.concat(arr2, arr3) // [5, 4, 100, 101, 'a', 'b']

`_Array_`.`**difference()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraydifference)

-----------------------------------------------------------------------------------------------------------------------------------

**Description:** Compares two arrays. Returns all elements in the base array that aren't present in `otherArray`.

**Syntax:** `_Array_`.difference(otherArray)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `otherArray` (Array) - The array to compare to the base array
    

**Examples:**

Copy

    // arr = [1, 2, 3]
    arr.difference([2, 3]) //=> [1]

`_Array_`.`**filter()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayfilter)

---------------------------------------------------------------------------------------------------------------------------

**Description:** Returns an array with only the elements satisfying a condition. The condition is a function that returns `true` or `false`.

**Syntax:** `_Array_`.filter(function(element, index?, array?), thisValue?)

**Returns:** Array

**Source:** JavaScript function

**Parameters:**

*   `function()` (function) - A function to run for each array element. If it returns `true`, the element will be kept. Consider using <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow\_functions”>arrow function notation to save space.
    
*   `element` (any) - The value of the current element
    
*   `index` (Number) - optional - The position of the current element in the array (starting at 0)
    
*   `array` (Array) - optional - The array being processed. Rarely needed.
    
*   `thisValue` (any) - optional - A value passed to the function as its `this` value. Rarely needed.
    

**Examples:**

Copy

    // Keep ages over 18 (using arrow function notation):
    // ages = [12, 33, 16, 40]
    ages.filter(age => (age > 18)) //=> [33, 40]

Copy

    // Keep names under 5 letters long (using arrow function notation):
    // names = ['Nathan', 'Bob', 'Sebastian']
    ages.filter(age => (age.length < 5)) //=> ["Bob"]
    
    // Or using traditional function notation:
    ages.filter(function(age){return age.length < 5}) //=> ["Bob"]

Copy

    // Keep numbers at odd indexes
    // nums = [1, 7, 3, 10, 5]
    ages.filter((num, index) => {return index%2 != 0}) //=> [7, 10]

`_Array_`.`**find()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayfind)

-----------------------------------------------------------------------------------------------------------------------

**Description:** Returns the first element from the array that satisfies the provided condition. The condition is a function that returns `true` or `false`. Returns `undefined` if no matches are found.

If you need all matching elements, use `filter()`.

**Syntax:** `_Array_`.find(function(element, index?, array?), thisValue?)

**Returns:** any

**Source:** JavaScript function

**Parameters:**

*   `function()` (function) - A function to run for each array element. As soon as it returns `true`, that element will be returned. Consider using <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow\_functions”>arrow function notation to save space.
    
*   `element` (any) - The value of the current element
    
*   `index` (Number) - optional - The position of the current element in the array (starting at 0)
    
*   `array` (Array) - optional - The array of the current element. Rarely needed.
    
*   `thisValue` (any) - optional - A value passed to the function as its `this` value. Rarely needed.
    

**Examples:**

Copy

    // Find first age over 18 (using arrow function notation):
    // ages = [12, 33, 16, 40]
    ages.find(age => (age > 18)) //=> 33

Copy

    // Find first name under 5 letters long (using arrow function notation):
    // names = ['Nathan', 'Bob', 'Sebastian']
    ages.find(age => (age.length < 5)) //=> 'Bob'
    
    // Or using traditional function notation:
    ages.find(function(age){return age.length < 5}) //=> 'Bob'

`_Array_`.`**first()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayfirst)

-------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the first element of the array

**Syntax:** `_Array_`.first()

**Returns:** any

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = ['quick', 'brown', 'fox']
    arr.first() //=> 'quick'

`_Array_`.`**includes()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayincludes)

-------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the array contains the specified element

**Syntax:** `_Array_`.includes(element, start?)

**Returns:** Boolean

**Source:** JavaScript function

**Parameters:**

*   `element` (any) - The value to search the array for
    
*   `start` (Number) - optional - The index to start looking from
    

**Examples:**

Copy

    // names = ["Bob", "Bill", "Nat"];
    names.includes("Nat") //=> true
    names.includes("Nathan") //=> false

`_Array_`.`**indexOf()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayindexof)

-----------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the position of the first matching element in the array, or -1 if the element isn’t found. Positions start at 0.

**Syntax:** `_Array_`.indexOf(element, start?)

**Returns:** Number

**Source:** JavaScript function

**Parameters:**

*   `element` (any) - The value to look for
    
*   `start` (Number) - optional - The index to start looking from
    

**Examples:**

Copy

    // names = ["Bob", "Bill", "Nat"];
    names.indexOf("Nat") //=> 2

Copy

    // names = ["Bob", "Bill", "Nat"];
    names.indexOf("Nathan") //=> -1

`_Array_`.`**intersection()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayintersection)

---------------------------------------------------------------------------------------------------------------------------------------

**Description:** Compares two arrays. Returns all elements in the base array that are also present in the other array.

**Syntax:** `_Array_`.intersection(otherArray)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `otherArray` (Array) - The array to compare to the base array
    

**Examples:**

Copy

    // arr = [1, 2]
    arr.intersection([2, 3]) //=> [2]

`_Array_`.`**isEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayisempty)

-----------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the array has no elements or is `null` or `undefined`

**Syntax:** `_Array_`.isEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = []
    arr.isEmpty() //=> true

Copy

    // arr = ['quick', 'brown', 'fox']
    arr.isEmpty() //=> false

`_Array_`.`**isNotEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayisnotempty)

-----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the array has at least one element

**Syntax:** `_Array_`.isNotEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = ['quick', 'brown', 'fox']
    arr.isNotEmpty() //=> true

Copy

    // arr = []
    arr.isNotEmpty() //=> false

`_Array_`.`**join()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayjoin)

-----------------------------------------------------------------------------------------------------------------------

**Description:** Merges all elements of the array into a single string, with an optional separator between each element.

The opposite of `split()`.

**Syntax:** `_Array_`.join(separator?)

**Returns:** String

**Source:** JavaScript function

**Parameters:**

*   `separator` (String) - optional - The character(s) to insert between each element
    

**Examples:**

Copy

    // arr = ['Wind', 'Water', 'Fire']
    a.join(" + ") //=> 'Wind + Water + Fire'

Copy

    // arr = ['Wind', 'Water', 'Fire']
    a.join() //=> 'Wind,Water,Fire'
    a.join("") //=> 'WindWaterFire'

`_Array_`.`**last()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraylast)

-----------------------------------------------------------------------------------------------------------------------

**Description:** Returns the last element of the array

**Syntax:** `_Array_`.last()

**Returns:** any

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = ['quick', 'brown', 'fox']
    arr.last() //=> 'fox'
    

`_Array_`.`**length**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraylength)

-------------------------------------------------------------------------------------------------------------------------

**Description:** The number of elements in the array

**Syntax:** `_Array_`.length

**Returns:** Number

**Source:** JavaScript function

**Examples:**

Copy

    // names = ["Bob", "Bill", "Nat"];
    names.length //=> 3

`_Array_`.`**map()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraymap)

---------------------------------------------------------------------------------------------------------------------

**Description:** Creates a new array by applying a function to each element of the original array

**Syntax:** `_Array_`.map(function(element, index?, array?), thisValue?)

**Returns:** Array

**Source:** JavaScript function

**Parameters:**

*   `function()` (function) - A function to run for each array element. In the new array, the output of this function takes the place of the element. Consider using <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow\_functions”>arrow function notation to save space.
    
*   `element` (any) - The value of the current element
    
*   `index` (Number) - optional - The position of the current element in the array (starting at 0)
    
*   `array` (Array) - optional - The array of the current element. Rarely needed.
    
*   `thisValue` (any) - optional - A value passed to the function as its `this` value. Rarely needed.
    

**Examples:**

Copy

    // Double all numbers (using arrow function notation):
    // nums = [12, 33, 16]
    nums.map(num => num*2) //=> [24, 66, 32]

Copy

    // Convert elements to uppercase (using arrow function notation):
    // words = ['hello', 'old', 'chap']
    words.map(word => word.toUpperCase()) //=> ['HELLO', 'OLD', 'CHAP']]
    
    // Or using traditional function notation:
    words.map(function(word){return word.toUpperCase()}) //=> ['HELLO', 'OLD', 'CHAP']]

`_Array_`.`**max()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraymax)

---------------------------------------------------------------------------------------------------------------------

**Description:** Returns the largest number in the array. Throws an error if there are any non-numbers.

**Syntax:** `_Array_`.max()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = [1, 12, 5]
    arr.max() //=> 12
    

`_Array_`.`**mergeIntoObject()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraymergeintoobject)

---------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Merges two arrays of Objects into a single Object, by merging the key-value pairs of each element. If the arrays are different lengths, keeps the elements from the longer array.

**Syntax:** `_Array_`.mergeIntoObject(otherArray)

**Returns:** Object

**Source:** Custom n8n functionality

**Parameters:**

*   `otherArray` (Array) - The array of Objects to merge with the base array
    

**Examples:**

Copy

    // arr = [{ name: 'Nathan' }, { age: 42 }]
    arr.mergeIntoObject([{ city: 'Berlin' }]) //=> { name: 'Nathan', age: 42, city: 'Berlin' }

`_Array_`.`**min()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraymin)

---------------------------------------------------------------------------------------------------------------------

**Description:** Returns the smallest number in the array. Throws an error if there are any non-numbers.

**Syntax:** `_Array_`.min()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = [12, 1, 5]
    arr.min() //=> 1

`_Array_`.`**pluck()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraypluck)

-------------------------------------------------------------------------------------------------------------------------

**Description:** Returns an array containing the values of the given field(s) in each Object of the array. Ignores any array elements that aren’t Objects or don’t have a key matching the field name(s) provided.

**Syntax:** `_Array_`.pluck(fieldName1?, fieldName2?, …)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `fieldName1` (String) - optional - The first key to retrieve the value of
    
*   `fieldName2` (String) - optional - The second key to retrieve the value of
    

**Examples:**

Copy

    // arr = [{'name':'Nathan','age':42},{'name':'Jan','city':'Berlin'}]
    arr.pluck('name') //=> ["Nathan", "Jan"]

Copy

    // arr = [{'name':'Nathan','age':42},{'name':'Jan','city':'Berlin'}]
    arr.pluck('age') //=> [42]

`_Array_`.`**randomItem()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayrandomitem)

-----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a randomly-chosen element from the array

**Syntax:** `_Array_`.randomItem()

**Returns:** any

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = ['quick', 'brown', 'fox']
    arr.randomItem() //=> 'brown'
    arr.randomItem() //=> 'quick'

`_Array_`.`**reduce()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayreduce)

---------------------------------------------------------------------------------------------------------------------------

**Description:** Reduces an array to a single value by applying a function to each element. The function combines the current element with the result of reducing the previous elements, producing a new result.

**Syntax:** `_Array_`.reduce(function(prevResult, currentElem, currentIndex?, array?), initResult)

**Source:** JavaScript function

**Parameters:**

*   `function()` (function) - A function to run for each array element. Takes the accumulated result and the current element, and returns a new accumulated result. Consider using <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow\_functions”>arrow function notation to save space.
    
*   `prevResult` (any) - The accumulated result from applying the function to previous elements. When processing the first element, it’s set to `initResult` (or the first array element if not specified).
    
*   `currentElem` (any) - The value in the array currently being processed
    
*   `currentIndex` (Number) - optional - The position of the current element in the array (starting at 0)
    
*   `array` (Array) - optional - The array being processed. Rarely needed.
    
*   `initResult` (any) - optional - The initial value of the prevResult, used when calling the function on the first array element. When not specified it’s set to the first array element, and the first function call is on the second array element instead of the first.
    

**Examples:**

Copy

    // Sum numbers (using arrow function notation):
    // nums = [12, 33, 16]
    nums.reduce((result, num) => (result+num), 0) //=> 61

Copy

    // Join letters and uppercase (using arrow function notation):
    // chars = ['a', 'b', 'c']
    chars.reduce((result, char) => (result+char.toUpperCase()), '') //=> 'ABC'
    
    // Or using traditional function notation:
    chars.reduce(function(result, char){return result+char.toUpperCase()}, '') //=> 'ABC'

`_Array_`.`**removeDuplicates()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayremoveduplicates)

-----------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Removes any re-occurring elements from the array

**Syntax:** `_Array_`.removeDuplicates(keys?)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `keys` (String) - optional - For use on arrays of Objects. A key, or comma-separated list of keys to restrict the check to. If omitted, all keys are checked.
    

**Examples:**

Copy

    // arr = ['quick', 'brown', 'quick']
    arr.removeDuplicates() //=> ['quick', 'brown']

`_Array_`.`**renameKeys()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayrenamekeys)

-----------------------------------------------------------------------------------------------------------------------------------

**Description:** Changes all matching keys (field names) of any Objects in the array. Rename more than one key by adding extra arguments, i.e. `from1, to1, from2, to2, ...`.

**Syntax:** `_Array_`.renameKeys(from, to)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `from` (String) - The key to rename
    
*   `to` (String) - The new key name
    

**Examples:**

Copy

    // arr = [{'name':'bob'},{'name':'meg'}]
    arr.renameKeys('name', 'x') //=> [{"x": "bob"},{"x": "meg"}]]

`_Array_`.`**reverse()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayreverse)

-----------------------------------------------------------------------------------------------------------------------------

**Description:** Reverses the order of the elements in the array

**Syntax:** `_Array_`.reverse()

**Returns:** Array

**Source:** JavaScript function

**Examples:**

Copy

    // arr = ['dog', 'bites', 'man']
    arr.reverse() //=> ['man', 'bites', 'dog']

`_Array_`.`**slice()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayslice)

-------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a portion of the array, from the `start` index up to (but not including) the `end` index. Indexes start at 0.

**Syntax:** `_Array_`.slice(start, end)

**Returns:** Array

**Source:** JavaScript function

**Parameters:**

*   `start` (Number) - optional - The position to start from. Positions start at 0. Negative numbers count back from the end of the array.
    
*   `end` (Number) - optional - The position to select up to. The element at the end position is not included. Negative numbers select from the end of the array. If omitted, will extract to the end of the array.
    

**Examples:**

Copy

    // arr = [1, 2, 3, 4, 5]
    arr.slice(2, 4) //=> [3, 4]

Copy

    // arr = [1, 2, 3, 4, 5]
    arr.slice(2) //=> [3, 4, 5]

Copy

    // arr = [1, 2, 3, 4, 5]
    arr.slice(-2) //=> [4, 5]

`_Array_`.`**smartJoin()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraysmartjoin)

---------------------------------------------------------------------------------------------------------------------------------

**Description:** Creates a single Object from an array of Objects. Each Object in the array provides one field for the returned Object. Each Object in the array must contain a field with the key name and a field with the value.

**Syntax:** `_Array_`.smartJoin(keyField, nameField)

**Returns:** Object

**Source:** Custom n8n functionality

**Parameters:**

*   `keyField` (String) - The field in each Object containing the key name
    
*   `nameField` (String) - The field in each Object containing the value
    

**Examples:**

Copy

    // arr => [{'field':'age','value':2},{'field':'city','value':'Berlin'}]
    arr.smartJoin('field','value') //=> {"age": 2, "city": "Berlin"}

`_Array_`.`**sort()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraysort)

-----------------------------------------------------------------------------------------------------------------------

**Description:** Reorders the elements of the array. For sorting strings alphabetically, no parameter is required. For sorting numbers or Objects, see examples.

**Syntax:** `_Array_`.sort(compareFunction(a, b)?)

**Returns:** Array

**Source:** JavaScript function

**Parameters:**

*   `compareFunction` (function) - optional - A function to compare two array elements and return a number indicating which one comes first: Return < 0: `a` comes before `b` Return 0: `a` and `b` are equal (leave order unchanged) Return > 0: `b` comes before `a`
    

If no function is specified, converts all values to strings and compares their character codes.

*   `a` (any) - The first element to compare in the function
    
*   `b` (any) - The second element to compare in the function
    

**Examples:**

Copy

    // No need for a param when sorting strings
    // arr = ['d', 'a', 'c', 'b']
    arr.sort() //=> ['a', 'b', 'c', 'd']

Copy

    // To sort numbers, you must use a function
    // arr = [4, 2, 1, 3]
    arr.sort((a, b) => (a - b)) //=> [1, 2, 3, 4]
    
    // Or using traditional function notation:
    arr.sort(function(a, b){return a - b}) //=> [1, 2, 3, 4]

Copy

    // Sort in reverse alphabetical order
    // arr = ['d', 'a', 'c', 'b']
    arr.sort((a, b) => b.localeCompare(a)) //=> ['d', 'c', 'b', 'a']

Copy

    // Sort array of objects by a property
    // arr = [{name:'Zak'}, {name:'Abe'}, {name:'Bob'}]
    arr.sort((a, b) => a.name.localeCompare(b.name)) //=> [{name:'Abe'}, {name:'Bob'}, {name:'Zak'}]

`_Array_`.`**sum()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraysum)

---------------------------------------------------------------------------------------------------------------------

**Description:** Returns the total of all the numbers in the array. Throws an error if there are any non-numbers.

**Syntax:** `_Array_`.sum()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = [12, 1, 5]
    arr.sum() //=> 18

`_Array_`.`**toJsonString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraytojsonstring)

---------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the array to a JSON string. The same as JavaScript’s `JSON.stringify()`.

**Syntax:** `_Array_`.toJsonString()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    // obj = ['quick', 'brown', 'fox']
    obj.toJsonString() //=> '["quick","brown","fox"]'

`_Array_`.`**toSpliced()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraytospliced)

---------------------------------------------------------------------------------------------------------------------------------

**Description:** Adds and/or removes array elements at a given position.

See also `slice()` and `append()`.

**Syntax:** `_Array_`.toSpliced(start, deleteCount, elem1, ....., elemN)

**Returns:** Array

**Source:** JavaScript function

**Parameters:**

*   `start` (Number) - The index (position) to add or remove elements at. New elements are inserted before the element at this index. A negative index counts back from the end of the array.
    
*   `deleteCount` (Number) - optional - The number of elements to remove. If omitted, removes all elements from the `start` index onwards.
    
*   `elem1` (any) - optional - The first new element to be added
    
*   `elem2` (any) - optional - The second new element to be added
    
*   `elemN` (any) - optional - The Nth new element to be added
    

**Examples:**

Copy

    // Insert element at index 1
    // months = ['Jan', 'Mar']
    months.toSpliced(1, 0, "Feb") // ['Jan', 'Feb', 'Mar']

Copy

    // Delete 2 elements starting at index 1
    // arr = ["don't", "make", "me", "do", "this"]
    arr.toSpliced(1, 2) // ["don't", "do", "this"]

Copy

    // Replace 2 elements starting at index 1
    // arr = ["don't", "be", "evil"]
    arr.toSpliced(1, 2, 'eat', 'slugs') // ["don't", "eat", "slugs"]

`_Array_`.`**toString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arraytostring)

-------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the array to a string, with values separated by commas. To use a different separator, use `join()` instead.

**Syntax:** `_Array_`.toString()

**Returns:** String

**Source:** JavaScript function

**Examples:**

Copy

    // words = ['make', 'my', 'day']
    words.toString() //=> 'make,my,day'

`_Array_`.`**union()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayunion)

-------------------------------------------------------------------------------------------------------------------------

**Description:** Concatenates two arrays and then removes any duplicates

**Syntax:** `_Array_`.union(otherArray)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `otherArray` (Array) - The array to union with the base array
    

**Examples:**

Copy

    // arr = [1, 2]
    arr.union([2, 3]) //=> [1, 2, 3]
    

`_Array_`.`**unique()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#arrayunique)

---------------------------------------------------------------------------------------------------------------------------

**Description:** Removes any duplicate elements from the array

**Syntax:** `_Array_`.unique()

**Returns:** Array

**Source:** Custom n8n functionality

**Examples:**

Copy

    // arr = ['quick', 'brown', 'quick']
    arr.unique() //=> ['quick', 'brown']

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array#related-resources)

--------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousExpression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
[NextBinaryfile](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile)

Last updated 10 days ago

Was this helpful?