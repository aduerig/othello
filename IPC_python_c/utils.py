import time
import sys
import struct
import numpy as np

PY_MAJOR_VERSION = sys.version_info[0]

if PY_MAJOR_VERSION > 2:
    NULL_CHAR = 0
else:
    NULL_CHAR = '\0'




def get_floats():
    arr = np.arange(1, 65, dtype=np.float32)
    for i in range(len(arr)):
        arr[i] = arr[i] / len(arr)
    # print(arr)
    return arr



def write_send_code(mapfile, write_file):
    # writing correct code back
    mapfile.seek(0)
    mapfile.write("\x01\x00\x00\x00")

    # write_file.write("wrote 1 to send_code\n")
    # write_file.flush()


def write_to_memory(mapfile, s):
    mapfile.seek(4)
    # write rest of string
    mapfile.write(s)
    

def write_floats_to_memory(mapfile, floats):
    s = floats.tobytes()
    write_to_memory(mapfile, s)


def write_all_zeroes(mapfile):
    mapfile.seek(4)

    s = ""
    for i in range(128 * 4):
        s += "\x00"
    mapfile.write(s)


def read_send_code(mapfile, write_file):
    mapfile.seek(0)
    # write_file.write("reading code\n")

    code_str = ""
    code_str += mapfile.read_byte()
    code_str += mapfile.read_byte()
    code_str += mapfile.read_byte()
    code_str += mapfile.read_byte()
    code_int = struct.unpack("<L", code_str)[0]
    # write_file.write("code is: {0}\n".format(code_int))

    return code_int


def read_ints_from_memory(mapfile, write_file):
    mapfile.seek(4)
    s = []
    # write_file.write("reading ints\n")

    # 128 ints 4 bytes each    
    for i in range(128 * 4):
        c = mapfile.read_byte()
        s.append(c)
    s = ''.join(s)

    inters = []
    for i in range(len(s)/4):
        inters.append(struct.unpack("<L", s[(i*4):(i*4)+4])[0])

    # write_file.write("parsed ints ")
    # for i in inters:
    #     s = "{0}, ".format(i)
    #     write_file.write(s)
    return inters