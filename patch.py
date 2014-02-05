import plistlib
import sys

root = plistlib.readPlist(sys.argv[1])
for t in root['CFBundleDocumentTypes']:
    if 'CFBundleTypeExtensions' in t:
        del t['CFBundleTypeExtensions']
        t['LSItemContentTypes'] = ['public.avchd-collection', 'public.iso-image']
plistlib.writePlist(root, sys.argv[1])      # Overwrites!
