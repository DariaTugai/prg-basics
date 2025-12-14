import re
with open('email.txt','r') as file:
    content = file.read().splitlines()

def email_sender(cont):
    sender=''
    for line in cont:
        if 'From' in line:
            regex='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com'
            sender=re.search(regex,line)
            if sender:
             return sender.group()
    return None

def email_recipient(cont):
    recipient=''
    for line in cont:
        if 'To' in line:
            regex='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com'
            recipient=re.search(regex,line)
            if recipient:
               return recipient.group()
    return None
            
def email_subject(cont):
    subject=''
    for line in cont:
        if 'Subject' in line:
            regex='(?<=Subject: ).+'
            # regex='\s[A-za-z0-9\.\s]+'
            subject=re.search(regex,line)
            if subject:
               return subject.group()
    return None

def email_body(cont):
    body_lines = []
    in_body = False

    for line in cont:
        if in_body:
            body_lines.append(line)
        elif line.strip() == "":
            in_body = True

    return "\n".join(body_lines) if body_lines else None


print(email_sender(content))
print(email_recipient(content))
print(email_subject(content))
print(email_body(content))

#The file email.txt contains a raw email.
#  Write a program that uses
#  regular expressions to fetch and print:
# sender email address
# recipient email address
# email subject
# email body
# For each of the above commands, 
# define a separate function (see below) that 
# returns the value read from the email. 
# Place the functions in a separate module called emails.

# email_sender()
# email_recipient()
# email_subject()
# email_body()
