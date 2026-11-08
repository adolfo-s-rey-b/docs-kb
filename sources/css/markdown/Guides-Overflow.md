*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#mdn-search)
    

CSS overflow
============

The **CSS overflow** module properties enable you to handle scrollable overflow in visual media.

Overflow happens when the content in an element box extends past one or more of the box's edges. **Scrollable overflow** is the content that appears outside the element box for which you might want to add a scrolling mechanism. CSS overflow properties let you control what happens when content overflows an element box, including creating carousels without JavaScript.

Painting effects that overflow the content but do not participate in the CSS box model do not affect layout. This type of overflow is also known as [ink overflow](https://developer.mozilla.org/en-US/docs/Glossary/Ink_overflow)
. Examples of ink overflows include box shadows, border images, text decoration, overhanging glyphs, and outlines. Ink overflows do not extend the scrollable overflow region.

[Overflow in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#overflow_in_action)

----------------------------------------------------------------------------------------------------------

Try the following example to see the effects of various `overflow` property values on the content overflow and scrollbars in the adjacent fixed-size box.

The example includes options to change the values for the `overflow-clip-margin` and `width` properties, as well as to programmatically scroll the content if the overflow property creates a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. Select `overflow: clip` and see the effect of different `overflow-clip-margin` values. Select `overflow: hidden` or `overflow: scroll` to check out the various `ScrollLeft` and `ScrollTop` slider settings.

    <article>
      <fieldset>
        <legend>Select options:</legend>
        <label
          ><code>overflow</code>:
          <select id="overflowValue">
            <option>hidden</option>
            <option>clip</option>
            <option>scroll</option>
            <option>auto</option>
            <option selected>visible</option>
            <option>overlay</option>
          </select>
        </label>
        <label>
          <code>overflow-clip-margin</code>:
          <input type="number" id="ocm" value="1" min="0" max="10" />
          <code>em</code>
        </label>
        <label
          ><input type="checkbox" id="wide" /> <code>width</code>:
          <code>20em</code> or <code>40em</code></label
        >
        <fieldset>
          <legend>Scroll programmatically:</legend>
          <label
            >ScrollLeft:
            <input type="range" min="0" max="100" value="0" id="scrollL"
          /></label>
          <label
            >ScrollTop:
            <input type="range" min="0" max="100" value="0" id="scrollT"
          /></label>
        </fieldset>
      </fieldset>
      <pre class="visible">&nbsp;
        Oh, Rubber Duckie, you're the one
        You make bath time lots of fun
        Rubber Duckie, I'm awfully fond of you
    
        Rubber Duckie, joy of joys
        When I squeeze you, you make noise
        Rubber Duckie, you're my very best friend, it's true
    
        Oh, every day when I make my way to the tubby
        I find a little fella who's cute and yellow and chubby
        Rub-a-dub-dubby
    
        <a href="#">Rubber Duckie</a>, you're so fine
        And I'm lucky that you're mine
        Rubber Duckie, I'm awfully fond of you
          </pre>
    </article>
    

    article {
      display: flex;
      gap: 1em;
    }
    
    label {
      display: block;
      white-space: nowrap;
    }
    
    pre {
      border: 2px dashed crimson;
      height: 150px;
      width: 20em;
      margin-bottom: 3em;
      overflow-clip-margin: 1em;
      text-align: center;
    }
    
    .wide {
      width: 40em;
    }
    
    ::before {
      font-weight: bold;
      color: white;
      background: crimson;
      display: inline-block;
      min-width: 50%;
      padding: 3px 5px;
      box-sizing: border-box;
    }
    
    .hidden {
      overflow: hidden;
    }
    .hidden::before {
      content: "hidden: ";
    }
    
    .clip {
      overflow: clip;
    }
    .clip::before {
      content: "clip: ";
    }
    
    .scroll {
      overflow: scroll;
    }
    .scroll::before {
      content: "scroll: ";
    }
    
    .auto {
      overflow: auto;
    }
    .auto::before {
      content: "auto: ";
    }
    
    .overlay {
      overflow: clip;
      overflow: overlay;
    }
    .overlay::before {
      content: "overlay (or clip if not supported): ";
    }
    
    .visible {
      overflow: visible;
    }
    .visible::before {
      content: "visible: ";
    }
    
    article:not(:has(pre.clip)) > fieldset > label:nth-of-type(2),
    article:not(:has(pre.hidden, pre.scroll, pre.auto, pre.overlay))
      fieldset
      fieldset {
      opacity: 20%;
      pointer-events: none;
    }
    

    const pre = document.querySelector("pre");
    const val = document.getElementById("overflowValue");
    const check = document.getElementById("wide");
    const ocm = document.getElementById("ocm");
    const scrollL = document.getElementById("scrollL");
    const scrollT = document.getElementById("scrollT");
    
    val.addEventListener("change", () => {
      if (pre.classList.contains("wide")) {
        pre.className = `wide ${val.value}`;
      } else {
        pre.className = `${val.value}`;
      }
      scrollExample();
      clipMargin();
    });
    
    check.addEventListener("change", () => {
      pre.classList.toggle("wide");
      scrollExample();
    });
    
    ocm.addEventListener("change", () => {
      clipMargin();
    });
    
    scrollL.addEventListener("change", () => {
      scrollExample();
    });
    scrollT.addEventListener("change", () => {
      scrollExample();
    });
    
    function scrollExample() {
      pre.scrollTo({
        top: scrollT.value,
        left: scrollL.value * 2,
        behavior: "smooth",
      });
    }
    
    function clipMargin() {
      pre.style.overflowClipMargin = `${ocm.value}em`;
    }
    

A link is included in the content box above to demonstrate the effects of keyboard focus on overflow and scroll behaviors. Try tabbing to the link or programmatically scrolling the content: the content will scroll only if the enumerated `<overflow>` value creates a scroll container.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#reference)

----------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#properties)

*   [`line-clamp`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp)
    
*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
     shorthand
*   [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
    
*   [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
    
*   [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
    
*   [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
    
*   [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
    
*   [`scroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-behavior)
    
*   [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
    
*   [`scroll-target-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group)
    
*   [`scrollbar-gutter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter)
    
*   [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
    

The CSS overflow level 4 module also introduces the `block-ellipsis`, `continue`, `max-lines`, `overflow-clip-margin-block`, `overflow-clip-margin-block-end`, `overflow-clip-margin-block-start`, `overflow-clip-margin-bottom`, `overflow-clip-margin-inline`, `overflow-clip-margin-inline-end`, `overflow-clip-margin-inline-start`, `overflow-clip-margin-left`, `overflow-clip-margin-right`, and `overflow-clip-margin-top` properties. Currently, no browsers support these features.

### [Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#selectors)

*   [`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)
    
*   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    
*   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
    
*   [`:target-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after)
    
*   [`:target-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-before)
    
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#data_types)

*   [`<overflow>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value)
     enumerated values

### [Glossary terms and definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#glossary_terms_and_definitions)

*   [Scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
    
*   [Scrollport](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container#scrollport)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#guides)

----------------------------------------------------------------------------------

[Learn: Overflowing content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Overflow)

Learn what overflow is and how to manage it.

[Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)

Create pure-CSS carousel UI features using scroll buttons, scroll markers, and generated columns.

[Creating a named scroll progress timeline animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#creating_a_named_scroll_progress_timeline_animation)

The CSS scroll timeline [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
 and [`scroll-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
 properties, along with the [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
 shorthand, create animations tied to the scroll offset of a scroll container.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#related_concepts)

------------------------------------------------------------------------------------------------------

*   [`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
    
*   [`scrollbar-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
     CSS property
*   [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
     CSS property
*   [`scrollbar-gutter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter)
     CSS property
*   [`scroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-behavior)
     CSS property
*   [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
     CSS shorthand property
*   [`scroll-padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
     CSS shorthand property
*   [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
     CSS property
*   [`scroll-snap-stop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
     CSS property
*   [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
     CSS property
*   [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
     CSS property
*   [`::-webkit-scrollbar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar)
     pseudo-element
*   [`scrollbar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/scrollbar_role)
     ARIA role
*   Element [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scroll "scroll()")
     method
*   Element [`scrollBy()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollBy "scrollBy()")
     method
*   Element [`scrollIntoView()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView "scrollIntoView()")
     method
*   Element [`scrollTo()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTo "scrollTo()")
     method
*   Element [`scrollTop`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop "scrollTop")
     property
*   Element [`scrollLeft`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollLeft "scrollLeft")
     property
*   Element [`scrollWidth`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollWidth "scrollWidth")
     property
*   Element [`scrollHeight`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight "scrollHeight")
     property
*   Document [`scroll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event "scroll")
     event
*   [Scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
     glossary term
*   [Ink overflow](https://developer.mozilla.org/en-US/docs/Glossary/Ink_overflow)
     glossary term

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#specifications)

--------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3](https://drafts.csswg.org/css-overflow/) |
| [CSS Overflow Module Level 4](https://drafts.csswg.org/css-overflow-4/) |
| [CSS Overflow Module Level 5](https://drafts.csswg.org/css-overflow-5/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow#see_also)

--------------------------------------------------------------------------------------

*   [CSS scrollbars styling](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scrollbars_styling)
     module
*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [CSSOM view](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view)
     module
*   How to [debug scrollable overflow](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/debug_scrollable_overflow/index.html "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/overflow/index.md?plain=1 "Folder: en-us/web/css/guides/overflow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FOverflow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Foverflow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FOverflow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Foverflow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1474534461893381d54c502e655f334b5568e597%0A*+Document+last+modified%3A+2026-08-21T19%3A37%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")