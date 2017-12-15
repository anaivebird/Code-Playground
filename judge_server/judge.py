import sys
from subprocess import *

p = Popen("g++ run.cpp -std=c++11 -o ./r", shell=True)
p.wait()

p = Popen("g++ judge.cpp -std=c++11 -o ./j", shell=True)
p.wait()

j = Popen('./j', stdin=PIPE, stdout=PIPE)
r = Popen('./r', stdin=PIPE, stdout=PIPE)

for _ in range(3):
	tstr = j.stdout.readline()
	print(tstr)
	r.stdin.write(tstr)

while True:
	info_r = r.stdout.readline()
	print(info_r)
	j.stdin.write(info_r)
	info_j = j.stdout.readline()
	r.stdin.write(info_j)
	print(info_j)
	Type = list(map((int), info_j.split()))[0]
	if Type == -1:
		break

