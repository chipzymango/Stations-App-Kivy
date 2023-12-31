from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from stopplaces import searchForStopPlace

class FirstScreen(Screen):
    searchTextInput = ObjectProperty(None)
    def addButton(self):
        searchTextInput = str(self.searchTextInput.text)
        newButton = Button(text=searchTextInput)
        self.ids.resultsGridLayout.add_widget(newButton)

    def findStopPlace(self):
        search = str(self.searchTextInput.text)
        stopPlaceResults = searchForStopPlace(str(search))

        for stopPlace in stopPlaceResults:
            buttonText = stopPlace["stopPlaceName"] + ", " + stopPlace["stopPlaceLocation"]
            stopPlaceButton = Button(text=buttonText)
            self.ids.resultsGridLayout.add_widget(stopPlaceButton)

class SecondScreen(Screen):
    pass

class ScreensManager(ScreenManager):
    pass

kv = Builder.load_file('stations.kv')

# subclass of kivy's app class (the root of all layouts/widgets)
class StationsApp(App):
    def build(self):
        return kv

# run
if __name__ == "__main__":
    StationsApp().run()