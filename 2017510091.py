#Importing the libs
import xml.etree.ElementTree as ET
import json
import csv 
import sys
from lxml import etree
from io import StringIO

#Variables to keep the syntax argumants
inputFile=sys.argv[1]
outputFile=sys.argv[2]
type=sys.argv[3]


#1-CONVERTING THE CSV FILE TO XML FORMAT 
def CSVtoXML(inputFile):

    #variable to keep the university name
    temp="temp"
    #openig the csv file to read
    with open (inputFile, "r", encoding="utf-8") as f:
        file = csv.reader(f, delimiter=";")
        #creating root
        root=ET.Element("departments")
        #skipping headers
        next(file)

        #the main loop for adding rows as sub elements to the tree
        for row in file:

            uType=row[0]
            university_name = row[1]
            faculty=row[2]
            program_kod=row[3]
            program=row[4]
            language=row[5] 
            sec=row[6]
            scolar=row[7]
            period=row[8]
            field=row[9]
            quota=row[10]
            firstStu=row[11]
            lastmin=row[12]
            lastminScore=row[13]     

            temp2=row[1]
            
            #Creating separated sub elements for each university
            if temp !=temp2: 
                sub1=ET.SubElement(root, "university")
                sub1.set("name", university_name)
                sub1.set("uType", uType)    
            sub2=ET.SubElement(sub1, "item")
            sub2.set("faculty", faculty)
            sub2.set("id", program_kod)
            ET.SubElement(sub2, "name", lang=language, second=sec).text = program
            ET.SubElement(sub2, "period").text = period
            ET.SubElement(sub2, "quota", spec=firstStu).text = quota
            ET.SubElement(sub2, "field").text = field
            ET.SubElement(sub2, "last_min_score", order=lastmin).text = lastminScore
            ET.SubElement(sub2, "grant").text = scolar

            temp=row[1]

    #adding root to the xml tree
    tree=ET.ElementTree(root)
    #writing tree to the output file
    tree.write(outputFile, encoding="utf-8") 
    #closing the csv file
    f.close() 

#2-CONVERTING THE XML FILE TO CSV FORMAT 
def XMLtoCSV(inputFile):
    #parsing the xml tree
    tree=ET.parse(inputFile)
    root=tree.getroot()

    #creating string variabla to write to the csv file
    str=""

    #adding headers to the str
    str += "University_name"+";" + "uType"+";"+"Faculty"+";"+"Id"+";"+"Language"+";"+"Second"+";"+ "Program"+";"+"Period"+";"+"Spec"+";"+"Quota"+";"+"Field"+";"+"Order"+";"+"Last_min_score"+";"+"Grant"+"\n"
    
    #searching the tree for finding the sub elements and adding to the str
    for uni in root.findall('university'):
        
        for item in uni.iter('item'):
            name = uni.get('name')
            str+=name + ";"
            type = uni.get('uType')
            str+=type + ";"
            faculty = item.get('faculty')
            str+=faculty + ";"
            id= item.get('id')
            str+=id + ";"
            for name in item.iter('name'):
                lang = name.get('lang')
                str+=lang+";"
                sec = name.get('second')
                str+=sec+";"
                prg= item.find('name').text
                str+=prg + ";"
                period=item.find('period').text
                str+=period + ";"
                for quota in item.iter('quota'):
                    spec=quota.get('spec')
                    str+=spec+";"
                    kont=item.find('quota').text
                    str+=kont +";"
                    field =item.find('field').text
                    str+=field+";"
                    for last in item.iter('last_min_score'):
                        order=last.get('order')
                        str+=order +";"
                        if item.find('last_min_score').text !=None:
                            min=item.find('last_min_score').text
                            str+= min+";"
                        elif item.find('last_min_score').text ==None:
                            str+= ""+";"
                        if item.find('grant').text != None:
                            grant=item.find('grant').text
                            str+= grant
                        elif item.find('grant').text ==None:
                            str+= ""+";"

                    #separate lines for each university
                    str +="\n"

    #opening the csv file and writing str too the file
    with open(outputFile,"w", encoding="utf-8") as f:
        f.write(str)
    f.close()

