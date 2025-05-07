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
# Caesar cipher decode function
def caesar_decode(message, offset):
  decoded_message = ""

  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      decoded_message += alphabet[(character_value + offset) % 26]
    else:
      decoded_message += character

  return decoded_message

# Caesar cipher encode function
def caesar_encode(message, offset):
  encoded_message = ""

  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      encoded_message += alphabet[(character_value - offset) % 26]
    else:
      encoded_message += character

  return encoded_message
# Encrypted message using Caesar cipher with an offset of 10
message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

# Decode message_one
print(caesar_decode(message_one, 10))

# Another message using Caesar cipher with a different offset
message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

# Decode message_two with offset 14
print(caesar_decode(message_two, 14))

# Brute-force Caesar decoding (try all 25 possible offsets)
brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# Try every possible offset to find the correct decoding
for i in range(1, 26):
  print("Offset: {}".format(i))
  print("\t {}".format(caesar_decode(brute_force_message, i)))
# Vigenère cipher decode function
def vigenere_decode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  # Generate a repeated keyword phrase to match message length
  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  decoded_message = ""

  # Decode each character using corresponding character from keyword
  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index + offset_index) % 26]
      decoded_message += new_character
    else:
      decoded_message += message[i]

  return decoded_message
