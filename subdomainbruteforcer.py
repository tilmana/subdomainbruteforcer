import urllib.request

domains = []
domain = input("Domain: ")
wordlist = input("Wordlist: ")

f = open(wordlist, "r")

lines = f.readlines()

for line in lines:
    print("trying " + str(line))
    stripped_line = line.strip()
    link = "http://" + stripped_line + "." + domain

    try:
        print(urllib.request.urlopen(link).getcode())
        domains.append(stripped_line)
    except Exception:
        continue
print("Valid domains found: ")
for domain in domains:
    print(domain)
