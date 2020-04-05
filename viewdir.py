def view_dir(path='.'):
    import os
    names=os.listdir(path)
    names.sort()
    for name in names:
        print(name,end=' ')
    print()
