For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md)
.

Here are some common errors and issues with the [Google Sheets node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets)
 and steps to resolve or troubleshoot them.

Append an array[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues#append-an-array)

--------------------------------------------------------------------------------------------------------------------------------

To insert an array of data into Google Sheets, you must convert the array into a valid JSON (key, value) format.

To do so, consider using:

1.  The [Split Out](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout)
     node.
    
2.  The [AI Transform](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aitransform)
     node. For example, try entering something like:
    
    Copy
    
        Convert 'languages' array to JSON (key, value) pairs.
    
3.  The [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)
    .
    

Column names were updated after the node's setup[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues#column-names-were-updated-after-the-nodes-setup)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You'll receive this error if the Google Sheet's column names have changed since you set up the node.

To refresh the column names, re-select **Mapping Column Mode**. This should prompt the node to fetch the column names again.

Once the column names refresh, update the node parameters.

[PreviousSheet Within Document operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations)
[NextGoogle Slides](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides)

Last updated 10 days ago

Was this helpful?