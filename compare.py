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

def compare_url_md5(url, md5) :
	m = hashlib.md5()
	try :
		http = httplib.HTTPConnection("localhost", timeout=60)
		http.request(method="GET", url=url)
		ret = http.getresponse()
		if (int(ret.status) == 200) :
			body = ret.read()
			m.update(body)

			if (m.hexdigest() == md5) :
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

		(url, path, md5) = msg.split(' ');

		'''
		ret = compare_url_path(url, path)
		'''
		ret = compare_url_md5(url, md5)
		if ret :
			print "succ:", url, path, md5
		else :
			print "failed:", url, path, md5


if __name__ == "__main__" :
	main()
