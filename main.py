import password_checker 
from report import PDF
import os

# Taking user input for both hash file and password's list (against which the hash will be compared)
user_input = input("Enter name/path of your file: ")
password_checker.T_file = input("Enter name/path of weak password's file: " )

# pdf stuff    
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)

# For printing the results (if found then print else do nothing) and percentage
with open(user_input,'r') as source_file:
    all_lines = 0
    vul_lines = 0
    for k in source_file:
        if k.strip():
            all_lines += 1
            hash = ""
            hash = k.rstrip()
            cracked_password1 = password_checker.crack_sha1_hash(hash)
            if cracked_password1 == False:
                pass
            else:
                pdf.cell(0, 10, ' Found ' + '('+str(cracked_password1)+')' + ' for ' + '('+str(hash)+')', 0, 1)
                vul_lines += 1
        else:
            pass

# naming the pdf file with counter in ascending order
increment = 0
filename = "report{}.pdf"
while os.path.isfile(filename.format(increment)):
    increment += 1
filename = filename.format(increment)


a = password_checker.percent(vul_lines,all_lines) 
b = str(a)

# printing final text related to the percentage
pdf.set_font('Arial', 'I', 14)
pdf.cell(80)
pdf.cell(81, 10, ' Percentage of your Vulnerable Passwords is ')
# + b + '%', 0, 1,'C')
print(a)
print(type(a))
pdf.percentage_to_round_chart(a, 50, "red")

# generating pdf and then opening it
pdf.output(filename,'F')
os.system(filename)


    

