import requests
import re
import json
from datetime import datetime
import isodate

class MoviePreview():
    def __init__(self,imdbID,name,year,picture):
        self.imdbID = imdbID
        self.name = name
        self.year = year
        self.picture = picture

    def __str__(self):
        return "(id : "+self.imdbID+", name : "+self.name + ", year : "+self.year+", picture "+self.picture+")"



class Movie():
    def __init__(self,title,year,contentRating,released,duration,genre,directors,creators,actors,plot,image,metascore,imdbRating,imdbVotes,imdbID,typeMedia,keywords):
        self.title = title
        self.year = year
        self.contentRating = contentRating
        self.released = released
        self.duration = duration
        self.genre = genre
        self.directors = directors
        self.creators = creators
        self.actors = actors
        self.plot = plot
        self.image = image
        self.metascore = metascore
        self.imdbRating = imdbRating
        self.imdbVotes = imdbVotes
        self.imdbID = imdbID
        self.type = typeMedia
        self.keywords = keywords

    def __str__(self):
        dic = self.__dict__
        return "(" + ", ".join([ str(k) + " : " + str(dic[k]) for k in dic]) + ")"

class IMDb():

    __url = "https://www.imdb.com/"
    def search(self,query,limit=0):
        result = []
        resQuery = requests.get(self.__url+"find?q="+query.replace(" ","+")+"&s=tt&ttype=ft") # can add "&exact=true" for restricted results
        groups = re.findall(r'<tr class="findResult.*?href="\/title\/(?P<id>.*?)\/.*?<img src="(?P<img>.*?)".*?<a href=".*?>(?P<title>.*?)<\/a>.*?\((?P<year>.*?)\)',resQuery.text, flags=re.I|re.M|re.U|re.S)
        
        if(limit != 0):
            groups = groups[:limit] 
        
        for group in groups:
            img = group[1].replace("._V1_UX32_CR0,0,32,44_AL_","")
            result.append(MoviePreview(group[0],group[2],group[3],img))

        return result
    
    
    def infoMovie(self,imdbID):
        result = None
        resQuery = requests.get(self.__url+"title/"+imdbID+"/")
        searchResult = re.search(r'<script type="application\/ld\+json">(?P<json>.*?)<\/script>',resQuery.text, flags=re.I|re.M|re.U|re.S|re.U)
        if searchResult:
            jsonText = searchResult.group("json")
            jsonObject = json.loads(jsonText)

            story = re.findall(r'id="titleStoryLine".*?class="inline canwrap".*?<span>(?P<metacritique>.*?)<\/span>',resQuery.text, flags=re.I|re.M|re.U|re.S|re.U)
            infoMetascore = re.findall(r'class="metacriticScore score_favorable titleReviewBarSubItem">\s*?<span>(?P<metacritique>.*?)<\/span>',resQuery.text, flags=re.I|re.M|re.U|re.S|re.U)
            
            actors = []
            if("actor" in  jsonObject):
                if( isinstance(jsonObject["actor"],list)):
                    for actor in jsonObject["actor"]:
                        actors.append(actor["name"])
                else:
                    actors.append(jsonObject["actor"]["name"])
            #Json in imdb was bad ( duplicate name )
            actors = list(set(actors))

            directors = []
            if("director" in  jsonObject):
                if( isinstance(jsonObject["director"],list)):
                    for director in jsonObject["director"]:
                        directors.append(director["name"])
                else:
                    directors.append(jsonObject["director"]["name"])
            #Json in imdb was bad ( duplicate name )
            directors = list(set(directors))

            creators = []
            if("creator" in  jsonObject):
                if( isinstance(jsonObject["creator"],list)):
                    for creator in jsonObject["creator"]:
                        if("name" in creator):
                            creators.append(creator["name"])
                else:
                    directors.append(jsonObject["creator"]["name"])
            #Json in imdb was bad ( duplicate name )
            creators = list(set(creators))


            result= Movie(title=jsonObject["name"] if "name" in jsonObject else "N/A",
                        year=jsonObject["datePublished"][:4] if "datePublished" in jsonObject else "N/A",
                        contentRating=jsonObject["contentRating"] if "contentRating" in jsonObject else "N/A",
                        released=jsonObject["datePublished"] if "datePublished" in jsonObject else "N/A",
                        duration=str( isodate.parse_duration(jsonObject["duration"])) if "duration" in jsonObject else "N/A",
                        genre=jsonObject["genre"] if "genre" in jsonObject else "N/A",
                        directors=directors,
                        creators=creators,
                        actors=actors,
                        plot=story[0][1:-1].strip() if len(story) > 0 else "N/A",
                        image=jsonObject["image"] if "image" in jsonObject else "N/A",
                        metascore= infoMetascore[0] if len(infoMetascore) > 0 else "N/A",
                        imdbRating=jsonObject["aggregateRating"]["ratingValue"] if "aggregateRating" in jsonObject else "N/A",
                        imdbVotes=jsonObject["aggregateRating"]["ratingCount"] if "aggregateRating" in jsonObject else "N/A",
                        imdbID=imdbID,
                        typeMedia=jsonObject["@type"] if "@type" in jsonObject else "N/A" ,
                        keywords=jsonObject["keywords"].split(",") if "keywords" in jsonObject else "N/A" )
        return result      




# if __name__ == "__main__":
#     db = IMDb()

#     research = db.search("Aveng",limit=6) # recherche les films Aveng dans imdb 
#     # si recherche illimité, retire limit=
#     print(" Research Aveng")
#     for k in research:
#         print(k)


#     result = db.infoMovie("tt4649466") # Avengers endgame

#     if(result != None):
#         print("\nInfo about Avengers endgame")
#         print(result)

#         #pour obtenir un json :
#         a = json.dumps(result.__dict__)
#         print(a)
#         # si tu veux le traiter comme un dictionnaire
#         a = result.__dict__




