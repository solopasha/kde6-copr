local function name2name_with_namespace(name)
    local maps = require "fedora.srpm.kde_maps"
    return maps[name]
end

return {
    name2name_with_namespace = name2name_with_namespace,
}
