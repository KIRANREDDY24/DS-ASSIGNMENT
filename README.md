# DS-ASSIGNMENT

                                                   Problem Statement


We are sharing data for our live demo classes right from parents showing interest in their conversion (Parent bought the live classes pack).


Following are the details of the data:
       1.Interested Users – Users (child) who have shown interest in joining the demo classes.
       2.Booked Users – Users who booked a trail class on our portal. There are cases where duplicate trails are possible, count both.
       3.Trainers – Trainers assigned to Trail Batch.
       4.Subscription Bought – Details of Sales that are made. Use only those cases where sale value is greater than equal to 499/-.


Using these data, create following metrics:
       1.Sales conversion with respect to Trainers
       2.Sales conversion with respect to Time slot
       3.Sales conversion with respect to Topic
       4.Sales conversion with respect to Source (Field available in Interested Users)
       5.Sales conversion wrt grade
       6.Time taken for Sales conversion
       7.Time slot – attendance %


Sales conversion refers to the number of users who have bought the session after showing interest and attending the trial session.




                                                      solution


1)
its clear from the problem statement that we need to consider the users who have brought the subsription for rupess 499 or grater.
so the python script @greater499.ipynb , sorts the users who have brought the subscription for rupess 499 or grater from the csv file named Subscription Bought.
we get 270 users(greater499.csv) . im considering phone number(register id) as key(pivot or whatever phrase you are good with) and mapping all the remaining data to the key. but 3 of them dont have phone number, with the help email-id i extracted 2 of the phone numbers from the csv file(Booked Users). one field have no phone numeber and email-id and no other information from which we can extract the phone number. even with the help of grade(IV) we cannot extract the phone or email-id, because there are so many users who are studying in grade IV.


2)
from the line "Sales conversion refers to the number of users who have bought the session after showing interest and attending the trial session", we can infer that we need to consider the user who have interrested, booked and brought the live demo class.

so we have to take all the common users from the three csv files(Interested Users, Booked Users, Subscription Bought(rupess >= 499) ). this extraction process can be done with help of phone number. after this process i got 67 users(interested, booked and brought(>=499)).in this 67(interested booked and brought.csv) users there are some repeated entries. after removing the duplicate entries we get 59 unique users.( unique59.ipynb )

now after merging the data from the all three files we get (total.csv) file.
3) now we are left with trainers and topics. we can get them by merging total.csv and trainer.csv
and the last one is source we get it from the interested users(using phone number)

4)
so we made the excel sheet containing(phone number, email-id,trainer,topic,grade,trail ,time slot, date, attendance, source)

with help of the final csv file(extreme.csv) we answer all the questions in the problem statement.



                                                         answers





1.

#N/A     --> 1            
FAC_5002 --> 2            
FAC_5003 --> 2              
FAC_5006 --> 1             
FAC_5008 --> 5                
FAC_5009 --> 6                
FAC_5011 --> 1                   
FAC_5012 --> 1                    
FAC_5013 --> 1                      
FAC_5015 --> 4                        
FAC_5016 --> 1                           
FAC_5017 --> 1                          
FAC_5019 --> 2                           
FAC_5020 --> 1                            
FAC_5022 --> 4                             
FAC_5024 --> 2                               
FAC_5025 --> 2                              
FAC_5026 --> 1                              
FAC_5027 --> 3                             
FAC_5028 --> 1                              
FAC_5029 --> 3                             
FAC_5031 --> 5                      
FAC_5036 --> 1                   
FAC_5038 --> 1                          
FAC_5039 --> 3                            
FAC_5044 --> 1                              
FAC_5046 --> 1                         
FAC_5052 --> 2                  
                                                      
                                                     

2.

11:15 am --->  9            
11:45 am --->  14        
4:00 pm  --->  10         
6:00 pm  --->  16          
6:15 pm  --->  10           



3.

'Category Spin'              --->4                       
'In my head or real?'        --->6                          
'Structure of a story'       --->2                        
'Word Whiz'                  --->11                              
'Spelling Star'              --->1                        
'Play with Punctuations'     --->4                      
'Sum it up'                  --->2                       
'Rocking with Rhymes'        --->5                   
'Name it'                    --->10                 
'Making Connections'         --->6             
"In my mind's eye"           --->8                  


4.




'lastchance'     --->1                     
'TEB2ASMS'       --->1                         
'ntfpush'        --->7                      
'T1KRMSMS'       --->6                      
'rfmsms'         --->12                     
'TEB11SMS'       --->3                      
'TEB3SMS'        --->7                       
'ntfuiuser'      --->2                         
'TEB12SMS'       --->1                           
'TEB4SMS'        --->4                         
'TEB5SMS'        --->8                     
'b1rmsms'        --->3                       
'b2rmsms'        --->2                     
'adarsh'         --->1                     
'b3rmsms'        --->1                


5.



'Grade 1'        --->9            
'Grade 2'        --->17                
'Grade 3'        --->14              
'Grade 4'        --->19             


6.


i have written script to extract sales conversion it took less than 3 minutes to extract the data.


7.

'Present',   ---> 53     ---> 90% (approx)                           
''           --->  2     ---> 3.3% (approx)          
'Absent'     --->  3     ---> 5% (approx)           
'Cancelled'  --->  1     ---> 1.7%  (approx)                 

