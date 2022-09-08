# QA - DEVOPS - PRACTICAL PROJECT
## Author - Tolu Rotimi
## Objective
* To create a application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
### Brief Outline
* The application will generata a random colour and personality and display to the user a personality associated from both.

## Services
* Service 1(Frontend)
  * This service is the user-interface
  * This sends requests to the other services and displays the personality generated 
* Service 2
  * This service recieved a HTTP Get request from service 1 and carries out the function to generate a random  
    object(colour). 
  ![image](https://user-images.githubusercontent.com/96881229/189162910-58af387d-963e-4a6a-9bc7-b591d4744a54.png)
* Service 3
  * This service recieved a HTTP Get request from service 1 and carries out the function to generate a random  
    object(personlaity). 
 ![image](https://user-images.githubusercontent.com/96881229/189163358-f7334d8e-fa71-4531-b097-d8623fba83e3.png)
* Service 4
  * This service recieved a HTTP POST request from service 1 and carries out the the function to pick out the character generated using the get requests from service 2 and 3 and display that to the use.
  
 ![image](https://user-images.githubusercontent.com/96881229/189163871-0293e8a1-7d26-4112-94c7-d839a397c97d.png)


## App Design

![image](https://user-images.githubusercontent.com/96881229/189169652-c5f7a090-60e8-44db-969c-306661cb4a6d.png)
 **Trello Board** 
I used Trello board to act as a visual for my product backlog. It helped act as a guide as to the next steps to take and what to prioritise by adjusting the different cards.

### **Risk Assessment**
Risk Assessement using excel showing the potential threats to the project. Encountered new potential threats as I progressed in the project and updated as I went along.

![image](https://user-images.githubusercontent.com/96881229/183014230-5c09d6d1-5713-485d-8b32-1ca8174d821d.png)

### **Testing**

![image](https://user-images.githubusercontent.com/96881229/189171000-afddc9a6-558a-4e55-a88e-e7a3b5e3cf13.png)



