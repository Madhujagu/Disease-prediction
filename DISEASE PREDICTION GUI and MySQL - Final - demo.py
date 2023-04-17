
from tkinter import * 
import numpy as np
import pandas as pd
# from gui_stuff import *
import mysql.connector
import tkinter.messagebox

def MAIN():
  R1=Tk()
  R1.geometry('700x500')
  R1.title('WELCOME-1')
  l=Label(R1, text="WELCOME TO DISEASE PREDICTION PORTAL", font=('algerain',14,'bold'), fg="orange")
  l.place(x=100, y=50)

  b1=Button(R1, text="Register",width=10,height=2,font=('algerain',14), bg="lightblue", fg="red", command=m1)
  b1.place(x=200, y=200)
  
  b2=Button(R1, text="Login",width=10,height=2, font=('algerain',14), bg="lightblue", fg="red", command=m3)
  b2.place(x=200, y=300)
  
  R1.mainloop()



def m1():
  def m2():
    username=e1.get()
    password=e2.get()
    email=e3.get()
    phoneno=e4.get()

    a=mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", database="disease prediction")
    b=a.cursor()
    b.execute("INSERT INTO t1 VALUES(%s,%s,%s,%s)",(username,password,email,phoneno))
    a.commit()

    if e1.get()=="" or e2.get=="":
      tkinter.messagebox.showinfo("SORRY!, PLEASE COMPLETE THE REQUIRED INFORMATION")
    else:
      tkinter.messagebox.showinfo("WELCOME %s" %username, "Lets Login")
      m3()

    
  R2=Tk()
  R2.geometry('600x500')
  R2.title('Register and Login')

  l=Label(R2, text="Login & Register", font=('algerain',14,'bold'), fg="orange")
  l.place(x=200, y=50)

  l1=Label(R2, text="Username", font=('algerain',14), fg="black")
  l1.place(x=100, y=200)
  l2=Label(R2, text="Password", font=('algerain',14), fg="black")
  l2.place(x=100, y=250)
  l3=Label(R2, text="Email", font=('algerain',14), fg="black")
  l3.place(x=100, y=300)
  l4=Label(R2, text="Phoneno", font=('algerain',14), fg="black")
  l4.place(x=100, y=350)
  
  e1=Entry(R2, font=14)
  e1.place(x=200, y=205)
  e2=Entry(R2, font=14, show="**")
  e2.place(x=200, y=255)
  e3=Entry(R2, font=14)
  e3.place(x=200, y=305)
  e4=Entry(R2, font=14)
  e4.place(x=200, y=355)

  b1=Button(R2, text="Signup",width=8,height=1, font=('algerain',14), bg="lightblue", fg="red", command=m2)
  b1.place(x=250, y=400)
      
  R2.mainloop()


def m3():
    def m4():
        a=mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", database="disease prediction")
        b=a.cursor()
        username=e1.get()
        password=e2.get()

        if (e1.get()=="" or e2.get()==""):
            tkinter.messagebox.showinfo("SORRY!, PLEASE COMPLETE THE REQUIRED INFORMATION")
        else:
            b.execute("SELECT * FROM t1 WHERE username=%s AND password=%s",(username,password))

            if b.fetchall():
                tkinter.messagebox.showinfo("WELCOME %s" % username, "Logged in successfully")
                m5()#from function def m5() Function call for Fraud Detection
                
            else:
                tkinter.messagebox .showinfo("Sorry", "Wrong Password")
            
        
    R3=Tk()
    R3.geometry('600x500')
    R3.title('Login')

    l=Label(R3, text="Login", font=('algerain',14,'bold'), fg="orange")
    l.place(x=200, y=50)

    l1=Label(R3, text="Username", font=('algerain',14), fg="black")
    l1.place(x=100, y=200)
    l2=Label(R3, text="Password", font=('algerain',14), fg="black")
    l2.place(x=100, y=250)
      
    e1=Entry(R3, font=14)
    e1.place(x=200, y=205)
    e2=Entry(R3, font=14, show="**")
    e2.place(x=200, y=255)

    b1=Button(R3, text="Login",width=8,height=1, font=('algerain',14), bg="lightblue", fg="red", command=m4)
    b1.place(x=250, y=400)

    R3.mainloop()

def m5():
  R1=Tk()
  R1.geometry('700x600')
  R1.title('WELCOME-2')

  l=Label(R1, text="DISEASE PREDICTION using ML", font=('algerain',18,'bold'), fg="orange")
  l.place(x=150, y=50)

  b1=Button(R1, text="Prediction",width=18,height=2,font=('algerain',14), bg="lightblue", fg="red", command=algorithm_selection)
  b1.place(x=150, y=250)
  
  R1.mainloop()

  
