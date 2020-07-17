#NetCat
# Transfering a file 
## This is the server. It has the file
nc -v -w 30 -p 666 < file.txt
## This is the client. It request the file. 
nc -v -w 2 192.168.0.10 666 > file.txt 
## replace IP address with the target ip 
## -v is for verbose, not required but this shows messages. 
## -w is the wait time, for example -w 30 means the server will stay open for 30 seconds
