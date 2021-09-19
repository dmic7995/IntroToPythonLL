#
# Example file for working with fetching internet data (json, xml, html)
#

import urllib.request # Provides the classes needed for an http:// request
# import ssl # The SSL module allows you to override 

def main():

    # # This statemtne helps work around the SSL certification error that keeps popping up for other websites
    # ssl._create_default_https_context = ssl._create_unverified_context

    # open a connection to a URL using urllib2
    webUrl = urllib.request.urlopen("https://www.zerohedge.com")
  
    # get the result code and print it
    print ("result code: " + str(webUrl.getcode()))
  
    # read the data from the URL and print it
    data = webUrl.read()
    print (data)

if __name__ == "__main__":
  main()
