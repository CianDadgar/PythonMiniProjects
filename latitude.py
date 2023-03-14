degrees = float(input( " Enter degrees "))
minutes = float(input( " Enter minutes "))
seconds = float(input( " Enter seconds "))

decimal = degrees + minutes/60.0 + seconds/3600.0
output = round(decimal,4)
print (output)
