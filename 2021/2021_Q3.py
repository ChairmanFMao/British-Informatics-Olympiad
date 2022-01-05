word = input()
desired = list(word)
window = ["A","B"]
smallest = 100

def search(moves):
    if (moves > 10):
        return
    if window == desired:
        global smallest
        if moves < smallest:
            smallest = moves
    
    if (len(window) >= 2):
        window[0], window[1] = window[1], window[0]
        search(moves+1)
        window[1], window[0] = window[0], window[1]
        window.append(window.pop(0))
        search(moves+1)
        window.append(window.pop())
        window.append(chr(ord(window[len(window)-1]) + 1))
        search(moves+1)

search(2)
print(smallest)