_G._savedEnv = getfenv()
function GetDesire()
	if _G.lina_mode == "defend_tower_mid" then return 1.0 else return 0.0 end;
end