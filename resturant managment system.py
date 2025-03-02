#sab se pehle customer ko welcome kare ge
print('\tHello Sir\nWelcome to Our Resturant')
print('************************')

#oske bad customer ko menu pesh kare ge
print("   \n    \033[41mHere's the menu ")
#menu ko print kare.
         #Menu
print(' Food items    Prices  ')
print('.......................')
print('Chiken karahi  Rs 1000','\nMutton Karahi  Rs 2050','\nBeef karahi    Rs 1900','\nMutton Korma   Rs 1850 ')
print('                       ')
print('Pizza          Rs 1100','\nBurger         Rs 300 ','\nShawarma       Rs 150 ','\nSandwich       Rs 250  ')
print('                       ')
print('Pepsi           Rs 170','\nPurified water  Rs 100','\nCoffe           Rs 300','\nOrganic Juice   Rs 250','\nSoda water      Rs 150 ')
print('                       ')
print('Ice Cream      Rs 200 ','\nBrownies       Rs 300 ','\nCake           Rs 900  ')
print('.......................\033[0m')

#sare menu ko dectionary me likhen
menu={
      'chiken karahi':1000,
    'mutton karahi':2050,
    'beef karahi':1900,
    'mutton Korma':1850,
    'pizza':1100,
    'burger':300,
    'shawarma':150,
    'sandwich':250,
    'pepsi':170,
    'purified water':100,
    'coffe':300,
    'organic juice':250,
    'soda water':150,
    'ice cream':200,
    'brownies':300,
    'cake':900
}
#customer se order len
total = 0
order_details=[]
while True:
    Customer_order = input('\nWhat would you like to eat: ').lower()
    if Customer_order in menu:
        print('Sure Sir.')
        total += menu[Customer_order]
        #list me add kar de customer order ko
        order_details.append((Customer_order,menu[Customer_order]))
    else:
        print('Sorry Sir, this item is not available.')

    again_order = input("\nIs there anything else you'd like (yes or no): ").lower()
    if again_order != 'yes':
        break
      #phir total bill ko print karna he
print('\n\033[41mYour order details:\033[0m')
for items,prices in order_details:                           #phir wo list wale itoms ko print karwna he
    print('\033[41m ',items.capitalize(),'=',prices,'\033[0m')
print('\033[41m..................\033[0m')
print(f' \033[41m Total= {total}\033[0m   ')

#jab order complete ho jaye to phir os se payment method poche,ke kis method ke sath wo payment karna chata he
    #payment methods
if Customer_order in menu:
    print('\n\t\t\t*')
    print('\t\t \033[41mPayment Methods\033[0m')
    print('\033[41m(Jazzcash , Easypaisa , Bank Transfer , Cash on Delivery)\033[0m')
    payment_method=input('\nSir, which payment method would you prefer to use: ')
    payment_method_list=['jazzcash' , 'easypaisa' , 'bank transfer' , 'cash on delivery']
    if payment_method in payment_method_list[0]:
       print('\t\033[0m(Jazzcash num: 03265212300)\033[0m')
    elif payment_method in payment_method_list[1]:
       print('\t\033[0m(Easypaisa num: 03107577184)\033[0m')
    elif payment_method in payment_method_list[2]:
       print('\t\033[0m( Bank Name: HBL )\033[0m\n\033[42m( Account num: PK94HBL0000001123456702 )\033[0m')
    elif payment_method in payment_method_list[3]:
       print('\033[0m(Sure Sir,your order will be ready in half an hour.)\033[0m')
    else:
       print('Sorry sir , this payment method is not available.')

#last per good by bole customer ko
input('\n\nThank you for visiting us,have a great day!')
