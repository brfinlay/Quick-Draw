from quickdraw import QuickDrawData
qd = QuickDrawData()

### Test run ###   
# ant = qd.get_drawing("ant")
# ant.image.save("/Users/brendafinlay/Documents/Cusack Lab/ant.gif")

all_objects = ["ant", "bee", "ear", "flamingo", "lion", "snail", "tiger", "zebra", "faces", "beaver", "cockroach", "fly", "goldfish", "goose", "gorilla", "grasshopper", "hamster", "hog", "koala", "ladybug", "otter", "ox", "peacock", "starfish", "triceratops", "wing", "ambulancce", "barn", "bathtub", "church", "mailbox", "stove", "television", "tractor", "bookcase", "crib", "desk", "jeep", "library", "pole", "racer", "refrigerator", "restaurant", "screen", "swing", "backpack", "banana", "baseball", "basketball", "broccoli", "broom", "bucket", "candle", "envelope", "hammer", "lipstick", "microphone", "nail", "necklace", "paintbrush", "pillow", "pineapple", "pizza", "radio", "screwdriver", "shovel", "sock", "strawberry", "teapot", "umbrella", "acorn", "balloon", "bib", "bow", "bubble", "cauliflower", "chain", "cheeseburger", "coffeepot", "cucumber", "daisy", "diaper", "drum", "gown", "hay", "hook", "hotdog", "jean", "kite", "knot", "lampshade", "lemon", "lotion", "mailbag", "mask", "mitten", "orange", "pajama", "pot", "pretzel", "safe", "sandal", "sunglass", "sunglasses", "sweatshirt", "tray", "wallet", "whistle", "wig"]

#### This function pulls a random drawing for each word ####
def get_image(list):
    for word in list:
        w = qd.get_drawing("%s" %word)
        if w.recognized == True:
            w.image.save("/Users/brendafinlay/Documents/Cusack Lab/Quick_Draw/%s.gif" %word)

get_image(all_objects)

# dodgy_drawings = ["ant", "ear", "lion", "tiger", "zebra"]

# def correct_image(list):

