# webserver-upload
First Python/Flask project - file upload server with (sorta)authentication

usage: server.py [-h] -p PORT [-o OUTFILE]

options:
  -h, --help            show this help message and exit</br>
  -p PORT, --port PORT  Assign a port for the web_uploader</br>
  -o OUTFILE, --outfile OUTFILE
                        Destination for uploaded file(s)
                        
Always wanted to write a file uploader for when on boxes that are CLM/Defender/etc.. locked down and need to exfil data; however, since I am on places like HTB
a lot, I know that it is a shared environment, so to keep people from uploading things to my box, I wanted to have some sort of authentication to keep that
from happening.