def algorithm_selection():

  l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
  'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
  'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
  'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
  'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
  'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
  'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
  'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
  'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
  'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
  'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
  'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
  'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
  'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
  'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
  'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
  'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
  'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
  'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
  'yellow_crust_ooze']

  disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
  'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
  ' Migraine','Cervical spondylosis',
  'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
  'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
  'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
  'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
  'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
  'Impetigo']

  l2=[]
  for x in range(0,len(l1)):
      l2.append(0)

  # TESTING DATA df -------------------------------------------------------------------------------------
  df=pd.read_csv("Training.csv")

  df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
  'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
  'Migraine':11,'Cervical spondylosis':12,
  'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
  'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
  'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
  'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
  '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
  'Impetigo':40}},inplace=True)

  # print(df.head())

  X= df[l1]

  y = df[["prognosis"]]
  np.ravel(y)  #retuns 1D array
  # print(y)

  # TRAINING DATA tr --------------------------------------------------------------------------------
  tr=pd.read_csv("Testing.csv")
  tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
  'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
  'Migraine':11,'Cervical spondylosis':12,
  'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
  'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
  'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
  'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
  '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
  'Impetigo':40}},inplace=True)

  X_test= tr[l1]
  y_test = tr[["prognosis"]]
  np.ravel(y_test)
  # ------------------------------------------------------------------------------------------------------

  def DecisionTree():

      from sklearn import tree

      clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
      clf3 = clf3.fit(X,y)

      # calculating accuracy-------------------------------------------------------------------
      from sklearn.metrics import accuracy_score
      y_pred=clf3.predict(X_test)
      print('Accuracy:',accuracy_score(y_test, y_pred))
      #print(accuracy_score(y_test, y_pred,normalize=False))
      # -----------------------------------------------------

      psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

      for k in range(0,len(l1)):
          # print (k,)
          for z in psymptoms:
              if(z==l1[k]):
                  l2[k]=1

      inputtest = [l2]
      predict = clf3.predict(inputtest)
      predicted=predict[0]

      h='no'
      for a in range(0,len(disease)):
          if(predicted == a):
              h='yes'
              break


      if (h=='yes'):
          t1.delete("1.0", END)
          t1.insert(END, disease[a])
      else:
          t1.delete("1.0", END)
          t1.insert(END, "Not Found")


  # gui_stuff------------------------------------------------------------------------------------

  root = Tk()
  root.configure(background='blue')

  # entry variables
  Symptom1 = StringVar()
  Symptom1.set(None)
  Symptom2 = StringVar()
  Symptom2.set(None)
  Symptom3 = StringVar()
  Symptom3.set(None)
  Symptom4 = StringVar()
  Symptom4.set(None)
  Symptom5 = StringVar()
  Symptom5.set(None)
  Name = StringVar()

  # Heading
  w2 = Label(root, justify=LEFT, text="Disease Predictor using Machine Learning", fg="white", bg="blue")
  w2.config(font=("Elephant", 30))

  w2.grid(row=1, column=0, columnspan=2, padx=100)
  w2 = Label(root, justify=LEFT, text="A Project by Madhu", fg="white", bg="blue")

  w2.config(font=("Aharoni", 30))
  w2.grid(row=2, column=0, columnspan=2, padx=100)

  # labels
  NameLb = Label(root, text="Name of the Patient", fg="yellow", bg="black")
  NameLb.grid(row=6, column=0, pady=15, sticky=W)


  S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="black")
  S1Lb.grid(row=7, column=0, pady=10, sticky=W)

  S2Lb = Label(root, text="Symptom 2", fg="yellow", bg="black")
  S2Lb.grid(row=8, column=0, pady=10, sticky=W)

  S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="black")
  S3Lb.grid(row=9, column=0, pady=10, sticky=W)

  S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="black")
  S4Lb.grid(row=10, column=0, pady=10, sticky=W)

  S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
  S5Lb.grid(row=11, column=0, pady=10, sticky=W)


  lrLb = Label(root, text="DecisionTree", fg="white", bg="red")
  lrLb.grid(row=15, column=0, pady=10,sticky=W)



  # entries
  OPTIONS = sorted(l1)

  NameEn = Entry(root, textvariable=Name)
  NameEn.grid(row=6, column=1)

  S1En = OptionMenu(root, Symptom1,*OPTIONS)
  S1En.grid(row=7, column=1)

  S2En = OptionMenu(root, Symptom2,*OPTIONS)
  S2En.grid(row=8, column=1)

  S3En = OptionMenu(root, Symptom3,*OPTIONS)
  S3En.grid(row=9, column=1)

  S4En = OptionMenu(root, Symptom4,*OPTIONS)
  S4En.grid(row=10, column=1)

  S5En = OptionMenu(root, Symptom5,*OPTIONS)
  S5En.grid(row=11, column=1)


  dst = Button(root, text="DecisionTree", command=DecisionTree,bg="green",fg="yellow")
  dst.grid(row=8, column=0,padx=10)



  #textfileds
  t1 = Text(root, height=1, width=40,bg="orange",fg="black")
  t1.grid(row=15, column=1, padx=10)


  root.mainloop()
MAIN()

