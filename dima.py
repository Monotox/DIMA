#!/usr/bin/env pyhon
# -*- coding: utf-8 -*-
import requests, sys, urllib, random, zipfile, os

def Setup():
	print "\n\n"
	print "  _____                      _                 _   _____                            "
	print " |  __ \                    | |               | | |_   _|                           "
	print " | |  | | _____      ___ __ | | ___   __ _  __| |   | |  _ __ ___   __ _ _   _ _ __ "
	print " | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |   | | | '_ ` _ \ / _` | | | | '__|"
	print " | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  _| |_| | | | | | (_| | |_| | |   "
	print " |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| |_____|_| |_| |_|\__, |\__,_|_|   "
	print "          |  \/  |                   /\   | | |                     __/ |           "
	print "          | \  / | __ _ ___ ___     /  \  | | |__  _   _ _ __ ___  |___/            "
	print "          | |\/| |/ _` / __/ __|   / /\ \ | | '_ \| | | | '_ ` _ \                  "
	print "          | |  | | (_| \__ \__ \  / ____ \| | |_) | |_| | | | | | |                 "
	print "          |_|  |_|\__,_|___/___/ /_/    \_\_|_.__/ \__,_|_| |_| |_|                 "
	print "\n\n"
	print "\n\n\n\nUso: python dima.py lista.txt\n"

def Mod():
	archive = open(sys.argv[1], 'r')
	for line in archive:
		split=line.split('\n')
		url = "".join(split)+"/zip"
		name = random.randrange(1, 1000)
		url_name=str(name)+'.zip'
		urllib.urlretrieve(url,url_name)
		print "\033[37;40m[D.I.M.A] \033[32;40mArchive download\033[37;40m:",url,"\033[32;40mArchive:\033[37;40m",url_name
		zip = zipfile.ZipFile(url_name)
		zip.extractall()
		print "[D.I.M.A] \033[32;40mArchive unzipped:\033[37;40m",url_name


if len(sys.argv) < 2:
	Setup()
	sys.exit()
else:
	Mod()
