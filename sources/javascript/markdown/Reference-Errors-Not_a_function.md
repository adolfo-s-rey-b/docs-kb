*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#mdn-search)
    

TypeError: "x" is not a function
================================

The JavaScript exception "is not a function" occurs when there was an attempt to call a value from a function, but the value is not actually a function.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#message)

-----------------------------------------------------------------------------------------------------------

TypeError: "x" is not a function. (V8-based & Firefox & Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#error_type)

-----------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#what_went_wrong)

----------------------------------------------------------------------------------------------------------------------------

It attempted to call a value from a function, but the value is not actually a function. Some code expects you to provide a function, but that didn't happen.

Maybe there is a typo in the function name? Maybe the object you are calling the method on does not have this function? For example, JavaScript `Objects` have no `map` function, but the JavaScript `Array` object does.

There are many built-in functions in need of a (callback) function. You will have to provide a function in order to have these methods working properly:

*   When working with [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
     or [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
     objects:
    
    *   [`Array.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
        , [`Array.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
        , [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
        , [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
        , [`Array.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
        , [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
        , [`Array.prototype.reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight)
        , [`Array.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
        
*   When working with [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
     and [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
     objects:
    
    *   [`Map.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach)
         and [`Set.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/forEach)
        

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#examples)

-------------------------------------------------------------------------------------------------------------

### [A typo in the function name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#a_typo_in_the_function_name)

In this case, which happens way too often, there is a typo in the method name:

The correct function name is `getElementById`:

### [Function called on the wrong object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#function_called_on_the_wrong_object)

For certain methods, you have to provide a (callback) function and it will work on specific objects only. In this example, [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
 is used, which will work with [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 objects only.

Use an array instead:

### [Function shares a name with a pre-existing property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#function_shares_a_name_with_a_pre-existing_property)

Sometimes when making a class, you may have a property and a function with the same name. Upon calling the function, the compiler thinks that the function ceases to exist.

Use a different property name instead:

### [Using parentheses for multiplication](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#using_parentheses_for_multiplication)

In math, you can write 2 × (3 + 5) as 2\*(3 + 5) or just 2(3 + 5).

Using the latter will throw an error:

You can correct the code by adding a `*` operator:

### [Import the exported module correctly](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#import_the_exported_module_correctly)

Ensure you are importing the module correctly.

An example helpers library (`helpers.js`)

The correct import usage (`App.js`):

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/not_a_function/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/not_a_function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FNot_a_function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fnot_a_function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FNot_a_function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fnot_a_function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")