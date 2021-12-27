from datetime import datetime
from datetime import timedelta

def time(): 
    
    j = datetime.now()
    s1 = j.strftime("%H:%M:%S")
    s2 = '07:27:00'
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    
    if tdelta.days < 0:
        tdelta = timedelta(days=0,seconds=tdelta.seconds, microseconds=tdelta.microseconds)

    b = tdelta.total_seconds()
    return b
  
  
  def time2(): 
    
    j = datetime.now()
    s1 = j.strftime("%H:%M:%S")
    s2 = '19:27:00'
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    
    if tdelta.days < 0:
        tdelta = timedelta(days=0,seconds=tdelta.seconds, microseconds=tdelta.microseconds)

    b = tdelta.total_seconds()
    return b

target_channel_id = # Insert Channel ID 
  
@tasks.loop(hours=24)
async def called_once_a_day():
    
    message_channel = client.get_channel(target_channel_id)
    await message_channel.send("WYSI @everyone")

@tasks.loop(hours=24)
async def called_once_a_day2():
    
    message_channel = client.get_channel(target_channel_id)
    await message_channel.send("WYSI @everyone")

@called_once_a_day.before_loop
async def before():

    await client.wait_until_ready()
    await asyncio.sleep(time())

    print("Finished waiting")

@called_once_a_day2.before_loop
async def before():

    await client.wait_until_ready()
    await asyncio.sleep(time2())

    print("Finished waiting")
    
client.run(#Bot Token)
