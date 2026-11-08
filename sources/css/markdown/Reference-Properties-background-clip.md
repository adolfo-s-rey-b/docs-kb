*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#mdn-search)
    

`background-clip` CSS property
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-clip`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether an element's background extends underneath its border box, padding box, or content box.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#try_it)

-------------------------------------------------------------------------------------------------------

    background-clip: border-box;
    

    background-clip: padding-box;
    

    background-clip: content-box;
    

    background-clip: text;
    color: transparent;
    text-shadow: none;
    

    <section id="default-example">
      <div id="example-element">This is the content of the element.</div>
    </section>
    

    #example-element {
      background-image: url("/shared-assets/images/examples/leopard.jpg");
      color: white;
      text-shadow: 2px 2px black;
      padding: 20px;
      border: 10px dashed #333333;
      font-size: 2em;
      font-weight: bold;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    background-clip: border-box;
    background-clip: padding-box;
    background-clip: content-box;
    background-clip: text;
    background-clip: border-area;
    
    /* Global values */
    background-clip: inherit;
    background-clip: initial;
    background-clip: revert;
    background-clip: revert-layer;
    background-clip: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#values)

[`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#border-box)

The background extends to the outside edge of the border (but underneath the border in z-ordering).

[`padding-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#padding-box)

The background extends to the outside edge of the padding. No background is drawn beneath the border.

[`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#content-box)

The background is painted within (clipped to) the content box.

[`text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#text)

The background is painted within (clipped to) the foreground text.

[`border-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#border-area)

The background is painted within (clipped to) the area painted by the border, taking [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
 and [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 into account but ignoring any transparency introduced by [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#description)

-----------------------------------------------------------------------------------------------------------------

The background is always drawn behind the border, so `background-clip: border-box` has a visual effect only when the border is partially opaque or has transparent or partially opaque regions. Also, the `background-clip: text` property has little to no visual effect if the text is fully or partially opaque.

**Note:** Because the [root element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 has a different background painting area, the `background-clip` property has no effect when specified on it. See "[The backgrounds of special elements.](https://drafts.csswg.org/css-backgrounds-3/#special-backgrounds "External link (opens in new tab)")
"

**Note:** For documents whose [root element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 is an HTML element: if the computed value of [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 on the root element is `none` and its [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 is `transparent`, user agents must instead propagate the computed values of the `background` properties from that element's first HTML [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 child element. The used values of that `<body>` element's `background` properties are their initial values, and the propagated values are treated as if they were specified on the root element. It is recommended that authors of HTML documents specify the canvas background for the `<body>` element rather than the HTML element.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#accessibility)

---------------------------------------------------------------------------------------------------------------------

When using `background-clip: text`, check that the contrast ratio between the background color and the color of the text placed over it is high enough that people experiencing low vision conditions will be able to read the content of the page.

If the background image does not load, this could also lead to the text becoming unreadable. Add a fallback [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 to prevent this from happening, and test without the image.

Consider using feature queries with [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 to test for support of `background-clip: text` and provide an accessible alternative where it is not supported.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `border-box` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a repeatable list |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

background-clip =   
  <bg-clip>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<bg-clip> =   
  <visual-box>             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 border-area [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 text [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<visual-box> =   
  content-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  padding-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  border-box     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#examples)

-----------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#html)

html

    <p class="border-box">The background extends behind the border.</p>
    <p class="padding-box">
      The background extends to the inside edge of the border.
    </p>
    <p class="content-box">
      The background extends only to the edge of the content box.
    </p>
    <p class="text">The background is clipped to the foreground text.</p>
    <p class="border-area">
      The background is clipped to the area painted by the border.
    </p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#css)

css

    p {
      border: 0.8em darkviolet;
      border-style: dotted double;
      margin: 1em 0;
      padding: 1.4em;
      background: linear-gradient(60deg, red, yellow, red, yellow, red);
      font: 900 1.2em sans-serif;
      text-decoration: underline;
    }
    
    .border-box {
      background-clip: border-box;
    }
    .padding-box {
      background-clip: padding-box;
    }
    .content-box {
      background-clip: content-box;
    }
    
    .text {
      background-clip: text;
      color: rgb(0 0 0 / 20%);
    }
    
    .border-area {
      background-clip: border-area;
      border-color: transparent;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# background-clip](https://drafts.csswg.org/css-backgrounds/#background-clip) |
| [CSS Backgrounds Module Level 4  <br>\# background-clip](https://drafts.csswg.org/css-backgrounds-4/#background-clip) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip#see_also)

-----------------------------------------------------------------------------------------------------------

*   The [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
     property creates a clipping region that defines what part of an _entire element_ should be displayed.
*   Background properties: [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    , [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    
*   [Introduction to the CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-clip/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-clip (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-clip&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-clip%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-clip%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-clip%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")