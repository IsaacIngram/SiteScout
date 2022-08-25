import validators, requests

class Webpage:

    def __init__(self, url):
        self.url = url

    # Set the URL of this webpage
    def setUrl(self, newUrl):
        self.url = newUrl

    # Get the URL of this webpage
    def getUrl(self):
        return self.url

    # Check whether the URL of this webpage is valid
    def validateUrl(self):
        return validators.url(self.url)

    # Get the HTML content of this webpage. Returns None if URL is invalid
    def getHtml(self):
        if self.validateUrl():
            return requests.get(self.url).text
        else:
            print("Error: Webpage getHtml method run on invalid URL!")
            print("Tip: Below error messages might be because of this.")
            return None

    # Get a specific line from the HTML file for this webpage
    def getLine(self, line):
        return self.getHtml().splitlines()[line]

    # Get a list of line numbers for lines that contain the given content
    def getLinesFromContent(self, content):
        html = self.getHtml()
        listOfLines = []

        i = 0
        while i < len(html.splitlines()):
            if content in html.splitlines()[i]:
                listOfLines.append(i+1)
            i = i+1
        return listOfLines

    # Gets content for a given attribute on a specific line
    def getAttributeContentFromLine(self, line, attributeName):
        html = self.getHtml()

        lengthOfTag = len(attributeName)
        lineText = html.splitlines()[line-1]

        tagStartIndex = lineText.find(attributeName)

        # Return an empty string since the htmlTag does not exist on this line
        if tagStartIndex < 0:
            return ""

        openQuoteIndex = -1
        closeQuoteIndex = -1

        i = tagStartIndex+lengthOfTag
        while i < len(lineText):
            if lineText[i] == '"':
                if openQuoteIndex < 0:
                    openQuoteIndex = i
                elif closeQuoteIndex < 0:
                    closeQuoteIndex = i
                    break
                else:
                    break
            i = i+1

        return lineText[openQuoteIndex+1:closeQuoteIndex]

    def getTagContentFromLine(self, line, tag):
        
        

