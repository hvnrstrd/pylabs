import json

file_path = r'C:\Users\HVNAERO\Desktop\labs4\jsonex\sample-data.json'
with open(file_path, 'r') as file:
    data = json.load(file)
output = "Interface Status\n"
output += "="*80 + "\n"
output += "{:<50} {:<20} {:<8} {:<6}\n".format("DN", "Description", "Speed", "MTU")
output += "-"*80 + "\n"

for interface in data['imdata']:
    for key, value in interface.items():
        dn = value['attributes']['dn']
        descr = value['attributes'].get('descr', '')
        speed = value['attributes'].get('speed', 'inherit')
        mtu = value['attributes']['mtu']
        output += "{:<50} {:<20} {:<8} {:<6}\n".format(dn, descr, speed, mtu)

print(output)
