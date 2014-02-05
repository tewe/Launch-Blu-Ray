MPV="/Applications/mpv.app/Contents/MacOS/mpv"

UTI=`/usr/bin/mdls -name kMDItemContentType -raw "$1"`

case "$UTI" in
	( "public.iso-image" ) $MPV dvd:// --dvd-device="$1" ;;
	( "public.avchd-collection" ) $MPV bd://1 bd://2 bd://3 bd://4 --bluray-device="`dirname "$1"`" ;;
	( * ) MPV "$1" ;;
esac
