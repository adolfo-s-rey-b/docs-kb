*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#mdn-search)
    

`page-orientation` CSS at-rule descriptor
=========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/126)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`page-orientation`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 descriptor for the [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 at-rule controls the rotation of a printed page. It handles the flow of content across pages when the orientation of a page is changed. This behavior differs from the [`size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size)
 descriptor in that a user can define the direction in which to rotate the page.

This descriptor helps with the layout and orientation of printed documents, especially when documents are printed double-sided. A user can specify how the pages will be rotated when printed. This is particularly useful to lay out content such as tables, which may be wider than the rest of the content, in a different orientation.

**Note:** [Margin boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#margin_at-rules)
 and other positional elements have no special interaction with this descriptor. Margins are laid out as normal in the unrotated page, then rotated along with everything else.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Displays the print content in an upright position */
    @page {
      page-orientation: upright;
    }
    
    /* Displays the print content rotated counter-clockwise */
    @page {
      page-orientation: rotate-left;
    }
    
    /* Displays the print content rotated clockwise */
    @page {
      page-orientation: rotate-right;
    }
    

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#values)

------------------------------------------------------------------------------------------------------------

[`upright`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#upright)

No orientation is applied and the page is laid out and formatted as normal.

[`rotate-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#rotate-left)

After a page is laid out, the page must be displayed rotated a quarter turn to the left (counter-clockwise).

[`rotate-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#rotate-right)

After the page is laid out, the page must be displayed rotated a quarter turn to the right (clockwise).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `upright` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

page-orientation =   
  upright       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rotate-left   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rotate-right    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#examples)

----------------------------------------------------------------------------------------------------------------

### [Rotating printed pages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#rotating_printed_pages)

This example shows how the contents of a print document can be rotated to suit the page content and the page position. In this first part of the CSS code, [named pages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#named_pages)
 are set up to define the direction in which to rotate the content.

css

    @page upright {
      size: portrait;
      page-orientation: upright;
    }
    
    @page left {
      size: landscape;
      page-orientation: rotate-left;
    }
    
    @page right {
      size: landscape;
      page-orientation: rotate-right;
    }
    

    fieldset {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      gap: 1rem;
      width: fit-content;
    }
    p {
      max-width: 60ch;
    }
    @media print {
      fieldset {
        display: none;
      }
      section {
        font-family: "Roboto", sans-serif;
        font-size: 1.5rem;
      }
    }
    

The second part of the CSS code declares a named page rule defined above for the selectors, such as `<section class="left">…</section>`.

css

    @media print {
      .upright {
        page: upright;
      }
      .left {
        page: left;
      }
      .right {
        page: right;
      }
    }
    

    <fieldset id="printStyle">
      <legend>
        Click Print. The page will be laid out in the defined orientation.
      </legend>
      <button id="print">Print</button>
    </fieldset>
    <div id="print-area">
      <section class="upright">
        <h2>Section in Portrait/Upright</h2>
        <p>This section will be printed in portrait and upright with:</p>
        <pre>
    .upright {
      size: portrait;
      page-orientation: upright;
    }
        </pre>
        <p>Paragraph one.</p>
        <p>Paragraph two.</p>
      </section>
      <section class="left">
        <h2>Section in Landscape/Left</h2>
        <p>This section will be printed in landscape and rotated left with:</p>
        <pre>
    .left {
      size: landscape;
      page-orientation: rotate-left;
    }
        </pre>
        <table>
          <thead>
            <tr>
              <th></th>
              <th>100m</th>
              <th>1500m</th>
              <th>Hurdles</th>
              <th>Long Jump</th>
              <th>High Jump</th>
              <th>Javelin</th>
              <th>Discus</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>Dave</th>
              <td>9.65</td>
              <td>3:49</td>
              <td>12.64</td>
              <td>8.54m</td>
              <td>1.95m</td>
              <td>56.65m</td>
              <td>47.63m</td>
            </tr>
            <tr>
              <th>Simon</th>
              <td>9.87</td>
              <td>3:52</td>
              <td>11.89</td>
              <td>8.16m</td>
              <td>1.96m</td>
              <td>59.03m</td>
              <td>45.72m</td>
            </tr>
            <tr>
              <th>Fred</th>
              <td>9.67</td>
              <td>3:52</td>
              <td>12.03</td>
              <td>8.04m</td>
              <td>2.01m</td>
              <td>62.58m</td>
              <td>46.83m</td>
            </tr>
            <tr>
              <th>Gary</th>
              <td>9.77</td>
              <td>3:56</td>
              <td>13.04</td>
              <td>7.96m</td>
              <td>2.02m</td>
              <td>63.87m</td>
              <td>47.73m</td>
            </tr>
            <tr>
              <th>Dick</th>
              <td>9.95</td>
              <td>3:44</td>
              <td>12.99</td>
              <td>5.66m</td>
              <td>1.97m</td>
              <td>56.43m</td>
              <td>43.87m</td>
            </tr>
            <tr>
              <th>Tom</th>
              <td>9.84</td>
              <td>3:48</td>
              <td>12.86</td>
              <td>6.87m</td>
              <td>1.95m</td>
              <td>67.03m</td>
              <td>42.73m</td>
            </tr>
            <tr>
              <th>Harry</th>
              <td>9.91</td>
              <td>3:53</td>
              <td>13.77</td>
              <td>7.34m</td>
              <td>1.94m</td>
              <td>62.84m</td>
              <td>46.72m</td>
            </tr>
          </tbody>
        </table>
      </section>
      <section class="right">
        <h2>Section in Landscape/Right</h2>
        <p>This section will be printed in landscape and rotated right with:</p>
        <pre>
    .right {
      size: landscape;
      page-orientation: rotate-right;
    }
        </pre>
        <table>
          <thead>
            <tr>
              <th></th>
              <th>100m</th>
              <th>1500m</th>
              <th>Hurdles</th>
              <th>Long Jump</th>
              <th>High Jump</th>
              <th>Javelin</th>
              <th>Discus</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>Dave</th>
              <td>9.65</td>
              <td>3:49</td>
              <td>12.64</td>
              <td>8.54m</td>
              <td>1.95m</td>
              <td>56.65m</td>
              <td>47.63m</td>
            </tr>
            <tr>
              <th>Simon</th>
              <td>9.87</td>
              <td>3:52</td>
              <td>11.89</td>
              <td>8.16m</td>
              <td>1.96m</td>
              <td>59.03m</td>
              <td>45.72m</td>
            </tr>
            <tr>
              <th>Fred</th>
              <td>9.67</td>
              <td>3:52</td>
              <td>12.03</td>
              <td>8.04m</td>
              <td>2.01m</td>
              <td>62.58m</td>
              <td>46.83m</td>
            </tr>
            <tr>
              <th>Gary</th>
              <td>9.77</td>
              <td>3:56</td>
              <td>13.04</td>
              <td>7.96m</td>
              <td>2.02m</td>
              <td>63.87m</td>
              <td>47.73m</td>
            </tr>
            <tr>
              <th>Dick</th>
              <td>9.95</td>
              <td>3:44</td>
              <td>12.99</td>
              <td>5.66m</td>
              <td>1.97m</td>
              <td>56.43m</td>
              <td>43.87m</td>
            </tr>
            <tr>
              <th>Tom</th>
              <td>9.84</td>
              <td>3:48</td>
              <td>12.86</td>
              <td>6.87m</td>
              <td>1.95m</td>
              <td>67.03m</td>
              <td>42.73m</td>
            </tr>
            <tr>
              <th>Harry</th>
              <td>9.91</td>
              <td>3:53</td>
              <td>13.77</td>
              <td>7.34m</td>
              <td>1.94m</td>
              <td>62.84m</td>
              <td>46.72m</td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
    

    const printButton = document.querySelector("#print");
    printButton.addEventListener("click", () => {
      window.print();
    });
    

Click the print button to see the page orientation on print.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Paged Media Module Level 3  <br>\# page-orientation-prop](https://drafts.csswg.org/css-page/#page-orientation-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@page/page-orientation/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@page/page-orientation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40page%2Fpage-orientation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40page%2Fpage-orientation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40page%2Fpage-orientation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40page%2Fpage-orientation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")