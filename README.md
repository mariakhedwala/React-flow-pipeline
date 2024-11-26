To set the **backend** up go to /backend dir make sure you have 'uvicorn' installed, you can get it using 'pip install uvicorn'
then hit uvicorn main:app --reload

To set-up **frontend** go to /frontend dir and hit
1. npm install //installs the deps
2. npm start //starts the Frontend server


This project is built in react and uses react-flow library to use draggable nodes and create handles.
1. Create nodes by dragging them into the dotted background.(you can see the mini map on the right, and controls on left)
2. Once dragged multiple nodes, connect them via handles by making edges.
3. If the desired graph is made, submit the chart/graph by clicking on submit button.
4. Submit hits the api to the backend and gives the response which shows the number of nodes, edges and if the graph is DAG.
