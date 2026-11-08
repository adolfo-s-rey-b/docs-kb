*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#mdn-search)
    

Working with objects
====================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
    

JavaScript is designed on an object-based paradigm. An object is a collection of [properties](https://developer.mozilla.org/en-US/docs/Glossary/Property/JavaScript)
, and a property is an association between a name (or _key_) and a value. A property's value can be a function, in which case the property is known as a [method](https://developer.mozilla.org/en-US/docs/Glossary/Method)
.

Objects in JavaScript, just as in many other programming languages, can be compared to objects in real life. In JavaScript, an object is a standalone entity, with properties and type. Compare it with a cup, for example. A cup is an object with properties. A cup has a color, a design, weight, a material it is made of, etc. In the same way, JavaScript objects can have properties, which define their characteristics.

In addition to objects that are predefined in the browser, you can define your own objects. This chapter describes how to use objects, properties, and methods, and how to create your own objects.

[Creating new objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#creating_new_objects)

--------------------------------------------------------------------------------------------------------------------------------

You can create an object using an [object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
. Alternatively, you can first create a constructor function and then instantiate an object by invoking that function with the `new` operator.

### [Using object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#using_object_initializers)

Object initializers are also called _object literals_. "Object initializer" is consistent with the terminology used by C++.

The syntax for an object using an object initializer is:

Each property name before the colon is either an identifier, a number literal, or a string literal, and each `valueN` is an expression whose value is assigned to the property name. The property name can also be an expression; computed keys need to be wrapped in square brackets. The [object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 reference contains a more detailed explanation of the syntax.

In this example, the newly created object is assigned to a variable `obj` — this is optional. If you do not need to refer to this object elsewhere, you do not need to assign it to a variable. (Note that you may need to wrap the object literal in parentheses if the object appears where a statement is expected, so as not to have the literal be confused with a block statement.)

Object initializers are expressions, and each object initializer results in a new object being created whenever the statement in which it appears is executed. Identical object initializers create distinct objects that do not compare to each other as equal.

The following statement creates an object and assigns it to the variable `x` if and only if the expression `cond` is true:

The following example creates `myHonda` with three properties. Note that the `engine` property is also an object with its own properties.

Objects created with initializers are called _plain objects_, because they are instances of [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
, but not any other object type. Some object types have special initializer syntaxes — for example, [array initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#array_literals)
 and [regex literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#creating_a_regular_expression)
.

### [Using a constructor function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#using_a_constructor_function)

Alternatively, you can create an object with these two steps:

1.  Define the object type by writing a constructor function. There is a strong convention, with good reason, to use a capital initial letter.
2.  Create an instance of the object with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
    .

To define an object type, create a function for the object type that specifies its name, properties, and methods. For example, suppose you want to create an object type for cars. You want this type of object to be called `Car`, and you want it to have properties for make, model, and year. To do this, you would write the following function:

Notice the use of `this` to assign values to the object's properties based on the values passed to the function.

Now you can create an object called `myCar` as follows:

This statement creates `myCar` and assigns it the specified values for its properties. Then the value of `myCar.make` is the string `"Eagle"`, `myCar.model` is the string `"Talon TSi"`, `myCar.year` is the integer `1993`, and so on. The order of arguments and parameters should be the same.

You can create any number of `Car` objects by calls to `new`. For example,

An object can have a property that is itself another object. For example, suppose you define an object called `Person` as follows:

and then instantiate two new `Person` objects as follows:

Then, you can rewrite the definition of `Car` to include an `owner` property that takes a `Person` object, as follows:

To instantiate the new objects, you then use the following:

Notice that instead of passing a literal string or integer value when creating the new objects, the above statements pass the objects `rand` and `ken` as the arguments for the owners. Then if you want to find out the name of the owner of `car2`, you can access the following property:

You can always add a property to a previously defined object. For example, the statement

adds a property `color` to `car1`, and assigns it a value of `"black"`. However, this does not affect any other objects. To add the new property to all objects of the same type, you have to add the property to the definition of the `Car` object type.

You can also use the [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 syntax instead of the `function` syntax to define a constructor function. For more information, see the [class guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
.

### [Using the Object.create() method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#using_the_object.create_method)

Objects can also be created using the [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
 method. This method can be very useful, because it allows you to choose the [prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 object for the object you want to create, without having to define a constructor function.

[Objects and properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#objects_and_properties)

------------------------------------------------------------------------------------------------------------------------------------

A JavaScript object has properties associated with it. Object properties are basically the same as variables, except that they are associated with objects, not [scopes](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
. The properties of an object define the characteristics of the object.

For example, this example creates an object named `myCar`, with properties named `make`, `model`, and `year`, with their values set to `"Ford"`, `"Mustang"`, and `1969`:

Like JavaScript variables, property names are case sensitive. Property names can only be strings or Symbols — all keys are [converted to strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
 unless they are Symbols. [Array indices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_indices)
 are, in fact, properties with string keys that contain integers.

### [Accessing properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#accessing_properties)

You can access a property of an object by its property name. [Property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
 come in two syntaxes: _dot notation_ and _bracket notation_. For example, you could access the properties of the `myCar` object as follows:

An object property name can be any JavaScript string or [symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
, including an empty string. However, you cannot use dot notation to access a property whose name is not a valid JavaScript identifier. For example, a property name that has a space or a hyphen, that starts with a number, or that is held inside a variable can only be accessed using the bracket notation. This notation is also very useful when property names are to be dynamically determined, i.e., not determinable until runtime. Examples are as follows:

In the above code, the key `anotherObj` is an object, which is neither a string nor a symbol. When it is added to the `myObj`, JavaScript calls the [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method of `anotherObj`, and use the resulting string as the new key.

You can also access properties with a string value stored in a variable. The variable must be passed in bracket notation. In the example above, the variable `str` held `"myString"` and it is `"myString"` that is the property name. Therefore, `myObj.str` will return as undefined.

This allows accessing any property as determined at runtime:

However, beware of using square brackets to access properties whose names are given by external input. This may make your code susceptible to [object injection attacks](https://github.com/eslint-community/eslint-plugin-security/blob/main/docs/the-dangers-of-square-bracket-notation.md "External link (opens in new tab)")
.

Nonexistent properties of an object have the value [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 (and not [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
).

### [Enumerating properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#enumerating_properties)

There are three native ways to list/traverse object properties:

*   [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
     loops. This method traverses all of the enumerable string properties of an object as well as its prototype chain.
*   [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
    . This method returns an array with only the enumerable own string property names ("keys") in the object `myObj`, but not those in the prototype chain.
*   [`Object.getOwnPropertyNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)
    . This method returns an array containing all the own string property names in the object `myObj`, regardless of if they are enumerable or not.

You can use the bracket notation with [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 to iterate over all the enumerable properties of an object. To illustrate how this works, the following function displays the properties of the object when you pass the object and the object's name as arguments to the function:

The term "own property" refers to the properties of the object, but excluding those of the prototype chain. So, the function call `showProps(myCar, 'myCar')` would print the following:

myCar.make = Ford
myCar.model = Mustang
myCar.year = 1969

The above is equivalent to:

There is no native way to list all inherited properties, including non-enumerable ones. However, this can be achieved with the following function:

For more information, see [Enumerability and ownership of properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
.

### [Deleting properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#deleting_properties)

You can remove a non-inherited property using the [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
 operator. The following code shows how to remove a property.

[Inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#inheritance)

--------------------------------------------------------------------------------------------------------------

All objects in JavaScript inherit from at least one other object. The object being inherited from is known as the prototype, and the inherited properties can be found in the `prototype` object of the constructor. See [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 for more information.

### [Defining properties for all objects of one type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#defining_properties_for_all_objects_of_one_type)

You can add a property to all objects created through a certain [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#using_a_constructor_function)
 using the [`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
 property. This defines a property that is shared by all objects of the specified type, rather than by just one instance of the object. The following code adds a `color` property to all objects of type `Car`, and then reads the property's value from an instance `car1`.

[Defining methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#defining_methods)

------------------------------------------------------------------------------------------------------------------------

A _method_ is a function associated with an object, or, put differently, a method is a property of an object that is a function. Methods are defined the way normal functions are defined, except that they have to be assigned as the property of an object. See also [method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
 for more details. An example is:

where `objectName` is an existing object, `methodName` is the name you are assigning to the method, and `functionName` is the name of the function.

You can then call the method in the context of the object as follows:

Methods are typically defined on the `prototype` object of the constructor, so that all objects of the same type share the same method. For example, you can define a function that formats and displays the properties of the previously-defined `Car` objects.

Notice the use of `this` to refer to the object to which the method belongs. Then you can call the `displayCar` method for each of the objects as follows:

### [Using this for object references](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#using_this_for_object_references)

JavaScript has a special keyword, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
, that you can use within a method to refer to the current object. For example, suppose you have 2 objects, `manager` and `intern`. Each object has its own `name`, `age` and `job`. In the function `sayHi()`, notice the use of `this.name`. When added to the 2 objects, the same function will print the message with the name of the respective object it's attached to.

`this` is a "hidden parameter" of a function call that's passed in by specifying the object before the function that was called. For example, in `manager.sayHi()`, `this` is the `manager` object, because `manager` comes before the function `sayHi()`. If you access the same function from another object, `this` will change as well. If you use other methods to call the function, like [`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
 or [`Reflect.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/apply)
, you can explicitly pass the value of `this` as an argument.

[Defining getters and setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#defining_getters_and_setters)

------------------------------------------------------------------------------------------------------------------------------------------------

A [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 is a function associated with a property that gets the value of a specific property. A [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 is a function associated with a property that sets the value of a specific property. Together, they can indirectly represent the value of a property.

Getters and setters can be either

*   defined within [object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#using_object_initializers)
    , or
*   added later to any existing object.

Within [object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#using_object_initializers)
, getters and setters are defined like regular [methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
, but prefixed with the keywords `get` or `set`. The getter method must not expect a parameter, while the setter method expects exactly one parameter (the new value to set). For instance:

The `myObj` object's properties are:

*   `myObj.a` — a number
*   `myObj.b` — a getter that returns `myObj.a` plus 1
*   `myObj.c` — a setter that sets the value of `myObj.a` to half of the value `myObj.c` is being set to

Getters and setters can also be added to an object at any time after creation using the [`Object.defineProperties()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperties)
 method. This method's first parameter is the object on which you want to define the getter or setter. The second parameter is an object whose property names are the getter or setter names, and whose property values are objects for defining the getter or setter functions. Here's an example that defines the same getter and setter used in the previous example:

Which of the two forms to choose depends on your programming style and task at hand. If you can change the definition of the original object, you will probably define getters and setters through the original initializer. This form is more compact and natural. However, if you need to add getters and setters later — maybe because you did not write the particular object — then the second form is the only possible form. The second form better represents the dynamic nature of JavaScript, but it can make the code hard to read and understand.

[Comparing objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#comparing_objects)

--------------------------------------------------------------------------------------------------------------------------

In JavaScript, objects are a reference type. Two distinct objects are never equal, even if they have the same properties. Only comparing the same object reference with itself yields true.

For more information about comparison operators, see [equality operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#equality_operators)
.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#see_also)

--------------------------------------------------------------------------------------------------------

*   [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
    
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/working_with_objects/index.md?plain=1 "Folder: en-us/web/javascript/guide/working_with_objects (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FWorking_with_objects&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fworking_with_objects%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FWorking_with_objects%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fworking_with_objects%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1474534461893381d54c502e655f334b5568e597%0A*+Document+last+modified%3A+2026-08-21T19%3A37%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")