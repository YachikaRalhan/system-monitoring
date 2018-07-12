import functions

op = {}


def cpu(cpu):
    parse_mpstat(cpu['mpstat'])
    return op


def parse_mpstat(cmd):
    out, err = functions.run_cmd(cmd)
    for line in out.splitlines():
        a = line.split()
    op['%usr'] = a[3]
    op['%nice'] = a[4]
    op['%sys'] = a[5]
    op['%iowait'] = a[6]
    op['%irq'] = a[7]
    op['%soft'] = a[8]
    op['%steal'] = a[9]
    op['%guest'] = a[10]
    op['%gnice'] = a[11]
    op['%idle'] = a[12]
    return op
