import os
def getDir(directory):
    dirNames = os.listdir(directory) #获取目录下所有一层文件与文件夹名
    for dirName in dirNames:        #遍历每个文件
        dirName = directory + '/'+ dirName    #获取绝对路径
        if os.path.isfile(dirName):         #判断是否为文件，若是则直接输出
            print('[+]' + dirName)
        else:
            print('[-]' + dirName)          #若不是则继续深入遍历