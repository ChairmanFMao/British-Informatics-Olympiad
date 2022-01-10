def a():
    n = int(input())
    message = input()

    # Turn the first rotor every time, turn the second rotor every 4
    # Must go in cycles of 16
    n %= 16

    # All of the values are decremented, negative values go to 3
    def rotate(rotor):
        for i in range(4):
            rotor[i] = rotor[i] - 1 if rotor[i] else 3
        rotor.append(rotor.pop(0))
        return rotor

    # This sets up the rotors
    rotor1 = [0,3,1,2]
    rotor2 = [0,2,1,3]
    reflector = [3,2,1,0]

    # This does all of the moves before encoding
    for i in range(n):
        rotor1 = rotate(rotor1)
        if i % 4 == 3:
            rotor2 = rotate(rotor2)

    # This will encode a character according to the current rotors
    def encode(letter):
        pos = ord(letter)-65
        pos = rotor1[pos]
        pos = rotor2[pos]
        pos = reflector[pos]
        for i in range(4):
            if rotor2[i] == pos:
                pos = i
                break
        for i in range(4):
            if rotor1[i] == pos:
                pos = i
                break
        return chr(pos+65)

    out = ""
    for i in range(len(message)):
        out += encode(message[i])
        # This keeps rotating the wheels
        n += 1
        rotor1 = rotate(rotor1)
        if not n % 4:
            rotor2 = rotate(rotor2)

    print(out)

a()

"""
Part b:
Just ran the code with: "0" and "AAAAAA"
BCBCDB
"""

"""
Part c:
I have found one way that works.
"""

"""
Part d:
No, this is not possible, if the encryption of A is B, then the encryption of
B, in that state, is A. This would make it impossible for A to encrypt to B,
as well as, B encrypting to C. C would have to encrypt to D and A would have
to encrypt to B if we take the first part of the statement as truth. If we took
the second part, B would encrypt to C and A would encrypt to D.
"""
