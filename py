# Define the lowercase alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Encrypted message using Caesar cipher with a shift of -10
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

# This will store the decoded message
translated_message = ""

# Loop through each character in the message
for character in message:
  if character in alphabet:
    # Find the position of the letter, shift it by +10, and wrap around using % 26
    character_value = alphabet.find(character)
    translated_message += alphabet[(character_value + 10) % 26]
  else:
    # Leave punctuation and spaces unchanged
    translated_message += character
