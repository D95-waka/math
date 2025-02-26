local function scan_theorems(line_content)
	local env = string.match(line_content, "\\begin%{([a-zA-Z]+)%}")
	if env ~= nil and Theorems_macro_names[env] ~= nil then
		Scan_in_process = env
		Theorems_buffer = Theorems_buffer .. line_content
		return line_content .. " \\directlua{ t = token.scan_word() table.insert(Theorems_c_arr, t) } \\thetheorem{} "
	end

	if Scan_in_process ~= nil then
		Theorems_buffer = Theorems_buffer .. line_content
	end

	if Scan_in_process ~= nil and string.find(line_content, "\\end{" .. Scan_in_process .. "}") then
		Scan_in_process = nil
		table.insert(Theorems_v_arr, Theorems_buffer)
		Theorems_buffer = ""
	end

	return line_content
end

function Theorems_summary_setup(macro_names)
	Scan_in_process = nil
	Theorems_buffer = ""
	Theorems_c_arr = {}
	Theorems_v_arr = {}
	Theorems_macro_names = {}
	for v in string.gmatch(macro_names, "[^, ]+") do
		Theorems_macro_names[v] = 1
	end

	luatexbase.add_to_callback("process_input_buffer", scan_theorems, "finish")
end

function Generate_theorems_summary()
	local original_section = token.scan_string()
	tex.print("\\begin{NoHyper}")
	for key, value in pairs(Theorems_v_arr) do
		local section_number = tonumber(string.match(Theorems_c_arr[key], "(%d+)%."))
		local theorem_number = tonumber(string.match(Theorems_c_arr[key], "%.(%d+)")) - 1
		tex.print("\\setcounter{theorem}{" .. theorem_number .. "}")
		tex.print("\\setcounter{section}{" .. section_number .. "}")
		tex.print(value)
	end

	tex.print("\\end{NoHyper}")
	tex.print("\\setcounter{section}{" .. original_section .. "}")
end
