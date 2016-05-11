#!/usr/bin/env python
import os

def search_and_replace(dir, old_str, new_str):
    for dname, dirs, files in os.walk(dir):
        for fname in files:
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            s = s.replace(old_str, new_str)
            with open(fpath, "w") as f:
                f.write(s)
                
search_and_replace(".", "old_str", "new_str")
