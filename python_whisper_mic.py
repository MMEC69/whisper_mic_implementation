from whisper_mic.whisper_mic import WhisperMic

command = input(">Program begins to record\n>To start press -s\n>To exit press -e\n>")

command = command.lower()
command2 = "-y"

if command == "-s":
    while command2 == "-y" :
        mic = WhisperMic()

        result = mic.listen()

        print(result)

        command2 = input(">Do you wish to continue.\n>if yes press -y else press -n\n>")
        command2 = command2.lower()

    print(">Exiting...")

elif(command == "-e"):
    print(">Program is closing.....")
    exit(0)

else:
    print(">An unknown error.")



