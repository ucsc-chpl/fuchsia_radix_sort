import sys
import os
import struct

def generate_c_header(input_file, output_file, symbol_name):
    symbol_name = f"{symbol_name}_comp_shader_binary"
    with open(input_file, "rb") as f:
        data = f.read()
    with open(output_file, "w") as f:
        f.write(f"const uint32_t {symbol_name}[] = {{\n")
        for i in range(0, len(data), 4):
            uint32_value = struct.unpack("<I", data[i:i+4])[0]
            if i + 4 < len(data):
                f.write(f"    0x{uint32_value:08x},\n")
            else:
                f.write(f"    0x{uint32_value:08x}\n")
        f.write("};\n")


generate_c_header(sys.argv[1], sys.argv[2], sys.argv[3])
