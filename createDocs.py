#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
import markdown
import os
import io

reviewsDir = "../hugo/sample/"
documentTitle = "Movie Reviews by Steve Mookie Kong"
finalDocumentFile = "../movie-reviews-all.html"

def create_header(documentTitle):
    header = "<html><head><title>" + documentTitle + "</title></head><body>"
    return(header)

def create_footer():
    footer = "</body></html>"
    return(footer)

def create_review(file):
    with open(file,"r") as mdfile:
        mytext = mdfile.read()
        mysections = mytext.split('---')

    header = mysections[1]
    body = mysections[2]

    meta = yaml.safe_load(header)

    reviewTitle = meta['title'] + " (" + str(meta['release_year']) + ")"
    reviewDate = meta['date'].strftime("%B %d, %Y")

    bodyNoPics = "<h1 id=\"Movie Title\">" + reviewTitle + "</h1>\n"
    bodyNoPics = bodyNoPics + "<p id=\"Review Publication Date\"><small><b>" + reviewDate + "</b></small></p>\n"

    if('rating' in meta):
        movieRating = "<b>" + str(meta['rating']) + "</b><i> out of 10</i>"
        bodyNoPics = bodyNoPics + "<p id=\"Review Rating\"><small>" + movieRating + "</small></p>\n"

    for line in body.split("\n"):
        if (not line.startswith("![")):
            bodyNoPics = bodyNoPics + line + "\n"

    bodyNoPics = bodyNoPics + "<br style=\"page-break-before: always\">"
    bodyHtml = markdown.markdown(bodyNoPics)
    return(bodyHtml)
    
def writeFinalDocument(finalDocumentFile,finalDocument):
    #doc = open(finalDocumentFile,"w")
    #doc.write(finalDocument)
    #doc.close()
    with io.open(finalDocumentFile,"w",encoding='utf-8-sig') as outputDoc:
        outputDoc.write(finalDocument)
        outputDoc.close()

def main():

    documentHeader = create_header(documentTitle)
    documentFooter = create_footer()

    documentBody = ""
    for file in os.listdir(reviewsDir):
        documentBody = documentBody + create_review(reviewsDir + file)

    finalDocument = documentHeader + documentBody + documentFooter

    writeFinalDocument(finalDocumentFile,finalDocument)

if __name__ == "__main__":
    main()
