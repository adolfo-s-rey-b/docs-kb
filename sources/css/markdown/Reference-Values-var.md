*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#mdn-search)
    

`var()` CSS function
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`var()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 can be used to insert the value of a [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 (sometimes called a "CSS variable") instead of any part of a value of another property.

The `var()` function cannot be used in property names, selectors or anything else besides property values. (Doing so usually produces invalid syntax, or else a value whose meaning has no connection to the variable.)

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#try_it)

---------------------------------------------------------------------------------------

    border-color: var(--color-a);
    

    border-color: var(--color-b);
    

    border-color: var(--color-c);
    

    <section class="default-example" id="default-example">
      <div id="example-element">
        Three color options have been set on the :root use these to change the
        border color.
      </div>
    </section>
    

    :root {
      --color-a: pink;
      --color-b: green;
      --color-c: rebeccapurple;
    }
    
    #example-element {
      border: 10px solid black;
      padding: 10px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#syntax)

---------------------------------------------------------------------------------------

css

    /* Basic usage */
    var(--custom-prop);
    
    /* With fallback */
    var(--custom-prop,);  /* empty value as fallback */
    var(--custom-prop, initial); /* initial value of the property as fallback */
    var(--custom-prop, red);
    var(--custom-prop, var(--default-value));
    var(--custom-prop, var(--default-value, red));
    

The first argument to the function is the name of the custom property to be substituted. An optional second argument to the function serves as a fallback value. The fallback is used when the referenced custom property doesn't have a usable value — what the specification calls the [guaranteed-invalid value](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
. In practice, this means the fallback is used when:

*   The custom property hasn't been declared on a rule that applies to the element, and it isn't registered (with [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
    ) with an `initial-value` descriptor.
*   The custom property is set to the [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
     keyword and isn't a registered custom property with an `initial-value`. Setting a non-registered custom property to `initial` resets it to the [guaranteed-invalid value](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
    .
*   The custom property's declared value is [invalid at computed-value time](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling#invalid_custom_properties)
     — for example, because of a cyclic dependency between custom properties — and the property is non-registered or is registered with the universal `*` syntax.

If the custom property is registered with [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 using a non-universal `syntax` and an `initial-value`, that initial value is substituted when no other declaration applies. The fallback is _not_ used in that case.

The other [CSS-wide keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#css-wide_keywords)
 — `inherit`, `unset`, `revert`, `revert-layer`, and `revert-rule` — behave in the same way when set as a custom property value as they do on any other property. They can resolve the custom property to an inherited or previously-cascaded value rather than to the [guaranteed-invalid value](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
, so they don't necessarily trigger the fallback. For example, if `--foo` is set to `revert-layer` in one cascade layer and to a color in another layer, `var(--foo)` resolves to the color value instead of using the fallback.

The syntax of the fallback, like that of custom properties, allows commas. For example, `var(--foo, red, blue)` defines a fallback of `red, blue`; that is, anything between the first comma and the end of the function is considered a fallback value.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#values)

[`<custom-property-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#custom-property-name)

A custom property's name represented by an identifier that starts with two dashes. Custom properties are solely for use by authors and users; CSS will never give them a meaning beyond what is presented here.

