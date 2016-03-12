#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PostRequest:
    def __init__(self, xml):
        self.touser = xml.find('ToUserName').text
        self.fromuser = xml.find('FromUserName').text
        self.createtime = xml.find('CreateTime').text
        self.msgtype = xml.find('MsgType').text
        self.msgid = xml.find('MsgId').text


class TextPostRequest(PostRequest):
    def __init__(self, xml):
        PostRequest.__init__(self, xml)
        self.content = xml.find('Content').text


class ImagePostRequest(PostRequest):
    def __init__(self, xml):
        PostRequest.__init__(self, xml)
        self.picurl = xml.find('PicUrl').text
        self.mediaid = xml.find('MediaId').text


class VoicePostRequest(PostRequest):
    def __init__(self, xml):
        PostRequest.__init__(self, xml)
        self.mediaid = xml.find('MediaId').text
        self.format = xml.find('Format').text


class RecVoicePostRequest(VoicePostRequest):
    def __init__(self, xml):
        VoicePostRequest.__init__(self, xml)
        self.recognition = xml.find('Recognition').text


class VideoPostRequest(PostRequest):
    def __init__(self, xml):
        PostRequest.__init__(self, xml)
        self.mediaId = xml.find('MediaId').text
        self.thumbmediaid = xml.find('ThumbMediaId').text


class LoactionPostRequest(PostRequest):
    def __init__(self, xml):
        PostRequest.__init__(self, xml)
        self.locationx = xml.find('Location_X').text
        self.locationy = xml.find('Location_Y').text
        self.scale = xml.find('Scale').text
        self.label = xml.find('Label').text


class LinkPostRequest(PostRequest):
    def __init__(self, xml):
        PostRequest.__init__(self, xml)
        self.title = xml.find('Title').text
        self.description = xml.find('Description').text
        self.url = xml.find('Url').text


class EventPostRequest(PostRequest):
    def __init__(self, xml):
        PostRequest.__init__(self, xml)
        self.event = xml.find('Event').text


class ScanEventPostRequest(EventPostRequest):
    def __init__(self, xml):
        EventPostRequest.__init__(self, xml)
        self.eventkey = xml.find('EventKey').text
        self.ticket = xml.find('Ticket').text


class LocationEventPostRequest(EventPostRequest):
    def __init__(self, xml):
        EventPostRequest.__init__(self, xml)
        self.latitude = xml.find('Latitude').text
        self.longitude = xml.find('Longitude').text
        self.precision = xml.find('Precision').text


class MenuEventPostRequest(EventPostRequest):
    def __init__(self, xml):
        EventPostRequest.__init__(self, xml)
        self.eventkey = xml.find('EventKey').text

