*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#mdn-search)
    

`type()` CSS function
=====================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/300)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#browser_compatibility)
 carefully before using this in production.

The **`type()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 allows you to specify a particular data type, and is used by the following CSS features:

*   The [`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
     function, to specify the data type that an attribute value should be parsed into.
*   The [`@function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
     at-rule, to specify the permitted data types for [CSS custom function](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
     parameters and results.

**Note:** The [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 at-rule [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
 descriptor value uses the same `<syntax>` to define the permitted data types for registered [custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
, however, this always takes the form of a string.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#syntax)

----------------------------------------------------------------------------------------

css

    /* Single value */
    type(<color>)
    type(auto)
    
    /* "|" combinator for multiple types */
    type(<length> | <percentage>)
    
    /* Space-separated list of values */
    type(<color>+)
    
    /* Comma-separated list of values */
    type(<length>#)
    
    /* Multiple keywords */
    type(red | blue | green)
    
    /* Combination of data type and keyword */
    type(<percentage> | auto)
    
    /* Universal syntax value */
    type(*)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#parameters)

The `type()` function's syntax is as follows:

type(<syntax>)

The `<syntax>` parameter is an expression defining the data type. This can take the following forms:

[`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#ident)

A CSS keyword value, written without angle brackets.

[`<syntax-type>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#syntax-type)

A type name, written in angle brackets, representing a CSS data type. The following data types are supported:

[`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#angle)

Accepts any valid [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 value.

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#color)

Accepts any valid [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value.

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#custom-ident)

Accepts any valid [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 value.

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#image)

Accepts any valid [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 value.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#integer)

Accepts any valid [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 value.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#length)

Accepts any valid [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#length-percentage)

Accepts any valid [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value and any valid [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 expression combining `<length>` and `<percentage>` values.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#number)

Accepts any valid [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 value.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#percentage)

Accepts any valid [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value.

[`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#resolution)

Accepts any valid [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
 value.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#string)

Accepts any valid [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 value.

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#time)

Accepts any valid [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 value.

[`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#transform-function)

Accepts any valid [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 value.

[`<transform-list>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#transform-list)

Accepts a list of valid [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 values. It is equivalent to `"<transform-function>+"`, and may not be followed by a `+` or `#` token.

[`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#url)

Accepts any valid [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 value.

[`*`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#sect)

The universal syntax.

You can combine `<syntax-type>` values using the following tokens:

[`+`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#sect_2)

A space-separated list of values is expected.

[`#`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#sect_3)

A comma-separated list of values is expected.

In addition, the `|` token can be used as a separator when specifying multiple values or combining `<ident>` and `<syntax-type>` values for the expected syntax.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#return_value)

A data type definition.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#description)

--------------------------------------------------------------------------------------------------

The `type()` function is used when you need to define a data type. It can be considered as a subset of the overall value definition syntax used to define the set of valid values for every CSS property and function.

Most commonly, you'll see `type()` used to specify a single data type. The next example uses the [`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
 function to set the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 property equal to the value of a user-defined `data-background` function. The required data type for the value has been specified as a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
.

css

    background-color: attr(data-background type(<color>), red);
    

You could also specify an exact keyword requirement (for example, `type(blue)`), but this would be overly limiting.

Specifying `type(*)` permits any valid CSS value. This is the universal syntax, which cannot be multiplied or combined with other syntax components.

### [Specifying multiple permitted types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#specifying_multiple_permitted_types)

You can use the `|` token as a separator when specifying a range of permitted data types, keywords, or a combination of both. For example:

*   `type(<length> | <percentage>)`
*   `type(red | green)`
*   `type(<length> | auto)`

The following example shows how a [`@function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
 at-rule can be used to define a [custom function](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
 that takes two color parameters, and returns the first one unless the viewport width is less than `700px`, in which case it returns the second one. The first one is allowed to be `red` or `green`, while the second one has to be `blue`.

css

    @function --color-choice(--color1 type(red | green), --color2 blue) {
      result: var(--color1);
      @media (width < 700px) {
        result: var(--color2);
      }
    }
    

**Note:** In the case of `@function` data types, you can omit the `type()` function and just include the value in cases where only one data type or keyword is specified. This is the case with the `blue` type definition in the previous custom function. This doesn't work with the `attr()` function.

### [Specifying lists of types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#specifying_lists_of_types)

The `+` and `#` tokens can be appended to a `<syntax-type>` to specify that you are expecting a space-separated list or a comma-separated list, respectively. For example:

*   A `<color>+` parameter expects a space-separated list of `<color>` values, for example `red blue #a60000 rgb(234 45 100)`.
*   A `<length>#` parameter expects a comma-separated lists of `<length>` values, for example `30px, 1em, 15vw`.

You can combine multiple tokens using `|` as a separator. For example, `<color># | <integer>#` would expect a comma-separated list of `<color>` values or a comma-separated list of `<integer>` values.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#formal_syntax)

------------------------------------------------------------------------------------------------------

<type()> =   
  type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#examples)

--------------------------------------------------------------------------------------------

You can find several other examples in the [`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
 and [`@function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
 documentation.

### [Basic `@function` data type definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#basic_function_data_type_definition)

This example defines a CSS custom function that combines multiple strings.

#### HTML

The HTML contains a single [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element with some text content.

html

    <section>What you gonna say?</section>
    

#### CSS

In the CSS, we start by specifying a `@function` called `--combine-strings`. This has a parameter called `--strings`, the data type of which is specified as one or more space-separated `<string>` values. It returns the string values with a space and a heart emoji appended onto the end.

css

    @function --combine-strings(--strings type(<string>+)) {
      result: var(--strings) " ❤️";
    }
    

We then specify some basic styles for the `<section>` element and use the `--combine-strings()` function to specify the value of its [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property, including two space-separated strings as the argument.

css

    section {
      font-family: system-ui;
      background-color: lime;
      padding: 20px;
    }
    
    section::after {
      content: --combine-strings("hello" "goodbye");
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Functions and Mixins Module  <br>\# funcdef-function-type](https://drafts.csswg.org/css-mixins-1/#funcdef-function-type) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type#see_also)

--------------------------------------------------------------------------------------------

*   [`@function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
     at-rule
*   [`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
     function
*   [Using CSS custom functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/type/index.md?plain=1 "Folder: en-us/web/css/reference/values/type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftype&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftype%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftype%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftype%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")