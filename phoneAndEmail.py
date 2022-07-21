import pyperclip, re

# Finds phone numbers and email addresses on the clipboard.
# Usage: ctrl + c to copy text and then run the script.

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @                 # '@' symbol
    [a-zA-Z0-9.-]+    # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

# Finds matches in clipboard text.
text = str(pyperclip.paste())

matches = []

# the phones extracted should be in one format
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy the results to the clipboard.
# Save the results to the file
with open('dump_emails_phones.txt', 'w') as dump:

    if len(matches) > 0:
        dump.write('\n'.join(matches))
        print('[!] Data has been written to the file successfully')
#    pyperclip.copy('\n'.join(matches))
#    print('Copied to clipboard: ')
#    print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')
