import contact
import contact_list

p1=contact.Contact('John Brown','brown@onet.pl',555234000)
p2=contact.Contact('Anna May','am@o2.pl',232000199)
p3=contact.Contact('George Small','smallg@google.pl',222999100)
  
w1=contact_list.Contact_List([p1,p2,p3])
w1.display()
