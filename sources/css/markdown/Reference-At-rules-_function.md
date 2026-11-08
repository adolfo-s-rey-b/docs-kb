*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#mdn-search)
    

`@function` CSS at-rule
=======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/300)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#browser_compatibility)
 carefully before using this in production.

The **`@function`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 enables defining [CSS custom functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
. Once defined, a custom function can be called using the [`<dashed-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function)
 syntax (for example, `--my-function(30px, 3)`) within any property value.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#syntax)

-----------------------------------------------------------------------------------------------

css

    @function --function-name(<function-parameter>#?) [returns <css-type>]? {
      <declaration-rule-list>
    }
    
    <function-parameter> = --param-name <css-type>? [ : <default-value> ]?
    

The different parts of the `@function` syntax are as follows:

[`--function-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#--function-name)

The identifying name of the function, a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 that starts with `--` and is followed by a valid, user-defined identifier. It is case-sensitive.

[`<function-parameter>#?` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#function-parameter)

Zero or more function parameter definitions. Multiple parameter definitions are separated by commas. Each parameter consists of:

[`--param-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#--param-name)

A [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 name to identify the parameter, a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 that starts with `--` and is followed by a valid, user-defined identifier. It is case-sensitive. Function parameters can be considered custom properties that are locally scoped to the function body.

[`<css-type>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#css-type)

A CSS data type or a [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
 function that defines the accepted data type(s) for the parameter. If this is not specified, any data type will be valid for the parameter (the same as specifying `type(*)`).

[`<default-value>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#default-value)

A CSS value specifying the default value to assign to the parameter if it is not specified when the function is called. This value must be valid according to the `<css-type>` if specified. The default value is separated from the other parts of the parameter definition with a colon (`:`).

[`[returns <css-type>]?` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#returns_css-type)

A CSS data type or a [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
 function, preceded by the keyword `returns`, which defines the accepted return type(s) for the parameter. If this is not specified, any data type will be valid for the parameter (the same as specifying `returns type(*)`), although bear in mind that the function will be invalid if the return type does not match the type produced by the `result` descriptor.

[`<declaration-rule-list>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#declaration-rule-list)

One or more CSS declarations or at-rules that define the body of the function, which contains its logic. Included declarations can include:

*   CSS custom properties, which are locally scoped to the function body.
*   The `result` descriptor, either directly inside the `@function` at-rule, or inside a nested at-rule.

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#descriptors)

[`result`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#result_2)

A valid property value that defines the result returned by the CSS custom function. The expression contained in the value is evaluated, and the result is returned.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#description)

---------------------------------------------------------------------------------------------------------

CSS custom functions allow you to define reusable sections of logic that will return different values depending on the parameters they accept as inputs and the logic defined inside the function body.

A typical CSS function looks like this:

css

    @function --transparent(--color, --alpha) {
      result: oklch(from var(--color) l c h / var(--alpha));
    }
    

The function has a name of `--transparent` and takes two custom properties as parameters, `--color` and `--alpha`, which can be used locally inside the function body. The body contains a single line, which is a `result` descriptor that defines the value returned by the function. The value of the `result` descriptor uses [CSS relative color syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
 to convert the input `--color` value into an [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
 color with the alpha channel value specified in the input `--alpha` value.

You can then call this function anywhere you want to produce a semi-transparent version of an existing color, for example:

css

    section {
      --base-color: #faa6ff;
      background-color: --transparent(var(--base-color), 0.8);
    }
    

The function is called by using [`<dashed-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function)
 syntax, which is the function name with parentheses on the end. The desired argument values are specified inside the parentheses.

**Note:** If multiple CSS functions are given the same name, the function in the stronger cascade [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
 wins. If all of them are in the same layer, the function defined last in the source order wins.

### [Specifying data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#specifying_data_types)

It is possible to specify data types for the function parameters and return types. For example:

css

    @function --transparent(--color <color>, --alpha <number>) returns <color> {
      result: oklch(from var(--color) l c h / var(--alpha));
    }
    

Now the function will only produce a valid value if the input arguments are a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 and a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, respectively, and the `result` is a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
. If not, for example:

css

    section {
      --base-color: #faa6ff;
      background-color: --transparent(var(--base-color), 50%);
    }
    

then the value will become invalid at computed-value time (because the specified `--alpha` argument is a `<percentage>` and not a `<number>` as expected) and the `background-color` will end up being set to `transparent`.

You can specify multiple accepted data types using a [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
 function with the `|` symbol as a separator, for example:

css

    @function --transparent(--color <color>, --alpha type(<number> | <percentage>))
      returns <color> {
      result: oklch(from var(--color) l c h / var(--alpha));
    }
    

With this adjustment, the `--transparent(var(--base-color), 50%)` function call is now valid.

### [Specifying default values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#specifying_default_values)

You can also specify default values for parameters, after a colon at the end of their definition. For example:

css

    @function --transparent(--color <color>, --alpha <number>: 0.8) returns <color> {
      result: oklch(from var(--color) l c h / var(--alpha));
    }
    

The `--alpha` parameter's default value is now `0.8`. If you want to use this value, you can omit the second argument when calling the function:

css

    section {
      --base-color: #faa6ff;
      background-color: --transparent(var(--base-color));
    }
    

**Note:** If an invalid value is passed in as a function argument and a default value is specified in that parameter definition, the invalid value will be ignored, and the default value will be used instead.

### [Passing comma-containing values as arguments](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#passing_comma-containing_values_as_arguments)

In the next example, the `--max-plus-x()` function expects to be passed a comma-separated list of lengths and a single length as arguments. It uses the CSS [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
 function to determine which of the list of lengths is the largest, adds it to the single length, then returns the result.

css

    @function --max-plus-x(--list <length>#, --x <length>) {
      result: calc(max(var(--list)) + var(--x));
    }
    

The first argument needs to be a comma-separated list, which could be misinterpreted as three separate arguments. To get around this problem, you can wrap the value in curly braces when passing it into the function call:

css

    div {
      width: --max-plus-x({1px, 7px, 2px}, 3px); /* 10px */
    }
    

### [Including custom properties inside functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#including_custom_properties_inside_functions)

As we've already seen, function parameters are defined as custom properties, which are then available inside the function body.

You can also specify custom properties inside the function body that will act as locally-scoped constants. In the following example, we define a function called `--anim-1s()`, which returns an [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand value where the duration and easing values are always the same, and only the animation name and count are varied.

css

    @function --anim-1s(--animation, --count) {
      --duration: 1s;
      --easing: linear;
      result: var(--animation) var(--duration) var(--count) var(--easing);
    }
    

This kind of usage allows you to write easier, more expressive syntax for animations, provided you know that you always want the duration and easing function to be the same:

css

    animation: --anim-1s(bounce, 2);
    

It is also worth noting that you can call one custom function from inside another. In such cases, a custom function can access local variables and function parameters from functions higher up in the call stack. Here, the outer function's parameter and local custom property will be available inside the scope of the inner function:

css

    @function --outer(--outer-arg) {
      --outer-local: 2;
      result: --inner();
    }
    
    @function --inner() returns <number> {
      result: calc(var(--outer-arg) + var(--outer-local));
    }
    
    div {
      z-index: --outer(1); /* 3 */
    }
    

In addition, custom properties defined on the same element where the custom function is being called will be available to it:

css

    @function --double-z() returns <number> {
      result: calc(var(--z) * 2);
    }
    
    div {
      --z: 3;
      z-index: --double-z(); /* 6 */
    }
    

When a custom property of the same name is defined in multiple places, function parameters override custom properties defined on the same element, and local custom properties defined inside the function body override both. In the following example, the `--add-a-b-c()` function uses the `--a` property from the `div` rule's custom property, the `--b` property from the function parameter, and the `--c` local custom property.

css

    @function --add-a-b-c(--b, --c) {
      --c: 300;
      result: calc(var(--a) + var(--b) + var(--c));
    }
    
    div {
      --a: 1;
      --b: 2;
      --c: 3;
      z-index: --add-a-b-c(20, 30); /* 321 */
    }
    

### [Including complex logic](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#including_complex_logic)

You can include more complex logic in functions using constructs such as [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rules and [`if()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if)
 functions. For example, the next function takes two arguments, one for a narrow-screen layout and one for a wide-screen layout. It returns the latter by default, but returns the former when the viewport width is less than `700px` wide, as detected using a media query.

css

    @function --narrow-wide(--narrow, --wide) {
      result: var(--wide);
      @media (width < 700px) {
        result: var(--narrow);
      }
    }
    

You can include multiple `result` descriptors to express different results for different logic outcomes.

**Note:** CSS functions behave in the same way as the rest of CSS regarding conflict resolution — last in source order wins. Therefore, in the above function, the `result` is `var(--wide)` unless the media query test returns true, in which case it is overridden by `var(--narrow)`.

There are no early returns in CSS functions like there are in JavaScript functions. In the above function, if the media query was written first, before the single `result` line, the `result` would always be `var(--wide)` because it would override `var(--narrow)` in cases where the media query test returns true.

We could rewrite the CSS custom function to use an `if()` function instead:

css

    @function --narrow-wide(--narrow, --wide) {
      result: if(media(width < 700px): var(--narrow) ; else: var(--wide));
    }
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#formal_syntax)

-------------------------------------------------------------------------------------------------------------

@function =   
  @function <function-token> <function-parameter>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 ) [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 returns <css-type> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 { <declaration-rule-list> }    
  
<function-parameter> =   
  <custom-property-name> <css-type>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 : <default-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<css-type> =   
  <syntax-component>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <type()>              
  
<default-value> =   
  <declaration-value>    
  
<syntax-component> =   
  <syntax-single-component> <syntax-multiplier>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '<' transform-list '>'                            
  
[<type()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
 =   
  type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 )    
  
<syntax-single-component> =   
  '<' <syntax-type-name> '>'  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
                       
  
<syntax-multiplier> =   
  '#'  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '+'    
  
<syntax-type-name> =   
  angle               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  custom-ident        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  image               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  integer             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  length              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  length-percentage   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  number              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  percentage          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  resolution          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  string              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  time                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  url                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  transform-function    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#examples)

---------------------------------------------------------------------------------------------------

For more examples, see our [Using CSS custom functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
 guide.

### [Basic `@function` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#basic_function_usage)

This example shows a basic function that doubles the value passed into it.

#### HTML

The markup features a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element containing some text content:

html

    <p>Some content</p>
    

#### CSS

In our styles, we first define the CSS custom function. The function is called `--double`, and accepts a single parameter of any type, which we've called `--value`. Inside the function body, we include a `result` descriptor that uses the [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 function to double the passed argument:

css

    @function --double(--value) {
      result: calc(var(--value) * 2);
    }
    

Next, we define a `--base-spacing` custom property with a value of `10px`. We assign that property to the [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 value, but then double it for the [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 value using the `--double()` custom function.

    html,
    body {
      height: 100%;
    }
    
    body {
      margin: 0;
      display: grid;
      place-items: center;
      font-family: system-ui;
    }
    

css

    p {
      --base-spacing: 10px;
      border-radius: var(--base-spacing);
      padding: --double(var(--base-spacing));
      width: 50%;
      background-color: wheat;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Functions and Mixins Module  <br>\# function-rule](https://drafts.csswg.org/css-mixins-1/#function-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#see_also)

---------------------------------------------------------------------------------------------------

*   [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
    
*   [`<dashed-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function)
     data type
*   [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
     function
*   [Using CSS custom functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
    
*   [CSS custom functions and mixins](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@function/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")