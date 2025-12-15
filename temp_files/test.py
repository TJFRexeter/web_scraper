import os
import re

path = str(os.getcwd()) + '/temp_files/'#+ "\\web_scraper\\"

filename = 'reduced_html.html'

with open(path+filename, 'r') as f:
    try:
        content = f.read()
    except OSError as e:
        print(e)

refined_str = re.sub('<[^<>]*>', '', content)

print(refined_str)