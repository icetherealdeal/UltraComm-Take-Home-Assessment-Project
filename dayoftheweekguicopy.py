#dayoftheweekgui.py
#By: Isaac Nguyen
#May 8, 2023
#This is a take home project assessment from UltraComm

from graphics import *
import calendar

'''Create a GUI that can take in a specific date and output what day of the week that was.
For example, for the date 01/29/1988, the output of the program should be Friday.
'''

def main():
    '''Setting up the graphics window
'''
    width = 640
    height = 480
    win = GraphWin("Day of the Week GUI", width, height)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("orange")

    title = Text(Point(5, 9.5), "DAY OF THE WEEK CALCULATOR")
    title.setStyle("bold")
    title.setSize(35)
    title.draw(win)
    
    input_box = Entry(Point(5,7.75), 10)
    input_box.draw(win)
    input_box_message = Text(Point(5, 8.25), "Enter a date in the following format (mm/dd/yyyy)")
    input_box_message.setSize(14)
    input_box_message.draw(win)
    
    button = Rectangle(Point(4, 4), Point(6, 3))
    button.setFill("lightblue")
    button.setOutline("white")
    button.draw(win)
    button_text = Text(Point(5, 3.5), "Calculate")
    button_text.setSize(18)
    button_text.draw(win)
    button_prompt = Text(Point(5, 4.25), "Click the button to calculate")
    button_prompt.setSize(14)
    button_prompt.draw(win)

    result_message = Text(Point(5, 6), "Pick out any date you want")
    result_message.setStyle("bold")
    result_message.setFill("white")
    result_message.setSize(18)
    result_message.draw(win)
    
    description1 = Text(Point(5, 1), "This app takes a specific date & outputs what day of the week it was")
    description1.draw(win)
    description2 = Text(Point(5, 0.5), "Ex. for the date 01/29/1988, the output of the program should be Friday")
    description2.draw(win)

    if win.getMouse(): #Pause for user to click in window
        terminate_message = Text(Point(5, 2.5), "Press the 'q' key to exit and close the window")
        terminate_message.setStyle("bold")
        terminate_message.setFill("red")
        terminate_message.setSize(26)
        terminate_message.draw(win)

        button.setFill("lightgreen")


    date = input_box.getText()
    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:])

    #Take the last two digits of the year.
    year_last_two = int(date[8:])
    
    #Add to that one–quarter of those two digits (discard any remainder)
    #Add to that the day of the month and the Month Key number for that month
    '''MONTH KEY: Jan=1 (LY=0), Feb=4 (LY=3), Mar=4, Apr=0, May=2, Jun=5, Jul=0
Aug=3, Sep=6, Oct=1, Nov=4, Dec=6
'''
    if month < 1 or month > 12:
        result_message.setText("Invalid month value. Must be between 1 & 12. Try again")
    
    #no leap year
    if not calendar.isleap(year):
        month_key_dic = {1:1, 2:4, 3:4, 4:0, 5:2, 6:5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6}
        total_sum = year_last_two + int(0.25*year_last_two) + day +  month_key_dic[month]
    #leap year
    else:
        month_key_dic = {1:0, 2:3, 3:4, 4:0, 5:2, 6:5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6}
        total_sum = year_last_two + int(0.25*year_last_two) + day +  month_key_dic[month]

    #EDGE CASES
    #If you’re searching for a week prior to 1900, add 2 to the sum before dividing; prior to 1800, add 4.
    if year < 1800:
        total_sum = total_sum + 4

    elif year < 1900:
        total_sum = total_sum +  2
    
    #From 2000 to 2099, subtract 1 from the sum before dividing.
    elif 2000 <= year <= 2099:
        total_sum = total_sum - 1
    
    #Divide the sum by 7. The remainder is the day of the week!
    day_of_the_week = total_sum%7
    
    #One is Sunday, two is Monday, and so on. If there is no remainder, the day is Saturday.    
    if day_of_the_week == 1:
        result_message.setText("The day is Sunday")

    elif day_of_the_week == 2:
        result_message.setText("The day is Monday")

    elif day_of_the_week == 3:
        result_message.setText("The day is Tuesday")

    elif day_of_the_week == 4:
        result_message.setText("The day is Wednesday" )

    elif day_of_the_week == 5:
        result_message.setText("The day is Thursday")

    elif day_of_the_week == 6:
        result_message.setText("The day is Friday")

    elif day_of_the_week == 0 :
        result_message.setText("The day is Saturday")

    #For non-leap years
    if not calendar.isleap(year):
        if month == 2:
            if day == 29:
                result_message.setText("This is a leap year. February only has 28 days. Try again")

    #The formula doesn’t work for days prior to 1753.
    if year < 1753:
        result_message.setText("Any year before 1753 does not work with the formula. Try again")
        result_message.setFill("blue")
        result_message.setSize(15)
        
    win.getKey()
    win.close()

main()
