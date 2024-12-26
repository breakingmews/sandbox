#!/bin/sh
# Removes silence from the beginning and end of audio files

source_folder="$1"

cd "$source_folder" || exit

target_folder="$(pwd)_trimmed"
mkdir -p "$target_folder"

echo "Removing silence from audio files in $source_folder and saving them in $target_folder"

for i in *.mp3;
    do name=`echo "$i" | cut -d'.' -f1`
    echo "$name"
    ffmpeg -i "$i" -af "silenceremove=start_periods=1:start_duration=1:start_threshold=-60dB:detection=peak,aformat=dblp,areverse,silenceremove=start_periods=1:start_duration=1:start_threshold=-60dB:detection=peak,aformat=dblp,areverse" "${target_folder}/${name}.mp3"
done
