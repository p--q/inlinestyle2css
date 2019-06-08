#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from .main import main
PROFILE = 0
if PROFILE:
	import cProfile, pstats
	pr = cProfile.Profile()
	pr.run('main()')
	with open("profile_stats.txt", "w") as f:
		stats = pstats.Stats(pr, stream=f).strip_dirs().sort_stats('cumulative')
# 		stats.print_stats()
# 		stats.print_callers()
		stats.print_callees()
	sys.exit(0)
sys.exit(main())
