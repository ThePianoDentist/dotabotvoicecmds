_G._savedEnv = getfenv()

function GetDesire()
	local handle = GetBot();
	local name = handle:GetUnitName();
	print("lich name: " .. name)
	mode = "none"
	CreateHTTPRequest(":5000/".. name):Send( function( result )
	                _G.lich_mode = result.Body
	                print(mode)

                end )
	print("lich mode: " .. tostring(_G.lich_mode))
	if _G.lich_mode == "laning" then return 1.0 else return 0.0 end;
end

