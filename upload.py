import ftplib, os.path, time

current_direcotry = os.path.dirname(os.path.realpath(__file__))

if not(os.path.exists(current_direcotry+'/info.txt')):
    info_file = open(current_direcotry+'/info.txt', 'w')
    info_file.close()

with open(current_direcotry+'/info.txt', "r") as file:
    lines = file.readlines()
    file.close()

for line in lines:
    line

if len(lines) > 1:
    use_path = input("Do you want to use last path? (y/n): ")
    while use_path != "y" and use_path != "n":
        use_path = input("Do you want to use last path? (y/n): ")

    if use_path == "y":
        file_path = lines[0].replace("\n","")
    else:
        file_path = input("Insert file path: ")

    if lines[1].replace("\n","") == "y":
        use_cred = input("Do you want to use previous credentials? (y/n): ")
        while use_cred != "y" and use_cred != "n":
            use_cred = input("Do you want to use previous credentials? (y/n): ")
    else:
        FTP_HOST = input("Insert FTP Host: ")
        FTP_USER = input("Insert FTP User: ")
        FTP_PASS = input("Insert FTP Password: ")


else:
    file_path = input("Insert file path: ")

    FTP_HOST = input("Insert FTP Host: ")
    FTP_USER = input("Insert FTP User: ")
    FTP_PASS = input("Insert FTP Password: ")

    lines.append(file_path)


last_mod = 0

if use_cred == "y":
    FTP_HOST = lines[2].replace("\n","")
    FTP_USER = lines[3].replace("\n","")
    FTP_PASS = lines[4].replace("\n","")
else:
    FTP_HOST = input("Insert FTP Host: ")
    FTP_USER = input("Insert FTP User: ")
    FTP_PASS = input("Insert FTP Password: ")


if len(lines) == 1 or (len(lines)>1 and lines[1].replace("\n","")=="n"):
    save_cred = input("Do you want to save your credentials for future usage? (y/n): ")
    while save_cred != "y" and save_cred != "n":
        save_cred = input("Do you want to save your credentials for future usage? (y/n): ")
    lines.append(save_cred)

if len(lines) > 1 and lines[1].replace("\n","") == "y":
    if len(lines) > 3:
        lines[2] = FTP_HOST
        lines[3] = FTP_USER
        lines[4] = FTP_PASS
    else:
        lines.append(FTP_HOST)
        lines.append(FTP_USER)
        lines.append(FTP_PASS)

print(lines)

with open(current_direcotry+'/info.txt', "w") as file:
    for line in lines:
        file.write(line.replace("\n","")+"\n")
    file.close()


print("Initializing program...")

def upload():
    session = ftplib.FTP(FTP_HOST,FTP_USER,FTP_PASS)
    file = open(file_path,'rb')                  # file to send
    session.storbinary('STOR redavide/sass/master.min.css', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
    pass

try:
    while True:
        if time.ctime(os.path.getmtime(file_path)) != last_mod:
            if last_mod != 0:
                print("Uploading")
                upload()
            last_mod = time.ctime(os.path.getmtime(file_path))
        time.sleep(1)



except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
