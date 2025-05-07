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
# Print the decoded message
print(translated_message)

# Message to encode using Caesar cipher with a shift of 10
message_for_v = "hey vishal! This is a super cool cipher, thanks for showing me! What else you got?"

translated_message_for_v = ""

# Encode message by shifting letters -10 in the alphabet
for character in message_for_v:
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message_for_v += alphabet[(character_value - 10) % 26]
  else:
    translated_message_for_v += character

# Print the encoded message
print(translated_message_for_v)
