facebook = True
twitter = False
instagram = False
if (facebook and twitter) or (facebook and instagram) or ( instagram and twitter):
    print('You are a good influencer!')
else:
    print('You are not a good influencer!')