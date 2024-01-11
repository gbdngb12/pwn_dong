config_arch = "x86-64"
config_os = "linux" # ['android', 'baremetal', 'cgc', 'freebsd', 'linux', 'windows']
config_mode = "local" # "local", "netcat", "ssh", "debugging"

config_loglevel = "debug" # ['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING']

struct_netcat = {
    "address" : "127.0.0.1",
    "port" : "12345"
}

struct_ssh = {
    "user" : "",
    "address" : "",
    "port" : "",
    "password" : "",
    "binary" : ""
}

struct_local = {
    "binary" : ""
}
