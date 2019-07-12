#pageCreator

def webCreator(pageName):
    # write-html.py
    fileName= pageName

    f = open('tuttlepower/' + fileName +'.html','w')

    #opens the head, which stores metadata, links to css and others
    g = open('tuttlepower\HTML\head.txt','r')

    #opens the header, which will include logo and top bar (content)
    h = open('tuttlepower/' + pageName+'/'+pageName+'Header.txt','r')

    #opens the body
    i = open('tuttlepower/' + pageName+'/'+pageName+'Body.txt','r')

    #opens the footer, which will hold scripts and close out the html
    j = open('tuttlepower/HTML/Footer.txt','r')

    #sets a string named head equal to all of the information in g, which is the Head
    head =(g.read())

    #sets a string named header equal to all of the information in h, which is the Header
    header =(h.read())

    #Sets the body to a string
    body =(i.read())

    #sets a string named footer equal to all of the information in i, which is the Footer
    footer = (j.read())

    message = head+header+body+footer

    f.write(message)
    f.close()

webCreator("index")
webCreator("Economics")
webCreator("Design")
webCreator("Politics")
webCreator("Programming")
webCreator("Timeline")
