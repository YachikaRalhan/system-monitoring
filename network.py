import functions


op = {
    'udp': [],
    "tcp": []
}


def network(nw):
    o = parse_netstat(nw['netstat'])
    return o


def parse_netstat(cmd):
    out, err = functions.run_cmd(cmd)
    op = {
        'udp': [],
        "tcp": []
    }
    for line in out.splitlines():
        a = line.split()
        if a[0] == 'tcp' or a[0] == 'tcp6':
            op['tcp'].append(assign_cols_tcp(a))
        elif a[0] == 'udp' or a[0] == 'udp6':
            op['udp'].append(assign_cols_udp(a))
    return op

def assign_cols_tcp(a):
    return {'localaddr': a[3], 'foreignaddr': a[4], 'state': a[5], 'pid': a[6]}


def assign_cols_udp(a):
    return {'localaddr': a[3], 'foreignaddr': a[4], 'pid': a[5]}
