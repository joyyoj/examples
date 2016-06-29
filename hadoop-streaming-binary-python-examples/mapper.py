
#!/usr/bin/env python
import log_event_pb2
import sys
import struct
import typedbytes
from struct import Struct

user_action = log_event_pb2.UserAction()
unpack_int = Struct('!i').unpack

class ProtobufReader:
    @staticmethod
    def next():
	key_len_str = sys.stdin.read(4)
	if len(key_len_str) != 4:
	    return (None, None)
	key_len = unpack_int(key_len_str)[0]
	key = sys.stdin.read(8) # ignore key_len key
	if len(key) != 8:
	    return (None, None)

	value_len_str = sys.stdin.read(4) # read
        if len(value_len_str) != 4:
  	    return (None, None)
	value_len = unpack_int(value_len_str)[0] 
	value = sys.stdin.read(value_len)
	if len(value) != value_len:
	    return (None, None)
	return (key, value) 

# input comes from STDIN (standard input)
while True:
    try:
	(key, value) = ProtobufReader.next()	
	if key == None:
	    break
	user_action.ParseFromString(value)
	s = " user id: %s ." % user_action.uid.user_id
    except BaseException, e:
	sys.stderr.write('Failed: ' + str(e))
	pass
