_G._savedEnv = getfenv()
function GetDesire()
	if _G.lich_mode == "attack" then return 1.0 else return 0.0 end;
end