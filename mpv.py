import os

from moreplistlib import getkind

MPV = '/Applications/mpv.app/Contents/MacOS/mpv'

def execmpv(path):
    kind = getkind(path)
    if kind == 'AVCHD Collection':
        path = os.path.dirname(path)
        os.execl(MPV, 'mpv','bd://1', 'bd://2', 'bd://3', 'bd://4', '--bluray-device=' + path)
    elif kind == 'ISO Disk Image':
        os.execl(MPV, 'mpv', 'dvd://', '--dvd-device=' + path)
    else:
        os.execl(MPV, 'mpv', path)

if __name__ == '__main__':
    import sys

    execmpv(sys.argv[1])
