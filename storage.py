import functions

op = []

def storage(storage):
    o = parse_netstat(storage['df'])
    return o


def parse_netstat(cmd):
    out, err = functions.run_cmd(cmd)
    op=[]
    for line in out.splitlines():
        a = line.split()
        op.append({'filesystem':a[0],'size':a[1],'used':a[2],'avail':a[3],'use%':a[4],'mountedOn':a[5]})
    return op
