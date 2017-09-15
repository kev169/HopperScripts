from os.path import exists, expanduser, split
import os
from os import makedirs

doc = Document.getCurrentDocument()
seg = doc.getCurrentSegment()

# get proc count
procCount = seg.getProcedureCount()
homeDir = expanduser("~")
head, appName = split(doc.getExecutableFilePath())
path = homeDir + '/hopperDumps/' + appName + '.c'
path2 = homeDir + '/hopperDumps/'
if not exists(path2):
	makedirs(path2)

print("[+] Generating nocode output for : %s/%s to %s"%(head, appName, path))
os.system("~/tools/bins/nocode %s/%s > %s"%(head, appName, path))
print "[*] nocode export complete. Export located at: %s" % (path)
