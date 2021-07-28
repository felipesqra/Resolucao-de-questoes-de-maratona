inputs = int(input())
words = []

for i in range(inputs):
  word = input()
  if(len(word) > 10):
    words.append(word[0] + str(len(word)-2) + word[len(word)-1])
  else:
    words.append(word)

for i in range(len(words)):
  print(words[i])