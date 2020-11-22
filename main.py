from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import random

Builder.load_file("main.kv")


class Game(Widget):
	
	check = ObjectProperty(None)
	pcimage = ObjectProperty(None)
	userimage = ObjectProperty(None)

	
	def rock(self):
		images = ["img/rock.jpg","img/papper.png","img/scissor.jpg"]
		self.userimage.source = "img/rock.jpg"
		self.pcimage.source = random.choice(images)
		# Check who won
		if self.pcimage.source == "img/papper.png":
			self.check.text = "You lose!"
		elif self.pcimage.source == "img/scissor.jpg":
			self.check.text = "You won!"
		else:
			self.check.text = "Draw!"

	def papper(self):
		images = ["img/rock.jpg","img/papper.png","img/scissor.jpg"]
		self.userimage.source = "img/papper.png"
		self.pcimage.source = random.choice(images)
		# Check who won
		if self.pcimage.source == "img/scissor.jpg":
			self.check.text = "You lose!"
		elif self.pcimage.source == "img/rock.jpg":
			self.check.text = "You won!"
		else:
			self.check.text = "Draw!"


	def scissor(self):
		images = ["img/rock.jpg","img/papper.png","img/scissor.jpg"]
		self.userimage.source = "img/scissor.jpg"
		self.pcimage.source = random.choice(images)
		# Check who won
		if self.pcimage.source == "img/rock.jpg":
			self.check.text = "You lose!"
		elif self.pcimage.source == "img/papper.png":
			self.check.text = "You won!"
		else:
			self.check.text = "Draw!"


class MainApp(App):
	def build(self):
		return Game()


if __name__ == '__main__':
	MainApp().run()
