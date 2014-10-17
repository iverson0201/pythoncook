#!/usr/bin/env python
# encoding: utf-8

from operator import itemgetter

# 据说是最快的方法
d = {'a':2, 'b':23, 'c':5, 'd':17, 'e':1}

# 按照value排序
d_v = sorted(d.iteritems(), key=itemgetter(1), reverse=True)
print 'sort by value: ', d_v

# 按照key排序
d_k = sorted(d.iteritems(), key=itemgetter(0), reverse=True)
print 'sort by key: ', d_k
