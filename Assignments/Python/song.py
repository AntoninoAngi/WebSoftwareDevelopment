import json


class Song:
    def __init__(self, id):
        self.id = id
        word = []
        word[:0] = id
        try:
            f = open("lastfm_subset/"+word[2]+"/"+word[3]+"/"+word[4]+"/" + id + ".json", "r")
            y = json.load(f)
            self.artist = y["artist"]
            self.timestamp = y["timestamp"]
            self.similars = y["similars"]
            self.tags = y["tags"]
            self.track_id = y["track_id"]
            self.title = y["title"]
        except:
            self.artist = "file"
            self.timestamp = "-1"
            self.similars = []
            self.tags = []
            self.track_id = id
            self.title = "not found"

    def get_tags(self, limit = 0):
        res = []
        for sublist in self.tags:
            if float(sublist[1]) >= limit:
                res.append(sublist[0])
        return res

    def get_similars(self, limit = 0):
        res = []
        for sublist in self.similars:
            if float(sublist[1]) >= limit:
                res.append(sublist[0])
        return res

    def shared_tags(self, otherSong):
        s1 = set([x[0] for x in self.tags])
        s2 = set([x[0] for x in otherSong.tags])

        return tuple (s1.intersection(s2))


    def combined_tags(self, otherSong):
        res = []
        for sublist in self.tags:
            res.append(sublist[0])
        for sublist in otherSong.tags:
            if sublist[0] not in res:
                res.append(sublist[0])
        return tuple(res)
