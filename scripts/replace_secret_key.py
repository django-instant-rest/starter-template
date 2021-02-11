# Execute this script to regenerate the secret key in settings.py

import re
import secrets
import fileinput

# Defining the file to be affected
filename = "mysite/settings.py"

# Defining the regex patterns necessary for find/replace
new_secret_key = secrets.token_urlsafe()
before = r"(\nSECRET_KEY = )(.*)(\n)"
after = rf"\1'{new_secret_key}'\3"

# Reading the original file contents
with open(filename) as r:
    text = r.read()

# Writing the new file contents
with open(filename, "w") as w:
    new_text = re.sub(before, after, text)
    w.write(new_text)
