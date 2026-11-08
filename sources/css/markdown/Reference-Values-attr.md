*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#mdn-search)
    

`attr()` CSS function
=====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** The `attr()` function can be used with any CSS property, but support for properties other than [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 is experimental.

The **`attr()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is used to retrieve the value of an attribute of the selected element and use it in a property value, similar to how the [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
 function substitutes a custom property value. It can also be used with [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
, in which case the attribute's value on the pseudo-element's originating element is returned.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#try_it)

----------------------------------------------------------------------------------------

    blockquote {
      margin: 1em 0;
    }
    
    blockquote::after {
      display: block;
      content: " (source: " attr(cite) ") ";
      color: hotpink;
    }
    

    <blockquote cite="https://mozilla.org/en-US/about/">
      Mozilla is working to put control of the internet back in the hands of the
      people using it.
    </blockquote>
    
    <blockquote cite="https://web.dev/about/">
      Build beautiful, accessible, fast, and secure websites that work
      cross-browser.
    </blockquote>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#syntax)

----------------------------------------------------------------------------------------

css

    /* Basic usage */
    attr(data-count)
    attr(href)
    
    /* With type */
    attr(data-width px)
    attr(data-size rem)
    attr(data-name raw-string)
    attr(id type(<custom-ident>))
    attr(data-count type(<number>))
    attr(data-size type(<length> | <percentage>))
    
    /* With fallback */
    attr(data-count type(<number>), 0)
    attr(data-width px, inherit)
    attr(data-something, "default")
    
    /* With namespace */
    attr(color|myAttr type(*), red)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#parameters)

The `attr()` function's syntax is as follows:

attr(<attr-name> <attr-type>? , <fallback-value>?)

The parameters are:

[`<attr-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#attr-name)

The attribute name whose value should be retrieved from the selected HTML element(s).

[Namespaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#namespaces)

The attribute name can contain a [`namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Namespaces)
 which allows the targeting elements of [XML](https://developer.mozilla.org/en-US/docs/Web/XML)
\-based markup languages such as [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 or [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
.

css

    @namespace svg url("http://www.w3.org/2000/svg");
    a {
      fill: attr(svg|myAttr type(*), green);
    }
    

**Note:** If no namespace is specified (just an identifier is given, like `attr(foo)`), the null namespace is implied. This is usually what's desired, as namespaced attributes are rare. As with attribute selectors, the case-sensitivity of `<attr-name>` depends on the document language.

[`<attr-type>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#attr-type)

Specifies how the attribute value is parsed into a CSS value. This can be the `raw-string` keyword, a [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
 function, or a CSS dimension unit (specified using an `<attr-unit>` identifier). When omitted, it defaults to `raw-string`.

[`raw-string`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#raw-string)

The `raw-string` keyword causes the attribute's literal value to be treated as the value of a CSS string, with no CSS parsing performed (including CSS escapes, whitespace removal, comments, etc.). The `<fallback-value>` is only used if the attribute is omitted; specifying an empty value doesn't trigger the fallback.

css

    attr(data-name raw-string, "stranger")
    

**Note:** This keyword was originally named and supported in Chromium browsers as `string`. Both keywords will be supported briefly, for backward compatibility purposes.

[`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)

The `type()` function takes a `<syntax>` as its argument that specifies what data type to parse the value into.

**Note:** For [security reasons](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#limitations_and_security)
 [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 is not allowed as an `attr()` data type.

[`<attr-unit>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#attr-unit)

The `<attr-unit>` identifier specifies the unit a numeric value should have (if any). It can be the `%` character (percentage) or a [CSS distance unit](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#distance_units)
 such as `px`, `rem`, `deg`, `s`, etc.

css

    attr(data-size rem)
    attr(data-width px, inherit)
    attr(data-rotation deg)
    

[`<fallback-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#fallback-value)

The value to be used if the specified attribute is missing or contains an invalid value.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#return_value)

The return value of `attr()` is the value of the HTML attribute whose name is `<attr-name>` parsed as the given `<attr-type>` or parsed as a CSS string.

When an `<attr-type>` is set, `attr()` will try to parse the attribute into that specified `<attr-type>` and return it. If the attribute cannot be parsed into the given `<attr-type>`, the `<fallback-value>` will be returned instead. When no `<attr-type>` is set, the attribute will be parsed into a CSS string.

If no `<fallback-value>` is set, the return value will default to an empty string when no `<attr-type>` is set or the [guaranteed-invalid value](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
 when an `<attr-type>` is set.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#description)

--------------------------------------------------------------------------------------------------

### [Limitations and security](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#limitations_and_security)

The `attr()` function can reference attributes that were never intended for styling use and might contain sensitive information (for example, a security token used by scripts on the page). In general, this is fine, but it can become a security threat when used in URLs.

For this reason, you can't use `attr()` to dynamically construct URLs:

html

    <!-- This won't work! -->
    <span data-icon="https://example.org/icons/question-mark.svg">help</span>
    

css

    span[data-icon] {
      background-image: url(attr(data-icon));
    }
    

This restriction also applies to any context that could potentially result in a `<url>` value. Values that use `attr()` get marked as _`attr()`\-tainted_, and using them as or in a `<url>` makes a declaration become ["invalid at computed value time" (IACVT)](https://www.bram.us/2024/02/26/css-what-is-iacvt/ "External link (opens in new tab)")
.

So, for example, functions like [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
 that take values that resolve to `<url>` also won't work:

css

    span[data-icon] {
      background: image-set(attr(data-icon));
    }
    

### [Backwards compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#backwards_compatibility)

Generally speaking, the modern `attr()` syntax is backward-compatible because the old way of using it — without specifying an `<attr-type>` — behaves the same as before. Having `attr(data-attr)` in your code is the same as writing `attr(data-attr type(<string>))` or the simpler `attr(data-attr string))`.

However, there are two edge cases where the modern `attr()` syntax behaves differently from the old syntax.

In the following snippet, browsers that don't support the modern `attr()` syntax will discard the second declaration because they cannot parse it. The result in those browsers is `"Hello World"`.

html

    <div text="Hello"></div>
    

css

    div::before {
      content: attr(text) " World";
    }
    div::before {
      content: attr(text) 1px;
    }
    

In browsers with support for the modern syntax, the output will be … nothing. Those browsers will successfully parse the second declaration, but because it is invalid content for the `content` property, the declaration becomes ["invalid at computed value time" or IACVT for short](https://www.bram.us/2024/02/26/css-what-is-iacvt/ "External link (opens in new tab)")
.

To prevent this kind of situation, [feature detection](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#feature_detection)
 is recommended.

A second edge case is the following:

html

    <div id="parent"><div id="child" data-attr="foo"></div></div>
    

css

    #parent {
      --x: attr(data-attr);
    }
    #child::before {
      content: var(--x);
    }
    

Browsers without support for modern syntax display the text `"foo"`. In browsers with modern `attr()` support there is no output.

This is because `attr()` — similar to custom properties that use the `var()` function — gets substituted at [computed value time](https://www.bram.us/2024/02/26/css-what-is-iacvt/#custom-properties "External link (opens in new tab)")
. With the modern behavior, `--x` first tries to read the `data-attr` attribute from the `#parent` element, which results in an empty string because there is no such attribute on `#parent`. That empty string then gets inherited by the `#child` element, resulting in a `content: ;` declaration being set.

To prevent this sort of situation, don't pass inherited `attr()` values onto children unless you explicitly want to.

### [Feature detection](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#feature_detection)

You can feature detect support for modern `attr()` syntax using the [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 at-rule. In the test, try to assign an advanced `attr()` to a (non-custom) CSS property.

For example:

css

    @supports (x: attr(x type(*))) {
      /* Browser has modern attr() support */
    }
    
    @supports not (x: attr(x type(*))) {
      /* Browser does not have modern attr() support */
    }
    

We can perform the same check in JavaScript with [`CSS.supports()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/supports_static)
:

js

    if (CSS.supports("x: attr(x type(*))")) {
      /* Browser has modern attr() support */
    }
    
    if (!CSS.supports("x: attr(x type(*))")) {
      /* Browser does not have modern attr() support */
    }
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#formal_syntax)

------------------------------------------------------------------------------------------------------

<attr()> =   
  attr( <attr-name> <attr-type>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <declaration-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<attr-name> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <ident-token>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 '|' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 <ident-token>    
  
<attr-type> =   
  type( <syntax> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  raw-string        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  number            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <attr-unit>         
  
<syntax> =   
  '\*'                                                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <syntax-component> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <syntax-combinator> <syntax-component> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <syntax-string>                                       
  
<attr-unit> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
<syntax-component> =   
  <syntax-single-component> <syntax-multiplier>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '<' transform-list '>'                            
  
<syntax-combinator> =   
  '|'    
  
<syntax-string> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#examples)

--------------------------------------------------------------------------------------------

### [content property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#content_property)

In this example, we prepend the value of the `data-foo` [`data-*`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)
 [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 to the contents of the [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element.

#### HTML

html

    <p data-foo="hello">world</p>
    

#### CSS

css

    [data-foo]::before {
      content: attr(data-foo) " ";
    }
    

#### Result

### [Using a fallback value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#using_a_fallback_value)

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#browser_compatibility)
 carefully before using this in production.

In this example, we append the value of `data-browser` [`data-*`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)
 [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 to the [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element. If the `data-browser` attribute is missing from the [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element, we append the _fallback_ value of "**Unknown**".

#### HTML

html

    <p data-browser="Firefox">My favorite browser is:</p>
    <p>Your favorite browser is:</p>
    

#### CSS

css

    p::after {
      content: " " attr(data-browser, "Unknown");
      color: tomato;
    }
    

#### Result

### [color value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#color_value)

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#browser_compatibility)
 carefully before using this in production.

In this example, we set the CSS value of [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 to the value of the `data-background` [`data-*`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)
 [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 assigned to the [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element.

#### HTML

html

    <div class="background" data-background="lime">
      background expected to be red if your browser does not support advanced usage
      of attr()
    </div>
    

#### CSS

    .background {
      height: 100vh;
    }
    

css

    .background {
      background-color: red;
    }
    
    .background[data-background] {
      background-color: attr(data-background type(<color>), red);
    }
    

#### Result

### [Using dimension units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#using_dimension_units)

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#browser_compatibility)
 carefully before using this in production.

In this example the `data-rotation` attribute is parsed into a `deg` unit, which specifies the element's rotation.

#### HTML

html

    <div data-rotation="-3">I am rotated by -3 degrees</div>
    <div data-rotation="2">And I by 2 degrees</div>
    <div>And so am I, using the fallback value of 1.5deg</div>
    

#### CSS

    body {
      min-height: 100svh;
      display: grid;
      place-content: center;
      gap: 1em;
    }
    div {
      margin: 0 auto;
      border: 1px solid;
      border-radius: 0.25em;
      padding: 0.5em;
    }
    

css

    div {
      width: fit-content;
      transform-origin: 50% 50%;
      rotate: attr(data-rotation deg, 1.5deg);
    }
    

#### Result

### [Parsing `attr()` values as `<custom-ident>`s](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#parsing_attr_values_as_custom-idents)

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#browser_compatibility)
 carefully before using this in production.

In this example, the values for the [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 property are derived from the `id` attribute of the element. The attribute gets parsed into a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
, which is what [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 accepts as a value.

The resulting values for [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 are `card-1`, `card-2`, `card-3`, etc.

#### HTML

The HTML contains four cards with different `id` attributes and a "Shuffle cards" `<button>`, which shuffles the cards.

html

    <div class="cards">
      <div class="card" id="card-1">1</div>
      <div class="card" id="card-2">2</div>
      <div class="card" id="card-3">3</div>
      <div class="card" id="card-4">4</div>
    </div>
    <button>Shuffle cards</button>
    

    <div class="warning">
      <p>
        Your browser does not support advanced <code>attr()</code>. As a result,
        this demo won't do anything.
      </p>
    </div>
    

#### CSS

The cards are laid out in a flex container:

css

    .cards {
      display: flex;
      flex-direction: row;
      gap: 1em;
      padding: 1em;
    }
    

    :root {
      view-transition-name: none;
    }
    ::view-transition {
      pointer-events: none;
    }
    
    @supports (x: attr(x type(*))) {
      .warning {
        display: none;
      }
    }
    
    @layer layout {
      .card {
        border-radius: 0.25em;
        width: 20vw;
        max-width: 5em;
        aspect-ratio: 1 / 1.6;
        background: lightgrey;
    
        display: grid;
        place-content: center;
        font-size: 2em;
      }
    
      * {
        box-sizing: border-box;
      }
    
      body {
        min-height: 100svh;
        display: grid;
        place-content: center;
      }
    
      button {
        justify-self: center;
      }
    }
    
    @layer warning {
      .warning {
        padding: 1em;
        border: 1px solid #cccccc;
        background: rgb(255 255 205 / 0.8);
        text-align: center;
        order: -1;
        margin: 1em;
      }
    
      .warning > :first-child {
        margin-top: 0;
      }
      .warning > :last-child {
        margin-bottom: 0;
      }
    }
    

On each card, the `attr()` function gets the `id` attribute and parses it into a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
, which is used as the value for the [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 property. When there is no `id` set on a card, the fallback value `none` is used instead.

css

    .card {
      view-transition-name: attr(id type(<custom-ident>), none);
      view-transition-class: card;
    }
    

#### JavaScript

When the `<button>` is pressed, the cards are shuffled. This is done by randomizing the order of an array containing references to all the cards and then updating the [`order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order)
 property of each card to its new array index position.

To animate each card to its new position, [View Transitions](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using)
 are used. This is done by wrapping the `order` update in a call to [`document.startViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/Document/startViewTransition)
.

js

    const shuffle = (array) => {
      for (let i = array.length - 1; i >= 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    };
    
    document.querySelector("button").addEventListener("click", (e) => {
      const $cards = Array.from(document.querySelectorAll(".card"));
      shuffle($cards);
      document.startViewTransition(() => {
        $cards.forEach(($card, i) => {
          $card.style.setProperty("order", i);
        });
      });
    });
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 5  <br>\# attr-notation](https://drafts.csswg.org/css-values-5/#attr-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr#see_also)

--------------------------------------------------------------------------------------------

*   [Attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
    
*   [HTML `data-*` attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)
    
*   [SVG `data-*` attributes](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/data-*)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/attr/index.md?plain=1 "Folder: en-us/web/css/reference/values/attr (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fattr&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fattr%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fattr%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fattr%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe2c34c75df6238fbeff790100cea1ab7e552e49e%0A*+Document+last+modified%3A+2026-09-04T19%3A00%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")