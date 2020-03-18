import corona_info as ci
from termcolor import colored

while True:
    print(colored('[01]', 'red'), colored('Create Corona Status', 'green'))
    print(colored('[02]', 'red'), colored('Current Corona Break Down By Country', 'green'))
    print(colored('[03]', 'red'), colored('Current Corona Breaking News', 'green'))
    print(colored('[04]', 'red'), colored('Get Advice For Corona', 'green'))
    print(colored('[05]', 'red'), colored('Exit', 'green'))

    def coronaInfo(select):
        print('****************************************')
        if select == "1":
            return ci.get_stats()
        elif select == "2":
            return ci.get_table()
        elif select == "3":
            return ci.get_news()
        elif select == "4":
            return ci.get_advice()
        elif select == "5":
            exit()
        else:
            print("Please Select right One")
        

    coronaInfo(select = input("Select One: "))
    print('****************************************')