import validators, requests


class Webpage:

    def __init__(self, url):
        self.url = url

    def set_url(self, newUrl):
        """
        Set the URL for this webpage
        :param newUrl: The new URL
        :return:
        """
        self.url = newUrl

    def get_url(self):
        """
        Get the URL for this webpage
        :return: The URL of this webpage
        """
        return self.url

    def validate_url(self):
        """
        Check whether the URL of this webpage is valid
        :return: Whether the URl of this webpage is valid as a boolean
        """
        return validators.url(self.url)

    def get_html(self):
        """
        Get the HTML contents of this webpage.
        :return: The HTML contents of this webpage. Returns NoneType if the URL is invalid.
        """
        if self.validate_url():
            return requests.get(self.url).text
        else:
            print("Error: Webpage getHtml method run on invalid URL!")
            print("Tip: Below error messages might be because of this.")
            return None

    def get_line(self, line):
        """
        Get a specific line from the HTML file for this webpage
        :param line: The line to get
        :return: The content of the specified line
        """
        return self.get_html().splitlines()[line]

    def get_lines_from_content(self, content):
        """
        Generate a list of line numbers that contain the given content
        :param content: The content to search for
        :return: A list of which lines contain this content
        """
        html = self.get_html()
        list_of_lines = []

        i = 0
        while i < len(html.splitlines()):
            if content in html.splitlines()[i]:
                list_of_lines.append(i+1)
            i = i+1
        return list_of_lines

