_G._savedEnv = getfenv()

function GetDesire()
	local handle = GetBot();
	local name = handle:GetUnitName();
	mode = "none"
	CreateHTTPRequest(":5000/".. name):Send( function( result )
	                _G.earthshaker_mode = result.Body
                end )
	--print("earthshaker mode: " .. tostring(_G.earthshaker_mode))
	if _G.earthshaker_mode == "laning" then return 1.0 else return 0.0 end;
end

