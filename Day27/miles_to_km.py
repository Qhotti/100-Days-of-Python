import tkinter as tk

window = tk.Tk()
window.title('Miles to Kilometer Converter')
window.minsize(width=200, height=100)
window.config(padx=20,pady=20)

def button_clicked():
    miles = round(int(input.get()) * 1.609 , 1)
    km_result.config(text=miles)

equal_to_label = tk.Label(text = 'is equal to', font = ('Arial',10,'bold'))
equal_to_label.grid(column=0, row=1)
equal_to_label.config(padx=10)

input = tk.Entry(width = 10)
input.grid(column=1,row=0)

km_result = tk.Label(text = 0, font = ('Arial',10))
km_result.grid(column=1, row=1)

button = tk.Button(text = 'Calculate', command=button_clicked)
button.grid(column=1,row=2)

m_label = tk.Label(text = 'Miles', font = ('Arial',10,'bold'))
m_label.grid(column=2, row=0)
m_label.config(padx=10)


km_label = tk.Label(text = 'Km', font = ('Arial',10,'bold'))
km_label.grid(column=2, row=1)
km_label.config(padx=10)








window.mainloop()