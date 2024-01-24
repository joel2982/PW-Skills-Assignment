month = input('Enter the Month = ')
spring = ['March','April']
autumn = ['September','October']
summer = ['May','June','July','August']
winter = ['November','December','January','February']
if month.title() in spring: 
    print('Spring Season')
elif month.title() in autumn: 
    print('Autumn Season')
elif month.title() in summer: 
    print('Summer Season')
elif month.title() in winter: 
    print('Winter Season')