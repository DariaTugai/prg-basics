translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
eng_word=input('Enter a word: ')
if eng_word in translations:
    for i,x in translations.items():
        if i==eng_word:
            print(x)
else:
    print('the translation is unavailable')