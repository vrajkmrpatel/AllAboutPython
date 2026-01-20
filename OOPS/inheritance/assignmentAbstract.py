from abc import ABC, abstractmethod

# Abstract base class
class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class HPNotebook(TouchScreenLaptop):
    def scroll(self):
        print("HP Notebook: Scrolling...")
    
    def click(self):
        print("HP Notebook: Clicking...")

class DELLNotebook(TouchScreenLaptop):
    def scroll(self):
        print("DELL Notebook: Scrolling...")
    
    def click(self):
        print("DELL Notebook: Clicking...")


hp = HPNotebook()
hp.scroll()  
hp.click()   

dell = DELLNotebook()
dell.scroll()  
dell.click()   
