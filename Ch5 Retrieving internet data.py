#
# Example file for working with fetching internet data (json, xml, html)
#

import urllib.request # Provides the classes needed for an http:// request

def main():
    weburl = urllib.request.urlopen("https://www.google.com/")
    print("result code: " + str(weburl.getCode()))

if __name__ == "__main__":
    main()