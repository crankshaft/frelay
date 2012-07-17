#!/usr/bin/python2.6

import subprocess
import sys
import re


def run_cmd(cmd):
	p = subprocess.Popen(cmd,stdout = subprocess.PIPE,shell=True,)
	p.wait()
	return p.stdout.read()

if len(sys.argv) != 2 :
	print "Usage: irqbalancer.py ethX"
	exit(1)

result = []
i = 0

irqs = run_cmd("cat /proc/interrupts | grep -e " + sys.argv[1])
cpus = int(run_cmd("cat /proc/cpuinfo |grep processor|wc -l"))

for j in irqs.strip().split("\n"):
	result.append(j.strip().split(":")[0])
queues = len(result)

if queues < 4:
	print "Doesn't support multi queue. Only #{i} queue(s)."
	exit(1);


i = 0
for irq in result :
	sa = 1 << i % cpus 
	print "Queue: %d  Mask: %x irq: %s" % (i, sa, irq)
	run_cmd("echo  %x > /proc/irq/%s/smp_affinity" % (sa, irq))
	i += 1
