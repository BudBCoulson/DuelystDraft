import csv

cards = [
  {
    'cardid': 20129,
    'name': 'Juxtaposition',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 0,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Switch positions between ANY two minions.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20085,
    'name': 'Mana Vortex',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 0,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'The next spell you cast this turn costs 1 less.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20355,
    'name': 'Meditate',
    'expansion': 'mythron',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 0,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      'Shuffle five copies of the spell you cast most recently into your deck (excluding Meditate).',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 126,
    'name': 'Ace',
    'expansion': 'shimzar',
    'cardtype': 'minion',
    'tribe': 'Battle Pet',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text': '<b>Ranged</b>',
    'attack': 1,
    'health': 2,
    'spirit': None
  },
  {
    'cardid': 20323,
    'name': 'Assassination Protocol',
    'expansion': 'immortal',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      'Reactivate an exhausted friendly minion. It cannot damage or attack Generals this turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 30023,
    'name': 'Crescent Spear',
    'expansion': 'shimzar',
    'cardtype': 'artifact',
    'tribe': '',
    'cost': 1,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'Your General gains +1 Attack. Spells you cast that deal damage deal +1 damage.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20088,
    'name': 'Ghost Lightning',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'basic',
    'faction': 'songhai',
    'text': 'Deal 1 damage to all enemy minions.',
    'attack': None,
    'health': None,
    'spirit': 0
  },
  {
    'cardid': 20275,
    'name': 'Gotatsu',
    'expansion': 'unearthed',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text': 'Deal 1 damage to a minion. Draw a card at end of turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 108,
    'name': 'Heartseeker',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text': '<b>Ranged</b>',
    'attack': 1,
    'health': 1,
    'spirit': None
  },
  {
    'cardid': 30052,
    'name': 'Horned Mask',
    'expansion': 'mythron',
    'cardtype': 'artifact',
    'tribe': '',
    'cost': 1,
    'rarity': 'epic',
    'faction': 'songhai',
    'text':
      'Your General gains +1 Attack.<br/>After a friendly minion with <b>Backstab</b> attacks, it gains +1/+1.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20086,
    'name': 'Inner Focus',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'basic',
    'faction': 'songhai',
    'text': 'Reactivate an exhausted friendly minion with 3 or less Attack.',
    'attack': None,
    'health': None,
    'spirit': 0
  },
  {
    'cardid': 20256,
    'name': 'Joseki',
    'expansion': 'ancients',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text': "Each player steals a random card from their opponent's deck.",
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 129,
    'name': 'Katara',
    'expansion': 'shimzar',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text': '<b>Backstab</b>: (1).',
    'attack': 1,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 20354,
    'name': 'Knucklestorm',
    'expansion': 'mythron',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text': '<b>Intensify</b>: Deal 1 damage to an enemy.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20168,
    'name': 'Mist Dragon Seal',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text': 'Give a friendly minion +1/+1 and teleport it anywhere.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20167,
    'name': 'Mist Walking',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Teleport your General up to 2 spaces.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20241,
    'name': 'Obscuring Blow',
    'expansion': 'ancients',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Give a friendly minion or General <b>Backstab</b> (2).',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20192,
    'name': 'Shadow Waltz',
    'expansion': 'shimzar',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      'Lower the cost of all minions with <b>Backstab</b> in your action bar by 1 and give them +1/+1.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20294,
    'name': 'Spiral Counter',
    'expansion': 'unearthed',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 1,
    'rarity': 'common',
    'faction': 'songhai',
    'text': 'Deal 8 damage to an enemy minion that attacked last turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20106,
    'name': 'Artifact Defiler',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'common',
    'faction': 'songhai',
    'text': 'Destroy all artifacts on the enemy General.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 30010,
    'name': 'Bloodrage Mask',
    'expansion': 'core',
    'cardtype': 'artifact',
    'tribe': '',
    'cost': 2,
    'rarity': 'basic',
    'faction': 'songhai',
    'text': 'Whenever you cast a spell, deal 1 damage to the enemy General.',
    'attack': None,
    'health': None,
    'spirit': 0
  },
  {
    'cardid': 115,
    'name': 'Chakri Avatar',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': 'Arcanyst',
    'cost': 2,
    'rarity': 'basic',
    'faction': 'songhai',
    'text': 'Whenever you cast a spell, this minion gains +1/+1',
    'attack': 1,
    'health': 2,
    'spirit': 0
  },
  {
    'cardid': 20191,
    'name': 'Crimson Coil',
    'expansion': 'shimzar',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'common',
    'faction': 'songhai',
    'text': 'Deal 2 damage to a minion. Activate your Battle Pets.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20094,
    'name': 'Deathstrike Seal',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      'Give a friendly minion, "Destroy any minion damaged by this minion."',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20143,
    'name': 'Eight Gates',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text': 'Spells you cast this turn that deal damage deal +2 damage.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20231,
    'name': 'Ethereal Blades',
    'expansion': 'ancients',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'common',
    'faction': 'songhai',
    'text': 'Give a friendly minion AND your General +2 Attack this turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 110,
    'name': 'Kaido Assassin',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 2,
    'rarity': 'basic',
    'faction': 'songhai',
    'text': '<b>Backstab</b>: (1).',
    'attack': 2,
    'health': 3,
    'spirit': 0
  },
  {
    'cardid': 30007,
    'name': 'Mask of Shadows',
    'expansion': 'core',
    'cardtype': 'artifact',
    'tribe': '',
    'cost': 2,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'Your General gains +1 Attack.<br/>Your General gains <b>Backstab</b> (4).',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20341,
    'name': 'Mass Flight',
    'expansion': 'immortal',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Give all friendly minions Flying this turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20194,
    'name': 'Mirror Meld',
    'expansion': 'shimzar',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Summon a copy of a friendly minion that costs 2 or less nearby.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20081,
    'name': 'Phoenix Fire',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'basic',
    'faction': 'songhai',
    'text': 'Deal 3 damage to anything.',
    'attack': None,
    'health': None,
    'spirit': 0
  },
  {
    'cardid': 20080,
    'name': 'Saberspine Seal',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'basic',
    'faction': 'songhai',
    'text': 'Give a minion or General +3 Attack this turn.',
    'attack': None,
    'health': None,
    'spirit': 0
  },
  {
    'cardid': 140,
    'name': 'Scroll Bandit',
    'expansion': 'unearthed',
    'cardtype': 'minion',
    'tribe': 'Arcanyst',
    'cost': 2,
    'rarity': 'epic',
    'faction': 'songhai',
    'text':
      "<b>Backstab</b>: (1).<br/>Whenever this backstabs, steal a spell from your opponent's deck.",
    'attack': 1,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 20365,
    'name': 'Second Self',
    'expansion': 'mythron',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 2,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Put an EXACT copy of a friendly minion into your action bar.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 145,
    'name': 'Suzumebachi',
    'expansion': 'immortal',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 2,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      'Whenever you cast a spell, this minion gains +1 Attack until your next turn.',
    'attack': 1,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 121,
    'name': 'Tusk Boar',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 2,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      '<b>Rush</b><br/>Return this minion to your action bar at the beginning of your turn.',
    'attack': 2,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 125,
    'name': 'Xho',
    'expansion': 'shimzar',
    'cardtype': 'minion',
    'tribe': 'Battle Pet',
    'cost': 2,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      '<b>Dying Wish</b>: Put a random Songhai spell into your action bar. It costs 1 less.',
    'attack': 2,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 20327,
    'name': 'Bamboozle',
    'expansion': 'immortal',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 3,
    'rarity': 'epic',
    'faction': 'songhai',
    'text':
      'Transform a nearby enemy minion into a 0/2 Panddo. If it is already a Panddo, instead destroy it and draw to fill your action bar.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 30027,
    'name': 'Bangle of Blinding Strike',
    'expansion': 'ancients',
    'cardtype': 'artifact',
    'tribe': '',
    'cost': 3,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Your General has <b>Celerity</b>.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 130,
    'name': 'Battle Panddo',
    'expansion': 'shimzar',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Whenever this minion takes damage, deal 1 damage to all enemies.',
    'attack': 2,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 117,
    'name': 'Celestial Phantom',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Destroy any minion damaged by this minion.',
    'attack': 1,
    'health': 5,
    'spirit': None
  },
  {
    'cardid': 30009,
    'name': 'Cyclone Mask',
    'expansion': 'core',
    'cardtype': 'artifact',
    'tribe': '',
    'cost': 3,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Your General gains <b>Ranged</b>.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 151,
    'name': 'Dusk Rigger',
    'expansion': 'immortal',
    'cardtype': 'minion',
    'tribe': 'Mech',
    'cost': 3,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      '<b>Backstab</b>: (2).<br/>Whenever this backstabs, put a MECHAZ0R Progression into your action bar.',
    'attack': 3,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 20283,
    'name': 'Flicker',
    'expansion': 'unearthed',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 3,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Teleport your General to a space behind an enemy.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 112,
    'name': 'Gore Horn',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': '<b>Backstab</b>: (2)<br/>After this minion attacks, it gains +1/+1.',
    'attack': 3,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 142,
    'name': 'Hundred-Handed Rakushi',
    'expansion': 'unearthed',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      '<b>Sentinel</b>: Minion summoned.<br/>Deal 2 damage to the minion that transformed this.',
    'attack': 3,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 114,
    'name': 'Jade Monk',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      'Whenever this minion takes damage, deal 1 damage to a random enemy minion.',
    'attack': 4,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 156,
    'name': 'Kaido Expert',
    'expansion': 'mythron',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      '<b>Backstab</b>: (1).<br/>Whenever this minion backstabs, summon a minion with <b>Backstab</b> that costs 2 or less from your deck nearby.',
    'attack': 2,
    'health': 2,
    'spirit': None
  },
  {
    'cardid': 128,
    'name': 'Ki Beholder',
    'expansion': 'shimzar',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      '<b>Ranged</b><br/><b>Opening Gambit</b>: An enemy minion cannot move next turn.',
    'attack': 3,
    'health': 2,
    'spirit': None
  },
  {
    'cardid': 20102,
    'name': 'Killing Edge',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 3,
    'rarity': 'basic',
    'faction': 'songhai',
    'text':
      'Give a friendly minion +4/+2. If that minion has <b>Backstab</b>, draw a card at end of turn.',
    'attack': None,
    'health': None,
    'spirit': 0
  },
  {
    'cardid': 122,
    'name': 'Lantern Fox',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'epic',
    'faction': 'songhai',
    'text':
      'Whenever this minion takes damage, put a Phoenix Fire into your action bar.',
    'attack': 2,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 144,
    'name': 'Mind-Cage Oni',
    'expansion': 'unearthed',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      '<b>Sentinel</b>: Spell cast.<br/>Whenever your opponent casts a spell, put a copy of that spell into your action bar.',
    'attack': 3,
    'health': 2,
    'spirit': None
  },
  {
    'cardid': 143,
    'name': 'Mizuchi',
    'expansion': 'unearthed',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      '<b>Sentinel</b>: General attacks.<br/><b>Flying</b><br/><b>Backstab</b>: (2).',
    'attack': 2,
    'health': 5,
    'spirit': None
  },
  {
    'cardid': 20087,
    'name': 'Onyx Bear Seal',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 3,
    'rarity': 'epic',
    'faction': 'songhai',
    'text':
      'Transform an enemy minion into a 0/2 Panddo that cannot be attacked.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 158,
    'name': 'Orizuru',
    'expansion': 'mythron',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'common',
    'faction': 'songhai',
    'text': '<b>Flying</b>',
    'attack': 3,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 20385,
    'name': 'Pandatentiary',
    'expansion': 'mythron',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 3,
    'rarity': 'epic',
    'faction': 'songhai',
    'text':
      'Surround the enemy General with friendly Panddo that disappear at the start of your next turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 149,
    'name': 'Penumbraxx',
    'expansion': 'immortal',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      '<b>Build</b>: (2).<br/><b>Backstab</b>: (2).<br/>Whenever this backstabs, transform it into a building with <b>Build</b> (1).',
    'attack': 4,
    'health': 1,
    'spirit': None
  },
  {
    'cardid': 135,
    'name': 'Sparrowhawk',
    'expansion': 'ancients',
    'cardtype': 'minion',
    'tribe': 'Arcanyst',
    'cost': 3,
    'rarity': 'common',
    'faction': 'songhai',
    'text': '<b>Bond</b>: Put a Mist Dragon Seal into your action bar.',
    'attack': 3,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 20328,
    'name': 'Substitution',
    'expansion': 'immortal',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 3,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Switch positions between a friendly minion and your General.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20314,
    'name': 'Thunderbomb',
    'expansion': 'immortal',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 3,
    'rarity': 'common',
    'faction': 'songhai',
    'text': 'Deal 3 damage to an enemy and 1 damage to all enemies around it.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 132,
    'name': 'Twilight Fox',
    'expansion': 'ancients',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      '<b>Blood Surge</b>: Teleport a random enemy to the space behind your General.',
    'attack': 3,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 20082,
    'name': 'Twin Strike',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 3,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      'Deal 2 damage to exactly two random enemy minions. Draw a card at end of turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 30033,
    'name': 'Unbounded Energy Amulet',
    'expansion': 'unearthed',
    'cardtype': 'artifact',
    'tribe': '',
    'cost': 3,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'Your General gains +1 Attack.<br/>Your General may move an additional space.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 134,
    'name': 'Whiplash',
    'expansion': 'ancients',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'common',
    'faction': 'songhai',
    'text': '<b>Blood Surge</b>: Deal 2 damage to the enemy General.',
    'attack': 4,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 109,
    'name': 'Widowmaker',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 3,
    'rarity': 'basic',
    'faction': 'songhai',
    'text': '<b>Ranged</b>',
    'attack': 2,
    'health': 3,
    'spirit': 0
  },
  {
    'cardid': 20100,
    'name': 'Ancestral Divination',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 4,
    'rarity': 'common',
    'faction': 'songhai',
    'text': 'Draw a card for each friendly minion.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 155,
    'name': 'Bakezori',
    'expansion': 'mythron',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 4,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Whenever this minion is moved for any reason, draw a card.',
    'attack': 2,
    'health': 6,
    'spirit': None
  },
  {
    'cardid': 160,
    'name': 'Coalfist',
    'expansion': 'mythron',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 4,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      '<b>Intensify</b>: Give a random nearby friendly minion +2 Attack this turn.',
    'attack': 5,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 20240,
    'name': 'Cobra Strike',
    'expansion': 'ancients',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 4,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Deal 3 damage to an enemy minion AND the enemy General.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 138,
    'name': 'Flamewreath',
    'expansion': 'unearthed',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 4,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      'Whenever this minion is moved for any reason, it deals 2 damage to all enemies around it.',
    'attack': 2,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 116,
    'name': 'Four Winds Magi',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': 'Arcanyst',
    'cost': 4,
    'rarity': 'rare',
    'faction': 'songhai',
    'text':
      'Whenever you cast a spell, deal 1 damage to enemy General and restore 1 Health to your General',
    'attack': 4,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 120,
    'name': 'Keshrai Fanblade',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 4,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      "<b>Opening Gambit</b>: Next turn, opponent's spells cost 2 more to cast",
    'attack': 5,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 136,
    'name': 'Kindling',
    'expansion': 'ancients',
    'cardtype': 'minion',
    'tribe': 'Arcanyst',
    'cost': 4,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Whenever you cast a spell, your Arcanyst minions gain +1 Attack.',
    'attack': 3,
    'health': 5,
    'spirit': None
  },
  {
    'cardid': 148,
    'name': 'Manakite Drifter',
    'expansion': 'immortal',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 4,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      '<b>Build</b>: (2).<br/>When this minion is built, gain +2 mana this turn.',
    'attack': 5,
    'health': 5,
    'spirit': None
  },
  {
    'cardid': 157,
    'name': 'Massacre Artist',
    'expansion': 'mythron',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 4,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      '<b>Backstab</b>: (2).<br/>After this minion attacks and backstabs, all attacks are backstabs this turn.',
    'attack': 2,
    'health': 5,
    'spirit': None
  },
  {
    'cardid': 20193,
    'name': 'Pandamonium',
    'expansion': 'shimzar',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 4,
    'rarity': 'epic',
    'faction': 'songhai',
    'text':
      'Transform ALL minions into 0/2 Panddo that cannot be attacked until end of turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 124,
    'name': 'Storm Sister Alkyone',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 4,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text': 'Spells you cast that deal damage deal +1 damage.',
    'attack': 3,
    'health': 5,
    'spirit': 0
  },
  {
    'cardid': 150,
    'name': 'Wildfire Tenketsu',
    'expansion': 'immortal',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 4,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': '<b>Blood Surge</b>: Put an Eight Gates into your action bar.',
    'attack': 3,
    'health': 5,
    'spirit': None
  },
  {
    'cardid': 20279,
    'name': 'Bombard',
    'expansion': 'unearthed',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 5,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Reactivate your minions with <b>Ranged</b>.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 133,
    'name': 'Geomancer',
    'expansion': 'ancients',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 5,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': '<b>Opening Gambit</b>: Your Bloodbound Spell is Phoenix Fire.',
    'attack': 5,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 119,
    'name': 'Hamon Bladeseeker',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 5,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'At the start of your turn, deal 2 damage to your General.',
    'attack': 8,
    'health': 8,
    'spirit': None
  },
  {
    'cardid': 20155,
    'name': "Heaven's Eclipse",
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 5,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text': 'Draw 3 spell cards from your deck.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 127,
    'name': 'Onyx Jaguar',
    'expansion': 'shimzar',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 5,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Whenever a friendly unit is moved for any reason, it gains +1/+1.',
    'attack': 3,
    'health': 3,
    'spirit': None
  },
  {
    'cardid': 20389,
    'name': 'Phoenix Barrage',
    'expansion': 'mythron',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 5,
    'rarity': 'common',
    'faction': 'songhai',
    'text':
      'Deal 3 damage to anything.<br/>Put a Phoenix Fire into your action bar.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 111,
    'name': 'Scarlet Viper',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 5,
    'rarity': 'common',
    'faction': 'songhai',
    'text': '<b>Flying</b><br/><b>Backstab</b>: (4).',
    'attack': 2,
    'health': 5,
    'spirit': None
  },
  {
    'cardid': 20326,
    'name': 'Seeker Squad',
    'expansion': 'immortal',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 5,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'Summon a Heartseeker in each nearby space diagonal from your General.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20267,
    'name': 'Twilight Reiki',
    'expansion': 'unearthed',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 5,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'Put 3 random Songhai minions into your action bar. They cost 1 less.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 159,
    'name': 'Xenkai Cannoneer',
    'expansion': 'mythron',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 5,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      '<b>Ranged</b><br/>Whenever you summon a minion with <b>Ranged</b>, that minion gains <b>Rush</b>.',
    'attack': 4,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 139,
    'name': 'Eternity Painter',
    'expansion': 'unearthed',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 6,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'At the end of your turn, transform all nearby enemy minions into 0/2 Panddos that cannot be attacked.',
    'attack': 3,
    'health': 4,
    'spirit': None
  },
  {
    'cardid': 20290,
    'name': 'Firestorm Mantra',
    'expansion': 'unearthed',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 6,
    'rarity': 'epic',
    'faction': 'songhai',
    'text':
      'Steal Health from the enemy General equal to twice the number of spells cast this turn.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 131,
    'name': 'Grandmaster Zendo',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 6,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text': 'The enemy General moves and attacks automatically.',
    'attack': 3,
    'health': 6,
    'spirit': None
  },
  {
    'cardid': 30038,
    'name': 'Ornate Hiogi',
    'expansion': 'immortal',
    'cardtype': 'artifact',
    'tribe': '',
    'cost': 6,
    'rarity': 'rare',
    'faction': 'songhai',
    'text': 'Whenever you cast a spell, draw a card.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 137,
    'name': 'Calligrapher',
    'expansion': 'ancients',
    'cardtype': 'minion',
    'tribe': 'Arcanyst',
    'cost': 7,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      '<b>Rush</b><br/>Whenever this minion attacks, put three Songhai spells into your action bar.',
    'attack': 3,
    'health': 7,
    'spirit': None
  },
  {
    'cardid': 146,
    'name': 'Second-sword Sarugi',
    'expansion': 'immortal',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 7,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text': 'Your spells cost 2 less.',
    'attack': 4,
    'health': 7,
    'spirit': None
  },
  {
    'cardid': 118,
    'name': 'Storm Kage',
    'expansion': 'core',
    'cardtype': 'minion',
    'tribe': '',
    'cost': 7,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'Whenever one of your spells deals damage, put a Kage Lightning in your action bar.',
    'attack': 5,
    'health': 10,
    'spirit': None
  },
  {
    'cardid': 20217,
    'name': 'Koan of Horns',
    'expansion': 'shimzar',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 8,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'Transform all minions in your action bar and deck into 0-cost Gore Horns. Draw 3 cards.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20084,
    'name': 'Spiral Technique',
    'expansion': 'core',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 8,
    'rarity': 'epic',
    'faction': 'songhai',
    'text': 'Deal 8 damage to anything.',
    'attack': None,
    'health': None,
    'spirit': None
  },
  {
    'cardid': 20377,
    'name': 'Kensho Vortex',
    'expansion': 'mythron',
    'cardtype': 'spell',
    'tribe': '',
    'cost': 11,
    'rarity': 'legendary',
    'faction': 'songhai',
    'text':
      'Costs 1 less for each spell you cast this game. Whenever you cast a spell this turn, summon a minion that costs up to 2 more nearby your General.',
    'attack': None,
    'health': None,
    'spirit': None
  }
]

with open('songhai.csv', 'w', newline='') as csvfile:
	w = csv.writer(csvfile)
	for d in cards:
		w.writerow([d['cardid']])
