paths = input("\nEnter the flight trace path (comma separated): ").split(', ')

path_dict = {}
for position in range(len(paths)):
    int_list = paths[position].split(' => ')
    path_dict[int_list[0]] = int_list[1]

    
print (path_dict)
source = input("\nChoose the starting place: ").upper()
destination = input("\nChoose the destination: ").upper()


flight_path = []
flight_path.append(source)
flight_path.append(path_dict[source])
next_hop = path_dict[source]


for position in path_dict.items():
    if path_dict[next_hop] == destination:
        flight_path.append(destination)
        break
    else:
        flight_path.append(path_dict[next_hop])
        next_hop = path_dict[next_hop]

        
flight_path = " => ".join(flight_path)


flight = '''  ,--.
  \  _\_
  _\/_|_\____.'\\
-(___.--._____(
     \   \\
      \   \\
       `--'
       '''
print(flight)
print(flight_path)
