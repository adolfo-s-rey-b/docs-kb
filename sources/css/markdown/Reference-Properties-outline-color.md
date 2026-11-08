*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#mdn-search)
    

`outline-color` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`outline-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the color of an element's outline.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#try_it)

-----------------------------------------------------------------------------------------------------

    outline-color: red;
    

    outline-color: #32a1ce;
    

    outline-color: rgb(170 50 220 / 0.6);
    

    outline-color: hsl(60 90% 50% / 0.8);
    

    outline-color: currentColor;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with an outline around it.
      </div>
    </section>
    

    #example-element {
      outline: 0.75em solid;
      padding: 0.75em;
      width: 80%;
      height: 100px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* <color> values */
    outline-color: #f92525;
    outline-color: rgb(30 222 121);
    outline-color: blue;
    
    /* Global values */
    outline-color: inherit;
    outline-color: initial;
    outline-color: revert;
    outline-color: revert-layer;
    outline-color: unset;
    

The `outline-color` property is specified as any one of the values listed below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#values)

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The color of the outline, specified as a `<color>`.

The specification also lists an additional value, `auto`, which is not currently supported in any browsers. When implemented, `auto` will compute to [`currentColor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#currentcolor_keyword)
 unless [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
 is set to `auto` then it will compute to the [accent color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/accent-color)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#description)

---------------------------------------------------------------------------------------------------------------

An outline is a line that is drawn around an element, outside the [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
. Unlike the element's border, the outline is drawn outside the element's frame, and may overlap other content. The border, on the other hand, will actually alter the page's layout to ensure that it fits without overlapping anything else (unless you explicitly set it to overlap).

It is often more convenient to use the shorthand property [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 when defining the appearance of an outline.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#accessibility)

-------------------------------------------------------------------------------------------------------------------

Custom [focus styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 commonly involve making adjustments to the [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 property. If the color of the outline is adjusted, it is important to ensure that the contrast ratio between it and the background the outline is placed over is high enough that people experiencing low vision conditions will be able to perceive it.

An outline is a visual indicator. In order to meet current [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/ "External link (opens in new tab)")
, [Success Criterion 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast "External link (opens in new tab)")
 requires a contrast ratio of at least 3:1 between the outline and the adjacent colors it sits against. Note that when the outline is used as a focus indicator, the adjacent colors include both the background outside the element and the element's own background when the outline borders both.

*   [WebAIM: Color Contrast Checker](https://webaim.org/resources/contrastchecker/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.11: Non-text Contrast | W3C Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | For the keyword `auto`, the computed value is `currentcolor`. For the color value, if the value is translucent, the computed value will be the `rgba()` corresponding one. If it isn't, it will be the `rgb()` corresponding one. The `transparent` keyword maps to `rgba(0,0,0,0)`. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

outline-color =   
  auto                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<'border-top-color'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
    
  
[<border-top-color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
 =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-1D>    
  
<image-1D> =   
  <stripes()>    
  
<stripes()> =   
  stripes( <color-stripe>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<color-stripe> =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
                            [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<flex>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#examples)

---------------------------------------------------------------------------------------------------------

### [Setting a solid blue outline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#setting_a_solid_blue_outline)

#### HTML

html

    <p>My outline is blue, as you can see.</p>
    

#### CSS

css

    p {
      outline: 2px solid; /* Set the outline width and style */
      outline-color: blue; /* Set the outline color */
      margin: 5px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# outline-color](https://drafts.csswg.org/css-ui/#outline-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color#see_also)

---------------------------------------------------------------------------------------------------------

*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    
*   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
    
*   The [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type
*   Other color-related properties: [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    , [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    , [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    , and [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 29, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/outline-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/outline-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foutline-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foutline-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foutline-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foutline-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4371d98674430c6693a5111df85438e7f5aa8fb7%0A*+Document+last+modified%3A+2026-09-29T16%3A16%3A19.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")