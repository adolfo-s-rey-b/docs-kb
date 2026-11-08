*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#mdn-search)
    

`caption-side` CSS property
===========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`caption-side`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property puts the content of a table's [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
 on the specified side. The values are relative to the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 of the table.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#try_it)

----------------------------------------------------------------------------------------------------

    caption-side: top;
    

    caption-side: bottom;
    

    <section class="default-example" id="default-example">
      <table class="transition-all" id="example-element">
        <caption>
          Famous animals
        </caption>
        <tbody>
          <tr>
            <th>Name</th>
            <th>Location</th>
          </tr>
          <tr>
            <td>Giraffe</td>
            <td>Africa</td>
          </tr>
          <tr>
            <td>Penguin</td>
            <td>Antarctica</td>
          </tr>
          <tr>
            <td>Sloth</td>
            <td>South America</td>
          </tr>
          <tr>
            <td>Tiger</td>
            <td>Asia</td>
          </tr>
        </tbody>
      </table>
    </section>
    

    table {
      font-size: 1.2rem;
      text-align: left;
      color: black;
    }
    
    th,
    td {
      padding: 0.2rem 1rem;
    }
    
    caption {
      background: #ffcc33;
      padding: 0.5rem 1rem;
    }
    
    tr {
      background: #eeeeee;
    }
    
    tr:nth-child(even) {
      background: #cccccc;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Directional values */
    caption-side: top;
    caption-side: bottom;
    
    /* Global values */
    caption-side: inherit;
    caption-side: initial;
    caption-side: revert;
    caption-side: revert-layer;
    caption-side: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#values)

This property is specified as one of the following keyword values:

[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#top)

The caption box should be positioned at the block start side of the table.

[`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#bottom)

The caption box should be positioned at the block end side of the table.

**Note:** The [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 module defines two logical values, `inline-start` and `inline-end`, to position the caption box at the inline start edge and inline end edge of the table, respectively. These values are not supported in any browsers.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `top` |
| Applies to | table-caption elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#formal_syntax)

------------------------------------------------------------------------------------------------------------------

caption-side =   
  top     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#examples)

--------------------------------------------------------------------------------------------------------

### [Setting captions above and below](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#setting_captions_above_and_below)

#### HTML

html

    <table class="top">
      <caption>
        Caption ABOVE the table
      </caption>
      <tbody>
        <tr>
          <td>Some data</td>
          <td>Some more data</td>
        </tr>
      </tbody>
    </table>
    
    <br />
    
    <table class="bottom">
      <caption>
        Caption BELOW the table
      </caption>
      <tbody>
        <tr>
          <td>Some data</td>
          <td>Some more data</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    .top caption {
      caption-side: top;
    }
    
    .bottom caption {
      caption-side: bottom;
    }
    
    table {
      border: 1px solid red;
    }
    
    td {
      border: 1px solid blue;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# propdef-caption-side](https://drafts.csswg.org/css2/#propdef-caption-side) |
| [CSS Logical Properties and Values Module Level 1  <br>\# caption-side](https://drafts.csswg.org/css-logical/#caption-side) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side#see_also)

--------------------------------------------------------------------------------------------------------

*   [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    
*   [CSS table](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Table)
     module
*   [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/caption-side/index.md?plain=1 "Folder: en-us/web/css/reference/properties/caption-side (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaption-side&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaption-side%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaption-side%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaption-side%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")