# from Exscript.util.interact import read_login
# from Exscript.protocols import Telnet
# from Exscript import Account

# # Reading login credentials
# # account = read_login()  # This reads from user input (username and password)
# account = Account(name="admin", password="ccp123")# This reads from user input (username and password)

# print(account)
# # Establishing Telnet connection
# conn = Telnet()
# conn.connect('192.168.110.3')
# conn.login(account)

# # Sending commands
# conn.execute('system-view')
# # conn.execute('ccp123')


# # conn.execute('quit')
# # conn.execute('save')
# # conn.execute('yes')

# conn.execute('quit')

# # Closing connection
# conn.send('exit')
# conn.close()
# print("Configuration completed successfully.")

import time
from Exscript.protocols import Telnet
from Exscript import Account

# Define router configurations
routers = [
    {'host': '192.168.110.5', 'username': 'admin', 'password': 'ccp123'},
    # {'host': '192.168.110.3', 'username': 'admin', 'password': 'ccp123'},
    # {'host': '192.168.110.4', 'username': 'admin', 'password': 'ccp123'},
    # Add more routers as needed
]

# Function to connect to a router and execute commands
def configure_router(router, account):
    conn = Telnet()
    try:
        conn.connect(router['host'])
        conn.login(account)
        print(f"Connected to {router['host']}")

        # Sending commands
        conn.execute('system-view')
        time.sleep(1)  # Adding sleep to ensure prompt is available
        conn.execute('interface GigabitEthernet0/0/1')
        time.sleep(1) 
        conn.execute('ip address 192.168.110.1 24')
        # time.sleep(1)  
        conn.execute('quit')
        time.sleep(1)  # Adding sleep to ensure the quit command has been processed
        print(f"Prompt received: {conn.response}")

        conn.send('save')  # Command to save the configuration
        print("Save command executed")

        # Log the full interaction
        # print(f"Expecting save confirmation prompt...")
        # conn.expect(r'Are you sure you want to save? \[Y/N\]:')
        print(f"Prompt received: {conn.response}")

        # Send confirmation to save
        conn.send('Y')
        conn.send('\n')  # Sending enter to confirm the command
        time.sleep(1)  # Adding sleep to ensure the save command has been processed

        # Log the final output
        print(f"Final Output: {conn.response}")

        # Exit the router session
        conn.send('exit')
        conn.close()
        print(f"Configuration completed on {router['host']}")
    except Exception as e:
        print(f"Failed to configure {router['host']}: {e}")

# Configure each router
for router in routers:
    # Update router credentials with user input
    account = Account(name=router['username'], password=router['password'])
    configure_router(router=router, account=account)
