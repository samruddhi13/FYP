from MCP3008 import MCP3008

thislist = []

adc = MCP3008()
for i in range(6):

    value = int(adc.read( channel = i )) # You can of course adapt the channel to be read out
    processedvalue =  round((value / 1023.0 * 3.3) ,2)
    thislist.insert(i, processedvalue)

#print("Applied voltage: %.2f" % (value / 1023.0 * 3.3) )

print(thislist)