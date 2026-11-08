For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram.md)
.

Use the Telegram node to automate work in [Telegram](https://telegram.org/)
 and integrate Telegram with other applications. n8n has built-in support for a wide range of Telegram features, including getting files as well as deleting and editing messages.

On this page, you'll find a list of operations the Telegram node supports and links to more resources.

**Credentials**

Refer to [Telegram credentials](https://docs.n8n.io/integrations/builtin/credentials/telegram)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram#operations)

----------------------------------------------------------------------------------------------------

*   [**Chat** operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations)
    
    *   [**Get**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations#get-chat)
         up-to-date information about a chat.
        
    *   [**Get Administrators**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations#get-administrators)
        : Get a list of all administrators in a chat.
        
    *   [**Get Member**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations#get-chat-member)
        : Get the details of a chat member.
        
    *   [**Leave**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations#leave-chat)
         a chat.
        
    *   [**Set Description**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations#set-description)
         of a chat.
        
    *   [**Set Title**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations#set-title)
         of a chat.
        
    
*   [**Callback** operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations)
    
    *   [**Answer Query**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations#answer-query)
        : Send answers to callback queries sent from [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards)
        .
        
    *   [**Answer Inline Query**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations#answer-inline-query)
        : Send answers to callback queries sent from inline queries.
        
    
*   [**File** operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations)
    
    *   [**Get File**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations#get-file)
         from Telegram.
        
    
*   [**Message** operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations)
    
    *   [**Delete Chat Message**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#delete-chat-message)
        .
        
    *   [**Edit Message Text**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#edit-message-text)
        : Edit the text of an existing message.
        
    *   [**Pin Chat Message**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#pin-chat-message)
         for the chat.
        
    *   [**Send Animation**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-animation)
         to the chat.
        
        *   For use with GIFs or H.264/MPEG-4 AVC videos without sound up to 50 MB in size.
            
        
    *   [**Send Audio**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-audio)
         file to the chat and display it in the music player.
        
    *   [**Send Chat Action**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-chat-action)
        : Tell the user that something is happening on the bot's side. The status is set for 5 seconds or less.
        
    *   [**Send Document**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-document)
         to the chat.
        
    *   [**Send Location**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-location)
        : Send a geolocation to the chat.
        
    *   [**Send Media Group**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-media-group)
        : Send a group of photos and/or videos.
        
    *   [**Send Message**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-message)
         to the chat.
        
    *   [**Send Photo**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-photo)
         to the chat.
        
    *   [**Send Sticker**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-sticker)
         to the chat.
        
        *   For use with static .WEBP, animated .TGS, or video .WEBM stickers.
            
        
    *   [**Send Video**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#send-video)
         to the chat.
        
    *   [**Unpin Chat Message**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations#unpin-chat-message)
         from the chat.
        
    
    **Add bot to channel**
    
    To use most of the **Message** operations, you must add your bot to a channel so that it can send messages to that channel. Refer to [Common Issues | Add a bot to a Telegram channel](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues#add-a-bot-to-a-telegram-channel)
     for more information.
    
    Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram#templates-and-examples)
    
    ----------------------------------------------------------------------------------------------------------------------------
    

[Browse n8n-nodes-base.telegram integration templates](https://n8n.io/integrations/telegram)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram#related-resources)

------------------------------------------------------------------------------------------------------------------

Refer to [Telegram's API documentation](https://core.telegram.org/bots/api)
 for more information about the service.

n8n provides a trigger node for Telegram. Refer to the [Telegram Trigger node documentation](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger)
 for more information.

Common issues[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram#common-issues)

----------------------------------------------------------------------------------------------------------

For common errors or issues and suggested resolution steps, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues)
.

[PreviousTapfiliate](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.tapfiliate)
[NextChat operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations)

Last updated 10 days ago

Was this helpful?