#3-CONVERTING THE XML FILE TO JSON FORMAT 
def XMLtoJSON(inputFile):
    #parsing the xml tree
    tree=ET.parse(inputFile)
    root=tree.getroot()

    #creating arrays and dictionaries for each university
    all=[] #the main array to write the json file
    departments=[]
    departments2=[]
    departments3=[]
    departments4=[]
    departments5=[]
    departments6=[]
    departments7=[]
    departments8=[]
    items=[]
    items2=[]
    items3=[]
    items4=[]
    items5=[]
    items6=[]
    items7=[]
    items8=[]
    deb={}
    deb2={}
    deb3={}
    deb4={}
    deb5={}
    deb6={}
    deb7={}
    deb8={}
    univ={}
    univ2={}
    univ3={}
    univ4={}
    univ5={}
    univ6={}
    univ7={}
    univ8={}

    #the main loop for finding the sub elements and adding to the their own dicttionaries and arrays 
    for child in root.iter('university'):     
        for item in child.iter('item'):
            cha={}
            cha2={}
            cha3={}
            cha4={}
            cha5={}
            cha6={}
            cha7={}
            cha8={}     
            if child.get('name')=="DOKUZ EYLÜL ÜNİVERSİTESİ":       
                cha['id']=item.get('id')
                for name in item.iter('name'):
                    cha['name']= item.find('name').text
                    cha['lang']=name.get('lang')
                    cha['second']=name.get('second')
                    cha['period']=item.find('period').text
                    for quo in item.iter('quota'):
                        cha['spec']=quo.get('spec')
                        cha['quota']=item.find('quota').text
                        cha['field']=item.find('field').text
                        for last in item.iter('last_min_score'):
                            univ['university_name']=child.get('name')
                            univ['uType']=child.get('uType')
                            deb['faculty']=item.get('faculty')                             
                            cha['last_min_score']=item.find('last_min_score').text
                            cha['order']=last.get('order')
                            cha['grant'] = item.find('grant').text
                            departments.append(cha)
                            deb['departments']=departments
                            univ['items']=items

            if child.get('name')=="EGE ÜNİVERSİTESİ":                 
                cha2['id']=item.get('id')
                for name in item.iter('name'):
                    cha2['name']= item.find('name').text
                    cha2['lang']=name.get('lang')
                    cha2['second']=name.get('second')
                    cha2['period']=item.find('period').text
                    for quo in item.iter('quota'):
                        cha2['spec']=quo.get('spec')
                        cha2['quota']=item.find('quota').text
                        cha2['field']=item.find('field').text
                        for last in item.iter('last_min_score'):
                            univ2['university_name']=child.get('name')
                            univ2['uType']=child.get('uType')
                            deb2['faculty']=item.get('faculty')                             
                            cha2['last_min_score']=item.find('last_min_score').text
                            cha2['order']=last.get('order')
                            cha2['grant'] = item.find('grant').text
                            departments2.append(cha2)
                            deb2['departments']=departments2
                            univ2['items']=items2

            if child.get('name')=="YAŞAR ÜNİVERSİTESİ":                 
                cha3['id']=item.get('id')
                for name in item.iter('name'):
                    cha3['name']= item.find('name').text
                    cha3['lang']=name.get('lang')
                    cha3['second']=name.get('second')
                    cha3['period']=item.find('period').text
                    for quo in item.iter('quota'):
                        cha3['spec']=quo.get('spec')
                        cha3['quota']=item.find('quota').text
                        cha3['field']=item.find('field').text
                        for last in item.iter('last_min_score'):
                            univ3['university_name']=child.get('name')
                            univ3['uType']=child.get('uType')
                            deb3['faculty']=item.get('faculty')                             
                            cha3['last_min_score']=item.find('last_min_score').text
                            cha3['order']=last.get('order')
                            cha3['grant'] = item.find('grant').text
                            departments3.append(cha3)
                            deb3['departments']=departments3
                            univ3['items']=items3

            if child.get('name')=="İZMİR EKONOMİ ÜNİVERSİTESİ":                 
                cha4['id']=item.get('id')
                for name in item.iter('name'):
                    cha4['name']= item.find('name').text
                    cha4['lang']=name.get('lang')
                    cha4['second']=name.get('second')
                    cha4['period']=item.find('period').text
                    for quo in item.iter('quota'):
                        cha4['spec']=quo.get('spec')
                        cha4['quota']=item.find('quota').text
                        cha4['field']=item.find('field').text
                        for last in item.iter('last_min_score'):
                            univ4['university_name']=child.get('name')
                            univ4['uType']=child.get('uType')
                            deb4['faculty']=item.get('faculty')                             
                            cha4['last_min_score']=item.find('last_min_score').text
                            cha4['order']=last.get('order')
                            cha4['grant'] = item.find('grant').text
                            departments4.append(cha4)
                            deb4['departments']=departments4
                            univ4['items']=items4

            if child.get('name')=="İZMİR YÜKSEK TEKNOLOJİ ENSTİTÜSÜ":                 
                cha5['id']=item.get('id')
                for name in item.iter('name'):
                    cha5['name']= item.find('name').text
                    cha5['lang']=name.get('lang')
                    cha5['second']=name.get('second')
                    cha5['period']=item.find('period').text
                    for quo in item.iter('quota'):
                        cha5['spec']=quo.get('spec')
                        cha5['quota']=item.find('quota').text
                        cha5['field']=item.find('field').text
                        for last in item.iter('last_min_score'):
                            univ5['university_name']=child.get('name')
                            univ5['uType']=child.get('uType')
                            deb5['faculty']=item.get('faculty')                             
                            cha5['last_min_score']=item.find('last_min_score').text
                            cha5['order']=last.get('order')
                            cha5['grant'] = item.find('grant').text
                            departments5.append(cha5)
                            deb5['departments']=departments5
                            univ5['items']=items5

            if child.get('name')=="İZMİR BAKIRÇAY ÜNİVERSİTESİ":                
                cha6['id']=item.get('id')
                for name in item.iter('name'):
                    cha6['name']= item.find('name').text
                    cha6['lang']=name.get('lang')
                    cha6['second']=name.get('second')
                    cha6['period']=item.find('period').text
                    for quo in item.iter('quota'):
                        cha6['spec']=quo.get('spec')
                        cha6['quota']=item.find('quota').text
                        cha6['field']=item.find('field').text
                        for last in item.iter('last_min_score'):
                            univ6['university_name']=child.get('name')
                            univ6['uType']=child.get('uType')
                            deb6['faculty']=item.get('faculty')                             
                            cha6['last_min_score']=item.find('last_min_score').text
                            cha6['order']=last.get('order')
                            cha6['grant'] = item.find('grant').text
                            departments6.append(cha6)
                            deb6['departments']=departments6
                            univ6['items']=items6

            if child.get('name')=="İZMİR DEMOKRASİ ÜNİVERSİTESİ":             
                cha7['id']=item.get('id')
                for name in item.iter('name'):
                    cha7['name']= item.find('name').text
                    cha7['lang']=name.get('lang')
                    cha7['second']=name.get('second')
                    cha7['period']=item.find('period').text
                    for quo in item.iter('quota'):
                        cha7['spec']=quo.get('spec')
                        cha7['quota']=item.find('quota').text
                        cha7['field']=item.find('field').text
                        for last in item.iter('last_min_score'):
                            univ7['university_name']=child.get('name')
                            univ7['uType']=child.get('uType')
                            deb7['faculty']=item.get('faculty')                             
                            cha7['last_min_score']=item.find('last_min_score').text
                            cha7['order']=last.get('order')
                            cha7['grant'] = item.find('grant').text
                            departments7.append(cha7)
                            deb7['departments']=departments7
                            univ7['items']=items7

            if child.get('name')=="İZMİR KATİP ÇELEBİ ÜNİVERSİTESİ":                 
                cha8['id']=item.get('id')
                for name in item.iter('name'):
                    cha8['name']= item.find('name').text
                    cha8['lang']=name.get('lang')
                    cha8['second']=name.get('second')
                    cha8['period']=item.find('period').text
                    for quo in item.iter('quota'):
                        cha8['spec']=quo.get('spec')
                        cha8['quota']=item.find('quota').text
                        cha8['field']=item.find('field').text
                        for last in item.iter('last_min_score'):
                            univ8['university_name']=child.get('name')
                            univ8['uType']=child.get('uType')
                            deb8['faculty']=item.get('faculty')                             
                            cha8['last_min_score']=item.find('last_min_score').text
                            cha8['order']=last.get('order')
                            cha8['grant'] = item.find('grant').text
                            departments8.append(cha8)
                            deb8['departments']=departments8
                            univ8['items']=items8

    items.append(deb)
    items2.append(deb2)
    items3.append(deb3)
    items4.append(deb4)
    items5.append(deb5)
    items6.append(deb6)
    items7.append(deb7)
    items8.append(deb8)  
    #adding universities to main array                      
    all.append(univ)
    all.append(univ2)
    all.append(univ3)
    all.append(univ4)
    all.append(univ5)
    all.append(univ6)
    all.append(univ7)
    all.append(univ8)                      
    
    #opening json file and writing the 'all' array to this file
    with open (outputFile, 'w') as f:
       json.dump(all, f, ensure_ascii=False)
    f.close()

