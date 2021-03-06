from pandas import read_excel
emaildata = None

try:
  emaildata = read_excel('emails-to-send.xlsx', sheet_name='Sheet1',
                         engine='openpyxl')
except IOError:
  print('unable to read')
  exit(1)

for email, hike in zip(emaildata["email"], emaildata["hike"]):
  print(f'to {email}: hike is {hike}')
