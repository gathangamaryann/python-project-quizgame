print("welcome to my computer quiz!")

playing = input ("do you want to play? ")

if playing.lower != "yes":
    

    print("okay! let's play:)")
    score=0

    answer =input("what does Cpu stands for? ")
    if answer.lower == "central process unit":
        print('correct!') 
        score +=1
        
    else:
        print('incorrect!')    
        
    answer =input("what does Psu stands for? ")
    if answer.lower == "Power supply":
        print('correct!') 
        score +=1
    else:
        print('incorrect!')  

    answer =input("what does Gpu stands for? ")
    if answer.lower == "Graphics process unit":
        print('correct!') 
        score +=1
    else:
        print('incorrect!')    
          
        
    answer =input("what does RAM stands for? ")
    if answer.lower == "Random acess memory":
        print('correct!') 
        score +=1
    else:
        print('incorrect!')   

        print("you got" +str(score) +"question corect!") 
        print("you got" +str((score / 4) * 100))
         