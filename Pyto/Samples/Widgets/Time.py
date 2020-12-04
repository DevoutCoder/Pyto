<<<<<<< HEAD
"""
A widget showing the current time.
"""

import widgets as wd
from datetime import time, date, datetime
=======
import widgets as wd
from datetime import time
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619

BACKGROUND = wd.Color.rgb(255/255, 250/255, 227/255)
FOREGROUND = wd.Color.rgb(75/255, 72/255, 55/255)

<<<<<<< HEAD
class TimeProvider(wd.TimelineProvider):
    
    def widget(self, date):
        widget = wd.Widget()
        
        now = date.time()
        
        hour = wd.Text(
            text=str(now.hour)+"h",
            font=wd.Font("AmericanTypewriter-Bold", 50),
            color=FOREGROUND,
        )
        
        minutes = wd.DynamicDate(
            date=time(now.hour, 0, 0),
            style=wd.DATE_STYLE_RELATIVE,
            font=wd.Font("AmericanTypewriter", 17),
            color=FOREGROUND,
            padding=wd.PADDING_ALL
        )

        layouts = [widget.small_layout, widget.medium_layout]
        for layout in layouts:
            
            layout.add_vertical_spacer()
            layout.add_row([hour])
            layout.add_row([minutes])
            layout.set_background_color(BACKGROUND)
    
        return widget
    
    def timeline(self):
        
        today = date.today()
        dates = []
        for i in range(24):
            now = time(i, 0, 0)
            current_date = datetime.combine(today, now)
            dates.append(current_date)
        
        return dates

wd.provide_timeline(TimeProvider())
=======
widget = wd.Widget()

date = wd.DynamicDate(
    date=time(0, 0, 0),
    style=wd.DATE_STYLE_RELATIVE,
    font=wd.Font("AmericanTypewriter-Bold", 30),
    color=FOREGROUND,
    padding=wd.PADDING_ALL
)

for layout in [
    widget.small_layout,
    widget.medium_layout,
    widget.large_layout]:
    
    layout.add_row([date])
    layout.set_background_color(BACKGROUND)

# Show the widget and reload every hour
# It needs to be reloaded at least once per day, but we don't know when the day will end
wd.schedule_next_reload(60*60)
wd.show_widget(widget)
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
