# COMP-1510-202330-Term-Project

## Your name:
Charlie Ho

## Your student number:
A01358146

## Your GitHub account ID:
char-lie-ho

## Any important comments you'd like to make about your work:

#### Game overview
Welcome to the CST Student Adventure at BCIT! In this text-based game, 
you'll step into the shoes of a Computer Systems Technology (CST) student navigating the challenges of BCIT. 
Your ultimate goal is to reach Term 4, ace an interview, and secure a job.

As you walk on the map, you will encounter Leetcode questions ,and you will have to solve them. 
Successfully answering a question will reward you with valuable knowledge, essential for advancing to higher terms.

To reach the interview, gather enough knowledge and head to the bottom right corner of the map. 
Your success in the interview may lead to a job offer. However, be mindful of your stress level. 
If it surpasses 50, your character will pass out, bringing the game to an end. 
Need a break? Visit home to reduce stress.


#### Package overview
To start the adventure, execute the `game.py` file. This is the entry point for the game.

In the `text` folder, you will find the external text files. 
Spoiler alert, don't open the text files after playing the game.

In the `test`, you will find all the unittests for all functions. 
This game has been thoroughly tested to minimize potential errors.

#### Required Information
| Requirement                           | Location                                                        | 
|---------------------------------------|-----------------------------------------------------------------| 
| Selection using if-statement          | In `advance.py`, inside `check_advance` function, line 23       | 
| Using the for-loop                    | In `game.py`, inside `display_map` function, line 50            | 
| Membership operator is used correctly | In `game.py`, inside `get_user_choice` function, line 77        | 
| Range function is used                | In `game.py`, inside `display_map` function, line 50            | 
| Itertools is thoughtfully used        | In `all_events.py`, inside `event` function, line 28            | 
| Random module is used                 | In `all_events.py`, inside `encounter_events` function, line 13 | 
| formatted f-strings                   | In `all_events.py`, inside `event` function, line 41            | 
| List comprehension                    | In `move.py`, inside `validate_move` function, line 24 & 25     | 


#### Contents of folder
    COMP1510TermProject/
    |-- text/
    |   |-- game_end1.txt
    |   |-- game_end2.txt
    |   |-- advance.txt
    |   |-- cat.txt
    |   |-- interview.txt
    |   |-- intro.txt
    |
    |-- __init__.py
    |-- advance.py
    |-- all_events.py
    |-- end_game.py
    |-- game.py
    |-- initialize_game.py
    |-- level_10_in_aardwolf.pdf
    |-- load_game.py
    |-- move.py
    |-- game.pdf
    |-- README.md
    |
    |-- test_advance.py
    |-- test_character_advance.py
    |-- test_conduct_interview.py
    |-- test_describe_current_location.py
    |-- test_display_map.py
    |-- test_encounter_event.py
    |-- test_end_of_game.py
    |-- test_event.py
    |-- test_game_difficulty.py
    |-- test_get_user_choice.py
    |-- test_handle_unsuccessful_candidate.py
    |-- test_home.py
    |-- test_make_board.py
    |-- test_move_character.py
    |-- test_validate_move.py
    |

*** end of document ***