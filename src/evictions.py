import sys
import queue
from collections import OrderedDict

def fifo(filePath):
    with open(filePath) as f:
        firstLine = f.readline().split()
        k = int(firstLine[0])
        m = int(firstLine[1])
        reqs = [int(x) for x in f.readline().split()]
        cache = queue.Queue(maxsize=k)
        missess = 0
        for req in reqs:
            if req not in cache.queue:
                missess += 1
                if cache.qsize() < k:
                    cache.put(req)
                else:
                    cache.get()
                    cache.put(req)
        return missess


def lru(filePath):
    with open(filePath) as f:
        firstLine = f.readline().split()
        k = int(firstLine[0])
        m = int(firstLine[1])
        reqs = [int(x) for x in f.readline().split()]
        cache = OrderedDict()
        missess = 0
        for req in reqs:
            if req in cache:
                cache.move_to_end(req)
            else:
                missess += 1
                if len(cache) < k:
                    cache[req] = True
                else:
                    cache.popitem(last=False)
                    cache[req] = True
        return missess


def optff(file):
    pass

def main():
    if len(sys.argv) != 2:
        print("Usage: py evictions.py <file>")
        sys.exit(1)
    filePath = sys.argv[1]
    print("FIFO  : ", fifo(filePath))
    print("LRU   : ", lru(filePath))
    print("OPTFF : ", optff(filePath))

if __name__=="__main__":
    main()