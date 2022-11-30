import re



# 4-5 v: mvvvc
# 1. - mit , austauschen
# 2. Buchstabe nach vorne holen
# 3. Eckige Klammern setzen
# 4. r" setzen und "" setzen
print(list("hlhhhhrdjncphc"))

# if list("hlhhhhrdjncphc")[5-1] == str("h") and list("hlhhhhrdjncphc")[8-1] != str("h"):
# 	print("yes")
# if list("rrrrrrzrrrrrqrrrrrr")[13-1] == str("r") and list("rrrrrrzrrrrrqrrrrrr")[16-1] != str("r"):
# 	print("yes")

if list("abcde")[1-1] == str("a") and list("abcde")[3-1] != str("a"):
	print("yes")

if list("mhjkjljjjz")[3-1] == str("j") and list("mhjkjljjjz")[9-1] != str("j"):
	print("yes")
if list("fzszzbzhsfxcmh")[4-1] == str("z") and list("fzszzbzhsfxcmh")[5-1] != str("z"):
	print("yes")
if list("ntngqrhnnrxjnnnnwxnn")[1-1] == str("n") and list("ntngqrhnnrxjnnnnwxnn")[11-1] != str("n"):
	print("yes")
if list("rllllj")[4-1] == str("l") and list("rllllj")[5-1] != str("l"):
	print("yes")

# if list("abcde")[1-1] == str("a") and list("abcde")[3-1] != str("a"):
# 	print("yes")


# if len(re.findall("[x]","qdzkpnhbdxcxsfsxkx")) in range(17,18):
#  	print("yes")
# if len(re.findall("[q]","qqqtqtql")) in range(1,8):
# 	print("yes")