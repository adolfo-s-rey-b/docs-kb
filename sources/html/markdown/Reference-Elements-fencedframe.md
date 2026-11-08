*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#mdn-search)
    

`<fencedframe>` HTML fenced frame element
=========================================

Deprecated

To be removed

This feature is pending removal from browsers. Using it now may lead to broken functionality in future updates. Following the announcement that Chrome will maintain its current approach to third-party cookies, Chrome decided to withdraw certain Privacy Sandbox features including the `<fencedframe>` element and related APIs.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<fencedframe>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a nested [browsing context](https://developer.mozilla.org/en-US/docs/Glossary/Browsing_context)
, embedding another HTML page into the current one. `<fencedframe>`s are very similar to [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 elements in form and function, except that:

*   Communication is restricted between the `<fencedframe>` content and its embedding site.
*   A `<fencedframe>` can access cross-site data, but only in a very specific set of controlled circumstances that preserve user privacy.
*   A `<fencedframe>` cannot be manipulated or have its data accessed via regular scripting (for example reading or setting the source URL). `<fencedframe>` content can only be embedded via [specific APIs](https://developer.mozilla.org/en-US/docs/Web/API/Fenced_frame_API#use_cases)
    .
*   A `<fencedframe>` cannot access the embedding context's DOM, nor can the embedding context access the `<fencedframe>`'s DOM.

The `<fencedframe>` element is a type of `<iframe>` with more native privacy features built in. It addresses shortcomings of `<iframe>`s such as reliance on third-party cookies and other privacy risks. See [Fenced frame API](https://developer.mozilla.org/en-US/docs/Web/API/Fenced_frame_API)
 for more details.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#attributes)

----------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`allow`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#allow)

Specifies a [Permissions Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Permissions_Policy)
 for the `<fencedframe>`, which defines what features are available to the `<fencedframe>` based on the origin of the request. See [Permissions policies available to fenced frames](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#permissions_policies_available_to_fenced_frames)
 for more details of which features can be controlled via a policy set on a fenced frame.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#height)

A unitless integer representing the height of the fenced frame in CSS pixels. The default is `150`.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#width)

A unitless integer representing the width of the fenced frame in CSS pixels. The default is `300`.

[Permissions policies available to fenced frames](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#permissions_policies_available_to_fenced_frames)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Permissions delegated from the top-level context to a fenced frame for allowing and denying features could be used as a communication channel, so constitute a privacy threat. As a result, standard web features that can have their availability controlled via [Permissions Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy)
 (for example, [`camera`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/camera)
 or [`geolocation`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/geolocation)
) are **not available** within fenced frames.

The only features that can be enabled by a policy inside fenced frames are the specific features designed to be used inside fenced frames:

*   [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience "External link (opens in new tab)")
    *   `attribution-reporting`
    *   `private-aggregation`
    *   `shared-storage`
    *   `shared-storage-select-url`
*   [Shared Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Shared_Storage_API)
    *   `attribution-reporting`
    *   `private-aggregation`
    *   `shared-storage`
    *   `shared-storage-select-url`

Currently these are always enabled inside fenced frames. In the future, which ones are enabled will be controllable using the `<fencedframe>` `allow` attribute. Blocking privacy sandbox features in this manner will also block the fenced frame from loading — there will be no communication channel at all.

[Focusing across fenced frame boundaries](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#focusing_across_fenced_frame_boundaries)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

The ability of the document's active focus to be moved across fenced frame boundaries (i.e., from an element outside the fenced frame to one inside, or vice versa) is limited. User-initiated actions such as a click or a tab can do so, as there is no fingerprinting risk there.

However, trying to traverse the boundary via an API call such as [`HTMLElement.focus()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus)
 is prohibited — a malicious script could use a series of such calls to leak inferred information across the boundary.

[Positioning and scaling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#positioning_and_scaling)

------------------------------------------------------------------------------------------------------------------------------------

Being a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, the `<fencedframe>` allows the position of the embedded document within its box to be adjusted using the [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
 property.

**Note:** The [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 property has no effect on `<fencedframe>` elements.

The size of the embedded content may be set by internal `contentWidth` and `contentHeight` properties of the `<fencedframe>`'s [`config`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFencedFrameElement/config "config")
 object. In such cases, changing the `width` or `height` of the `<fencedframe>` will change the size of the embedded container on the page, but the document inside the container will be visually scaled to fit. The reported width and height of the embedded document (i.e., [`Window.innerWidth`](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth)
 and [`Window.innerHeight`](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerHeight)
) will be unchanged.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#accessibility)

----------------------------------------------------------------------------------------------------------------

People navigating with assistive technology, such as a screen reader, can use the [`title` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 on a `<fencedframe>` to label its content. The title's value should concisely describe the embedded content:

Without this title, they have to navigate into the `<fencedframe>` to determine what its embedded content is. This context shift can be confusing and time-consuming, especially for pages with multiple `<fencedframe>`s and/or if embeds contain interactive content like video or audio.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#examples)

------------------------------------------------------------------------------------------------------

To set what content will be shown in a `<fencedframe>`, a utilizing API (such as [Protected Audience](https://privacysandbox.google.com/private-advertising/protected-audience "External link (opens in new tab)")
 or [Shared Storage](https://privacysandbox.google.com/private-advertising/shared-storage "External link (opens in new tab)")
) generates a [`FencedFrameConfig`](https://developer.mozilla.org/en-US/docs/Web/API/FencedFrameConfig)
 object, which is then set as the value of the `<fencedframe>`'s `config` property.

The following example gets a `FencedFrameConfig` from a Protected Audience API's ad auction, which is then used to display the winning ad in a `<fencedframe>`:

**Note:** `resolveToConfig: true` must be passed in to the `runAdAuction()` call to obtain a `FencedFrameConfig` object. If it is not set, the resulting [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 will resolve to a URN that can only be used in an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#technical_summary)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, embedded content, interactive content, palpable content. |
| Permitted content | None. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts embedded content. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | [`application`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role)<br>, [`document`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/document_role)<br>, [`img`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/img_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role) |
| DOM interface | [`HTMLFencedFrameElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFencedFrameElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Fenced Frame  <br>\# the-fencedframe-element](https://wicg.github.io/fenced-frame/#the-fencedframe-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe#see_also)

------------------------------------------------------------------------------------------------------

*   [Fenced Frame API](https://developer.mozilla.org/en-US/docs/Web/API/Fenced_frame_API)
    
*   [Fenced frames](https://privacysandbox.google.com/private-advertising/fenced-frame "External link (opens in new tab)")
     on privacysandbox.google.com
*   [The Privacy Sandbox](https://privacysandbox.google.com/ "External link (opens in new tab)")
     on privacysandbox.google.com

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/fencedframe/index.md?plain=1 "Folder: en-us/web/html/reference/elements/fencedframe (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ffencedframe&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ffencedframe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ffencedframe%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ffencedframe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe316526e520d8163e9151dca8973eb777b5285e0%0A*+Document+last+modified%3A+2026-08-27T06%3A55%3A42.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")