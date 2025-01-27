from datetime import datetime 

# =>  Get current date and time 
getdatetime = datetime.now()
print("current data and time = "  ,getdatetime) #current data and time =  2025-01-26 22:19:15.126430
print("Year =", getdatetime.year) # Year = 2025
print("Month =", getdatetime.month) # Month = 1
print("Day =", getdatetime.day) # Day = 26
print("Hour =", getdatetime.hour) # Hour = 22
print("Minute =", getdatetime.minute) # Minute = 21
print("Second =", getdatetime.second) # Second = 25

# =>  Create a specific datetime 
setdatetime = datetime(2004,11,1,0,32,40)
print("My birthday is = " , setdatetime)

# => Strftime , string Formatting Date time 
getnow = datetime.now()
formatdatetime = getnow.strftime("%Y-%B-%d %H:%M:%S")
print("Formatted Date Time = ", formatdatetime)  # 2025-January-26 22:35:35


# =>  strptime () , conbert a string to datetime
strdate = "2025-01-26 22:25:44"
convertdate = datetime.strptime(strdate,"%Y-%m-%d %H:%M:%S")
print("Converted Datetime = ", convertdate) #2025-01-26 22:25:44
