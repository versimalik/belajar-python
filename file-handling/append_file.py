goal_list = ["Python","HTML","CSS"]
goal_list += ["Database","Django"]


# append goal list to newnote.txt
file = open("newnote.txt","a")
file.write("\n")
for goal in goal_list:
	file.write(f"Master {goal}\n")
file.close()