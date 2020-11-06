# coding=UTF-8
import  getopt
import  sys
import  os
import  re
import errno

## 获取参数
newdict=[]

def gci(filepath):
#遍历filepath下所有文件，包括子目录
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)
    # #isdir和isfile参数必须跟绝对路径
    if os.path.isdir(fi_d):
      gci(fi_d)
    else:
      newdict.append(fi_d)
  return  newdict




def autodir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def write(dirname,orfile,nocap):  ##目录名同时作为函数名来进行导入

    f1 = open(orfile)
    content = f1.read()
    newfilepath=dirname+"/"+orfile.split("/")[2]
    print  newfilepath
    autodir(newfilepath)
    with open(newfilepath, 'w') as f:
        if  nocap:
            f.write(content.format(a=dirname))
        else:
            print dirname.capitalize()
            f.write(content.format(a=dirname.capitalize()))


def  gen():
    clname = sys.argv[1]
    dict=gci("viewsettemp/")
    for i in dict:#
      if  "apps.py" in i:
                write(clname,i,True)
      else:
            write(clname, i, False)



#print(gci("./temp/"))

gen()


##使用方法  autoviewset.py +目录名  根据目录名生成类名    写入后需手动到setting installapp





