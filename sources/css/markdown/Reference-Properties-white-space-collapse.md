*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#mdn-search)
    

`white-space-collapse` CSS property
===================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2024.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`white-space-collapse`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls how [white space](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
 inside an element is collapsed.

**Note:** The `white-space-collapse` and [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
 properties can be declared together using the [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 shorthand property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    white-space-collapse: collapse;
    white-space-collapse: preserve;
    white-space-collapse: preserve-breaks;
    white-space-collapse: preserve-spaces;
    white-space-collapse: break-spaces;
    
    /* Global values */
    white-space-collapse: inherit;
    white-space-collapse: initial;
    white-space-collapse: revert;
    white-space-collapse: revert-layer;
    white-space-collapse: unset;
    

The `white-space-collapse` property is specified as a single keyword chosen from the list of values below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#values)

[`collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#collapse)

White space sequences are [collapsed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Whitespace#collapsing_and_transformation)
.

[`preserve`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#preserve)

White space sequences and segment break characters are preserved.

[`preserve-breaks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#preserve-breaks)

White space sequences are collapsed, while segment break characters are preserved.

[`preserve-spaces`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#preserve-spaces)

White space sequences are preserved, while tabs and segment break characters are converted to spaces.

[`break-spaces`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#break-spaces)

The behavior is identical to `preserve`, except that:

*   Any sequence of preserved white space always takes up space, including at the end of the line.
*   A line-breaking opportunity exists after every preserved white space character, including between white space characters.
*   Preserved spaces take up space and do not hang, thus affecting the box's intrinsic sizes ([`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
     size and [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
     size).

**Note:** _Segment break characters_ are characters such as line feeds that cause text to break onto new lines.

**Note:** The [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
 module defines a `discard` value for the `white-space-collapse` property to discard all white space in the element, however, this is not supported in any browsers.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `collapse` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

white-space-collapse =   
  collapse         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  discard          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  preserve         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  preserve-breaks  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  preserve-spaces  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  break-spaces       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#examples)

----------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#html)

html

    <h2 class="collapse">Default behavior;
      all   whitespace   is   collapsed
      in    the          heading       .</h2>
    
    <h2 class="preserve">In this case
      all   whitespace   is   preserved
      in    the          heading       .</h2>
    
    <h2 class="preserve-breaks">In this case only
      the   line breaks  are  preserved
      in    the          heading       .</h2>
    
    <h2 class="preserve-spaces">In this case only
      the   spaces       are  preserved
      in    the          heading       .</h2>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#css)

css

    .collapse {
      white-space-collapse: collapse;
    }
    
    .preserve {
      white-space-collapse: preserve;
    }
    
    .preserve-breaks {
      white-space-collapse: preserve-breaks;
    }
    
    .preserve-spaces {
      white-space-collapse: preserve-spaces;
    }
    
    h2 {
      font-size: 1.6rem;
      font-family: monospace;
      border-bottom: 1px dotted #cccccc;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# white-space-collapsing](https://drafts.csswg.org/css-text-4/#white-space-collapsing) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse#see_also)

----------------------------------------------------------------------------------------------------------------

*   Shorthand for `white-space-collapse` and [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
    : The [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
     property.
*   [CSS text module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
    
*   [Handling whitespace in CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Whitespace)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/white-space-collapse/index.md?plain=1 "Folder: en-us/web/css/reference/properties/white-space-collapse (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwhite-space-collapse&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwhite-space-collapse%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwhite-space-collapse%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwhite-space-collapse%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")