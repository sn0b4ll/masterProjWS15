import sys, socket
import re
import csv
from time import sleep
import subprocess
#import aesopenssl

def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    #print 'verb: ' + str(arguments.verbose)
    #if arguments.verbose: print 'command: ' + command

Fahrzeugtypenstring = ""
f = open("info/Fahrzeugtypen.csv", 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        Fahrzeugtypenstring += str(row)[2:5] + "|"
finally:
    f.close()
Fahrzeugtypenstring = Fahrzeugtypenstring[:-1]

OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

TCP_IP = '127.0.0.1'
#TCP_IP = '88.198.205.243'
TCP_PORT = 1337
BUFFER_SIZE = 512

pattern =  "^(WVW|WV2|1VW|3VW|9BW|AAV)(ZZZ)?(" + Fahrzeugtypenstring + ")([ABCDEFGHJKLMNPRSTVWXY]|[0-9])([ABCDEFGHJKLMNPRSTUVWXYZ]|[0-9])[0-9]{6}$"
counter = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)
clients = []

try:
    while 1:
        conn, addr = s.accept()
        if not str(addr[0]) in clients:
            clients.append(str(addr[0]))
            print(OKGREEN + "[+] Client %s connected" % (str(addr[0])) + ENDC)
        #print(OKBLUE    + "[*] Starting keydump..."                     + ENDC)
        tmp = ""
        conn.send("\n********************************************************\n")
        conn.send("**************** Welcome to Folkswagen *****************\n")
        conn.send("********************************************************\n")
        conn.send("\n********************************************************\n")
        conn.send("*                                                      *\n")
        conn.send("* FFFFFFFFFFFFFFFFF  W               W               W *\n")
        conn.send("* FF                  W             W W             W  *\n")
        conn.send("* FF                   W           W   W           W   *\n")
        conn.send("* FF                    W         W     W         W    *\n")
        conn.send("* FFFFFFFFFFF            W       W       W       W     *\n")
        conn.send("* FF                      W     W         W     W      *\n")
        conn.send("* FF                       W   W           W   W       *\n")
        conn.send("* FF                        W W             W W        *\n")
        conn.send("* FF                         W               W         *\n")
        conn.send("*                                                      *\n")
        conn.send("********************************************************\n\n\n")

        conn.send("Ey du Gradler gib a moi dei Fahrgsteinumma ei:\n")

        translator = False
        addfzn = False
        decrypt = False

        numberplz = "Ey du Gradler gib a moi dei Fahrgsteinumma ei:\n"
        wordplz = "Welches bayrische Wort moechten sie wissen?\n"
        wrongnum = "\nDes is fei koa gscheide Numma du de** du dammischer...\n\nSollten sie aus dem Ausland kommen und kein Bayrisch\nsprechen koennen sie auch unseren Uebersetzer nutzen!\nGeben sie dafuer folgendes ein: \n\"I ko koa bayrisch\"\n"
        cake = "The cake is a lie!\n"
        quittrans = "Der Uebersetzer laesst sich mit exit oder quit beenden.\n"
        emission = "Dei Emissionwert der ist ned so guad schaust ma her: \n"

        while 1:
            try:
                data = conn.recv(BUFFER_SIZE)  # This returns immediately with no data, when client connection is run from script and doesn't send() anything, just connects.
                print "data: " + data
            except ConnectionResetError as e:
                #print(FAIL + "\n[-] Client %s disconnected hard" % (str(addr[0])) + ENDC)
                break
            if not data:
                print((WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC))
                break
            else:
                data = (str(data)).strip()
                sys.stdout.flush()
                if translator:
                    if(data == "quit" or data == "exit"):
                        translator = False
                        conn.send(numberplz)
                    else:
                        if not "\"" in data:
                            r = execute_shell("../ro/aesopenssl \"" + data + "\"")
                            tmp = r.stdout.read()
                            conn.send("\nDas Wort " + data + " bedeutet " + tmp + " in deutsch.\n");
                        conn.send(wordplz)
                elif addfzn:
                    if(data == "quit" or data == "exit"):
                        addfzn = False
                        conn.send("left addfzn mode\n")
                    else:
                        #print(data)
                        #print("./setflag " + data)
                        if not "\"" in data:
                            r = execute_shell("export LD_LIBRARY_PATH=../ro/chilkat-9.5.0-x86_64-linux-gcc/lib:$LD_LIBRARY_PATH; " + "../ro/setflag " + data)
                            tmp = r.stdout.read()
                            conn.send(tmp)
                            print "after execute_shell()"
                        conn.send("Neue fzn eingeben:\n");
                elif decrypt:
                    if(data == "quit" or data == "exit"):
                        decrypt = False
                        conn.send("left decrypt mode\n")
                    else:
                        if not "\"" in data:
                            r = execute_shell("export LD_LIBRARY_PATH=../ro/chilkat-9.5.0-x86_64-linux-gcc/lib:$LD_LIBRARY_PATH; " + "../ro/setflag -h " + data) # TODO
                            tmp = r.stdout.read()
                            conn.send(tmp)
                            print "after execute_shell()"
                        conn.send("\nYou might wanna decrypt something...:\n");
                elif(data == "quit" or data == "exit"):
                    print((WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC))
                    break
                elif(data == "help"):
                    conn.send(cake)
                elif(data == "I ko koa bayrisch"):
                    translator = True
                    conn.send(quittrans)
                    conn.send(wordplz)
                elif(data == "addfzn"):
                    conn.send("Neue fzn eingeben:\n")
                    addfzn = True
                elif(data == "decrypt"):
                    conn.send("You might wanna decrypt something...:\n")
                    decrypt = True
                else:
                #elif(re.match(pattern, data)):
                    print("./commandInjection " + data)
                    if not "\"" in data:
                        r = execute_shell("../ro/commandInjection \"" + data + "\"")
                        tmp = r.stdout.read()
                    if tmp != "Na\n":
                        print(tmp)
                        conn.send(emission + tmp + "\n")
                    else:
                        conn.send(wrongnum)
        sys.stdout.flush()
        conn.close()
except KeyboardInterrupt as e:
    s.close()
    print(OKBLUE + "\n[-] Shutting down.." + ENDC)
except Exception as e:
    s.close()
    print(FAIL + "[X] Unhandelt Error:")
    print(e)
