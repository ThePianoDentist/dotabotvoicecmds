_G._savedEnv = getfenv()
function GetDesire()
	if _G.earthshaker_mode == "retreat" then return 1.0 else return 0.0 end;
end