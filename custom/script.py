import glob


img_paths = glob.glob("images/val/*")

with open("val.txt", "w+") as f:
    for p in img_paths:
        f.write(p)
        f.write('\n')
