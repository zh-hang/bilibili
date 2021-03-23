import scrapy
import re
import json


class VideoSpider(scrapy.Spider):
    name = 'video'
    start_urls = ['http://api.bilibili.com/x/web-interface/view?aid=' + str(i * 43 + i * 11) for i in
                  range(1, 10000000)]
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }

    def parse(self, response):
        video_info = json.loads(response.text)
        if video_info['code'] == 0:
            yield {'aid': video_info['data']['stat']['aid'],'tid':video_info['data']['tid'], 'view': video_info['data']['stat']['view'],
                   'danmaku': video_info['data']['stat']['danmaku'], 'reply': video_info['data']['stat']['reply'],
                   'favorite': video_info['data']['stat']['favorite'], 'coin': video_info['data']['stat']['coin'],
                   'share': video_info['data']['stat']['share'], 'like': video_info['data']['stat']['like']}
