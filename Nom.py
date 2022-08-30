from tkinter import ttk
from tkinter import *
import sqlite3

class product: 
    
    db_name = 'My_database.db'

    def __init__(self, window):         #Constructor que hace que cada vez que se inicia la clase, ejecute una instancia que le de nombre a la ventana de la aplicacion  
        self.wind = window
        self.wind.title('Products Aplication')
        
#Creación del frame para adaptar los elementos
        frame = LabelFrame(self.wind, text = 'Register a new Product')
        frame.grid(row = 0, column = 0, columnspan= 3, pady=20)
                
#Creación de input: Employee_Name, Employee_LastName, Basic Wage, Worked_Days and ID Document
        Label(frame, text = 'Employee Name: ').grid(row =1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column = 1)
        
        Label(frame, text = 'Employee Last Name: ').grid(row =2, column = 0)
        self.lname = Entry(frame)
        self.lname.grid(row=2, column = 1)

        Label(frame, text = 'Id Document: ').grid(row =3, column = 0)
        self.document = Entry(frame)
        self.document.grid(row=3, column = 1)
        
        Label(frame, text = 'Basic Wage: ').grid(row =4, column = 0)
        self.wage = Entry(frame)
        self.wage.grid(row=4, column = 1)
        
        Label(frame, text = 'Worked Days: ').grid(row =5, column = 0)
        self.workdays = Entry(frame)
        self.workdays.grid(row=5, column = 1)
  
    
        #Boton Entrada de Productos
        ttk.Button(frame, text= ' SaveProduct ', command=self.add_product).grid(row = 6, columnspan= 2, sticky =W + E)
        

        #Mensajes de alerta
        self.message = Label(text='', fg = 'red')
        self.message.grid(row = 3, column=0, columnspan= 2, sticky= W+E)
        
        #Creación de la tabla con detalles del empleado:
        self.tree = ttk.Treeview(height = 10, columns= ('#1', '#2', '#3','#4','#5'))
        self.tree['show'] = 'headings'
        self.tree.grid(row = 7, column = 0, columnspan = 6)
        self.tree.heading('#1', text = 'Name', anchor= CENTER)
        self.tree.heading('#2', text = 'LastName', anchor= CENTER)
        self.tree.heading('#3', text = 'Id Document', anchor= CENTER)
        self.tree.heading('#4', text = 'Wage', anchor= CENTER)
        self.tree.heading('#5', text = 'Worked Days', anchor= CENTER)
        
        
        
        
        # Botones de la tabla para borrar registro
        ttk.Button(text = 'DELETE', command=self.delete_employee).grid(row = 8, column=2, sticky= W + E)
        ttk.Button(text = 'EDIT').grid(row = 8, column=3, sticky= W + E) 
        self.get_employees()
       
       
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result =  cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_employees (self):
        #lIMPIAR TABLE
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
            
        #query
        query = 'SELECT * FROM employees ORDER BY name DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[0])
            
            
    def validation(self):
        return len(self.name.get()) != 0 and len(self.lname.get()) != 0       
    
    
    
    def add_product(self):
        if self.validation():
            query = 'INSERT INTO employees VALUES (?, ?)'
            parameters = (self.name.get(), self.lname.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Empleado {} añadido satisfactoriamente'.format(self.name.get())
            self.name.delete(0, END)
            self.lname.delete(0, END)
        
        else:
            self.message['text'] = 'Nombre y Precio son requeridos'
        self.get_employees()
        
        
    def delete_employee(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Porfavor elija un empleado para eliminar su registro'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        quey = 'DELETE FROM employees WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Registro {} eliminado satisfactoriamente'.format(name)
        self.get_employees()
        
if __name__ == '__main__':
    window = Tk()
    application = product (window)
    window.mainloop()