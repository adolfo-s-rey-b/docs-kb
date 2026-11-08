*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#mdn-search)
    

`mask-composite` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-composite`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property represents a compositing operation used on the current mask layer with the mask layers below it.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    mask-composite: add;
    mask-composite: subtract;
    mask-composite: intersect;
    mask-composite: exclude;
    
    /* Global values */
    mask-composite: inherit;
    mask-composite: initial;
    mask-composite: revert;
    mask-composite: revert-layer;
    mask-composite: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#values)

The property accepts a comma-separated list of `<compositing-operator>` keyword values, each representing a Porter-Duff compositing operator which defines the compositing operation used on the current mask layer with the mask layers below it, including:

[`add`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#add)

The associated mask image is placed over all mask layers below it (with the corresponding compositing operators applied). This is the default value.

[`subtract`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#subtract)

The associated mask image is placed, where it falls outside of all mask layers below it (with the corresponding compositing operators applied).

[`intersect`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#intersect)

The parts of the associated mask image that overlap all composited mask layers below it replace those previously composited layers.

[`exclude`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#exclude)

The non-overlapping regions of the associated mask image and the mask layers below it, with their corresponding compositing operators applied, are combined.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#description)

----------------------------------------------------------------------------------------------------------------

When an element has multiple mask layers applied, the `mask-composite` property can be used to define how the multiple masks interact with each other, or are combined, in creating the final mask effect.

The number of layers is determined by the number of comma-separated values in the `mask-image` property value (even if a value is `none`). Each `mask-composite` value in the comma-separated list of values is matched up with a `mask-image` value, in order. If the number of values in `mask-composite` are equal to or greater than the number of `mask-image` values, the extra values are ignored. If the `mask-composite` property doesn't have enough comma-separated values to match the number of layers, the list of values are repeated until there are enough.

For processing, the _source layer_, which is current or associated mask layer image, is either added to (the default), subtracted from, intersected with, or is excluded from, the destination layers. The _destination layers_ are the mask layers below the source with their corresponding compositing operators applied; this includes all the previous layers, composed in order of appearance within the comma-separated list of masks. All mask layers below the current mask layer must be composited before applying the compositing operation for the current mask layer. Mask layer images are transformed to alpha masks for processing before being combined by the defined compositing value.

The multiple mask layers applied to any element or pseudo-element act as if they are rendered into an isolated group. In other words, the mask layers are composited with other mask layers, not with the element's content or the content behind the element.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `add` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

mask-composite =   
  <compositing-operator>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<compositing-operator> =   
  add        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  subtract   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  intersect  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  exclude      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#examples)

----------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#basic_usage)

This example demonstrates the basic usage of the `mask-composite` property.

#### HTML

We include an HTML [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element, that we will then style.

html

    <div></div>
    

#### CSS

We provide size and color our `<div>`, then add two [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
s, and make their size match that of the element they're masking with the [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
 property. Lastly, we subtract the second mask image from the first mask image with the `mask-composite` property set to `subtract`.

css

    div {
      width: 100px;
      height: 100px;
      background-color: red;
    
      mask-image:
        url("https://mdn.github.io/shared-assets/images/examples/mdn.svg"),
        url("https://mdn.github.io/shared-assets/images/examples/mask-star.svg");
      mask-size: 100% 100%;
    
      mask-composite: subtract;
    }
    

#### Results

### [Value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#value_comparison)

This example demonstrates the `mask-composite` property's four `<compositing-operator>` keyword values, along with comparing the effects of [`alpha` and `luminance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
 mask modes.

#### HTML

We have a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 that contains eight images. The `<table>` has been hidden for brevity.

    <table>
      <tbody>
        <tr>
          <th colspan="4">mask-type: alpha</th>
        </tr>
        <tr>
          <th>mask-composite: add</th>
          <th>mask-composite: subtract</th>
          <th>mask-composite: intersect</th>
          <th>mask-composite: exclude</th>
        </tr>
        <tr class="alphaMaskType">
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
        </tr>
    
        <tr>
          <th colspan="4">
            <code>mask-type: luminance</code>
          </th>
        </tr>
        <tr>
          <th>mask-composite: add</th>
          <th>mask-composite: subtract</th>
          <th>mask-composite: intersect</th>
          <th>mask-composite: exclude</th>
        </tr>
        <tr class="luminanceMaskType">
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
        </tr>
      </tbody>
    </table>
    

html

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    

And an SVG with 4 masks; an alpha heart and circle and a luminance heart and circle. The heart masks are defined using solid colors. The circle masks are created using semi-transparent white and black [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
 and [`fill`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)
 colors.

html

    <svg height="0" width="0">
      <mask id="heartAlpha" class="alpha">
        <path
          d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
          fill="green"
          stroke="white"
          stroke-width="20" />
      </mask>
      <mask id="circleAlpha" class="alpha">
        <circle
          cx="130"
          cy="130"
          r="50"
          fill="rgb(0 0 0 / 0.5)"
          stroke="rgb(255 255 255 / 0.5)"
          stroke-width="20" />
      </mask>
      <mask id="heartLuminance" class="luminance">
        <path
          d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
          fill="green"
          stroke="white"
          stroke-width="20" />
      </mask>
      <mask id="circleLuminance" class="luminance">
        <circle
          cx="130"
          cy="130"
          r="50"
          fill="rgb(0 0 0 / 0.5)"
          stroke="rgb(255 255 255 / 0.5)"
          stroke-width="20" />
      </mask>
    </svg>
    

#### CSS

First we style the `<mask>` elements, providing each mask with a [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
 property value of either `alpha` or `luminance`.

css

    mask.luminance {
      mask-type: luminance;
    }
    
    mask.alpha {
      mask-type: alpha;
    }
    

We then apply the heart and circle masks as the comma-separated [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 property values. These are applied to each [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element, with all the images in a row getting the same masks.

css

    /* apply the mask images */
    tr.alphaMaskType img {
      mask-image: url("#heartAlpha"), url("#circleAlpha");
    }
    
    tr.luminanceMaskType img {
      mask-image: url("#heartLuminance"), url("#circleLuminance");
    }
    

Finally, we compose the masks using the `mask-composite` property, applying the four different enumerated `mask-composite` values by table column.

css

    /* property we're testing */
    td:nth-of-type(1) img {
      mask-composite: add;
    }
    td:nth-of-type(2) img {
      mask-composite: subtract;
    }
    td:nth-of-type(3) img {
      mask-composite: intersect;
    }
    td:nth-of-type(4) img {
      mask-composite: exclude;
    }
    

The table styles have been hidden for the sake of brevity.

    mask {
      height: 50%;
    }
    
    table,
    td,
    th {
      border: 1px solid;
    }
    th {
      font-family: monospace;
    }
    th {
      color: green;
    }
    body > img {
      display: none;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-composite](https://drafts.csswg.org/css-masking/#the-mask-composite) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite#see_also)

----------------------------------------------------------------------------------------------------------

*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
     shorthand
*   [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
    
*   [`mask-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
    
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS `mask` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-composite/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-composite (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-composite&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-composite%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-composite%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-composite%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")