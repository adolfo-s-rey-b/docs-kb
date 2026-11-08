*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#mdn-search)
    

`all` CSS property
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`all`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property resets all of an element's properties except [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
. It can set properties to their initial or inherited values, or to the values specified in another cascade layer or stylesheet origin.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#try_it)

-------------------------------------------------------------------------------------------

    /* no all property */
    

    all: initial;
    

    all: inherit;
    

    all: unset;
    

    all: revert;
    

    <section id="default-example">
      <div class="example-container-bg">
        <div class="example-container">
          <p id="example-element">
            This paragraph has a font size of 1.5rem and a color of gold. It also
            has 1rem of vertical margin set by the user-agent. The parent of the
            paragraph is a &lt;div&gt; with a dashed blue border.
          </p>
        </div>
      </div>
    </section>
    

    #example-element {
      color: gold;
      padding: 10px;
      font-size: 1.5rem;
      text-align: left;
      width: 100%;
    }
    
    .example-container {
      border: 2px dashed #2d5ae1;
    }
    
    .example-container-bg {
      background-color: #77767b;
      padding: 20px;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for all CSS properties except for [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#syntax)

-------------------------------------------------------------------------------------------

css

    /* Global values */
    all: initial;
    all: inherit;
    all: unset;
    all: revert;
    all: revert-layer;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#values)

The `all` property is specified as one of the CSS global keyword values. Note that none of these values affect the [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
 and [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 properties.

[`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)

Specifies that all the element's properties should be changed to their [initial values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
.

[`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)

Specifies that all the element's properties should be changed to their [inherited values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
.

[`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)

Specifies that all the element's properties should be changed to their inherited values if they inherit by default, or to their initial values if not.

[`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)

Specifies behavior that depends on the stylesheet origin to which the declaration belongs:

*   If the rule belongs to the [author origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#author_stylesheets)
    , the `revert` value rolls back the [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
     to the user level, so that the [specified values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
     are calculated as if no author-level rules were specified for the element. For purposes of `revert`, the author origin includes the Override and Animation origins.
*   If the rule belongs to the [user origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#user_stylesheets)
    , the `revert` value rolls back the [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
     to the user-agent level, so that the [specified values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
     are calculated as if no author-level or user-level rules were specified for the element.
*   If the rule belongs to the [user-agent origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#user-agent_stylesheets)
    , the `revert` value acts like `unset`.

[`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)

Specifies that all the element's properties should roll back the cascade to a previous [cascade layer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
, if one exists. If no other cascade layer exists, the element's properties will roll back to the matching rule, if one exists, in the current layer or to a previous [style origin](https://developer.mozilla.org/en-US/docs/Glossary/Style_origin)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#formal_definition)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | There is no practical initial value for it. |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as the specified value applies to each property this is a shorthand for. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand (all properties but [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)<br> and [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)<br>) |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#formal_syntax)

---------------------------------------------------------------------------------------------------------

all =   
  initial       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inherit       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  unset         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  revert        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  revert-layer  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  revert-rule     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#examples)

-----------------------------------------------------------------------------------------------

In this example, the CSS file contains styling for the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
 element in addition to some styling for the parent `<body>` element. Various outputs in the Results subsection demonstrate how the styling of the `<blockquote>` element is affected when different values are applied to the `all` property inside the `blockquote` rule.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#html)

html

    <blockquote id="quote">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </blockquote>
    Phasellus eget velit sagittis.
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#css)

css

    body {
      font-size: small;
      background-color: #f0f0f0;
      color: blue;
      margin: 0;
      padding: 0;
    }
    
    blockquote {
      background-color: skyblue;
      color: red;
    }
    

### [Results](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#results)

#### A. No `all` property

    <blockquote id="quote">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </blockquote>
    Phasellus eget velit sagittis.
    

    body {
      font-size: small;
      background-color: #f0f0f0;
      color: blue;
    }
    blockquote {
      background-color: skyblue;
      color: red;
    }
    

This is the scenario in which no `all` property is set inside the `blockquote` rule. The [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
 element uses the browser's default styling which gives it a margin, together with a specific background and text color as specified in the stylesheet. It also behaves as a _block_ element: the text that follows it is beneath it.

#### B. `all: initial`

    <blockquote id="quote">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </blockquote>
    Phasellus eget velit sagittis.
    

    body {
      font-size: small;
      background-color: #f0f0f0;
      color: blue;
    }
    blockquote {
      background-color: skyblue;
      color: red;
      all: initial;
    }
    

With the `all` property set to `initial` in the `blockquote` rule, the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
 element doesn't use the browser default styling anymore: it is an _inline_ element now (initial value), its [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#formal_definition)
 is `transparent` (initial value), its [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#formal_definition)
 is `medium`, and its [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color#formal_definition)
 is `black` (initial value).

#### C. `all: inherit`

    <blockquote id="quote">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </blockquote>
    Phasellus eget velit sagittis.
    

    body {
      font-size: small;
      background-color: #f0f0f0;
      color: blue;
    }
    blockquote {
      background-color: skyblue;
      color: red;
      all: inherit;
    }
    

In this case, the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
 element doesn't use the browser default styling. Instead, it inherits style values from its parent [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element: it is a _block_ element now (inherited value), its [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 is `#F0F0F0` (inherited value), its [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 is `small` (inherited value), and its [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 is `blue` (inherited value).

#### D. `all: unset`

    <blockquote id="quote">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </blockquote>
    Phasellus eget velit sagittis.
    

    body {
      font-size: small;
      background-color: #f0f0f0;
      color: blue;
    }
    blockquote {
      background-color: skyblue;
      color: red;
      all: unset;
    }
    

When the `unset` value is applied to the `all` property in the `blockquote` rule, the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
 element doesn't use the browser default styling. Because [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#formal_definition)
 is a non-inherited property and [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#formal_definition)
 and [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color#formal_definition)
 are inherited properties, the `<blockquote>` element is an _inline_ element now (initial value), its [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 is `transparent` (initial value), but its [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 is still `small` (inherited value), and its [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 is `blue` (inherited value).

#### E. `all: revert`

    <blockquote id="quote">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </blockquote>
    Phasellus eget velit sagittis.
    

    body {
      font-size: small;
      background-color: #f0f0f0;
      color: blue;
    }
    blockquote {
      background-color: skyblue;
      color: red;
      all: revert;
    }
    

When the `all` property is set to `revert` in the `blockquote` rule, the `blockquote` rule is considered to be non-existent and the styling property values are inherited from the ones applied to the parent element `<body>`. So the `<blockquote>` element gets styled as a _block_ element, with [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 `#F0F0F0`, [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 `small`, and [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 `blue` - all values inherited from the `body` rule.

#### F. `all: revert-layer`

    <blockquote id="quote">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </blockquote>
    Phasellus eget velit sagittis.
    

    body {
      font-size: small;
      background-color: #f0f0f0;
      color: blue;
    }
    blockquote {
      background-color: skyblue;
      color: red;
      all: revert-layer;
    }
    

There are no cascade layers defined in the CSS file, so the `<blockquote>` element inherits its style from the matching `body` rule. The `<blockquote>` element here is styled as a _block_ element, with [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 `#F0F0F0`, [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 `small`, and [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 `blue` - all values inherited from the `body` rule. This scenario is an example of the case when `all` set to `revert-layer` behaves the same as when `all` is set to `revert`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 4  <br>\# all-shorthand](https://drafts.csswg.org/css-cascade/#all-shorthand) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all#see_also)

-----------------------------------------------------------------------------------------------

CSS global keyword values: [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
, [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
, [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
, [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
, [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/all/index.md?plain=1 "Folder: en-us/web/css/reference/properties/all (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fall&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fall%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fall%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fall%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8a13259a44523cd17b4fe347088b62c6d7a35265%0A*+Document+last+modified%3A+2026-09-07T03%3A59%3A20.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")