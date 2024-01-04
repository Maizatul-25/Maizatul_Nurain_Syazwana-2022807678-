import tkinter as tk
import mysql.connector

# Connect to your MySQL database 
mydb = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="", 
    database="muet_test_for_repeater" 
)

# Create a cursor object to execute SQL queries 
mycursor = mydb.cursor() 
 

# Function to insert data into the table
def collect_data():
    name = name_entry.get()
    age = age_entry.get()
    ic = ic_entry.get ()
    semester = semester_type.get ()

    package =  package_type.get()
    category = int(category_type.get())

    prices = {
        "Package Smart": 100,
        "Package Intelligent": 150,
        "Package Brilliant": 175,
        }
    
    total_price = (prices[package]*category)
    output_label.config(text=f"package: {package}, \ncategory: {category}, \n\nTotal Price: RM{total_price}")

    print("Name:",name)
    print("Age:", age)
    print("Ic:", ic)
    print("Semester:", semester)

    # To insert data 
    sql = "INSERT INTO registration (NAME, AGE, IC, SEMESTER, PACKAGE, CATEGORY) VALUES (%s, %s, %s,%s, %s, %s )" 
    val = (name,age,ic,semester, package, category) 
    mycursor.execute(sql, val) 
    mydb.commit() 

    

 

# Tkinter GUI
root = tk.Tk()
root.title("MySQL Database with Tkinter")
root.geometry("1000x700")
root.configure (bg= "#FFB90F") 

#Page title= 

label = tk.Label (root, text= 'MUET TEST FOR REPEATER', font= ("calibri", 15, "bold") , fg= "blue" , bg = "orange") 
label.pack (ipadx=6 , ipady=6)
#frame= 

frame = tk.Frame(root, bg="#FFB90F")
frame.pack()

#information about student=
#frame(bingo)=

bingo= tk.LabelFrame(frame, text="", bg="#FFB90F")
bingo.grid (row=1, column=1, sticky="News", ipadx= 4, ipady= 4)

label_name = tk.Label(bingo, text="Name:", font=("calibri", 14, "bold" ) , fg="#8B7D6B", bg="orange")
label_name.pack()
name_entry = tk.Entry(bingo)
name_entry.pack()

label_age = tk.Label(bingo, text="Age:", font=("calibri", 14, "bold" ) , fg="#8B7D6B", bg="orange")
label_age.pack()
age_entry = tk.Entry(bingo)
age_entry.pack()

label_ic = tk.Label (bingo, text="Ic:", font=("calibri", 14, "bold" ) , fg="#8B7D6B", bg="orange")
label_ic.pack()
ic_entry = tk.Entry(bingo)
ic_entry.pack()

label_semester = tk.Label (bingo, text="Semester:",font=("calibri", 14, "bold" ) , fg="#8B7D6B", bg="orange")
label_semester.pack()
semester_type= tk.StringVar (bingo)
semester_type.set("Select your Semester")
semester_dropdown= tk.OptionMenu (bingo, semester_type, 1, 2, 3, 4, 5, 6 )
semester_dropdown.pack(pady=10)


#Choosing test =
#frame(kirby)=

kirby= tk.LabelFrame(frame, text="", bg="#FFB90F")
kirby.grid (row=0, column=0, sticky="News", ipadx= 1, ipady= 1)


packs_Label = tk.Label (kirby, text= "Here are the Test", font= ("calibri", 13, "bold") , fg= "blue" , bg = "orange")
packs_Label.pack(padx=3, pady=10,)

packs_Label = tk.Label (kirby, text= "Test A= Listening Test", font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)

packs_Label = tk.Label (kirby, text= "Test B= Writting Test", font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)

packs_Label = tk.Label (kirby, text= "Test C= Oral Test", font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)



# Choosing the test based on package 
# frame(aum)

aum= tk.LabelFrame(frame, text="", bg="#FFB90F")
aum.grid (row=0, column=2, sticky="News", ipadx= 1, ipady= 1)


packs_Label = tk.Label (aum, text= "Here are the Test based on Package" ,font= ("calibri", 13, "bold") , fg= "blue" , bg = "orange")
packs_Label.pack(padx=3, pady=10)

packs_Label = tk.Label (aum, text= "Package smart=  Test A + Test B" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2) 

packs_Label = tk.Label (aum, text= "Package Intelligent=  Test B + Test C",font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)

packs_Label = tk.Label (aum, text= "Package Brilliant =  Test A +  Test B  + Test C" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)



lala= tk.LabelFrame(frame, text="", bg="#FFB90F")
lala.grid (row=0, column=4, sticky="News", ipadx= 1, ipady= 1)


packs_Label = tk.Label (aum, text= "The Prices" ,font= ("calibri", 13, "bold") , fg= "blue" , bg = "orange")
packs_Label.pack(padx=3, pady=10)

packs_Label = tk.Label (aum, text= "Package Smart= RM 100" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2) 

packs_Label = tk.Label (aum, text= "Package Intelligent=  RM 150" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)

packs_Label = tk.Label (aum, text= "Package Brilliant = RM 175" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)


#choosing the Category
#frame (ish)

ish= tk.LabelFrame(frame, text="", bg="#FFB90F")
ish.grid (row=0, column=1 , sticky="News", ipadx= 1, ipady= 1)


packs_Label = tk.Label (ish, text= "The Repeater category" ,font= ("calibri", 13, "bold") , fg= "blue" , bg = "orange")
packs_Label.pack(padx=3, pady=10)

packs_Label = tk.Label (ish, text= "if you are once repeater: please select 1" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2) 

packs_Label = tk.Label (ish, text= "if you are twice repeater: please select 2" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)

packs_Label = tk.Label (ish, text= "if you are thrice repeater: please select 3" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)

packs_Label = tk.Label (ish, text= "P/S: The price based is multipication of the price and how many times you repeat" ,font= ("calibri", 11, ) , fg= "white" , bg = "orange")
packs_Label.pack(padx=2, pady=2)


#choosing the option 
#frame (nono)


nono= tk.LabelFrame(frame, text="", bg="#FFB90F")
nono.grid (row=1, column=0, sticky="News", ipadx= 1, ipady= 1)

packs_Label = tk.Label (nono, text= "Option", font= ("calibri", 13, "bold") , fg= "blue" , bg = "orange")
packs_Label.pack(padx=3, pady=10,)

package_type= tk.StringVar (nono)
package_type.set("Select your package")
package_dropdown= tk.OptionMenu (nono, package_type, "Package Smart", "Package Intelligent", "Package Brilliant" )
package_dropdown.pack(pady=10)

category_type= tk.StringVar (nono)
category_type.set("Select your category")
category_dropdown= tk.OptionMenu (nono, category_type, 1, 2, 3 )
category_dropdown.pack(pady=10) 



# Buttons to perform operations
# Buttons grid

save_button = tk.Button(root, text="Done", command= collect_data)
save_button.place (x= 800, y = 450, width= 80, height= 50)

#prices 
#frame (nais)

nais= tk.LabelFrame(frame, text="", bg="#FFB90F")
nais.grid (row=1, column=2, sticky="News", ipadx= 1, ipady= 1)

label= tk.Label(nais,text= 'total price', font= ("calibri",12,))
label.pack(ipadx=10, ipady=10) 

output_label= tk.Label(nais ,text="")
output_label.pack(ipadx=15,ipady=10)




root.mainloop() 