# import playsound
import threading
import time
#image to ASCII generator : https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/
cake='''

           _..._  ,s$$$s.                                                                                          _..._  ,s$$$s.
         .$$$$$$$s$$ss$$$$,                                                                                     .$$$$$$$s$$ss$$$$,
         $$$sss$$$$s$$$$$$$                                                                                     $$$sss$$$$s$$$$$$$
         $$ss$$$$$$$$$$$$$$                                   (             )                                   $$ss$$$$$$$$$$$$$$
         '$$$s$$$$$$$$$$$$'                           )      (*)           (*)      (                           '$$$s$$$$$$$$$$$$'
          '$$$$$$$$$$$$$$'                           (*)      |             |      (*)                           '$$$$$$$$$$$$$$'
            S$$$$$$$$$$$'                             |      |~|           |~|      |                              S$$$$$$$$$$$'
             '$$$$$$$$$'                             |~|     | |           | |     |~|                              '$$$$$$$$$'
               '$$$$$'                               | |     | |           | |     | |                                '$$$$$'
                '$$$'                               ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.                                '$$$'
                  ;                            .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.                            ;
                 ;                           ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,                         ; 
                 ;                          a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a                        ;
                 ',                         ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';                        ',
                  ;                         ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;                         ;
                 ,'                         ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;                        ,'
                 ;                          ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;                        ;
                 ',                         ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;                        ',
                  ',                        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;                         ',
                   ;                        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;                          ;
                  '                     ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,                      '
                                     .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
                                    .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
                                    %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
                                    %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
                                    `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
                                      `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                          `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                                 """"""""""""""`,,,,,,,,,'"""""""""""""""""
                                                                `%%%%%%%'
                                                                 `%%%%%'
                                                                   %%% 
                                                                  %%%%%
                                                               .,%%%%%%%,.
                                                          ,%%%%%%%%%%%%%%%%%%%,

'''
# Text to ASCII ART GENERATOR link : https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
wish='''                                                                        



  
                                                                                
                                                                          

'''

def task1():
	for letter in cake:
		time.sleep(0.01)
		print(letter, end='')
	for letter in wish:
		time.sleep(0.01)
		print(letter, end='')

def task2():
	playsound('C:\\Users\\alway\\OneDrive\\PROJECTS\\HAPPY BIRTHDAY-3')

t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

# starting threads
t1.start()
t2.start()