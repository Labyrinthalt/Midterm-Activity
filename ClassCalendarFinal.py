class calendar:
    def __init__(self, year):
        self.events = {}

    def is_leap_year(self, year):
        if year % 4 == 0:
            return True
        else:
            return False

    def get_days_in_month(self, month, year):
        match month:
            case 1:
                return 31
            case 2:
                if self.is_leap_year(year):
                    return 29
                else:
                    return 28
            case 3:
                return 31
            case 4:
                return 30
            case 5:
                return 31
            case 6:
                return 30
            case 7:
                return 31
            case 8:
                return 31
            case 9:
                return 30
            case 10:
                return 31
            case 11:
                return 30
            case 12:
                return 31
            case _:
                return -1 

    def get_month_name(self, month):
        match month:
            case 1:  
                return "January"
            case 2:  
                return "February"
            case 3:  
                return "March"
            case 4:  
                return "April"
            case 5:  
                return "May"
            case 6:  
                return "June"
            case 7:  
                return "July"
            case 8:  
                return "August"
            case 9:  
                return "September"
            case 10: 
                return "October"
            case 11: 
                return "November"
            case 12: 
                return "December"
            case _:  
                return "unknown"

    def is_valid_date(self, day, month, year):
        if year < 2026 or year > 2028:
            print(" [ERROR] year must be between 2026 and 2028")
            return False

        if month < 1 or month > 12:
            print(" [ERROR] month must be between 1 and 12")
            return False

        max_day = self.get_days_in_month(month, year)
        if day < 1 or day > max_day:
            print(f" [ERROR] day must be between 1 and {max_day} for {self.get_month_name(month)} {year}!")
            return False

        return True

    def add_event(self, day, month, year, event_name):
        if self.is_valid_date(day, month, year):
            date_key = f"{year}-{month}-{day}"
            
            if date_key not in self.events:
                self.events[date_key] = []
            
            self.events[date_key].append(event_name)
            print(f"\n[SUCCESS] Event '{event_name}' Added on {self.get_month_name(month)} {day}, {year}!")

    def view_events_on_date(self, day, month, year):
        if self.is_valid_date(day, month, year):
            date_key = f"{year}-{month}-{day}"
            
            if date_key in self.events:
                print(f"\n--- Events on {self.get_month_name(month)} {day}, {year} ---")
                for event in self.events[date_key]:
                    print(f"- {event}")
            else:
                print(f"\n[INFO] No events found for this date.")

    def view_all_events(self):
        if not self.events:
            print("\n[INFO] The calendar is currently empty.")
        else:
            print("\n--- ALL SCHEDULED EVENTS ---")
            for date in self.events:
                for event in self.events[date]:
                    print(f"{date}: {event}")

    def delete_event(self, day, month, year):
        date_key = f"{year}-{month}-{day}"
        if date_key in self.events:
            del self.events[date_key]
            print(f"\n[SUCCESS] All events on {date_key} have been deleted.")
        else:
            print(f"\n[ERROR] No events found on that date to delete.")

my_cal = calendar(2026)

while True:
    print("\n---- MAIN MENU ----")
    print("1. Add an Event")
    print("2. View Events on a Date")
    print("3. View All Events")
    print("4. Delete an Event")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\n--- ADD AN EVENT ---")
        y = int(input("Year (2026-2028): "))
        m = int(input("Month (1-12): "))
        d = int(input("Day: "))
        name = input("Enter event name: ")
        my_cal.add_event(d, m, y, name)

    elif choice == "2":
        print("\n--- VIEW EVENTS ON A DATE ---")
        y = int(input("Year: "))
        m = int(input("Month: "))
        d = int(input("Day: "))
        my_cal.view_events_on_date(d, m, y)

    elif choice == "3":
        my_cal.view_all_events()

    elif choice == "4":
        print("\n--- DELETE AN EVENT ---")
        y = int(input("Year: "))
        m = int(input("Month: "))
        d = int(input("Day: "))
        my_cal.delete_event(d, m, y)

    elif choice == "5":
        print("Exiting calendar...")
        print("i always come back...")
        break
        
    else:
        print("Invalid choice. Please try again.")