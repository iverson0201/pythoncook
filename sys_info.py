#!/usr/bin/env python
# encoding: utf-8

# 使用 Python 获取 Linux 系统信息

import os
import platform

def print_base_info():
    print 'platform.uname(): ', platform.uname()
    print 'platform.system(): ', platform.system()
    print 'platform.release(): ', platform.release()
    print 'platform.linux_distribution(): ', platform.linux_distribution()
    print 'platform.architecture(): ', platform.architecture()

def cpu_info():
    cpuinfo = {}
    procinfo = {}
    nprocs = 0

    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                cpuinfo['proc%s' % nprocs] = procinfo
                nprocs += 1
                procinfo = {}
            elif len(line.split(':')) == 2:
                procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
            else:
                procinfo[line.split(':')[0].strip()] = ''
    return cpuinfo

def mem_info():
    meminfo = {}

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

def net_devs():
    with open('/proc/net/dev') as f:
        net_dump = f.readlines()
    device_data = {}
    from collections import namedtuple
    data = namedtuple('data',['rx','tx'])
    for line in net_dump[2:]:
        line = line.split(':')
        if line[0].strip() != 'lo':
            device_data[line[0].strip()] = data(float(line[1].split()[0])/(1024.0*1024.0),
                                                float(line[1].split()[8])/(1024.0*1024.0))
    return device_data

def process_list():
    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)
    return pids


if __name__ == '__main__':
    print_base_info()
    print 'cpu info dict: ', cpu_info()
    print 'mem info dict: ', mem_info()
    print 'netdevs info dict: ', net_devs()
    print 'pids: ', process_list()
