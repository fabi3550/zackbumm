from gtts import gTTS
import time
import os

zahl=1
zackbummlang = 'de'
numberslang = 'ru'

while True:

	try:
		if (zahl % 3) == 0 and (zahl % 5) == 0:
			tts = gTTS(text='zack bumm', lang=zackbummlang)
		elif (zahl % 3) == 0 and (zahl % 5) > 0:
			tts = gTTS(text='zack', lang=zackbummlang)
		elif (zahl % 3) > 0 and (zahl % 5) == 0:
			tts = gTTS(text='bumm', lang=zackbummlang)
		else:
			tts = gTTS(text=str(zahl), lang=numberslang)
		
		tts.save("out.mp3")
		os.system("mpg123 out.mp3 --quiet")
		zahl = zahl + 1
		time.sleep(0.4)
		
	except gtts.tts.gTTSError as e:
		print(e)
		
	except OSError as e:
		print(e)

