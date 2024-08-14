import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")
''' re.sub(pattern, repl, string, count=0, flags=0)'''
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1)

''' re.split(pattern, string, maxsplit=0, flags=0)'''
''' re.findall(pattern, string, flags=0) '''

