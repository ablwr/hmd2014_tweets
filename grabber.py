#!/usr/bin/env python

import twarc

for tweet in twarc.search("hmd2014"):
  print tweet["created_at"] + " @" + tweet["user"]["screen_name"] + ": " + tweet["text"]