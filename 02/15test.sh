#! /bin/bash
diff <(tail -5 hightemp.txt) <(python 15.py 5)
diff <(tail -15 hightemp.txt) <(python 15.py 15)
diff <(tail -100 hightemp.txt) <(python 15.py 100)
