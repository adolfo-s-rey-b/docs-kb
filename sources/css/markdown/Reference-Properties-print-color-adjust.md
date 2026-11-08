*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#mdn-search)
    

`print-color-adjust` CSS property
=================================

Baseline 2025

Newly available

Since May 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`print-color-adjust`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets what, if anything, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 may do to optimize the appearance of the element on the output device. By default, the browser is allowed to make any adjustments to the element's appearance it determines to be necessary and prudent given the type and capabilities of the output device.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#syntax)

----------------------------------------------------------------------------------------------------------

css

    print-color-adjust: economy;
    print-color-adjust: exact;
    
    /* Global values */
    print-color-adjust: inherit;
    print-color-adjust: initial;
    print-color-adjust: revert;
    print-color-adjust: revert-layer;
    print-color-adjust: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#values)

This property is specified as one of the following keyword values:

[`economy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#economy)

The user agent is allowed to make adjustments to the element as it deems appropriate and prudent in order to optimize the output for the device it's being rendered for. For example, when printing, a browser might opt to leave out all background images and to adjust text colors to be sure the contrast is optimized for reading on white paper. This is the default.

[`exact`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#exact)

The element's content has been specifically and carefully crafted to use colors, images, and styles in a thoughtful and/or important way, such that being altered by the browser might actually make things worse rather than better. The appearance of the content should not be changed except by the user's request. For example, a page might include a list of information with rows whose background colors alternate between white and a light gray. Removing the background color would decrease the legibility of the content.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#usage_notes)

--------------------------------------------------------------------------------------------------------------------

There are a number of reasons a browser might wish to deviate from the specified appearance, such as:

*   The content uses text and background colors that will be too similar on the output device for legibility purposes.
*   If the output device is a printer, and to save ink, dark or extremely dense background images might be removed.
*   When printing a page, the browser might want to replace light-colored text on a dark background with dark text on a white background.

Any options the user agent offers the user to allow them to control the use of color and images will take priority over the value of `print-color-adjust`. In other words, there isn't any guarantee that `print-color-adjust` will do anything. Not only can the user override the behavior, but each user agent is allowed to decide for itself how to handle `print-color-adjust` in any given situation.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `economy` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

print-color-adjust =   
  economy  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  exact      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#examples)

--------------------------------------------------------------------------------------------------------------

### [Preserving low contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#preserving_low_contrast)

In this example, a box is shown which uses a [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 and a translucent [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
 function atop a black background color to have a dark blue gradient behind medium red text. For whatever reason, this is the desired appearance in any rendering environment, including on paper, so we also use `print-color-adjust: exact` to tell the browser not to make color or style adjustments to the box when rendering it.

#### CSS

css

    .my-box {
      background-color: black;
      background-image: linear-gradient(rgb(0 0 180 / 50%), rgb(70 140 220 / 50%));
      color: #990000;
      width: 15rem;
      height: 6rem;
      text-align: center;
      font:
        24px "Helvetica",
        sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      print-color-adjust: exact;
    }
    

#### HTML

html

    <div class="my-box">
      <p>Need more contrast!</p>
    </div>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Adjustment Module Level 1  <br>\# propdef-print-color-adjust](https://drafts.csswg.org/css-color-adjust/#propdef-print-color-adjust) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust#see_also)

--------------------------------------------------------------------------------------------------------------

*   Other color-related properties: [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    , [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    , [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    , [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    , and [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/print-color-adjust/index.md?plain=1 "Folder: en-us/web/css/reference/properties/print-color-adjust (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fprint-color-adjust&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fprint-color-adjust%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fprint-color-adjust%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fprint-color-adjust%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F28f5f3b9b463fa842fa686ccc73c9e1d9b06282b%0A*+Document+last+modified%3A+2026-08-27T09%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")