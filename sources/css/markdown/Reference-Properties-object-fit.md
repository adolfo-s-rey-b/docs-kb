*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#mdn-search)
    

`object-fit` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`object-fit`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how the content of a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, such as an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
, should be resized to fit its container.

**Note:** The `object-fit` property has no effect on [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
, [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
, and [`<fencedframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe)
 elements.

You can alter the alignment of the replaced element's content object within the element's box using the [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
 property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#try_it)

--------------------------------------------------------------------------------------------------

    object-fit: fill;
    

    object-fit: contain;
    

    object-fit: cover;
    

    object-fit: none;
    

    object-fit: scale-down;
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/plumeria-146x200.jpg" />
    </section>
    

    #example-element {
      height: 100%;
      width: 100%;
      border: 2px dotted #888888;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#syntax)

--------------------------------------------------------------------------------------------------

css

    object-fit: contain;
    object-fit: cover;
    object-fit: fill;
    object-fit: none;
    object-fit: scale-down;
    
    /* Global values */
    object-fit: inherit;
    object-fit: initial;
    object-fit: revert;
    object-fit: revert-layer;
    object-fit: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#values)

This property is specified as one of the following keyword values:

[`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#contain)

The replaced content is scaled to maintain its [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 while fitting within the element's content box. The entire object is made to fill the box, while preserving its aspect ratio, so the object will be ["letterboxed"](https://en.wikipedia.org/wiki/Letterboxing_(filming) "External link (opens in new tab)")
 or ["pillarboxed"](https://en.wikipedia.org/wiki/Pillarbox "External link (opens in new tab)")
 if its aspect ratio does not match the aspect ratio of the box.

[`cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#cover)

The replaced content is sized to maintain its aspect ratio while filling the element's entire content box. If the object's aspect ratio does not match the aspect ratio of its box, then the object will be clipped to fit.

[`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#fill)

The replaced content is sized to fill the element's content box. This is the [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
 value. The entire object will completely fill the box. If the object's [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 does not match the aspect ratio of its box, then the object will be stretched to fit.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#none)

The replaced content is not resized.

[`scale-down`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#scale-down)

The content is sized as if `none` or `contain` were specified, whichever would result in a smaller concrete object size.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `fill` |
| Applies to | replaced elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#formal_syntax)

----------------------------------------------------------------------------------------------------------------

object-fit =   
  fill                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 contain [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 cover [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 scale-down    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#examples)

------------------------------------------------------------------------------------------------------

### [Setting object-fit for an image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#setting_object-fit_for_an_image)

#### HTML

html

    <section>
      <h2>object-fit: fill</h2>
      <img class="fill" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <img class="fill narrow" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <h2>object-fit: contain</h2>
      <img class="contain" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <img class="contain narrow" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <h2>object-fit: cover</h2>
      <img class="cover" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <img class="cover narrow" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <h2>object-fit: none</h2>
      <img class="none" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <img class="none narrow" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <h2>object-fit: scale-down</h2>
      <img class="scale-down" src="mdn_logo_only_color.png" alt="MDN Logo" />
    
      <img class="scale-down narrow" src="mdn_logo_only_color.png" alt="MDN Logo" />
    </section>
    

#### CSS

css

    h2 {
      font-family: "Courier New", monospace;
      font-size: 1em;
      margin: 1em 0 0.3em;
    }
    
    img {
      width: 150px;
      height: 100px;
      border: 1px solid black;
      margin: 10px 0;
    }
    
    .narrow {
      width: 100px;
      height: 150px;
    }
    
    .fill {
      object-fit: fill;
    }
    
    .contain {
      object-fit: contain;
    }
    
    .cover {
      object-fit: cover;
    }
    
    .none {
      object-fit: none;
    }
    
    .scale-down {
      object-fit: scale-down;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 3  <br>\# the-object-fit](https://drafts.csswg.org/css-images/#the-object-fit) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit#see_also)

------------------------------------------------------------------------------------------------------

*   Other image-related CSS properties: [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
    , [`image-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation)
    , [`image-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering)
    , [`image-resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution)
    .
*   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/object-fit/index.md?plain=1 "Folder: en-us/web/css/reference/properties/object-fit (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fobject-fit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fobject-fit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fobject-fit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fobject-fit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")