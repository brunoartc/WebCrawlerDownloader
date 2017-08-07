import urllib.request as req
import re
import config
linksUteis=[]
linksFound=[]
inutil=config.inutil
util=config.util
linki=config.link
verbose=0
ddone=0
if (verbose>-1): print ("starting. This may take a while...")

def crawler(page, link):
    global ddone
    if (page.find("<title>Index of")!=-1):
        done,total=0,0
        for m in re.finditer("href=\"", page):
            total+=1
        done+=1
        if  (verbose>0): print("crawling ", link)
        for m in re.finditer("href=\"", page):



            if (page[m.end():].find("\"")<50 and page[m.end()]!="?" and page[m.end()]!="/"):

                if any(word in page[m.end():m.end()+page[m.end():].find("\"")] for word in inutil):
                    pass
                else:
                    if (verbose>0): print ("found href= ",page[m.end():m.end()+page[m.end():].find("\"")])
                    vlink = ''.join([link, page[m.end():m.end()+page[m.end():].find("\"")]])
                    linksFound.append(vlink)
                    vpage=""
                    if any(exte in page[m.end():m.end()+page[m.end():].find("\"")] for exte in util):
                        if (verbose>-1): print("found what you like " + page[m.end():m.end()+page[m.end():].find("\"")])
                        if (verbose>0): print("from " + vlink)
                        req.urlretrieve(vlink, "./files/" + page[m.end():m.end()+page[m.end():].find("\"")])
                        linksUteis.append(vlink)
                    else:
                        try:
                            if (verbose>0): print ("trying urlopen in= ",vlink)
                            vpage=str(req.urlopen(linksFound[-1]).read())
                            crawler(vpage,vlink)
                        except Exception as e:
                            if (verbose>0): print(e)
                        if (verbose>-1):
                            if (ddone<done/total*100): ddone=done/total*100
                            print (str(ddone) + "% done")
crawler(str(req.urlopen(linki).read()),linki)
if (verbose>-1): print(linksUteis)
if (verbose>-1): print(linksFound)
