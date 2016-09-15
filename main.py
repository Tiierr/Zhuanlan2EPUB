# coding:utf8
import sys
from toEpub import html2epub

reload(sys)
sys.setdefaultencoding('utf8')

sys.getdefaultencoding()

def start_transfer():
    path = 'papers'
    ToPath = path + '_epub'
    zh = html2epub(path, ToPath)
    zh.start()
