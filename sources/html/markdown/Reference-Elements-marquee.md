*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#mdn-search)
    

`<marquee>` HTML marquee element
================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<marquee>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to insert a scrolling area of text. You can control what happens when the text reaches the edges of its content area using its attributes.

The HTML `<marquee>` element is deprecated and its use is strongly discouraged. If you must create the effect of scrolling text or continuous elements, consider using [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 with [CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
 instead of `<marquee>` elements to smoothly animate content. Additionally, include the [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
 CSS [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 query to stop the animation based on user preference, thereby improving user experience and accessibility.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#attributes)

------------------------------------------------------------------------------------------------------

[`behavior`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#behavior)

Sets how the text is scrolled within the marquee. Possible values are `scroll`, `slide` and `alternate`. If no value is specified, the default value is `scroll`.

[`bgcolor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#bgcolor)

Sets the background color through color name or hexadecimal value.

[`direction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#direction)

Sets the direction of the scrolling within the marquee. Possible values are `left`, `right`, `up` and `down`. If no value is specified, the default value is `left`.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#height)

Sets the height in pixels or percentage value.

[`hspace`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#hspace)

Sets the horizontal margin

[`loop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#loop)

Sets the number of times the marquee will scroll. If no value is specified, the default value is −1, which means the marquee will scroll continuously.

[`scrollamount`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#scrollamount)

Sets the amount of scrolling at each interval in pixels. The default value is 6.

[`scrolldelay`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#scrolldelay)

Sets the interval between each scroll movement in milliseconds. The default value is 85. Note that any value smaller than 60 is ignored and the value 60 is used instead unless `truespeed` is specified.

[`truespeed`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#truespeed)

By default, `scrolldelay` values lower than 60 are ignored. If `truespeed` is present, those values are not ignored.

[`vspace`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#vspace)

Sets the vertical margin in pixels or percentage value.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#width)

Sets the width in pixels or percentage value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#examples)

--------------------------------------------------------------------------------------------------

html

    <marquee>This text will scroll from right to left</marquee>
    
    <marquee direction="up">This text will scroll from bottom to top</marquee>
    
    <marquee
      direction="down"
      width="250"
      height="200"
      behavior="alternate"
      class="outlined">
      <marquee behavior="alternate">This text will bounce</marquee>
    </marquee>
    

css

    .outlined {
      border: solid;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#technical_summary)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| DOM interface | [`HTMLMarqueeElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMarqueeElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-marquee-element-2](https://html.spec.whatwg.org/multipage/rendering.html#the-marquee-element-2) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee#see_also)

--------------------------------------------------------------------------------------------------

*   CSS [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
     property
*   CSS [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
     property
*   [CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [`HTMLMarqueeElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMarqueeElement)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/marquee/index.md?plain=1 "Folder: en-us/web/html/reference/elements/marquee (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmarquee&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmarquee%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmarquee%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmarquee%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")