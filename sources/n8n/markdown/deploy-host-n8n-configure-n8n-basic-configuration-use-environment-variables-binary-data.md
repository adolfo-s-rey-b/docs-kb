For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data.md)
.

**File-based configuration**

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#keeping-sensitive-data-in-separate-files)
 for more details.

By default, n8n uses memory to store binary data. On self-hosted Business and Enterprise plans, you can choose to use an external service instead. Refer to [External storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
 for more information on using external storage for binary data.

Variable

Type

Default

Description

`N8N_AVAILABLE_BINARY_DATA_MODES`

String

`filesystem`

A comma separated list of available binary data modes.

`N8N_BINARY_DATA_DATABASE_MAX_FILE_SIZE`

Number

`512`

Maximum size (in MiB) of a single file n8n stores when `N8N_DEFAULT_BINARY_DATA_MODE` is `database`. Can't exceed `1024`, the limit of a database column. Storing a larger file fails.

`N8N_BINARY_DATA_STORAGE_PATH`

String

`N8N_USER_FOLDER/binaryData`

The path where n8n stores binary data.

`N8N_DEFAULT_BINARY_DATA_MODE`

String

`default`

The default binary data mode. `default` keeps binary data in memory. Set to `filesystem` to use the filesystem, `s3` to use AWS S3, `azure` to use Azure Blob Storage, or `database` to use the DB. Note that binary data pruning operates on the active binary data mode. For example, if your instance stored data in S3, and you later switched to filesystem mode, n8n only prunes binary data in the filesystem. This may change in future.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------------

*   [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
    

[PreviousAsk n8n AI](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant)
[NextCredentials](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials)

Last updated 10 days ago

Was this helpful?