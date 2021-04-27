#!/usr/bin/env python
#
# 
#
# dom-brute.py - Bruteforce as many TLD's as possible for a prefix.
#
# By @RandomRobbieBF
# 
#

import requests
import sys
import argparse
import os.path
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
session = requests.Session()



parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="ext.txt",required=False, help="File of TLD's")
parser.add_argument("-p", "--prefix", default="",required=True, help="Prefix of Domain")


args = parser.parse_args()
urls = args.file
prefix = args.prefix



def grab_file (URL,prefix,suffix):
	print ("[*] Testing: "+URL+"\n")
	try:
		
		
		headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"}
		response = session.get(URL, headers=headers, timeout=10, verify=False)
		result = response.text
		try:
			if response.status_code == 200:
				text_file = open(""+prefix+"-domains-200.txt", "a")
				text_file.write(""+URL+"\n")
				text_file.close()
				
			else:
				text_file1 = open(""+prefix+"-domains-non-200.txt", "a")
				text_file1.write(""+URL+"\n")
				text_file1.close()
					
			print ("[*] Alive TLD: "+suffix+" [*]\n ")
		except Exception as e:
			#print (str(e))		
			print ("[*] Dead TLD: "+suffix+" [*]\n ")
			
			
	except Exception as e:
		#print (e)
		print ("[*] Dead TLD: "+suffix+" [*]\n ")
	


if os.path.exists(urls):
		with open(urls, 'r') as f:
			for line in f:
				suffix = line.replace("\n","")
				try:
					URL = "http://"+prefix+"."+suffix+""
					grab_file (URL,prefix,suffix)
					os.system("docker run --rm -v $(pwd):/data leonjza/gowitness gowitness file -f data/"+prefix+"-domains-200.txt")
				except KeyboardInterrupt:
					print ("Ctrl-c pressed ...")
					sys.exit(1)
				except Exception as e:
					print('Error: %s' % e)
					pass
		f.close()
