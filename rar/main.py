import os
import sys

from unrar import rarfile


def rar_cracking(filename):
    fp = rarfile.RarFile('test.rar')
    fpPwd = open('pwd.txt')
    for pwd in fpPwd:
        pwd = pwd.rstrip()
        try:
            fp.extractall(path='test', pwd=pwd.encode())
            print('[+] Find the password: ' + pwd)
            fp.close()
            break
        except:
            pass
    fpPwd.close()


if __name__ == '__main__':
    filename = sys.argv[1]
    if os.path.isfile(filename) and filename.endswith('.rar'):
        rar_cracking(filename)
    else:
        print('Not a rar file')

