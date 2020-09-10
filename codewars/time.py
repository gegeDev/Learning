import unittest
def make_readable(seconds):
    hours = seconds // 3600 
    seconds -= 3600 * hours
    minutes = seconds // 60
    seconds -= minutes * 60
    if hours < 10: hours = "0" + str(hours)
    if minutes < 10: minutes = "0" + str(minutes)
    if seconds < 10: seconds = "0" + str(seconds)
    return "{0}:{1}:{2}".format(hours, minutes, seconds)

def refactored(seconds):
    return "{:02}:{:02}:{:02}".format(seconds // 3600, s / 60 % 60, s % 60)
    #jak widać takie użycie format sprawia że przed jednocyfrowymi liczbami jest zero ale nie wiem jak to działa, do sprawdzenia kiedyś (czytaj nigdy)
class Testy(unittest.TestCase):
    def test_first(test):
        test.assertEqual(make_readable(0), "00:00:00")
        test.assertEqual(make_readable(5), "00:00:05")
        test.assertEqual(make_readable(60), "00:01:00")
        test.assertEqual(make_readable(86399), "23:59:59")
        test.assertEqual(make_readable(359999), "99:59:59")

unittest.main()
