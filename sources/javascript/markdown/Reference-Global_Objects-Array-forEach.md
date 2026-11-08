*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#mdn-search)
    

Array.prototype.forEach()
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`forEach()`** method of [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instances executes a provided function once for each array element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#try_it)

----------------------------------------------------------------------------------------------------------------

    const array = ["a", "b", "c"];
    
    array.forEach((element) => console.log(element));
    
    // Expected output: "a"
    // Expected output: "b"
    // Expected output: "c"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#syntax)

----------------------------------------------------------------------------------------------------------------

js

    forEach(callbackFn)
    forEach(callbackFn, thisArg)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#parameters)

[`callbackFn`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#callbackfn)

A function to execute for each element in the array. Its return value is discarded. The function is called with the following arguments:

[`element`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#element)

The current element being processed in the array.

[`index`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#index)

The index of the current element being processed in the array.

[`array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#array)

The array `forEach()` was called upon.

[`thisArg` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#thisarg)

A value to use as `this` when executing `callbackFn`. See [iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#return_value)

None ([`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
).

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#description)

--------------------------------------------------------------------------------------------------------------------------

The `forEach()` method is an [iterative method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
. It calls a provided `callbackFn` function once for each element in an array in ascending-index order. Unlike [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
, `forEach()` always returns [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 and is not chainable. The typical use case is to execute side effects at the end of a chain. Read the [iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
 section for more information about how these methods work in general.

`callbackFn` is invoked only for array indexes which have assigned values. It is not invoked for empty slots in [sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
.

The `forEach()` method is [generic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)
. It only expects the `this` value to have a `length` property and integer-keyed properties.

There is no way to stop or break a `forEach()` loop other than by throwing an exception. If you need such behavior, the `forEach()` method is the wrong tool.

Early termination may be accomplished with looping statements like [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
, [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
, and [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
. Array methods like [`every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
, [`some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
, [`find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
, and [`findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)
 also stops iteration immediately when further iteration is not necessary.

`forEach()` expects a synchronous function — it does not wait for promises. Make sure you are aware of the implications while using promises (or async functions) as `forEach` callbacks.

js

    const ratings = [5, 4, 5];
    let sum = 0;
    
    const sumFunction = async (a, b) => a + b;
    
    ratings.forEach(async (rating) => {
      sum = await sumFunction(sum, rating);
    });
    
    console.log(sum);
    // Naively expected output: 14
    // Actual output: 0
    

To run a series of asynchronous operations sequentially or concurrently, see [promise composition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#composition)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#examples)

--------------------------------------------------------------------------------------------------------------------

### [Converting a for loop to forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#converting_a_for_loop_to_foreach)

js

    const items = ["item1", "item2", "item3"];
    const copyItems = [];
    
    // before
    for (let i = 0; i < items.length; i++) {
      copyItems.push(items[i]);
    }
    
    // after
    items.forEach((item) => {
      copyItems.push(item);
    });
    

### [Printing the contents of an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#printing_the_contents_of_an_array)

**Note:** In order to display the content of an array in the console, you can use [`console.table()`](https://developer.mozilla.org/en-US/docs/Web/API/console/table_static "console.table()")
, which prints a formatted version of the array.

The following example illustrates an alternative approach, using `forEach()`.

The following code logs a line for each element in an array:

js

    const logArrayElements = (element, index /*, array */) => {
      console.log(`a[${index}] = ${element}`);
    };
    
    // Notice that index 2 is skipped, since there is no item at
    // that position in the array.
    [2, 5, , 9].forEach(logArrayElements);
    // Logs:
    // a[0] = 2
    // a[1] = 5
    // a[3] = 9
    

### [Using thisArg](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#using_thisarg)

The following (contrived) example updates an object's properties from each entry in the array:

js

    class Counter {
      constructor() {
        this.sum = 0;
        this.count = 0;
      }
      add(array) {
        // Only function expressions have their own this bindings.
        array.forEach(function countEntry(entry) {
          this.sum += entry;
          ++this.count;
        }, this);
      }
    }
    
    const obj = new Counter();
    obj.add([2, 5, 9]);
    console.log(obj.count); // 3
    console.log(obj.sum); // 16
    

Since the `thisArg` parameter (`this`) is provided to `forEach()`, it is passed to `callback` each time it's invoked. The callback uses it as its `this` value.

**Note:** If passing the callback function used an [arrow function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
, the `thisArg` parameter could be omitted, since all arrow functions lexically bind the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 value.

### [An object copy function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#an_object_copy_function)

The following code creates a copy of a given object.

There are different ways to create a copy of an object. The following is just one way and is presented to explain how `Array.prototype.forEach()` works by using `Object.*` utility functions.

js

    const copy = (obj) => {
      const copy = Object.create(Object.getPrototypeOf(obj));
      const propNames = Object.getOwnPropertyNames(obj);
      propNames.forEach((name) => {
        const desc = Object.getOwnPropertyDescriptor(obj, name);
        Object.defineProperty(copy, name, desc);
      });
      return copy;
    };
    
    const obj1 = { a: 1, b: 2 };
    const obj2 = copy(obj1); // obj2 looks like obj1 now
    

### [Flatten an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#flatten_an_array)

The following example is only here for learning purpose. If you want to flatten an array using built-in methods, you can use [`Array.prototype.flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)
.

js

    const flatten = (arr) => {
      const result = [];
      arr.forEach((item) => {
        if (Array.isArray(item)) {
          result.push(...flatten(item));
        } else {
          result.push(item);
        }
      });
      return result;
    };
    
    // Usage
    const nested = [1, 2, 3, [4, 5, [6, 7], 8, 9]];
    console.log(flatten(nested)); // [1, 2, 3, 4, 5, 6, 7, 8, 9]
    

### [Using the third argument of callbackFn](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#using_the_third_argument_of_callbackfn)

The `array` argument is useful if you want to access another element in the array, especially when you don't have an existing variable that refers to the array. The following example first uses `filter()` to extract the positive values and then uses `forEach()` to log its neighbors.

js

    const numbers = [3, -1, 1, 4, 1, 5];
    numbers
      .filter((num) => num > 0)
      .forEach((num, idx, arr) => {
        // Without the arr argument, there's no way to easily access the
        // intermediate array without saving it to a variable.
        console.log(arr[idx - 1], num, arr[idx + 1]);
      });
    // undefined 3 1
    // 3 1 4
    // 1 4 1
    // 4 1 5
    // 1 5 undefined
    

### [Using forEach() on sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#using_foreach_on_sparse_arrays)

js

    const arraySparse = [1, 3, /* empty */, 7];
    let numCallbackRuns = 0;
    
    arraySparse.forEach((element) => {
      console.log({ element });
      numCallbackRuns++;
    });
    
    console.log({ numCallbackRuns });
    
    // { element: 1 }
    // { element: 3 }
    // { element: 7 }
    // { numCallbackRuns: 3 }
    

The callback function is not invoked for the missing value at index 2.

### [Calling forEach() on non-array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#calling_foreach_on_non-array_objects)

The `forEach()` method reads the `length` property of `this` and then accesses each property whose key is a nonnegative integer less than `length`.

js

    const arrayLike = {
      length: 3,
      0: 2,
      1: 3,
      2: 4,
      3: 5, // ignored by forEach() since length is 3
    };
    Array.prototype.forEach.call(arrayLike, (x) => console.log(x));
    // 2
    // 3
    // 4
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-array.prototype.foreach](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.foreach) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Array.prototype.forEach` in `core-js`](https://core-js.io/docs/features/ecmascript/array "External link (opens in new tab)")
    
*   [es-shims polyfill of `Array.prototype.forEach`](https://www.npmjs.com/package/array.prototype.foreach "External link (opens in new tab)")
    
*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
*   [`Array.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
    
*   [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
    
*   [`Array.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
    
*   [`Array.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
    
*   [`Array.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
    
*   [`TypedArray.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/forEach)
    
*   [`Map.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach)
    
*   [`Set.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/forEach)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/foreach/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array/foreach (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FforEach&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fforeach%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FforEach%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fforeach%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")