import json

from flask import Response
from flask_api import FlaskAPI, status, exceptions
from constants import *

app = FlaskAPI(__name__)

DESIRE_STATE = {
    'npc_dota_hero_earthshaker': BOT_MODE_LANING,
    'npc_dota_hero_lich': BOT_MODE_LANING,
    'npc_dota_hero_lina': BOT_MODE_LANING,
'npc_dota_hero_drow_ranger': BOT_MODE_LANING,
'npc_dota_hero_crystal_maiden': BOT_MODE_LANING,
}


@app.route("/<hero>", methods=['POST'])
def desires(hero):
    """
    List or create notes.
    """
    print(DESIRE_STATE[hero])
    response = Response(
        response=DESIRE_STATE[hero],
        status=200,
    )
    return response


@app.route("/<hero>/<mode>", methods=['POST'])
def set_desires(hero, mode):
    """
    Retrieve, update or delete note instances.
    """
    print("hero: {}, mode: {}".format(hero, mode))
    if hero not in DESIRE_STATE:
        raise exceptions.NotFound()
    DESIRE_STATE[hero] = mode
    return DESIRE_STATE[hero]


if __name__ == "__main__":
    app.run(debug=True)