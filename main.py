from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics','width','350')
Config.set('graphics','height','500')

class Desktop(BoxLayout):
    # needed for hiding and unhiding history labels and buttons
    activate = True 

    # variable that contains all text that is represented as history
    history_output = ''

# activated when equal sign button is pressed 
    def btn_equal(self):
        self.history_output += self.label_output.text +'='
        try: 
            result = eval(self.label_output.text)
        except:
            result = False
        self.label_output.text = str(result)
        self.history_output += str(result)+'\n'
        
        if self.history_output.count('\n')>3:
            print('True')
            self.history_output = ' '.join(w+'\n' for w in self.history_output.split()[1:])
            print(self.history_output)
        
        self.history_label.text = self.history_output
        
 


# adds simple symbols like 1 2 3 + or 9 - / *
    def btn_add_symbol(self, instance):
        if  instance.text == '.' and self.label_output.text == "0":
            pass
        elif self.label_output.text == '0' or self.label_output.text == 'False' :
            self.label_output.text = ''
        if instance.text == 'x':
            self.label_output.text+='*'
        else:self.label_output.text+=instance.text

# delte the last symbol
    def btn_backspace(self):
        self.label_output.text = self.label_output.text[:-1]
    
    
    def add_parenthesis(self):
        if self.label_output.text.count('(')==0:
            self.label_output.text+='('
        elif self.label_output.text.count('(')>self.label_output.text.count(')'):
            self.label_output.text+=')'
        elif self.label_output.text.count('(') == self.label_output.text.count(')'):
            self.label_output.text+='('
        else:
            self.label_output.text+='('

# clears all output 
    def btn_clear_all(self):
        self.label_output.text = '0'

# manages history button, hides it and unhides it when needed 
    def btn_history(self,instance):
        if self.activate == False:
            self.history_label.size_hint, self.history_label.opacity, self.history_label.disabled = (0,0),0,True
            self.clean_history_btn.size_hint, self.clean_history_btn.opacity, self.clean_history_btn.disabled = (0,0),0,True
            self.activate = True
            instance.text = 'Hisotry'
        else:
            self.history_label.size_hint, self.history_label.opacity, self.history_label.disabled = (1,.7),1,False
            self.clean_history_btn.size_hint, self.clean_history_btn.opacity, self.clean_history_btn.disabled = (1,.1),1,False
            self.activate = False
            instance.text = 'Less'
        print(self.activate)

# cleans all history output
    def clean_history(self):
        self.history_output = ''
        self.history_label.text = ''
    

class CalculatorApp(App):
    def build(self):
        b  = BoxLayout()
        b.add_widget(Desktop())
        return b


def main():
    CalculatorApp().run()

if __name__ == '__main__':
    main()