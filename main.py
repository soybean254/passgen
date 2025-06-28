import customtkinter as ctk

from generator import generate_password

number_of_symbols = 18
def display_password(number_of_symbols):
    #очищаем виджет
    text_output.delete(0,'end')
    #выводим пароль в виджет
    text_output.insert(0,generate_password(number_of_symbols))
#настройка интерфейса
ctk.set_appearance_mode('dark')
#окно программы
root = ctk.CTk()

root.title("Pass generator")

root.resizable(0,0)

#виджеты (1 поле для ввода)(2 размещаем виджет в окне)(3 настройка текста и вводной строки)
text_output = ctk.CTkEntry(root,
                         placeholder_text='password',
                         corner_radius=90,
                         width=16*number_of_symbols,
                         height=40,
                         justify='center',
                         font=('monospase', 20,'bold'))

text_output.grid(column = 0, row = 0, padx = 40, pady = 40)
#виджет номер (4 кнопка)
#настройки  кнопки
pass_btn = ctk.CTkButton(root,
                         text='Generate',
                         fg_color='green',
                         hover_color='black',
                         corner_radius=90,
                         font=('sans-serif', 20, 'bold'),
                         height = 40,
                         command=lambda: display_password(number_of_symbols))

pass_btn.grid(column = 0, row = 1, padx = 40, pady = (0,40), sticky = 'we' )

root.mainloop()