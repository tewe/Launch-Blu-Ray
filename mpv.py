import os

MPV = '/Applications/mpv.app/Contents/MacOS/mpv'

def isbd(path):
    index = os.path.join(path, 'index.bdmv')     # TODO does uppercase occur?
    return os.path.isfile(index)

def isdvd(path):
    _, ext = os.path.splitext(path)
    return ext.lower() == '.iso'

def execmpv(path):
    if isbd(path):
        path = os.path.dirname(path)
        os.execl(MPV, 'mpv','bd://1', 'bd://2', 'bd://3', 'bd://4', '--bluray-device=' + path)
    elif isdvd(path):
        os.execl(MPV, 'mpv', 'dvd://', '--dvd-device=' + path)
    else:
        os.execl(MPV, 'mpv', path)

if __name__ == '__main__':
    import sys

    execmpv(sys.argv[1])
