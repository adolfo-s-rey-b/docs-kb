For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date.md)
.

`_Date_`.`**toDateTime()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date#datetodatetime)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts a JavaScript Date to a Luxon DateTime. The DateTime contains the same information, but is easier to manipulate.

**Syntax:** `_Date_`.toDateTime()

**Returns:** DateTime

**Source:** Custom n8n functionality

**Examples:**

Copy

    // date = new Date("2024-03-30T18:49")
    date.toDateTime().plus(5, 'days') //=> 2024-04-04T18:49

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date#related-resources)

-------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousCustomdata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata)
[NextDatetime](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime)

Last updated 10 days ago

Was this helpful?