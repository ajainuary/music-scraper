#!/bin/sh
./Apple_Music_Playlist.py > list.txt
youtube-dl --config-location youtube-dl.conf -a list.txt
rm list.txt