#4-CONVERTING THE JSON FILE TO XML FORMAT 
def JSONtoXML(inputFile):
    #opening the json file to read 
    with open(inputFile, 'r', encoding="utf-8") as f:
        data =json.load(f)
        
        #creating the root element to xml
        root=ET.Element("departments")

        #main loop for finding the keys and adding to xml as sub element
        for line in data:
            sub1=ET.SubElement(root, "university")
            university_name=line['university_name']
            sub1.set("name", university_name)
            uType=line['uType']
            sub1.set("uType", uType)
            items=line['items']                  
            for lines in items:               
                deps=lines['departments']          
                for deep in deps:
                    sub2=ET.SubElement(sub1, "item")
                    faculty=lines['faculty']
                    sub2.set("faculty", faculty)
                    program_kod=deep['id']
                    sub2.set("id", program_kod)
                    program=deep['name']
                    language=deep['lang']
                    sec=deep['second']
                    ET.SubElement(sub2, "name", lang=language, second=sec).text = program
                    period=deep['period']
                    ET.SubElement(sub2, "period").text = period
                    firstStu=deep['spec']
                    quota=deep['quota']
                    ET.SubElement(sub2, "quota", spec=firstStu).text = quota
                    field=deep['field']
                    ET.SubElement(sub2, "field").text = field
                    lastmin=deep['order']
                    lastminScore=deep['last_min_score']
                    ET.SubElement(sub2, "last_min_score", order=lastmin).text = lastminScore
                    scolar=deep['grant']
                    ET.SubElement(sub2, "grant").text = scolar

    #adding the root to xml tree
    tree=ET.ElementTree(root)
    #writing the xml tree to the output file
    tree.write(outputFile, encoding="utf-8") 
    f.close()

