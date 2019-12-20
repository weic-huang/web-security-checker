import re

class HtmlScanner():
    def __init__(self):
        pass

    def checkHiddenObject(self, elements):
    # Check if elements contain hidden elements.
    # Only check for visibility = "hidden", not display = "none",
    # since the latter cannot be clicked.

        for e in elements:
            if len(re.search(r'visibility\s*(:|=)(\s|\"|\')*hidden(\s|\"|\')*', e)) != 0:
                if len(re.search(r'display\s*(:|=)(\s|\"|\')*none(\s|\"|\')*', e)) == 0 and ('click' not in e):
                    return True
        return False
