# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np
import copy

def move_up(cost_to_come,parent_node): #Applies up move, if there is obstacle returns original node
    x = parent_node[0]
    y = parent_node[1]
    move = y+1
    up = ((x,move), 1.0)
    return up

def move_up_right(cost_to_come,parent_node): #Applies up_right move, if there is obstacle returns original node
    x = parent_node[0]
    y = parent_node[1]
    movex = x + 1
    movey = y + 1
    up_right = ((movex, movey),1.4)
    return up_right

def move_right(cost_to_come,parent_node): #moves blank right after checking for obstacle, if there is obstacle returns original node
    x = parent_node[0]
    y = parent_node[1]
    move = x + 1
    right = ((move,y), 1.0)
    return right

def move_down_right(cost_to_come,parent_node): #moves blank right after checking for obstacle, if there is obstacle returns original node
    x = parent_node[0]
    y = parent_node[1]
    movex = x + 1
    movey= y-1
    down_right = ((movex, movey),1.4)
    return down_right

def move_down(cost_to_come,parent_node): #moves blank right after checking for obstacle, if there is obstacle returns original node
    x = parent_node[0]
    y = parent_node[1]
    movey= y-1
    down = ((x, movey), 1.0)
    return down

def move_down_left(cost_to_come,parent_node): #moves blank right after checking for obstacle, if there is obstacle returns original node
    x = parent_node[0]
    y = parent_node[1]
    movey= y-1
    movex= x-1
    down_left = ((movex, movey),1.4)
    return down_left

def move_left(cost_to_come,parent_node): #moves blank left after checking for obstacle, if there is obstacle returns original node
    x = parent_node[0]
    y = parent_node[1]
    movex = x - 1
    left = ((movex, y), 1.0)
    return left

def move_up_left(cost_to_come,parent_node): #moves blank left after checking for obstacle, if there is obstacle returns original node
    x = parent_node[0]
    y = parent_node[1]
    movex = x - 1
    movey = y+1
    up_left = ((movex, movey),1.4)
    return up_left

def generate_path(reverse_path):
    next_node = []
    while next_node != "N/A":
        search_for = reverse_path[-1]
        reverse_path.append(cost_to_come[search_for]['parent node'])
        next_node = cost_to_come[search_for]['parent node']

    print("This is the reverse path from goal to start", reverse_path)

    # This loop creates the forward path to goal
    t = 0
    forward_path = []
    for t in range(len(reverse_path)):
        forward_path.append(reverse_path.pop(-1))

    # # this eliminates the start node from forward_path
    forward_path.pop(0)
    return forward_path

def check_for_goal(parent_node, goal_node):
    SolutionFound=False
    if parent_node == goal_node:
        SolutionFound=True
    return SolutionFound


cost_to_come=[]
visual_map=np.zeros((250, 600, 3), np.uint8)
visual_map[0:250,0:600,:] = [0,0,255]

x=0
y=0
node = 0
cost_to_come={}
for x in range(600):
    for y in range(250):
        node=(x,y)
        cost_to_come[node]={'x':0, 'y':0, 'parent node':"N/A", 'cost to come':0}
#cost_to_come = [node_id, x, y, parent node, cost to come]
        if (x >= 95) and (x <= 155) and (y >= 0) and (y <= 105):  #Obstacle A check
            cost_to_come[node]={'x': x,'y': y,'parent node': "N/A", 'cost to come':-1.0}
        else:
            if (x >= 95) and (x <= 155) and (y >= 145) and (y <= 250): #Obstacle B check
                cost_to_come[node]={'x': x,'y': y,'parent node': "N/A", 'cost to come':-1.0}
            else:
                #Obstacle C1 check
                if (x >= 300 - 37.5*3**0.5-5) and (x <= 300) and (y >= -(1/3)**(0.5)*(x-300)+(125-75-50**(0.5))) and (y <= (1/3)**(0.5)*(x-300)+(125+75+50**(0.5))):
                    cost_to_come[node]={'x': x,'y': y,'parent node': "N/A", 'cost to come':-1.0}
                else:
                    #Obstacle C2 check
                    if (x <= 300 + 37.5*3**0.5+5) and (x >= 300) and (y >= (1/3)**(0.5)*(x-300)+(125-75-50**(0.5))) and (y <= -(1/3)**(0.5)*(x-300)+(125+75+50**(0.5))):
                        cost_to_come[node]={'x': x,'y': y,'parent node': "N/A", 'cost to come':-1.0}
                    else:
                        #Obstacle D check
                        if (x >= 455) and (y >= (105/60)*(x - 515) + 125) and (y <= -1*(105/60)*(x - 515) + 125):
                            cost_to_come[node]={'x': x,'y': y,'parent node': "N/A", 'cost to come':-1.0}
                        else:
                            #Walls check
                            if (x <= 5) or (x >= 595) or (y <= 5) or (y >= 245):
                                cost_to_come[node]={'x': x,'y': y,'parent node': "N/A", 'cost to come':-1.0}
                            else:
                                cost_to_come[node]={'x': x,'y': y,'parent node': "N/A", 'cost to come': float('inf')}
                                visual_map[y,x,:] = [100,100,100]
        # node = node + 1

#Visualize Space
cv2.imshow("Zeros matx", visual_map)  # show numpy array
cv2.waitKey(0)  # wait for ay key to exit window
cv2.destroyAllWindows()  # close all windows

SolutionFound = False
# parent_node=0
counter=0

