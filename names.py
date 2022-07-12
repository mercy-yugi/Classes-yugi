from paramiko import Agent


def student():
    list=[{age:19,name:'Mercy'},{age:20,name:'Yugi'}]
    for age,name in list.items():
        print(age,name)
student()
