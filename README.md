plugin.video.videoseeker
========================

XBMC Add-on that allows playlist/shortcut videos to be started at a designated offset time.

###Format

```
plugin://plugin.video.videoseeker/?offset=<Time_In_Seconds>&media=<URL_Encoded_XBMC_Media>
```

###Example

A .m3u playlist with two items, both YouTube videos, the first starts playing 3 minutes into the video and the second starts 2 minutes in.

```
#EXTM3U

#EXTINF:835, Understanding the Russian mindset 
plugin://plugin.video.videoseeker/?offset=180.0&media=plugin%3A%2F%2Fplugin.video.youtube%2Fplay%2F%3Fvideo_id%3DHE6rSljTwdU

#EXTINF:6422, The Transcontinental Railroad
plugin://plugin.video.videoseeker/?offset=120.0&media=plugin%3A%2F%2Fplugin.video.youtube%2Fplay%2F%3Fvideo_id%3D-kq1r27S5DU
```
