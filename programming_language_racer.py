import matplotlib.pyplot as plt
import subprocess
import numpy as np
from util_scripts.logger import CustomLogger

NO_TESTS = 10

def compile_java_files():
    subprocess.run("javac Java/*.java", shell=True)

def compile_c_files():
    subprocess.run("g++ C/radix_sort.cpp C/timing.c -o C/radix_sort", shell=True)
    subprocess.run("g++ C/dynamic_mem_access.cpp C/timing.c -o C/dynamic_mem_access", shell=True)
    subprocess.run("g++ C/static_mem_access.cpp C/timing.c -o C/static_mem_access", shell=True)
    subprocess.run("g++ C/thread_context.c C/timing.c -o C/thread_context -pthread", shell=True)
    subprocess.run("g++ C/thread_create.c C/timing.c -o C/thread_create -pthread", shell=True)

def init():
    compile_java_files()
    compile_c_files()

def test_mem_access():
    data = {'Java': [], 'Python': [], 'C/C++\ndynamic': [], 'C/C++\nstatic': []}
    for _ in range(NO_TESTS):
        data['Java'].append(int(subprocess.getoutput("cd Java && java mem_access")))
        data['Python'].append(int(subprocess.getoutput("cd Python && python3 mem_access.py")))
        data['C/C++\ndynamic'].append(int(subprocess.getoutput("C/dynamic_mem_access")))
        data['C/C++\nstatic'].append(int(subprocess.getoutput("C/static_mem_access")))
    return data, "Microseconds\nlower the better", "Memory access speed"

def test_radix_sort():
    data = {'Java': [], 'Python': [], 'C/C++': []}
    for _ in range(NO_TESTS):
        data['Java'].append(int(subprocess.getoutput("cd Java && java radix_sort")))
        data['Python'].append(int(subprocess.getoutput("cd Python && python3 radix_sort.py")))
        data['C/C++'].append(int(subprocess.getoutput("C/radix_sort")))
    return data, "Microseconds\nlower the better", "Radix sort speed"

def test_thread_creation():
    data = {'Java': [], 'Python': [], 'C/C++': []}
    for _ in range(NO_TESTS):
        data['Java'].append(int(subprocess.getoutput("cd Java && java thread_create")))
        data['Python'].append(int(subprocess.getoutput("cd Python && python3 thread_create.py")))
        data['C/C++'].append(int(subprocess.getoutput("C/thread_create")))
    return data, "Microseconds\nlower the better", "Time taken to create 100 threads"   

def test_thread_context():
    data = {'Java': [], 'Python': [], 'C/C++': []}
    for _ in range(NO_TESTS):
        data['Java'].append(int(subprocess.getoutput("cd Java && java thread_context")))
        data['Python'].append(int(subprocess.getoutput("cd Python && python3 thread_context.py")))
        data['C/C++'].append(int(subprocess.getoutput("C/thread_context")))
    return data, "Number of thread switches\nhigher the better", "Number of thread switches"  

def plot(competitors: dict, measured: str, title: str, no_languages = 3):
    competitors = {k: np.array([i for i in v if i > 0]) for k, v in competitors.items()}
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))
    # Set position of bar on X axis
    br1 = np.arange(no_languages)
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    
    mins = []
    maxs = []
    means = []
    for v in competitors.values():
        mins.append(np.min(v))
        means.append(np.mean(v))
        maxs.append(np.max(v))

    plt.bar(br1, mins, color ='r', width = barWidth,
            edgecolor ='grey', label ='min')
    plt.bar(br2, means, color ='g', width = barWidth,
            edgecolor ='grey', label ='average')
    plt.bar(br3, maxs, color ='b', width = barWidth,
            edgecolor ='grey', label ='max')
    
    # Adding Xticks
    plt.xlabel('Programming language', fontweight ='bold', fontsize = 15)
    plt.ylabel(measured, fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(no_languages)],
            [k for k in competitors])
    plt.title(title)
    plt.legend()
    plt.draw()

def main():

    import argparse

    parser = argparse.ArgumentParser(description='Programming language drag racer')
    parser.add_argument('--race', nargs='+', default=[], choices=['thread_create', 'thread_context', 'mem_access', 'radix_sort', 'all'])
    parser.add_argument('--prepare', action='store_true')
    args = parser.parse_args()

    if args.prepare:
        init()

    if 'all' in args.race:
        CustomLogger.info("Running tests for memory access speed...")
        mem_access_data, mem_access_measured, mem_access_title = test_mem_access()
        plot(mem_access_data, mem_access_measured, mem_access_title, 4)
        CustomLogger.success("DONE")

        CustomLogger.info("Running tests for radix sort speed...")
        radix_sort_data, radix_sort_measured, radix_sort_title = test_radix_sort()
        plot(radix_sort_data, radix_sort_measured, radix_sort_title)
        CustomLogger.success("DONE")

        CustomLogger.info("Running tests for thread creation speed...")
        thread_create_data, thread_create_measured, thread_create_title = test_thread_creation()
        plot(thread_create_data, thread_create_measured, thread_create_title)
        CustomLogger.success("DONE")

        CustomLogger.info("Running tests for thread context speed...")
        thread_context_data, thread_context_measured, thread_context_title = test_thread_context()
        plot(thread_context_data, thread_context_measured, thread_context_title)
        CustomLogger.success("DONE")

    else:
        for i in args.race:
            if i == 'thread_create':
                CustomLogger.info("Running tests for thread creation speed...")
                thread_create_data, thread_create_measured, thread_create_title = test_thread_creation()
                plot(thread_create_data, thread_create_measured, thread_create_title)
                CustomLogger.success("DONE")
            elif i == 'thread_context':
                CustomLogger.info("Running tests for thread context speed...")
                thread_context_data, thread_context_measured, thread_context_title = test_thread_context()
                plot(thread_context_data, thread_context_measured, thread_context_title)
                CustomLogger.success("DONE")
            elif i == 'mem_access':
                CustomLogger.info("Running tests for memory access speed...")
                mem_access_data, mem_access_measured, mem_access_title = test_mem_access()
                plot(mem_access_data, mem_access_measured, mem_access_title, 4)
                CustomLogger.success("DONE")
            elif i == 'radix_sort':
                CustomLogger.info("Running tests for radix sort speed...")
                radix_sort_data, radix_sort_measured, radix_sort_title = test_radix_sort()
                plot(radix_sort_data, radix_sort_measured, radix_sort_title)
                CustomLogger.success("DONE")
    plt.show()

if __name__ == '__main__':
    main()