[`<declaration-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#declaration-value)

A fallback value for the custom property, used when the referenced custom property has the [guaranteed-invalid value](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
 (see the [Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#syntax)
 section above for the conditions under which this happens). This value may contain any character except some characters with special meaning like newlines, unmatched closing brackets, i.e., `)`, `]`, or `}`, top-level semicolons, or exclamation marks. The fallback value can itself be a custom property using the `var()` syntax. If the fallback value is omitted, and the custom property has the [guaranteed-invalid value](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
, the `var()` function resolves to an [invalid value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#invalid_values)
.

**Note:** `var(--a,)` is valid, specifying that if the `--a` custom property has the guaranteed-invalid value, the `var()` should be replaced with nothing.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#formal_syntax)

-----------------------------------------------------------------------------------------------------

<var()> =   
  var( <custom-property-name> , <declaration-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#examples)

-------------------------------------------------------------------------------------------

### [Using a custom property set on :root](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#using_a_custom_property_set_on_root)

#### CSS

css

    :root {
      --main-bg-color: pink;
    }
    
    body {
      background-color: var(--main-bg-color);
    }
    

#### Result

Here, the value of the `background-color` property has been set via the custom property `--main-bg-color`. So the background color of the HTML body will be pink.

### [Using a custom property before it is set](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#using_a_custom_property_before_it_is_set)

#### CSS

css

    body {
      background-color: var(--main-bg-color);
    }
    
    :root {
      --main-bg-color: pink;
    }
    

#### Result

In this example, the background color of the HTML body will be pink even though the custom property is set later.

### [Using a custom property set in another file](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#using_a_custom_property_set_in_another_file)

#### HTML

html

    <!doctype html>
    <html lang="en-US">
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="1.css" />
        <link rel="stylesheet" href="2.css" />
      </head>
      <body></body>
    </html>
    

#### CSS

css

    /* 1.css */
    body {
      background-color: var(--main-bg-color);
    }
    

css

    /* 2.css */
    :root {
      --main-bg-color: pink;
    }
    

#### Result

The background color of the HTML body will be pink in this case even though the custom property is declared in another file.

### [Custom properties with fallbacks for use when the property has not been set](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#custom_properties_with_fallbacks_for_use_when_the_property_has_not_been_set)

#### HTML

html

    <div class="component">
      <h1 class="header">Header</h1>
      <p class="text">Text</p>
    </div>
    

#### CSS

css

    /* In the component's style: */
    .component .header {
      /* header-color isn't set, and so remains blue, the fallback value */
      color: var(--header-color, blue);
    }
    
    .component .text {
      color: var(--text-color, black);
    }
    
    /* In the larger application's style: */
    .component {
      --text-color: #008800;
    }
    

#### Result

Since `--header-color` isn't set, the text "Header" will be blue, the fallback value.

### [Using a custom property as a fallback](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#using_a_custom_property_as_a_fallback)

#### CSS

css

    :root {
      --backup-bg-color: teal;
    }
    
    body {
      background-color: var(--main-bg-color, var(--backup-bg-color, white));
    }
    

#### Result

Since `--main-bg-color` isn't set, the body's `background-color` will fall back to `--backup-bg-color`, which is teal.

### [Invalid values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#invalid_values)

`var()` functions can resolve to invalid values if:

*   The custom property is not defined and no fallback value is provided.
*   The custom property is defined but its value is an invalid value for the property it is used in.

When this happens, the property is treated as if it has value [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
. This is because variables can't "fail early" like other syntax errors can, so by the time the user agent realizes a property value is invalid, it has already thrown away the other cascaded values.

For example:

#### HTML

html

    <p class="p1">Undefined variable</p>
    <p class="p2">Invalid variable</p>
    <p class="p3">Invalid literal color</p>
    

#### CSS

css

    p {
      color: red;
    }
    
    .p1 {
      color: var(--invalid-color);
    }
    
    .p2 {
      --invalid-color: 20px;
      color: var(--invalid-color);
    }
    
    .p3 {
      color: 20px;
    }
    

#### Result

Note how the paragraphs using `var()` are reset to the default black, but the paragraph with an invalid literal color is still red, because the `color: 20px` declaration is simply ignored.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Custom Properties for Cascading Variables Module Level 1  <br>\# using-variables](https://drafts.csswg.org/css-variables/#using-variables) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#see_also)

-------------------------------------------------------------------------------------------

*   [`env(…)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
     – read‑only environment variables controlled by the user‑agent.
*   [Using CSS custom properties (variables)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
    
*   [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
     at-rule
*   [Registering CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Registering_properties)
    
*   [CSS custom properties for cascading variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/var/index.md?plain=1 "Folder: en-us/web/css/reference/values/var (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fvar&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fvar%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fvar%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fvar%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")