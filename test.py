#!/usr/bin/python3

from Field import Field

slice = [Field(None), Field(2), Field(None), Field(4), Field(2), Field(2),  Field(4)]

slice = [Field(None), Field(None), Field(None), Field(None), Field(2), Field(2),  Field(4)]

def moveSlice(slice, toleft):
    if not toleft:
        slice.reverse()
    last = None # indicate index of last number which can be uped
    for i in range(len(slice)):
        if slice[i].getValue() == ".":
            continue
        elif last == None:
            last = 0
            (slice[last], slice[i] ) = (slice[i], slice[last])
        elif slice[last].getValue() == slice[i].getValue():
            slice[last].up()
            slice[i] = Field(None)
            last += 1
        elif slice[last].getValue() == ".":
            (slice[last], slice[i]) = (slice[i], slice[last])
        else:
            last += 1
            slice[last] = slice[i]
            slice[i] = Field(None)
    if not toleft:
        slice.reverse()
    return slice


print(*moveSlice(slice, 0))

