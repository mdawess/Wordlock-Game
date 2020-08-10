"""Starter code for CSC108 Assignment 1 Winter 2020"""

# Game setting constants
SECTION_LENGTH = 3
ANSWER = 'CATDOGFOXEMU'

# Move constants
SWAP = 'S'
ROTATE = 'R'
CHECK = 'C'
 
def get_section_start(section_num: int) -> int: 
    """Return the starting index of the section corresponding to section_num.
    
    >>> get_section_start(1)
    0
    >>> get_section_start(3)
    6
    """
    return SECTION_LENGTH * (section_num - 1)  
    

def is_valid_move(move: str) -> bool:
    """Return True if and only if move is one of 'S', 'R' or 'C'.
    
    >>> is_valid_move('S')
    True
    >>> is_valid_move('T')
    False
    """
    if move == 'S':
        return True 
    elif move == 'R':
        return True 
    elif move == 'C':
        return True 
    else: 
        return False 
    
def is_valid_section(section: int) -> bool: 
    """Return True if and only if the section is greater then 0 but 
    less than num_sections.
    
    >>> is_valid_section(1)
    True 
    >>> is_valid_section(5)
    False 
    """
    num_sections = len(ANSWER) / SECTION_LENGTH
    
    return bool(0 < section <= num_sections)

def check_section(state: str, section: int) -> bool:
    """Return true if and only if the specified section in state
    matches the specified section in ANSWER.
    
    >>> check_section('CATGODXOFEMU', 1)
    True 
    >>> check_section('CATGODXOFEMU', 2)
    False 
    """
    return bool(state[((section * SECTION_LENGTH) - SECTION_LENGTH):\
    (section * SECTION_LENGTH)] == ANSWER[((section * SECTION_LENGTH) -\
    SECTION_LENGTH):(section * SECTION_LENGTH)])
           
def change_state(state: str, section: int, move: str) -> str:
    """Return a new string that reflects the updated state after a
    valid move was applied to the chosen section. 
    
    >>> change_state('wrdokoclgmaee', 2, 'S')
    'wrdolockgmae'
    >>> change_state('atcgodxofemu', 1, 'R')
    'catgodxofemu'
    """
    if move == 'S' and section == 1:
        return state[SECTION_LENGTH - 1] + state[1:SECTION_LENGTH - 1] +\
        state[0] + state[SECTION_LENGTH:]
    elif move == 'S' and section >= 2:
        return state[:SECTION_LENGTH * (section - 1)] +\
        state[(SECTION_LENGTH * section) - 1] +\
        state[(SECTION_LENGTH * (section - 1) + 1):\
        (SECTION_LENGTH * section - 1)] +\
        state[SECTION_LENGTH * (section - 1)] +\
        state[SECTION_LENGTH * section:]
    elif move == 'R' and section == 1:
        return state[(SECTION_LENGTH * section - 1)] +\
        state[SECTION_LENGTH * (section - 1):(SECTION_LENGTH * section) - 1] +\
        state[SECTION_LENGTH * section:]
    elif move == 'R' and section >= 2:
        return state[:SECTION_LENGTH * (section - 1)] +\
        state[(SECTION_LENGTH * section) - 1] +\
        state[(SECTION_LENGTH * (section - 1)):\
        ((SECTION_LENGTH * section) - 1)] +\
        state[SECTION_LENGTH * section:]
    else:
        return None
    
     

def get_move_hint(state: str, section: int) -> str:
    """Return a move suggestion based on the specified section and 
    current state of the word.
    
    >>> get_move_hint('TACDOGOXFEMU', 3)
    'R'
    >>> get_move_hint('TACDOGXFOEMU', 1)
    'S'
    """
    
    x = (section * SECTION_LENGTH) - SECTION_LENGTH
    y = (section * SECTION_LENGTH * 2) - (SECTION_LENGTH * section) 
    
    z = state[x:y]
    w = ((SECTION_LENGTH * (section - 1)) + 1)
    
    if z[::-1] == ANSWER[x:y]:
        return 'S'
    
    elif state[w] != ANSWER[w]:
        return 'R'
    else: 
        return None