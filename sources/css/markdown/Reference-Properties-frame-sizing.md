*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#mdn-search)
    

`frame-sizing` CSS property
===========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/914)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#browser_compatibility)
 carefully before using this in production.

The **`frame-sizing`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to set an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 element's horizontal or vertical size to equal the layout size of its embedded document in the same dimension, but only if the embedded document has opted in to sharing its size information.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    frame-sizing: auto;
    frame-sizing: content-width;
    frame-sizing: content-height;
    frame-sizing: content-inline-size;
    frame-sizing: content-block-size;
    
    /* Global values */
    frame-sizing: inherit;
    frame-sizing: initial;
    frame-sizing: revert;
    frame-sizing: revert-layer;
    frame-sizing: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#auto)

The initial value. The `<iframe>` element's size is not affected by the layout size of its embedded document.

[`content-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#content-width)

The `<iframe>` element's [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 is set to the layout width of its embedded document.

[`content-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#content-height)

The `<iframe>` element's [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 is set to the layout height of its embedded document.

[`content-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#content-inline-size)

The `<iframe>` element's [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
 is set to the layout size of its embedded document in the inline direction.

[`content-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#content-block-size)

The `<iframe>` element's [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
 is set to the layout size of its embedded document in the block direction.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#description)

--------------------------------------------------------------------------------------------------------------

For security and privacy reasons, [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 elements do not by default expose any information to the parent document about the size of the content in the document they are embedding.

To enable responsive sizing of [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 elements based on their content, the [`<meta name="responsive-embedded-sizing">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/responsive-embedded-sizing)
 tag can be included in an embedded document to opt it in to sharing its size information with the parent document. The `frame-sizing` property can then be set on the `<iframe>` to cause it to adopt the same horizontal or vertical size as the embedded document's actual content size (termed the **internal layout intrinsic size** in the spec, but abbreviated to "layout size" in our documentation). The document content will then fit seamlessly into the embedding `<iframe>`, avoiding unnecessary scrollbars.

The `frame-sizing` property can take values of `content-width` or `content-height` to cause the `<iframe>` element's `width` or `height` to adopt the embedded document's layout width or layout height, respectively.

There are also logical equivalents available — `frame-sizing` can take values of `content-inline-size` or `content-block-size` to cause the `<iframe>` element's `inline-size` or `block-size` to adopt the embedded document's inline size or block size, respectively. The block or inline direction is determined by the `<iframe>` element's [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, not that of the embedded document's content.

To resize the `<iframe>` dynamically as the embedded document changes layout size, you can call the [`Window.requestResize()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestResize)
 method from the embedded document to make it report an updated size.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | replaced elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#formal_syntax)

------------------------------------------------------------------------------------------------------------------

frame-sizing =   
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  content-width        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  content-height       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  content-block-size   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  content-inline-size    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#examples)

--------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#basic_usage)

This example demonstrates usage of the `frame-sizing` property.

We have two documents, the main `index.html` document, and the embedded `frame.html` document.

#### The main `index.html`

The `index.html` document's HTML contains a heading and an `<iframe>`, into which is embedded the `frame.html` document:

html

    <h1>Responsive iframes — basic example</h1>
    
    <iframe src="frame.html"></iframe>
    

In the `index.html` CSS, we give the `<iframe>` a `frame-sizing` value of `content-block-size`. Because the `<iframe>` has a horizontal `writing-mode`, its `height` will be set to the embedded document's layout height.

css

    iframe {
      frame-sizing: content-block-size;
      border: 2px solid gray;
    }
    

#### The embedded `frame.html`

The `frame.html` document contains a heading and some paragraphs. More significantly, however, it includes the `<meta name="responsive-embedded-sizing" />` tag, which opts it in to sharing its content layout size with the parent document.

html

    <head>
      ...
    
      <meta name="responsive-embedded-sizing" />
    
      ...
    </head>
    <body>
      <h1>This is my frame</h1>
      <p>This is the content of my discontent.</p>
      <p>This is some more content.</p>
    </body>
    

#### Result

Open our [basic responsive `<iframe>` sizing demo](https://mdn.github.io/dom-examples/responsive-iframe-sizing/basic/ "External link (opens in new tab)")
 in a separate tab to see it in action ([see the source code](https://github.com/mdn/dom-examples/tree/main/responsive-iframe-sizing/basic "External link (opens in new tab)")
).

Even though no explicit `height` has been set on the `<iframe>`, it is sized to the right height to exactly contain its embedded document, with no scroll bars.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 4  <br>\# responsive-iframes](https://drafts.csswg.org/css-sizing-4/#responsive-iframes) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing#see_also)

--------------------------------------------------------------------------------------------------------

*   [CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
     module
*   [`<meta name="responsive-embedded-sizing">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/responsive-embedded-sizing)
    
*   [`Window.requestResize()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestResize)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/frame-sizing/index.md?plain=1 "Folder: en-us/web/css/reference/properties/frame-sizing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fframe-sizing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fframe-sizing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fframe-sizing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fframe-sizing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")