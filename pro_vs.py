from moviepy.editor import *
import random
# import os
# import shutil


def get_clip_size(summary_length):
    return int(50/(15*60)*summary_length)


def get_summary_clips_seconds(vid_length, clip_size, summary_length):
    print('--> Calculating clips...')
    # diving seconds by clip_size
    div_seconds = []

    for vl in range(1, vid_length + 1, clip_size):
        div_seconds.append(vl)

    # calculations
    total_num_of_clips = len(div_seconds)
    num_of_clip_needed = int(summary_length/clip_size)
    num_of_clip_skip = int(total_num_of_clips / num_of_clip_needed)

    # getting summary clip seconds
    summa_clip_seconds = []

    for i in range(0, len(div_seconds), num_of_clip_skip):
        summa_clip_seconds.append(div_seconds[i])

    return summa_clip_seconds


def main(vid_path, summary_length, subclip=None):
    open_files = []

    video = VideoFileClip(vid_path)

    open_files.append(video)

    if subclip:
        video = video.subclip(subclip[0], video.duration - subclip[1])

    vid_length = int(video.duration)

    clip_size = get_clip_size(summary_length)

    summary_clip_seconds = get_summary_clips_seconds(
        vid_length,
        clip_size,
        summary_length
    )

    clips = []

    for second in summary_clip_seconds:
        if vid_length > second + clip_size:
            clip = video.subclip(second, second + clip_size)
            clips.append(clip)
            open_files.append(clip)

    final = concatenate_videoclips(clips)
    final = final.without_audio()

    final.write_videofile('a.mp4')



