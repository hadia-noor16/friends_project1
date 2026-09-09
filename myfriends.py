"""Assignment 1: Friend of a Friend

Please complete these functions, to answer queries given a dataset of
friendship relations, that meet the specifications of the handout
and docstrings below.

Notes:
- you should create and test your own scenarios to fully test your functions, 
  including testing of "edge cases"
"""

from py_friends.friends import Friends

"""
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************

If you worked in a group on this project, please type the EIDs of your groupmates below (do not include yourself).
Leave it as TODO otherwise.
Groupmate 1: TODO
Groupmate 2: TODO
"""

def load_pairs(filename):
    """
    Args:
        filename (str): name of input file

    Returns:
        List of pairs, where each pair is a Tuple of two strings

    Notes:
    - Each non-empty line in the input file contains two strings, that
      are separated by one or more space characters.
    - You should remove whitespace characters, and skip over empty input lines.
    """
    list_of_pairs = []
    with open(filename, 'rt') as infile:
        for line in infile:
            list_of_pairs.append(line.strip().split(' '))
    print(list_of_pairs)

# ------------ BEGIN YOUR CODE ------------

        
        #pass    # implement your code here


# ------------ END YOUR CODE ------------

    return list_of_pairs 

def make_friends_directory(pairs):
    """Create a directory of persons, for looking up immediate friends

    Args:
        pairs (List[Tuple[str, str]]): list of pairs

    Returns:
        Dict[str, Set] where each key is a person, with value being the set of 
        related persons given in the input list of pairs

    Notes:
    - you should infer from the input that relationships are two-way: 
      if given a pair (x,y), then assume that y is a friend of x, and x is 
      a friend of y
    - no own-relationships: ignore pairs of the form (x, x)
    """
    directory = dict()

    # ------------ BEGIN YOUR CODE ------------
    for person1, person2 in pairs:
        #print(person1, person2)
        if person1 not in directory:
            directory[person1] = set()
        if person2 not in directory:
            directory[person2] = set()

        directory[person1].add(person2)
        directory[person2].add(person1)

    #print(directory)

    
    #pass    # implement your code here


    # ------------ END YOUR CODE ------------

    return directory


def find_all_number_of_friends(my_dir):
    """List every person in the directory by the number of friends each has

    Returns a sorted (in decreasing order by number of friends) list 
    of 2-tuples, where each tuples has the person's name as the first element,
    the the number of friends as the second element.
    """
    # {'CHEWBACCA': {'LUKE', 'LEIA', 'C-3PO', 'R2-D2', 'OBI-WAN', 'HAN'},
    #  'R2-D2': {'BIGGS', 'LUKE', 'BERU', 'LEIA', 'C-3PO', 'OBI-WAN', 'OWEN', 'HAN', 'CHEWBACCA'},
    #  'C-3PO': {'BIGGS', 'BERU', 'LUKE', 'LEIA', 'R2-D2', 'OBI-WAN', 'OWEN', 'HAN', 'CHEWBACCA', 'REDLEADER'},
    #  'BERU': {'LUKE', 'LEIA', 'C-3PO', 'R2-D2', 'OWEN'},
    #  'LUKE': {'BIGGS', 'BERU', 'WEDGE', 'LEIA', 'C-3PO', 'R2-D2', 'REDTEN', 'DODONNA', 'OBI-WAN', 'GOLDLEADER', 'CAMIE',
    #           'OWEN', 'HAN', 'CHEWBACCA', 'REDLEADER'}, 'OWEN': {'BERU', 'C-3PO', 'LUKE', 'R2-D2'},
    #  'OBI-WAN': {'LUKE', 'DARTHVADER', 'LEIA', 'C-3PO', 'R2-D2', 'HAN', 'CHEWBACCA'},
    #  'LEIA': {'BIGGS', 'DARTHVADER', 'LUKE', 'BERU', 'TARKIN', 'C-3PO', 'REDLEADER', 'R2-D2', 'OBI-WAN', 'HAN',
    #           'CHEWBACCA', 'MOTTI'},
    #  'BIGGS': {'LUKE', 'LEIA', 'C-3PO', 'R2-D2', 'GOLDLEADER', 'CAMIE', 'WEDGE', 'REDLEADER'},
    #  'HAN': {'LUKE', 'LEIA', 'C-3PO', 'R2-D2', 'OBI-WAN', 'CHEWBACCA'}, 'CAMIE': {'BIGGS', 'LUKE'},
    #  'DARTHVADER': {'MOTTI', 'TARKIN', 'OBI-WAN', 'LEIA'}, 'MOTTI': {'LEIA', 'DARTHVADER', 'TARKIN'},
    #  'TARKIN': {'LEIA', 'DARTHVADER', 'MOTTI'}, 'DODONNA': {'WEDGE', 'LUKE', 'GOLDLEADER'},
    #  'GOLDLEADER': {'BIGGS', 'LUKE', 'DODONNA', 'WEDGE', 'REDLEADER'},
    #  'WEDGE': {'BIGGS', 'LUKE', 'DODONNA', 'GOLDLEADER', 'REDLEADER'},
    #  'REDLEADER': {'BIGGS', 'LUKE', 'LEIA', 'C-3PO', 'REDTEN', 'GOLDLEADER', 'WEDGE'}, 'REDTEN': {'LUKE', 'REDLEADER'}}
    friends_list = []
    #count=0
    #dict={}

    # ------------ BEGIN YOUR CODE ------------

    for person in my_dir:
        number_of_friends = len(my_dir[person])
        friends_list.append((person, number_of_friends))

    print (friends_list)



    #pass    # implement your code here
    

    # ------------ END YOUR CODE ------------
    #print(friends_list)
    return friends_list


