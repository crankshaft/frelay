import os
import sys
import time
import httplib

def post_file(body, dest) :
	parse = dest.split('/')
	http = httplib.HTTPConnection(parse[2], timeout=60)
	http.request(method='POST', url='/'+'/'.join(parse[3:]), body=body)
	ret = http.getresponse()

	if (int(ret.status) == 201) :
		return True
	else :
	 return False

def relay_file(path, dst) :
	try :
		if path[0:7] == "http://" :
			body = "asdf"
		else :
			if not os.path.exists(path) :
				return False
			with open(path, 'r') as f:
				body = f.read()
		if not body :
			return False

		if dst[0:7] == "http://" :
			return post_file(body, dst)
		else :
			return False
	except :
		return False


def main() :

	while True:
		try:
			line = sys.stdin.readline()
			if not line :
				print "stop"
				break
			path = line.strip('\r\n ')
			if not path :
				continue
		except :
			return

		ret = relay_file(path, "http://localhost:8080/"+os.path.split(path)[1])
		if ret :
			print "succ:", path
		else :
			print "failed:", path


if __name__ == "__main__" :
	main()
