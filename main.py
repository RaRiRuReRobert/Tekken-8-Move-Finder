from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


#Tekken 8 move finder
#Find every move of a given frame data by web scraping online resource

character = input("Welcome to the Tekken 8 move finder!\nWhat character's moveset would you like to search through?: ")

frame_search = input("How many startup frames would you like the move to have?: ")

include_below = input("Would you like to find moves with fewer startup frames as well(Yes/No): ")
##depending on the response a different function is called

url = f"https://wavu.wiki/t/{character}_movetable"

#opens url
response = requests.get(url)
movetable_webpage = response.text
soup = BeautifulSoup(movetable_webpage, "html.parser")

#Get all startup frames in a list
move_startup = [startup_frames.getText().strip("i,")for startup_frames in soup.find_all(name="td", class_="field_Startup")]
move_input = [frames.getText().strip(f"{character}-")for frames in soup.find_all(name="td", class_="field_Move")]

result_frames = []
result_inputs = []
all_inputs_and_frames = []

#print(move_startup)
#print(move_input)

#Reductive method for narrowing down which moves to display\


def exact_frames():
    global move_startup
    global move_input
    global all_inputs_and_frames
    for frames in move_startup:
        frame_index = move_startup.index(frames)
        if frames == "":
            frame_data = 1000
        elif "~" in frames:
            frame_data = int(frames[:2])
        else:
            frame_data = int(frames)

        if frame_data == int(frame_search):
            result_frames.append(move_startup[frame_index])
            result_inputs.append(move_input[frame_index])
            data = {
                "input":move_input[frame_index],
                "startup frames": move_startup[frame_index],
            }
            all_inputs_and_frames.append(data)
            del move_startup[frame_index]
            del move_input[frame_index]


def fewer_frames():
    global move_startup
    global move_input
    global all_inputs_and_frames
    for frames in move_startup:
        frame_index = move_startup.index(frames)
        if frames == "":
            frame_data = 1000
        elif "~" in frames:
            frame_data = int(frames[:2])
        else:
            frame_data = int(frames)

        if frame_data <= int(frame_search):
            result_frames.append(move_startup[frame_index])
            result_inputs.append(move_input[frame_index])
            data = {
                "input": move_input[frame_index],
                "startup frames": move_startup[frame_index],
            }
            all_inputs_and_frames.append(data)
            del move_startup[frame_index]
            del move_input[frame_index]
#print(result_frames)
#print(result_inputs)

if include_below == "Yes":
    fewer_frames()
    print(all_inputs_and_frames)
elif include_below == "No":
    exact_frames()
    print(all_inputs_and_frames)
else:
    print("Invalid input, please rerun program")
