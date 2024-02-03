#str()
#int()
#float()

greet = 'hellooo'
print(len(greet)) #7
print('=========')
# print(greet[0:7])
print(greet[0:len(greet)])

# String Methods
# Regularly used
# .capitalize()
# .casefold() => to lowercase
# .count() => Returns no. times a CHAR occurs
# .encode() => Useful for Backdoor engineering to encode('commands')
# before sending to victims' machines
# 
# .endswith() => Return True if string ends with specified value
# .find() => Searches CHAR => return POSITION
#
# .format() => Formats specified values
# .lower() => Converts STRING => Lowercase
# .upper() => Converts STRING => Uppercase
# .replace() => 
# .strip() => Returns a trimmed string

quote = 'to be or not to be'
#quote.format()
print(quote.upper()) # TO BE OR NOT TO BE

print(quote.find('be')) # 'be' exist? return index : return None

print(quote.replace('be', 'BE')) # Replacing
print(quote) # to be or not to be => Cuz String != Immutable

