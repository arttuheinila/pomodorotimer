  # Pomodoro timer

Pomodoro Work Timer Program that times your work in 25 minute sprints, after which the program starts a 5 minute break. The timer logs your working habits to a file separate file. After 4 pomodoros the program activates a longer break
Program includes a changing GUI that has distinct color and location on screen to signal whether you should be working or taking a break.

Note: The latest version is made to work with Linux so there might be problems with Windows.
  For Windows with the music to signal completion of a working sprint I have used  :
        subprocess.Popen(['start', 'smb3_airship_clear.wav'], shell=True)
        time.sleep(10)
        os.system('TASKKILL /F /IM mpc-be64.exe')

Python, GUI, Access file system
