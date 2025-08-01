# voting system
# user details (input, age_check, udate , resistorer check)
# count voutes
# diffrent candiates
# winner announcement
# 
candidates_list={
        "c1":{
            "name":"jhon",
            "votes": 0,
            "symbol":" 🗳️ "
        },
        "c2":{
            "name":"Anna",
            "votes": 0,
            "symbol":" 🌟 "
        }
    } 

Resistor_details = {
        "user1": {
            "id": 1,
            "name": "imad",
            "age": 20,
            "voting_status":False
        },
        "user2": {
            "id": 2,
            "name": "eman",
            "age": 20,
            "voting_status":False
        },
        "user3": {
            "id": 3,
            "name": "khan",
            "age": 20,
            "voting_status":False
        },
        "user4": {
            "id": 4,
            "name": "ali",
            "age": 16,
            "voting_status":False
        },

        "user5":{
            "id": 5,
            "name": "sara",
            "age": 18,
            "voting_status":True
        }
    }
# user details function
def user_details(Name):
    print("\n--- User Details ---")
    Name = Name.lower()
    
    for user in Resistor_details.values():
        if Name == user["name"].lower():
            if user["age"]>18 and user["voting_status"]==False: 
                print("Welcome ", user["name"] ,"you are eligible to vote!")
            elif user["age"]<18:
                print("You are not eligible!")
            
            elif user["voting_status"]==True:
                print("You have already voted!")

def candidates():
    print ("List of candidates:")
    for candidate in candidates_list.values():
        print(f" Candidate = {candidate['name']}, Symbol = {candidate['symbol']}")

# vote function

def vote(choice_name, user_name):
    user_name = user_name.lower()
    choice_name = choice_name.lower()

    for user in Resistor_details.values():
        if user_name == user["name"].lower():
            if user["voting_status"]:
                print(" You have already voted!")
                return

          
            for key, candidate in candidates_list.items():
                if candidate["name"].lower() == choice_name:
                    candidates_list[key]["votes"] += 1
                    user["voting_status"] = True
                    print(f" Thank you for voting for {candidate['name']}!")
                    return

            print(" Invalid candidate name. Please try again.")
            return

    print("User not found. Please check your name and try again.")

# winner function
def winner():
    max_votes=0
    w_name=" "
    for candidate  in candidates_list.values():
        if candidate["votes"]> max_votes:
            max_votes = candidate["votes"]
            w_name = candidate["name"]
        if max_votes>0:
            print(f"The winner is {w_name} with {max_votes} votes! 🎉")
        
        else:
            print("No votes were cast. No winner can be declared.")

def display_results():
    print("\n--- Voting Results ---")
    for candidate in candidates_list.values():
        print(f"{candidate['name']}: {candidate['votes']} votes {candidate['symbol']}")
  

# voting system
def main():
    while True:
        print("Welcome to the Voting System!")
        print("1. Check User Details")
        print("2. Cast Vote")
        print("3. display results")

        choice=input("Enter your choice (1-3) or 'exit' to quit: ")
        if choice =="1":
            name=input("Please enter your details to check if you are eligible to vote.")
            user_details(name)
        elif choice =="2":
            candidates()
            user_name=input("Enter your name to vote: ").lower()
            user_details(user_name)
            vote_choice = input("Enter the candidate's name to vote (jhon/anna): ").lower()
            vote(vote_choice,user_name)
        elif choice =="3":
            display_results()
            winner()
        else:
            print("Invalid choice. Please try again.")

        if choice.lower() == 'exit' or choice.lower() == 'quit':
            print("Exiting the voting system. Thank you!")
            break

main()