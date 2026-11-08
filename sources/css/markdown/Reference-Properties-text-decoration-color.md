*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#mdn-search)
    

`text-decoration-color` CSS property
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-decoration-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the color of decorations added to text by [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
.

The color applies to decorations, such as underlines, overlines, strikethroughs, and wavy lines like those used to mark misspellings, in the scope of the property's value.

CSS does not provide a direct mechanism for specifying a unique color for each line type. This effect can nevertheless be achieved by nesting elements, applying a different line type to each element (with the [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
 property), and specifying the line color (with `text-decoration-color`) on a per-element basis.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#try_it)

-------------------------------------------------------------------------------------------------------------

    text-decoration-color: red;
    

    text-decoration-color: #21ff21;
    

    text-decoration-color: rgb(255 90 255);
    

    text-decoration-color: hsl(70 100% 40%);
    

    text-decoration-color: currentColor;
    

    <section id="default-example">
      <p>
        I'd far rather be
        <span class="transition-all" id="example-element">happy than right</span>
        any day.
      </p>
    </section>
    

    p {
      font: 1.5em sans-serif;
    }
    
    #example-element {
      text-decoration-line: underline;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* <color> values */
    text-decoration-color: currentColor;
    text-decoration-color: red;
    text-decoration-color: #00ff00;
    text-decoration-color: rgb(255 128 128 / 50%);
    text-decoration-color: transparent;
    
    /* Global values */
    text-decoration-color: inherit;
    text-decoration-color: initial;
    text-decoration-color: revert;
    text-decoration-color: revert-layer;
    text-decoration-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#values)

This property is specified as one `<color>` value:

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The color of the line decoration.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#accessibility)

---------------------------------------------------------------------------------------------------------------------------

It is important to ensure that the contrast ratio between the color of the text, the background the text is placed over, and the text decoration line is high enough that people experiencing low vision conditions will be able to read the content of the page. Color contrast ratio is determined by comparing the luminosity of the text and background color values.

Color alone should not be used to convey meaning. For example, change of text and text-decoration-color alone is not enough to indicate a link has focus.

*   [WebAIM: Color Contrast Checker](https://webaim.org/resources/contrastchecker/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.3 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `currentcolor` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | computed color |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

text-decoration-color =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#examples)

-----------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#basic_example)

html

    <p>
      This paragraph has <s>some erroneous text</s> inside it that I want to call
      attention to.
    </p>
    

css

    p {
      text-decoration-line: underline;
      text-decoration-color: cyan;
    }
    
    s {
      text-decoration-line: line-through;
      text-decoration-color: red;
      text-decoration-style: wavy;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 3  <br>\# text-decoration-color-property](https://drafts.csswg.org/css-text-decor/#text-decoration-color-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color#see_also)

-----------------------------------------------------------------------------------------------------------------

*   When setting multiple line-decoration properties at once, it may be more convenient to use the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
     shorthand property instead.
*   The [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type
*   Other color-related properties: [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    , [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    , [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    , [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    , [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    , and [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-decoration-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-decoration-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")