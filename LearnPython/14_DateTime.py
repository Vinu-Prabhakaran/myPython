from datetime import datetime,time,timezone,date

if __name__ == '__main__':
    print(time(11,22,33,123,timezone.utc))
    print(datetime(2026,11,22,12,11,32))
    print(date(2022,11,30))

    # Replace
    my_date = datetime(2020,11,22,1,32,33)
    print(my_date)
    my_date = my_date.replace(month=10) # in place function. So need to reassign inorder to update stored value
    print(my_date)

    # Perform arithmetics
    from_date = date(2021,11,23)
    to_date = date(2023,10,22)
    print(to_date - from_date)