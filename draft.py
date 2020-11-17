import random as r
import pandas as pd
import base64
import webbrowser
import string
import tkinter as tk

'''
factions = ['Lyonar Kingdoms', 'Songhai Empire', 'Vetruvian Imperium',
			'Abyssian Host', 'Magmar Aspects', 'Vanar Kindred']
generals = ['Argeon Highmayne', 'Zir\'an Sunforge', 'Brome Warcrest', 
			'Kaleos Xaan', 'Reva Eventide', 'Shidai Stormblossom',
			'Zirix Starstrider', 'Scioness Sajj', 'Ciphyron Ascendant',
			'Lilithe Blightchaser', 'Cassyva Soulreaper', 'Maehv Skinsolder',
			'Vaath the Immortal', 'Starhorn the Seeker','Ragnora the Relentless',
			'Faie Bloodwing', 'Kara Winterblade', 'Ilena Cryobyte']
expansions = ['Core', 'Denizens of Shim\'zar', 'Bloodbound Ancients',
			'Unearthed Prophecy', 'Immortal Vanguard', 'Trials of Mythron']
rarities = ['Common', 'Rare', 'Epic', 'Legendary']
'''

card_csv = pd.read_csv('Data/DC.csv')
ch = None
	
def draftsim():
	deck = {}
	
	gens = card_csv[card_csv['- rarity'] == 'Basic'].reset_index(drop=True)
	choices = r.sample(list(range(18)),4)
	offered = [gens['- name'].iloc[x] for x in choices]
	
	#print('Choose a general:')
	#for i in range(4):
	#	print(str(i) + '. ' + offered[i])
	
	win = tk.Tk()
	win.title('Choose a General')
	win.geometry('1150x375')
	for i in range(4):
		img = tk.PhotoImage(file="DPC/Generals/" + cleantext(offered[i]) + ".png").subsample(2,2)
		but = tk.Button(win,image=img,command=(lambda i=i: clicked(i,win)))
		but.image = img
		but.grid(row=1,column=i)
	win.mainloop()
	
	gennum = choices[ch]
	fkey = gennum // 3 + 1
	deck[str(gens['- id'].iloc[gennum])] = [gens['- name'].iloc[gennum],1]
	
	options = card_csv[(card_csv['- faction number'] == 0) | 
			(card_csv['- faction number'] == fkey)].reset_index(drop=True)
	opt_c = options[options['- rarity'] == 'Common']
	opt_r = options[options['- rarity'] == 'Rare']
	opt_e = options[options['- rarity'] == 'Epic']
	opt_l = options[options['- rarity'] == 'Legendary']
	
	e, nl, fl = False, False, False
	
	for j in range(29):
		#generate a set of 3 cards to choose from
		#user picks one to add to draft deck
		
		#rarity
		#counts: 227 neutrals (rarity 89/51/40/47)
		#98 in each faction (rarity 37/21/20/20)
		
		#remember to incorporate functionality for gauntlet-only cards
		
		if e: s = 26
		elif nl or fl: s = 28
		else: s = r.randrange(29)
		if s < 20: #common/basic
			bucket = r.sample(list(range(126)),3)
			fkeys = fkeylist(bucket,89,fkey)
			restricted = opt_c
		elif s < 26: #rare
			bucket = r.sample(list(range(72)),3)
			fkeys = fkeylist(bucket,51,fkey)
			restricted = opt_r
		elif s < 28: #epic
			bucket = r.sample(list(range(60)),3)
			fkeys = fkeylist(bucket,40,fkey)
			restricted = opt_e
		else: #legendary
			if nl: bucket = r.sample(list(range(47)),3)
			elif fl: bucket = r.sample(list(range(47,67)),3)
			else: bucket = r.sample(list(range(67)),3)
			fkeys = fkeylist(bucket,47,fkey)
			restricted = opt_l
		
		offered = [restricted['- name'].iloc[x] for x in bucket]
			
		#print('Pick ' + str(j+1) + '. Choose a card:')
		#for i in range(3):
		#	print(str(i) + '. ' + offered[i])
		
		win = tk.Tk()
		win.title('Choice ' + str(j+1) +' of 29')
		win.geometry('865x375')
		for i in range(3):
			img = tk.PhotoImage(file="DPC/" + str(fkeys[i]) + "/" + cleantext(offered[i]) + ".png").subsample(2,2)
			but = tk.Button(win,image=img,command=(lambda i=i: clicked(i,win)))
			but.image = img
			but.grid(row=1,column=i)
		win.mainloop()
					
		cardnum = bucket[ch]
		
		if restricted['- name'].iloc[cardnum] == 'Fortuneshaper':
			e = True
		elif restricted['- name'].iloc[cardnum] == 'Futureshaker':
			nl = True
		elif restricted['- name'].iloc[cardnum] == 'Fatesealer':
			fl = True
		else:
			e, nl, fl = False, False, False
		
		if str(restricted['- id'].iloc[cardnum]) in deck:
			deck[str(restricted['- id'].iloc[cardnum])][1] += 1
		else:
			deck[str(restricted['- id'].iloc[cardnum])] = [restricted['- name'].iloc[cardnum],1]
		
	return deck
	
def describedeck(deck):
	print('Gauntlet draft')
	
	for card in deck:
		print(str(deck[card][1]) + ' ' + deck[card][0])
		
def encodedeck(deck):
	#number:card ID
	#comma seperated
	
	deckstr = ''
	for card in deck:
		deckstr += str(deck[card][1]) + ':' + card + ','
	encoded = base64.b64encode(deckstr[:-1].encode('utf-8'))
	
	return str(encoded)[2:-1]
	
def cleantext(s):
	s_clean = ''
	
	for w in s:
		if (w not in string.punctuation) and (w != ' '):
			s_clean += w
			
	return s_clean
	
def clicked(i,wind):
	global ch
	ch = i
	wind.destroy()
	
def fkeylist(bucket,nnum,fkey):
	fkeys = []
	for b in bucket:
		if b < nnum:
			fkeys.append(0)
		else:
			fkeys.append(fkey)
	return fkeys

d = draftsim()
describedeck(d)
url = 'https://dl.bagoum.com/deckbuilder#'+encodedeck(d)
webbrowser.open(url)
