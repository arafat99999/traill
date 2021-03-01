#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/12.0 (Android; Opera Mini/52.2.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def exb():
    print '[!] Exit Successful'
    os.sys.exit()

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print 
    print
    print "\033[031m╔══╗═══\033[033m╔═══════════════════╗"
    print "\033[031m|\033[030mNO\033[031m|   \033[031m|\033[037mMENU TOOLS\033[031m         |"
    print "\033[032m╚══╝═══\033[036m╚═══════════════════╝"
    print "\033[1;94m<═════════════════════════════════════════════>"
    print " \033[1;96m╔═══════════════╗"
    print "\033[1;96m |\033[1;97mWITHOUT LOGIN \033[1;96m |"
    print " \033[1;96m╚═══════════════╝"
    print"\033[1;92m1.\033[1;97m├\033[1;93m PAKISTAN WITHOUT LOGIN"
    print"\033[1;95m2.\033[1;97m├\033[1;93m MAIL WITHOUT LOGIN"
    print"\033[1;94m3.\033[1;97m├\033[1;93m TARGET WITHOUT LOGIN"
    print" \033[1;96m╔═══════════════╗"
    print"\033[1;96m |\033[1;97mWITH LOGIN   \033[1;96m  |"
    print" \033[1;96m╚═══════════════╝"
    print"\033[1;93m4.\033[1;97m├\033[1;92m CRACKING WITH LOGIN"
    print"\033[1;91m5.\033[1;97m├\033[1;92m YAHOO WITH LOGIN"
    
    pilih_Somi()
    
def pilih_Somi():    
    Somi = raw_input("\n\033[1;97m>\033[1;93m")
    if Somi =="":
        print "\x1b[1;97mWRONG "
        pilih_Somi()
    elif Somi =="y":
    	os.system("rm -rf $HOME/WORLD")
        os.system("cd $HOME && git clone https://github.com/Somi190/WORLD.git")     
        
        time.sleep(5)
        os.system("cd $HOME/WORLD && python2 WORLD.py")
 
    elif Somi =="n":
    	exb()
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()
