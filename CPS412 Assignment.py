#CPS412 Assignment


#Students:  Danny Vo 
#           Jana Habibi 
#           Kevin Kim 
#           Nicole Lin

#To install python's package manager if not installed yet, in command (assuming python is installed)
#type "python get-pip.py"
# OR  "pip install pip"

#  Then type in command prompt to install the following packages necessary for this program
#  pip install openpyxl
#  pip install pandas
#  pip install matplotlib
#  pip install windows-curses


#DESCRIPTION 

# Reads from excel sheet, for every question there is a function that prints their corresponding graph
# At the bottom of the code, if you decide not to use the interactive menu through the command prompt at the folder's directory
# You can display all graphs

# If user chooses interactive menu option in an IDE, it will cause an error. MUST be run through command prompt.
# To run the interactive menu please read the README.txt file for instructions to run the .py file from command prompt and navigate the interactive menu



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


import pandas as pd
from matplotlib import pyplot as plt


# Defining our excel workbook
wb = pd.read_excel('ChatGPT survey.xlsx')
question_dict = wb.to_dict()


#Defining our questions
age = 'What is your age?'

gender = 'What gender do you identify as?'

ethnicity = 'What is your ethnicity?'

academic = 'Your current level of academic study?'

faculty = 'What is your faculty?'

used_chatgpt = 'Have you used ChatGPT before?'

exp_chatgpt = 'How experienced are you with ChatGPT?'

productivity = 'Have you noticed an increase in productivity during or after the use of ChatGPT?'

impact = 'Do you think ChatGPT will have an impact on students and their learning capabilities?'

pos_neg_impact = 'If you answered yes:\nWould it have a negative or positive impact?'

chatgpt_uses = 'What are some of the ways you can use ChatGPT?\n\nSelect all that apply:'

instructor_implement_chatgpt = 'If the usage of ChatGPT is allowed in learning, what are some ways do you think an instructor can implement ChatGPT in their teachings?\n  \nSelect all that apply:'

reliable_consistent = 'Do you think ChatGPT is a reliable and consistent source for information?'

education_implement_chatgpt = 'Should education systems implement the complete usage of ChatGPT?'

regulations = 'If you answered "Yes, but with regulations":\nWhat regulations do you think the education system can implement to uphold academic integrity among students?\n\nSelect all that apply:'






#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ AGE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#counting the responses to each option
#converting the dictionary containing all age values ot list so we can count the instances of a answer
c_under_17 = list(question_dict[age].values()).count('Under 17')

c_17_24 = list(question_dict[age].values()).count('17-24')

c_25_34 = list(question_dict[age].values()).count('25-34')

c_35_44 = list(question_dict[age].values()).count('35-44')

c_45_over = list(question_dict[age].values()).count('45+')



#defining the data
age_bar_height = [c_under_17, c_17_24, c_25_34, c_35_44, c_45_over]
age_label = ['Under 17', '17-24', '25-34', '35-44', '45+']

def age():

    #setting up the graph
    for i in range(len(age_label)):
        plt.text(i, age_bar_height[i]+0.5, age_bar_height[i], ha = 'center')
    
    color_age = ['seagreen', 'indianred', 'cornflowerblue', 'mediumslateblue', 'gold']
    #plt.style.use('ggplot')

    plt.xlabel('Ages')
    plt.ylabel('Responses')
    plt.title('What is your age?')
    plt.bar(age_label, age_bar_height, color = color_age)

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ GENDER \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#Count of responses to each answer
female = list(question_dict[gender].values()).count('Female')

male = list(question_dict[gender].values()).count('Male')

other_gender = list(question_dict[gender].values()).count('Other')


#setting bar heights
gender_value = [female, male, other_gender]
gender_label = ['Female', 'Male', 'Other']

def gender():

    #setting up the pie chart
    color_gender = ['indianred', 'dodgerblue', 'gold']
    plt.title('What is your gender?')
    plt.pie(gender_value, labels = gender_label, colors = color_gender, autopct = '%1.1f%%', wedgeprops={"edgecolor":"white", 'linewidth':2, 'antialiased': True})

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ETHNICITY \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#Count of responses to each answer

#For questions that contain checkboxes (can select multiple options), in the dictionary it will present a single string value with all answers combined

