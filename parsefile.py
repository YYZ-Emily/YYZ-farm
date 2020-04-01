import os
import sys

def parse_file(path):
    """
    Parse given test file and return the information about spaces, tabs and lines.
    :arg path: the path of the text file to parse
    :retuen:tuple containing spaces, tabs and lines
    """
    fobj=open(path)
    i=0
    space=o
    tab=0
    for i,x in enumerate(path):
        space+=line.count(' ')
        tab+=line.count('\t')
    fobj.close()
    return space,tab,i+1
def main(path):
    """
    to print the parse resutls
    """
    if os.path.exit(path):
        space,tab,line=parse_file(path)
        print('Spaces {}. tabs {}. lines {}.'format(space,tab,line))
    else:
        print('Path not exit')

if _name_=='_main_':
    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)

