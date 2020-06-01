import requests
import re
from lxml import etree
from enc import n
from Crypto.Cipher import AES
import os
import shutil
import threading
import time


def get_course(url):
    response = requests.get(url)
    xpath = etree.HTML(response.text)
    for_xpath = xpath.xpath('//div[@class="course-info-main clearfix w"]')[0]

    title = xpath.xpath("/html/head/title/text()")[0].strip()
    data = {}
    data['title'] = title
    introduction = for_xpath.xpath('//div[@class="course-description course-wrap"]/text()')[0].strip()
    data['introduction'] = introduction
    chapter_xpath = for_xpath.xpath('//div[@class="chapter course-wrap "]')
    data['chapter'] = []

    for chapter_ in chapter_xpath:
        chapter_title = chapter_.xpath("h3/text()")[0].strip()
        chapter_descript = chapter_.xpath('div[@class="chapter-description"]/text()')[0].strip()
        course_name_list = chapter_.xpath('ul[@class="video"]//li[@data-media-id]/a[@class="J-media-item"]/text()')
        course_name_list = [i.strip().replace(" ","") for i in course_name_list if i.strip().replace(" ",'') != '']
        href_list = chapter_.xpath('ul[@class="video"]//li[@data-media-id]/a[@class="J-media-item"]/@href')
        chapter_content = [dict(title=n.replace("\n",""),href="https://www.imooc.com" + u) for n,u in zip(course_name_list,href_list)] 
        dict_ = dict(chapter_title=chapter_title,chapter_descript=chapter_descript,chapter_content=chapter_content)
        data['chapter'].append(dict_)
    return data

def del_no_ues(data):
    data = data.replace("['","").replace("']","")
    return data

def get_id(url):
    response = requests.get(url)
    id_ = re.findall('OP_CONFIG.mongo_id="(.*?)"',response.text)
    url = 'https://www.imooc.com/course/playlist/19975?t=m3u8&_id=%s&cdn=aliyun1' % id_
    return url

def get_key(key_url):
    response = requests.get(key_url)
    key = response.json()['data']['info']
    key = n(key,'1')
    return key

def get_video_clarity(url):
    url = get_id(url)
    response = requests.get(url)
    data = []
    for url in n(response.json()['data']['info'],'').split("\n")[2:]:
        if '#' in url:
            bindwidth,resolution = re.findall("BANDWIDTH=(.*?), RESOLUTION=(.*)",url)[0]
        else:
            url = del_no_ues(url)
            d = dict(bindwidth=bindwidth,resolution=resolution,url=url)            
            data.append(d)
    return data


def get_video_ts(url):
    response = requests.get(url)
    info = response.json()['data']['info']
    data = n(info,"")
    ts_list = []
    for t in data.split("\n"):
        if "#EXT-X-KEY:METHOD=AES-128" in t:
            key_url = del_no_ues(t.replace('#EXT-X-KEY:METHOD=AES-128,URI="','').replace('"',''))
        elif "#" not in t:
            ts_list.append(t)
    key = get_key(key_url)
    return ts_list,key

def download_ts(path,url,cryptor):
    data = requests.get(url).content
    with open(path,'wb') as f:
        f.write(cryptor.decrypt(data))

def hecheng(chapter_dir,name):
    os.chdir(chapter_dir)
    ts_list = os.listdir('.')
    num = len(ts_list)
    str_ = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc "../%s.mp4"' %(
              '|'.join([str(i)+".ts" for i in range(num)]),name)
    os.system(str_)
    os.chdir('../..')
    shutil.rmtree(chapter_dir)


def main(url):
    course_info = get_course(url)
    for chapter in course_info['chapter']:
        chapter_dir = chapter['chapter_title'].replace("/",'or')
        if not os.path.exists(chapter_dir):
            os.makedirs(chapter_dir)

        for course in chapter['chapter_content']:
            video_url = get_video_clarity(course['href'])[0]['url']
            ts_list,key = get_video_ts(video_url)
            cryptor = AES.new(key, AES.MODE_CBC,key)
            video_name = course['title'].replace("/",'or')
            thread_list = []
            if not os.path.exists(chapter_dir + '/' + video_name):
                os.makedirs(chapter_dir + '/' + video_name)

            for index,url in enumerate(ts_list):
                path = chapter_dir + '/' + video_name +'/' + str(index) + ".ts"
                download_ts(path,url,cryptor)

            hecheng(chapter_dir + '/' + video_name,video_name)


if __name__ == '__main__':
    url = 'https://www.imooc.com/learn/927'
    main(url)