#ex. pets = {0: 'meow, woof', 1: 'meow', 2: 'meow', 3: 'woof'}
#  problem: if we use .count("meow"), it will only count if the entire value is "meow"

#   solution: using list comphrension
#      we iterate through each dict_value,      
#      check if value "meow" is in dict_value 
#      append a boolean value to a temp list
#      'sum' function counts the true values of temp list and assign to new varible
indigenous = sum('Indigenous (First Nations, Inuit, Métis, etc)' in value for value in question_dict[ethnicity].values())

east_asia = sum('East Asia (China, Japan, Korea, Taiwan, etc)' in value for value in question_dict[ethnicity].values())

west_asia = sum('West Asia (Iran, Iraq, Israel, Qatar, etc)' in value for value in question_dict[ethnicity].values())

southeastern_asia = sum('Southeastern Asia (Indonesia, Thailand, Vietnam, Philippines, etc)' in value for value in question_dict[ethnicity].values())

south_asia = sum('South Asia (India, Pakistan, etc)' in value for value in question_dict[ethnicity].values())

central_asia = sum('Central Asia (Kazakhstan, Tajikistan, Uzbekistan, etc)' in value for value in question_dict[ethnicity].values())

north_america = sum('North America (Canada, United States of America, Mexico, etc)' in value for value in question_dict[ethnicity].values())

south_america = sum('South America (Brazil, Argentina, Peru, etc)' in value for value in question_dict[ethnicity].values())

white_caucasian = sum('White/Caucasian' in value for value in question_dict[ethnicity].values())

black_african_american = sum('Black/African American' in value for value in question_dict[ethnicity].values())

other_ethnicity = sum('Other' in value for value in question_dict[ethnicity].values())



#setting bar heights (counts)
ethnicity_bar_height = [indigenous, east_asia, west_asia, southeastern_asia, south_asia, central_asia, north_america, south_america, white_caucasian, black_african_american, other_ethnicity]

#setting the labels for each bar
ethnicity_label = ['Other', 'East Asia', 'West Asia', 'Southeastern Asia', 'South Asia', 'Central Asia', 'North America', 'South America', 'White/Caucasian', 'Black/African American','Indigenous',]

def ethnicity():

    #setting up the graph
    plt.rcParams.update({'figure.autolayout': True})
    color_ethnicity = ['salmon', 'indianred', 'orange', 'gold', 'seagreen', 'darkgreen', 'royalblue', 'midnightblue', 'indigo', 'darkviolet', 'mediumvioletred']
    fig, ax = plt.subplots()

    for i in range(len(ethnicity_label)):
        plt.text(ethnicity_bar_height[i]+0.3, i-0.1, ethnicity_bar_height[i])
    
    plt.ylabel('Ethnicity')
    plt.xlabel('Responses')
    plt.title('What is your ethnicity?')
    plt.barh(ethnicity_label, ethnicity_bar_height, height = 0.8, color = color_ethnicity)

    #print graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ LEVEL OF STUDY \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#Count of responses to each answer
bachelors = list(question_dict[academic].values()).count("Bachelor's Degree (Undergraduate)")

masters = list(question_dict[academic].values()).count("Master's Degree")

phD = list(question_dict[academic].values()).count("PhD")

other_academic = list(question_dict[academic].values()).count("Other")



#setting bar heights
academics_bar_height = [bachelors, masters, phD, other_academic]

#setting the labels for each bar
academics_label = ["Bachelor's Degree", "Master's Degree", "PhD", "Other"]

def level_study():

    #setting up the graph
    for i in range(len(academics_label)):
        plt.text(i, academics_bar_height[i]+0.5, academics_bar_height[i], ha = 'center')
    color_academics = ['seagreen', 'indianred', 'royalblue', 'slategrey']
    #plt.style.use('ggplot')
    plt.xlabel('Academic Level')
    plt.ylabel('Responses')
    plt.title('What is your current level of academic study?')
    plt.bar(academics_label, academics_bar_height, color = color_academics)

    #print graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ FACULTY \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#Count of responses to each answer
science = list(question_dict[faculty].values()).count("Faculty of Science (Biology, Comp Sci, Mathematics, Biomedical, etc.)")

engineering_architecture = list(question_dict[faculty].values()).count("Faculty of Engineering and Architectural Science (Mech Eng, Comp Eng, Civil Eng, etc.)")

