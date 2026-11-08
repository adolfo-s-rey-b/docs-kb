*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#mdn-search)
    

`content` CSS property
======================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`content`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property replaces content with a generated value. It can be used to define what is rendered inside an element or pseudo-element. For elements, the `content` property specifies whether the element renders normally (`normal` or `none`) or is replaced with an image (and associated "alt" text). For pseudo-elements and margin boxes, `content` defines the content as images, text, both, or none, which determines whether the element renders at all.

Objects inserted using the `content` property are **anonymous [replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
**.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#try_it)

-----------------------------------------------------------------------------------------------

    .topic-games::before {
      content: "🎮 " / "games";
    }
    
    .topic-weather::before {
      content: "⛅ " / "cloudy";
    }
    
    .topic-hot::before {
      content: url("/shared-assets/images/examples/fire.png") / "On fire";
      margin-right: 6px;
    }
    

    <p class="topic-games">Game News: A new inFamous is not planned</p>
    
    <p class="topic-weather">
      Weather for Today: Heat, violent storms and twisters
    </p>
    
    <p class="topic-hot">Trending Article: Must-watch videos of the week</p>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Keywords that cannot be combined with other values */
    content: normal;
    content: none;
    
    /* <content-replacement>: <image> values */
    content: url("http://www.example.com/test.png");
    content: linear-gradient(#e66465, #9198e5);
    content: image-set("image1x.png" 1x, "image2x.png" 2x);
    
    /* speech output: alternative text after a "/"  */
    content: url("../img/test.png") / "This is the alt text";
    content: counter(chapter) / "Chapter " counter(chapter);
    
    /* <string> value */
    content: "unparsed text";
    
    /* <counter> values, optionally with <list-style-type> */
    content: counter(chapter_counter);
    content: counter(chapter_counter, upper-roman);
    content: counters(section_counter, ".");
    content: counters(section_counter, ".", decimal-leading-zero);
    
    /* attr() value linked to the HTML attribute value */
    content: attr(href);
    
    /* <quote> values */
    content: open-quote;
    content: close-quote;
    content: no-open-quote;
    content: no-close-quote;
    
    /* <content-list>: a list of content values. 
    Several values can be used simultaneously */
    content: "prefix" url("http://www.example.com/test.png");
    content: "prefix" url("/img/test.png") "suffix" / "Alt text";
    content: open-quote counter(chapter_counter);
    
    /* Global values */
    content: inherit;
    content: initial;
    content: revert;
    content: revert-layer;
    content: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#values)

The value can be:

*   One of two keywords: `none` or `normal`. `normal` is the default property value.
*   `<content-replacement>` when replacing a DOM node. `<content-replacement>` is always an `<image>`.
*   A `<content-list>` when replacing pseudo-elements and margin boxes. A `<content-list>` is a list of one or more anonymous inline boxes appearing in the order specified. Each `<content-list>` item is of type [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#string)
    , [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#image)
    , [`<counter>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#counter)
    , [`<quote>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#quote)
    , [`<target>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#target)
    , or [`<leader()>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#leader)
    .
*   An optional alternative text value that can include `<string>`, `<counter>`, or [`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#attrx)
     function values, preceded by a slash (`/`).

The keywords and data types mentioned above are described in more detail below:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#none)

When applied to a pseudo-element, the pseudo-element is not generated. When applied to an element, the value has no effect.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#normal)

For the [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
 pseudo-elements, this value computes to `none` . For other pseudo-elements such as [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
, [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
, or [`::file-selector-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button)
, it produces the element's initial (or normal) content. For regular elements or page margin boxes, it computes to the element's descendants. This is the default value.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)

A sequence of characters enclosed in matching single or double quotes. Multiple string values will be concatenated (there is no concatenation operator in CSS).

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)

An [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
, representing an image to display. This can be equal to a [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
, [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
, or [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
 data type, or a part of the webpage itself, defined by the [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 function.

[`<counter>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#counter)

The `<counter>` value is a [CSS counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
, generally a number produced by computations defined by [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
 and [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 properties. It can be displayed using either the [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 or [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function.

[`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)

The [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 function has two forms: 'counter(_name_)' or 'counter(_name_, style)'. The generated text is the value of the innermost counter of the given name in scope at the given pseudo-element. It is formatted in the specified [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 (`decimal` by default).

[`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)

The [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function also has two forms: 'counters(_name_, _string_)' or 'counters(_name_, _string_, _style_)'. The generated text is the value of all counters with the given name in scope at the given pseudo-element, from outermost to innermost, separated by the specified string. The counters are rendered in the indicated [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 (`decimal` by default).

[`<quote>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#quote)

The `<quote>` data type includes language- and position-dependent keywords:

[`open-quote` and `close-quote`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#open-quote)

These values are replaced by the appropriate string from the [`quotes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes)
 property.

[`no-open-quote` and `no-close-quote`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#no-open-quote)

Introduces no content, but increments (decrements) the level of nesting for quotes.

[`<target>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#target)

The `<target>` data type includes three target functions, `<target-counter()>`, `<target-counters()>`, and `<target-text()>` that create cross-references obtained from the target end of a link. See [Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#formal_syntax)
.

[`<leader()>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#leader)

The `<leader()>` data type includes a leader function: `leader( <leader-type> )`. This function accepts the keyword values `dotted`, `solid`, or `space` (equal to `leader(".")`, `leader("_")`, and `leader(" ")`, respectively), or a `<string>` as a parameter. When supported and used as a value for `content`, the leader-type provided will be inserted as a repeating pattern, visually connecting content across a horizontal line.

[`attr(x)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#attrx)

The `attr(x)` CSS function retrieves the value of an attribute of the selected element, or the pseudo-element's originating element. The value of the element's attribute `x` is an unparsed string representing the attribute name. If there is no attribute `x`, an empty string is returned. The case sensitivity of the attribute name parameter depends on the document language.

[alternative text: `/ <string> | <counter> | attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#alternative_text_string_counter_attr)

Alternative text may be specified for an image or any `<content-list>` items, by appending a forward slash and then a combination of strings, counters, and `attr()` functions. The alternative text is intended for speech output by screen-readers, but may also be displayed in some browsers.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | All elements, tree-abiding pseudo-elements, and page margin boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | On elements, always computes to `normal`. On [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br>, if `normal` is specified, computes to `none`. Otherwise, for URI values, the absolute URI; for `attr()` values, the resulting string; for other keywords, as specified. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#formal_syntax)

-------------------------------------------------------------------------------------------------------------

content =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <content-replacement> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <content-list> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <alt-text> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>                                           
  
<content-replacement> =   
  <image>    
  
<content-list> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <attr()> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 contents [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <quote> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <leader()> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <target> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <string()> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <content()> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <counter> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <symbolic-glyph> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
<alt-text> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <counter> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <attr()> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
[<element()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 =   
  element( <id-selector> )    
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cross-fade()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<gradient>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
        
  
[<attr()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
 =   
  attr( <attr-name> <attr-type>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <declaration-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<quote> =   
  open-quote      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  close-quote     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-open-quote   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-close-quote    
  
<leader()> =   
  leader( <leader-type> )    
  
<target> =   
  <target-counter()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <target-counters()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <target-text()>        
  
[<string()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 =   
  string( [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 first [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 last [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 first-except [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<content()> =   
  content( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 text [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 before [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 after [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 first-letter [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 marker [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<counter>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 =   
  <counter()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <counters()>    
  
<symbolic-glyph> =   
  disc               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  circle             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  square             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  disclosure-open    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  disclosure-closed    
  
<id-selector> =   
  <hash-token>    
  
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
  
<attr-name> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <ident-token>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 '|' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 <ident-token>    
  
<attr-type> =   
  type( <syntax> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  raw-string        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  number            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <attr-unit>         
  
<leader-type> =   
  dotted    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
<target-counter()> =   
  target-counter( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 , <counter-style>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<target-counters()> =   
  target-counters( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 , [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 , <counter-style>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<target-text()> =   
  target-text( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 content [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 before [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 after [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 first-letter [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<counter()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 =   
  counter( <counter-name> , <counter-style>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<counters()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 =   
  counters( <counter-name> , [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 , <counter-style>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
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
    
  
<syntax> =   
  '\*'                                                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <syntax-component> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <syntax-combinator> <syntax-component> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <syntax-string>                                       
  
<attr-unit> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
<counter-style> =   
  <counter-style-name>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <symbols()>             
  
<counter-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
<syntax-component> =   
  <syntax-single-component> <syntax-multiplier>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '<' transform-list '>'                            
  
<syntax-combinator> =   
  '|'    
  
<syntax-string> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
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
  
<syntax-single-component> =   
  '<' <syntax-type-name> '>'  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
                       
  
<syntax-multiplier> =   
  '#'  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '+'    
  
<symbols-type> =   
  cyclic      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  numeric     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alphabetic  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  symbolic    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fixed         
  
<syntax-type-name> =   
  angle               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  custom-ident        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  image               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  integer             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  length              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  length-percentage   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  number              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  percentage          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  resolution          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  string              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  time                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  url                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  transform-function    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#accessibility)

-------------------------------------------------------------------------------------------------------------

CSS-generated content is not included in the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
. Because of this, it will not be represented in the [accessibility tree](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility#accessibility_apis)
 and certain assistive technology/browser combinations will not announce it. If the content conveys information that is critical to understanding the page's purpose, it is better to include it in the main document.

If inserted content is not decorative, check that the information is provided to assistive technologies and is also available when CSS is turned off.

*   [Accessibility support for CSS generated content – Tink](https://tink.uk/accessibility-support-for-css-generated-content/ "External link (opens in new tab)")
     (2015)
*   [WCAG, Guideline 1.3: Create content that can be presented in different ways](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.3_%E2%80%94_create_content_that_can_be_presented_in_different_ways)
    
*   [Understanding Success Criterion 1.3.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/content-structure-separation-programmatic.html "External link (opens in new tab)")
    
*   [Failure of Success Criterion 1.3.1: inserting non-decorative generated content](https://www.w3.org/TR/WCAG20-TECHS/F87 "External link (opens in new tab)")
     Techniques for WCAG 2.0

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#examples)

---------------------------------------------------------------------------------------------------

The first five examples create generated content on pseudo-elements. The last three are [examples of element replacement](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#element_replacement_with_url)
.

### [Appending strings based on an element's class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#appending_strings_based_on_an_elements_class)

This example inserts generated text after the text of elements that have a particular class name. The text is colored red.

#### HTML

html

    <h2>Paperback Best Sellers</h2>
    <ol>
      <li>Political Thriller</li>
      <li class="new-entry">Halloween Stories</li>
      <li>My Biography</li>
      <li class="new-entry">Vampire Romance</li>
    </ol>
    

#### CSS

css

    .new-entry::after {
      content: " New!"; /* The leading space creates separation
                           between the DOM node's content and the generated content
                           being added. */
      color: red;
    }
    

#### Result

### [Quotes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#quotes)

This example inserts differently colored quotation marks around quotes.

#### HTML

html

    <p>
      According to Sir Tim Berners-Lee,
      <q cite="http://www.w3.org/People/Berners-Lee/FAQ.html#Internet">
        I was lucky enough to invent the Web at the time when the Internet already
        existed - and had for a decade and a half.
      </q>
      We must understand that there is nothing fundamentally wrong with building on
      the contributions of others.
    </p>
    <p lang="fr-fr">
      Mais c'est Magritte qui a dit,
      <q lang="fr-fr"> Ceci n'est pas une pipe. </q>.
    </p>
    

#### CSS

css

    q {
      color: blue;
    }
    
    q::before,
    q::after {
      font-size: larger;
      color: red;
      background: #cccccc;
    }
    
    q::before {
      content: open-quote;
    }
    
    q::after {
      content: close-quote;
    }
    

#### Result

Note the [type of quotes generated](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#auto_quotes)
 is based on the language. Browsers add open- and close-quotes before and after [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
 elements by default, so the quotes in this example would appear without them being explicitly set. They could have been turned off by setting the respective `content` property values to `no-open-quote` and `no-close-quote`, or by setting them both to `none`. They can also be turned off by setting the [`quotes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes)
 property to `none` instead.

### [Adding text to list item counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#adding_text_to_list_item_counters)

This example combines a counter sandwiched between two `<string>`s prepended to all list items, creating a more detailed marker for list items ([`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
) within unordered lists ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
).

#### HTML

html

    <ol>
      <li>Dogs</li>
      <li>Cats</li>
      <li>
        Birds
        <ol>
          <li>Owls</li>
          <li>Ducks</li>
          <li>Flightless</li>
        </ol>
      </li>
      <li>Marsupials</li>
    </ol>
    

#### CSS

css

    ol {
      counter-reset: items;
      margin-left: 2em;
    }
    li {
      counter-increment: items;
    }
    li::marker {
      content: "item " counters(items, ".", numeric) ": ";
    }
    

#### Result

The generated content on each list item's marker adds the text "item " as a prefix, including a space to separate the prefix from the counter, which is followed by ": ", a colon and an additional space. The [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function defines a numeric `items` counter, in which the numbers of nested ordered lists have their numbers separated with a period (`.`) in most browsers.

### [Strings with attribute values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#strings_with_attribute_values)

This example is useful for print stylesheets. It uses an [attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
 to select every fully qualified secure link, adding the value of the `href` attribute after the link text as the content of the [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
 pseudo-element.

#### HTML

html

    <ul>
      <li><a href="https://mozilla.com">Mozilla</a></li>
      <li><a href="/">MDN</a></li>
      <li><a href="https://openwebdocs.org">OpenWebDocs</a></li>
    </ul>
    

#### CSS

css

    a[href^="https://"]::after {
      content: " (URL: " attr(href) ")";
      color: darkgreen;
    }
    

#### Result

The generated content is the value of the `href` attribute, prepended by "URL: ", with a space, all in parentheses.

### [Adding an image with alternative text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#adding_an_image_with_alternative_text)

This example inserts an image before all links. Two `content` values are provided. The later `content` value includes an image with alternative text that a screen reader can output as speech.

#### HTML

html

    <a href="https://www.mozilla.org/en-US/">Mozilla Home Page</a>
    

#### CSS

The CSS to show the image and set the alternative text is shown below. This also sets the font and color for the content.

css

    a::before {
      content: url("https://mozorg.cdn.mozilla.net/media/img/favicon.ico") /
        " MOZILLA: ";
    }
    

#### Result

**Note:** The alternative text value is exposed in the browser's accessibility tree. Refer to the [See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#see_also)
 section for browser-specific accessibility panels.

If using a screen reader, it should speak the word "MOZILLA" when it reaches the image. You can select the `::before` pseudo-element with your developer tools selection tool, and view the [accessible name](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name)
 in the accessibility panel.

### [Including counters in alternative text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#including_counters_in_alternative_text)

This example features a list of links to a set of book chapters, and shows how to use generated content to include a book icon and a counter before each one, with alternative text that includes the literal word "Chapter" in place of the icon. This results in the word "chapter" and the chapter number preceding the text in each link's [accessible name](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name)
, which will be announced to screen reader users when the link receives focus.

#### HTML

We include a heading followed by an ordered list of chapter title links using [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
, [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
, and [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements.

html

    <h2>Chapter list</h2>
    <ol>
      <li><a href="#">A stranger calls</a></li>
      <li><a href="#">Two owls</a></li>
      <li><a href="#">Dinner was bland</a></li>
      <li><a href="#">Three owls</a></li>
      <li><a href="#">No-one answered the door</a></li>
      <li><a href="#">The stranger leaves</a></li>
      <li><a href="#">Bedtime</a></li>
    </ol>
    

#### CSS

The CSS includes a [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
 for the `chapter` counter on the `<ol>` element. We also increment the `chapter` counter on each `<li>` element using [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
, and remove the list markers by setting a [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 value of `none`.

css

    ol {
      counter-reset: chapter;
    }
    
    li {
      counter-increment: chapter;
      list-style-type: none;
    }
    

Next, we set the `<a>` elements' [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 pseudo-elements to have generated `content` equal to a book emoji to represent a chapter, plus the current `chapter` counter value, and a space character so that the generated content is separated from the link text. Finally, we set the generated content's alt text to the current `chapter` counter value preceded by the word "Chapter".

css

    a::before {
      content: "📖 " counter(chapter) " " / "Chapter " counter(chapter);
    }
    

#### Result

When a screen reader navigates to a link within the list, supporting browsers will announce "Chapter" followed by the current counter number, followed by the link text, for example, "Chapter 1 A stranger calls" and "Chapter 2 Two owls".

### [Element replacement with URL](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#element_replacement_with_url)

This example replaces a regular element! The element's contents are replaced with an SVG using the [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 type.

Pseudo-elements aren't rendered on replaced elements. As this element is replaced, any matching `::after` or `::before` are not generated or applied. To demonstrate this, we include an `::after` declaration block, attempting to add the `id` as generated content. This pseudo-element will not be generated as the element is replaced.

#### HTML

html

    <div id="replaced">This content is replaced!</div>
    

#### CSS

css

    #replaced {
      content: url("mdn.svg");
    }
    
    /* will not show if element replacement is supported */
    div::after {
      content: " (" attr(id) ")";
    }
    

#### Result

When generating content on regular elements (rather than just on pseudo-elements), the entire element is replaced. This means that `::before` and `::after` pseudo-elements are not generated.

### [Element replacement with `<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#element_replacement_with_gradient)

This example demonstrates how an element's contents can be replaced by any type of `<image>`, in this case, a CSS gradient. The element's contents are replaced with a [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
. We provide alt text because all images should be described for accessibility.

#### HTML

html

    <div id="replaced">I disappear</div>
    

#### CSS

css

    div {
      border: 1px solid;
      background-color: #cccccc;
      min-height: 100px;
      min-width: 100px;
    }
    
    #replaced {
      content: repeating-linear-gradient(blue 0, orange 10%) /
        "Gradients and alt text are supported";
    }
    

#### Result

Check the [browser compatibility chart](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#browser_compatibility)
. All browsers support gradients and all browsers support replacing elements with images, but not all browsers support gradients as a `content` value.

### [Element replacement with `image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#element_replacement_with_image-set)

This example replaces an element's content with an [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
. If the users display has normal resolution the `1x.png` will be displayed. Screens with a higher resolution will display the `2x.png` image.

#### HTML

html

    <div id="replaced">I disappear!</div>
    

#### CSS

    div {
      width: 100px;
      border: 1px solid lightgrey;
    }
    

css

    #replaced {
      content: image-set(
        "1x.png" 1x,
        "2x.png" 2x
      ) / "DPI";
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Generated Content Module Level 3  <br>\# propdef-content](https://drafts.csswg.org/css-content/#propdef-content) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#see_also)

---------------------------------------------------------------------------------------------------

*   [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
    
*   [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
    
*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
    
*   [`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)
    
*   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    
*   [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
    
*   [`quotes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes)
    
*   [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    
*   [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
    
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    
*   [Replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
    
*   [CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
     module
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   Browser accessibility panels: [Firefox Accessibility inspector](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/ "External link (opens in new tab)")
    , [Chrome Accessibility pane](https://developer.chrome.com/docs/devtools/accessibility/reference#pane "External link (opens in new tab)")
    , and [Safari Accessibility tree](https://university.webflow.com/glossary/accessibility-tree#:~:text=To%20view%20a%20website%E2%80%99s%20accessibility%20tree%20in%20Safari "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/content/index.md?plain=1 "Folder: en-us/web/css/reference/properties/content (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc655f38c10ba17b853b0e66b43cf4cf2b176e424%0A*+Document+last+modified%3A+2026-08-04T23%3A29%3A57.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")