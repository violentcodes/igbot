import mouse,keyboard,colorama,random,os,pyfiglet,webbrowser,time
from colorama import Style,Fore
from pyfiglet import Figlet
print(Fore.MAGENTA + Style.BRIGHT + pyfiglet.figlet_format("IGBOT"))
print(Fore.BLUE + Style.NORMAL + "made by Saksham Sharma(violentcodes) & ritish(only made README.md)")
a = input("enter name 1:")
b = input("enter name 2:") 
c = input("enter name 3:") 
d = input("enter name 4:") 
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
keyboard.write(b + "@gmail.com")     
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
mouse.move(840,400)



 


