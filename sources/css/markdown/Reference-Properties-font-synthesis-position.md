*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#mdn-search)
    

`font-synthesis-position` CSS property
======================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/217)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#browser_compatibility)
 carefully before using this in production.

The **`font-synthesis-position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property lets you specify whether or not a browser may synthesize the subscript and superscript "position" typefaces when they are missing in a font family, while using [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
 to set the positions.

The **`font-synthesis-position`** property has no effect when using the [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
 and [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
 elements.

It is often convenient to use the shorthand property [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
 to control all typeface synthesis values.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#syntax)

---------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    font-synthesis-position: auto;
    font-synthesis-position: none;
    
    /* Global values */
    font-synthesis-position: inherit;
    font-synthesis-position: initial;
    font-synthesis-position: revert;
    font-synthesis-position: revert-layer;
    font-synthesis-position: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#auto)

Indicates that a missing position typeface may be synthesized by the browser if needed.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#none)

Indicates that the synthesis of a missing position typeface by the browser is not allowed.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

font-synthesis-position =   
  auto  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#examples)

-------------------------------------------------------------------------------------------------------------------

### [Disabling synthesis of position typeface](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#disabling_synthesis_of_position_typeface)

This example shows turning off synthesis of the superscript and subscript typefaces by the browser in the `Montserrat` font.

#### HTML

html

    <p>
      These are the default position <span class="super">superscript</span>,
      position <span class="sub">subscript</span>, <strong>bold</strong> and
      <em>oblique</em> typefaces.
    </p>
    
    <p class="no-syn">
      The positions <span class="super">superscript</span> and
      <span class="sub">subscript</span> typeface is turned off here but not the
      <strong>bold</strong> and <em>oblique</em> typefaces (on browsers that support
      <code>font-synthesis-position</code>).
    </p>
    

#### CSS

css

    @import "https://fonts.googleapis.com/css2?family=Montserrat&display=swap";
    
    * {
      font-family: "Montserrat", sans-serif;
    }
    .super {
      font-variant-position: super;
    }
    .sub {
      font-variant-position: sub;
    }
    .no-syn {
      font-synthesis-position: none;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-synthesis-position](https://drafts.csswg.org/css-fonts/#font-synthesis-position) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
     shorthand, [`font-synthesis-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style)
    , [`font-synthesis-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    , [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    , [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    , [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-synthesis-position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-synthesis-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-synthesis-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-synthesis-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-synthesis-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-synthesis-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")