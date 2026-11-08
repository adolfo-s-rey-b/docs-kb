For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images.md)
.

Binary data is any file-type data, such as image files or documents.

This page collects resources relating to binary data in n8n.

Working with binary data in your workflows[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images#working-with-binary-data-in-your-workflows)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can process binary data in n8n workflows. n8n provides nodes to help you work with binary data. You can also use code.

### Nodes[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images#nodes)

There are three key nodes dedicated to handling binary data files:

*   [Convert to File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile)
     to take input data and output it as a file.
    
*   [Extract From File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile)
     to get data from a binary format and convert it to JSON.
    
*   [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile)
     to read and write files from/to the machine where n8n is running.
    

There are separate nodes for working with XML and HTML data:

*   [HTML](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html)
    
*   [XML](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml)
    

And nodes for performing common tasks:

*   [Compression](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression)
    
*   [Edit Image](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage)
    
*   [FTP](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ftp)
    

You can trigger a workflow based on changes to a local file using the [Local File trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger)
.

To split or concatenate binary data items, use the [data transformation nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes#other-data-transformation-nodes)
.

### Code[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images#code)

You can use the [Code node](https://docs.n8n.io/build/code-in-n8n/using-the-code-node)
 to manipulate binary data in your workflows. For example, [Get the binary data buffer](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer)
: get the binary data available in your workflow.

Configure binary data mode when self-hosting[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images#configure-binary-data-mode-when-self-hosting)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can configure how your self-hosted n8n instance handles binary data using the [Binary data environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data)
. This includes tasks such as setting the storage path and choosing how to store binary data.

Your configuration affects how well n8n scales: [Scaling | Binary data filesystem mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data)
.

Reading and writing binary files can have security implications. If you want to disable reading and writing binary data, use the `NODES_EXCLUDE` environment variable. Refer to [Environment variables | Nodes](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes)
 for more information.

Related resources[](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------

*   [Handle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)
    
*   [Work with dates and times](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-dates-and-times)
    
*   [Query JSON data](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data)
    

[PreviousHandle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)
[NextWork with dates and times](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-dates-and-times)

Last updated 10 days ago

Was this helpful?