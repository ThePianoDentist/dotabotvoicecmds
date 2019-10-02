function GetBotNames()
    if GetTeam() == TEAM_RADIANT then
        return {"Burning", "Puppey", "Miracle-", "Fear", "Universe"}
    else return {"S4", "GH", "RTZ", "Sumail", "Synderen"} end
    end

function Think()
    if IsInCMPickPhase() then
        	CMPickHero("npc_dota_hero_bane") --dire
        	CMPickHero("npc_dota_hero_drow_ranger")
        	CMPickHero("npc_dota_hero_earthshaker")
        	CMPickHero("npc_dota_hero_axe") --dire
        	CMPickHero("npc_dota_hero_lich")
        	CMPickHero("npc_dota_hero_juggernaut") --dire
        	CMPickHero("npc_dota_hero_lina")
        	CMPickHero("npc_dota_hero_mirana") --dire
            CMPickHero("npc_dota_hero_nevermore") --dire
        	CMPickHero("npc_dota_hero_crystal_maiden")
    elseif IsInCMBanPhase() then
        	CMBanHero("npc_dota_hero_treant")
        	CMBanHero("npc_dota_hero_tinker")
        	CMBanHero("npc_dota_hero_meepo")
        	CMBanHero("npc_dota_hero_tiny")
        	CMBanHero("npc_dota_hero_viper")
        	CMBanHero("npc_dota_hero_pugna")
        	CMBanHero("npc_dota_hero_enigma")
            CMBanHero("npc_dota_hero_witch_doctor")
            CMBanHero("npc_dota_hero_leshrac")
            CMBanHero("npc_dota_hero_zuus")
            CMBanHero("npc_dota_hero_warlock")
            CMBanHero("npc_dota_hero_techies")
            CMBanHero("npc_dota_hero_venomancer")
    else
        	SelectHero(2, "npc_dota_hero_drow_ranger")
        	SelectHero(3, "npc_dota_hero_lich")
        	SelectHero(4, "npc_dota_hero_lina")
        	SelectHero(5, "npc_dota_hero_crystal_maiden")
        	SelectHero(6, "npc_dota_hero_earthshaker")
            SelectHero(7, "npc_dota_hero_axe")
            SelectHero(8, "npc_dota_hero_mirana")
            SelectHero(9, "npc_dota_hero_juggernaut")
            SelectHero(10, "npc_dota_hero_nevermore")
            SelectHero(11, "npc_dota_hero_bane")
    end

end

----------------------------------------------------------------------------------------------------
