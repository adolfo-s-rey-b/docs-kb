*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#mdn-search)
    

`list-style` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`list-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property allows you to set all the list style properties at once.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#try_it)

--------------------------------------------------------------------------------------------------

    list-style: square;
    

    list-style: inside;
    

    list-style: url("/shared-assets/images/examples/rocket.svg");
    

    list-style: none;
    

    list-style: georgian inside url("/shared-assets/images/examples/rocket.svg");
    

    list-style: georgian outside url("/non-existent.svg");
    

    <section class="default-example" id="default-example">
      <div>
        <p>NASA Notable Missions</p>
        <ul class="transition-all" id="example-element">
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
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    
*   [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    
*   [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#syntax)

--------------------------------------------------------------------------------------------------

css

    /* type */
    list-style: square;
    
    /* image */
    list-style: url("../img/shape.png");
    
    /* position */
    list-style: inside;
    
    /* two values */
    list-style: georgian outside;
    list-style: url("img/pip.svg") inside;
    
    /* three values */
    list-style: lower-roman url("img/shape.png") outside;
    
    /* Keyword value */
    list-style: none;
    
    /* Global values */
    list-style: inherit;
    list-style: initial;
    list-style: revert;
    list-style: revert-layer;
    list-style: unset;
    

The `list-style` property is specified as one, two, or three values in any order. If [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 and [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
 are both set, the `list-style-type` is used as a fallback if the image is unavailable.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#values)

[`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)

A `<counter-style>`, [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
, or `none`. If omitted in the shorthand, it defaults to `disc`. See [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
.

[`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)

An [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 or `none`. If omitted, it defaults to `none`. See [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
.

[`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)

Either `inside` or `outside`. If omitted, it defaults to `outside`. See [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#none)

No list style is used.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#description)

------------------------------------------------------------------------------------------------------------

The `list-style` property lets you customize the appearance of list items. The values of this property are applied to list items, including [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements and elements with ``[`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display) : list-item;``.

### [List style inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#list_style_inheritance)

Because the [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 longhand property is inherited, `list-style` can be set on a parent element (normally [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 or [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) to make the same list styling apply to its list items. However, user-agent stylesheets set `list-style-type` on `<ul>`, `<ol>`, and [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
 elements, so nested lists use these default values instead of inheriting the ancestor list's `list-style`. The [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
 and [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
 values normally inherit into nested lists. To make nested lists inherit the marker type as well, set `list-style` or `list-style-type` to `inherit` on the nested list elements.

For example, in cases like this:

html

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>
        Three
        <ul>
          <li>Four</li>
          <li>Five</li>
          <li>Six</li>
        </ul>
      </li>
    </ul>
    

Where a custom style is set on the outer list:

css

    body > ul {
      list-style: square;
    }
    

The inner list won't inherit the custom style unless you set it to inherit:

css

    ul ul {
      list-style: inherit;
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#accessibility)

----------------------------------------------------------------------------------------------------------------

Safari does not recognize ordered or unordered lists as lists in the accessibility tree if they have a `list-style` value of `none`, unless the list is nested within the [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
 navigation element. This [behavior is intentional](https://webkit.org/b/170179#c1 "External link (opens in new tab)")
 and is not considered a bug.

To ensure lists are announced as lists, include [`role="list"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/list_role)
 to [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 and [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 elements, especially if the list is not nested in a `<nav>`. This restores list semantics without affecting the design:

html

    <ul role="list">
      <li>An item</li>
      <li>Another item</li>
    </ul>
    

If an ARIA `role` is not an option for your code, CSS can be used instead. Adding non-empty [pseudo-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 such as text or images before each list item can restore list semantics, but impacts the visual appearance. Safari determines if the added pseudo-content suffices as accessible content, restoring list semantics if so. Generally, Safari considers text and images as sufficient, which is why the `content: "+ ";` shown below works (but requires additional styling to not affect the design).

css

    ul {
      list-style: none;
    }
    
    ul li::before {
      content: "+ ";
    }
    

A declaration of `content: "";` (an empty string) is ignored, as are `content` values that contain only spaces, such as `content: " ";`.

These CSS workarounds should only be used when an HTML solution is unavailable, and only after testing to ensure that they don't result in unexpected behaviors that may negatively impact user experience.

*   ['Fixing' Lists](https://www.scottohara.me/blog/2019/01/12/lists-and-safari.html "External link (opens in new tab)")
     (2023)
*   [VoiceOver and list-style-type: none](https://gerardkcohen.me/writing/2017/voiceover-list-style-type.html "External link (opens in new tab)")
     (2017)
*   [Understanding WCAG: Create content that can be presented in different ways](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.3_%E2%80%94_create_content_that_can_be_presented_in_different_ways)
    
*   [Understanding success criterion 1.3.1: Info and relationships | WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)<br>    : `disc`<br>*   [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)<br>    : `outside`<br>*   [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)<br>    : `none` |
| Applies to | list items |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)<br>    : The keyword `none` or the computed <image><br>*   [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)<br>    : as specified<br>*   [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)<br>    : discrete<br>*   [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)<br>    : discrete<br>*   [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)<br>    : discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#formal_syntax)

----------------------------------------------------------------------------------------------------------------

list-style =   
  [<'list-style-position'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'list-style-image'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
     [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'list-style-type'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
        
  
[<list-style-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
 =   
  inside   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outside    
  
[<list-style-image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
 =   
  <image>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none       
  
[<list-style-type>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 =   
  <counter-style>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
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
        
  
<counter-style> =   
  <counter-style-name>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <symbols()>             
  
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
  
<counter-style-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
[<symbols()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
 =   
  symbols( <symbols-type>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <image> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
 )    
  
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
  
<symbols-type> =   
  cyclic      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  numeric     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alphabetic  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  symbolic    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fixed         

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#examples)

------------------------------------------------------------------------------------------------------

### [Setting list style type and position](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#setting_list_style_type_and_position)

#### HTML

html

    List 1
    <ul class="one">
      <li>List Item1</li>
      <li>List Item2</li>
      <li>List Item3</li>
    </ul>
    List 2
    <ul class="two">
      <li>List Item A</li>
      <li>List Item B</li>
      <li>List Item C</li>
    </ul>
    

#### CSS

css

    .one {
      list-style: circle;
    }
    
    .two {
      list-style: square inside;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3  <br>\# list-style-property](https://drafts.csswg.org/css-lists/#list-style-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#see_also)

------------------------------------------------------------------------------------------------------

*   Component properties: [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
    , [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    , and [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    
*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
     pseudo-element
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/list-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/list-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flist-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flist-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flist-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flist-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc2375c58cf5a6f0fd7053f3cee7cba8bd88a2bbe%0A*+Document+last+modified%3A+2026-09-10T07%3A32%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")