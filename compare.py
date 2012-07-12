import os
import sys
import time
import httplib
import hashlib

def compare_url_path(url, path) :
	m = hashlib.md5()
	try :
		with open(path, 'r') as f :
			body = f.read()
			m.update(body)
	except :
		return False
	
	m2 = hashlib.md5()
	try :
		http = httplib.HTTPConnection("localhost", timeout=60)
		http.request(method="GET", url=url)
		ret = http.getresponse()
		if (int(ret.status) == 200) :
			body = ret.read()
			m2.update(body)

			if (m.digest() == m2.digest()) :
				return True
	except :
	   return False

	return False

def main() :

	while True:
		try:
			line = sys.stdin.readline()
			if not line :
				print "stop"
				break
			msg = line.strip('\r\n ')
			if not msg :
				continue
		except :
			return

		(url, path) = msg.split(' ');

		ret = compare_url_path(url, path)
		if ret :
			print "succ:", url, path
		else :
			print "failed:", url, path


if __name__ == "__main__" :
	main()
