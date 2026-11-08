*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#mdn-search)
    

Closures
========

A **closure** is the combination of a function bundled together (enclosed) with references to its surrounding state (the **lexical environment**). In other words, a closure gives a function access to its outer scope. In JavaScript, closures are created every time a function is created, at function creation time.

[Lexical scoping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#lexical_scoping)

----------------------------------------------------------------------------------------------------------

Consider the following example code:

`init()` creates a local variable called `name` and a function called `displayName()`. The `displayName()` function is an inner function that is defined inside `init()` and is available only within the body of the `init()` function. Note that the `displayName()` function has no local variables of its own. However, since inner functions have access to the variables of outer scopes, `displayName()` can access the variable `name` declared in the parent function, `init()`.

If you run this code in your console, you can see that the `console.log()` statement within the `displayName()` function successfully displays the value of the `name` variable, which is declared in its parent function. This is an example of _lexical scoping_, which describes how a parser resolves variable names when functions are nested. The word _lexical_ refers to the fact that lexical scoping uses the location where a variable is declared within the source code to determine where that variable is available. Nested functions have access to variables declared in their outer scope.

### [Scoping with let and const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#scoping_with_let_and_const)

Traditionally (before ES6), JavaScript variables only had two kinds of scopes: _function scope_ and _global scope_. Variables declared with `var` are either function-scoped or global-scoped, depending on whether they are declared within a function or outside a function. This can be tricky, because blocks with curly braces do not create scopes:

For people from other languages (e.g., C, Java) where blocks create scopes, the above code should throw an error on the `console.log` line, because we are outside the scope of `x` in either block. However, because blocks don't create scopes for `var`, the `var` statements here actually create a global variable. There is also [a practical example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#creating_closures_in_loops_a_common_mistake)
 introduced below that illustrates how this can cause actual bugs when combined with closures.

In ES6, JavaScript introduced the `let` and `const` declarations, which, among other things like [temporal dead zones](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
, allow you to create block-scoped variables.

In essence, blocks are finally treated as scopes in ES6, but only if you declare variables with `let` or `const`. In addition, ES6 introduced [modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
, which introduced another kind of scope. Closures are able to capture variables in all these scopes, which we will introduce later.

[Closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#closure)

------------------------------------------------------------------------------------------

Consider the following code example:

Running this code has exactly the same effect as the previous example of the `init()` function above. What's different (and interesting) is that the `displayName()` inner function is returned from the outer function _before being executed_.

At first glance, it might seem unintuitive that this code still works. In some programming languages, the local variables within a function exist for just the duration of that function's execution. Once `makeFunc()` finishes executing, you might expect that the `name` variable would no longer be accessible. However, because the code still works, this is obviously not the case in JavaScript.

The reason is that functions in JavaScript form closures. A _closure_ is the combination of a function and the lexical environment within which that function was declared. This environment consists of any variables that were in-scope at the time the closure was created. In this case, `myFunc` is a reference to the instance of the function `displayName` that is created when `makeFunc` is run. The instance of `displayName` maintains a reference to its lexical environment, within which the variable `name` exists. For this reason, when `myFunc` is invoked, the variable `name` remains available for use, and "Mozilla" is passed to `console.log`.

Here's a slightly more interesting example—a `makeAdder` function:

In this example, we have defined a function `makeAdder(x)`, that takes a single argument `x`, and returns a new function. The function it returns takes a single argument `y`, and returns the sum of `x` and `y`.

In essence, `makeAdder` is a function factory. It creates functions that can add a specific value to their argument. In the above example, the function factory creates two new functions—one that adds five to its argument, and one that adds 10.

`add5` and `add10` both form closures. They share the same function body definition, but store different lexical environments. In `add5`'s lexical environment, `x` is 5, while in the lexical environment for `add10`, `x` is 10.

[Practical closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#practical_closures)

----------------------------------------------------------------------------------------------------------------

Closures are useful because they let you associate data (the lexical environment) with a function that operates on that data. This has obvious parallels to object-oriented programming, where objects allow you to associate data (the object's properties) with one or more methods.

Consequently, you can use a closure anywhere that you might normally use an object with only a single method.

Situations where you might want to do this are particularly common on the web. Much of the code written in front-end JavaScript is event-based. You define some behavior, and then attach it to an event that is triggered by the user (such as a click or a keypress). The code is attached as a callback (a single function that is executed in response to the event).

For instance, suppose we want to add buttons to a page to adjust the text size. One way of doing this is to specify the font-size of the `body` element (in pixels), and then set the size of the other elements on the page (such as headers) using the relative `em` unit:

Such interactive text size buttons can change the `font-size` property of the `body` element, and the adjustments are picked up by other elements on the page thanks to the relative units.

Here's the JavaScript:

`size12`, `size14`, and `size16` are now functions that resize the body text to 12, 14, and 16 pixels, respectively. You can attach them to buttons as demonstrated in the following code example.

[Emulating private methods with closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#emulating_private_methods_with_closures)

----------------------------------------------------------------------------------------------------------------------------------------------------------

Languages such as Java allow you to declare methods as private, meaning that they can be called only by other methods in the same class.

JavaScript, prior to [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
, didn't have a native way of declaring [private methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#private_methods)
, but it was possible to emulate private methods using closures. Private methods aren't just useful for restricting access to code. They also provide a powerful way of managing your global namespace.

The following code illustrates how to use closures to define public functions that can access private functions and variables. Note that these closures follow the [Module Design Pattern](https://www.google.com/search?q=javascript+module+pattern "External link (opens in new tab)")
.

In previous examples, each closure had its own lexical environment. Here though, there is a single lexical environment that is shared by the three functions: `counter.increment`, `counter.decrement`, and `counter.value`.

The shared lexical environment is created in the body of an anonymous function, _which is executed as soon as it has been defined_ (also known as an [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
). The lexical environment contains two private items: a variable called `privateCounter`, and a function called `changeBy`. You can't access either of these private members from outside the anonymous function. Instead, you indirectly access them using the three public functions that are returned from the anonymous wrapper.

Those three public functions form closures that share the same lexical environment. Thanks to JavaScript's lexical scoping, they each have access to the `privateCounter` variable and the `changeBy` function.

Notice how the two counters maintain their independence from one another. Each closure references a different version of the `privateCounter` variable through its own closure. Each time one of the counters is called, its lexical environment changes by changing the value of this variable. Changes to the variable value in one closure don't affect the value in the other closure.

**Note:** Using closures in this way provides benefits that are normally associated with object-oriented programming. In particular, _data hiding_ and _encapsulation_.

[Closure scope chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#closure_scope_chain)

------------------------------------------------------------------------------------------------------------------

A nested function's access to the outer function's scope includes the enclosing scope of the outer function—effectively creating a chain of function scopes. To demonstrate, consider the following example code.

You can also write without anonymous functions:

In the example above, there's a series of nested functions, all of which have access to the outer functions' scope. In this context, we can say that closures have access to _all_ outer scopes.

Closures can capture variables in block scopes and module scopes as well. For example, the following creates a closure over the block-scoped variable `y`:

Closures over modules can be more interesting.

Here, the module exports a pair of getter-setter functions, which close over the module-scoped variable `x`. Even when `x` is not directly accessible from other modules, it can be read and written with the functions.

Closures can close over imported values as well, which are regarded as _live [bindings](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
_, because when the original value changes, the imported one changes accordingly.

[Creating closures in loops: A common mistake](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#creating_closures_in_loops_a_common_mistake)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Prior to the introduction of the [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 keyword, a common problem with closures occurred when you created them inside a loop. To demonstrate, consider the following example code.

html

    <p id="help">Helpful notes will appear here</p>
    <p>Email: <input type="text" id="email" name="email" /></p>
    <p>Name: <input type="text" id="name" name="name" /></p>
    <p>Age: <input type="text" id="age" name="age" /></p>
    

js

    function showHelp(help) {
      document.getElementById("help").textContent = help;
    }
    
    function setupHelp() {
      var helpText = [\
        { id: "email", help: "Your email address" },\
        { id: "name", help: "Your full name" },\
        { id: "age", help: "Your age (you must be over 16)" },\
      ];
    
      for (var i = 0; i < helpText.length; i++) {
        // Culprit is the use of `var` on this line
        var item = helpText[i];
        document.getElementById(item.id).onfocus = function () {
          showHelp(item.help);
        };
      }
    }
    
    setupHelp();
    

The `helpText` array defines three helpful hints, each associated with the ID of an input field in the document. The loop cycles through these definitions, hooking up an `onfocus` event to each one that shows the associated help method.

If you try this code out, you'll see that it doesn't work as expected. No matter what field you focus on, the message about your age will be displayed.

The reason for this is that the functions assigned to `onfocus` form closures; they consist of the function definition and the captured environment from the `setupHelp` function's scope. Three closures have been created by the loop, but each one shares the same single lexical environment, which has a variable with changing values (`item`). This is because the variable `item` is declared with `var` and thus has function scope due to hoisting. The value of `item.help` is determined when the `onfocus` callbacks are executed. Because the loop has already run its course by that time, the `item` variable object (shared by all three closures) has been left pointing to the last entry in the `helpText` list.

One solution in this case is to use more closures: in particular, to use a function factory as described earlier:

    <p id="help">Helpful notes will appear here</p>
    <p>Email: <input type="text" id="email" name="email" /></p>
    <p>Name: <input type="text" id="name" name="name" /></p>
    <p>Age: <input type="text" id="age" name="age" /></p>
    

js

    function showHelp(help) {
      document.getElementById("help").textContent = help;
    }
    
    function makeHelpCallback(help) {
      return function () {
        showHelp(help);
      };
    }
    
    function setupHelp() {
      var helpText = [\
        { id: "email", help: "Your email address" },\
        { id: "name", help: "Your full name" },\
        { id: "age", help: "Your age (you must be over 16)" },\
      ];
    
      for (var i = 0; i < helpText.length; i++) {
        var item = helpText[i];
        document.getElementById(item.id).onfocus = makeHelpCallback(item.help);
      }
    }
    
    setupHelp();
    

This works as expected. Rather than the callbacks all sharing a single lexical environment, the `makeHelpCallback` function creates _a new lexical environment_ for each callback, in which `help` refers to the corresponding string from the `helpText` array.

One other way to write the above using anonymous closures is:

If you don't want to use more closures, you can use the [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 or [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
 keyword:

This example uses `const` instead of `var`, so every closure binds the block-scoped variable, meaning that no additional closures are required.

If you are writing modern JavaScript anyway, you can consider more alternatives to the plain `for` loop, such as using [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loop and declaring `item` as `let` or `const`, or using the [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
 method, which both avoid the closure problem.

[Performance considerations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#performance_considerations)

--------------------------------------------------------------------------------------------------------------------------------

As mentioned previously, each function instance manages its own scope and closure. Therefore, it is unwise to unnecessarily create functions within other functions if closures are not needed for a particular task, as it will negatively affect script performance both in terms of processing speed and memory consumption.

For instance, when creating a new object/class, methods should normally be associated to the object's prototype rather than defined into the object constructor. The reason is that whenever the constructor is called, the methods would get reassigned (that is, for every object creation).

Consider the following case:

Because the previous code does not take advantage of the benefits of using closures in this particular instance, we could instead rewrite it to avoid using closures as follows:

However, redefining the prototype is not recommended. The following example instead appends to the existing prototype:

In the two previous examples, the inherited prototype can be shared by all objects and the method definitions need not occur at every object creation. See [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 for more.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 4, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/closures/index.md?plain=1 "Folder: en-us/web/javascript/guide/closures (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FClosures&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fclosures%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FClosures%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fclosures%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F984adfc302136da0ee90eab7caaa85d577b735e6%0A*+Document+last+modified%3A+2025-11-04T07%3A08%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")