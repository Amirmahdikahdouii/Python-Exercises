shekarestan_suffering = int(input())
shekarestan_death = int(input())
namakestan_suffering = int(input())
namakestan_death = int(input())
if shekarestan_suffering - shekarestan_death > namakestan_suffering - namakestan_death:
    print("Shekarestan")
elif shekarestan_suffering - shekarestan_death == namakestan_suffering - namakestan_death:
    print("Equal")
else:
    print("Namakestan")