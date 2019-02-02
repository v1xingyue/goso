--
--- LuaJIT 2.0.4
--
local ffi = require("ffi")
local goso = ffi.load("./goso.so")

ffi.cdef[[
    char * BoxHello(char* message);
]]

local taskString = "info from lua!"
local message_block = goso.BoxHello(ffi.cast('char *',taskString))
local message = ffi.string(message_block)
print(message)


