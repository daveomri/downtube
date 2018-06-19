#!/usr/bin/env python3
# This program is bridge between you and file on youtube
import os
import sys
from tkinter import * # Tk, Label, Entry, OptionMenu, StringVar, LEFT, Button, END
class downtube:
	def __init__(self, gui):
		# Building Frame
		self.gui = gui
		self.formats=["mp3", "wav", "opus", "ogg", "mp4", "mkv", "3gp"]
		self.listvideo = ["mp4","mkv", "3gp"]
		self.whattodo=["Unoma", "Playlist", "File"]
		if self.gui == 1:
			try:
				# Building of frame
				self.root = Tk()
				self.root.configure(background="#191919")
				self.root.wm_title("downtube")
				self.root.minsize(430, 120)
				self.root.maxsize(430, 120)
				# Text informing user about downloading
				self.text = Label(self.root, text="Insert address", font="fixedsys 11", bg="#191919", fg="#ffffff")
				self.text.pack()
				# List of video formats
				def sendIt():
					self.urldow = self.url.get()
					self.var = self.variable.get()
					self.whatto = self.whatvariable.get()
					# If no url or path is given, just pass
					if len(self.urldow) == 0:
						pass
					else:
						# Which way to choose
						self.text.config(text="Working on it..")
						self.text.update()
						self.showmetheway()
				# Entry for url or path to file
				self.url = Entry(self.root)
				self.url.pack()
				self.url.config(width=60)
				self.url.focus_set()
				# List of formats
				self.variable = StringVar(self.root)
				self.variable.set(self.formats[0])
				self.list = OptionMenu(self.root, self.variable, *self.formats).pack(side=LEFT, padx=20, pady=20)
				# Button
				self.buttondue = Button(self.root, text="Get", command=sendIt, font="system 8 bold", bg="#19aa19", fg="#ffffff").pack(side = LEFT, padx=80, pady=20)
				# List of choices what to do with user url or path to file
				self.whatvariable = StringVar(self.root)
				self.whatvariable.set(self.whattodo[0])
				self.list = OptionMenu(self.root, self.whatvariable, *self.whattodo).pack(side=LEFT)
				# End of frame
				self.root.mainloop()
			except KeyboardInterrupt:
				exit()
			except:
				print("Sorry, something went wrong.")
				exit()
		else:
			try:
				self.whatto = input("Unoma/Playlist/File: ")
				while (self.whatto in self.whattodo) == False:
					self.whatto = input("Unoma/Playlist/File: ")
					self.urldow = input("URL/ptf: ")
				self.var = input("Format (type list to see all formats): ")
				while (self.var in self.formats) == False:
					if self.var == "list":
						for format in self.formats:
							print(format)
					else:
						print("I'm sorry, but your choice is incorrect. \n For list of available types type 'list'.")
						self.var = input("Format: ")
				self.showmetheway()
			except KeyboardInterrupt:
				exit()
			except:
				print("Sorry, something went wrong.")
				exit()
	def showmetheway(self):
		if self.var == "ogg":
			self.var = "vorbis"
		# Function for starting download
		if self.whatto == "Unoma":
			self.download_one()
		elif self.whatto == "Playlist":
			self.download_playlist()
		else:
			self.download_from_file()
	def download_one(self):
		if (self.var in self.listvideo) == True:
			if self.var == "mp4":
				os.system("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' "+str(self.urldow))
			else:
				os.system("youtube-dl --merge-output-format "+str(self.var)+" "+str(self.urldow))
		else:
			os.system("youtube-dl -i --extract-audio --audio-format " + str(self.var) + " --audio-quality 0 " + str(self.urldow))
		self.end_it()
	def download_playlist(self):
		if (self.var in self.listvideo) == True:
			if self.var == "mp4":
				os.system("youtube-dl -ic --yes-playlist -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' "+str(self.urldow))
			else:
				os.system("youtube-dl -ic --yes-playlist -f "+str(self.var)+" --audio-quality 0 "+str(self.urldow))
			#os.system("youtube-dl -ict --yes-playlist -f "+str(self.var)+" --audio-quality 0 "+str(self.urldow))
		else:
			os.system("youtube-dl -ict --yes-playlist --extract-audio --audio-format "+str(self.var)+" --audio-quality 0 "+str(self.urldow))
		self.end_it()
	def download_from_file(self):
		self.file = open(str(self.urldow), "r")
		self.listofurls = self.file.read().split("\n")
		self.file.close()
		if (self.var in self.listvideo) == True:
			if self.var == "mp4":
				self.command = "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' "
			else:
				self.command = "youtube-dl -f "+str(self.var) + " "
		else:
			self.command = "youtube-dl -i --extract-audio --audio-format " + str(self.var) + " --audio-quality 0 "
		for i in self.listofurls:
				if len(i) != 0:
					os.system(self.command+str(i))
				else:
					pass
		self.end_it()
	def end_it(self):
		if self.gui == 1:
			self.text.config(text="Insert address/path")
			self.url.delete(0, END)
		else:
			exit()
def start_program():
	if len(sys.argv) > 1:
		if str(sys.argv[1]) == "--help":
			os.system("echo '\033[0;32mdowntube\033[0m command for gui\n\033[0;32mdowntube -t\033[0m command for text-mode'")
		else:
			master = downtube(0)
	else:
		master = downtube(1)
start_program()
