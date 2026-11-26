local envs = {
  NOTE = "adm-note",
  TIP = "adm-tip",
  IMPORTANT = "adm-important",
  WARNING = "adm-warning",
  CAUTION = "adm-caution",
}

local function blocks_to_latex(blocks)
  local doc = pandoc.Pandoc(blocks)
  return pandoc.write(doc, "latex")
end

function BlockQuote(el)
  if #el.content == 0 then return nil end
  local first = el.content[1]
  if first.t ~= "Para" and first.t ~= "Plain" then return nil end

  local first_inline = first.content[1]
  if not first_inline or first_inline.t ~= "Str" then return nil end

  local kind = first_inline.text:match("^%[!([A-Za-z]+)%]$")
  if not kind then return nil end

  local env = envs[kind:upper()]
  if not env then return nil end

  table.remove(first.content, 1)
  if first.content[1] and (first.content[1].t == "SoftBreak" or first.content[1].t == "Space") then
    table.remove(first.content, 1)
  end
  if #first.content == 0 then
    table.remove(el.content, 1)
  end

  local body_tex = blocks_to_latex(el.content)
  local raw_tex = "\\begin{" .. env .. "}\n" .. body_tex .. "\\end{" .. env .. "}\n"
  return pandoc.RawBlock("latex", raw_tex)
end