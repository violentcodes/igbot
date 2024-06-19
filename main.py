import mouse,keyboard,colorama,random,os,pyfiglet,webbrowser,time,string
from tempMail import EMail
from colorama import Style,Fore
from pyfiglet import Figlet
print(Fore.MAGENTA + Style.BRIGHT + pyfiglet.figlet_format("IGBOT"))
print(Fore.BLUE + Style.NORMAL + "made by Saksham Sharma(violentcodes) & ritish(only made README.md)")
a = ''.join(random.choices(string.ascii_letters, k=10))
b = EMail()
c = ''.join(random.choices(string.ascii_letters, k=8))
d = ''.join(random.choices(string.ascii_letters, k=10)) 
e = input("enter your instagram profile link:")
print(f"Generated email address: {b.address}")
print("Generated password:" , d)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,  
                    webbrowser.BackgroundBrowser(chrome_path)) 
webbrowser.get('chrome').open_new_tab("https://www.instagram.com/accounts/emailsignup/")
time.sleep(1) 
mouse.move(802, 463)
time.sleep(2)
mouse.click("left")
keyboard.write(a)
mouse.move(700, 360 )  
mouse.click('left')
keyboard.write(str(b))
mouse.move(700,410) 
mouse.click('left')
keyboard.write(c)   
mouse.move(700,500) 
mouse.click('left')
keyboard.write(d)  
mouse.move(700,680)
mouse.click('left')
time.sleep(3)
mouse.move(840,340)
mouse.click('left')
time.sleep(0.3)
mouse.move(840,650)
mouse.click('left')
mouse.move(840,430)
mouse.click('left')
g = input("enter otp:")
keyboard.press_and_release("alt+tab")
time.sleep(1)
keyboard.press_and_release("ctrl+tab")
time.sleep(1)
mouse.move(840,430)
keyboard.write(g)





 


