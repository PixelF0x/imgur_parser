import string, random, os, sys, _thread, httplib2, time

if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python3 " + sys.argv[0] + " (Number of threads)")
THREAD_AMOUNT = int(sys.argv[1])

input("Press ENTER run script\n")

INVALID = [0, 503, 5082, 4939, 4940, 4941, 12003, 5556]
if not os.path.isdir("Photos"):
     os.mkdir("Photos")
os.chdir("Photos")
#if not os.path.isdir("bug"):
#    os.mkdir("bug")
def scrape_pictures(thread):
    while True:
        #url = 'http://img.prntscr.com/img?url=http://i.imgur.com/' url = 'https://prnt.sc/'
        url = 'http://i.imgur.com/'
        length = random.choice((5, 6))
        if length == 5:
            url += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        else:
            url += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
            url += ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))
            url += '.jpg'
        

            filename = url.rsplit('/', 1)[-1]

            h = httplib2.Http('.cache' + thread)
            response, content = h.request(url)
            out = open(filename, 'wb')
            out.write(content)
            out.close()

            file_size = os.path.getsize(filename)
            size_test=os.path.getsize(filename)
            
                
            if (file_size in INVALID) or (size_test== 5553):
                #print("[-] Invalid: " + url)
                os.remove(filename)
            else:
                print("[+] Valid: " + url)
            '''if  (size_test== 5553):
                #print("[-] Bug " + url)
                os.remove(filename)
                #os.replace(filename, 'bug/'+filename)'''

for thread in range(1, THREAD_AMOUNT + 1):
    thread = str(thread)
    try:
        _thread.start_new_thread(scrape_pictures, (thread,))
    except:
        print('Error starting thread ' + thread)
print('Succesfully started ' + thread + ' threads.')

while True:
    time.sleep(1)
