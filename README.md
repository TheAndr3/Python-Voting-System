# Python-Voting-System
Personal project made with python
Sure! Here's the translation of the entire text into English:

# Introduction

The Universidade Estadual de Feira de Santana - UEFS, every 4 years, undergoes an electoral process that elects the Rector and Vice-Rector for the University's management for the same period. The UEFS Electoral Commission sought the Computer Engineering course board to develop a Voting Control System that registers, computes votes, and announces the winner of future elections. Currently, this process is not electronic. The electoral commission informed that one or more slates may run for the rectorate, as long as they obey some pre-established requirements verified by the commission. The Voting Control System should enable:

- Registration of candidates for Rector and Vice-Rector.
- Alteration of candidate names after registration.
- Exclusion of a slate if it was incorrectly registered.
- Reading of information about possible voters:
  - NTSD = Total number of voting faculty members.
  - NTST = Total number of voting administrative staff.
  - NTD = Total number of voting students.

The voting period will take place over 3 business days. Faculty members, administrative staff, and students will be eligible to vote. To register the vote, the voter signs an attendance list, and in the system, they must inform their category (1 - Administrative Staff; 2 - Faculty Member; 3 - Student) and then choose the slate or the option of a Null/Blank vote and record it. There will be 4 voting urns distributed across the following modules:
- MODULE 1: Names starting with the letters A, B, C, D.
- MODULE 3: Names starting with the letters E, F, G, H, I, J.
- MODULE 5: Names starting with the letters K, L, M, N, O.
- MODULE 7: Names starting with the letters P, Q, R, S, T, U, V, W, X, Y, Z.

At the end of each voting day, the system must save all the registered votes in each urn for a possible audit. After the voting period, the Voting Control System must calculate and display the following information:
- Number of voters per day/category.
- Number of Null/Blank votes per day/category.
- Total number of Null/Blank votes.
- Total number of votes computed in each urn.
- NVSD = Number of votes for each slate by faculty members.
- NVST = Number of votes for each slate by administrative staff.
- NVD = Number of votes for each slate by students.
- Percentage of absences per category.
- E = Score of each slate.
- Winning slate.

# Methodology

To solve this problem, the MI Algoritmos class gathered in groups and discussed the best approach for the program's functionality. Each member of the class developed their own code, but with very similar functionalities. I decided to build my system using only the method of Classes, so it is noticeable that all the code functions are inside classes. I focused on constructing two main classes: 'Cadastro' (Registration), which would serve as the basis for the first stage, involving all the registration, alteration, and exclusion of slates, and the second class 'Votação' (Voting), which refers to the second main stage of the program and is more complex, handling the voting process for the defined slates in the 1st Stage.

With two main classes, I had to use inheritance mechanisms to pass the 'Cadastro' list of candidates to the 'Votação' class without any problems. The system also includes methods to save elements to files, mainly for potential audits, where only the most necessary information is saved.

# Results and Discussions

## Results

Below, I will detail the results, thought processes, logic, and code details that I created, as well as a 'manual' for using the program.

### How to Use the Program

Here is a detailed step-by-step guide on how the user should use the program:

### First 'Body'/Main - Cadastro (Registration)

The first part concerns the use of the 'Cadastro' (Registration) class, which is defined first. In this part, I create a closed 'Loop'/'While' for the slate registration stage, as there is no return after leaving this stage. Here, the user can exclude any slate, change the names of the Rector or Vice-Rector of the chosen slate by the index, and add as many slates as the user wants, with certain parameters such as being able to move on to the voting stage when there are 2 or more slates or, for example, only being able to access the Alteration/Exclusion part when a slate has already been registered. Finally, the user will choose to proceed to the voting stage, and the program will save the list of candidates for potential audits in a file, where the user can choose the name, and then move on to the total number of each category that will vote.

### Second 'Body'/Main - Votação (Voting)

After the user chooses the maximum quantity for each category, we enter the second main body, where I call all the functions written in the 'Votação' class. This body only runs a loop for 3 days using a for loop, starting on day 1. In this, the user will choose whether or not to vote on that day. If yes, the day will start, and it will follow the procedure I established. If the user does not want to vote, they will skip to the next day. The procedure that repeats on all days is as follows: First, it will ask for the user's name's initial, which will be sent to a list corresponding to the module. Then the user will have to choose their category, which is divided into 4 options: the 3 categories and an option to exit and skip the day. This option is useful if there are no more people to vote, and the user accidentally enters this stage; they can exit.

After that, it will print the slates from the list of the 'Cadastro' class with the available indices for the user to vote. Upon choosing, a message will confirm the vote for the slate, and the user can choose to proceed to the next day or vote again, and this repeats on all days.

### Report

The report was created using variables to facilitate and reduce visual clutter when printing the code, having many parts divided by comments for better visualization. To print certain parts, I used functions already created (e.g., votes per module), and I also had to go through a whole dictionary to print each slate and its votes related to the category.

### Errors and Tests

The program has strong error handling, especially in the registration part, which is refined to the last details. The part with the most errors would be during the voting stage, where errors can occur if the user accidentally presses 'enter' and skips a stage they did not want to, which would require extra time to handle the error. Another possible error is the number of votes in the modules not being coherent with the actual number of votes, as if the number of users who vote ends and the user still wants
