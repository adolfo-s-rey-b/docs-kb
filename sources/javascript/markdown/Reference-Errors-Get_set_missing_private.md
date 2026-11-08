*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#mdn-search)
    

TypeError: can't access/set private field or method: object is not the right class
==================================================================================

The JavaScript exception "can't access private field or method: object is not the right class" or "can't set private field: object is not the right class" occurs when a private field or method is get or set on an object that does not have this [private element](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 defined.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#message)

--------------------------------------------------------------------------------------------------------------------

TypeError: Cannot read private member #x from an object whose class did not declare it (V8-based)
TypeError: Cannot write private member #x to an object whose class did not declare it (V8-based)
TypeError: can't access private field or method: object is not the right class (Firefox)
TypeError: can't set private field: object is not the right class (Firefox)
TypeError: Cannot access invalid private field (evaluating 'this.#x') (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#error_type)

--------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------------------

You are trying to get or set a private field or method on an object, but that object does not contain this private element. Private instance properties can only be accessed on instances of the class (including its subclasses) that declares them; private static properties can only be accessed on the class itself that declares them, and not on subclasses.

This error occurs when the private name exists in the class scope but the object it's accessed on is invalid. If the private name does not exist, you will get a [syntax error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method)
 instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#examples)

----------------------------------------------------------------------------------------------------------------------

### [Mismatched static/instance fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#mismatched_staticinstance_fields)

You may have declared the field as a static field, but are trying to access it on an instance, or vice versa.

To fix this, either change the field to be an instance field, or access the field on the class itself, or declare another field on the instance. Note that the private namespace is shared between static and instance properties, so you cannot have a static and instance private element with the same name.

### [Wrong object used](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#wrong_object_used)

Perhaps you have a method that access `this.#x`, but it is called with another `this` value.

This is because [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
 calls the replacer function with the object containing `value` as `this`, so the private field is not accessible. To fix this, you can bind the method to the object, or use an arrow function, to ensure that `replacer.func` is called with the correct `this` value.

Most of the time, if you accidentally unbound a method, the method would be called with `undefined` as `this`, which would result in a different error (TypeError: can't convert undefined to object). This error only occurs when the method is called with a different object as `this`, either by using [`call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
 or [`apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
, or by passing the method as a callback to a function that calls it with a different `this` value.

If you don't know for sure that the object will contain the private element, as in the following code:

You can use the [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 operator to perform a _branded check_ first.

### [Accessing static elements on subclasses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#accessing_static_elements_on_subclasses)

If you have a [private static property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#private_static_fields)
, you can only access it on the class that declares it, not on subclasses.

To fix this, never access private static properties through `this`. Instead, always explicitly specify the class's name.

### [Accessing same-name private elements on another class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#accessing_same-name_private_elements_on_another_class)

Unlike normal string or symbol properties, private names are not shared between classes. If you have a private element with the same name in two classes, they are still not the same element, and you cannot access one class's private element from another class.

### [Adding private elements to unrelated objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#adding_private_elements_to_unrelated_objects)

You cannot dynamically _add_ private elements to unrelated objects.

If you really want to do this, consider the [return override](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#returning_overriding_object)
 trick. However, in general, you would probably want to use a [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
 instead.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jan 25, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/get_set_missing_private/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/get_set_missing_private (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FGet_set_missing_private&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fget_set_missing_private%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FGet_set_missing_private%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fget_set_missing_private%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06e6e54baef7032c4e81ca93291fde0a0585de8b%0A*+Document+last+modified%3A+2026-01-25T19%3A35%3A57.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")