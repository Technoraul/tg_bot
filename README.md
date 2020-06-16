
## Telegram bot on python.
This bot was created so that the company's employees in the work chat /roll with whom they will go to lunch today.

Telegram bot has 3 commands:
/getid - returns your ID (works in private messages)
/get_groupid - returns group ID (works in private messages)
/roll - returns two random values from the file text.txt (works in chat)

### Manual:
1.Set your values here so that the bot works:

-WORK_GROUP_ID = -group_id

-TEST_GROUP_ID = -group_id (optional)

-admin [id, id]

-updater = Updater(token='BOT_TOKEN')

  
2.Create a file text.txt and fill it with content.
3.Create a service for your bot using systemd service utility
 