arts = list(question_dict[faculty].values()).count("Faculty of Arts (Criminology, History, Psychology, English, Arts, etc.)")

law = list(question_dict[faculty].values()).count("Faculty of Law")

community_service = list(question_dict[faculty].values()).count("Faculty of Community Services (Nursing, Social Work, Youth Care, Nutrition & Food, etc.)")

communication_design = list(question_dict[faculty].values()).count("Faculty of Communication & Design (Fashion, Image Arts, Performance, Design, etc.)")

business = list(question_dict[faculty].values()).count("Faculty of Business")


#setting the bar height
faculty_bar_height = [business, communication_design, community_service, law, arts, engineering_architecture, science]

#setting labels for each bar
faculty_label = ['Faculty of Business', 'Faculty of\nCommunication & Design', 'Faculty of\nCommunity Services', 'Faculty of Law', 'Faculty of Arts',
                 'Faculty of Engineering', 'Faculty of Science']

def faculty():

    #setting up the graph
    plt.rcParams.update({'figure.autolayout': True})
    for i in range(len(faculty_label)):
        plt.text(faculty_bar_height[i]+0.15, i-0.1, faculty_bar_height[i])
    color_faculty = ['seagreen', 'navy', 'rosybrown', 'purple', 'palevioletred', 'steelblue', 'gold']
    plt.ylabel('Faculty')
    plt.xlabel('Responses')
    plt.title('What is your faculty?')
    plt.barh(faculty_label, faculty_bar_height, height = 0.8, color = color_faculty)

    #printing graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ HAVE YOU USED CHATGPT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#count
yes = list(question_dict[used_chatgpt].values()).count('Yes')

no = list(question_dict[used_chatgpt].values()).count('No')

#setting pie values
used_chatgpt_value = [yes, no]
used_chatgpt_label = ['Yes', 'No']

def used_chatgpt():

    #setting up the pie graph
    color_used_chatgpt = ['dodgerblue', 'indianred']
    plt.title('Have you used ChatGPT before?')
    plt.pie(used_chatgpt_value, labels = used_chatgpt_label, colors = color_used_chatgpt, autopct = '%1.1f%%', wedgeprops={"edgecolor":"white", 'linewidth':2, 'antialiased': True})

    #printing the pie graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ EXPERIENCE WITH CHATGPT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#counting the responses of each answer
one = list(question_dict[exp_chatgpt].values()).count(1)

two = list(question_dict[exp_chatgpt].values()).count(2)

three = list(question_dict[exp_chatgpt].values()).count(3)

four = list(question_dict[exp_chatgpt].values()).count(4)

five = list(question_dict[exp_chatgpt].values()).count(5)

#setting bar heights
exp_chatgpt_bar_height = [one, two, three, four, five]
exp_chatgpt_label = ['1', '2', '3', '4', '5']
    
def experience():
    #setting up the graph
    plt.xlabel('No experience  ->  Very experienced')
    plt.ylabel('Responses')
    plt.title('How experienced are you with ChatGPT?')
    plt.grid()
    plt.plot(exp_chatgpt_label, exp_chatgpt_bar_height, marker ='o', markerfacecolor = 'snow')

    #printing the graph
    plt.show()




#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ PRODUCTIVITY WITHCHATGPT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#count
one_p = list(question_dict[productivity].values()).count(1)

two_p = list(question_dict[productivity].values()).count(2)

three_p = list(question_dict[productivity].values()).count(3)

four_p = list(question_dict[productivity].values()).count(4)

five_p = list(question_dict[productivity].values()).count(5)

#setting bar heights
productivity_bar_height = [one_p, two_p, three_p, four_p, five_p]
productivity_label = ['1', '2', '3', '4', '5']

def productivity():
    
    #setting up the graph
    for i in range(len(productivity_label)):
        plt.text(i, productivity_bar_height[i]+0.3, productivity_bar_height[i], ha = 'center')
    color_productivity = ['slateblue', 'lightsteelblue','slateblue', 'lightsteelblue', 'slateblue']
    plt.xlabel('Not Much  ->  A lot')
    plt.ylabel('Responses')
    plt.title('Productivity during or after\nthe use of ChatGPT?')
    plt.bar(productivity_label, productivity_bar_height, color = color_productivity)

    #print graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ WILL CHATGPT HAVE AN IMPACT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#count
yes_impact = list(question_dict[impact].values()).count('Yes')

