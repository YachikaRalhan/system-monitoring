



import glob, os,sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p','--path', type = str,required='true', help ='path of dir')
parser.add_argument('-f','--filetype', type = str,required='true', help ='type of file')
args = parser.parse_args()
os.chdir(args.path)

for file in glob.glob(args.filetype):
    print(file)
#print "This is the name of the script: ", sys.argv[0]
#print "The arguments are: " , str(sys.argv)

