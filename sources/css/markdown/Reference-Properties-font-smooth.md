*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#mdn-search)
    

`font-smooth` CSS property
==========================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`font-smooth`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls the application of anti-aliasing when fonts are rendered.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    font-smooth: auto;
    font-smooth: never;
    font-smooth: always;
    
    /* <length> value */
    font-smooth: 2em;
    
    /* Global values */
    font-smooth: inherit;
    font-smooth: initial;
    font-smooth: revert;
    font-smooth: revert-layer;
    font-smooth: unset;
    

**Note:** WebKit implements a similar property, but with different values: **`-webkit-font-smoothing`**. It only works on macOS.

*   `auto` - Let the browser decide (Uses subpixel anti-aliasing when available; this is the default)
*   `none` - Turn font smoothing off; display text with jagged sharp edges.
*   `antialiased` - Smooth the font on the level of the pixel, as opposed to the subpixel. Switching from subpixel rendering to anti-aliasing for light text on dark backgrounds makes it look lighter.
*   `subpixel-antialiased` - On most non-retina displays, this will give the sharpest text.

**Note:** Firefox implements a similar property, but with different values: **`-moz-osx-font-smoothing`**. It only works on macOS.

*   `auto` - Allow the browser to select an optimization for font smoothing, typically `grayscale`.
*   `grayscale` - Render text with grayscale anti-aliasing, as opposed to the subpixel. Switching from subpixel rendering to anti-aliasing for light text on dark backgrounds makes it look lighter.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

font-smooth =   
  auto             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  never            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  always           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <absolute-size>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
           
  
[<absolute-size>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size)
 =   
  xx-small   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x-small    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  small      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  large      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x-large    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xx-large   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xxx-large    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#examples)

-------------------------------------------------------------------------------------------------------

### [Basic usage example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#basic_usage_example)

The following example shows the Safari/Chromium and Firefox equivalents that turn on font-smoothing on macOS. In both cases the smoothed font should look slightly lighter in weight.

For those of you not on a macOS system, here is a screenshot (the live version appears later on):

![Two texts examples one with the font-smooth property and another one without](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth/smoothing.png)

#### HTML

html

    <p>Without font smoothing</p>
    
    <p class="smoothed">With font smoothing</p>
    

#### CSS

css

    html {
      background-color: black;
      color: white;
      font-size: 3rem;
    }
    
    p {
      text-align: center;
    }
    
    .smoothed {
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#specifications)

-------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth#see_also)

-------------------------------------------------------------------------------------------------------

*   [Please Stop "Fixing" Font Smoothing](https://usabilitypost.com/2012/11/05/stop-fixing-font-smoothing/ "External link (opens in new tab)")
     by Dmitry Fadeyev (2012)
*   [Laissez-faire font smoothing and anti-aliasing](https://www.zachleat.com/web/font-smooth/ "External link (opens in new tab)")
     by Zach Leatherman (2017)
*   [Improve text rendering (A Modern CSS Reset)](https://www.joshwcomeau.com/css/custom-css-reset/#five-improve-text-rendering-6 "External link (opens in new tab)")
     by Josh W. Comeau (2021)
*   [What's the deal with WebKit Font Smoothing?](https://dbushell.com/2024/11/05/webkit-font-smoothing/ "External link (opens in new tab)")
     by David Bushell (2024)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-smooth/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-smooth (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-smooth&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-smooth%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-smooth%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-smooth%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")