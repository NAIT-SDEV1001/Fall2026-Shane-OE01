# *args must be before the **kwargs

def order_summary(*items, **options):
    print("Items: ")
    #loop through items (tuple)
    for item in items:
        print(f"- {item}")

    #loop through options
    for key, value in options.items():
        print(f"{key}: {value}")


order_summary("burger","pasta","milkshake",takeout = True, bag = False)
#options {"takeout":True,"bag":False}