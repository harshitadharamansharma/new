# file.py
import re

tokens = (
  ('STRING', re.compile('"[^"]+"')),  # longest match
  ('ID', re.compile('[a-zA-Z_]+')),
  ('SPACE', re.compile('\s+')),
  ('DIGIT', re.compile('\d+')),
)


def user_query_tokenizer(message):
  
  i = 0
  lexeme = []
  while i < len(message):
    match = False
    for token, regex in tokens:
      result = regex.match(message, i)
      if result:
        lexeme.append((token, result.group(0)))
        i = result.end()
        match = True
        break
    if not match:
      raise Exception('lexical error at {0}'.format(i))
  return lexeme


# user_messge=
for i in user_query_tokenizer(input('enter your message')):
  print(i)