no_impact = list(question_dict[impact].values()).count('No')

#setting pie values
yesno_impact_value = [yes_impact, no_impact]
yesno_impact_label = ['Yes', 'No']

def chatgpt_impact():

    #setting up the graph
    yesno_impact_color = ['dodgerblue','indianred']
    plt.title('Will ChatGPT Impact Students')
    plt.pie(yesno_impact_value, labels = yesno_impact_label, colors = yesno_impact_color, autopct = '%1.1f%%', wedgeprops={"edgecolor":"white", 'linewidth':2, 'antialiased': True})

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ POS or NEG IMPACT? \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#count
pos_impact = list(question_dict[pos_neg_impact].values()).count("Positive Impact")

neg_impact = list(question_dict[pos_neg_impact].values()).count("Negative Impact")

#setting pie values
posneg_impact_value = [pos_impact, neg_impact]
posneg_impact_label = ['Positive Impact', 'Negative Impact']

def posneg_impact():

    #setting up the graph
    posneg_impact_color = ['dodgerblue', 'indianred']
    plt.title('Will ChatGPT Have A\nPositive Or Negative Impact?')
    plt.pie(posneg_impact_value, labels = posneg_impact_label, colors = posneg_impact_color, autopct = '%1.1f%%', wedgeprops={"edgecolor":"white", 'linewidth':2, 'antialiased': True})

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Some of the ways you can use ChatGPT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

RS_E = sum('Researching/Search Engine' in value for value in question_dict[chatgpt_uses].values())

SA = sum('School aid' in value for value in question_dict[chatgpt_uses].values())

LA = sum('Life Advice' in value for value in question_dict[chatgpt_uses].values())

Converse = sum('Converse with ChatGPT' in value for value in question_dict[chatgpt_uses].values())

WR_C = sum('Write/Review Code' in value for value in question_dict[chatgpt_uses].values())

EW = sum('Essay Writing' in value for value in question_dict[chatgpt_uses].values())

E = sum('Entertainment' in value for value in question_dict[chatgpt_uses].values())

other_uses = sum('Other' in value for value in question_dict[chatgpt_uses].values())

#setting bar heights

chatgptways_height = [other_uses, E, EW, Converse, WR_C,  LA, SA, RS_E]
chatgptways_label = ['Other', 'Entertainment', 'Essay Writing', 'Converse with\nChatGPT', 'Write/Review Code', 'Life Advice', 'School Aid', 'Researching/Search\nEngine']


def ways_to_use_chatgpt():
    
    #setting up the graph
    plt.style.use('default')
    plt.rcParams.update({'figure.autolayout': True})
    for i in range(len(chatgptways_label)):
        plt.text(chatgptways_height[i]+0.3, i-0.1, chatgptways_height[i])
    chatgptways_color = ['firebrick', 'coral', 'gold', 'darkolivegreen', 'seagreen', 'lightblue', 'slateblue', 'palevioletred']
    plt.ylabel('Ways To Use ChatGPT')
    plt.xlabel('Responses')
    plt.title('Ways you can use ChatGPT?')
    plt.barh(chatgptways_label, chatgptways_height, height = 0.8, color = chatgptways_color)

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Ways a instructor can implement chatgpt \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



QSE = sum('Quick Search Engine' in value for value in question_dict[instructor_implement_chatgpt].values())

feedback = sum('Analyze or Provide Feedback for Students' in value for value in question_dict[instructor_implement_chatgpt].values())

VA = sum('Virtual Assistance' in value for value in question_dict[instructor_implement_chatgpt].values())

STE_IL = sum('Student Engagement with Interactive Learning' in value for value in question_dict[instructor_implement_chatgpt].values())

SC = sum('Student Counseling' in value for value in question_dict[instructor_implement_chatgpt].values())

Other_I = sum('Other' in value for value in question_dict[instructor_implement_chatgpt].values())

#setting bar heights
II_height = [Other_I, SC, STE_IL, VA, feedback, QSE]
II_label = ['Other', 'Student\nCounseling', 'Interactive\nLearning', 'Virtual\nAssistance', 'Feedback for\nStudents', 'Quick Search\nEngine']

