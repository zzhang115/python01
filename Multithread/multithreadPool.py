import multiprocessing, sys, os, time

result=[]
def run(h):
    print "threading list:", h, os.getpid()
    time.sleep(2)
p=multiprocessing.Pool(processes=25)
for i in range(100):
    result.append(p.apply_async(run, ('%s'%i,)))
p.close()

for res in result:
    res.get(timeout=5)
