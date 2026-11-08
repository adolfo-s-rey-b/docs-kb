*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#mdn-search)
    

`list-style-position` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`list-style-position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the position of the [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
 relative to a list item.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#try_it)

-----------------------------------------------------------------------------------------------------------

    list-style-position: inside;
    

    list-style-position: outside;
    

    <section class="default-example" id="default-example">
      <div>
        <p>NASA Notable Missions</p>
        <ul class="transition-all" id="example-element">
          <li>Apollo 11: First Human Landing</li>
          <li>City in Space: The International Space Station</li>
          <li>Great Observatory: The Hubble Space Telescope</li>
          <li>Everlasting Mars Rovers</li>
        </ul>
      </div>
    </section>
    

    .default-example {
      font-size: 1.2rem;
    }
    
    #example-element {
      width: 100%;
      background: #be094b;
      color: white;
    }
    
    section {
      text-align: left;
      flex-direction: column;
    }
    
    hr {
      width: 50%;
      color: lightgray;
      margin: 0.5em;
    }
    
    .note {
      font-size: 0.8rem;
    }
    
    .note a {
      color: #009e5f;
    }
    
    @counter-style space-counter {
      symbols: "\1F680" "\1F6F8" "\1F6F0" "\1F52D";
      suffix: " ";
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    list-style-position: inside;
    list-style-position: outside;
    
    /* Global values */
    list-style-position: inherit;
    list-style-position: initial;
    list-style-position: revert;
    list-style-position: revert-layer;
    list-style-position: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#values)

This property is specified as one of the following keyword values:

[`inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#inside)

The [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
 is the first element among the list item's contents.

[`outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#outside)

The [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
 is outside the principal block box. This is the default value for [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#description)

---------------------------------------------------------------------------------------------------------------------

This property is applied to list items, i.e., elements with ``[`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display) : list-item;``. [By default](https://html.spec.whatwg.org/multipage/rendering.html#lists "External link (opens in new tab)")
 this includes [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements. Because this property is inherited, it can be set on the parent element (normally [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 or [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) to let it apply to all list items.

If a block element is the first child of a list element declared as `list-style-position: inside`, then the block element is placed on the line after the marker-box.

It is often more convenient to use the shorthand [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `outside` |
| Applies to | list items |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

list-style-position =   
  inside   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outside    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#examples)

---------------------------------------------------------------------------------------------------------------

### [Setting list item position](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#setting_list_item_position)

#### HTML

html

    <p>List 1</p>
    <ul class="inside">
      <li>List Item 1-1</li>
      <li>List Item 1-2</li>
      <li>List Item 1-3</li>
      <li>List Item 1-4</li>
    </ul>
    <p>List 2</p>
    <ul class="outside">
      <li>List Item 2-1</li>
      <li>List Item 2-2</li>
      <li>List Item 2-3</li>
      <li>List Item 2-4</li>
    </ul>
    <p>List 3</p>
    <ul class="inside-img">
      <li>List Item 3-1</li>
      <li>List Item 3-2</li>
      <li>List Item 3-3</li>
      <li>List Item 3-4</li>
    </ul>
    

#### CSS

css

    .inside {
      list-style-position: inside;
      list-style-type: square;
    }
    
    .outside {
      list-style-position: outside;
      list-style-type: circle;
    }
    
    .inside-img {
      list-style-position: inside;
      list-style-image: url("star-solid.gif");
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3  <br>\# list-style-position-property](https://drafts.csswg.org/css-lists/#list-style-position-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
     shorthand
*   [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
     property
*   [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
     property
*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
     pseudo-element
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/list-style-position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/list-style-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flist-style-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flist-style-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flist-style-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flist-style-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")