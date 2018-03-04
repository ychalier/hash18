import multiprocessing, threading, time


class Thread(threading.Thread):
    def __init__(self, function, args=[]):
        threading.Thread.__init__(self)
        self.function = function
        self.args = args

    def run(self):
        # print("[THREAD]\tstarting\t", self.name)
        self.function(self.args)
        # print("[THREAD]\texiting \t", self.name)


class Process(multiprocessing.Process):
    def __init__(self, function, data):
        multiprocessing.Process.__init__(self, target=function, args=(data,))

    def run(self):
        # print("[PROCESS]\tstarting\t", self.name)
        multiprocessing.Process.run(self)
        # print("[PROCESS]\texiting \t", self.name)


class Map(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, args):
        for arg in args:
            self.function(arg)


def dispatch(mode, function, dataset, n=None):
    if n is None:
        n = multiprocessing.cpu_count()
    step, jobs = len(dataset) // n, []
    for i in range(n):
        if i < n - 1:
            data = dataset[step * i : step * (i+1)]
        else:
            data = dataset[step * i:]
        if mode in ["p", "process"]:
            jobs.append(Process(Map(function), data))
        elif mode in ["t", "thread"]:
            jobs.append(Thread(Map(function), data))
    return jobs


def start_and_wait(jobs):
    t_start = time.time()
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    t_elapsed = time.time() - t_start
    print("All jobs terminated.\nElapsed time (seconds):", t_elapsed)
    return t_elapsed
