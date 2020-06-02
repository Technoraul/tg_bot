# tg_bot
telegram bot on python.

This telegram bot has 3 commands:
/get_id - returns your ID
/get_group_id - returns group ID
/roll - returns two random values from the file text.txt

Manual:
1.Set your values here so that the bot works:
  -WORK_GROUP_ID = -group_id
  -TEST_GROUP_ID = -group_id
  -admin [id, id]
  -updater = Updater(token='BOT_TOKEN')
  
2. Create a file text.txt and fill it with content.
  
The bot was created so that the company's employees in the work chat /roll with whom they will go to lunch today.
