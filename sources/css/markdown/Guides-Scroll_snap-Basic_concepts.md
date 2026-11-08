*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#mdn-search)
    

Basic concepts of scroll snap
=============================

The properties in the [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
 module enable you to define how scrolling snaps to specific points as a user scrolls through a document.

The [scroll snap](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap)
 feature lets you define the snap positions where a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
's scrollport may end or "snap to" after a scrolling operation has completed.

[Key properties for CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#key_properties_for_css_scroll_snap)

------------------------------------------------------------------------------------------------------------------------------------------------------------

Before you can define scroll snapping, you need to enable scrolling on a scroll container. You can do this by ensuring that the scroll container has a defined size and that it has [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 enabled.

You can then define scroll snapping on the scroll container by using the following two key properties:

*   [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
    : Using this property, you can define whether or not the scrollable viewport can be snapped to, whether snapping is required or optional, and the axis on which the snapping should occur.
*   [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
    : This property is set on every child of the scroll container and you can use it to define each child's snap position or lack thereof.
*   [`scroll-snap-stop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
    : This property ensures that a child is snapped to during scrolling and not passed over.
*   [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
    : This property can be set on child elements that are snapped to during scrolling to create an outset from the defined box.
*   [`scroll-padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
    : This property can be set on the scroll container to create a snapping offset.

The example below demonstrates scroll snapping along the vertical axis, which is defined by `scroll-snap-type`. Additionally, `scroll-snap-align` applies on all the children of the `<section>` element, dictating the point where the scrolling of each child should stop.

html

    <article class="scroller">
      <section>
        <h2>Section one</h2>
      </section>
      <section>
        <h2>Section two</h2>
      </section>
      <section>
        <h2>Section three</h2>
      </section>
    </article>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .scroller {
      border: 4px solid #333333;
      width: 300px;
    }
    
    .scroller section {
      min-height: 100%;
      padding: 10px;
    }
    
    .scroller section:nth-child(odd) {
      background-color: #cccccc;
    }
    

css

    .scroller {
      height: 300px;
      overflow-y: scroll;
      scroll-snap-type: y mandatory;
    }
    
    .scroller section {
      scroll-snap-align: start;
    }
    

[Using scroll-snap-type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#using_scroll-snap-type)

------------------------------------------------------------------------------------------------------------------------------------

The [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 property needs to know the axis along which scroll snapping happens. This can be `x`, `y`, or the logical mappings `block` or `inline`. You can also use the keyword `both` to have scroll snapping work along both axes.

You can also pass in the keywords `mandatory` or `proximity`. The `mandatory` keyword tells the browser whether the content _has_ to snap to a certain point, no matter where the scroll is. The `proximity` keyword means that the content may snap to the point, but does not have to.

Using `mandatory` creates a very consistent scrolling experience — you know the browser will always snap to each defined point. This means that you can be confident that something you expect to be at the top of the screen will be there when scrolling finishes. However, it can cause problems if the content is larger than you expect — users may find themselves in the frustrating position of never being able to scroll and view a certain point in the content. Therefore, the use of `mandatory` should be carefully considered and only used in situations where you know how much content is on the screen or scrollable section at any time.

**Note:** Never use `mandatory` if the content inside one of your child elements will overflow the parent container because user will not be able to scroll the overflowing content into view.

The `proximity` value only snaps child elements to a position when it is close by, with the browsers determining the exact distance. Click "Play" to edit the example below in the MDN Playground. Alternate the `scroll-snap-type` value between `mandatory` and `proximity` to see the effect this has on the scroll experience.

html

    <article class="scroller">
      <section>
        <h2>Section one</h2>
        <p>
          Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
          kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus
          winter purslane kale. Celery potato scallion desert raisin horseradish
          spinach carrot soko.
        </p>
      </section>
      <section>
        <h2>Section two</h2>
        <p>
          Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
          kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus
          winter purslane kale. Celery potato scallion desert raisin horseradish
          spinach carrot soko.
        </p>
      </section>
      <section>
        <h2>Section three</h2>
        <p>
          Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
          kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus
          winter purslane kale. Celery potato scallion desert raisin horseradish
          spinach carrot soko.
        </p>
      </section>
    </article>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .scroller {
      border: 4px solid #333333;
      width: 300px;
    }
    
    .scroller section {
      min-height: 100%;
      padding: 10px;
    }
    
    .scroller section:nth-child(odd) {
      background-color: #cccccc;
    }
    

css

    .scroller {
      height: 300px;
      overflow-y: scroll;
      scroll-snap-type: y mandatory;
    }
    
    .scroller section {
      scroll-snap-align: start;
    }
    

In the above example, both [`height: 300px;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 and [`overflow-y: scroll;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
 are set on the scroll container. If the content doesn't overflow its container, there is nothing to scroll.

[Using scroll-snap-align](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#using_scroll-snap-align)

--------------------------------------------------------------------------------------------------------------------------------------

The valid values for the [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
 property include `start`, `end`, `center`, and `none`. These values are used to indicate the point in the scroll container to which the content should snap. Click "Play" in the example below and change the value of `scroll-snap-align` to see how this changes the scroll behavior.

    <article class="scroller">
      <section>
        <h2>Section one</h2>
        <p>
          Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
          kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus
          winter purslane kale. Celery potato scallion desert raisin horseradish
          spinach carrot soko.
        </p>
      </section>
      <section>
        <h2>Section two</h2>
        <p>
          Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
          kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus
          winter purslane kale. Celery potato scallion desert raisin horseradish
          spinach carrot soko.
        </p>
      </section>
      <section>
        <h2>Section three</h2>
        <p>
          Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
          kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus
          winter purslane kale. Celery potato scallion desert raisin horseradish
          spinach carrot soko.
        </p>
      </section>
    </article>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .scroller {
      border: 4px solid #333333;
      width: 300px;
    }
    
    .scroller section {
      min-height: 100%;
      padding: 10px;
    }
    
    .scroller section:nth-child(odd) {
      background-color: #cccccc;
    }
    

css

    .scroller {
      height: 200px;
      overflow-y: scroll;
      scroll-snap-type: y mandatory;
    }
    
    .scroller section {
      scroll-snap-align: start;
    }
    

If `scroll-snap-type` is `mandatory` and `scroll-snap-align` on a child is either set to `none` or not set (in which case, it defaults to `none`), the user will be unable to scroll that element into view.

[Using scroll-padding](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#using_scroll-padding)

--------------------------------------------------------------------------------------------------------------------------------

When using `start` or `end`, if you do not want the content to snap right to the edge of the scroll container, or if you want the snap position to be slightly offset from center when using `center`, use the [`scroll-padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
 property or its equivalent longhand values to add some padding.

In the example below, `scroll-padding` is set to `50px`. When the content snaps to the start of the second and third sections, scrolling stops 50 pixels away from the start of the section. Try changing the `scroll-padding` value to see how this changes the distance.

html

    <article class="scroller">
      <section>
        <h2>Section one</h2>
      </section>
      <section>
        <h2>Section two</h2>
      </section>
      <section>
        <h2>Section three</h2>
      </section>
    </article>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .scroller {
      border: 4px solid #333333;
      width: 300px;
    }
    
    .scroller section {
      min-height: 100%;
      padding: 10px;
    }
    
    .scroller section:nth-child(odd) {
      background-color: #cccccc;
    }
    

css

    .scroller {
      height: 300px;
      overflow-y: scroll;
      scroll-snap-type: y mandatory;
      scroll-padding: 50px;
    }
    
    .scroller section {
      scroll-snap-align: start;
    }
    

This is potentially useful if you have a [fixed](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#fixed_positioning)
 element such as a navigation bar, which could end up overlapping scrolled content. By using `scroll-padding`, you can reserve space for the fixed element, as shown in the example below, where the `<h1>` element remains on screen as the content scrolls beneath it. Without padding, the heading would overlap some of the content when snapping happens.

    <article class="scroller">
      <h1>Sticky Heading</h1>
      <section>
        <h2>Section one</h2>
      </section>
      <section>
        <h2>Section two</h2>
      </section>
      <section>
        <h2>Section three</h2>
      </section>
    </article>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .scroller {
      border: 4px solid #333333;
      width: 300px;
    }
    
    .scroller section {
      min-height: 100%;
      padding: 10px;
    }
    
    .scroller section:nth-child(odd) {
      background-color: #cccccc;
    }
    

css

    .scroller h1 {
      position: sticky;
      top: 0;
      min-height: 40px;
      background-color: black;
      color: white;
      margin: 0;
      padding: 0;
    }
    
    .scroller h2 {
      margin: 0;
      padding: 0;
    }
    
    .scroller {
      height: 300px;
      overflow-y: scroll;
      scroll-snap-type: y mandatory;
      scroll-padding: 50px;
    }
    
    .scroller section {
      scroll-snap-align: start;
    }
    

[Using scroll-margin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#using_scroll-margin)

------------------------------------------------------------------------------------------------------------------------------

The [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
 property or the longhand scroll margin values can be set on child elements, defining an outset from the defined box. This allows for different amounts of space for different child elements and can be used in conjunction with `scroll-padding` on the parent.

    <article class="scroller">
      <section>
        <h2>Section one</h2>
      </section>
      <section>
        <h2>Section two</h2>
      </section>
      <section>
        <h2>Section three</h2>
      </section>
    </article>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .scroller {
      border: 4px solid #333333;
      width: 300px;
    }
    
    .scroller section {
      min-height: 100%;
      padding: 10px;
    }
    
    .scroller section:nth-child(odd) {
      background-color: #cccccc;
    }
    

css

    .scroller {
      height: 300px;
      overflow-y: scroll;
      scroll-snap-type: y mandatory;
    }
    
    .scroller section {
      scroll-snap-align: start;
      scroll-margin: 40px;
    }
    

[Using scroll-snap-stop](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#using_scroll-snap-stop)

------------------------------------------------------------------------------------------------------------------------------------

Using the [`scroll-snap-stop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
 property, you can specify whether the scrolling must snap to the defined snap points. In the above examples, this would mean that the scrolling would stop at the start of each section or be able to skip past sections.

With this property definition, you can ensure that users see each section of the scroller and don't accidentally scroll past them. However, this setting can also negatively affect user experience by preventing the user from quickly scrolling to their desired content.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts#see_also)

--------------------------------------------------------------------------------------------------------

*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Practical CSS scroll snapping](https://css-tricks.com/practical-css-scroll-snapping/ "External link (opens in new tab)")
     on CSS-Tricks (2020)
*   [CSS scroll snap](https://12daysofweb.dev/2022/css-scroll-snap/ "External link (opens in new tab)")
     on 12 Days of Web (2019)
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)
*   [Scroll snap examples](https://codepen.io/collection/KpqBGW "External link (opens in new tab)")
     on CodePen

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/scroll_snap/basic_concepts/index.md?plain=1 "Folder: en-us/web/css/guides/scroll_snap/basic_concepts (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll_snap%2FBasic_concepts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fscroll_snap%2Fbasic_concepts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll_snap%2FBasic_concepts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fscroll_snap%2Fbasic_concepts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa14f56b06eabf3b182ae4bc0e02634a8ccc01f20%0A*+Document+last+modified%3A+2026-02-26T23%3A33%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")