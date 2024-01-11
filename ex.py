from utils import *
from config import *

context.arch = config_arch # 익스플로잇 대상 아키텍처 'x86-64'
context.os = config_os
context.log_level = config_loglevel

if config_mode == "local" :
    p = process(struct_local["binary"])
elif config_mode == "netcat" :
    p = remote(struct_netcat["address"], struct_netcat["port"])
elif config_mode == "ssh" :
    p1 = ssh(struct_ssh["user"], struct_ssh["address"], port=struct_ssh["port"], password=struct_ssh["password"])
    p = p1.process(struct_ssh["binary"])
elif config_mode == "debugging" :
    p = process(struct_local["binary"])
    script = '''
    set follow-fork-mode child
    handle SIGALRM ignore
    break *main
    '''
    gdb.attach(p, script)
else :
    print("unknown config_mode ", config_mode)
    exit(1)

if config_os == "windows" :
    executable = {} #winfile(struct_local["binary"])
    print("not supported windows yet")
    exit(1)
elif config_os == "linux" :
    executable = ELF(struct_local["binary"])
