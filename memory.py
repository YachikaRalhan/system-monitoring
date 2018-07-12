import functions


def memory(memory):
    op = parse_netstat(memory['free'])
    return op


def parse_netstat(cmd):
    out, err = functions.run_cmd(cmd)
    for line in out.splitlines():
        a = line.split()
    return {'total': a[1], 'used': a[2], 'free': a[3], 'shared': a[4], 'buff/cache': a[5], 'avail': a[6]}
