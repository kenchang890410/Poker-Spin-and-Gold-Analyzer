import os
mode = 0.25
directory_path = "./025spin250729"
Prize = [mode*2, mode*3, mode*4, mode*5, mode*10]
Prize_count = [0, 0, 0, 0, 0]
win_type = [0, 0, 0, 0, 0]
win_type_rate = [0, 0, 0, 0, 0]
win_prize = 0
win_game_count = 0

# Function to read all txt files in a directory and print the third line
txt_files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]

for txt_file in txt_files:
    file_path = os.path.join(directory_path, txt_file)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read all lines in the file
            lines = file.readlines()
            
            if len(lines) >= 4:

                for i in range(5):
                    if(float(lines[3].strip().split(" ")[3].split("$")[1]) == float(Prize[i])):
                        Prize_count[i] = Prize_count[i] + 1

            if len(lines) >= 7:

                if lines[6].strip().split(" ")[3] == "1st":
                    if(float(lines[3].strip().split(" ")[3].split("$")[1])== mode*10):
                        game_prize = 8*mode
                    else:
                        game_prize = float(lines[3].strip().split(" ")[3].split("$")[1])
                    win_prize = win_prize + game_prize
                    win_game_count += 1
                    win_type[Prize.index(float(lines[3].strip().split(" ")[3].split("$")[1]))] += 1
                
                if(float(lines[3].strip().split(" ")[3].split("$")[1]) == mode*10) and (lines[6].strip().split(" ")[3] == "2nd"):
                    win_prize = win_prize + mode*2
            else:
                print(f"File: {txt_file} has less than 3 lines.")
    except Exception as e:
        print(f"Error reading {txt_file}: {e}")

game_prize_frequency = [num / sum(Prize_count) for num in Prize_count]
game_ev = 0
for i in range(5):
    game_ev += game_prize_frequency[i] * Prize[i]

for i in range(len(win_type)):
    if Prize_count[i] == 0:
        continue
    win_type_rate[i] = win_type[i] / Prize_count[i]

print("total game : ", sum(Prize_count))
print(f"win rate : {win_game_count} / {sum(Prize_count)} = {win_game_count / sum(Prize_count)}")
print("total game frequency : ", Prize_count)
print("total game prize rate : ", [num / sum(Prize_count) for num in Prize_count])
print("win_type : ", win_type)
print("win_type rate: ", win_type_rate)
print(f"profit : {win_prize} - {sum(Prize_count)*mode} = {win_prize-sum(Prize_count)*mode}")
print(f"profit {(win_prize-sum(Prize_count)*mode) / 0.25} buy in")
print("per game ev : ", game_ev)
print("per game expected profit : ", game_ev * win_game_count / sum(Prize_count) - mode)
print("expected profit: ", (game_ev * win_game_count / sum(Prize_count) - mode) * sum(Prize_count)) 
print(f"need {mode / game_ev} win rate to make a profit")
print("per game expected profit with 33% win rate: ", game_ev / 3 - mode)

print("expected profit with 33% win rate: ", (game_ev / 3 - mode) * sum(Prize_count)) 
