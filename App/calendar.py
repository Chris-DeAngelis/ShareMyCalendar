import streamlit as st
import pandas as pd
import numpy as np
#from icalendar import Calendar #, Event, vCalAddress, vText
from datetime import datetime, timedelta

############## Page Setup ##############
st.set_page_config(
    page_title='Share My Calendar',
    page_icon=':bar_chart:', #"👋",
    #initial_sidebar_state="expanded",
    layout='wide',
    menu_items={
        #'Get Help': 'http://spauldingridge.com',
        #'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': '# Built by Chris DeAngelis, CFA | cdeangelis@spauldingridge.com'
    }
)

############## App Introduction ##############
st.header('Share Your Calendar Time Blocks to Facilitate Scheduling')
st.write('Load your calendar and generate a screenshot of your availability. Your calendar data is never stored or shared and is cleared upon exiting Streamlit.')
with st.expander("Instructions", expanded=False):
    st.write(
        """
        1. Open Outlook and go to settings
        2. Instruction #2
        3. ...
        4. ...
        """)
st.divider()
# Create a double-ended datetime slider
# start_date = datetime.now()
# end_date = start_date + timedelta(days=365)
# st.write('Filter Calendar Dates')
# selected_date_range = st.slider(
#     'Select a Date Range',
#     min_value=start_date,
#     max_value=end_date,
#     value=(start_date, start_date + timedelta(days=28)),
#     step=timedelta(days=1),
# )

# ############## Upload a Calendar File ##############
# calendar_file = None
# calendar_file = st.file_uploader('Upload an .ics File from Outlook', accept_multiple_files=False)

# ############## Build Functions ##############
# def parse_calendar(file_path):
#     with open(file_path, 'rb') as file:
#         cal = Calendar.from_ical(file.read())
#     return cal

# def get_events(calendar):
#     events = []
#     for component in calendar.walk():
#         if component.name == "VEVENT":
#             start = component.get('dtstart').dt
#             end = component.get('dtend').dt

#             # Convert to datetime if it's a date
#             if isinstance(start, datetime):
#                 start = start.replace(tzinfo=pytz.UTC)
#             else:
#                 start = datetime.combine(start, datetime.min.time()).replace(tzinfo=pytz.UTC)

#             if isinstance(end, datetime):
#                 end = end.replace(tzinfo=pytz.UTC)
#             else:
#                 end = datetime.combine(end, datetime.max.time()).replace(tzinfo=pytz.UTC)

#             events.append((start, end))
#     return sorted(events)

# def analyze_schedule(events, start_date, end_date):
#     current = start_date
#     free_times = []
#     busy_times = []

#     for event_start, event_end in events:
#         if current < event_start:
#             free_times.append((current, event_start))
#         busy_times.append((max(current, event_start), event_end))
#         current = max(current, event_end)

#     if current < end_date:
#         free_times.append((current, end_date))

#     return free_times, busy_times

# def format_time_range(start, end):
#     return f"{start.strftime('%Y-%m-%d %H:%M')} to {end.strftime('%Y-%m-%d %H:%M')}"

# def main():
#     calendar = parse_calendar('reachcalendar.ics')
#     events = get_events(calendar)

#     # Analyze schedule for the next 7 days
#     start_date = datetime.now(pytz.UTC).replace(hour=0, minute=0, second=0, microsecond=0)
#     end_date = start_date + timedelta(days=7)

#     free_times, busy_times = analyze_schedule(events, start_date, end_date)

#     print("Free times:")
#     for start, end in free_times:
#         print(format_time_range(start, end))

#     print("\nBusy times:")
#     for start, end in busy_times:
#         print(format_time_range(start, end))

# if __name__ == "__main__":
#     main()

# def create_calendar(year, month):
#     # Create a calendar for the specified month
#     cal = calendar.monthcalendar(year, month)
    
#     # Create a Streamlit container for the calendar
#     cal_container = st.container()
    
#     with cal_container:
#         # Display month and year
#         st.header(f"{calendar.month_name[month]} {year}")
        
#         # Create 7 columns for the days of the week
#         cols = st.columns(7)
#         for i, day in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
#             cols[i].write(day)
        
#         # Display the calendar
#         for week in cal:
#             cols = st.columns(7)
#             for i, day in enumerate(week):
#                 if day != 0:
#                     date = datetime(year, month, day)
#                     if date in available_dates:
#                         cols[i].markdown(f"<div style='background-color: #90EE90; padding: 10px; border-radius: 5px;'>{day}</div>", unsafe_allow_html=True)
#                     elif date in busy_dates:
#                         cols[i].markdown(f"<div style='background-color: #FFA07A; padding: 10px; border-radius: 5px;'>{day}</div>", unsafe_allow_html=True)
#                     else:
#                         cols[i].markdown(f"<div style='background-color: #F0F0F0; padding: 10px; border-radius: 5px;'>{day}</div>", unsafe_allow_html=True)
#                 else:
#                     cols[i].write("")

# ############## Show Calendar ##############
# # Streamlit app
# st.title("Calendar View")

# # Get current year and month
# if calendar_file != None:
#   create_calendar(start_date.year, start_date.month)
# else:
#   st.write('Please Upload a Calendar files (.ics) to get started')

# # Display legend
# st.write('Calendar Legend:')
# st.markdown("<div style='background-color: #90EE90; padding: 5px; border-radius: 5px;'>Available</div>", unsafe_allow_html=True)
# st.markdown("<div style='background-color: #FFA07A; padding: 5px; border-radius: 5px;'>Busy</div>", unsafe_allow_html=True)
# st.markdown("<div style='background-color: #F0F0F0; padding: 5px; border-radius: 5px;'>No Data</div>", unsafe_allow_html=True)
