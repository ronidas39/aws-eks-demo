import yaml,io,glob,os,sys
from yaml.loader import SafeLoader

# Open the file and load the file
with io.open("files.txt","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()

lines=data.split("\n")
pwd=os.getcwd()
files=glob.glob(pwd+"/*.yaml")

for file in files:
    if file.split("/")[-1] in lines:
        print(f"{file.split('/')[-1]} is ok ")

    else:
        print(f"{file.split('/')[-1]} is invalid file")
        sys.exit()

with io.open("parser_ok.txt","w",encoding="utf-8") as f1:
    f1.write("ok")
    f1.close()