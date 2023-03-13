READ ME for Project2.py

NOTE to TA:
Since the map is symetrical, I just flip the map when plotting it with a simple y=250-y transform.

Libraries used in this code:
python "copy" library is loaded, but not used
python opencv2 library is loaded for visualization
python numpy library is loaded for array manipulation and plotting


Functions defined in this code:
move_up - Applies up move action and returns new node
move_up_right - Applies up-right move and returns new node
move_right - Applies right move and returns new node
move_down_right - Applies down-right move and returns new node
move_down - Applies down move and returns new node
move_down_left - Applies down-left move and returns new node
move_left - Applies left move and returns new node
move_up_left - Applies up-left move and returns new node
generate_path - accepts reverse_path variable (which at this point is only the goal node 
		index and the parent node index) and searchs sequentially for parent nodes
		until the start node is reached.  It nows the start node has been reached
		when the next parent node is "N/A".  The function then uses a loop to
		reverse the order.  Then the meaningless parent node, "N/A", is removed
		from the list.  The forward path is then returned to the main code.

Instructions for use:
The only thing a user needs to do to run the program and click run.
They will be shown the map and obstacles, which the user should press any key to clear.
They will then be prompted to input a starting x coordinate after which they should press enter.
Then they will then be prompted to input a starting x coordinate after which they should press enter.
The program will check to see if it the combination of x and y coordinates is a valid starting
position.  If not, the program will promt for new entries.
This above process is followed to get the goal position.
Once the goal value is determined to be valid, the program will begin creating the node graph.
When the optimal path is found, a window will appear showing the order in which the nodes were
investigated.  Once the investigated nodes are done populating, the optimal path is shown in green.



