import sys
import TCP_Connection as tcp

host_address = sys.argv[1]
host_port = sys.argv[2]
tcp.connection(host_address, host_port)
