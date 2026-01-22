import urllib.request

try:
      url = urllib.request.urlopen("https://vrajpatel.vercel.app/")
      content = url.read()
      url.close()
except urllib.error.HTTPError:
      print("The webpage is not found")
      exit()

f = open("Networking/vraj.html", "wb")
f.write(content)
f.close()