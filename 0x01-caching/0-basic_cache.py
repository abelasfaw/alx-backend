#!/usr/bin/python3
'''Basic Cache'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Basic cache operation'''

    def put(self, key, item):
        '''assigns value to cache_data'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''returns value in cache data'''
        return self.cache_data.get(key, None)
