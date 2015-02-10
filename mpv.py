import os

MPV = '/Applications/mpv.app/Contents/MacOS/mpv'

def isbd(path):
    index = os.path.join(path, 'index.bdmv')     # TODO does uppercase occur?
    return os.path.isfile(index)

def isdvd(path):
    _, ext = os.path.splitext(path)
    return ext.lower() == '.iso'

def execmpv(path):
    # TODO normalize https://github.com/mpv-player/mpv/issues/1027#issuecomment-72899151
    if isbd(path):
        path = os.path.dirname(path)
        args = ['bd://%i' % i for i in range(9)] + ['--bluray-device=%s' % path]
        os.execl(MPV, 'mpv', *args)
    elif isdvd(path):
        os.execl(MPV, 'mpv', 'dvd://', '--dvd-device=' + path)
    else:
        os.execl(MPV, 'mpv', path)

if __name__ == '__main__':
    import sys

    execmpv(sys.argv[1])
