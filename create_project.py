# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pathlib import Path

import sys

projectname = sys.argv[1]

filename = projectname + '.sublime-project'
my_file = Path(filename)
if not my_file.is_file():
	template_text = '''{
		"build_systems":
		[
			{
				"file_regex": "^[ ]*File \\\"(...*?)\\\", line ([0-9]*)",
				"name": "Anaconda Python Builder",
				"selector": "source.python",
				"shell_cmd": "\\\"/home/arodriguez/.virtualenvs/to_replace/bin/python\\\" -u \\\"$file\\\""
			}
		],
		"folders":
		[
			{
	            "follow_symlinks": true,
	            "path": "to_replace"
			}
		],
		"settings":
		{
			"python_interpreter": "/home/arodriguez/.virtualenvs/to_replace/bin/python",
		}
	}'''
	with open(filename, 'w') as f: 
		f.write(template_text.replace('to_replace', projectname))
	print ('Created project: ' + filename)

