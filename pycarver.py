#!/usr/bin/env python3

import subprocess
import sh

subprocess.call('clear', shell=True)


rawimage = "/home/kalibox/Scripts/python/dfrws-2006-challenge.raw"

#grep = subprocess.Popen(['grep', ' ffd8 '], stdin=xxd.stdout, stdout=subprocess.PIPE)
#xxd.stdout.close()

#print(output.strip().split('\n')[0])
desdecodes = []
hastacodes = []
#bytecode = 0

print('Grepping " ffd8 ff" from ', str(rawimage))
output = sh.grep(sh.xxd('-s 0', rawimage), ' ffd8 ff')

print('Parsing output from " ffd8 ff"')
for line in output:
    hexcode = line.strip().split(':')[0]
    bytecode = int(sh.bc(sh.echo('ibase=16; ' + hexcode.upper())))
    print(bytecode)
    desdecodes.append(bytecode)
    start = "-s " + str(bytecode)
    hasta_output = sh.grep(sh.xxd(start, rawimage), '-m 1', ' ffd9 ')
    hexcode = hasta_output.strip().split(':')[0]
    bytecode = int(sh.bc(sh.echo('ibase=16; ' + hexcode.upper()))) + 2
    print(bytecode)
    hastacodes.append(bytecode)

#desdecodes = build_desdecodes(rawimage, desdecodes)

print(len(desdecodes))
print(len(hastacodes))
#sizes = []
status = "status=progress"
ifile = "if=" + str(rawimage)
bs = "bs=1"
oflag = "oflag=seek_bytes"
i = 0
for code in desdecodes:
    ofile = "jpeg" + str(i) + ".jpg"
    seek = "seek=" + str(desdecodes[i])
    size = int(hastacodes[i])-int(desdecodes[i])
    count = "count=" + str(size)
    print("desde: ", code, " size: ", size)
    print("ofile: ", ofile)
    dd = 'sudo dd ' + status + ' ' + ifile + ' ' + seek + ' ' + count + ' of=' + ofile + ' ' + oflag
    print(dd)
    print('\n')
    subprocess.run(dd, shell=True)
    i = i + 1