def make_team_roster(person, my_dir):
    """Returns str encoding of a person's team of friends of friends
    Args:
        person (str): the team leader's name
        my_dir (Dict): dictionary of all relationships

    Returns:
        str of the form 'A_B_D_G' where the underscore '_' is the
        separator character, and the first substring is the 
        team leader's name, i.e. A.  Subsequent unique substrings are 
        friends of A or friends of friends of A, in ASCII order
        and excluding the team leader's name (i.e. A only appears
        as the first substring)

    Notes:
    - Team is drawn from only within two circles of A -- friends of A, plus 
      their immediate friends only
    """

    # {'CHEWBACCA': {'LUKE', 'LEIA', 'C-3PO', 'R2-D2', 'OBI-WAN', 'HAN'},
    #  'R2-D2': {'BIGGS', 'LUKE', 'BERU', 'LEIA', 'C-3PO', 'OBI-WAN', 'OWEN', 'HAN', 'CHEWBACCA'},
    #  'C-3PO': {'BIGGS', 'BERU', 'LUKE', 'LEIA', 'R2-D2', 'OBI-WAN', 'OWEN', 'HAN', 'CHEWBACCA', 'REDLEADER'},
    #  'BERU': {'LUKE', 'LEIA', 'C-3PO', 'R2-D2', 'OWEN'},
    #  'LUKE': {'BIGGS', 'BERU', 'WEDGE', 'LEIA', 'C-3PO', 'R2-D2', 'REDTEN', 'DODONNA', 'OBI-WAN', 'GOLDLEADER', 'CAMIE',
    #           'OWEN', 'HAN', 'CHEWBACCA', 'REDLEADER'}, 'OWEN': {'BERU', 'C-3PO', 'LUKE', 'R2-D2'},
    #  'OBI-WAN': {'LUKE', 'DARTHVADER', 'LEIA', 'C-3PO', 'R2-D2', 'HAN', 'CHEWBACCA'},
    #  'LEIA': {'BIGGS', 'DARTHVADER', 'LUKE', 'BERU', 'TARKIN', 'C-3PO', 'REDLEADER', 'R2-D2', 'OBI-WAN', 'HAN',
    #           'CHEWBACCA', 'MOTTI'},
    #  'BIGGS': {'LUKE', 'LEIA', 'C-3PO', 'R2-D2', 'GOLDLEADER', 'CAMIE', 'WEDGE', 'REDLEADER'},
    #  'HAN': {'LUKE', 'LEIA', 'C-3PO', 'R2-D2', 'OBI-WAN', 'CHEWBACCA'}, 'CAMIE': {'BIGGS', 'LUKE'},
    #  'DARTHVADER': {'MOTTI', 'TARKIN', 'OBI-WAN', 'LEIA'}, 'MOTTI': {'LEIA', 'DARTHVADER', 'TARKIN'},
    #  'TARKIN': {'LEIA', 'DARTHVADER', 'MOTTI'}, 'DODONNA': {'WEDGE', 'LUKE', 'GOLDLEADER'},
    #  'GOLDLEADER': {'BIGGS', 'LUKE', 'DODONNA', 'WEDGE', 'REDLEADER'},
    #  'WEDGE': {'BIGGS', 'LUKE', 'DODONNA', 'GOLDLEADER', 'REDLEADER'},
    #  'REDLEADER': {'BIGGS', 'LUKE', 'LEIA', 'C-3PO', 'REDTEN', 'GOLDLEADER', 'WEDGE'}, 'REDTEN': {'LUKE', 'REDLEADER'}}

    assert person in my_dir
    label = person
    circle1=[]
    circle2=[]

    # ------------ BEGIN YOUR CODE ------------

    for person,friends in my_dir.items():
        for friend in friends:
            if person == label:
                circle1.append(friend)  # only friends of DARTHVADER in cirlce 1

                circle2.extend(my_dir[friend])  #friends of friends of circle 1. Extend func adds EACH PERSON separately, not as one item

                if label in circle2:   # we don't want Darthvader in list as he is the leader
                    circle2.remove(label)
        # if person == label:
        #     circle1.append(friend)
        #     circle2.append(my_dir[friend])
    circle= sorted(set(circle1+circle2))#adds both list of friends in circle 1 and 2, remove duplicates and combines them




    #circle=sorted(set(circle))
    print(circle)

    label = label + '_' + '_'.join(circle)  #starts with label i.e Darthvader_ and then join all elements of list as a string using _
   # print(label)                         #Since it doesn't put _ before first element of cirlce list, I had to do it after label.


    
    #pass    # implement your code here


    # ------------ END YOUR CODE ------------

    return label


