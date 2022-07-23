#!/usr/bin/python

def fileread(filename):
    result = []
    try:
            inputfile = open(filename, 'r')
    except IOError:
        print "[ERROR ] - File not found [" + filename + "]"
        return " File not found "

    for item in inputfile:
        result.append(item)
    inputfile.close()
    return result
print "[INFO  ] - Starting [Main Process]"
print "2of4brif            : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/2of4brif.txt'))
print "2of12               : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/2of12.txt'))
print "3esl                : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/3esl.txt'))
print "5desk               : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/5desk.txt'))
print "6of12               : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/6of12.txt'))
print "500-worst-passwords : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/500-worst-passwords.txt'))
print "agid                : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/agid.txt'))
print "cain                : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/cain.txt'))
print "conficker           : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/conficker.txt'))
print "john                : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/john.txt'))
print "neol2007            : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/neol2007.txt'))
print "passwords           : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/passwords.txt'))
print "twitter-banned      : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/twitter-banned.txt'))
print "words               : " ,len(fileread('/Users/denisjackman/Documents/workspace/CodeAcademy/dicts/words'))
print "[INFO  ] - Finishing [Main Process]"
