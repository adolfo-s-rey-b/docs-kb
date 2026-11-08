*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#mdn-search)
    

`resize` CSS property
=====================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/17)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`resize`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether an element is resizable, and if so, in which directions.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#try_it)

----------------------------------------------------------------------------------------------

    resize: both;
    

    resize: horizontal;
    

    resize: vertical;
    

    resize: none;
    

    <section class="default-example" id="default-example">
      <div id="example-element">Try resizing this element.</div>
    </section>
    

    #example-element {
      background: linear-gradient(135deg, cyan 0%, cyan 94%, white 95%);
      border: 3px solid #c5c5c5;
      overflow: auto;
      width: 250px;
      height: 250px;
      font-weight: bold;
      color: black;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 10px;
    }
    

`resize` does not apply to the following:

*   Inline elements
*   Block elements for which the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
     property is set to `visible` or `clip`

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#syntax)

----------------------------------------------------------------------------------------------

css

    /* Keyword values */
    resize: none;
    resize: both;
    resize: horizontal;
    resize: vertical;
    resize: block;
    resize: inline;
    
    /* Global values */
    resize: inherit;
    resize: initial;
    resize: revert;
    resize: revert-layer;
    resize: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#none)

The element offers no user-controllable method for resizing it.

[`both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#both)

The element displays a mechanism for allowing the user to resize it, which may be resized both horizontally and vertically.

[`horizontal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#horizontal)

The element displays a mechanism for allowing the user to resize it in the _horizontal_ direction.

[`vertical`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#vertical)

The element displays a mechanism for allowing the user to resize it in the _vertical_ direction.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#block)

The element displays a mechanism for allowing the user to resize it in the _block_ direction (either horizontally or vertically, depending on the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 and [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 value).

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#inline)

The element displays a mechanism for allowing the user to resize it in the _inline_ direction (either horizontally or vertically, depending on the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 and [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 value).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | elements with [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)<br> other than `visible`, and optionally replaced elements representing images or videos, and iframes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#formal_syntax)

------------------------------------------------------------------------------------------------------------

resize =   
  none        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  both        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  horizontal  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  vertical    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline        

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#examples)

--------------------------------------------------------------------------------------------------

### [Disabling resizability of text areas](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#disabling_resizability_of_text_areas)

In many browsers, [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements are resizable by default. You may override this behavior with the `resize` property.

#### HTML

html

    <textarea>Type some text here.</textarea>
    

#### CSS

css

    textarea {
      resize: none; /* Disables resizability */
    }
    

#### Result

### [Using resize with arbitrary elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#using_resize_with_arbitrary_elements)

You can use the `resize` property to make any element resizable. In the example below, a resizable [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 contains a resizable paragraph ([`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element).

#### HTML

html

    <div class="resizable">
      <p class="resizable">
        This paragraph is resizable in all directions, because the CSS `resize`
        property is set to `both` on this element.
      </p>
    </div>
    

#### CSS

css

    .resizable {
      resize: both;
      overflow: scroll;
      border: 1px solid black;
    }
    
    div {
      height: 300px;
      width: 300px;
    }
    
    p {
      height: 200px;
      width: 200px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# resize](https://drafts.csswg.org/css-ui/#resize) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize#see_also)

--------------------------------------------------------------------------------------------------

*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/resize/index.md?plain=1 "Folder: en-us/web/css/reference/properties/resize (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fresize&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fresize%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fresize%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fresize%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")