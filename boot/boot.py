#!/usr/bin/env python

import os, json
import urllib2
import yaml

import vocabcompiler

def configure():
    print "COMPILING DICTIONARY"
    vocabcompiler.compile("../client/sentences.txt", "../client/dictionary.dic", "../client/languagemodel.lm")

    print "STARTING CLIENT PROGRAM"
    os.system("/home/pi/jasper/client/start.sh &")

if __name__ == "__main__":
    print "==========STARTING JASPER CLIENT=========="
    print "=========================================="
    print "COPYRIGHT 2013 SHUBHRO SAHA, CHARLIE MARSH"
    print "=========================================="
    configure()
