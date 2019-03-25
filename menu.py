from db import MongoDB
from neo4j import NeoDB
import os




class Menu():

    def __init__(self):
        self.neo_db = NeoDB()
        self.mongo_db = MongoDB()
        self.query_history = []


    def main_menu(self):
        print("*******SELECT AN OPTION*************")
        print("************************************")
        print("* 1 - Create DBs (Mongo and Neo4j)**")
        print("* 2 - Perform Query for Answer 1  **")
        print("* 3 - Perform Query for Answer 2  **")
        print("* 4 - Query MongoDB               **")
        print("* 5 - Query Neo4j                 **")
        print("* 6 - Query History               **")
        print("* 7 - Import CSV file to MongoDB  **")
        print("* 8 - Import CSV file to Neo4j    **")
        print("* 9 - Quit the APP                **")
        print("************************************")
        print("NOTE: Please run Option 1 before any others")


    def parse_choice(self, choice):
        if(choice=="1"): #todo: show all the user
            self.neo_db.setup()
            self.mongo_db.setupv2()
            input("Press Enter to continue...")
        if(choice=="2"):
            self.get_user_list() 
        if(choice=="3"):
            print(self.mongo_db.return_users()) #todo: return each user once
            user = input("\nSelect User you would like to find \ntrusted colleagues-of-colleagues \nwith one or more interests: ")
            print(self.mongo_db.answer_for_question2(user))
            input("Press Enter to continue...")
            pass
        if(choice=="4"):
            
            query = input("Write Query for MongoDB: ")
            self.query_history.append(query)
            pass
        if(choice=="5"):
            query = input("Write Query for Neo4j: ")
            print("To delete all nodes: MATCH (n:Person) OPTIONAL MATCH (n)-[r]-() DELETE r,n")
            self.query_history.append(query)
            pass
        if(choice=="6"):
            print(self.query_history)
            pass
        if(choice=="7"):
            print("Import CSV file ... \n") 
            print("For example: /home/Navid/Documents/BigData/project1_sample/user.csv\n")
            filepath = input ("enter file path:")
            self.mongo_db.import_content(filepath)

            pass
        if(choice=="8"): #Import CSV neo4j
            print ("This is critical, so you need to contact the DB admin\n")
            print ("***** Instructions for Neo4J DB Admin******\n")
            print("Please Copy all of  the CSV files into the neo4j import folder \n ")
            print ("Next, copy the path to csv file, and be sure if it is relation or node.\n")
            print ("For example on ubuntu machines, the path is:\n")
            print("/var/lib/neo4j/import/*.csv\n")
            print ("login to the neo4j managment console, and execute the following cypher query\n")
            print ("""LOAD CSV WITH HEADERS FROM 'file:///project1_sample/user.csv' AS line
                    MERGE (:user { User_id: line.User_id, name: line.`First name`, lastname: line.`Last name`}\n
                       OR \n
                    LOAD CSV WITH HEADERS FROM 'file:///project1_sample/distance.csv' AS line \n
                    CREATE (:distance { Organization1: line.`Organization 1`, Organization2: line.`Organization 2`,\n
                    Distance: line.Distance}) \n
                        OR \n
                    LOAD CSV WITH HEADERS FROM 'file:///project1_sample/interest.csv' AS line MERGE \n
                    (:interest { User_id: line.User_id, Interest: line.`Interest`, InterestLevel: line.`Interest level`}) \n
                        OR \n
                    LOAD CSV WITH HEADERS FROM 'file:///project1_sample/organization.csv' AS line MERGE (:organization \n
                    { User_id: line.User_id, organization: line.`organization`, organization_type: line.`organization type`}) \n
                        OR \n    
                    LOAD CSV WITH HEADERS FROM 'file:///project1_sample/project.csv' \n
                    AS line MERGE (:project { User_id: line.User_id, Project: line.Project})

                    LOAD CSV WITH HEADERS FROM 'file:///project1_sample/skill.csv'\n
                    AS line MERGE (:skill { User_Id: line.User_Id, Skill: line.`Skill `,Skill_level: line.`Skill level`})\n
                      OR \n
                          
                        """)

           

            pass


        if(choice=="9"):
            quit()

    def get_user_list(self):
        print( self.neo_db.get_all_users() )
        user = input("SELECT User (Type Name): ")
        company = input("SELECT Company Name of Same User: ")
        self.neo_db.query_for_answer_1(user, company)
        input("Press ENTER to Continue...")


    def run(self):
        print("Welcome To Collaboration NET DB")
        while(True):
            self.main_menu()
            choice = input("Choice: ")
            self.parse_choice(choice)
