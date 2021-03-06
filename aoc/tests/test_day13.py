import unittest

from aoc.day13 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual((7, 3), solve1('''/->-\        
|   |  /----\\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   '''))
        print('Solving 1')
        self.assertEqual((108, 60), solve1(text))

    def test_solve2(self):
        self.assertEqual((6, 4), solve2('''/>-<\  
|   |  
| /<+-\\
| | | v
\>+</ |
  |   ^
  \<->/'''))
        print('Solving 2')
        self.assertEqual((92, 42), solve2(text))


text = '''           /----------------------------------------------------------------\                                     /-----------------\                 
           |                                                                |                              /------+-----------------+-----------\     
    /------+---------------\                /-------------------------------+------------------------------+------+---------------\ |           |     
    |      |               |                v                 /-------------+-------------\                |      |               | |           |     
    |      |               |                |   /-------------+-------------+-------------+----------------+------+---------------+-+---------\ |     
    |      |               |           /----+---+---\         |             |             |     /----------+------+-----------\   | |         | |     
    |      |               |           |    |   |   |         |            /+-------------+-----+----------+-----\|           |   | |         | |     
   /+------+---------------+-----------+----+---+---+---------+------------++-------------+-----+----------+-\   ||           |   | |         | |     
   ||      |               |       /---+----+---+---+---------+------------++-------------+-----+-------\  | |   ||           |   | |         | |     
   ||      |               | /-----+---+----+-\ |   |         |         /--++-------------+-----+-------+--+-+---++----\      |   | |         | |     
   ||      |               | |     |   |    | | |   |        /+---------+--++-------------+-----+-------+--+-+---++----+------+---+-+----\    | |     
/--++------+---------------+-+-----+---+----+-+-+---+--------++---------+--++---\         |  /--+-------+--+-+---++----+------+\  | |    |    | |     
|  ||      |               | |     |   |    | | |   |        ||         |  ||   |         |  |  |       |  | |   ||    |      ||  | |    |    | |     
|  ||      |               | |     |   |  /-+-+-+---+----\  /++---------+--++---+-\      /+--+--+-------+--+-+---++----+------++--+-+----+----+-+-\   
|  ||      | /-------------+-+-----+---+--+-+-+-+---+----+--+++---------+--++---+-+------++--+--+-\     |  ^ |   ||    |     /++--+-+----+\   | | |   
|  ||      | |          /--+-+-----+---+--+-+-+-+---+----+--+++---------+--++---+-+------++--+-\| |     |  | |   ||/---+-----+++--+-+----++--\| | |   
|  ||      | |          |  | | /---+---+--+-+-+\|   |    |  |||         |/-++---+-+------++--+-++-+-----+--+-+-\ |||   |     |||  | |    ||  || | |   
|  ||      | |          |  | | |/--+---+--+-+-+++---+----+--+++---------++-++---+-+------++--+-++\|     |  | | | |||   |     |||  | |    ||  || | |   
|  |\------+-+----------+--/ | ||  |   |  | | |||   |    |  |||         || ||   | |      ||  | ||||     |  | | | |||   |     |||  | |    ||  || | |   
|  |       | |          |    | ||  |   | /+-+-+++---+----+--+++---------++-++---+-+------++--+-++++-----+--+-+-+-+++---+-----+++--+-+--\ ||  || | |   
|  |       | |          |    \-++--+---+-++-+-/||   |    |  |||         || ||   | |      ||  | ||||     |  | | | |||   |     |||  | |  | ||  || | |   
|  |       | |          |      ||  |   | || v  ||/--+----+--+++---------++-++---+-+------++--+-++++-----+--+-+-+-+++---+--\  |||  | |  | ||  || | |   
|  |       | |          |      ||  |   \-++-+--+++--/    |  |||         || ||   | |      ||  | ||||     |  | | | |||   |  |  |||  | |  | ||  || | |   
|  |   /---+-+----------+-----\||  |     || |  |||       |  |||         || ||   | |      ||  | ||||     |  | | | |\+---+--+--+++--+-/  | ||  || | |   
|  |   |   | |          |     |||  |     || |  |||   /---+--+++---------++-++---+\|     /++--+-++++----\|  | | | | |   |  |  |||  |    | ||  || | |   
|  |   |  /+-+----------+---\ |||  |     || |  |||   |   |  |||    /----++-++---+++---\ |\+--+-++++----++--+-+-+-+-+---+--+--+++--+----+-++--++-+-/   
|  |   |  || |          |/--+-+++--+-----++-+--+++---+\  |  \++----+----++-++---++/   | | |  | ||||    ||  | | | | |   |  |  |||  |    | ||  || |     
|  |   |  || |      /---++--+-+++--+-----++-+--+++---++--+-\ || /--+----++-++---++----+-+-+--+-++++---\||  | | | | |   |  |  |||  |    | ||  || |     
|  |   |  || |     /+---++--+-+++--+-----++-+--+++---++--+-+-++-+--+----++-++---++----+-+-+--+-++++---+++--+-+-+\| |   |  |  |||  |    | ||  || |     
|  |   |  || |     ||   ||  | |||  |     || |  |||   ||  | | || |  |/---++-++---++--\ | | |  | ||||   |||  | | ||| |   |  |  |||  |    | ||  || |     
|  |   |  || |  /--++---++--+-+++--+-\   || |  |||  /++--+-+-++-+--++---++-++---++-\| | | |  | ||||   |||  | | ||| |   |  |  |||  |    | ||  || |     
|  |   |  || |  |  ||   || /+-+++--+-+---++-+--+++--+++--+-+-++-+--++---++-++---++-++-+-+-+--+-++++---+++--+-+-+++-+-\ |  |  |||  |    | ||  || |     
|  |   |  || |  |  ||   || || |||  | |   || |  |||  |||  | | || |  ||   || ||/--++-++-+-+-+--+-++++---+++--+-+-+++-+-+-+--+--+++--+----+-++--++\|     
|  |   |  || |  |  ||   || || |||  | | /-++-+--+++--+++--+-+-++\|  ||   || |||  || || | | |  | ||||   |||  | | ||| | | |  |  |||  |    | ||  ||||     
|  |   |/-++-+--+--++---++-++-+++--+-+\| || |  |||  ||| /+-+-++++-<++---++-+++-\|| || | | |  | ||||   |||  \-+-+++-+-+-+--+--+++--+----+-++--+++/     
|  |   || || |  |  ||   || || |||  | ||| || |  |||  ||| || | ||||  ||   || ||| ||| || | | |  | ||||   |||    | ||| | | |  |  |||  |    | ||  |||      
|/-+---++-++-+--+--++--\|| || |||  | ||| || |/-+++--+++-++-+-++++--++---++-+++-+++-++-+-+-+--+-++++---+++----+-+++-+\| |/-+--+++--+----+-++--+++----\ 
|| |   || || |  |  ||  ||| || |||  | ||| || || |||  ||| || | ||||  ||   || ||| ||| || | |/+--+-++++---+++----+-+++-+++-++\|  |||  |    | ||  |||    | 
|| |   || || |  |  ||  ||| || |||  | ||v || || |||  ||| || | ||||  ||   || ||| ||| || | |||/-+-++++---+++--\ | ||| ||| ||||  |||  |    | ||  |||    | 
|| |   || || |  |  ||  ||| ||/+++--+-+++-++-++-+++--+++-++-+-++++--++---++-+++-+++-++\| |||| | ||||   |||  | | |v| \++-++++--+++--+----+-++--/||    | 
|| |   || || |  |  ||  ||| ||||||  | |||/++-++-+++--+++-++-+-++++--++---++-+++-+++-++++-++++-+-++++---+++--+-+\|||  || ||||  |||  |    | ||   ||    | 
|| |   || || |  |  ||  ||| ||||||  | |||||| || |||  ||| || | ||||  ||   || ||| ||| |||| |||| | ||||   |||  | |||||  || ||||  |||  |    | ||   ||    | 
|| |   || || |  |  ||  ||| ||||||  | |||||| || ||| /+++-++-+-++++--++---++-+++-+++-++++-++++-+-++++---+++--+-+++++--++-++++--+++--+----+-++---++\   | 
|| |   || || |  |  ||  ||| |||||| /+-++++++-++-+++-++++-++-+-++++--++---++-+++-+++-++++-++++-+-++++---+++--+-+++++--++-++++-\|||  |    | ||   |||   | 
|| |   || || |  |  ||  ||| |||||| || |||||| || ||| |||| || | |||\--++---++-+++-+++-++++-++++-+-++++---/||  |/+++++--++-++++-++++\ |    | ||   |||   | 
|| |   || || |  |  ||  ||| |||||| || |||||| || ||| ||||/++-+-+++---++---++-+++-+++-++++-++++-+-++++\   || /+++++++--++\|||| ||||| |    | ||   |||   | 
|| |   || || |  |  ||  ||| |||||| || |||||| || ||| ||||||| | |||   ||   || ||| ||| |||| |||| | |||||   || ||||||||  ||||||| ||||| |    | ||   |||   | 
|| \---++-++-+--+--++--+++-++++++-++-++++++-++-+++-+++++++-+-+++---++---++-+++-+++-++++-++++-+-+++++---++-+++/||||  ||||||| ||||| |    | ||   |||   | 
||     || || |  |  \+--+++-++++++-++-++++++-++-+++-+++++++-+-+++---++---++-+++-+++-++++-++++-+-+++++---++-+++-++/|  ||||||| ||||| |    | ||   |||   | 
||     || || |  |   |  ||| |||||| || |||||| || ||| ||||||| | |||   ||   || ||| ||| |||| |||| | |||||   || ||| || |  ||||||| ||||| |    | ||   |||   | 
|| /---++-++-+--+---+--+++-++++++-++-++++++-++-+++-+++++++-+-+++---++---++-+++-+++\|||| |||| | |||||   || ||| || |  ||||||| ||||| |    | ||   |||   | 
|| |   || || |  |   | /+++-++++++-++-++++++-++-+++-+++++++-+-+++---++---++-+++-++++++++-++++-+-+++++\  || ||| || |  ||||||| ||||| |    | ||   |||   | 
|| |   || || | /+---+-++++-++++++-++-++++++-++-+++-+++++++-+-+++---++\  || ||| |||||||| |||| | ||||||  || ||| || |  ||||||| ||||| |    | ||   |||   | 
|| |   || || | ||   | |||| |||||| || |||||| || ||| ||\++++-+-+++---+++--++-+++-++/||||| |||| | ||||||  || ||| || |  ||||||| ||||| |    | ||   |||   | 
|| |   || || | ||   | |||| |||||| || |||||| || ||| || |||| | |||   |||  || ||| || ||||| |||| | ||||||  || ||| || |  ||||||| ||||| |    | ||   |||   | 
|| |   || || | ||   | |||| |||||| || |||||| || ||| |\-++++-+-+++---+++--++-+++-++-+/||| |||| | ||||||  || ||| || |  ||||||| ||||| |    | ||   |||   | 
|| |   || || | ||   | |||| |||||| || ||||||/++-+++-+--++++-+-+++---+++--++-+++-++-+-+++-++++-+-++++++--++-+++-++-+--+++++++-+++++-+--\ | ||   |||   | 
|| |   || || | ||   | |||| |||||| || ||||||||| ||| |  |||| | |||   |||  || \++-++-+-+++-++++-+-++++++--++-+++-++-/  ||||||| ||||| |  | | ||   |||   | 
|| |   || || | ||   | |||| |||||| || ||||||||| |\+-+--++++-+-+++---+++--++--++-++-+-+++-++++-+-++++++--++-+++-++----+++++++-+++++-+--+-+-++---/||   | 
|| |   || || | ||   | ||||/++++++-++-+++++++++-+-+\|  |||| | |||   |||  ||  || || | ||| \+++-+-++++++--/| |||/++<---+++++++-+++++-+--+-+-++----++---+\\
|| |   || || | ||   | ||||||||||| || ||||||||| | |||  |||| | \++---+++--++--++-++-+-+++--+++-+-++++++---+-++++++----+++++++-+++++-+--+-+-/|    ||   ||
|| |   || |^ | ||   | ||||||||||| || |||||||||/+-+++--++++-+--++---+++\ ||  || || | |||  ||| | ||||||   | ||||||    ||||||| ||||| |  | |  |    ||   ||
|| |   || || | ||   | ||||||||||| || ||||||||||| |||  |||| | /++---++++-++--++-++-+-+++--+++-+-++++++---+-++++++--\ ||||||| ||||| |  | |  |    ||   ||
|| |   || || | ||   | ||||||||||| || ||||||||||| |||  |||| | |||   |||| ||  || || | |||  ||| | ||||||   | ||||||  | ||||||| ||||| |  | |  |    ||   ||
|| |/--++-++-+-++---+-+++++++++++-++-+++++++++++-+++--++++-+\|||   |||| ||  || || | |||  ||| | ||||||   | ||||||  | ||||||| ||||| |  | |  |    ||   ||
|| ||  || || | ||   | ||||||||||| || ||||||||\++-+++--++++-+++++---++++-++--++-++-+-+++--+++-+-++++++---+-++++++--+-/|||||| ||||| |  | |  |    ||   ||
|| ||  || || | ||   | |||\+++++++-++-++++++++-++-+++--/||| |||||/--++++-++--++-++-+-+++--+++-+-++++++---+-++++++\ |  |||||| ||||| |  | |  |    ||   ||
|| ||  ||/++-+-++---+-+++-+++++++-++-++++++++-++-+++---+++-++++++--++++-++--++-++-+-+++--+++-+-++++++---+-+++++++\|  |||||| ||||| |  | |  |    ||   ||
|| ||  ||||| | ||   | ||| ||||||| || |||||\++-++-+++---++/ ||||||  |^|| || /++-++-+-+++--+++-+-++++++---+-+++++++++--++++++-+++++-+--+-+--+----++-\ ||
||/++--+++++-+-++---+\||| ||||||| || ||||| || || |||   ||  ||||||  |||| |\-+++-++-+-+++--+++-+-++++++---+-+++++/|||  |||||| ||||| |  | |  |    || | ||
|||||  ||||| | ||   ||||| ||||||| || ||||| || || |||   ||  ||||||  |||| |  ||| || | |||  ||| | ||||||   | ||||| |||  |||||| ||||| |  | |  |    || | ||
|||||  ||||| | ||   ||||| ||||||| |\-+++++-++-++-+++---++--++++++--++++-+--+++-++-+-+++--+++-+-++++++---//+++++-+++--++++++-+++++-+--+-+--+\   || | ||
|||||  ||||| | ||   ||||| ||||||| |  ||\++-++-++-+++---++--++++/|  ||||/+--+++-++-+-+++--+++-+-++++++----++++++-+++--++++++-+++++-+--+-+\ ||   || | ||
|||||  ||||| | ||   ||||| ||||||| |  || || || || |||   ||  |||| |  ||||||  ||| || | |||  |||/+-++++++----++++++-+++--++++++-+++++-+--+\|| ||   || | ||
|||||  ||||| | ||   ||||| ||||||| |  || || || || |||   || /++++-+--++++++--+++-++-+-+++--+++++-++++++----++++++-+++--++++++-+++++-+--++++-++---++-+\||
|||||  ||||| | ||   ||||| ||||||| |  || || || || |||   || ||||| |  ||||||  ||| || | |||  ||||\-++++++----++++++-+++--++++++-+++/| |  |||| ||   || ||||
|||||  ||||| | \+---+++++-+++++++-+--++-++-++-++-+++---++-+++++-+--++/|||  ||| || | |||  ||||  ||||||    |||||| |||  |||||| ||| | |  |||| ||   || ||||
|||^|  ||||| |  |   ||||| ||||||| |  || || || || |||   || ||||| |  || |||  ||| || | |||  |||| /++++++----++++++-+++--++++++-+++-+-+--++++-++---++\||||
|||||  ||||| |  |   ||||| ||||||| |  || || || || |||   || |||\+-+--++-+++--+++-++-+-+++--++++-+++++++----++++++-++/  |||||| ||| | |  |||| ||   |||||||
|||||  ||||| |  |   ||||| |||||\+-+--++-++-++-+/ |||   || ||| \-+--++-+++--+++-++-+-+++--+/|| |||||||  /-++++++-++---++++++-+++-+-+--++++\||   |||||||
|||||  ||||| |  \---+++++-+++++-+-+--/| || || |  |||   || |||   |  || |||  ||| || | |||  | || ||\++++--+-++++++-++---++++++-++/ | |  |||||||   |||||||
|||||  ||||| |      |v||| ||||| | |   | || || |  |||   || |||   |  \+-+++--+++-++-+-++/  | || || ||||/-+-++++++-++---++++++-++--+-+-\|||||||   |||||||
|||||  ||||| |    /-+++++-+++++-+-+---+-++-++-+--+++---++-+++---+---+\|||  ||| || | ||   | || || ||||| | |||\++-++---++++++-++--/ | ||||||||   |||||||
|^|||  ||||| |    | ||||| ||||| | |   | || || |  |||   || |||   |   ||||\--+++-++-+-++---+-++-++-+++++-+-+++-++-++---++/||| ||    | ||||||||   |||||||
|||||  ||||| |    | ||||| ||||| |/+---+-++-++-+--+++---++-+++---+---++++---+++-++-+-++---+-++-++-+++++-+-+++-++-++---++-+++-++----+\||||||||   |||||||
|||||  ||||| |    | ||||| ||||| |||   | || || |  |||   || |||   |   ||||   ||| || | ||   | || || ||||| |/+++-++-++\  || ||| ||    ||||||||||   |||||||
|||||  ||||| |    | ||||| ||||| |||   | || || |  |||   |\-+++---+---++++---+++-/| | ||  /+-++-++-+++++-+++++-++-+++--++-+++\||    ||||||||||   |||||||
|||||  ||||| | /--+-+++++-+++++-+++---+-++-++-+--+++---+--+++---+--\||||   |||  | | ||  || || || ||||| ||||| || |||  || ||||||    ||||||||||   |||||||
|||||  ||||| | |  | ||||| ||||| ||| /-+-++-++-+--+++---+--+++---+--+++++---+++--+-+-++--++-++-++-+++++-+++++-++\|||  || ||||||    ||||||||||   |||||||
|||||  ||||| | |  | ||||| ||||| ||| | | || || |  |||   |  |||   |  |||||   \++--+-+-++--++-++-++-+++++-+++++-++++++--++-++++++----++++++++++---+++/|||
|||||  ||||| | |  | ||||| ||||| ||| | | || || |  |||   |  |||   |  |||||    ||  | | ||  || || || ||||| ||||| ||||||  || ||||||    ||||||||||   ||| |||
|||||  ||||| | |  | ||||| ||||| ||| | | || || |  \++---+--+++---+--+++++----++--+-+-++--++-++-++-+++++-+++++-++++++--++-++/||\----++++++++/|   ||| |||
|||||  ||||| | |  | ||||| ||||| ||| | | || || |   ||   |  |||   |/-+++++----++--+-+-++--++-++-++-+++++-+++++-++++++--++-++-++----\|||||||| |   ||| |||
|||||  ||||| \-+--+-+++++-+++++-+++-+-+-++-++-+---++---+--+++---++-+++++----++--+-+-++--++-++-++-+/||| ||||| ||||||/-++-++-++----+++++++++-+-\ ||| |||
|||||  |||||   |  | ||||| ||||| ||| | | || || |  /++---+--+++\  || |||||    ||  | | ||  || || || | ||| ||||| \++++++-++-++-++----+++++++++-+-+-+++-++/
|||||  \++++---+--+-+++++-++++/ ||| | | || || |/-+++---+-\||||  || |||||    ||  | | ||  || || || | ||| ||\++--++++++-++-++-++----+++++++++-/ | ||| || 
|||||   ||||   |  | ||||| ||||  ||| |/+-++-++-++-+++<--+-+++++--++-+++++----++--+-+-++--++\|| || | ||| || ||  |||||| || || ||    |||||||||   | ||| || 
|||||   ||||   |  | ||||| ||||  ||| ||| || || || |||/<-+-+++++--++\|||||    ||  | | ||  ||||| || | ||| ||/++--++++++-++\|| ||    |||||||||   | ||| || 
|||||   ||||   |  | ||||| ||||  ||| ||| || || || ||||  | |||||  ||||||||    ||  | | ||  ||||\-++-+-+++-+++++--++++++-+++++-++----+++++/|||   | ||| || 
|||||   ||||  /+--+-+++++-++++--+++-+++-++-++-++-++++--+-+++++--++++++++----++--+-+-++--++++--++-+-+++\|||||  |||||| ||||| ||    ||||| |||   | ||| || 
|||||   ||||  ||  | ||||| ||||  ||| ||| || |\-++-++++--+-+++++--++++++++----++--+-+-++--++++--++-+-+++++++++--++++++-+++++-++----+/||| |||   | ||| || 
\++++---++++--++--+-+++++-++++--+++-+++-++-+--++-++++--+-+++++--++++++++----++--/ | ||  ||||  || | |||||||||  |||||| ||||| ||    | ||| |||   | ||| || 
 \+++---++++--++--+-+++/| ||||  ||| ||| |\-+--++-++++--+-+++++--++++++++----++----+-++--++++--++-+-+++++++++--++++++-+++++-++----+-+++-/||   | ||| || 
  |||   ||||  ||  | ||| | |||\--+++-+++-+--+--++-++++--+-+++++--++++++++----++----+-+/  ||||  || | |||||||||  |||||| ||||| ||    | |||  ||   | ||| || 
  |||   \+++--++--+-+++-+-+++---+++-++/ |  |  || ||||/-+-+++++--++++++++----++----+-+---++++--++-+-+++++++++--++++++-+++++-++\   | |||  ||   | ||| || 
  |||    |||  ||  | ||| | |||   ||| ||  |  |  \+-+++++-+-+++++--++++++/|    ||    | |   ||||  || | |||||||||  |||||| ||||| |||   | |||  ||   | ||| || 
  |||    |||  ||  | ||| | |||   ||| ||  |  |   | ||||| | |||||  |||||| |    ||    | |   ||||  || | |||||||||  |||||| ||||| |||   | |||  ||   | ||| || 
  |||    ||\--++--+-+++-+-+++---+++-++--+--+---+-+++++-+-+++++--++++++-+----/|    | |   ||||  ||/+-+++++++++--++++++-+++++-+++---+-+++-\||   | ||| || 
  |||    ||   ||/-+-+++-+-+++---+++-++--+--+---+-+++++-+-+++++--++++++-+-----+----+-+---++++-\|||| |||||||||  |||||| ||||| |||   | ||| |||   | ||| || 
  |||    ||   ||| | ||| \-+++---+++-++--+--+---+-+++++-+-+++++--++++++-+-----+----+-+---++++-++/|| |||||||||  |||||| ||||| |||   | ||| |||   | ||| || 
  |||    ||   ||| | |||   |||   ||| ||  \--+---+-+++++-+-+++++--++++++-+-----+----+-+---++++-++-++-+++++++++--/||||| ||||| |||   | ||| |||   | ||| || 
  |||    ||   ||| | |||   |||   ||| ||     |   | ||||| | |||||  |\++++-+--->-+----+-+---++++-++-++-+++++++++---+++++-+++++-+++---/ ||| |||   | ||| || 
  |||    ||   ||| | |||   |||   ||| |\-----+---+-+++++-+-+++++--+-++++-+-----+----+-+---++/| || || |||||||||/--+++++-+++++-+++-----+++-+++---+-+++\|| 
  |||    ||   ||| | |||   |||   \++-+------+---+-+++++-+-+++++--+-++++-+-----+----+-+---++-+-++-+/ ||||||||||  ||||| ||||| |||     ||| |||   | |||||| 
  |||    ||   ||| | |||   \++----++-+------+---+-+/||| | |||||  | |||| \-----+----+-+---++-+-++-+--++++++++++--+++++-+++++-+++-----+++-+/|   | |||||| 
  |||    \+---+++-+-+++----++----++-+------+---+-+-+++-+-+++++--+-++++-------+----+-+---++-+-++-+--++++++++++--++/|| ||||| |||     ||| | |   | |||||| 
  |||     |   ||| | |||    ||    || |      |   | | ||| | |||||  | ||||       |    | |   || | || \--++++++++++--++-++-+++++-+++-----+++-/ |   | |||||| 
  |||     |   ||\-+-+++----++----++-+------+---+-+-+++-+-+++++--+-++++-------+----+-+---++-+-/|    ||||\+++++--++-++-+++++-+++-----+++---/   | |||||| 
  |||     |   ||  | |||    ||    |\-+------+---+-+-+++-+-+++++--+-++++-------+----+-+---++-+--+----++++-+++++--++-++-+++++-+/|     |||       | |||||| 
  |||   /-+---++--+-+++----++----+--+------+---+-+-+++-+-+++++--+-++++--\    |    | | /-++-+--+----++++-+++++--++-++-+++++-+-+-----+++-------+-++++++\\
  |||   | |   ||  | |||    ||    |  |      |   | | \++-+-+++++--+-++++--+----+----+-+-+-++-+--+----++++-+++++--++-++-+++++-+-+-----+++-------+-+/|||||
  |||   | |   ||  | ||\----++----+--+------+---+-+--++-+-+++++--+-++++--+----+----+-+-+-++-+--+----+/|| |||||  || || |||\+-+-+-----+++-------+-+-+++/|
  |||   | |   ||  | ||     ||    |  |      |   | |  || | |||||  | ||||  |    |    | | | |\-+--+----+-++-+++++--++-++-+++-/ | |     |||       | | ||| |
  |||   | |   |\--+-++-----++----+--+------+---+-+--++-+-+++++--+-+/||  |    |    | | | |  |  |    | || |||||  || || |||   | |     |||       | | ||| |
  |||   | |   |   | ||     ||    |  \------+---+-+--++-+-+++++--+-+-++--+----+----+-+-+-+--+--+----+-++-+++++--/| || |||   | |     |||       | | ||| |
  |||   | |   |   | ||     ||    |         |   | |  || | |||||  | | ||  |    |    | | | |  |  |    | || ||\++---+-++-+/|   | |     |||       | | ||| |
  |||   | \---+---+-++-----+/    |    /----+---+-+--++-+-+++++--+-+-++--+----+----+-+-+-+--+--+----+-++-++-++---+-++-+-+---+-+\    |||       | | ||| |
  |||   |     |   | ||     |/----+----+----+---+-+--++\| |||||  | | \+--+----+----+-/ | |  |  |    | || \+-++---+-/| | |   | ||    |||       | | ||| |
  |||   |     |   | ||     |^    |    |    |   | |  |||| |||||  | |  |  |    |    |   | |  |  |    | ||  \-++---+--+-+-/   | ||    |||       | | ||| |
  |||   |     |   | ||     ||    \----+----+---+-+--++++-+++++--+-+--+--+----+----+---+-+--+--+----+-++----++---+--+-+-----+-++----/||       | | ||| |
  |||   |     |   | \+-----++---------+----+---+-+--++++-++/||  | |  |  |    |    |   | |  |  |    | ||    ||   |  \-+-----+-++-----++-------/ | ||| |
  |||   |     |   |  |     ||         |    |   | |  |||| || ||  | |  |  |    |    |   | |  |  |    | ||    ||   |    |     | ||     ||         | ||| |
  |||   |     |   |  |     \+---------+----+---+-+--++++-++-++--+-+--+--+----+----+---+-+--+--+----+-++----++---+----/     | ||     ||         | ||| |
  |||   |     |   |  |      |         |    |   | |  |||\-++-++--+-+--+--+----+----+---+-+--+--+----/ ||    ||   |          | ||     ||         | ||| |
  |||   |     |   |  |      |         |    |   | \--+++--++-+/  | |  |  |    |    |   | |  |  |      ||    ||   |          | ||     ||         | ||| |
  |||   |     |   |  |      |         |    |   \----+++--/\-+---+-+--+--+----+----+---+-+--+--+------++----++---+----------+-++-----++---------+-++/ |
  |||   |     |   |  |      |    /----+----+--------+++-----+-\ | |  |  |    |    |   | |  |  |      \+----++---+----------+-++-----/|         | ||  |
  |||   |     |   |  |      \----+----+----+--------++/     | | | |  |  |    |    |   | |  |  |       |    ||   |          | ||      |         | ||  |
  |||   |     |   \--+-----------+----+----+--------++------+-+-+-+--/  |    \----+---+-+--+--+-------+----++---+----------+-++------+---------/ ||  |
  |||   |     |      |           |    |    |        |\------+-+-+-+-----+---------+---+-+--+--+-------+----++---+----------+-/|      |           ||  |
  |||   |     |      |           |    |    |        \-------+-+-+-/     |         |   | |  |  \-------+----++---+----------+--+------+-----------/|  |
  |\+---+-----+------+-----------+----+----+----------------+-+-+-------+---------/   | |  |          |    ||   |          |  |      |            |  |
  \-+---+-----+------/           |    |    |                | | |       |             | |  |          |    ||   |          |  |      |            |  |
    |   |     |                  |    |    \----------------+-+-+-------+-------------+-+--+----------+----++---+----------+--+------/            |  |
    |   \-----+------------------+----+---------------------+-+-+-------/             \-+--+----------+----++---+----------+--+-------------------+--/
    |         |                  \----+---------------------+-/ |                       |  \----------+----/|   |          |  |                   |   
    \---------+-----------------------+---------------------/   |                       \-------------+-----+---+----------/  |                   |   
              |                       |                         \-------------------------------------+-----+---/             |                   |   
              \-----------------------+---------------------------------------------------------------/     \-----------------+-------------------/   
                                      \-------------------------------------------------------------------------------------->/                       
'''
