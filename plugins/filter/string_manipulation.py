#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FilterModule(object):
    def remove_keys_from_dict(self, dictionary, keys):
        """Remove keys from a dictionary."""
        if not isinstance(dictionary, dict):
            raise TypeError("dictionary must be a dict")
        if not isinstance(keys, list):
            raise TypeError("keys must be a list")
        if not keys:
            raise ValueError("keys must not be empty")
        return {key: value for key, value in dictionary.items() if key not in keys}

    def filter_keys_from_dict(self, dictionary, keys):
        """Return only the keys specified in the list."""
        if not isinstance(dictionary, dict):
            raise TypeError("dictionary must be a dict")
        if not isinstance(keys, list):
            raise TypeError("keys must be a list")
        if not keys:
            raise ValueError("keys must not be empty")
        return {key: value for key, value in dictionary.items() if key in keys}

    def filters(self):
        return {
            "remove_keys_from_dict": self.remove_keys_from_dict,
            "filter_keys_from_dict": self.filter_keys_from_dict,
        }
