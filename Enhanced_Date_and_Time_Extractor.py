#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the 'extract_datetime' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING dateTimeString as parameter.
#
import re
from datetime import datetime

class InvalidDateFormat(Exception):
    pass

class InvalidMonthName(Exception):
    pass

def extract_datetime(dateTimeString):
    month_map = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }

    try:
        # Case 1: YYYY-MM-DD HH:mm:ss
        if re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", dateTimeString):
            try:
                dt = datetime.strptime(dateTimeString, "%Y-%m-%d %H:%M:%S")
            except:
                raise InvalidDateFormat("Invalid date or time values")

        # Case 2: YYYY/MM/DD HH:mm:ss
        elif re.match(r"^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}$", dateTimeString):
            try:
                dt = datetime.strptime(dateTimeString, "%Y/%m/%d %H:%M:%S")
            except:
                raise InvalidDateFormat("Invalid date or time values")

        # Case 3: DD Month YYYY HH:mm:ss
        elif re.match(r"^\d{2} [A-Za-z]+ \d{4} \d{2}:\d{2}:\d{2}$", dateTimeString):
            parts = dateTimeString.split(" ")
            day = int(parts[0])
            month_str = parts[1].lower()
            if month_str not in month_map:
                raise InvalidMonthName("Invalid month name")
            month = month_map[month_str]
            year = int(parts[2])
            hour, minute, second = map(int, parts[3].split(":"))
            try:
                dt = datetime(year, month, day, hour, minute, second)
            except:
                raise InvalidDateFormat("Invalid date or time values")

        else:
            raise InvalidDateFormat("Invalid date and time format")

        return (
            f"Year: {dt.year}, Month: {dt.month}, Day: {dt.day}, "
            f"Hour: {dt.hour}, Minute: {dt.minute}, Second: {dt.second}"
        )

    except InvalidMonthName:
        raise
    except InvalidDateFormat:
        raise
    except Exception:
        raise InvalidDateFormat("Invalid date or time values")

# Driver_code
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    try:
        dateTimeString = input()
        result = extract_datetime(dateTimeString)
        fptr.write(result)
    except InvalidDateFormat as e:
        fptr.write(str(e))
    except InvalidMonthName as e:
        fptr.write(str(e))

    fptr.close()