#5-CONVERTING THE CSV FILE TO JSON FORMAT  
def CSVtoJSON(inputFile):
    #opening the csv file to read
    with open (inputFile, "r", encoding="utf-8") as f:
        file = csv.reader(f, delimiter=";")

        #creating arrays and dictionaries for each university
        all=[] #array to write in json file
        departments=[]
        departments2=[]
        departments3=[]
        departments4=[]
        departments5=[]
        departments6=[]
        departments7=[]
        departments8=[]
        items=[]
        items2=[]
        items3=[]
        items4=[]
        items5=[]
        items6=[]
        items7=[]
        items8=[]
        deb={}
        deb2={}
        deb3={}
        deb4={}
        deb5={}
        deb6={}
        deb7={}
        deb8={}
        univ={}
        univ2={}
        univ3={}
        univ4={}
        univ5={}
        univ6={}
        univ7={}
        univ8={}

        #skipping the headers
        next(file)

        #the main loop for adding rows to their own arrays and dictionaries
        for row in file:
            cha={}
            cha2={}
            cha3={}
            cha4={}
            cha5={}
            cha6={}
            cha7={}
            cha8={}

            if row[1]=="DOKUZ EYLÜL ÜNİVERSİTESİ":
                univ['uType']=row[0]
                univ['university_name'] = row[1]
                deb['faculty']=row[2]
                cha['id']=row[3]
                cha['name']=row[4]            
                cha['lang']=row[5]
                cha['second']=row[6] 
                cha['period']=row[8]          
                cha['spec']=row[11]
                cha['quota']=row[10]
                cha['field']=row[9]
                cha['last_min_score']=row[13] 
                cha['order']=row[12]
                cha['grant']=row[7]
                departments.append(cha)
                deb['departments']=departments
                univ['items']=items

            if row[1]=="EGE ÜNİVERSİTESİ":
                univ2['uType']=row[0]
                univ2['university_name'] = row[1]
                deb2['faculty']=row[2]
                cha2['id']=row[3]
                cha2['name']=row[4]            
                cha2['lang']=row[5]
                cha2['second']=row[6] 
                cha2['period']=row[8]          
                cha2['spec']=row[11]
                cha2['quota']=row[10]
                cha2['field']=row[9]
                cha2['last_min_score']=row[13] 
                cha2['order']=row[12]
                cha2['grant']=row[7]
                departments2.append(cha2)
                deb2['departments']=departments2
                univ2['items']=items2

            if row[1]=="YAŞAR ÜNİVERSİTESİ":
                univ3['uType']=row[0]
                univ3['university_name'] = row[1]
                deb3['faculty']=row[2]
                cha3['id']=row[3]
                cha3['name']=row[4]            
                cha3['lang']=row[5]
                cha3['second']=row[6] 
                cha3['period']=row[8]          
                cha3['spec']=row[11]
                cha3['quota']=row[10]
                cha3['field']=row[9]
                cha3['last_min_score']=row[13] 
                cha3['order']=row[12]
                cha3['grant']=row[7]
                departments3.append(cha3)
                deb3['departments']=departments3
                univ3['items']=items3

            if row[1]=="İZMİR EKONOMİ ÜNİVERSİTESİ":
                univ4['uType']=row[0]
                univ4['university_name'] = row[1]
                deb4['faculty']=row[2]
                cha4['id']=row[3]
                cha4['name']=row[4]            
                cha4['lang']=row[5]
                cha4['second']=row[6] 
                cha4['period']=row[8]          
                cha4['spec']=row[11]
                cha4['quota']=row[10]
                cha4['field']=row[9]
                cha4['last_min_score']=row[13] 
                cha4['order']=row[12]
                cha4['grant']=row[7]
                departments4.append(cha4)
                deb4['departments']=departments4
                univ4['items']=items4

            if row[1]=="İZMİR YÜKSEK TEKNOLOJİ ENSTİTÜSÜ":
                univ5['uType']=row[0]
                univ5['university_name'] = row[1]
                deb5['faculty']=row[2]
                cha5['id']=row[3]
                cha5['name']=row[4]            
                cha5['lang']=row[5]
                cha5['second']=row[6] 
                cha5['period']=row[8]          
                cha5['spec']=row[11]
                cha5['quota']=row[10]
                cha5['field']=row[9]
                cha5['last_min_score']=row[13] 
                cha5['order']=row[12]
                cha5['grant']=row[7]
                departments5.append(cha5)
                deb5['departments']=departments5
                univ5['items']=items5

            if row[1]=="İZMİR BAKIRÇAY ÜNİVERSİTESİ":
                univ6['uType']=row[0]
                univ6['university_name'] = row[1]
                deb6['faculty']=row[2]
                cha6['id']=row[3]
                cha6['name']=row[4]            
                cha6['lang']=row[5]
                cha6['second']=row[6] 
                cha6['period']=row[8]          
                cha6['spec']=row[11]
                cha6['quota']=row[10]
                cha6['field']=row[9]
                cha6['last_min_score']=row[13] 
                cha6['order']=row[12]
                cha6['grant']=row[7]
                departments6.append(cha6)
                deb6['departments']=departments6
                univ6['items']=items6

            if row[1]=="İZMİR DEMOKRASİ ÜNİVERSİTESİ":
                univ7['uType']=row[0]
                univ7['university_name'] = row[1]
                deb7['faculty']=row[2]
                cha7['id']=row[3]
                cha7['name']=row[4]            
                cha7['lang']=row[5]
                cha7['second']=row[6] 
                cha7['period']=row[8]          
                cha7['spec']=row[11]
                cha7['quota']=row[10]
                cha7['field']=row[9]
                cha7['last_min_score']=row[13] 
                cha7['order']=row[12]
                cha7['grant']=row[7]
                departments7.append(cha7)
                deb7['departments']=departments7
                univ7['items']=items7

            if row[1]=="İZMİR KATİP ÇELEBİ ÜNİVERSİTESİ":
                univ8['uType']=row[0]
                univ8['university_name'] = row[1]
                deb8['faculty']=row[2]
                cha8['id']=row[3]
                cha8['name']=row[4]            
                cha8['lang']=row[5]
                cha8['second']=row[6] 
                cha8['period']=row[8]          
                cha8['spec']=row[11]
                cha8['quota']=row[10]
                cha8['field']=row[9]
                cha8['last_min_score']=row[13] 
                cha8['order']=row[12]
                cha8['grant']=row[7]
                departments8.append(cha8)
                deb8['departments']=departments8
                univ8['items']=items8

        items.append(deb)
        items2.append(deb2)
        items3.append(deb3)
        items4.append(deb4)
        items5.append(deb5)
        items6.append(deb6)
        items7.append(deb7)
        items8.append(deb8)
        #adding universities to main array
        all.append(univ)
        all.append(univ2)
        all.append(univ3)
        all.append(univ4)
        all.append(univ5)
        all.append(univ6)
        all.append(univ7)
        all.append(univ8)
    #closing csv file
    f.close()

    #opening json file to write the main array all
    with open (outputFile, 'w') as f:
       json.dump(all, f, ensure_ascii=False)
    f.close()

