def spin_words(sentence):
    arr = sentence.split(" ")
    for i in range(len(arr)):
        if len(arr[i]) > 4 : arr[i] = arr[i][::-1]
    return "".join(i + " " for i in arr)[:len(sentence)]

def refactored(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")]) #zapisanie else w skróconym ifie w takim miejscu
print(spin_words("Stop spinning my words!"))
