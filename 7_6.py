def card(number):
    numberstr=str(number)
    hide=numberstr[0:2]+'*'*(len(numberstr)-6)+numberstr[len(numberstr)-5:len(numberstr)-1]
    return hide
print(card(33333337))