def find_smallest_team(my_dir):
    """Find team with smallest size, and return its roster label str
    - if ties, return the team roster label that is first in ASCII order
    """
    smallest_teams = []
    all_friends=[]

    # ------------ BEGIN YOUR CODE
    for person,friends in my_dir.items():
        circle_1=[] # for each member, find friends from circle 1
        circle_2=[]  # for each member, find friends of friends
        circle=[]    # Sum of friends from both circles
        for friend in friends:
            circle_1.append(friend)    # append all friends of person 1
            circle_2.extend(my_dir[friend])  #append all friends of friend from circle 1
        circle=sorted(set(circle_1+circle_2))
        circle.remove(person)

        label= person + '_' + '_'.join(circle)
        all_friends.append(label)    # append all created labels in a list
    #print(all_friends)
    team={}   #empty dictionary to put all rosters and their count
    total_friends=[]

    for members in all_friends:   # takes each roster like "Han_leia_Luke_hanna"
        total_friends=members.split('_')   #splits each person by _ and put in a list
        team[members]=int (len(total_friends)-1)  #  adding item into dict, key= members, value is lenth of their roster
                                                    # find the length of list to find total length of roster,
                                                  # -1 because first name is the leader, we only need friends count
    #print(team)

    minimum=min(team.values())  # extracts minimum value from dict
    #print(minimum)

    for key,value in team.items():
        if value==minimum:   #compare each value with minimum i.e 12

            smallest_teams.append(key)  #append all the items with min value

    #print(smallest_teams)
    smallest_teams.sort() # sort items alphabetically

    #pass    # implement your code here

    
    # ------------ END YOUR CODE

    return smallest_teams[0] if smallest_teams else ""   #return first item from the list



if __name__ == '__main__':
    # To run and examine your function calls

    print('\n1. run load_pairs')
    my_pairs = load_pairs('myfriends.txt')
    print(my_pairs)

    print('\n2. run make_friends_directory')
    my_dir = make_friends_directory(my_pairs)
    print(my_dir) 

    print('\n3. run find_all_number_of_friends')
    print(find_all_number_of_friends(my_dir))

    print('\n4. run make_team_roster')
    my_person = 'DARTHVADER'   # test with this person as team leader
    team_roster = make_team_roster(my_person, my_dir)
    print(team_roster) 

    print('\n5. run find_smallest_team')
    print(find_smallest_team(my_dir))

    print('\n6. run Friends iterator')
    friends_iterator = Friends(my_dir)
    for num, pair in enumerate(friends_iterator):
        print(num, pair)
        if num == 10:
            break
    # since index 0 we read 11 elements
    print(len(list(friends_iterator)) + num + 1)
