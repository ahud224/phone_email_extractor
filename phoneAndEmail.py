import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # hyphen/period
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # hyphen/period
    (\d{4})                         # last 4
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''',re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # user name
    @                               # @
    [a-zA-Z0-9.-]+                  # domain
    (\.[a-zA-Z]{2,4})               # top level domain
    )''',re.VERBOSE)

# Find matches in clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #takes the 1st (area code), 3rd(first 3 digits) and 5th (last 4 digits) groups and adds a hypen to make a phone #
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text): # grabs the whole the whole email address 
    matches.append(groups[0])


# copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('no phone numbers or email addresses found')

