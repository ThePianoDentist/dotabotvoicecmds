BOT_MODE_LANING = "laning"
BOT_MODE_ATTACK = "attack"
BOT_MODE_ROAM = "roam"
BOT_MODE_RETREAT = "retreat"
BOT_MODE_SECRET_SHOP = "secretshop"
BOT_MODE_SIDE_SHOP = "sideshop"
BOT_MODE_PUSH_TOWER_TOP = "pushtowertop"
BOT_MODE_PUSH_TOWER_MID = "pushtowermid"
BOT_MODE_PUSH_TOWER_BOT = "pushtowerbot"
BOT_MODE_DEFEND_TOWER_TOP = "defendtowertop"
BOT_MODE_DEFEND_TOWER_MID = "defendtowermid"
BOT_MODE_DEFEND_TOWER_BOT = "defendtowerbot"
BOT_MODE_ASSEMBLE = "assemble"
BOT_MODE_TEAM_ROAM = "teamroam"
BOT_MODE_FARM = "farm"
BOT_MODE_DEFEND_ALLY = "defendally"
BOT_MODE_EVASIVE_MANEUVERS = "evasivemaneuvers"
BOT_MODE_ROSHAN = "roshan"
BOT_MODE_ITEM = "item"
BOT_MODE_WARD = "ward"
BOT_MODE_RUNE = "rune"

VALID_MODES = [
    BOT_MODE_LANING, BOT_MODE_ATTACK, BOT_MODE_ROAM, BOT_MODE_RETREAT,
    BOT_MODE_PUSH_TOWER_TOP, BOT_MODE_PUSH_TOWER_MID, BOT_MODE_PUSH_TOWER_BOT, BOT_MODE_DEFEND_TOWER_TOP,
    BOT_MODE_DEFEND_TOWER_MID, BOT_MODE_DEFEND_TOWER_BOT, BOT_MODE_ASSEMBLE, BOT_MODE_TEAM_ROAM, BOT_MODE_FARM,
    BOT_MODE_DEFEND_ALLY, BOT_MODE_EVASIVE_MANEUVERS, BOT_MODE_ROSHAN, BOT_MODE_ITEM, BOT_MODE_WARD,
    #BOT_MODE_SECRET_SHOP, BOT_MODE_SIDE_SHOP
]


PLAYERS_TO_HERO = {'burning': 'npc_dota_hero_drow_ranger',
                   'puppy': 'npc_dota_hero_lich',
                   'miracle': 'npc_dota_hero_lina',
                   'universe': 'npc_dota_hero_earthshaker',
                   'fear': 'npc_dota_hero_crystal_maiden'
                   }