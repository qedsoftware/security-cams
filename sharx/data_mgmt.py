#!/usr/bin/env python
import os
from datetime import datetime, timedelta

MAX_DAYS = 7
files = [f for f in sorted(os.listdir("."))]
records = filter(lambda x: x.endswith('.thm') or x.endswith('.mov'), files)
expiration = "MA_"+(datetime.now()-timedelta(days=MAX_DAYS)).strftime("%Y-%m-%d")

for r in records:
    if r < expiration:
        os.remove(r)
