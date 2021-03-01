#Change test for github
#SDEV 140 Celsius to Fahrenheit Ch. 13 Ex. 4
#Reuben A. McFarland
#A program that converts from Celsius to Fahrenheit (and the other way) with a graphical interface


import tkinter
import tkinter.messagebox



class MyGUI:
    def __init__(self):
        #Main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Celsius to Fahrenheit')

        #Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.radio_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Pack Frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.radio_frame.pack()
        self.bottom_frame.pack()

        #Prompt
        self.lable1 = tkinter.Label(self.top_frame, text = 'Enter a temperature') 
        self.lable1.pack(side = 'left')

        #Text entry
        self.temp_enter = tkinter.Entry(self.middle_frame, width = 10)
        self.temp_enter.pack(side = 'left')

        #Radio buttons
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.radio1 = tkinter.Radiobutton(self.radio_frame, text = 'Celsius', variable = self.radio_var, value = 1)
        self.radio2 = tkinter.Radiobutton(self.radio_frame, text = 'Fahrenheit', variable = self.radio_var, value = 2)
        self.radio1.pack(side = 'left')
        self.radio2.pack(side = 'left')
        
        #Exit button
        self.exit_button = tkinter.Button(self.bottom_frame, text = 'Exit', command = self.main_window.destroy)
        self.exit_button.pack(side = 'left', padx = 2, pady = 10)
        #calculate button
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Calculate', command = self.do_calc)
        self.calc_button.pack(side = 'left', padx = 2, pady = 10)

        #Start the interface
        tkinter.mainloop()


    #Callback for calculate button
    def do_calc(self):
        tempToConvert = 0.0
        convertedTemp = 0.0

        try:        
            tempToConvert = float(self.temp_enter.get())
            if int(self.radio_var.get()) == 1:#Celsius to Fahrenheit
                self.temp_enter.delete(0, 'end')#Clear old entry
                convertedTemp = 9.0/5.0 * tempToConvert + 32      
                answerMessage = "C to F is {0:.2f}".format(convertedTemp)
                tkinter.messagebox.showinfo(title ='Answer', message = answerMessage)
            else:#Fahrenheit to Celsius
                self.temp_enter.delete(0, 'end')#Clear old entry
                convertedTemp = (tempToConvert - 32) *5.0/9.0 
                answerMessage = "F to C is {0:.2f}".format(convertedTemp)
                tkinter.messagebox.showinfo(title ='Answer', message = answerMessage)
        except:
            tkinter.messagebox.showwarning(title = 'Error', message = 'Error, not a valid entry')

          


        

        

        
def main():
    my_gui = MyGUI()
    






















if __name__ == "__main__":
    main()
