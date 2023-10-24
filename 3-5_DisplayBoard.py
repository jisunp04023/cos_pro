# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(phrases, second):
	s = "______________" + phrases
	start = second
	end = second + 14
	
	while True:
		if start < len(s) and end < len(s):
			break
		
		if start >= len(s):
			start -= len(s)
			
		if end >= len(s):
			end -= len(s)
	
	return s[start : end]
