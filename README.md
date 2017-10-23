# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax

# Name: Maxwell Logan
# Contact: mlogan@uoregon.edu

## ACP Time Calculator

There are several distances for a brevet, 200, 300, 400, 600, and 1000
km. Based on the start date and time that the user enters, as well as
the distance for each the control point, the calculator displays 
information on when the point opens and closes. 

The calculation works in two cases:
- The control point is under the brevet distance
- The control point is equal to or above the brevet distance

In the former, the open and close times are calculated based on a
table at https://rusa.org/octime_alg.html that displays various
maximum and minimum speeds a biker can go within specific distances.
The open times use the minimum distances and speeds, while the closing
times use the maximum ones. The calculation is then made, with the 
minimum or maximum kilometer divided by the min or max speed. The 
whole number is subtracted from that value, used as the number of 
hours, and the decimals left over are converted to the number of 
minutes, giving the total time elapsed since the brevet started.

If a control point distance is above a section on the table at
https://rusa.org/octime_alg.html , then the distances are split up
and the pieces of the race that are within specific distance ranges
are calculated using those specific speeds.

In the latter, the open time is calculated as above, but the closing
time is dictated by a set of default times, as mentioned in Article 9
of https://rusa.org/pages/rulesForRiders .

## ACP Controle Times

That's "controle" with an 'e', because it's French, although "control"
is also accepted. Controls are points where   
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must  
arrive at the location.   

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html . Additional background information
is in https://rusa.org/pages/rulesForRiders .  

We are essentially replacing the calculator at
https://rusa.org/octime_acp.html . We can also use that calculator
to clarify requirements and develop test data.  

## AJAX and Flask reimplementation

The current RUSA controle time calculator is a Perl script that takes
an HTML form and emits a text page. The reimplementation will fill in
times as the input fields are filled.  Each time a distance is filled
in, the corresponding open and close times should be filled in.