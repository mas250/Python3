import urllib.request

url = 'http://empslocal.ex.ac.uk/studyres/ECM1408/secret.html'
connection = urllib.request.urlopen(url)
for line in connection.fp:
    s = line.decode()
    print(s.strip())
