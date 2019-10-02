_G._savedEnv = getfenv()
function GetDesire()
	if _G.crystal_maiden_mode == "defend_ally" then return 1.0 else return 0.0 end;
end