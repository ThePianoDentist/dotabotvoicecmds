_G._savedEnv = getfenv()

function GetDesire()
	local handle = GetBot();
	local name = handle:GetUnitName();
	mode = "none"
	CreateHTTPRequest(":5000/".. name):Send( function( result )
	                _G.crystal_maiden_mode = result.Body
                end )
	--print("crystal_maiden mode: " .. tostring(_G.crystal_maiden_mode))
	if _G.crystal_maiden_mode == "laning" then return 1.0 else return 0.0 end;
end

