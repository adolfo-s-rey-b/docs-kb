For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/use-an-api-playground.md)
.

This documentation site provides a playground to test out calls. Self-hosted users also have access to a built-in playground hosted as part of their instance.

Documentation playground[](https://docs.n8n.io/connect/n8n-api/use-an-api-playground#documentation-playground)

---------------------------------------------------------------------------------------------------------------

You can test API calls from this site's [endpoint reference](https://docs.n8n.io/connect/n8n-api/api-reference)
. You need to set your server's base URL and instance name, and add an API key.

n8n uses [Scalar's](https://github.com/scalar/scalar)
 open source API platform to power this functionality.

**Exposed API key and data**

Use a test API key with limited scopes and test data when using a playground. All calls from the playground are routed through Scalar's proxy servers.

**Real data**

You have access to your live data. This is useful for trying out requests. Be aware you can change or delete real data.

Built-in playground[](https://docs.n8n.io/connect/n8n-api/use-an-api-playground#built-in-playground)

-----------------------------------------------------------------------------------------------------

**Feature availability**

The API playground is available on:

*   **Self-hosted:** All editions
    

It isn't available on n8n Cloud.

The n8n API comes with a built-in Swagger UI playground in self-hosted versions. This provides interactive documentation, where you can try out requests. The path to access the playground depends on your hosting.

n8n constructs the path from values set in your environment variables:

Copy

    N8N_HOST:N8N_PORT/N8N_PATH/api/v<api-version-number>/docs

The API version number is `1`. There may be multiple versions available in the future.

**Real data**

If you select **Authorize** and enter your API key in the API playground, you have access to your live data. This is useful for trying out requests. Be aware you can change or delete real data.

The API includes built-in documentation about credential formats. This is available using the `credentials` endpoint:

Copy

    N8N_HOST:N8N_PORT/N8N_PATH/api/v<api-version-number>/credentials/schema/{credentialTypeName}

**How to find** `**credentialTypeName**`

To find the type, download your workflow as JSON and examine it. For example, for a Google Drive node the `{credentialTypeName}` is `googleDriveOAuth2Api`:

Copy

    {
        ...,
        "credentials": {
            "googleDriveOAuth2Api": {
            "id": "9",
            "name": "Google Drive"
            }
        }
    }

Related resources[](https://docs.n8n.io/connect/n8n-api/use-an-api-playground#related-resources)

-------------------------------------------------------------------------------------------------

*   [n8n API](https://docs.n8n.io/connect/n8n-api)
    
*   [Authentication](https://docs.n8n.io/connect/n8n-api/authentication)
    
*   [Pagination](https://docs.n8n.io/connect/n8n-api/pagination)
    
*   [Idempotency](https://docs.n8n.io/connect/n8n-api/idempotency)
    
*   [Endpoint reference](https://docs.n8n.io/connect/n8n-api/api-reference)
    

[PreviousIdempotency](https://docs.n8n.io/connect/n8n-api/idempotency)
[NextEndpoint reference](https://docs.n8n.io/connect/n8n-api/api-reference)

Last updated 10 days ago

Was this helpful?