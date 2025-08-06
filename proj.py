def inter(url):
    import re
    import linkGrabber
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen as uReq
    import urllib.error
    from openpyxl import Workbook
    book = Workbook()
    sheet = book.active
    links = linkGrabber.Links(url)
    gb = links.find(limit = 1000, duplicate =False, href= re.compile("^/store/apps/details"))
    sd=[]
    for x in range(0,len(gb)):
        sd.append(gb[x].get('href'))
        b=dict.fromkeys(sd)
    #print(list(b.keys()))
    li = list(b.keys())

    for i in range(0, len(li)) :
        li[i] = 'https://play.google.com' + li[i]
    x=0
    while(x<len(li)):
        my_url=li[x]
        try:
            conn = urllib.request.urlopen(my_url)
        except urllib.error.HTTPError as e:
            x=x+1
        except urllib.error.URLError as e:
            x=x+1
        else:

            uClient=uReq(my_url)
            page_html=uClient.read()
            uClient.close()
            page_soup=soup(page_html,'html.parser')
            containers=page_soup.findAll("div",{"class":"JNury Ekdcne"})
            container=containers[0]
            title=container.findAll("h1",{"class":"AHFaub"})
            Developer=container.findAll("a",{"class":"hrTbp R8zArc"})
            Developer=container.findAll("a",{"class":"hrTbp R8zArc"})
            rating=container.findAll("div",{"class":"BHMmbe"})
            but=container.findAll("span",{"class":"oocvOe"})
            desc=container.findAll("div",{"class":"DWPxHb"})
            containers2=page_soup.findAll("div",{"class":"IxB2fe"})
            container2=containers2[0]
            attr=container2.findAll("div",{"class":"IQ1z0d"})

            if(len(rating)==0):
                a=title[0].text
                b=Developer[0].text
                c=Developer[1].text
                d='-'
                if (len(attr[0].text) > 18):
                    e = attr[1].text
                    k = attr[2].text
                    g = attr[3].text
                    h = attr[4].text
                    i = attr[5].text
                else:
                    e = attr[0].text
                    k = attr[1].text
                    g = attr[2].text
                    h = attr[3].text
                    i = attr[4].text
            elif(len(but)==0 or but[0].text=='Install'):
                a=title[0].text
                b=Developer[0].text
                c=Developer[1].text
                d=rating[0].text
                e=attr[0].text
                k=attr[1].text
                g=attr[2].text
                h=attr[3].text
                i=attr[4].text
            elif(len(rating)==0 and len(but)==0):
                a=title[0].text
                b=Developer[0].text
                c=Developer[1].text
                d='-'
                e=attr[1].text
                k=attr[2].text
                g=attr[3].text
                h=attr[4].text
                i=attr[5].text
            else:
                a=title[0].text
                b=Developer[0].text
                c=Developer[1].text
                d=rating[0].text
                e=attr[1].text
                k=attr[2].text
                g=attr[3].text
                h=attr[4].text
                i=attr[5].text

            
            if(x==0):
                head=('App','Developer','Category','Rating','Updated','Size','Installs','Current Version')
                sheet.append(head)
            row = (a ,b,c,d,e,k,g,h)
            sheet.append(row)
            x=x+1

    book.save("cat.xlsx")
