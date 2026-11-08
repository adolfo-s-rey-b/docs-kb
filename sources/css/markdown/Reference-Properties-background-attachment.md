*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#mdn-search)
    

`background-attachment` CSS property
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/498)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-attachment`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether a background image's position is fixed within the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
, or scrolls with its containing block.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#try_it)

-------------------------------------------------------------------------------------------------------------

    background-attachment: scroll;
    

    background-attachment: fixed;
    

    background-attachment: local;
    

    background-attachment: fixed, scroll;
    

    background-attachment: scroll, fixed;
    

    <section id="default-example">
      <div id="example-element">
        <p>
          From there to here<br />
          from here to there,<br />
          Funny things<br />
          Are everywhere.
        </p>
        <p>--Dr. Seuss</p>
      </div>
    </section>
    

    body {
      overflow: scroll;
    }
    
    #default-example {
      height: 600px;
    }
    
    #example-element {
      max-width: 20rem;
      height: 100%;
      background:
        url("/shared-assets/images/examples/lizard.png") right 3rem top 1rem / 15rem
          no-repeat,
        url("/shared-assets/images/examples/moon.jpg") center / 10rem;
      font-size: 1.2rem;
      font-weight: bolder;
      overflow: auto;
      padding: 20px;
      color: red;
      text-shadow:
        0 0 0.5rem black,
        0 0 0.5rem black;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    background-attachment: scroll;
    background-attachment: fixed;
    background-attachment: local;
    
    /* Global values */
    background-attachment: inherit;
    background-attachment: initial;
    background-attachment: revert;
    background-attachment: revert-layer;
    background-attachment: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#values)

This property is specified as one or more comma-separated keyword values:

[`fixed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#fixed)

The background is fixed relative to the viewport. Even if an element has a scrolling mechanism, the background doesn't move with the element. If set, the [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
 property is ignored.

[`local`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#local)

The background is fixed relative to the element's contents. If the element has a scrolling mechanism, the background scrolls with the element's contents, and the background painting area and background positioning area are relative to the scrollable area of the element rather than to the border framing them.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#scroll)

The background is fixed relative to the element itself and does not scroll with its contents. (It is effectively attached to the element's border.)

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `scroll` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

background-attachment =   
  <attachment>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<attachment> =   
  scroll  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fixed   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  local     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#examples)

-----------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#basic_example)

#### HTML

We include an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) with some list items ([`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
).

html

    <ul>
      <li>One fish</li>
      <li>Two fish</li>
      <li>Red fish</li>
      <li>Blue fish</li>
      <li>Black fish</li>
      <li>Blue fish</li>
      <li>Old fish</li>
      <li>New fish.</li>
      <li>This one has a little star.</li>
      <li>This one has a little car.</li>
      <li>Say! What a lot</li>
      <li>Of fish there are.</li>
    </ul>
    

#### CSS

We define a [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 and set the `background-attachment` to `fixed`. We also include a [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, and [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 to ensure the element scrolls.

css

    ul {
      background-image: url("star-solid.gif");
      background-attachment: fixed;
    
      width: 300px;
      height: 70px;
      overflow: scroll;
    }
    

#### Result

Note how the background remains fixed relative to the list's viewport when you scroll the overflowing text into view.

### [Multiple background images](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#multiple_background_images)

This property supports multiple background images. You can specify a different `<attachment>` for each background, separated by commas. Each image is matched with the corresponding `<attachment>` type, from first specified to last.

#### HTML

We include all of Dr. Seuss's poem.

html

    <div>
      <ul>
        <li>One fish</li>
        <li>Two fish</li>
        <li>Red fish</li>
        <li>Blue fish</li>
        <li>Black fish</li>
        <li>Blue fish</li>
        <li>Old fish</li>
        <li>New fish.</li>
        <li>This one has a little star.</li>
        <li>This one has a little car.</li>
        <li>Say! What a lot</li>
        <li>Of fish there are.</li>
        <li>Yes. Some are red. And some are blue.</li>
        <li>Some are old. And some are new.</li>
        <li>Some are sad.</li>
        <li>And some are glad.</li>
        <li>And some are very, very bad.</li>
        <li>Why are they</li>
        <li>Sad and glad and bad?</li>
        <li>I do not know.</li>
        <li>Go ask your dad.</li>
        <li>Some are thin.</li>
        <li>And some are fat.</li>
        <li>The fat one has</li>
        <li>A yellow hat.</li>
        <li>From there to here, from here to there,</li>
        <li>Funny things</li>
        <li>Are everywhere.</li>
      </ul>
      <p>--Dr. Seuss</p>
    </div>
    

#### CSS

We include a [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, and [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 on the parent [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 to ensure the contents scroll.

We define two comma-separated background images on the list, and set the `background-attachment` to `fixed, scroll`, meaning the first background image will be `fixed` and the second will `scroll`. We set the [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 to make both background images repeat vertically, separating them with the [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 property.

css

    div {
      width: 300px;
      height: 200px;
      overflow: scroll;
    }
    ul {
      background-image: url("star-solid.gif"), url("star-transparent.gif");
      background-attachment: fixed, scroll;
      background-repeat: repeat-y;
      background-position:
        0 0,
        100px 0;
    }
    

#### Result

Note how the first background image is fixed to the viewport while the second background image is fixed relative to the list.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# background-attachment](https://drafts.csswg.org/css-backgrounds/#background-attachment) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment#see_also)

-----------------------------------------------------------------------------------------------------------------

*   The other [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
     CSS properties:
    *   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
        
    *   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
        
    *   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
        
    *   [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
        
    *   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
        
    *   [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
        
    *   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
        
*   [Using multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-attachment/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-attachment (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-attachment&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-attachment%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-attachment%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-attachment%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")