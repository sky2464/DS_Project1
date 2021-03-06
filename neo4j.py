from py2neo import Graph, Node, Relationship
import pandas as pd

class NeoDB():

    def __init__(self):
        self.graph = Graph(host="127.0.0.1", user="neo4j",bolt=True, password="1234")
        self.setup_node_list = [
            "CREATE (u1:User {name:'Eli', currentProject: 'Backend'})",
            "CREATE (u2:User {name:'Bob', currentProject: 'Backend'})",
            "CREATE (u4:User {name:'Sandy', currentProject: 'Capstone'})",
            "CREATE (u5:User {name:'Jake', currentProject: 'Capstone'})",
            "CREATE (u3:User {name:'Ruby', currentProject: 'Frontend'})",
            "CREATE (u6:User {name:'Amy', currentProject: 'Data Discovery'})",
            "CREATE (u7:User {name:'Paul', currentProject: 'Data Discovery'})",
            "CREATE (u9:User {name:'Navid', currentProject: 'Backend'})",
            "CREATE (o1:Organization {name: 'Hunter College', type:'University'})",
            "CREATE (o2:Organization {name: 'SSC', type:'Company'})",
            "CREATE (o3:Organization {name: 'NSA', type:'Government'})",
            "CREATE (s:Skill {name:'Python'})",
            "CREATE (s1:Skill {name:'Java'})",
            "CREATE (s2:Skill {name:'C++'})",
            "CREATE (s3:Skill {name:'Julia'})",
            "CREATE (s4:Skill {name:'Genetic Algorithms'})",
            "CREATE (s5:Skill {name:'Discrete Math'})",
            "CREATE (s6:Skill {name:'Accounting'})",
            "CREATE (s7:Skill {name:'Copywriting'})",
            "CREATE (s8:Skill {name:'Foreign Languages'})",
            "CREATE (s9:Skill {name:'Web Development'})",
            "CREATE (s10:Skill {name:'Critical Thinking'})",
            "CREATE (s11:Skill {name:'Communication'})",
            "CREATE (s12:Skill {name:'Time Management'})",
            "CREATE (s13:Skill {name:'Statistical Analysis'})",
            "CREATE (s14:Skill {name:'Software Development'})",
            "CREATE (s15:Skill {name:'MySQL'})",
            "CREATE (s16:Skill {name:'Linux'})",
            "CREATE (s17:Skill {name:'Information Security'})",
            "CREATE (s18:Skill {name:'Data Modeling'})",
            "CREATE (s19:Skill {name:'Networking'})",
            "CREATE (s22:Skill {name:'McAfee'})",
            "CREATE (s20:Skill {name:'Javascript'})",
            "CREATE (s21:Skill {name:'HTML'})",
            "CREATE (i1:Interest {name:'Weightlifting'})",
            "CREATE (i2:Interest {name:'Bowling'})",
            "CREATE (i3:Interest {name:'Swimming'})",
            "CREATE (i4:Interest {name:'Basketball'})",
            "CREATE (i5:Interest {name:'Ultimate Frisbee'})",
            "CREATE (i6:Interest {name:'Kart racing'})",
            "CREATE (i7:Interest {name:'Traveling'})",
            "CREATE (i8:Interest {name:'Martial Arts'})",
            "CREATE (i9:Interest {name:'Videogames'})",
            "CREATE (i10:Interest {name:'Hiking'})",
            "CREATE (i11:Interest {name:'Cycling'})",
            "CREATE (i12:Interest {name:'Volleyball'})",
            "CREATE (i13:Interest {name:'Boxing'})",
            "CREATE (i14:Interest {name:'Gardening'})"

            ]
        self.relationship_list = [
            "MATCH (a:User {name:'Eli'}),(b:Skill {name:'Python'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Eli'}),(b:Skill {name:'Linux'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",
            "MATCH (a:User {name:'Eli'}),(b:Skill {name:'MySQL'}) MERGE (a)-[r:SKILLED_IN {level: 3}]->(b)",
            "MATCH (a:User {name:'Eli'}),(b:Skill {name:'Critical Thinking'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",
            "MATCH (a:User {name:'Eli'}),(b:Skill {name:'Java'}) MERGE (a)-[r:SKILLED_IN {level: 2}]->(b)",
            "MATCH (a:User {name:'Bob'}),(b:Skill {name:'Java'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Bob'}),(b:Skill {name:'Python'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",
            "MATCH (a:User {name:'Bob'}),(b:Skill {name:'MySQL'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",
            "MATCH (a:User {name:'Bob'}),(b:Skill {name:'Time Management'}) MERGE (a)-[r:SKILLED_IN {level: 2}]->(b)",
            "MATCH (a:User {name:'Bob'}),(b:Skill {name:'C++'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Sandy'}),(b:Skill {name:'Web Development'}) MERGE (a)-[r:SKILLED_IN {level: 1}]->(b)",
            "MATCH (a:User {name:'Sandy'}),(b:Skill {name:'Networking'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Sandy'}),(b:Skill {name:'MySQL'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Sandy'}),(b:Skill {name:'Communication'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",
            "MATCH (a:User {name:'Sandy'}),(b:Skill {name:'Software Development'}) MERGE (a)-[r:SKILLED_IN {level: 3}]->(b)",
            "MATCH (a:User {name:'Jake'}),(b:Skill {name:'Web Development'}) MERGE (a)-[r:SKILLED_IN {level: 3}]->(b)",
            "MATCH (a:User {name:'Jake'}),(b:Skill {name:'Networking'}) MERGE (a)-[r:SKILLED_IN {level: 2}]->(b)",
            "MATCH (a:User {name:'Jake'}),(b:Skill {name:'MySQL'}) MERGE (a)-[r:SKILLED_IN {level: 2}]->(b)",
            "MATCH (a:User {name:'Jake'}),(b:Skill {name:'Communication'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",
            "MATCH (a:User {name:'Jake'}),(b:Skill {name:'Software Development'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Ruby'}),(b:Skill {name:'Web Development'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Ruby'}),(b:Skill {name:'Javascript'}) MERGE (a)-[r:SKILLED_IN {level: 3}]->(b)",
            "MATCH (a:User {name:'Ruby'}),(b:Skill {name:'MySQL'}) MERGE (a)-[r:SKILLED_IN {level: 1}]->(b)",
            "MATCH (a:User {name:'Ruby'}),(b:Skill {name:'HTML'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",
            "MATCH (a:User {name:'Ruby'}),(b:Skill {name:'Accounting'}) MERGE (a)-[r:SKILLED_IN {level: 1}]->(b)",
            "MATCH (a:User {name:'Amy'}),(b:Skill {name:'Web Development'}) MERGE (a)-[r:SKILLED_IN {level: 3}]->(b)",
            "MATCH (a:User {name:'Amy'}),(b:Skill {name:'Information Security'}) MERGE (a)-[r:SKILLED_IN {level: 2}]->(b)",
            "MATCH (a:User {name:'Amy'}),(b:Skill {name:'MySQL'}) MERGE (a)-[r:SKILLED_IN {level: 2}]->(b)",
            "MATCH (a:User {name:'Amy'}),(b:Skill {name:'C++'}) MERGE (a)-[r:SKILLED_IN {level: 3}]->(b)",
            "MATCH (a:User {name:'Amy'}),(b:Skill {name:'Copywriting'}) MERGE (a)-[r:SKILLED_IN {level: 1}]->(b)",
            "MATCH (a:User {name:'Paul'}),(b:Skill {name:'Information Security'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Paul'}),(b:Skill {name:'C++'}) MERGE (a)-[r:SKILLED_IN {level: 3}]->(b)",
            "MATCH (a:User {name:'Paul'}),(b:Skill {name:'Foreign Languages'}) MERGE (a)-[r:SKILLED_IN {level: 2}]->(b)",
            "MATCH (a:User {name:'Paul'}),(b:Skill {name:'MySQL'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Paul'}),(b:Skill {name:'Linux'}) MERGE (a)-[r:SKILLED_IN {level: 3}]->(b)",
            
            "MATCH (a:User {name:'Navid'}),(b:Skill {name:'Python'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Navid'}),(b:Skill {name:'Linux'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",
            "MATCH (a:User {name:'Navid'}),(b:Skill {name:'McAfee'}) MERGE (a)-[r:SKILLED_IN {level: 5}]->(b)",
            "MATCH (a:User {name:'Navid'}),(b:Skill {name:'Critical Thinking'}) MERGE (a)-[r:SKILLED_IN {level: 4}]->(b)",

            "MATCH (a:User {name:'Eli'}), (b:Organization {name:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {name:'Navid'}),(b:Organization {name:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {name:'Bob'}),(b:Organization {name:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {name:'Ruby'}),(b:Organization {name:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {name:'Sandy'}),(b:Organization {name:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {name:'Jake'}),(b:Organization {name:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {name:'Amy'}),(b:Organization {name:'NSA'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {name:'Paul'}),(b:Organization {name:'NSA'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:Organization {name:'SSC'}),(b:Organization {name:'NSA'}) MERGE (a)-[r:DISTANCE {miles: 20}]->(b)",
            "MATCH (a:Organization {name:'SSC'}),(b:Organization {name:'Hunter College'}) MERGE (a)-[r:DISTANCE {miles: 8}]->(b)",
            "MATCH (a:Organization {name:'Hunter College'}),(b:Organization {name:'NSA'}) MERGE (a)-[r:DISTANCE {miles: 20}]->(b)",

            "MATCH (a:User {name:'Eli'}),(i:Interest {name:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {name:'Eli'}),(i:Interest {name:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {name:'Eli'}),(i:Interest {name:'Videogames'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {name:'Eli'}),(i:Interest {name:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {level: 2}]->(i)",
            "MATCH (a:User {name:'Eli'}),(i:Interest {name:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {level: 9}]->(i)",
            "MATCH (a:User {name:'Bob'}),(i:Interest {name:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {level: 5}]->(i)",
            "MATCH (a:User {name:'Bob'}),(i:Interest {name:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {level: 3}]->(i)",
            "MATCH (a:User {name:'Bob'}),(i:Interest {name:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {name:'Bob'}),(i:Interest {name:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {level: 8}]->(i)",
            "MATCH (a:User {name:'Bob'}),(i:Interest {name:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {name:'Sandy'}),(i:Interest {name:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {level: 2}]->(i)",
            "MATCH (a:User {name:'Sandy'}),(i:Interest {name:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {level: 8}]->(i)",
            "MATCH (a:User {name:'Sandy'}),(i:Interest {name:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {name:'Sandy'}),(i:Interest {name:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {name:'Sandy'}),(i:Interest {name:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {level: 5}]->(i)",
            "MATCH (a:User {name:'Jake'}),(i:Interest {name:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {name:'Jake'}),(i:Interest {name:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {name:'Jake'}),(i:Interest {name:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {level: 9}]->(i)",
            "MATCH (a:User {name:'Jake'}),(i:Interest {name:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {name:'Jake'}),(i:Interest {name:'Videogames'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {name:'Ruby'}),(i:Interest {name:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {level: 5}]->(i)",
            "MATCH (a:User {name:'Ruby'}),(i:Interest {name:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {level: 5}]->(i)",
            "MATCH (a:User {name:'Ruby'}),(i:Interest {name:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {name:'Ruby'}),(i:Interest {name:'Volleyball'}) MERGE (a)-[r:INTERESTED_IN {level: 8}]->(i)",
            "MATCH (a:User {name:'Ruby'}),(i:Interest {name:'Cycling'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {name:'Amy'}),(i:Interest {name:'Gardening'}) MERGE (a)-[r:INTERESTED_IN {level: 9}]->(i)",
            "MATCH (a:User {name:'Amy'}),(i:Interest {name:'Volleyball'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {name:'Amy'}),(i:Interest {name:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {name:'Amy'}),(i:Interest {name:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {name:'Amy'}),(i:Interest {name:'Cycling'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {name:'Paul'}),(i:Interest {name:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {name:'Paul'}),(i:Interest {name:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {name:'Paul'}),(i:Interest {name:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {name:'Paul'}),(i:Interest {name:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {level: 2}]->(i)",
            "MATCH (a:User {name:'Paul'}),(i:Interest {name:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {level: 9}]->(i)"
        ]

    def setup(self):
        self.graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
        for s in self.setup_node_list:
            self.graph.run(s)
        for r in self.relationship_list:
            self.graph.run(r)

    def get_all_users(self):
        query_string = """MATCH (u:User)-[]->(o:Organization)
                        RETURN u.name as Name, u.currentProject as Project,
                        o.name as OrgName, o.type as OrgType"""
        return pd.DataFrame(self.graph.run(query_string).data()).to_string()


    def query_for_answer_1(self, username, company_name):
        query_string = """
        MATCH (u:User)-[r]->(s:Skill)<-[r1]-(u1:User)-[]-(o:Organization)-[r2]-(o1:Organization)
        WHERE (u.name='{}') and (o.name='{}' or o1.name='{}') and (r2.miles <=10)
        WITH DISTINCT u1.name as name, o.name as org_name, collect(s.name) as common_skills, sum(r1.level) as weight
        ORDER BY weight DESC
        RETURN name, org_name, common_skills, weight""".format(username, company_name, company_name)
        print( pd.DataFrame(self.graph.run(query_string).data()).to_string() )
