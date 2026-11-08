For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination.md)
.

The HTTP Request node supports pagination. This page provides some example configurations, including using the [HTTP node variables](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/http-node)
.

Refer to [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 for more information on the node.

**API differences**

Different APIs implement pagination in different ways. Check the API documentation for the API you're using for details. You need to find out things like:

*   Does the API provide the URL for the next page?
    
*   Are there API-specific limits on page size or page number?
    
*   The structure of the data that the API returns.
    

Enable pagination[](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination#enable-pagination)

-------------------------------------------------------------------------------------------------------------------

In the HTTP Request node, select **Add Option** > **Pagination**.

Use a URL from the response to get the next page using `$response`[](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination#use-a-url-from-the-response-to-get-the-next-page-using-dollarresponse)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the API returns the URL of the next page in its response:

1.  Set **Pagination Mode** to **Response Contains Next URL**. n8n displays the parameters for this option.
    
2.  In **Next URL**, use an expression to set the URL. The exact expression depends on the data returned by your API. For example, if the API includes a parameter called `next-page` in the response body:
    
    Copy
    
        {{ $response.body["next-page"] }}
    

Get the next page by number using `$pageCount`[](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination#get-the-next-page-by-number-using-dollarpagecount)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the API you're using supports targeting a specific page by number:

1.  Set **Pagination Mode** to **Update a Parameter in Each Request**.
    
2.  Set **Type** to **Query**.
    
3.  Enter the **Name** of the query parameter. This depends on your API and is usually described in its documentation. For example, some APIs use a query parameter named `page` to set the page. So **Name** would be `page`.
    
4.  Hover over **Value** and toggle **Expression** on.
    
5.  Enter `{{ $pageCount + 1 }}`
    

`$pageCount` is the number of pages the HTTP Request node has fetched. It starts at zero. Most API pagination counts from one (the first page is page one). This means that adding `+1` to `$pageCount` means the node fetches page one on its first loop, page two on its second, and so on.

Navigate pagination through body parameters[](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination#navigate-pagination-through-body-parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the API you're using allows you to paginate through the body parameters:

1.  Set the HTTP Request Method to **POST**
    
2.  Set **Pagination Mode** to **Update a Parameter in Each Request**.
    
3.  Select **Body** in the **Type** parameter.
    
4.  Enter the **Name** of the body parameter. This depends on the API you're using. `page` is a common key name.
    
5.  Hover over **Value** and toggle **Expression** on.
    
6.  Enter `{{ $pageCount + 1 }}`
    

Set the page size in the query[](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination#set-the-page-size-in-the-query)

---------------------------------------------------------------------------------------------------------------------------------------------

If the API you're using supports choosing the page size in the query:

1.  Select **Send Query Parameters** in main node parameters (this is the parameters you see when you first open the node, not the settings within options).
    
2.  Enter the **Name** of the query parameter. This depends on your API. For example, a lot of APIs use a query parameter named `limit` to set page size. So **Name** would be `limit`.
    
3.  In **Value**, enter your page size.
    

Related resources[](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination#related-resources)

-------------------------------------------------------------------------------------------------------------------

*   [HTTP Request node](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node)
    

[PreviousHTTP Request node](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node)
[NextIntegrate AI](https://docs.n8n.io/build/integrate-ai)

Last updated 10 days ago

Was this helpful?