_G._savedEnv = getfenv()

function GetDesire()
	local handle = GetBot();
	local name = handle:GetUnitName();
	mode = "none"
	CreateHTTPRequest(":5000/".. name):Send( function( result )
	                _G.drow_ranger_mode = result.Body

                end )
	--print("drow_ranger mode: " .. tostring(_G.drow_ranger_mode))
	if _G.drow_ranger_mode == "laning" then return 1.0 else return 0.0 end;
end

