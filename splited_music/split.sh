#!/bin/bash
segment=5 # 每段音频的长度，单位为秒
start_offset=20 # 开头不需要的部分，单位为秒
end_offset=20 # 结尾不需要的部分，单位为秒

for input in *.wav; do
    duration=$(ffmpeg -i "$input" 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,//)
    length=$(echo "$duration" | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }' | cut -d '.' -f 1)
    output_dir="${input%.*}"
    mkdir "$output_dir"
    counter=1
    for ((start=start_offset; start<$length-end_offset; start+=$segment)); do
        ffmpeg -i "$input" -ss "$start" -t "$segment" -acodec copy "${output_dir}/${counter}.wav"
        echo "裁剪音频：${output_dir}/${counter}.wav"
        counter=$((counter+1))
    done
    rm "$input"
    echo "删除原音频文件：$input"
done
