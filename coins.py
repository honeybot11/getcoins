import samino,time,os,sys
vip = [""] # userIds
client = samino.Client("22D3085F471DF87A00FB4CE43052685FE93239644F93AD2140B23F3C77277FF6CAE5A0C164593CD9A8")
client.login(email="kknkk1223@gmail.com",password="9jaia0")

@client.event("on_message")
def on_message(data: samino.lib.Event):
	msg = data.message.content
	msgId = data.message.messageId
	comId = data.ndcId
	chatId = data.message.chatId
	userId = data.message.userId
	nickname = data.message.author.nickname
	try: mentionIds = data.message.json["extensions"]["mentionedArray"]
	except: pass
	local = samino.Local(comId)
	if msg.startswith("!get"):
		local.send_message(chatId,f"{nickname} done ",asWeb=True)
		for a in range(300): client.watch_ad(userId)

def socketRoot():
	while True:
		print("updating socket....")
		client.launch()
		shundle = client.socket;shundle.close();client.launch()
		time.sleep(300)
		sys.argv;sys.executable;print("restart now")
		os.execv(sys.executable, [ python ] + sys.argv)
socketRoot()
