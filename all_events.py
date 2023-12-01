import random


def encounter_event():  # DONE, finish unittest
    """
    Determine if the player encounters an event.

    :postcondition: return a boolean value indicating whether the character encounters an event
    :return: a boolean value of character-event encounter
    """
    encounter = random.random()
    if encounter < 0.25:  # the chance of an event happens is 25%
        return True
    else:
        return False


def event(character):  # DONE, finish unittest
    """
    Simulate a typing game where the player attempts to solve a Leetcode question.

    :param character: a dictionary contains character status
    :precondition: character must contain 'Difficulty', 'Knowledge','Name', and 'Stress' as keys
    :postcondition: 'Knowledge' and 'Stress' will be updated based on user's input
    """
    difficulty = character["Difficulty"]
    progress = 0
    attempt_times = 0
    print('You discover an interesting Leetcode Question.🤔\n(Hint: You can type anything to try to solve.)')
    while progress < 100:
        attempt_text = input()
        # the player will make progress when the enter something
        if attempt_text:
            attempt_times += 1
            progress += random.randint(10, 50)
            progress = min(progress, 100)  # ensure progress doesn't exceed 100
            print('You have finished %d%%' % progress)
        else:
            print('Hint: You can type anything to try to solve.')
    character["Knowledge"] += (4 - difficulty) * 1  # higher difficulty will have less gained knowledge
    character["Stress"] += attempt_times
    print('Great job, %s!' % character['Name'])
    print('You have learned from this. [Knowledge = %d]' % character["Knowledge"])
    print('However, you are more stressed now. [Stress = %d]' % character["Stress"])
    return character


def interview(character):  # DONE
    """
    Simulate a job interview screening process based on the knowledge of character.

    :param character: a dictionary describing the character
    :precondition: character must contain "Knowledge" as keys
    :postcondition: execute the specific function based on character's knowledge value
    """
    print('You have arrive the interview room.💼💻')
    if character["Knowledge"] <= 15:  # the character has to have 15 knowledge to have a chance to be hired
        handle_unsuccessful_candidate(character)
    else:
        conduct_interview(character)


def handle_unsuccessful_candidate(character):  # DONE, finish unittest
    """
    Handle the case when the character's knowledge is not sufficient for the job.

    :param character: a dictionary describing the character
    :precondition: character must contain "Knowledge" and "Stress" as keys
    :postcondition: modify the character's info based on the unsuccessful interview

    >>> character1 = {"Knowledge": 10, "Stress": 14}
    >>> handle_unsuccessful_candidate(character1)
    Sorry, your skills and experience do not meet our current needs.
    Please try to study more and come back.
    You are exhausted from this interview. [Stress = 24]
    However, you also learn from this. [Knowledge = 11]
    """
    character["Stress"] += 10
    character["Knowledge"] += 1
    print('Sorry, your skills and experience do not meet our current needs.')
    print('Please try to study more and come back.')
    print('You are exhausted from this interview. [Stress = %d]' % character["Stress"])
    print('However, you also learn from this. [Knowledge = %d]' % character["Knowledge"])


def conduct_interview(character):  # DONE, finish unittest
    """
    Simulate a job interview process and assess the character's suitability for the position.

    :param character: a dictionary describing the character
    :precondition: character must contain "Knowledge", "Stress",and "Hired" as keys
    :postcondition: modify the character's info based on the game's outcome
    """
    actual_number = random.randint(1, 5)
    guess_number = input('People say interviewing is a numbers game, let\'s pick a number between 1 and 5. ')
    try:
        guess_number = int(guess_number)
    except ValueError:
        character["Stress"] += 5
        print("Oh, you can't even type numbers?!")
        print('Sorry, your skills and experience do not meet our current needs.')
        print('Your current stress is [Stress = %d]' % character["Stress"])
    else:
        if actual_number != guess_number:
            character["Stress"] += 5
            print('Sorry, your skills and experience do not meet our current needs.')
            print('[Stress +5], your current stress is [Stress = %d]' % character["Stress"])
        else:
            character["Hired"] = True


def home(character):  # DONE, finish unittest
    """
    Decrease character's stress when at home.

    :param character: a dictionary describing the character
    :precondition: character must contain "Stress" as key
    :precondition: cat.txt must exist in the package
    :postcondition: reduce character 'Stress' by 3, and print out useful information
    """
    character["Stress"] = max(character["Stress"] - 3, 0)  # decrease stress by 3, but won't go below zero
    with open("cat.txt") as file_object:
        text = file_object.read()
        print(text)
    print("Your cat welcomes you home")
    print("You have lower your stress [Stress = %d]" % character["Stress"])
    return character