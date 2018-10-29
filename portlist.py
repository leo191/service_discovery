import subprocess as sp


def list_ips(port):
    check_netstat = sp.run(["which","netstat"])
    if check_netstat.returncode != 0:
        print("install netstat!")
        exit(1)
    netargs = ['nestat', '-tn']
    greparg = ['grep',':80']
    awkarg = ['awk', '']

