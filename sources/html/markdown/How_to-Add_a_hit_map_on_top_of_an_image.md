*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image#mdn-search)
    

Add a hitmap on top of an image
===============================

You can create a clickable image map in HTML using [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 and [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
 elements. This article describes how to set up an image map, and some downsides to consider before you build one.

|     |     |
| --- | --- |Here are some things you need to know
| Prerequisites: | You should already know how to [create a basic HTML document](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website)<br> and how to [add accessible images to a webpage.](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_images#how_do_we_put_an_image_on_a_webpage) |
| Objective: | Learn how to make different regions of one image link to different pages. |

**Warning:** This article discusses client-side image maps only. Do not use server-side image maps, which require the user to have a mouse.

[Image maps, and their drawbacks](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image#image_maps_and_their_drawbacks)

------------------------------------------------------------------------------------------------------------------------------------------------------------

When you nest an image inside [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, the entire image links to one webpage. An image map, on the other hand, contains several active regions (called "hotspots") that each link to a different resource.

Formerly, image maps were a popular navigation device, but it's important to thoroughly consider their performance and accessibility ramifications.

**Warning:** Multiple images referencing the same image map may lead to unexpected browser behavior, severely degrading usability and accessibility. For example, when a user keyboard navigates an image with a re-used image map in Safari and Chromium-based browsers, latter image instances using that same image map are skipped entirely. In Firefox, all image maps get keyboard focus simultaneously and when the user keyboard navigates past the image, the next focused element is the one after the last image instance, effectively skipping everything between the two images.

[Text links](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Creating_links)
 (perhaps styled with CSS) are preferable to image maps for several reasons: text links are lightweight, maintainable, often more SEO-friendly, and support accessibility needs (e.g., screen readers, text-only browsers, translation services).

[How to insert an image map, properly](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image#how_to_insert_an_image_map_properly)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Step 1: The image](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image#step_1_the_image)

Not just any image is acceptable.

*   The image must make it clear what happens when people follow image links. `alt` text is mandatory, of course, but many people never see it.
*   The image must clearly indicate where hotspots begin and end.
*   Hotspots must be large enough to tap comfortably, at any viewport size. How large is large enough? [72 × 72 CSS pixels is a good minimum,](https://uxmovement.com/mobile/finger-friendly-design-ideal-mobile-touch-target-sizes/ "External link (opens in new tab)")
     with additional generous gaps between touch targets. The map of the world at [50languages.com](https://www.goethe-verlag.com/book2/ "External link (opens in new tab)")
     (as of time of writing) illustrates the problem perfectly. It's much easier to tap Russia or North America than Albania or Estonia.

You insert your image [much the same way as always](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_images#how_do_we_put_an_image_on_a_webpage)
 (with an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element and [`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#alt)
 text). If the image is only present as a navigation device, you may write `alt=""`, provided you furnish appropriate [`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#alt)
 text in the [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements later on.

You will need a special [`usemap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#usemap)
 attribute. Come up with a unique name, containing no spaces, for your image map. Then assign that name (preceded by a hash) as the value for the `usemap` attribute:

### [Step 2: Activate your hotspots](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image#step_2_activate_your_hotspots)

In this step, put all your code inside a [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
 element. `<map>` only needs one attribute, the same map [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#name)
 as you used in your `usemap` attribute above:

Inside the `<map>` element, we need [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements. An `<area>` element corresponds to a single hotspot. To keep keyboard navigation intuitive, make sure the source order of `<area>` elements corresponds to the visual order of hotspots.

`<area>` elements are [void elements](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)
, but do require four attributes:

[`shape`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#shape)

The `shape` attribute takes one of four values: `circle`, `rect`, `poly`, and `default`. An `<area>` whose `shape` is `default` occupies the entire image, minus any other hotspots you've defined. If there is any overlap between the defined areas, the source order determines which area takes preference. The shape you choose determines the coordinate information you'll need to provide in `coords`.

[`coords`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#coords)

Coordinates are given in CSS pixels, and its value is dependent on the `shape` selected.

*   For a circle, provide the center's x and y coordinates, followed by the length of the radius.
*   For a rectangle, provide the x and y coordinates of the upper-left and bottom-right corners.
*   For a polygon, to provide the x and y coordinates of each corner (so, at least six values).

[`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#href)

The URL of the resource you're linking to. You may leave this attribute blank if you _don't_ want the current area to link anywhere (say, if you're making a hollow circle.)

[`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#alt)

A mandatory attribute, telling people where the link goes or what it does. `alt` text only displays when the image is unavailable. Please refer to our [guidelines for writing accessible link text](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Creating_links#use_clear_link_wording)
.

You may write `alt=""` if the `href` attribute is blank _and_ the entire image already has an `alt` attribute.

### [Step 3: Make sure it works for everybody](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image#step_3_make_sure_it_works_for_everybody)

You aren't done until you test image maps rigorously on many browsers and devices. Try following links with your keyboard alone. Try turning images off.

If your image map is wider than about 240px, you'll need to make further adjustments to make your website responsive. It's not enough to resize the image for small screens, because the coordinates stay the same and no longer match the image.

[Learn more](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image#learn_more)

-------------------------------------------------------------------------------------------------------------------

*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    
*   [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
    
*   [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
    
*   [Online image map editor](https://www.maschek.hu/imagemap/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 9, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_a_hit_map_on_top_of_an_image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/how_to/add_a_hit_map_on_top_of_an_image/index.md?plain=1 "Folder: en-us/web/html/how_to/add_a_hit_map_on_top_of_an_image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FAdd_a_hit_map_on_top_of_an_image&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fhow_to%2Fadd_a_hit_map_on_top_of_an_image%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FAdd_a_hit_map_on_top_of_an_image%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fhow_to%2Fadd_a_hit_map_on_top_of_an_image%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0754cd805a8e010d2e3a2a065f634a3bcf358252%0A*+Document+last+modified%3A+2025-07-09T21%3A49%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")