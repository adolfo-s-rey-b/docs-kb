For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/line.md)
.

**Feature availability**

The Line node is deprecated from n8n 1.64.0. LINE Notify ends its own service on April 1, 2025, after which the node stops working. View LINE Notify's [end of service announcement](https://notify-bot.line.me/closing-announce)
 for more information.

You can use these credentials to authenticate the following nodes:

*   [Line](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.line)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/line#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------

*   Notify OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/line#related-resources)

-------------------------------------------------------------------------------------------------

Refer to [Line Notify's API documentation](https://notify-bot.line.me/doc/en/)
 for more information about the service.

Using Notify OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/line#using-notify-oauth2)

-----------------------------------------------------------------------------------------------------

To configure this credential, you'll need a [Line](https://line.me/en/)
 account and:

*   A **Client ID**
    
*   A **Client Secret**
    

To generate both, connect Line with [Line Notify](https://notify-bot.line.me/en/)
. Then:

1.  Open the Line Notify page to [add a new service](https://notify-bot.line.me/my/services/new)
    .
    
2.  Enter a **Service name**. This name displays when someone tries to connect to the service.
    
3.  Enter a **Service description**.
    
4.  Enter a **Service URL**
    
5.  Enter your **Company/Enterprise**.
    
6.  Select your **Country/region**.
    
7.  Enter your name or team name as the **Representative**.
    
8.  Enter a valid **Email address**. Line will verify this email address before the service is fully registered. Use an email address you have ready access to.
    
9.  Copy the **OAuth Redirect URL** from your n8n credential and enter it as the **Callback URL** in Line Notify.
    
10.  Select **Agree and continue** to agree to the terms of service.
    
11.  Verify the information you entered is correct and select **Add**.
    
12.  Check your email and open the Line Notify Registration URL to verify your email address.
    
13.  Once verification is complete, open [**My services**](https://notify-bot.line.me/my/services/)
    .
    
14.  Select the service you just added.
    
15.  Copy the **Client ID** and enter it in your n8n credential.
    
16.  Select the option to **Display** the **Client Secret**. Copy the **Client Secret** and enter it in your n8n credential.
    
17.  In n8n, select **Connect my account** and follow the on-screen prompts to finish the credential.
    

Refer to the Authentication section of [Line Notify's API documentation](https://notify-bot.line.me/doc/en/)
 for more information.

[PreviousLemonade credentials](https://docs.n8n.io/integrations/builtin/credentials/lemonade)
[NextLinear credentials](https://docs.n8n.io/integrations/builtin/credentials/linear)

Last updated 10 days ago

Was this helpful?