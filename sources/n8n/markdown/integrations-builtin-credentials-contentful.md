For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/contentful.md)
.

You can use these credentials to authenticate the following nodes:

*   [Contentful](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.contentful)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/contentful#prerequisites)

-----------------------------------------------------------------------------------------------

*   Create a [Contentful](https://www.contentful.com/)
     account.
    
*   Create a [Contentful space](https://www.contentful.com/help/getting-started/contentful-101/#step-2-create-a-space)
    .
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/contentful#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------------

*   API access token
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/contentful#related-resources)

-------------------------------------------------------------------------------------------------------

Refer to [Contentful's API documentation](https://www.contentful.com/developers/docs/references/)
 for more information about the service.

Using API access token[](https://docs.n8n.io/integrations/builtin/credentials/contentful#using-api-access-token)

-----------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   Your Contentful **Space ID**: The Space ID displays as you generate the tokens; You can also refer to the [Contentful Find space ID documentation](https://www.contentful.com/help/spaces/find-space-id/)
     to view the Space ID.
    
*   A **Content Delivery API Access Token**: Required if you want to use the [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/)
    . Leave blank if you don't intend to use this API.
    
*   A **Content Preview API Access Token**: Required if you want to use the [Content Preview API](https://www.contentful.com/developers/docs/references/content-preview-api/)
    . Leave blank if you don't intend to use this API.
    

View and generate access tokens in Contentful in **Settings > API keys**. Contentful generates tokens for both Content Delivery API and Content Preview API as part of a single key. Refer to the [Contentful API authentication documentation](https://www.contentful.com/developers/docs/references/authentication/)
 for detailed instructions.

[PreviousConfluence credentials](https://docs.n8n.io/integrations/builtin/credentials/confluence)
[NextConvertAPI credentials](https://docs.n8n.io/integrations/builtin/credentials/convertapi)

Last updated 10 days ago

Was this helpful?