#importing tkinter module
from tkinter import *      #imporing all modules avilable in tkinter


class LoanCalculator:
    def __init__(self):
        window=Tk()
        window.title("Loan Calculator App")
        window.configure(background="black")
        window.geometry("600x300")
        window.resizable(width=False,height=False)
        #adding Labels
        Anual_Interst_rate=Label(window,font="Helvetica 14 bold",text="Anual Interst Rate",bg="black",fg="white")
        Anual_Interst_rate.grid(column=0,row=0,padx=15)

        Number_of_Year=Label(window,font="Helvetica 14 bold",text="Number of Year",bg="black",fg="white")
        Number_of_Year.grid(column=0,row=1,padx=15)

        Loan_Amount=Label(window,font="Helvetica 14 bold",text="Loan Amount",bg="black",fg="white")
        Loan_Amount.grid(column=0,row=2,padx=15)

        Monthly_Payment=Label(window,font="Helvetica 14 bold",text="Monthly Payment",bg="black",fg="white")
        Monthly_Payment.grid(column=0,row=3,padx=15)

        Total_Payment=Label(window,font="Helvetica 14 bold",text="Total Payment",bg="black",fg="white")
        Total_Payment.grid(column=0,row=4,padx=15)


        #adding variable

        self.AnualInterstRateVar=StringVar()
        Entry(window,textvariable=self.AnualInterstRateVar,justify=RIGHT).grid(row=0,column=4)

        self.NumberofYearVar=StringVar()
        Entry(window,textvariable=self.NumberofYearVar,justify=RIGHT).grid(row=1,column=4)

        self.LoanAmountVar=StringVar()
        Entry(window,textvariable=self.LoanAmountVar,justify=RIGHT).grid(row=2,column=4)

        self.MonthlyPaymentVar=StringVar()
        lblMonthlyPayment=Label(window,font="Helvetica 14 bold",textvariable=self.MonthlyPaymentVar,bg="black",fg="white")
        lblMonthlyPayment.grid(row=3,column=4)

        self.TotalPaymentVar=StringVar()
        lblTotalPayment=Label(window,font="Helvetica 14 bold",textvariable=self.TotalPaymentVar,bg="black",fg="white")
        lblTotalPayment.grid(row=4,column=4)



        #creating button

        btnComputePayment=Button(window,text="Compute Payment",bg="green",fg="white",command=self.ComputePayment)
        btnComputePayment.grid(row=5,column=0)

        clear_btn=Button(window,text="Clear",bg="white",fg="black",command=self.clear)
        clear_btn.grid(row=5,column=4)





        window.mainloop()
    def ComputePayment(self):
        Monthly_Payment=self.getMonthly_Payment(
        float(self.LoanAmountVar.get()),
        float(self.AnualInterstRateVar.get()) /1200 ,
        int(self.NumberofYearVar.get()))

        self.MonthlyPaymentVar.set(format(Monthly_Payment, '10.2f'))
        Total_Payment=float(self.MonthlyPaymentVar.get())*12 \
        *int(self.NumberofYearVar.get())
        self.TotalPaymentVar.set(format(Total_Payment, '10.2f'))

    def getMonthly_Payment(self,Loan_Amount,monthly_Interst_rate,Number_of_Year):
        Monthly_Payment=Loan_Amount*monthly_Interst_rate/(1-1/(1+monthly_Interst_rate)**(Number_of_Year*12))
        return Monthly_Payment



    def clear(self):
        self.AnualInterstRateVar.set("")
        self.NumberofYearVar.set("")
        self.LoanAmountVar.set("")
        self.MonthlyPaymentVar.set("")
        self.TotalPaymentVar.set("")
















LoanCalculator()
