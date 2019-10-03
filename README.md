# Illumio-Coding-Challenge

## Time started the challenge:
  2:29 PM MST
  
## Time Finished the challenge:
 3:58 PM MST
 
## Time started README.md:
4:00 PM MST

## Time finished README.md:
4:28 PM MST

## Solution to Coding Challenge:
  ### Code Flow:
  - The program uses a set to hold both directions and protocols. That is because sets can not have duplicate direction or protocol. So, it works very well in this case.
  - It uses a dictionary that holds ranges for both port numbers and ip address numbers, I used ipaddress class' built-in comparison functions to compare between IP Address ranges.
  - If all directions, protocols, ports and IP Addresses exist in the class, then there is no need to go through the rest of the csv file (since a baseline would be ~500k lines)
  - Used a dictionary for ports and ranges to have O(1) get, set and delete. 
  - For ports and addresses, the program goes through each dictionary, and checks whether the argument is in the range of any of the elements of the dictionary. Otherwise, create a new element with the given arguments. So, worst case is O(n) where n is the length of the dictionary.
  - Finally, have boolean values to check if all values in direction, protocol, port, IP Address exist to briefly decrease the running time of the algorithm.
  
The code was tested with the given examples, and it passed them.
Unfortunately, I did not have time to add any comments
  

## Teams Interested In:
I'm really interested in the platform and policy teams, I think that the work they do is fantastic and really fun, and I would really enjoy working with them since I have already worked on similar technologies such as: 
  - RESTful API Development
  - Caching (I worked on a high-volume project at work, where I had to migrate our cache from Memcached to Redis, and minimize time taken to process data since all customers use the data saved in the cache)
  - SQL (I worked on MySQL and SQLite)
  - Web Development (I've worked on frameworks such as Django, Flask and ASP.NET and would really enjoy working on Ruby)
 
 ### Platform Team:
 The areas that interest me in the platform team are: 
 - Authentication and Authorization
 - Caching and Persistence
 - API support
 
 ### Policy Team
 The areas that interest me in the policy team are:
 - Getting more experience writing concurrent code for a distributed system that is deployed in Illumio's SaaS (as referenced from the Illumio website)
 - Working on technologies such as Redis, Ruby, NGINX and Kubernetes/Docker


# Looking forward to hearing back from Illumio for this amazing opportunity!
