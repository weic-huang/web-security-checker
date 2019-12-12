import re

class HtmlScanner():
    def __init__(self, HtmlObject):
        self.HtmlObject = HtmlObject

    def checkHiddenObject(self):
    # Check if the HtmlObject contains hidden elements.
    # Only check for visibility = "hidden", not display = "none",
    # since the latter cannot be clicked.

        if len(re.search(r'visibility\s*(:|=)(\s|\"|\')*hidden(\s|\"|\')*', self.HtmlObject)) != 0:
            return True
        return False
