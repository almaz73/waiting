import requests
import random


randPic = '🐮🐭🐫🐯🦏🦍🦊🦒🐀🐨🦘🐖🦇🦓🐰🦝🦔🦄🐆🐄🐷🦙🐽🐻🐈🐣🐔🐤🦜🐧🦉🦃🦚🐸🐍🦎🐊🦖🐲🐉🐋🦈🐳🐙🦋🦠🦂🕷🐜🌹🌺🌼🌻🌴🌲🌳🍂☘🌈✍🐕☹☻😁😂😃😆😇😈😉😊😋😌😍😎😏😐😒🚤😓😔😖😘😚😜😝😞😠😡😢😣😤😥😨😩😪😫😭😰🌏🍀😱😲😳😵😶😷😸🙀🙅🙆🙇🙉🙊🙋🙌🙍🙎✋🐲👀🐝💢☘✌∞©🐾💋👣🚗☠🚀🚃🚄🚅🚇🚉🚌🚏🚑🚒🚓🚕😄😅🚙🚚🚢🔥🎃👻🍬🦇💀🧡💣💥♻🧨🤔⚠🔎😘❌📈🍿☑✅🖤🧠❓❗®✉🔒☯☭🔱🎁🧢📊💕🤍🥱🛒🦠🍄🍓🧸🧺🪞⚡🐳💰🥇❤️🤙💪😤🍋😿🍒🗝️⌛🕗🌚'
url = 'https://favqs.com/api/qotd'
def nextCitation():
  pic = randPic[random.randrange(1,210)]
  pic0 = randPic[random.randrange(1,210)]

  response = requests.get(url)
  data = response.json()
  text =  data['quote']['body']
  author = data['quote']['author']
  return (f'{pic0} {pic0} {pic0} \n{text} \n{pic} author: {author} ')

