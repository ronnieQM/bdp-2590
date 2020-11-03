import time
import sys
import os


def welcome():
    # message = 'welcome'
    #
    # for char in message:
    #     sys.stdout.write(char)
    #     sys.stdout.flush()
    #     time.sleep(.2)

    message = """
                                                                                                                                                                       
bbbbbbbb                                                              dddddddd                                                                                         
b::::::b              iiii                                            d::::::d                          tttt                                                           
b::::::b             i::::i                                           d::::::d                       ttt:::t                                                           
b::::::b              iiii                                            d::::::d                       t:::::t                                                           
 b:::::b                                                              d:::::d                        t:::::t                                                           
 b:::::bbbbbbbbb    iiiiiii    ggggggggg   ggggg              ddddddddd:::::d   aaaaaaaaaaaaa  ttttttt:::::ttttttt      aaaaaaaaaaaaa                                  
 b::::::::::::::bb  i:::::i   g:::::::::ggg::::g            dd::::::::::::::d   a::::::::::::a t:::::::::::::::::t      a::::::::::::a                                 
 b::::::::::::::::b  i::::i  g:::::::::::::::::g           d::::::::::::::::d   aaaaaaaaa:::::at:::::::::::::::::t      aaaaaaaaa:::::a                                
 b:::::bbbbb:::::::b i::::i g::::::ggggg::::::gg          d:::::::ddddd:::::d            a::::atttttt:::::::tttttt               a::::a                                
 b:::::b    b::::::b i::::i g:::::g     g:::::g           d::::::d    d:::::d     aaaaaaa:::::a      t:::::t              aaaaaaa:::::a                                
 b:::::b     b:::::b i::::i g:::::g     g:::::g           d:::::d     d:::::d   aa::::::::::::a      t:::::t            aa::::::::::::a                                
 b:::::b     b:::::b i::::i g:::::g     g:::::g           d:::::d     d:::::d  a::::aaaa::::::a      t:::::t           a::::aaaa::::::a                                
 b:::::b     b:::::b i::::i g::::::g    g:::::g           d:::::d     d:::::d a::::a    a:::::a      t:::::t    tttttta::::a    a:::::a                                
 b:::::bbbbbb::::::bi::::::ig:::::::ggggg:::::g           d::::::ddddd::::::dda::::a    a:::::a      t::::::tttt:::::ta::::a    a:::::a                                
 b::::::::::::::::b i::::::i g::::::::::::::::g            d:::::::::::::::::da:::::aaaa::::::a      tt::::::::::::::ta:::::aaaa::::::a                                
 b:::::::::::::::b  i::::::i  gg::::::::::::::g             d:::::::::ddd::::d a::::::::::aa:::a       tt:::::::::::tt a::::::::::aa:::a                               
 bbbbbbbbbbbbbbbb   iiiiiiii    gggggggg::::::g              ddddddddd   ddddd  aaaaaaaaaa  aaaa         ttttttttttt    aaaaaaaaaa  aaaa                               
                                        g:::::g                                                                                                                        
                            gggggg      g:::::g                                                                                                                        
                            g:::::gg   gg:::::g                                                                                                                        
                             g::::::ggg:::::::g                                                                                                                        
                              gg:::::::::::::g                                                                                                                         
                                ggg::::::ggg                                                                                                                           
                                   gggggg                                                                                                                              
                                                                                                                                                                       
                                                                                                  dddddddd                                                             
XXXXXXX       XXXXXXXMMMMMMMM               MMMMMMMMLLLLLLLLLLL                                   d::::::d                                                             
X:::::X       X:::::XM:::::::M             M:::::::ML:::::::::L                                   d::::::d                                                             
X:::::X       X:::::XM::::::::M           M::::::::ML:::::::::L                                   d::::::d                                                             
X::::::X     X::::::XM:::::::::M         M:::::::::MLL:::::::LL                                   d:::::d                                                              
XXX:::::X   X:::::XXXM::::::::::M       M::::::::::M  L:::::L                             ddddddddd:::::d     eeeeeeeeeeee       mmmmmmm    mmmmmmm      ooooooooooo   
   X:::::X X:::::X   M:::::::::::M     M:::::::::::M  L:::::L                           dd::::::::::::::d   ee::::::::::::ee   mm:::::::m  m:::::::mm  oo:::::::::::oo 
    X:::::X:::::X    M:::::::M::::M   M::::M:::::::M  L:::::L                          d::::::::::::::::d  e::::::eeeee:::::eem::::::::::mm::::::::::mo:::::::::::::::o
     X:::::::::X     M::::::M M::::M M::::M M::::::M  L:::::L                         d:::::::ddddd:::::d e::::::e     e:::::em::::::::::::::::::::::mo:::::ooooo:::::o
     X:::::::::X     M::::::M  M::::M::::M  M::::::M  L:::::L                         d::::::d    d:::::d e:::::::eeeee::::::em:::::mmm::::::mmm:::::mo::::o     o::::o
    X:::::X:::::X    M::::::M   M:::::::M   M::::::M  L:::::L                         d:::::d     d:::::d e:::::::::::::::::e m::::m   m::::m   m::::mo::::o     o::::o
   X:::::X X:::::X   M::::::M    M:::::M    M::::::M  L:::::L                         d:::::d     d:::::d e::::::eeeeeeeeeee  m::::m   m::::m   m::::mo::::o     o::::o
XXX:::::X   X:::::XXXM::::::M     MMMMM     M::::::M  L:::::L         LLLLLL          d:::::d     d:::::d e:::::::e           m::::m   m::::m   m::::mo::::o     o::::o
X::::::X     X::::::XM::::::M               M::::::MLL:::::::LLLLLLLLL:::::L          d::::::ddddd::::::dde::::::::e          m::::m   m::::m   m::::mo:::::ooooo:::::o
X:::::X       X:::::XM::::::M               M::::::ML::::::::::::::::::::::L           d:::::::::::::::::d e::::::::eeeeeeee  m::::m   m::::m   m::::mo:::::::::::::::o
X:::::X       X:::::XM::::::M               M::::::ML::::::::::::::::::::::L            d:::::::::ddd::::d  ee:::::::::::::e  m::::m   m::::m   m::::m oo:::::::::::oo 
XXXXXXX       XXXXXXXMMMMMMMM               MMMMMMMMLLLLLLLLLLLLLLLLLLLLLLLL             ddddddddd   ddddd    eeeeeeeeeeeeee  mmmmmm   mmmmmm   mmmmmm   ooooooooooo   
                                                                                                                                                                       
                                                                                                                                                                       
"""

    try:
        for char in message:
            sys.stdout.write(char)
            time.sleep(.00001)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        pass
    os.system('cls' if os.name == 'nt' else 'clear')




def waiter():
    try:
        raw_input('. . . ')
    except:
        input('. . . ')



def breakpoint():
    x = '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .'
    try:
        while True:
            for i in x:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(3)
    except KeyboardInterrupt:
        pass
def clearit():
    os.system('cls' if os.name == 'nt' else 'clear')

def breakout():
    exit()
    print('\nbye\n')
