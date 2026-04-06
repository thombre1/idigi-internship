import asyncio

# This is our async function, might take some time
async def brew_chai(name):
    print(f"Started brewing {name} chai...")
    await asyncio.sleep(2)
    print("Chai Brewed.")
    

# Our main Function can also be async and it awaits for the result of the await funtion call inside it
# First the Masala chai will go and it will wait async-ly due to asyncio.sleep() 
# instantaneously the execution will be switched to next function
# The next function if sync, it will wait for its execution 
# If the next function is async, it will execute till if finds a await
# As soon as a await is found it will wait async-ly for it to finish, till then it moves on to the next function
# When the await returns its value it will be put in the Event Queue and Executed according to its order in that queue
async def main():
    await asyncio.gather(
        brew_chai("Masala"),
        brew_chai("Ginger"),
        brew_chai("Elaichi"),
            )

asyncio.run(main())
