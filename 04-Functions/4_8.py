def time_string(hours, minutes, time_format):
    apm='am'
    hour=''
    minut=''
    if time_format == "24":
        hour=hours
        minut=minutes
        return (f'{hour:02d}:{minut:02d}')
    else:
        if hours< 12 and hours >=0:
            hour=hours
            minut=minutes
            return (f'{hour:02d}:{minut:02d} {apm}')
        elif hours==12:
            hour=hours
            minut=minutes
            apm='pm'
            return (f'{hour:02d}:{minut:02d} {apm}')
        else:
            hour=hours-12
            minut=minutes
            apm='pm'
            return (f'{hour:02d}:{minut:02d} {apm}')
print(time_string(12,4,'12'))