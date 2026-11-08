For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile.md)
.

`binaryFile`.`**directory**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfiledirectory)

--------------------------------------------------------------------------------------------------------------------------------------------

**Description:** The path to the directory that the file is stored in. Useful for distinguishing between files with the same name in different directories. Not set if n8n is configured to store files in its database.

**Syntax:** `binaryFile`.`**directory**`

**Returns:** String

**Source:** Custom n8n functionality

`binaryFile`.`**fileExtension**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilefileextension)

----------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** The suffix attached to the filename (e.g. `txt`)

**Syntax:** `binaryFile`.`**fileExtension**`

**Returns:** String

**Source:** Custom n8n functionality

`binaryFile`.`**fileName**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilefilename)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** The name of the file, including extension

**Syntax:** `binaryFile`.`**fileName**`

**Returns:** String

**Source:** Custom n8n functionality

`binaryFile`.`**fileSize**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilefilesize)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** A string representing the size of the file

**Syntax:** `binaryFile`.`**fileSize**`

**Returns:** String

**Source:** Custom n8n functionality

`binaryFile`.`**fileType**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilefiletype)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** A string representing the type of the file, e.g. `image`. Corresponds to the first part of the MIME type.

**Syntax:** `binaryFile`.`**fileType**`

**Returns:** String

**Source:** Custom n8n functionality

`binaryFile`.`**id**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfileid)

------------------------------------------------------------------------------------------------------------------------------

**Description:** The unique ID of the file. Used to identify the file when it is stored on disk or in a storage service such as S3.

**Syntax:** `binaryFile`.`**id**`

**Returns:** String

**Source:** Custom n8n functionality

`binaryFile`.`**mimeType**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#binaryfilemimetype)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** A string representing the format of the file’s contents, e.g. `image/jpeg`

**Syntax:** `binaryFile`.`**mimeType**`

**Returns:** String

**Source:** Custom n8n functionality

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile#related-resources)

-------------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousArray](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array)
[NextBoolean](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean)

Last updated 10 days ago

Was this helpful?