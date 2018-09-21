def function(temp):
    
    for i in range(3):
        print(temp)
        temp += [1]
        function(temp)

temp = [1]
function(temp)