def instructor_implements():

    #setting up the graph
    plt.rcParams.update({'figure.autolayout': True})
    for i in range(len(II_label)):
        plt.text(II_height[i]+0.3, i-0.1, II_height[i])
    II_color = ['rebeccapurple', 'darkslateblue', 'slateblue', 'cornflowerblue', 'lightskyblue', 'lightsteelblue']
    plt.ylabel('Ways ChatGPT Can Be Used By Instructor')
    plt.xlabel('Responses')
    plt.title('Ways An Instructor\nCan Implement ChatGPT')
    plt.barh(II_label, II_height, height = 0.8, color = II_color)

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ RELIABILITY AND CONSISTENCY \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#count
one1 = list(question_dict[reliable_consistent].values()).count(1)

two2 = list(question_dict[reliable_consistent].values()).count(2)

three3 = list(question_dict[reliable_consistent].values()).count(3)

four4 = list(question_dict[reliable_consistent].values()).count(4)

five5 = list(question_dict[reliable_consistent].values()).count(5)

#setting bar heights
RC_bar_height = [one1, two2, three3, four4, five5]
RC_label = ['1', '2', '3', '4', '5']

def reliability_consistency():

    #setting up the graph
    plt.grid()
    plt.xlabel('Not Really  ->  Very')
    plt.ylabel('Responses')
    plt.title('How Reliable & Consistent is ChatGPT')
    plt.plot(RC_label, RC_bar_height, marker='o', markerfacecolor = 'snow')

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Should ChatGPT be Implemented \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#Count of responses to each answer
Allow = list(question_dict[education_implement_chatgpt].values()).count('Allow the complete usage of ChatGPT')

regulate = list(question_dict[education_implement_chatgpt].values()).count('Yes, but with regulations')

No = list(question_dict[education_implement_chatgpt].values()).count('No')

#setting bar heights
implement_bar_height = [Allow, regulate, No]
implement_label = ['Allow', 'Yes with Regulations', 'No']

def should_be_implemented():

    #setting up the graph
    plt.style.use("default")
    for i in range(len(implement_label)):
        plt.text(i, implement_bar_height[i]+0.5, implement_bar_height[i], ha = 'center')
    color_implement = ['indianred', 'steelblue', 'gold']
    plt.ylabel('Responses')
    plt.title('Should ChatGPT Be\nImplemented in Academia')
    plt.bar(implement_label, implement_bar_height, color = color_implement)

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Regulations on ChatGPT if Implemented \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#The other method of counting responses for a question with checkboxes (can select multiple options) did not work 
#           because for this question there are NaN values as this question was not required to be answered

#NaN (Not a Number), it is a special floating point value which cannot be casted to any other types

# So if we use limit = sum("Limit usage of ChatGPT to demonstrations & examples done by instructor" in 
#           value for value in question_dict[regulations].values())

#   it will give us a TypeError: "arguement of type 'float' is not iterable"
#   it refers to the NaN values
#   to fix this we implement if(pd.isna(value)): continue, a function from 
#      the pandas import, it checks if the value is a NaN, if so skip this iteration
#temp = []
#for value in question_dict[regulations].values():
#    if(pd.isna(value)):
#      continue
#    elif("Limit usage of ChatGPT to demonstrations & examples done by instructor" in #value):
#        temp.append(1)
limit = sum(1 for value in question_dict[regulations].values() if not pd.isna(value) and "Limit usage of ChatGPT to demonstrations & examples done by instructor" in value)

full = sum(1 for value in question_dict[regulations].values() if not pd.isna(value) and "Allowing students to freely use ChatGPT to its fullest" in value)

Guidelines = sum(1 for value in question_dict[regulations].values() if not pd.isna(value) and "Provide clear guidelines and expectations of it's usage" in value)

Plagiarism = sum(1 for value in question_dict[regulations].values() if not pd.isna(value) and "Plagiarism detection tools (Turnitin, Grammarly, etc.)" in value)

#setting bar heights
regulations_height = [Plagiarism, Guidelines, full, limit]
regulations_label = ['Plagiarism Detection Tool', 'Clear Guidelines &\nExpectations', 'Allow full usage\nof ChatGPT',
                     'Limit usage of ChatGPT to\ndemonstrations & examples' 
                      ]


