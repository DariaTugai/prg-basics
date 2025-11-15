###
# Counts vowels in the text
#
text = input('Enter some text: ')
vowels = "aeiouAEIOU"
vowel_count = 0
a=0

# Count vowels in the text
#for char in text:
#   if char in vowels:
#        vowel_count += 1

while a<= (len(text)-1):
    if text[a] in vowels:
        vowel_count+=1
        a+=1
    else:
        a+=1
print(f"The number of vowels in the text is: {vowel_count}")
