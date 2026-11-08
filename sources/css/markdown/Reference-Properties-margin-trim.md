*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#mdn-search)
    

`margin-trim` CSS property
==========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/201)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `margin-trim` property allows the container to trim the margins of its children where they adjoin the container's edges.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#syntax)

---------------------------------------------------------------------------------------------------

css

    margin-trim: none;
    margin-trim: block;
    margin-trim: block-start;
    margin-trim: block-end;
    margin-trim: inline;
    margin-trim: inline-start;
    margin-trim: inline-end;
    
    /* Global values */
    margin-trim: inherit;
    margin-trim: initial;
    margin-trim: revert;
    margin-trim: revert-layer;
    margin-trim: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#none)

Margins are not trimmed by the container.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#block)

Margins provided to the block children where they adjoin the container's edges are trimmed to zero without affecting the margins provided to the container.

[`block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#block-start)

Margin of the first block child with the container's edge is trimmed to zero.

[`block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#block-end)

Margin of last block child with the container's edge is trimmed to zero.

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#inline)

Margins provided to the inline children where they adjoin the container's edges are trimmed to zero, without affecting the spacing at the beginning and end of the row.

[`inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#inline-start)

Margin between the container's edge and the first inline child is trimmed to zero.

[`inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#inline-end)

Margin between the container's edge and the last inline child is trimmed to zero.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | Block containers and multi-column containers. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

margin-trim =   
  none                          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block                         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 block-start [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 block-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#examples)

-------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#basic_usage)

Once support is implemented for this property, it will probably work like so:

When you've got a container with some inline children and you want to put a margin between each child but not have it interfere with the spacing at the end of the row, you might do something like this:

css

    article {
      background-color: red;
      margin: 20px;
      padding: 20px;
      display: inline-block;
    }
    
    article > span {
      background-color: black;
      color: white;
      text-align: center;
      padding: 10px;
      margin-right: 20px;
      margin-left: 30px;
    }
    

The problem here is that you'd end up with 20px too much spacing at the right of the row, so you'd maybe do this to fix it:

css

    span:last-child {
      margin-right: 0;
      margin-left: 0;
    }
    

It is a pain having to write another rule to achieve this, and it is also not very flexible. Instead, `margin-trim` could fix it:

css

    article {
      margin-trim: inline-end;
      /* … */
    }
    

Similarly, to remove left margin with the container's edge:

css

    article {
      margin-trim: inline-start;
      /* … */
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Model Module Level 4  <br>\# margin-trim](https://drafts.csswg.org/css-box-4/#margin-trim) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim#see_also)

-------------------------------------------------------------------------------------------------------

*   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/margin-trim/index.md?plain=1 "Folder: en-us/web/css/reference/properties/margin-trim (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin-trim&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin-trim%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin-trim%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin-trim%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf7ff749b987d530e9a6c07f23ac66f94d968e57%0A*+Document+last+modified%3A+2026-10-07T02%3A00%3A05.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")