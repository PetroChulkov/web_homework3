from multiprocessing import Pool, cpu_count
import time
from ast import literal_eval


def factorize(number):

    list = []
    for i in range(1, number + 1):

        if number % i == 0:
            list.append(i)

    return list


def callback(list):
    end = time.time() - start
    for x in list:
        print(f"Result for {x[-1]} is: {x}")

    print(f'Total time: {round(end, 2)} seconds')



if __name__ == '__main__':
    a = literal_eval(input("Please type your data in list format, exmpl: [a, b, c]:"))
    start = time.time()
    print(f"Count CPU: {cpu_count()}")
    with Pool(cpu_count()) as p:
        p.map_async(factorize, a , callback=callback)
        p.close()
        p.join()