#Initialize the starting point
start_cost=0.0
bad_choice=True
while bad_choice == True:
    start_x=input('What is the x coordinate (integer only) of your starting point?\n')
    start_x=int(start_x)
    start_y=input('What is the y coordinate (integer only) of your starting point?\n')
    start_y=int(start_y)
    start_node=(start_x,start_y)
    if cost_to_come[start_node]['cost to come'] == -1:
        print('This is an invalid starting position, please try again.\n')
    else:
        bad_choice=False

cost_to_come[start_node]['cost to come']=0.0

#Define goal node by x,y coordinates
bad_choice = True
while bad_choice == True:
    goal_x = input('What is the x coordinate (integer only) of your target position?\n')
    goal_x=int(goal_x)
    goal_y = input('What is the y coordinate (integer only) of your target position?\n')
    goal_y=int(goal_y)
    goal_node=(goal_x, goal_y)
    if cost_to_come[goal_node]['cost to come'] == -1:
        print('This is an invalid target position, please try again.\n')
    else:
        bad_choice = False

#Initialize list of nodes that need to be expanded/investigated/have moves applied
queue={}
queue[start_node]=cost_to_come[start_node]['cost to come']
#print(queue)
closed_list = []
while SolutionFound!=True:           #counter<10:
    # print("Counter", counter)
    #sort queue for lowest cost_to_come
    # cost_order={}

    queue=sorted(queue.items(), key = lambda cost: cost[1])

    # identify the parent node and eliminate it from the list of nodes that need to be investigated
    parent_node=queue.pop(0)
    parent_node=parent_node[0]
    queue=dict(queue)
    # check if the last popped node is a match for goal
    # if it's a match, initializes reverse_path list and adds node to node map

    SolutionFound=check_for_goal(parent_node, goal_node)
    if SolutionFound == True:
        print(cost_to_come[parent_node])
        reverse_path = [goal_node,cost_to_come[goal_node]['parent node']]
        print(reverse_path)
        break

    closed_list.append(parent_node)

# #     #perform "moves" on "parent" node to create "new" nodes
# #     #each function checks for a valid move, if not valid, returns "parent" node

    up=move_up(cost_to_come,parent_node)
    # print(cost_to_come[parent_node])
    # print(cost_to_come[up])

    up_right=move_up_right(cost_to_come,parent_node)
    # print(cost_to_come[parent_node])
    # print(cost_to_come[up_right])
    right=move_right(cost_to_come,parent_node)
    # print(cost_to_come[parent_node])
    # print(cost_to_come[right])
    down_right=move_down_right(cost_to_come,parent_node)
    # print(cost_to_come[parent_node])
    # print(cost_to_come[down_right])
    down=move_down(cost_to_come,parent_node)
    # print(cost_to_come[parent_node])
    # print(cost_to_come[down])
    down_left=move_down_left(cost_to_come,parent_node)
    # print(cost_to_come[parent_node])
    # print(cost_to_come[down_left])
    left=move_left(cost_to_come,parent_node)
    # print(cost_to_come[parent_node])
    # print(cost_to_come[left])
    up_left=move_up_left(cost_to_come,parent_node)
    # print(cost_to_come[parent_node])
    # print(cost_to_come[up_left])

    #stores the "new" nodes in another dictionary for future use in loop
    action_dict={0:up, 1:up_right,2:right,3:down_right,4:down,5:down_left,6:left, 7: up_left}

    #initialize variable before loop begins
    match=False

    #for each action in action_dict loop runs (outer for-loop)
    for j in range(len(action_dict)):
        match=False
#         #inner for-loop checks one "new" node from action_dict to determine
        for i in range(len(closed_list)):
            # print("length closed list =", + len(closed_list))
            #checks if "new" node is already in the closed list
            if action_dict[j][0] == closed_list[i] or cost_to_come[action_dict[j][0]]['cost to come'] == -1:
                i=i+1
                break
            #checks if "new" node is in an obstable space
            # if cost_to_come[action_dict[j][0]]['cost to come'] == -1:
            #     i=i+1
            #     break
            #if node is not in an obstacle or in the closed list, calc new cost-to-come
            # print(cost_to_come[parent_node])
            new_cost_to_come = cost_to_come[parent_node]['cost to come'] + action_dict[j][1]
            if cost_to_come[parent_node]['cost to come'] + action_dict[j][1] < cost_to_come[action_dict[j][0]]['cost to come']:
                cost_to_come[action_dict[j][0]]['cost to come']=cost_to_come[parent_node]['cost to come'] + action_dict[j][1]
                cost_to_come[action_dict[j][0]]['parent node']=parent_node
                node=action_dict[j][0]
                queue[node]=cost_to_come[action_dict[j][0]]['cost to come']
    counter=counter+1
#    print(counter)
#This loop creates the reverse path by searching for the next parent node until the start node's parent "NA" is found
forward_path=generate_path(reverse_path)

x=[]
y=[]
visual_map_explore=visual_map
for i in range(len(closed_list)):
    coord=closed_list[i]
    x=250-int(coord[1])
    y=int(coord[0])
    visual_map_explore[x][y]=0
    cv2.imshow("Zeros matx", visual_map_explore)  # show numpy array
    cv2.waitKey(1)  # wait for ay key to exit window

cv2.destroyAllWindows()  # close all windows

x=[]
y=[]
for i in range(len(forward_path)):
    coord=forward_path[i]
    x=250-int(coord[1])
    y=int(coord[0])
    visual_map[x,y,:] = [0,255,0]
    cv2.imshow("Zeros matx", visual_map)  # show numpy array
    cv2.waitKey(50)  # wait for ay key to exit window

cv2.waitKey(0)  # wait for ay key to exit window

cv2.destroyAllWindows()  # close all windows

