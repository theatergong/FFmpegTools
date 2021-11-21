import os
import re

os.system("clear")
os.system("figlet FFmpegTools")
number = int(input('''
1-获取视频信息
2-下载m3u8链接
3-录制直播源
4-删除视频中的音频
5-转换视频格式
6-视频压H264与H265编码
7-提取视频中的音频文件
8-调整视频尺寸(分辨率)
9-光流法补帧60FPS
10-视频本体倒放
11-视频中音频倒放
12-退出\n
输入：'''))
if number == 1:
    os.system("clear")
    one = str(input("请输入视频文件(带后缀)："))
    cmd = 'ffmpeg -i "%s"' %(one)
    os.system(cmd)
if number == 2:
    os.system("clear")
    m3u8 = str(input("请输入m3u8链接："))
    name = str(input("请输入视频保存名称(带路径，带后缀)："))
    threads = str(input("请输入线程："))
    cmd = 'ffmpeg -threads %s -i "%s" -vcodec copy -acodec copy "%s"' %(threads, m3u8, name)
    os.system(cmd)
if number == 3:
    os.system("clear")
    m3u8 = str(input("请输入m3u8直播源："))
    name = str(input("请输入视频保存名称(带路径，带后缀)："))
    cmd = 'ffmpeg -i "%s" -c copy "%s"' %(m3u8, name)
    os.system(cmd)
if number == 4:
    os.system("clear")
    one = str(input("请输入视频文件(带后缀)："))
    two = one.replace(".","_new.")
    cmd = 'ffmpeg -i "%s" -an "%s"' %(one, two)
    os.system(cmd)
if number == 5:
    os.system("clear")
    print("支持视频格式如下：")
    os.system("ffmpeg -formats")
    one = str(input("请输入视频文件(带后缀)："))
    two = str(input("请输入视频格式(例如mp4)："))
    type = one.split(".")[-1]
    three = one.replace(type,two)
    cmd = 'ffmpeg -i "%s" -qscale 0 "%s"' %(one, three)
    os.system(cmd)
if number == 6:
    os.system("clear")
    coding = str(input("请输入压制编码(264或265)："))
    print("Crf值越大，画质越差，文件越小  ——  (范围0-51)")
    crf = str(input("请输入Crf值："))
    one = str(input("请输入视频文件(带后缀)："))
    two = one.replace(".","_new.")
    cmd = 'ffmpeg -i "%s" -c:v libx%s -crf %s -c:a copy "%s"' %(one, coding, crf, two)
    os.system(cmd)
if number == 7:
    os.system("clear")
    one = str(input("请输入视频文件(带后缀)："))
    two = one.replace(".","_new.")
    cmd = 'ffmpeg -i "%s" -vn -acodec copy "%s"' %(one, two)
    os.system(cmd)
if number == 8:
    os.system("clear")
    print("尺寸大小 —— 例如 1280:720")
    size = str(input("请输入尺寸大小："))
    one = str(input("请输入视频文件(带后缀)："))
    two = one.replace(".","_new.")
    cmd = 'ffmpeg -i "%s" -filter:v scale=%s -c:a copy "%s"' %(one, size, two)
    os.system(cmd)
if number == 9:
    os.system("clear")
    one = str(input("请输入视频文件(带后缀)："))
    two = one.replace(".","_new.")
    cmd = 'ffmpeg -y -hide_banner -i "%s" -filter_complex "[0:v]scale=-2:-2[v];[v]minterpolate="mi_mode=mci:mc_mode=aobmc:me_mode=bidir:mb_size=16:vsbmc=1:fps=60"" -max_muxing_queue_size 1024  "%s" && am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE  -d "file://"%s""' %(one, two, two)
    os.system(cmd)                
if number == 10:
    os.system("clear")
    one = str(input("请输入视频文件(带后缀)："))
    two = one.replace(".","_new.")
    cmd = 'ffmpeg -y -hide_banner -i "%s" -vf reverse -af areverse  "%s" && am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE  -d "file://"%s""' %(one, two, two)
    os.system(cmd)
if number == 11:
    os.system("clear")
    one = str(input("请输入视频文件(带后缀)："))
    two = one.replace(".","_new.")
    cmd = 'ffmpeg -y -hide_banner -i "%s" -af areverse  "%s" && am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE  -d "file://"%s""' %(one, two, two)
    os.system(cmd)
if number == 12:
    print("程序已退出！")
    exit()
