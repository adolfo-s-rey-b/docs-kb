*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#mdn-search)
    

`tab-size` CSS property
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since August 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`tab-size`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is used to customize the width of tab characters (U+0009).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#try_it)

------------------------------------------------------------------------------------------------

    tab-size: 10px;
    

    tab-size: 16px;
    

    tab-size: 24px;
    

    tab-size: 4;
    

    <section id="default-example">
      <pre id="example-element">&#9;123</pre>
    </section>
    

    #example-element {
      border: 1px solid;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#syntax)

------------------------------------------------------------------------------------------------

css

    /* <number> values */
    tab-size: 4;
    tab-size: 0;
    
    /* <length> values */
    tab-size: 10px;
    tab-size: 2em;
    
    /* Global values */
    tab-size: inherit;
    tab-size: initial;
    tab-size: revert;
    tab-size: revert-layer;
    tab-size: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#values)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

A multiple of the advance width of the space character (U+0020) to be used as the width of tabs. Must be non-negative. The advance width means the distance a cursor or a print head moves before printing the next character.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The width of tabs. Must be non-negative.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#formal_definition)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `8` |
| Applies to | block containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified integer or an absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#formal_syntax)

--------------------------------------------------------------------------------------------------------------

tab-size =   
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#examples)

----------------------------------------------------------------------------------------------------

### [Expanding by character count](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#expanding_by_character_count)

css

    pre {
      tab-size: 4; /* Set tab size to 4 characters wide */
    }
    

### [Collapse tabs](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#collapse_tabs)

css

    pre {
      tab-size: 0; /* Remove indentation */
    }
    

### [Default tab size vs custom sizes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#default_tab_size_vs_custom_sizes)

This example compares a default tab size with a custom tab size. Note that [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 is set to `pre` to prevent the tabs from collapsing.

#### HTML

html

    <p>no tab</p>
    <p>&#0009;default tab size of 8 characters wide</p>
    <p class="custom-number">&#0009;custom tab size of 3 characters wide</p>
    <p>&nbsp;&nbsp;&nbsp;3 spaces, equivalent to the custom tab size</p>
    <p class="custom-length">&#0009;custom tab size of 50px wide</p>
    

#### CSS

    body {
      border: 1px solid red;
      margin: 1rem;
    }
    

css

    p {
      white-space: pre;
    }
    
    .custom-number {
      tab-size: 3;
    }
    
    .custom-length {
      tab-size: 50px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# tab-size-property](https://drafts.csswg.org/css-text/#tab-size-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size#see_also)

----------------------------------------------------------------------------------------------------

*   [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/tab-size/index.md?plain=1 "Folder: en-us/web/css/reference/properties/tab-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftab-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftab-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftab-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftab-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")