#6-CONVERTING THE JSON FILE TO CSV FORMAT        
def JSONtoCSV(inputFile):
    #opening the json file to read
    with open(inputFile, 'r', encoding="utf-8") as f:
        data =json.load(f)

        #string variable to wtite to csv file
        str=""
        #adding header to str variable
        str += "University_name"+";" + "uType"+";"+"Faculty"+";"+"Id"+";"+"Language"+";"+"Second"+";"+ "Program"+";"+"Period"+";"+"Spec"+";"+"Quota"+";"+"Field"+";"+"Order"+";"+"Last_min_score"+";"+"Grant"+"\n"

        #finding keys one by one and adding to str variable for all lines in this loop
        for line in data:
          
            university_name=line['university_name']           
            uType=line['uType']          
            items=line['items']                  
            for lines in items:
                faculty=lines['faculty']               
                deps=lines['departments']         
                for deep in deps:
                    str += university_name + ";"
                    str+=uType+";"
                    str+=faculty+";"
                    program_kod=deep['id']
                    str+=program_kod+";"
                    language=deep['lang']
                    str+=language+";"
                    sec=deep['second']
                    str+=sec+";"
                    program=deep['name']
                    str+=program+";" 
                    period=deep['period']
                    str+=period+";"
                    firstStu=deep['spec']
                    str+=firstStu+";"
                    quota=deep['quota']
                    str+=quota+";"
                    field=deep['field']
                    str+=field+";"
                    lastmin=deep['order']
                    str+=lastmin+";"
                    if deep['last_min_score'] !=None:
                        lastminScore=deep['last_min_score']
                        str+=lastminScore+";"
                    elif deep['last_min_score'] ==None:
                        str+=""+";"
                    if deep['grant'] !=None:
                        scolar=deep['grant']
                        str+=scolar
                    elif deep['grant'] ==None:
                        str+=""+";"

                    #separate lines for each university
                    str+="\n"
        #closing the json file
        f.close()

        #opening the csv file to write and write the str to csv file
        with open(outputFile,"w", encoding="utf-8") as f:
            f.write(str)
        f.close()

#7-Validation method/Checking if the xml file is weel-formed
def validation(xmlFile,xsdFile):

    doc = etree.parse(xmlFile)
    root = doc.getroot()

    xmlschema_doc = etree.parse(xsdFile)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    doc = etree.XML(etree.tostring(root))

    #is_valid is a boolean variable
    validation_result = xmlschema.validate(doc)

    print(validation_result)

#Choosing method according to the number entered
if type=="1":
    CSVtoXML(inputFile)
elif type=="2":
    XMLtoCSV(inputFile)
elif type=="3":
    XMLtoJSON(inputFile)
elif type=="4":
    JSONtoXML(inputFile)
elif type=="5":
    CSVtoJSON(inputFile)
elif type=="6":
    JSONtoCSV(inputFile)
else:
    validation(inputFile,outputFile)

