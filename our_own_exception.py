class valuetoohigherror(Exception):
    pass
class valuetoolowerror(Exception):
   def __init__(self, message, value):
      self.message  = message
      self.value = value
def test_value(x):
    if x>100:
     raise valuetoohigherror('value is too high')
    if x<100:
       raise valuetoolowerror('value too low', x)
try:
   test_value(1)
except valuetoolowerror as e:
   print(e.message, e.value)