_G._savedEnv = getfenv()
function GetDesire()
	if _G.drow_ranger_mode == "roam" then return 1.0 else return 0.0 end;
end