*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#mdn-search)
    

`<dashed-function>` CSS type
============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/300)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#browser_compatibility)
 carefully before using this in production.

The **`<dashed-function>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents the syntax used to call [CSS custom functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
, which are defined using the [`@function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
 at-rule.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#syntax)

---------------------------------------------------------------------------------------------------

A `<dashed-function>` value consists of the [`--function-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#--function-name)
, followed by parentheses containing the function's arguments (for example, `--my-function(30px, 3)`).

You can include `<dashed-function>` values in place of regular CSS property values or property value components, in cases where you want to dynamically calculate the values based on function logic rather than providing static values.

In cases where you want to [pass comma-containing values as arguments](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#passing_comma-containing_values_as_arguments)
, you can do so by wrapping them in curly braces (`{ }`).

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#examples)

-------------------------------------------------------------------------------------------------------

For more examples, see our [Using CSS custom functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
 guide.

### [Basic `<dashed-function>` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#basic_dashed-function_usage)

This example shows a basic function that returns a semi-transparent version of the color passed to it.

#### HTML

The markup features a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 containing some text content:

html

    <p>Some content</p>
    

#### CSS

In our styles, we first define the CSS custom function. The function is called `--transparent` and accepts two parameters: a color and a numeric alpha channel value. Inside the function body, we use [relative color syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
 to transform the passed color into an [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
 color with an alpha channel equal to the passed alpha value; this becomes the function's `result`:

css

    @function --transparent(--color <color>, --alpha <number>) {
      result: oklch(from var(--color) l c h / var(--alpha));
    }
    

Next, we define a `--base-color` custom property with a value of `#faa6ff` on the `:root` element. We assign that property to be the value of the `<p>` element's [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 color, and then set its [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 value to equal a transparent version of the same color. This is done by setting the value to equal the `<dashed-function>` syntax, specifying the `--transparent()` function and passing it arguments of `var(--base-color)` and `0.8`.

    html,
    body {
      height: 100%;
    }
    
    body {
      margin: 0;
      display: grid;
      place-items: center;
      font-family: system-ui;
      background-image: repeating-linear-gradient(
        -45deg,
        transparent 0 20px,
        lightgrey 20px 40px
      );
    }
    

css

    :root {
      --base-color: #faa6ff;
    }
    
    p {
      width: 50%;
      padding: 30px;
      border-radius: 20px;
      border: 3px solid var(--base-color);
      background-color: --transparent(var(--base-color), 0.8);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Functions and Mixins Module  <br>\# using-custom-functions](https://drafts.csswg.org/css-mixins-1/#using-custom-functions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function#see_also)

-------------------------------------------------------------------------------------------------------

*   [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
    
*   [`@function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
     at-rule
*   [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
     function
*   [Using CSS custom functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)
    
*   [CSS custom functions and mixins](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/dashed-function/index.md?plain=1 "Folder: en-us/web/css/reference/values/dashed-function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdashed-function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdashed-function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdashed-function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdashed-function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")