For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md)
.

Use the Convert to File node to take input data and output it as a file. This converts the input JSON data into a binary format.

**Extract From File**

To extract data from a file and convert it to JSON, use the [Extract from File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile)
 node.

Operations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#operations)

----------------------------------------------------------------------------------------------------------

*   [**Convert to CSV**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-csv)
    
*   [**Convert to HTML**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-html)
    
*   [**Convert to ICS**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-ics)
    
*   [**Convert to JSON**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-json)
    
*   [**Convert to ODS**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-ods)
    
*   [**Convert to RTF**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-rtf)
    
*   [**Convert to Text File**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-text-file)
    
*   [**Convert to XLS**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-xls)
    
*   [**Convert to XLSX**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-xlsx)
    
*   [**Move Base64 String to File**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#move-base64-string-to-file)
    

Node parameters and options depend on the operation you select.

### Convert to CSV[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-csv)

Configure the node for this operation with the **Put Output File in Field** parameter. Enter the name of the field in the output data to contain the file.

#### Convert to CSV options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-csv-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   If the first row of the file contains header names, turn on the **Header Row** option.
    

### Convert to HTML[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-html)

Configure the node for this operation with the **Put Output File in Field** parameter. Enter the name of the field in the output data to contain the file.

#### Convert to HTML options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-html-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   If the first row of the file contains header names, turn on the **Header Row** option.
    

### Convert to ICS[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-ics)

*   **Put Output File in Field**. Enter the name of the field in the output data to contain the file.
    
*   **Event Title**: Enter the title for the event.
    
*   **Start**: Enter the date and time the event will start. All-day events ignore the time.
    
*   **End**: Enter the date and time the event will end. All-day events ignore the time. If unset, the node uses the start date.
    
*   **All Day**: Select whether the event is an all day event (turned on) or not (turned off).
    

#### Convert to ICS options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-ics-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   **Attendees**: Use this option to add attendees to the event. For each attendee, add:
    
    *   **Name**
        
    *   **Email**
        
    *   **RSVP**: Select whether the attendee needs to confirm attendance (turned on) or doesn't (turned off).
        
    
*   **Busy Status**: Use this option to set the busy status for Microsoft applications like Outlook. Choose from:
    
    *   **Busy**
        
    *   **Tentative**
        
    
*   **Calendar Name**: For Apple and Microsoft calendars, enter the [calendar name](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-oxcical/1da58449-b97e-46bd-b018-a1ce576f3e6d)
     for the event.
    
*   **Description**: Enter an event description.
    
*   **Geolocation**: Enter the **Latitude** and **Longitude** for the event's location.
    
*   **Location**: Enter the event's intended venue/location.
    
*   **Recurrence Rule**: Enter a rule to define the repeat pattern of the event (RRULE). Generate rules using the [iCalendar.org RRULE Tool](https://icalendar.org/rrule-tool.html)
    .
    
*   **Organizer**: Enter the organizer's **Name** and **Email**.
    
*   **Sequence**: If you're sending an update for an event with the same universally unique ID (UID), enter the revision sequence number.
    
*   **Status**: Set the status of the event. Choose from:
    
    *   **Confirmed**
        
    *   **Cancelled**
        
    *   **Tentative**
        
    
*   **UID**: Enter a universally unique ID (UID) for the event. The UID should be globally unique. The node automatically generates a UID if you don't enter one.
    
*   **URL**: Enter a URL associated with the event.
    
*   **Use Workflow Timezone**: Whether to use UTC time zone (turned off) or the workflow's timezone (turned on). Set the workflow's timezone in the [Workflow Settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
    .
    

### Convert to JSON[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-json)

Choose the best output **Mode** for your needs from these options:

*   **All Items to One File**: Send all input items to a single file.
    
*   **Each Item to Separate File**: Create a file for every input item.
    

#### Convert to JSON options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-json-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   **Format**: Choose whether to format the JSON for easier reading (turned on) or not (turned off).
    
*   **Encoding**: Choose the character set to use to encode the data. The default is **utf8**.
    

### Convert to ODS[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-ods)

Configure the node for this operation with the **Put Output File in Field** parameter. Enter the name of the field in the output data to contain the file.

#### Convert to ODS options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-ods-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   **Compression**: Choose whether to compress and reduce the file's output size.
    
*   **Header Row**: Turn on if the first row of the file contains header names.
    
*   **Sheet Name**: Enter the Sheet Name to create in the spreadsheet.
    

### Convert to RTF[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-rtf)

Configure the node for this operation with the **Put Output File in Field** parameter. Enter the name of the field in the output data to contain the file.

#### Convert to RFT options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-rft-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   If the first row of the file contains header names, turn on the **Header Row** option.
    

### Convert to Text File[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-text-file)

Enter the name of the **Text Input Field** that contains a string to convert to a file. Use dot-notation for deep fields, for example `level1.level2.currentKey`.

#### Convert to Text File options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-text-file-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   **Encoding**: Choose the character set to use to encode the data. The default is **utf8**.
    

### Convert to XLS[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-xls)

Configure the node for this operation with the **Put Output File in Field** parameter. Enter the name of the field in the output data to contain the file.

#### Convert to XLS options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-xls-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   **Header Row**: Turn on if the first row of the file contains header names.
    
*   **Sheet Name**: Enter the Sheet Name to create in the spreadsheet.
    

### Convert to XLSX[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-xlsx)

Configure the node for this operation with the **Put Output File in Field** parameter. Enter the name of the field in the output data to contain the file.

#### Convert to XLSX options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#convert-to-xlsx-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   **Compression**: Choose whether to compress and reduce the file's output size.
    
*   **Header Row**: Turn on if the first row of the file contains header names.
    
*   **Sheet Name**: Enter the Sheet Name to create in the spreadsheet.
    

### Move Base64 String to File[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#move-base64-string-to-file)

Enter the name of the **Base64 Input Field** that contains the Base64 string to convert to a file. Use dot-notation for deep fields, for example `level1.level2.currentKey`.

#### Move Base64 String to File options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#move-base64-string-to-file-options)

You can also configure this operation with these **Options**:

*   **File Name**: Enter the file name for the generated output file.
    
*   **MIME Type**: Enter the MIME type of the output file. Refer to [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)
     for a list of common MIME types and the file extensions they relate to.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------

[Browse Convert to File integration templates](https://n8n.io/integrations/convert-to-file)
 or [search all templates](https://n8n.io/workflows/)

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues)
[NextCrypto](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto)

Last updated 10 days ago

Was this helpful?