need_conversion=input("Enter the input like convert to what you need:").lower()
given_value=float(input("Enter the value which need to be converted:"))
if need_conversion=="convert speed to kmph":
    given_value*=18/5
    print(str(given_value)+"km/hr")
elif need_conversion=="convert speed to m/sec":
    given_value*=5/18
    print(str(given_value)+"m/sec")