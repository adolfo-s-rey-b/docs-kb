*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Replaced_element_properties#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Replaced_element_properties#mdn-search)
    

Styling replaced elements
=========================

Some [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 properties apply to all elements, some only to grid and flex containers, others only to transformable elements. This guide introduces the properties that only apply to _replaced elements_.

A **[replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
** is an element whose representation is outside the scope of CSS; they're external objects whose representation is independent of the CSS formatting model. Some replaced elements, such as [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 elements, may have stylesheets of their own, but they don't inherit the styles of the parent document.

[Using CSS with replaced elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Replaced_element_properties#using_css_with_replaced_elements)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

CSS handles replaced elements specifically in some cases, like when calculating margins and some `auto` values. Only replaced elements can ever have [intrinsic dimensions](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
. Some replaced elements, but not all, have intrinsic dimensions or a defined baseline, which is used by some CSS properties, such as [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
.

While document styles can set the size and position of replaced elements, document styles don't affect the replaced elements' content, with some exceptions: The [CSS images module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
 includes properties which support controlling the positioning of the element's content within its box.

[Controlling object position within the content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Replaced_element_properties#controlling_object_position_within_the_content_box)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The CSS images module defines two properties which can be used to specify how the object contained within the replaced element should be positioned within the element's box area. The `object-fit` property is used to size objects, while the `object-position` property is used to position them.

### [The `object-fit` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Replaced_element_properties#the_object-fit_property)

The `object-fit` property specifies how the replaced element's content object should be fitted to the containing element's box. The property defines how images, videos and other embeddable media formats respond to the height and width of the replaced element's content box. If the height, width, or aspect-ratio of an element differ from the resource that will be occupying space reserved for the element, the `fill`, `contain`, `cover`, `scale-down`, and `none` values define whether the browser should scale the resource, cover the allocated space, contain the asset within the space, or allow the resource to be distorted.

When contained or scaled down, any areas of the box not covered by the replaced element will show the element's background.

The `object-fit` property has no effect on [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
, [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
, and [`<fencedframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe)
 elements.

![A square photo of the progressive pride flag flying near a chimney.](https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg)

If we place the image, a square with a 1:1 aspect ratio, in a 100px x 300px box (1:3 aspect ratio), by default the image will fill the box, distorting itself. We can use the `object-fit` property to define how the image should be rendered when forced into a box with a different size and aspect ratio:

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <p>
      <label><input type="checkbox" /> Change dimensions</label>
    </p>
    

    body {
      display: flex;
      gap: 20px;
      flex-flow: row wrap;
      grid-auto-flow: column;
      max-width: 98%;
      margin: 10px auto 0;
    }
    img {
      width: 100px;
      height: 300px;
      outline: 2px solid purple;
    }
    body:has(:checked) img {
      width: 300px;
      height: 100px;
    }
    

css

    img:nth-of-type(1) {
      object-fit: fill;
    }
    img:nth-of-type(2) {
      object-fit: cover;
    }
    img:nth-of-type(3) {
      object-fit: contain;
    }
    img:nth-of-type(4) {
      object-fit: scale-down;
    }
    img:nth-of-type(5) {
      object-fit: none;
    }
    img:nth-of-type(6) {
      /* no object-fit property */
      outline: 2px dashed red;
    }
    

Check the box to set the height and width values. Note that only the `fill` value (the default) distorts the original image. With all other values, the intrinsic aspect ratio of the image is maintained.

### [The `object-position` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Replaced_element_properties#the_object-position_property)

The `object-position` property specifies the alignment of the replaced element's content object within the element's box.

Often used in conjunction with the [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 property, it takes as its value a [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
 value, the same value type as used for [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
.

css

    img {
      object-position: bottom right;
    }
    

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    

It can be used without `object-fit`. In this case, the image is rendered at it's intrinsic size (218px x 218px), with the position of the contents of the image set by the `object-position` value.

    img {
      margin: 10px 0 0 10px;
    }
    

css

    img {
      outline: 2px solid;
      object-position: 114px 72px;
    }
    

The `object-position` property works equally well with `<iframe>`, `<video>`, and `<embed>` elements as it does for `<img>`.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Replaced_element_properties#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    
*   [CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
     module
*   [CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
     module
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Replaced_element_properties/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/images/replaced_element_properties/index.md?plain=1 "Folder: en-us/web/css/guides/images/replaced_element_properties (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FImages%2FReplaced_element_properties&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fimages%2Freplaced_element_properties%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FImages%2FReplaced_element_properties%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fimages%2Freplaced_element_properties%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fba3c8980510073ee92674aa71cb2c8c5b71294ab%0A*+Document+last+modified%3A+2026-08-27T09%3A13%3A05.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")