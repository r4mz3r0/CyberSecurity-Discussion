# Remotely controlling a computer using the command line. Using the -e (executable) flag
#This is the machine we want to remotely control <br> 
 <span style="color: red">nc -Lp 666 -vv -e cmd.exe  </span><br>
  ## nc stands for netcat 
  ## -L is the "listen" flag. Why it is upper case? It listens until told otherwise. 
  ## -L flag is only allowed by windows. Use -l instead for linux, or to for listening temporarily. 
  ## -vv is double verbose, give out as much information onto the console. 
  ## -e is the program we want to execute, in this case it is cmd.exe 
#This is the machine that controls <br> 
nc 192.0.0.1 666 <br> 
  ## 192.0.0.1 is to be replaced with target IP, 
  ## 666 is the target address it should be up and listening
