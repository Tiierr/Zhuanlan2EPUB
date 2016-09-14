# coding:utf8
import sys
from html2epub import html2epub

reload(sys)
sys.setdefaultencoding('utf8')

sys.getdefaultencoding()

if __name__ == '__main__':
    path = 'papers'
    ToPath = path + '_epub'
    zh = html2epub(path, ToPath)
    zh.start()
