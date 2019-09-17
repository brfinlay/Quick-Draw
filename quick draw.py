from quickdraw import QuickDrawData
qd = QuickDrawData()

# n=268
objects_list = ["angel", "ant", "bear", "bat", "bee", "bird", "butterfly", "camel", "cow", "crab", "crocodile", "dog", "dolphin", "dragon", "duck", "elephant", "cat", "campfire", "face", "fish", "flamingo", "frog", "giraffe", "hedgehog", "horse", "hurricane", "kangaroo", "lightning", "lion", "lobster", "mermaid", "monkey", "mosquito", "mouse", "ocean", "arm", "ear", "elbow", "eye", "leg", "nose", "mouth", "octopus", "owl", "panda", "parrot", "penguin", "pig", "rabbit", "raccoon", "rain", "rhinoceros", "river", "scorpion", "shark", "sheep", "snail", "snake", "spider", "squirrel", "star", "swan", "tiger", "toe", "tornado", "zebra", "windmill", "airplane", "ambulance", "anvil", "axe", "barn", "bathtub", "bed", "bench", "bicycle", "bridge", "bulldozer", "bus", "bush", "cactus", "cannon", "canoe", "car", "castle", "cello", "chair", "chandelier", "church", "cloud", "computer", "couch", "dishwasher", "door", "dresser", "fence", "fireplace", "garden", "helicopter", "hospital", "house", "jail", "ladder", "laptop", "lighthouse", "mailbox", "microwave", "moon", "mountain", "oven", "parachute", "piano", "pond", "pool", "rainbow", "sailboat", "sink", "skyscraper", "snowman", "speedboat", "stairs", "stove", "streetlight", "submarine", "suitcase", "sun", "sword", "table", "television", "tent", "toilet", "tractor", "train", "tree", "truck", "van", "whale", "wheel", "apple", "asparagus", "backpack", "banana", "bandage", "baseball", "basket", "basketball", "belt", "binoculars", "blackberry", "blueberry", "book", "boomerang", "bowtie", "bracelet", "brain", "bread", "broccoli", "broom", "bucket", "cake", "calculator", "calendar", "camera", "candle", "carrot", "clarinet", "clock", "compass", "cookie", "cooler", "crayon", "crown", "cup", "diamond", "drill", "dumbbell", "envelope", "eraser", "eyeglasses", "fan", "feather", "finger", "flashlight", "flower", "foot", "fork", "grass", "guitar", "hamburger", "hammer", "hand", "harp", "hat", "headphones", "helmet", "hourglass", "jacket", "key", "keyboard", "knee", "knife", "lantern", "leaf", "lighter", "lipstick", "lollipop", "map", "marker", "megaphone", "microphone", "motorbike", "mug", "mushroom", "nail", "necklace", "onion", "paintbrush", "pants", "passport", "peanut", "pear", "pencil", "pillow", "pineapple", "pizza", "pliers", "popsicle", "postcard", "potato", "purse", "radio", "rake", "rifle", "sandwich", "saw", "saxophone", "scissors", "screwdriver", "shoe", "shorts", "shovel", "skateboard", "skull", "snorkel", "snowflake", "sock", "spoon", "spreadsheet", "steak", "stereo", "stethoscope", "strawberry", "sweater", "syringe", "teapot", "telephone", "toaster", "tooth", "toothbrush", "toothpaste", "trombone", "trumpet", "umbrella", "underwear", "vase", "violin", "watermelon", "wristwatch"]
included = ["beach", "beard", "goatee", "moustache"]

#### This function pulls a random drawing that was successfully identified for each word ####
# Index was changed to get images 1-10 and saved into respective index1-20 folders in Quick_Draw -> Transferred to USB stick
def get_image(list):
    for word in list:
        w = qd.get_drawing("%s" %word, index=20)
        if w.recognized == True:
            w.image.save("/Users/brendafinlay/Documents/Cusack_Lab/index 20/%s.gif" %word)

get_image(included)

# Index folders have different n numbers because image at index x will only be pulled if it satisfies w.recognised==True






