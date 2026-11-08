For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md)
.

A common pattern in n8n workflows is to receive a file, either from an [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 (for files you are fetching from a website), a [Webhook Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook)
 (for files which are sent to your workflow from elsewhere), or from a local source. Data obtained in this way is often in a binary format, for example a spreadsheet or PDF.

The Extract From File node extracts data from a binary format file and converts it to JSON, which can then be easily manipulated by the rest of your workflow. For converting JSON back into a binary file type, please see the [Convert to File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile)
 node.

Operations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile#operations)

------------------------------------------------------------------------------------------------------------

Use the **Operations** drop-down to select the format of the source file to extract data from.

*   **Extract From CSV**: The "Comma Separated Values" file type is commonly used for tabulated data.
    
*   **Extract From HTML**: Extract fields from standard web page HTML format files.
    
*   **Extract From JSON**: Extract JSON data from a binary file.
    
*   **Extract From ICS**: Extract fields from iCalendar format files.
    
*   **Extract From ODS**: Extract fields from ODS spreadsheet files.
    
*   **Extract From PDF**: Extract fields from Portable Document Format files.
    
*   **Extract From RTF**: Extract fields from Rich Text Format files.
    
*   **Extract From Text File**: Extract fields from a standard text file format.
    
*   **Extract From XLS**: Extract fields from a Microsoft Excel file (older format).
    
*   **Extract From XLSX**: Extract fields from a Microsoft Excel file.
    
*   **Move File to Base64 String**: Converts binary data to a text-friendly [base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4)
     format.
    

Example workflow[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile#example-workflow)

------------------------------------------------------------------------------------------------------------------------

In this example, a Webhook node is used to trigger the workflow. When a CSV file is sent to the webhook address, the file data is output and received by the Extract From File node.

Set to operate as 'Extract from CSV', the node then outputs the data as a series of JSON 'row' objects:

Copy

    {
      "row": {
      "0": "apple",
      "1": "1",
      "2": "2",
      "3": "3"
      }
      ...

**Receiving files with a webhook**

Select the Webhook Node's **Add Options** button and select **Raw body**, then enable that setting to get the node to output the binary file that the subsequent node is expecting.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile#node-parameters)

----------------------------------------------------------------------------------------------------------------------

### Input Binary Field[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile#input-binary-field)

Enter the name of the field from the node input data that contains the binary file. The default is 'data'.

### Destination Output Field[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile#destination-output-field)

Enter the name of the field in the node output that will contain the extracted data.

This parameter is only available for these operations:

*   Extract From JSON
    
*   Extract From ICS
    
*   Extract From Text File
    
*   Move File to Base64 String
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------

[Browse Extract From File integration templates](https://n8n.io/integrations/extract-from-file)
 or [search all templates](https://n8n.io/workflows/)

[PreviousExecution Data](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata)
[NextFilter](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filter)

Last updated 10 days ago

Was this helpful?