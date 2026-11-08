*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#mdn-search)
    

`list-style-image` CSS property
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`list-style-image`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets an image to be used as the list item marker.

It is often more convenient to use the shorthand [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#try_it)

--------------------------------------------------------------------------------------------------------

    list-style-image: url("/shared-assets/images/examples/rocket.svg");
    

    list-style-image: none;
    

    <section class="default-example" id="default-example">
      <div>
        <p>NASA Notable Missions</p>
        <ul class="transition-all unhighlighted" id="example-element">
          <li>Apollo</li>
          <li>Hubble</li>
          <li>Chandra</li>
          <li>Cassini-Huygens</li>
          <li>Spitzer</li>
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
    

**Note:** This property is applied to list items, i.e., elements with ``[`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display) : list-item;`` [by default](https://html.spec.whatwg.org/multipage/rendering.html#lists "External link (opens in new tab)")
 this includes [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements. Because this property is inherited, it can be set on the parent element (normally [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 or [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) to let it apply to all list items.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    list-style-image: none;
    
    /* <url> values */
    list-style-image: url("star-solid.gif");
    
    /* valid image values */
    list-style-image: linear-gradient(to left bottom, red, blue);
    
    /* Global values */
    list-style-image: inherit;
    list-style-image: initial;
    list-style-image: revert;
    list-style-image: revert-layer;
    list-style-image: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#values)

This property is specified as a single value from the following list:

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)

A valid image to use as the marker.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#none)

Specifies that no image is used as the marker. If this value is set, the marker defined in [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 will be used instead. This is the default value for [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | list items |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | The keyword `none` or the computed <image> |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

list-style-image =   
  <image>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none       
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cross-fade()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<gradient>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
        
  
[<image()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  image( <image-tags>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image-src>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 , [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
! )    
  
[<image-set()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
 =   
  image-set( <image-set-option>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<cross-fade()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
 =   
  cross-fade( <cf-image>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<element()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 =   
  element( <id-selector> )    
  
<image-tags> =   
  ltr  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rtl    
  
<image-src> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
<image-set-option> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<resolution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<cf-image> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<id-selector> =   
  <hash-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#examples)

------------------------------------------------------------------------------------------------------------

### [Using a url value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#using_a_url_value)

This example has a star as a marker, which we include using the [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 image function.

#### HTML

html

    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
    

#### CSS

css

    ul {
      list-style-image: url("star-solid.gif");
    }
    

#### Result

### [Using a gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#using_a_gradient)

This example has a [CSS gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
 as a marker, which we create uses the [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
 image function.

#### HTML

html

    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
    

#### CSS

css

    ul {
      font-size: 200%;
      list-style-image: linear-gradient(to left bottom, red, blue);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3  <br>\# image-markers](https://drafts.csswg.org/css-lists/#image-markers) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image#see_also)

------------------------------------------------------------------------------------------------------------

*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
     shorthand
*   [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
     property
*   [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
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

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/list-style-image/index.md?plain=1 "Folder: en-us/web/css/reference/properties/list-style-image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flist-style-image&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flist-style-image%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flist-style-image%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flist-style-image%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")