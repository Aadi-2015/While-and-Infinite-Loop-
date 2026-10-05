# My chore checklist countdown

# Part 1: Chores
total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to complete today.")

# Part 2: Keep a counter
completed_count = 0 
chores_num = 1

# Part 3:The While Loop 
while chores_num == total_chores:
    # Part 4:
    if chores_num == 1: next_chore ="Make your bed"
    elif chores_num == 2: next_chore = "Feed the pet"
    elif chores_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"
    
    answer = input(f"Have you finished:  {next_chore}? (yes/no): ")
    
    # Part 5:
    if answer == "yes":
        completed_count += 1
        chores_num += 1
        print("Great job, chore completed!")
    else:
        print("Finish it soon.")
        
    # Part 6:
    print(f"Chores remaining   :{total_chores - completed_count}")
    
# Part 7:
print("======ALL CHORES COMPLETE======")   
print(" Great Work completing all chores today.")

# Part 8:
print("Now let's safely peek at an infinite loop....")
test = 0
safecounter = 0
while test<= 0:
    print("This value never changes so this will run forever.")
    safecounter += 1
    if safecounter ==3:
        print("(Stopping here purpose a real infinite loop never stops)") 
        break
    
# 
print("\n==Chore list summary==")
print("Chores assinged today :",original_count)         
print("Chores completed today :",completed_count)
print("Chores remaining :",total_chores-completed_count)
print("==========================================================")