def regulations():
    
    #setting up the graph
    plt.rcParams.update({'figure.autolayout': True})
    for i in range(len(regulations_label)):
        plt.text(regulations_height[i]+0.3, i-0.1, regulations_height[i])
    regulations_color = ['brown', 'lightcoral', 'pink', 'mistyrose']
    plt.ylabel('Regulations')
    plt.xlabel('Responses')
    plt.title('Which regulations should be\nimplemented along with ChatGPT?')
    plt.barh(regulations_label, regulations_height, height = 0.8, color = regulations_color)

    #printing the graph
    plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Experience vs Productivity \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def experience_vs_productivity():
    plt.grid()
    plt.xlabel('Little  ->   A lot')
    plt.ylabel('Productivity and Experience')
    plt.title('Experience vs Productivity')
    plt.plot(exp_chatgpt_label, exp_chatgpt_bar_height,'k--', marker='o', markerfacecolor = 'snow', label ='Experience')
    plt.plot(exp_chatgpt_label, productivity_bar_height,'b', marker='o', markerfacecolor = 'snow', label = 'Productivity')
    plt.legend()
    plt.show()





#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ MENU \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    
import curses
from curses import wrapper
import time

#menu items to be displayed in command prompt window
menu = ['ChatGPT Survey Summary Graphs', '1.  Age', '2.  Gender', '3.  Ethnicity', '4.  Level of study', 
        '5.  Faculty', '6.  Used ChatGPT before', '7.  How experienced are you with ChatGPT', '8.  Productivity during or after the use of ChatGPT',
        '9.  Will ChatGPT have an impact on students', '10. Will it have a positive or negative impact', '11. Ways to use ChatGPT', 
        '12. Ways an instructor can implement ChatGPT', '13. Is ChatGPT reliable and consistent', '14. Should ChatGPT be implemented in education',
        "15. What regulations should be enforced for ChatGPT's implementation", "16. Experience Vs Productivity",
        'Quit']


#function that prints the menu contents along with highlighting the current selection
def printmenu(stdscr, current_row):
    h, w = stdscr.getmaxyx()
    
    for index, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + index
        
        if index == current_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, 28, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            if index == 0:
                stdscr.addstr(y, x, row, curses.color_pair(2))
            else:
                stdscr.addstr(y, 27, row+"\n\n")
               
    stdscr.refresh()



#a function that allows user to navigate and interact with the menu
def mainmenu(stdscr):
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 1
    printmenu(stdscr, current_row)

    # What each interaction does, when a selection is done it prints a graph
    while 1:
        key = stdscr.getch()
        stdscr.clear()
        
        if key == curses.KEY_UP and current_row > 1:
            current_row -= 1
            
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
            
        elif key == curses.KEY_ENTER or key in [10, 13]:
            
            if current_row == len(menu)-1:
                break
            stdscr.addstr(0, 0, "Press Enter To Return To Menu")
            stdscr.refresh()
            if current_row == 1:
                age()
            elif current_row == 2:
                gender()
            elif current_row == 3:
                ethnicity()
            elif current_row == 4:
                level_study()
            elif current_row == 5:
                faculty()
            elif current_row == 6:
                used_chatgpt()
            elif current_row == 7:
                experience()        
            elif current_row == 8:
                productivity()
            elif current_row == 9:
                chatgpt_impact()
            elif current_row == 10:
                posneg_impact()
            elif current_row == 11:
                ways_to_use_chatgpt()
            elif current_row == 12:
                instructor_implements()
            elif current_row == 13:
                reliability_consistency()
            elif current_row == 14:
                should_be_implemented()
            elif current_row == 15:
                regulations()
            elif current_row == 16:
                experience_vs_productivity()
            stdscr.getch()
            stdscr.clear()
            
    
        printmenu(stdscr, current_row)
        stdscr.refresh()
   
    


#def runmenu(mainmenu):
#    wrapper(mainmenu)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# If program is not run by command prompt for interactive menu, display all graphs in IDE
print("1. Print all graphs now")
print("2. Run interactive menu (Command Prompt Only)")

ans = input("Please select '1' or '2': ")
all_graphs = [age, gender, ethnicity, level_study, faculty, used_chatgpt,
            experience, productivity, chatgpt_impact, posneg_impact, ways_to_use_chatgpt,
            instructor_implements, reliability_consistency,
            should_be_implemented, regulations, experience_vs_productivity]

if(ans == '1'):
    print("Printing graphs")
    for graph in all_graphs:
        graph()


elif(ans == '2'):
    wrapper(mainmenu)

