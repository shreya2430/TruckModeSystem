# TruckModeSystem

A warehouse has certain number of trucks that transport supplies in and out of the warehouse. Each truck has a unique identifier and a counter to keep a track of how many orders did each truck fulfilled. Whenever a truck moves in/out of the warehouse its unique ID is recorded. Every day when the truck arrives at the warehouse for the first time, the counter is set to 0. 
From then onwards, the counter is incremented each time the truck enters and exits the warehouse. When the truck will leave the warehouse to deliver supplies to the client, an order will be opened against its ID in the system and the counter will be ‘odd’. This is considered as an open order. The order will be marked as closed when the truck arrives back at the warehouse and the truck’s counter will be ‘even’ at that time. If the counter is 0, it means they have not started working and have just arrived to the warehouse for the first time in the day. Hence the counter indicates the number and status of orders. 
The warehouse manager requires assistance in keeping a track of open and closed orders through an automated system. In addition to this each truck can do a maximum of ‘x’ deliveries in a day. The implemented system will also help the manager in assigning orders to each vehicle. It can identify which trucks have completed their maximum deliveries for the day and which ones can still be assigned with more orders. 
The warehouse manager uses the above system to answer the below questions: 
1. Total vehicles that came to the warehouse for work?
 2. Check specific truck whereabouts 
3. Number of open, closed and yet to be fulfilled orders
 4. List of trucks that have moved in/out of the warehouse more than ’z’ number of times. 
5. List and number of trucks that have completed their maximum deliveries for the day 
6. List and number of trucks that are currently in the warehouse and available to deliver supplies
