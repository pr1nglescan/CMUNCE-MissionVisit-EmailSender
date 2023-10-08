from draftwriter import gmail_create_draft
import pandas as pd

#dictionary of email adresses with fields: sender, recipients, CCs
addresses = {'Sender': '',
             'Recipients': [],
             'CC': []}

contact_sheet = pd.read_excel('mission_emails.xlsx', sheet_name="Export",
                              header = 0)

for country in contact_sheet.index:
    countryName = contact_sheet.loc[country, 'Mission']
    addresses['Sender'] = 'dk3260@columbia.edu'
    emails = str(contact_sheet.loc[country, 'Email'])
    addresses['Recipients'] = emails.split(' ')
    addresses['CC'] = ['aa4681@columbia.edu', 'mlk2195@columbia.edu', 'jlv2151@columbia.edu']

    subject = 'Mission Visit Inquiry—Columbia University Model UN'

    with open('MissionEmailTemp_html.txt', 'r', encoding="utf-8") as f:
        content = f.read()
        content = content.replace("INSERT_HERE", str(countryName))

    gmail_create_draft(addresses, subject, content)

#tester
addresses['Sender'] = 'dk3260@columbia.edu'
addresses['Recipients'] = ['fdq2000@barnard.edu', 'tio2003@barnard.edu']
addresses['CC'] = ['jlv2151@columbia.edu', 'mc5297@columbia.edu']

subject = 'Testing New Code'

#with open('MissionAPI_testingtext_html.txt', 'r', encoding="utf-8") as f:
#    message_h = f.read()


#gmail_create_draft(addresses, subject, message_h)