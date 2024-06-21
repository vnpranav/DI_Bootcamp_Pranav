import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "1990-01-01"
print("Updated data:", data)

with open('person.json','w') as f:
    json.dump(data, f, indent=4)