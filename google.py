#!/usr/bin/env python2.7

try:
    import gevent
    from gevent import monkey
    monkey.patch_all()
except:
    monkey = None

from multiprocessing.pool import ThreadPool
import argparse
import httplib
import socket
import time
import re

socket.setdefaulttimeout(3)

def get_connect_time(ip, port):
    conn = httplib.HTTPConnection(ip, port)
    try:
        conn.request('HEAD', '/')
        resp = conn.getresponse()
        if resp.status == 200 and resp.getheader('server') == 'gws':
            conn = httplib.HTTPConnection(ip, port)
            conn.request('HEAD', '/')
            s = time.time()
            resp = conn.getresponse()
            dt = time.time() - s
            if resp.status == 200:
                return dt
    except:
        pass
    return 0

def ping(ip):
    t = get_connect_time(ip, 80)
    return (ip, t)

def bi_value(x):
    if x < 0: y = -1
    elif x > 0: y = 1
    else: y = 0
    return y

def get_available_google_ips(seeds, threads=None, max=None):
    threads = threads if threads else (500 if monkey else 10)
    max = max if max else 50
    gen = random_ip_generator(seeds)
    pool = ThreadPool(processes=threads)
    available_ips = []
    while len(available_ips) <= max:
        latent_ips = [gen.next() for _ in range(threads)]
        results = pool.map(ping, latent_ips)
        for ip, dt in results:
            if dt > 0:
                available_ips.append((ip, dt))
    sorted_ips = map(lambda x: x[0], sorted(available_ips, lambda (_, a), (__, b): bi_value(a-b)))
    return sorted_ips[:max]


def random_ip_generator(seeds):
    from random import randint
    cached = set()
    seeds_len = len(seeds) - 1
    count = 1
    def gen():
        idx = randint(0, seeds_len)
        seed = seeds[idx]
        prefix, _range = seed.rsplit('.', 1)
        while True:
            ip = '.'.join([prefix, str(randint(*map(int, _range.split('-'))))])
            if ip in cached:
                continue
            cached.add(ip)
            return ip
    while True:
        yield gen()

def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--threads', default=500, type=int)
    parser.add_argument('-o', '--output', default='output.txt')
    parser.add_argument('-m', '--max', default=50, type=int)
    parser.add_argument('seed_file', default='input.txt')

    args = parser.parse_args()
    threads = args.threads
    output = args.output
    seed_file = args.seed_file

    with open(seed_file) as fr:
        seeds = fr.readlines()
    google_ips = get_available_google_ips(seeds, threads)
    with open(output, 'w') as fw:
        fw.write('|'.join(google_ips))

if __name__ == '__main__':
    _main()
